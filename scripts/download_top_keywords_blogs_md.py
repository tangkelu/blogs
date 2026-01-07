#!/usr/bin/env python3
"""
Download blog/article pages referenced by Excel files under `top_blog_keywords/`
and save them as formatted Markdown (with YAML frontmatter) under:

  /data/top_keywords_blog/<site>/

Images referenced in the extracted main content are downloaded and rewritten to
local relative paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

import pandas as pd
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger("download_top_keywords_blogs_md")


BLOG_URL_PATTERNS = re.compile(
    r"/(blog|blogs|news|article|articles|insights|post|resource|resources|learn|knowledge|guides|guide|whitepaper|case-study|case-studies)/",
    re.IGNORECASE,
)

NON_ARTICLE_PATH_PATTERNS = re.compile(
    r"/(tag|tags|category|categories|author|authors|search|page)/",
    re.IGNORECASE,
)

TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "igshid",
    "_ga",
    "ref",
    "source",
}

TRACKING_QUERY_PREFIXES = ("utm_",)


def _slugify(value: str, max_len: int = 80) -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = value.replace("/", "-")
    value = re.sub(r"[^a-z0-9\\-_.]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-._")
    if not value:
        return "item"
    return value[:max_len].rstrip("-._")


def _site_from_url(url: str) -> str:
    netloc = urlsplit(url).netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def _normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        return url
    parts = urlsplit(url)
    if not parts.scheme:
        url = "https://" + url
        parts = urlsplit(url)

    query_pairs = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        k_lower = k.lower()
        if k_lower in TRACKING_QUERY_KEYS:
            continue
        if any(k_lower.startswith(p) for p in TRACKING_QUERY_PREFIXES):
            continue
        query_pairs.append((k, v))

    new_query = urlencode(query_pairs, doseq=True)
    normalized = urlunsplit((parts.scheme, parts.netloc.lower(), parts.path, new_query, ""))
    return normalized.rstrip()


def _looks_like_article(url: str) -> bool:
    try:
        parts = urlsplit(url)
    except Exception:
        return False
    if parts.scheme not in ("http", "https"):
        return False
    if not parts.netloc:
        return False
    path = parts.path or "/"
    path_lower = path.lower()

    if path_lower.endswith((".pdf", ".zip", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".mp4")):
        return False
    if NON_ARTICLE_PATH_PATTERNS.search(path_lower):
        return False
    if not BLOG_URL_PATTERNS.search(path_lower):
        return False

    # Filter obvious listing pages.
    if path_lower.rstrip("/") in (
        "/blog",
        "/blogs",
        "/news",
        "/article",
        "/articles",
        "/insights",
        "/resources",
        "/resource",
        "/learn",
        "/knowledge",
        "/guides",
        "/guide",
    ):
        return False

    # Must have some depth beyond the section itself.
    segments = [s for s in path.split("/") if s]
    return len(segments) >= 2


def _create_session() -> requests.Session:
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.6,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        }
    )
    return session


def _parse_srcset(srcset: str) -> Optional[str]:
    candidates: list[tuple[int, str]] = []
    for part in (srcset or "").split(","):
        item = part.strip()
        if not item:
            continue
        bits = item.split()
        url = bits[0]
        width = 0
        if len(bits) > 1:
            m = re.match(r"^(\\d+)(w|x)$", bits[1].strip())
            if m:
                width = int(m.group(1))
        candidates.append((width, url))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def _best_img_src(img_tag) -> Optional[str]:
    for key in ("src", "data-src", "data-original", "data-lazy-src", "data-url"):
        v = img_tag.get(key)
        if v and isinstance(v, str) and v.strip():
            if v.strip().startswith("data:"):
                continue
            return v.strip()
    srcset = img_tag.get("srcset")
    if isinstance(srcset, str) and srcset.strip():
        best = _parse_srcset(srcset.strip())
        if best and not best.startswith("data:"):
            return best
    return None


def _extract_title(soup: BeautifulSoup) -> str:
    for sel in [
        ('meta', {"property": "og:title"}),
        ('meta', {"name": "twitter:title"}),
    ]:
        tag = soup.find(sel[0], attrs=sel[1])
        if tag and tag.get("content"):
            return str(tag["content"]).strip()
    h1 = soup.find("h1")
    if h1:
        t = h1.get_text(" ", strip=True)
        if t:
            return t
    title_tag = soup.find("title")
    if title_tag:
        t = title_tag.get_text(" ", strip=True)
        if t:
            return t
    return "Untitled"


def _extract_description(soup: BeautifulSoup) -> str:
    for sel in [
        ('meta', {"name": "description"}),
        ('meta', {"property": "og:description"}),
        ('meta', {"name": "twitter:description"}),
    ]:
        tag = soup.find(sel[0], attrs=sel[1])
        if tag and tag.get("content"):
            return str(tag["content"]).strip()
    return ""

def _extract_og_image(soup: BeautifulSoup) -> str:
    for sel in [
        ('meta', {"property": "og:image"}),
        ('meta', {"name": "twitter:image"}),
        ('meta', {"property": "twitter:image"}),
    ]:
        tag = soup.find(sel[0], attrs=sel[1])
        if tag and tag.get("content"):
            return str(tag["content"]).strip()
    return ""


def _extract_published_date(soup: BeautifulSoup) -> Optional[str]:
    for sel in [
        ('meta', {"property": "article:published_time"}),
        ('meta', {"name": "pubdate"}),
        ('meta', {"name": "publishdate"}),
        ('meta', {"name": "timestamp"}),
        ('meta', {"itemprop": "datePublished"}),
    ]:
        tag = soup.find(sel[0], attrs=sel[1])
        if tag and tag.get("content"):
            raw = str(tag["content"]).strip()
            dt = _parse_date(raw)
            if dt:
                return dt

    time_tag = soup.find("time")
    if time_tag:
        raw = time_tag.get("datetime") or time_tag.get_text(" ", strip=True)
        if raw:
            dt = _parse_date(str(raw).strip())
            if dt:
                return dt
    return None


def _parse_date(value: str) -> Optional[str]:
    value = value.strip()
    if not value:
        return None
    # Common ISO formats.
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f%z"):
        try:
            dt = datetime.strptime(value, fmt)
            return dt.strftime("%Y-%m-%d")
        except Exception:
            continue
    # Fallback: pick YYYY-MM-DD anywhere.
    m = re.search(r"(20\\d{2})[-/](\\d{1,2})[-/](\\d{1,2})", value)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        try:
            return datetime(y, mo, d).strftime("%Y-%m-%d")
        except Exception:
            return None
    return None


def _clean_soup(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(["script", "style", "nav", "footer", "header", "form", "noscript", "svg"]):
        tag.decompose()
    to_remove = []
    for tag in soup.find_all(True):
        attrs = getattr(tag, "attrs", None)
        if attrs is None:
            continue
        classes = attrs.get("class") or []
        klass = " ".join(classes).lower() if isinstance(classes, list) else str(classes).lower()
        ident = str(attrs.get("id") or "").lower()
        blob = f"{klass} {ident}"
        if any(
            key in blob
            for key in (
                "cookie",
                "breadcrumb",
                "subscribe",
                "newsletter",
                "popup",
                "modal",
                "share",
                "social",
                "related",
                "recommend",
                "comment",
                "advert",
                "ads",
                "promo",
                "sidebar",
                "nav",
            )
        ):
            to_remove.append(tag)
    for tag in to_remove:
        tag.decompose()


def _link_density(elem) -> float:
    text = elem.get_text(" ", strip=True)
    if not text:
        return 0.0
    link_text = " ".join(a.get_text(" ", strip=True) for a in elem.find_all("a"))
    return min(1.0, len(link_text) / max(1, len(text)))


def _score_container(elem) -> float:
    text = elem.get_text(" ", strip=True)
    text_len = len(text)
    if text_len < 200:
        return 0.0
    p_count = len(elem.find_all("p"))
    img_count = len(elem.find_all("img"))
    density = _link_density(elem)
    return text_len + 120 * min(p_count, 30) + 80 * min(img_count, 20) - 1200 * density


def _pick_main_container(soup: BeautifulSoup):
    selectors = [
        "article",
        "main",
        '[role="main"]',
        '[itemprop="articleBody"]',
        '.article-body',
        ".post-content",
        ".article-content",
        ".entry-content",
        ".content",
        "#content",
        "#main",
    ]
    candidates = []
    for sel in selectors:
        for el in soup.select(sel):
            candidates.append(el)
    # Also consider big div/section blocks.
    candidates.extend(soup.find_all(["div", "section"], limit=200))
    best = None
    best_score = 0.0
    for el in candidates:
        score = _score_container(el)
        if score > best_score:
            best = el
            best_score = score
    if best is not None:
        return best
    return soup.body or soup

def _absolutize_links(container, page_url: str) -> None:
    for a in container.find_all("a", href=True):
        href = (a.get("href") or "").strip()
        if not href:
            continue
        if href.startswith("#") or href.lower().startswith("javascript:"):
            continue
        if href.lower().startswith(("mailto:", "tel:")):
            continue
        a["href"] = urljoin(page_url, href)


def _absolutize_images(container, page_url: str) -> None:
    for img in container.find_all("img"):
        src = _best_img_src(img)
        if not src:
            continue
        abs_src = urljoin(page_url, src)
        img["src"] = abs_src
        for k in ("srcset", "data-srcset"):
            if img.has_attr(k):
                del img[k]


def _extract_article_text_from_json_ld(soup: BeautifulSoup) -> str:
    parts: list[str] = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.get_text(strip=True)
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue
        queue = data if isinstance(data, list) else [data]
        while queue:
            item = queue.pop(0)
            if isinstance(item, dict):
                if "articleBody" in item and isinstance(item["articleBody"], str):
                    parts.append(item["articleBody"].strip())
                for v in item.values():
                    if isinstance(v, (dict, list)):
                        queue.append(v)
            elif isinstance(item, list):
                queue.extend(item)
    text = "\n\n".join(p for p in parts if p)
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def _estimate_reading_time_minutes(text: str) -> int:
    text = text.strip()
    if not text:
        return 1
    words = len(re.findall(r"[A-Za-z0-9]+", text))
    cjk = len(re.findall(r"[\\u4e00-\\u9fff]", text))
    minutes_words = words / 220 if words else 0
    minutes_cjk = cjk / 500 if cjk else 0
    minutes = max(minutes_words, minutes_cjk, len(text) / 1200)
    return max(1, int(minutes + 0.999))


def _yaml_escape(value: str) -> str:
    value = (value or "").strip().replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\\s+", " ", value).strip()
    value = value.replace('"', "'")
    return value


@dataclass(frozen=True)
class ArticleJob:
    url: str
    site: str
    tags: tuple[str, ...]


class BlogMarkdownDownloader:
    def __init__(
        self,
        output_dir: Path,
        *,
        download_images: bool,
        overwrite: bool,
        polite_delay_s: float,
        max_images_per_article: int,
    ) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.download_images = download_images
        self.overwrite = overwrite
        self.polite_delay_s = polite_delay_s
        self.max_images_per_article = max_images_per_article
        self._local = threading.local()
        self._manifest_lock = threading.Lock()
        self._completed_lock = threading.Lock()
        self.manifest_path = self.output_dir / "_manifest.jsonl"
        self.completed_urls = self._load_completed_urls()

    def _get_session(self) -> requests.Session:
        sess = getattr(self._local, "session", None)
        if sess is None:
            sess = _create_session()
            self._local.session = sess
        return sess

    def _load_completed_urls(self) -> set[str]:
        completed: set[str] = set()
        if not self.manifest_path.exists():
            return completed
        try:
            with self.manifest_path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    url = rec.get("url")
                    ok = rec.get("ok")
                    if ok and isinstance(url, str):
                        completed.add(url)
        except Exception as e:
            logger.warning(f"Failed to read manifest {self.manifest_path}: {e}")
        return completed

    def _append_manifest(self, rec: dict) -> None:
        rec = dict(rec)
        rec["ts"] = datetime.now().isoformat(timespec="seconds")
        with self._manifest_lock:
            with self.manifest_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def _fetch_html(self, url: str) -> Optional[str]:
        try:
            resp = self._get_session().get(url, timeout=25)
        except Exception as e:
            self._append_manifest({"url": url, "ok": False, "error": f"request:{type(e).__name__}"})
            return None
        if resp.status_code != 200:
            self._append_manifest({"url": url, "ok": False, "error": f"status:{resp.status_code}"})
            return None
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text

    def _download_image(self, image_url: str, target_path: Path) -> bool:
        try:
            resp = self._get_session().get(image_url, timeout=25, stream=True)
        except Exception:
            return False
        if resp.status_code != 200:
            return False
        content_type = (resp.headers.get("content-type") or "").lower()
        if not content_type.startswith("image/"):
            return False

        target_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(target_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=65536):
                    if chunk:
                        f.write(chunk)
        except Exception:
            return False
        return True

    def _guess_image_ext(self, image_url: str, content_type: str = "") -> str:
        path = urlsplit(image_url).path.lower()
        m = re.search(r"\\.(jpg|jpeg|png|webp|gif|bmp|tiff|svg)$", path)
        if m:
            ext = m.group(1)
            return ".jpg" if ext == "jpeg" else f".{ext}"
        if content_type.startswith("image/"):
            subtype = content_type.split("/", 1)[1].split(";")[0].strip()
            subtype = subtype.replace("jpeg", "jpg")
            if subtype:
                return f".{subtype}"
        return ".jpg"

    def _rewrite_and_download_images(
        self,
        container,
        *,
        page_url: str,
        assets_fs_dir: Path,
        assets_md_dir: str,
    ) -> tuple[list[str], list[str]]:
        downloaded_local_paths: list[str] = []
        failed_sources: list[str] = []

        img_tags = container.find_all("img")
        if self.max_images_per_article > 0:
            img_tags = img_tags[: self.max_images_per_article]

        for idx, img in enumerate(img_tags, start=1):
            src = _best_img_src(img)
            if not src:
                continue
            abs_src = urljoin(page_url, src)

            # Determine target filename (stable-ish).
            base = f"img_{idx:03}"
            ext = self._guess_image_ext(abs_src)
            target_rel = f"{assets_md_dir}/{base}{ext}"
            target_path = assets_fs_dir / f"{base}{ext}"

            ok = True
            if not target_path.exists() or self.overwrite:
                ok = self._download_image(abs_src, target_path)

            if ok:
                downloaded_local_paths.append(target_rel)
                img["src"] = target_rel
                for k in ("srcset", "data-srcset"):
                    if img.has_attr(k):
                        del img[k]
            else:
                failed_sources.append(abs_src)
                img["src"] = abs_src
                for k in ("srcset", "data-srcset"):
                    if img.has_attr(k):
                        del img[k]

        return downloaded_local_paths, failed_sources

    def _html_container_to_markdown(self, container) -> str:
        html = str(container)
        md = html_to_md(html, heading_style="ATX")
        md = md.replace("\r\n", "\n").replace("\r", "\n")
        md = re.sub(r"\n{3,}", "\n\n", md).strip()
        return md

    def _output_paths_for_url(self, site: str, url: str) -> tuple[Path, str, Path, str]:
        url_parts = urlsplit(url)
        last = url_parts.path.rstrip("/").split("/")[-1] or "index"
        slug = _slugify(last)
        url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
        if len(slug) < 6:
            slug = f"{slug}-{url_hash}"
        md_filename = f"{slug}.md"

        site_dir = self.output_dir / site
        md_path = site_dir / md_filename
        assets_fs_dir = site_dir / "_assets" / slug
        assets_md_dir = f"_assets/{slug}"
        return md_path, slug, assets_fs_dir, assets_md_dir

    def download_one(self, job: ArticleJob) -> dict:
        url = job.url
        if url in self.completed_urls and not self.overwrite:
            return {"url": url, "ok": True, "skipped": True}

        try:
            md_path, _, assets_fs_dir, assets_md_dir = self._output_paths_for_url(job.site, url)
            md_path.parent.mkdir(parents=True, exist_ok=True)

            if md_path.exists() and not self.overwrite and url not in self.completed_urls:
                return {"url": url, "ok": True, "skipped": True, "reason": "exists"}

            html = self._fetch_html(url)
            if not html:
                return {"url": url, "ok": False}

            soup = BeautifulSoup(html, "lxml")
            _clean_soup(soup)
            title = _extract_title(soup)
            description = _extract_description(soup)
            date = _extract_published_date(soup) or datetime.now().strftime("%Y-%m-%d")
            og_image = _extract_og_image(soup)

            container = _pick_main_container(soup)
            _absolutize_links(container, url)
            if self.download_images:
                downloaded_imgs, failed_imgs = self._rewrite_and_download_images(
                    container,
                    page_url=url,
                    assets_fs_dir=assets_fs_dir,
                    assets_md_dir=assets_md_dir,
                )
            else:
                downloaded_imgs, failed_imgs = [], []
                _absolutize_images(container, url)

            md_body = self._html_container_to_markdown(container)
            if not md_body or len(re.sub(r"\\s+", "", md_body)) < 200:
                ld_text = _extract_article_text_from_json_ld(soup)
                if ld_text:
                    md_body = ld_text
            if not md_body:
                self._append_manifest({"url": url, "ok": False, "error": "empty_markdown"})
                return {"url": url, "ok": False}

            # Drop a leading H1 if it duplicates the title.
            md_lines = md_body.splitlines()
            if md_lines and md_lines[0].startswith("# "):
                first_h1 = md_lines[0][2:].strip()
                if first_h1 and first_h1.lower() == title.strip().lower():
                    md_body = "\n".join(md_lines[1:]).lstrip()

            if not description:
                first_para = next(
                    (ln.strip() for ln in md_body.splitlines() if ln.strip() and not ln.strip().startswith("#")),
                    "",
                )
                description = first_para[:180]

            reading_time = _estimate_reading_time_minutes(md_body)
            image_field = downloaded_imgs[0] if downloaded_imgs else (og_image or "")
            tags = [job.site]
            for t in job.tags:
                if t and t not in tags:
                    tags.append(t)
                if len(tags) >= 8:
                    break

            fm = (
                "---\n"
                f'title: "{_yaml_escape(title)}"\n'
                f'description: "{_yaml_escape(description)}"\n'
                "category: technology\n"
                f'date: "{date}"\n'
                "featured: false\n"
                f'image: "{image_field}"\n'
                f"readingTime: {reading_time}\n"
                "tags: ["
                + ", ".join(f'"{_yaml_escape(t)}"' for t in tags)
                + "]\n"
                "---\n\n"
            )

            footer = f"\n\n---\n\n**Source:** {url}\n"
            if failed_imgs:
                footer += "\n\n**Failed images:**\n" + "\n".join(f"- {u}" for u in failed_imgs) + "\n"

            content = fm + md_body.strip() + footer
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)

            rec = {
                "url": url,
                "ok": True,
                "site": job.site,
                "md": str(md_path),
                "images": len(downloaded_imgs),
                "failed_images": len(failed_imgs),
            }
            self._append_manifest(rec)
            with self._completed_lock:
                self.completed_urls.add(url)

            if self.polite_delay_s > 0:
                time.sleep(self.polite_delay_s)

            return rec
        except Exception as e:
            self._append_manifest({"url": url, "ok": False, "error": f"exception:{type(e).__name__}"})
            return {"url": url, "ok": False, "error": str(e)}


def _collect_jobs_from_excels(
    excel_dir: Path,
    *,
    max_position: Optional[int],
    max_urls_per_site: Optional[int],
) -> list[ArticleJob]:
    excel_files = sorted(excel_dir.glob("*.xlsx"))
    if not excel_files:
        raise SystemExit(f"No .xlsx files found under {excel_dir}")

    url_to_keywords: dict[str, list[str]] = {}
    url_to_site: dict[str, str] = {}
    url_best_rank: dict[str, float] = {}

    for excel_path in excel_files:
        try:
            df = pd.read_excel(excel_path)
        except Exception as e:
            logger.warning(f"Skip unreadable excel {excel_path}: {e}")
            continue
        if "URL" not in df.columns:
            continue
        if "Position" not in df.columns:
            df["Position"] = 999999
        if "Keyword" not in df.columns:
            df["Keyword"] = ""

        df = df.dropna(subset=["URL"]).copy()
        df["URL"] = df["URL"].astype(str).map(_normalize_url)
        df = df[df["URL"].map(_looks_like_article)]
        if max_position is not None:
            pos = pd.to_numeric(df["Position"], errors="coerce").fillna(999999)
            df = df[pos.astype(int) <= int(max_position)]

        # Prefer better ranks first.
        df = df.sort_values(by=["Position"], ascending=True)

        for _, row in df.iterrows():
            url = str(row["URL"]).strip()
            if not url:
                continue
            site = _site_from_url(url)
            url_to_site[url] = site
            try:
                rank = float(row.get("Position") or 999999)
            except Exception:
                rank = 999999.0
            url_best_rank[url] = min(url_best_rank.get(url, 999999.0), rank)
            kw = str(row.get("Keyword") or "").strip()
            if kw:
                url_to_keywords.setdefault(url, [])
                if kw not in url_to_keywords[url]:
                    url_to_keywords[url].append(kw)

    # Cap per-site if requested.
    site_to_urls: dict[str, list[str]] = {}
    site_to_seen: dict[str, set[str]] = {}
    for url, site in url_to_site.items():
        seen = site_to_seen.setdefault(site, set())
        if url in seen:
            continue
        seen.add(url)
        site_to_urls.setdefault(site, []).append(url)

    jobs: list[ArticleJob] = []
    for site, urls in sorted(site_to_urls.items(), key=lambda x: x[0]):
        urls_sorted = sorted(urls, key=lambda u: (url_best_rank.get(u, 999999.0), u))
        if max_urls_per_site is not None:
            urls_sorted = urls_sorted[: int(max_urls_per_site)]
        for url in urls_sorted:
            kws = tuple(url_to_keywords.get(url, [])[:10])
            jobs.append(ArticleJob(url=url, site=site, tags=kws))
    return jobs


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--excel-dir", default="top_blog_keywords", help="Directory containing .xlsx files")
    parser.add_argument("--output-dir", default="/data/top_keywords_blog", help="Output base directory")
    parser.add_argument("--max-position", type=int, default=10, help="Only keep rows with Position <= N")
    parser.add_argument("--all-positions", action="store_true", help="Ignore Position filter")
    parser.add_argument("--max-urls-per-site", type=int, default=0, help="Optional cap per site (0 = no cap)")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent article workers")
    parser.add_argument("--polite-delay", type=float, default=0.0, help="Sleep seconds after each saved article")
    parser.add_argument("--max-images", type=int, default=30, help="Max images to download per article")
    parser.add_argument("--no-images", action="store_true", help="Do not download images; keep absolute image URLs")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing markdown/images")
    parser.add_argument("--dry-run", action="store_true", help="Only print planned counts")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    excel_dir = Path(args.excel_dir)
    output_dir = Path(args.output_dir)
    max_position: Optional[int] = None if args.all_positions else int(args.max_position)
    max_urls_per_site: Optional[int] = None if int(args.max_urls_per_site) <= 0 else int(args.max_urls_per_site)

    jobs = _collect_jobs_from_excels(excel_dir, max_position=max_position, max_urls_per_site=max_urls_per_site)
    by_site: dict[str, int] = {}
    for j in jobs:
        by_site[j.site] = by_site.get(j.site, 0) + 1

    logger.info(f"Planned sites: {len(by_site)}")
    logger.info(f"Planned articles: {len(jobs)}")
    for site, n in sorted(by_site.items(), key=lambda x: (-x[1], x[0]))[:10]:
        logger.info(f"Top site: {site} -> {n}")

    if args.dry_run:
        return 0

    downloader = BlogMarkdownDownloader(
        output_dir,
        download_images=not bool(args.no_images),
        overwrite=bool(args.overwrite),
        polite_delay_s=float(args.polite_delay),
        max_images_per_article=int(args.max_images),
    )

    ok = 0
    skipped = 0
    failed = 0
    start = time.time()

    workers = max(1, int(args.workers))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(downloader.download_one, job) for job in jobs]
        for fut in as_completed(futures):
            try:
                rec = fut.result()
            except Exception as e:
                failed += 1
                logger.warning(f"✗ future exception: {type(e).__name__}: {e}")
                continue
            if rec.get("ok"):
                if rec.get("skipped"):
                    skipped += 1
                else:
                    ok += 1
                    logger.info(f"✓ {rec.get('site')} {rec.get('url')} (images={rec.get('images')})")
            else:
                failed += 1
                logger.warning(f"✗ {rec.get('url')}")

    elapsed = time.time() - start
    logger.info(f"Done: ok={ok} skipped={skipped} failed={failed} elapsed={elapsed:.1f}s")
    logger.info(f"Output: {output_dir}")
    logger.info(f"Manifest: {downloader.manifest_path}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
