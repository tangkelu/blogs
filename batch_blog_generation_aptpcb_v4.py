#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 4 APTPCB demo blogs (query/pillar/playbook/story) with optional RAG context.
This script reuses core logic from batch_blog_generation_openai.py, but adds a
--use-rag flag to inject retrieved snippets from a local embedding index.
"""

import argparse
import json
import os
import random
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests

try:
    import numpy as np
except Exception:  # pragma: no cover - optional dependency
    np = None


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR))
import batch_blog_generation_openai as gen  # noqa: E402


DEFAULT_PROMPTS_DIR = Path("/code/blogs/prompts_aptpcb/blogs_prompt_v5")
DEFAULT_BASE_TEMPLATES_DIR = DEFAULT_PROMPTS_DIR / "_base_templates_v3"
DEFAULT_OUTPUT_BASE_DIR = Path("/code/blogs/blogs_aptpcb_v4")
DEFAULT_SITEMAP_FILE = Path("/code/hileap/frontendAPT/public/sitemap.xml")
DEFAULT_INTERNAL_LINK_POOL = Path("/code/blogs/prompts_aptpcb/internal_link_pool.md")
DEFAULT_ASSETS_IMAGE_CATALOG = Path("/code/hileap/frontendAPT/docs/assets-img-filenames.md")
DEFAULT_MODULES_DIR = DEFAULT_PROMPTS_DIR / "_modules_v1"

DEFAULT_RAG_INDEX = Path("/data/top_keywords_blog/rag_index.jsonl")
DEFAULT_EMBED_BASE_URL = os.getenv("RAG_EMBED_BASE_URL", "http://192.168.50.27:11434/v1")
DEFAULT_EMBED_MODEL = os.getenv("RAG_EMBED_MODEL", "nomic-embed-text")
DEFAULT_EMBED_API_KEY = os.getenv("RAG_EMBED_API_KEY", "ollama")


def _load_api_defaults() -> Tuple[str, str, str]:
    """
    Default to the same API settings as batch_blog_generation_openai.py.
    Allow overriding via env vars (GEN_API_*).
    """
    base_url = os.getenv("GEN_API_BASE_URL", getattr(gen, "GEMINI_API_URL", "https://max.openai365.top/v1"))
    api_key = os.getenv("GEN_API_KEY", getattr(gen, "API_KEY", ""))
    model = os.getenv("GEN_MODEL", getattr(gen, "MODEL", "[满血Pro] gemini-3-pro-preview-maxthinking"))
    return base_url, api_key, model


def parse_args() -> argparse.Namespace:
    base_url, api_key, model = _load_api_defaults()
    parser = argparse.ArgumentParser(description="Generate 4 demo blogs with optional RAG context.")
    parser.add_argument("--prompts-dir", default=str(DEFAULT_PROMPTS_DIR))
    parser.add_argument("--base-templates-dir", default=str(DEFAULT_BASE_TEMPLATES_DIR))
    parser.add_argument("--output-base-dir", default=str(DEFAULT_OUTPUT_BASE_DIR))
    parser.add_argument("--sitemap-file", default=str(DEFAULT_SITEMAP_FILE))
    parser.add_argument("--internal-link-pool", default=str(DEFAULT_INTERNAL_LINK_POOL))
    parser.add_argument("--assets-image-catalog", default=str(DEFAULT_ASSETS_IMAGE_CATALOG))
    parser.add_argument("--modules-dir", default=str(DEFAULT_MODULES_DIR))
    parser.add_argument("--output-lang", choices=["cn", "en", "auto"], default="en")
    parser.add_argument("--image-policy", choices=["auto", "llm", "none"], default="auto")
    parser.add_argument("--max-generation-attempts", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--strict-template", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--compact-prompt", action=argparse.BooleanOptionalAction, default=False)

    parser.add_argument("--api-base-url", default=base_url)
    parser.add_argument("--api-key", default=api_key)
    parser.add_argument("--model", default=model)

    parser.add_argument("--use-rag", action="store_true", help="Inject retrieved context into the prompt.")
    parser.add_argument("--rag-index", default=str(DEFAULT_RAG_INDEX))
    parser.add_argument("--rag-top-k", type=int, default=20)
    parser.add_argument("--rag-max-chunks", type=int, default=10)
    parser.add_argument("--rag-max-chars", type=int, default=3200)
    parser.add_argument("--rag-min-score", type=float, default=0.2)
    parser.add_argument("--rag-per-source", type=int, default=2)
    parser.add_argument("--rag-embed-base-url", default=DEFAULT_EMBED_BASE_URL)
    parser.add_argument("--rag-embed-api-key", default=DEFAULT_EMBED_API_KEY)
    parser.add_argument("--rag-embed-model", default=DEFAULT_EMBED_MODEL)
    return parser.parse_args()


def load_keywords(path: Path) -> Dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _keyword_tokens(text: str) -> set:
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    stop = {
        "the", "and", "or", "for", "of", "to", "in", "on", "with", "without",
        "a", "an", "vs", "how", "what", "when", "why", "guide", "checklist",
        "best", "practices", "rules", "design", "manufacturing", "assembly",
        "pcb", "pcba",
    }
    return {t for t in tokens if t not in stop and len(t) > 1}


def _similarity(a: str, b: str) -> float:
    ta = _keyword_tokens(a)
    tb = _keyword_tokens(b)
    if not ta or not tb:
        return 0.0
    inter = len(ta & tb)
    union = len(ta | tb)
    return inter / union if union else 0.0


def _pick_lsi(main_keyword: Dict, keywords_data: Dict) -> List[str]:
    subsection = main_keyword.get("subsection")
    if not subsection:
        return []
    candidates = [
        kw for sub in keywords_data.get("subsections", [])
        if sub.get("name") == subsection
        for kw in sub.get("keywords", [])
        if kw.get("keyword") != main_keyword.get("keyword")
    ]
    scored = [(kw, _similarity(main_keyword["keyword"], kw["keyword"])) for kw in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    picked = []
    for kw, score in scored:
        if len(picked) >= 5:
            break
        if score <= 0 and len(picked) >= 2:
            continue
        picked.append(kw["keyword"])
    return picked


def _collect_categories(prompts_dir: Path) -> List[Path]:
    categories = []
    for path in prompts_dir.iterdir():
        if path.is_dir() and (path / "keywords.json").exists():
            categories.append(path)
    categories.sort()
    return categories


def _select_keyword_for_template(
    categories: List[Path],
    intent: Optional[str],
    used_keywords: set,
) -> Tuple[Optional[Path], Optional[Dict], Optional[Dict]]:
    category_pool = categories[:]
    random.shuffle(category_pool)
    for category_dir in category_pool:
        keywords_data = load_keywords(category_dir / "keywords.json")
        candidates = []
        for subsection in keywords_data.get("subsections", []):
            for kw in subsection.get("keywords", []):
                kw["subsection"] = subsection.get("name")
                if kw.get("keyword") in used_keywords:
                    continue
                if intent and kw.get("intent") != intent:
                    continue
                candidates.append(kw)
        if not candidates and intent:
            for subsection in keywords_data.get("subsections", []):
                for kw in subsection.get("keywords", []):
                    kw["subsection"] = subsection.get("name")
                    if kw.get("keyword") in used_keywords:
                        continue
                    candidates.append(kw)
        if candidates:
            return category_dir, random.choice(candidates), keywords_data
    return None, None, None


class RagIndex:
    def __init__(self, path: Path):
        self.path = path
        self.records: List[Dict] = []
        self.vectors = None
        self.norms = None

    def load(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f"RAG index not found: {self.path}")
        records = []
        vectors = []
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                records.append(
                    {
                        "path": row.get("path", ""),
                        "url": row.get("url", ""),
                        "title": row.get("title", ""),
                        "text": row.get("text", ""),
                        "embedding": row.get("embedding", []),
                    }
                )
                vectors.append(row.get("embedding", []))
        if np is not None:
            self.vectors = np.asarray(vectors, dtype="float32")
            self.norms = np.linalg.norm(self.vectors, axis=1) + 1e-12
        else:
            self.vectors = vectors
            self.norms = None
        self.records = records

    def search(
        self,
        query_vec: List[float],
        *,
        top_k: int,
        min_score: float,
        per_source: int,
        max_chunks: int,
    ) -> List[Dict]:
        if not self.records:
            return []
        if np is not None and isinstance(self.vectors, np.ndarray):
            q = np.asarray(query_vec, dtype="float32")
            q_norm = np.linalg.norm(q) + 1e-12
            scores = (self.vectors @ q) / (self.norms * q_norm)
            idx = np.argsort(-scores)
            ranked = [(int(i), float(scores[int(i)])) for i in idx[: top_k * 4]]
        else:
            q_norm = sum(x * x for x in query_vec) ** 0.5 + 1e-12
            ranked = []
            for i, v in enumerate(self.vectors):
                if not v:
                    continue
                dot = sum(a * b for a, b in zip(query_vec, v))
                v_norm = sum(x * x for x in v) ** 0.5 + 1e-12
                ranked.append((i, dot / (v_norm * q_norm)))
            ranked.sort(key=lambda x: x[1], reverse=True)
            ranked = ranked[: top_k * 4]

        picked = []
        per_path = {}
        for i, score in ranked:
            if score < min_score:
                continue
            rec = self.records[i]
            path = rec.get("path") or ""
            per_path[path] = per_path.get(path, 0) + 1
            if per_path[path] > per_source:
                continue
            rec = dict(rec)
            rec["score"] = score
            picked.append(rec)
            if len(picked) >= max_chunks:
                break
        return picked


def _embed_query(
    query: str,
    *,
    base_url: str,
    api_key: str,
    model: str,
    timeout_seconds: int = 60,
) -> List[float]:
    endpoint = f"{base_url.rstrip('/')}/embeddings"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model, "input": [query]}
    resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout_seconds)
    if resp.status_code >= 400:
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        raise RuntimeError(f"Embeddings request failed ({resp.status_code}): {detail}")
    data = resp.json()
    items = data.get("data", [])
    if not items:
        raise RuntimeError(f"Embeddings response missing data: {data}")
    return items[0]["embedding"]


def _build_rag_block(chunks: List[Dict], *, max_chars: int) -> str:
    if not chunks:
        return ""
    lines = [
        "\n\n[Retrieved context for reference only. Do NOT output this block.]",
        "Use these snippets as factual grounding; paraphrase and do not copy verbatim.",
    ]
    total = 0
    for i, rec in enumerate(chunks, 1):
        title = rec.get("title") or "Untitled"
        url = rec.get("url") or rec.get("path") or ""
        text = rec.get("text", "").strip()
        entry = f"[{i}] {title} ({url})\n{text}"
        if total + len(entry) > max_chars:
            break
        lines.append(entry)
        total += len(entry)
    return "\n\n".join(lines).strip()


def _build_prompt(
    *,
    template_file: Path,
    keyword: str,
    lsi_keywords: List[str],
    internal_pool_text: str,
    assets_pool_text: str,
    modules_text: str,
    use_compact: bool,
) -> Tuple[str, str]:
    raw = template_file.read_text(encoding="utf-8")
    filled = gen.fill_template_variables(raw, keyword, lsi_keywords)
    template_kind = gen._detect_v3_template_kind(filled)
    if template_kind == "unknown":
        template_kind = gen._detect_v2_template_kind(filled)

    if use_compact:
        v3_kind = gen._detect_v3_template_kind(filled)
        v2_kind = gen._detect_v2_template_kind(filled) if v3_kind == "unknown" else "unknown"
        if v3_kind != "unknown" and v3_kind != "story":
            filled = gen._compact_v3_prompt(
                kind=v3_kind,
                keyword=keyword,
                lsi_keywords=lsi_keywords,
                internal_link_pool=internal_pool_text,
                assets_image_pool=assets_pool_text,
                modules_text=modules_text,
            )
        elif v2_kind != "unknown" and v2_kind != "story":
            filled = gen._compact_v2_prompt(
                kind=v2_kind,
                keyword=keyword,
                lsi_keywords=lsi_keywords,
                internal_link_pool=internal_pool_text,
                assets_image_pool=assets_pool_text,
                modules_text=modules_text,
            )
        else:
            if "{{internal_link_pool}}" in filled:
                filled = filled.replace("{{internal_link_pool}}", internal_pool_text or "")
            if "{{assets_image_pool}}" in filled:
                filled = filled.replace("{{assets_image_pool}}", assets_pool_text or "")
            if modules_text:
                filled = gen._inject_modules(filled, modules_text)
    else:
        if "{{internal_link_pool}}" in filled:
            filled = filled.replace("{{internal_link_pool}}", internal_pool_text or "")
        if "{{assets_image_pool}}" in filled:
            filled = filled.replace("{{assets_image_pool}}", assets_pool_text or "")
        if modules_text:
            filled = gen._inject_modules(filled, modules_text)

    if (
        "### 字数要求" not in filled
        and "总字数" not in filled
        and "Word count target" not in filled
    ):
        filled += "\n\n### 字数要求\n- 总字数：2800-3500词（依主题复杂度调整）\n"

    return filled, template_kind


def _resolve_template_file(base_dir: Path, kind: str) -> Path:
    name = f"aptpcb-{kind}.md"
    path = base_dir / name
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {path}")
    return path


def _generate_one(
    *,
    template_kind: str,
    template_file: Path,
    keyword: str,
    lsi_keywords: List[str],
    rag_index: Optional[RagIndex],
    args: argparse.Namespace,
    assets_pool_paths: List[str],
) -> Optional[Path]:
    internal_pool_text = ""
    if args.internal_link_pool and Path(args.internal_link_pool).exists():
        internal_pool_text = gen._load_internal_link_pool_text(Path(args.internal_link_pool))

    assets_pool_text = ""
    if args.assets_image_catalog and Path(args.assets_image_catalog).exists():
        catalog_paths = gen.load_assets_image_catalog_paths(Path(args.assets_image_catalog))
        pool = gen.select_assets_image_pool(
            catalog_paths=catalog_paths,
            keyword=keyword,
            lsi_keywords=lsi_keywords,
            pool_size=gen.ASSETS_IMAGE_POOL_SIZE,
        )
        assets_pool_paths[:] = list(pool or [])
        assets_pool_text = gen.format_assets_image_pool_text(pool or [])

    modules_text = ""
    if template_kind != "story":
        modules = gen._infer_modules(keyword, lsi_keywords)
        modules_text = gen._load_modules_text(modules, keyword=keyword, lsi_keywords=lsi_keywords)

    prompt, kind_detected = _build_prompt(
        template_file=template_file,
        keyword=keyword,
        lsi_keywords=lsi_keywords,
        internal_pool_text=internal_pool_text,
        assets_pool_text=assets_pool_text,
        modules_text=modules_text,
        use_compact=bool(args.compact_prompt),
    )
    prompt_base = prompt

    if args.use_rag and rag_index is not None:
        query_text = f"{keyword}. Related: {', '.join(lsi_keywords)}"
        query_vec = _embed_query(
            query_text,
            base_url=args.rag_embed_base_url,
            api_key=args.rag_embed_api_key,
            model=args.rag_embed_model,
        )
        chunks = rag_index.search(
            query_vec,
            top_k=args.rag_top_k,
            min_score=args.rag_min_score,
            per_source=args.rag_per_source,
            max_chunks=args.rag_max_chunks,
        )
        rag_block = _build_rag_block(chunks, max_chars=args.rag_max_chars)
        if rag_block:
            prompt = prompt + "\n\n" + rag_block

    if args.dry_run:
        print("🧪 DRY RUN: skip generation")
        print(f"🧩 Template: {template_file.name}")
        print(f"🔑 Keyword: {keyword}")
        print(f"🔗 LSI: {', '.join(lsi_keywords)}")
        print(f"📏 Prompt chars: {len(prompt)}")
        return None

    print(f"🤖 Using {gen.MODEL} for {template_kind}...")
    blog_content = gen.generate_blog_with_gemini(prompt, max_retries=1)
    if not blog_content:
        print("❌ Generation failed")
        return None

    blog_content = gen.post_process_content(blog_content)
    language = gen.detect_language(blog_content)
    kind_hint = kind_detected if kind_detected != "unknown" else gen._infer_article_kind_from_content(blog_content)

    # Basic normalization (no local content injection).
    blog_content = gen.fix_malformed_conclusion_heading(blog_content)
    blog_content = gen.repair_truncated_key_takeaways(blog_content)
    blog_content = gen.ensure_blog_quick_quote_marker(blog_content, kind_hint=kind_hint)
    if kind_hint == "story":
        blog_content = gen.strip_story_key_takeaways(blog_content, kind_hint=kind_hint)
        blog_content = gen.fix_story_context_heading(blog_content, kind_hint=kind_hint)
        blog_content = gen.rebuild_contents_toc(blog_content, kind_hint=kind_hint)
    else:
        blog_content = gen.ensure_contents_toc(blog_content, kind_hint=kind_hint)

    if args.strict_template:
        required_patterns = gen._required_section_patterns_from_prompt(prompt_base)
        missing_sections = gen._missing_required_sections(blog_content, required_patterns)
        if missing_sections:
            print(f"⚠️ Missing required sections (no retry): {', '.join(missing_sections)}")

    base_slug = gen.generate_base_slug({"keyword": keyword}, template_file.stem, lsi_keywords)
    unique_slug = gen.ensure_unique_slug(
        base_slug,
        keyword=keyword,
        lsi_keywords=lsi_keywords,
        kind=kind_hint,
    )

    blog_content = gen.build_front_matter(
        blog_content,
        keyword,
        template_file.stem,
        lsi_keywords,
        unique_slug,
        original_keyword=keyword,
    )
    blog_content = gen.normalize_h1_to_front_matter_title(blog_content, fallback_title=keyword)
    if gen.IMAGE_POLICY == "auto":
        hero_path = assets_pool_paths[0] if assets_pool_paths else ""
        blog_content = gen.ensure_hero_image(blog_content, hero_path)
    elif gen.IMAGE_POLICY == "llm":
        blog_content = gen.ensure_hero_image(blog_content, "")

    kind = kind_hint if kind_hint != "unknown" else gen._infer_article_kind_from_content(blog_content)
    blog_content = gen.ensure_opening_paragraph(blog_content, keyword=keyword, kind=kind)
    blog_content = gen.ensure_highlights(blog_content, keyword=keyword, kind=kind)
    blog_content = gen.ensure_front_matter_description(blog_content, keyword=keyword)
    blog_content = gen.ensure_title_case_and_headings(blog_content, language=language)
    blog_content = gen.ensure_playbook_section_tables(blog_content, keyword=keyword)
    blog_content = gen.normalize_h1_to_front_matter_title(blog_content, fallback_title=keyword)
    blog_content = gen.ensure_blog_quick_quote_marker(blog_content, kind_hint=kind)
    blog_content = gen.fix_toc_leaked_into_key_takeaways(blog_content)
    if kind == "story":
        blog_content = gen.strip_story_key_takeaways(blog_content, kind_hint=kind)
        blog_content = gen.fix_story_context_heading(blog_content, kind_hint=kind)
        blog_content = gen.rebuild_contents_toc(blog_content, kind_hint=kind)
    else:
        blog_content = gen.ensure_contents_toc(blog_content, kind_hint=kind)

    filename = gen.generate_filename_from_slug(unique_slug)
    lang_dir = args.output_lang
    if lang_dir == "auto":
        lang_dir = "cn" if language == "中文" else "en"
    file_path = gen.save_blog_to_file(blog_content, filename, lang_dir=lang_dir)
    print(f"✅ Saved: {file_path}")
    return file_path


def main() -> None:
    args = parse_args()
    random.seed(42)

    gen.PROMPTS_DIR = Path(args.prompts_dir)
    gen.OUTPUT_BASE_DIR = Path(args.output_base_dir)
    gen.SITEMAP_FILE = Path(args.sitemap_file)
    gen.OUTPUT_LANG_MODE = args.output_lang
    gen.BASE_TEMPLATES_DIR = Path(args.base_templates_dir)
    gen.INTERNAL_LINK_POOL_FILE = Path(args.internal_link_pool)
    gen.MODULES_DIR = Path(args.modules_dir)
    gen.ASSETS_IMAGE_CATALOG_FILE = Path(args.assets_image_catalog)
    gen.IMAGE_POLICY = args.image_policy
    gen.MAX_GENERATION_ATTEMPTS = int(args.max_generation_attempts or 3)

    gen.API_KEY = args.api_key
    gen.GEMINI_API_URL = args.api_base_url
    gen.MODEL = args.model

    sitemap_slugs = gen.load_sitemap_slugs(gen.SITEMAP_FILE)
    local_slugs = gen.load_local_blog_slugs(gen.OUTPUT_BASE_DIR)
    gen.USED_SLUGS = set(sitemap_slugs) | set(local_slugs)

    rag_index = None
    if args.use_rag:
        rag_index = RagIndex(Path(args.rag_index))
        rag_index.load()

    categories = _collect_categories(Path(args.prompts_dir))
    if not categories:
        raise SystemExit(f"No categories found in {args.prompts_dir}")

    template_kinds = ["query", "pillar", "playbook", "story"]
    intent_map = {"query": "query", "pillar": "pillar", "playbook": "playbook", "story": None}
    used_keywords = set()
    outputs = []

    print("=" * 80)
    print("APTPCB v4 demo generation (4 templates)")
    print("=" * 80)
    print(f"Prompts dir: {args.prompts_dir}")
    print(f"Base templates: {args.base_templates_dir}")
    print(f"Output dir: {args.output_base_dir}")
    print(f"Use RAG: {args.use_rag}")
    print(f"Compact prompt: {args.compact_prompt}")
    if args.use_rag:
        print(f"RAG index: {args.rag_index}")
        print(f"RAG embed base: {args.rag_embed_base_url}")
        print(f"RAG model: {args.rag_embed_model}")
    print("=" * 80)

    for kind in template_kinds:
        category_dir, main_kw, keywords_data = _select_keyword_for_template(
            categories,
            intent_map.get(kind),
            used_keywords,
        )
        if not main_kw:
            print(f"⚠️ No keyword found for template {kind}")
            continue
        used_keywords.add(main_kw["keyword"])
        lsi = _pick_lsi(main_kw, keywords_data or {})
        template_file = _resolve_template_file(Path(args.base_templates_dir), kind)
        assets_pool_paths: List[str] = []
        path = _generate_one(
            template_kind=kind,
            template_file=template_file,
            keyword=main_kw["keyword"],
            lsi_keywords=lsi,
            rag_index=rag_index,
            args=args,
            assets_pool_paths=assets_pool_paths,
        )
        if path:
            outputs.append(path)

    print("=" * 80)
    if outputs:
        print("Generated demo files:")
        for p in outputs:
            print(f"- {p}")
    else:
        print("No files generated.")
    print("=" * 80)


if __name__ == "__main__":
    main()
