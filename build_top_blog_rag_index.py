#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a lightweight RAG index (embeddings) from local top-ranked blog markdown files.
The output is a JSONL file where each line is:
{ "id": "...", "path": "...", "url": "...", "text": "...", "embedding": [...] }
"""

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import requests


DEFAULT_SOURCE_DIR = Path("/data/top_keywords_blog")
DEFAULT_OUTPUT = Path("/data/top_keywords_blog/rag_index.jsonl")
DEFAULT_EMBED_MODEL = os.getenv("BLOG_EMBED_MODEL", "text-embedding-3-small")
DEFAULT_API_BASE_URL = os.getenv("BLOG_API_BASE_URL", "https://www.chataiapi.com/v1")
DEFAULT_API_KEY = os.getenv("BLOG_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")

EXCLUDE_DIRS = {"deep_read", "deep_read_v2", "_assets", ".git", "__pycache__"}
EXCLUDE_FILES = {"SEO_INSIGHTS.md", "_deleted_unused_md.txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a local RAG index from markdown files.")
    parser.add_argument("--source-dir", default=str(DEFAULT_SOURCE_DIR), help="Root dir with markdown files.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSONL index path.")
    parser.add_argument("--manifest", default=None, help="Optional manifest jsonl for URL mapping.")
    parser.add_argument("--api-base-url", default=DEFAULT_API_BASE_URL, help="OpenAI-compatible base URL.")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="API key (or set BLOG_API_KEY).")
    parser.add_argument("--embed-model", default=DEFAULT_EMBED_MODEL, help="Embedding model name.")
    parser.add_argument("--max-files", type=int, default=None, help="Process at most N files.")
    parser.add_argument("--max-chunks-per-file", type=int, default=None, help="Cap chunks per file.")
    parser.add_argument("--start-index", type=int, default=None, help="Start index within the file list.")
    parser.add_argument("--end-index", type=int, default=None, help="End index (exclusive) within the file list.")
    parser.add_argument("--append", action="store_true", help="Append to output instead of overwriting.")
    parser.add_argument("--skip-existing", action="store_true", help="Skip files already present in output JSONL.")
    parser.add_argument("--max-words", type=int, default=320, help="Max words per chunk.")
    parser.add_argument("--max-chars", type=int, default=2000, help="Max characters per chunk.")
    parser.add_argument("--overlap-paragraphs", type=int, default=1, help="Paragraph overlap between chunks.")
    parser.add_argument("--batch-size", type=int, default=8, help="Embedding batch size.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Sleep seconds between batches.")
    parser.add_argument("--dry-run", action="store_true", help="Scan and show counts without embedding.")
    return parser.parse_args()


def _strip_front_matter(text: str) -> str:
    if not text:
        return ""
    if text.lstrip().startswith("---"):
        markers = list(re.finditer(r"^---\s*$", text, flags=re.MULTILINE))
        if len(markers) >= 2 and markers[0].start() < 5:
            return text[markers[1].end() :].strip()
    return text


def _extract_title(text: str) -> str:
    m = re.search(r"(?m)^\s*#\s+(.+?)\s*$", text or "")
    return m.group(1).strip() if m else ""


def _split_paragraphs(text: str) -> List[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text or "") if p.strip()]
    cleaned = []
    for p in paragraphs:
        if re.match(r"^\s*!\[", p) or re.match(r"^\s*<img\b", p):
            continue
        if len(p) < 20 and not re.match(r"^\s*#+\s+", p):
            continue
        cleaned.append(p)
    return cleaned


def _split_long_paragraph(paragraph: str, max_words: int, max_chars: int) -> List[str]:
    words = paragraph.split()
    if len(words) <= max_words and len(paragraph) <= max_chars:
        return [paragraph]
    out = []
    if len(words) > max_words:
        for i in range(0, len(words), max_words):
            chunk = " ".join(words[i : i + max_words])
            if len(chunk) <= max_chars:
                out.append(chunk)
            else:
                for j in range(0, len(chunk), max_chars):
                    out.append(chunk[j : j + max_chars])
        return out
    # Fallback: very long strings without whitespace.
    for i in range(0, len(paragraph), max_chars):
        out.append(paragraph[i : i + max_chars])
    return out


def _normalize_paragraphs(paragraphs: List[str], max_words: int, max_chars: int) -> List[str]:
    out: List[str] = []
    for p in paragraphs:
        out.extend(_split_long_paragraph(p, max_words, max_chars))
    return out


def _chunk_paragraphs(paragraphs: List[str], max_words: int, overlap_paragraphs: int, max_chars: int) -> List[str]:
    chunks: List[str] = []
    current: List[str] = []
    current_words = 0
    current_chars = 0
    for p in paragraphs:
        words = len(p.split())
        if current and (current_words + words > max_words or current_chars + len(p) > max_chars):
            chunks.append("\n\n".join(current).strip())
            if overlap_paragraphs > 0:
                current = current[-overlap_paragraphs:]
                current_words = sum(len(c.split()) for c in current)
                current_chars = sum(len(c) for c in current)
            else:
                current = []
                current_words = 0
                current_chars = 0
        current.append(p)
        current_words += words
        current_chars += len(p)
    if current:
        chunks.append("\n\n".join(current).strip())
    return [c for c in chunks if c]


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if path.name in EXCLUDE_FILES:
            continue
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        yield path


def load_manifest_index(manifest_path: Optional[Path]) -> Dict[str, Dict]:
    if not manifest_path or not manifest_path.exists():
        return {}
    index: Dict[str, Dict] = {}
    with open(manifest_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            md_path = row.get("md")
            if not md_path:
                continue
            index[os.path.abspath(md_path)] = row
    return index


def embed_texts(
    *,
    texts: List[str],
    base_url: str,
    api_key: str,
    model: str,
    timeout_seconds: int = 120,
) -> List[List[float]]:
    endpoint = f"{base_url.rstrip('/')}/embeddings"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model, "input": texts}
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
    embeddings: List[List[float]] = []
    for item in items:
        emb = item.get("embedding")
        if not emb:
            raise RuntimeError(f"Embeddings response missing embedding: {item}")
        embeddings.append(emb)
    return embeddings


def main() -> None:
    args = parse_args()
    source_dir = Path(args.source_dir)
    output_path = Path(args.output)
    manifest_path = Path(args.manifest) if args.manifest else source_dir / "_manifest.jsonl"

    if not source_dir.exists():
        raise SystemExit(f"Source dir not found: {source_dir}")
    if not args.api_key and not args.dry_run:
        raise SystemExit("Missing --api-key (or set BLOG_API_KEY/OPENAI_API_KEY).")

    manifest_index = load_manifest_index(manifest_path)
    files = list(iter_markdown_files(source_dir))
    start_idx = max(0, int(args.start_index)) if args.start_index is not None else 0
    end_idx = int(args.end_index) if args.end_index is not None else None
    if end_idx is not None and end_idx < start_idx:
        raise SystemExit("--end-index must be >= --start-index")
    files = files[start_idx:end_idx]
    if args.max_files:
        files = files[: max(0, args.max_files)]

    print("=" * 80)
    print("Build Top Blog RAG Index")
    print("=" * 80)
    print(f"Source dir: {source_dir}")
    print(f"Manifest: {manifest_path if manifest_path.exists() else 'none'}")
    print(f"Files: {len(files)}")
    print(f"Output: {output_path}")
    print(f"Embed model: {args.embed_model}")
    if args.append:
        print("Output mode: append")
    if args.skip_existing:
        print("Skip existing: enabled")
    if args.start_index is not None or args.end_index is not None:
        print(f"File slice: {start_idx}:{'' if end_idx is None else end_idx}")
    print(f"Batch size: {args.batch_size}")
    print(f"Max words: {args.max_words}")
    print(f"Max chars: {args.max_chars}")
    print(f"Overlap paragraphs: {args.overlap_paragraphs}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 80)

    if args.dry_run:
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    skip_paths: Optional[set] = None
    if args.skip_existing and output_path.exists():
        skip_paths = set()
        try:
            with open(output_path, "r", encoding="utf-8") as existing:
                for line in existing:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    p = row.get("path")
                    if p:
                        skip_paths.add(p)
        except Exception as e:
            print(f"⚠️ Failed to load existing index for skip: {e}")
            skip_paths = None
    processed = 0
    written = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if args.append else "w"
    with open(output_path, mode, encoding="utf-8") as out:
        for path in files:
            processed += 1
            if skip_paths is not None and os.path.abspath(str(path)) in skip_paths:
                continue
            try:
                raw = path.read_text(encoding="utf-8", errors="ignore")
            except Exception as e:
                print(f"⚠️ Skip unreadable file: {path} ({e})")
                continue

            title = _extract_title(raw)
            body = _strip_front_matter(raw)
            paragraphs = _split_paragraphs(body)
            paragraphs = _normalize_paragraphs(
                paragraphs,
                max_words=max(80, args.max_words),
                max_chars=max(400, args.max_chars),
            )
            chunks = _chunk_paragraphs(
                paragraphs,
                max_words=args.max_words,
                overlap_paragraphs=args.overlap_paragraphs,
                max_chars=args.max_chars,
            )
            if args.max_chunks_per_file:
                chunks = chunks[: max(0, args.max_chunks_per_file)]

            if not chunks:
                continue

            abs_path = os.path.abspath(str(path))
            manifest_row = manifest_index.get(abs_path, {})
            url = manifest_row.get("url", "")

            for i in range(0, len(chunks), args.batch_size):
                batch = chunks[i : i + args.batch_size]
                try:
                    embeddings = embed_texts(
                        texts=batch,
                        base_url=args.api_base_url,
                        api_key=args.api_key,
                        model=args.embed_model,
                    )
                except Exception as e:
                    print(f"⚠️ Embedding failed: {path} batch {i}: {e}")
                    continue

                for j, emb in enumerate(embeddings):
                    chunk_text = batch[j].strip()
                    if not chunk_text:
                        continue
                    record = {
                        "id": f"{abs_path}::chunk{i + j}",
                        "path": abs_path,
                        "url": url,
                        "title": title,
                        "text": chunk_text,
                        "embedding": emb,
                    }
                    out.write(json.dumps(record, ensure_ascii=False) + "\n")
                    written += 1

                if args.sleep:
                    time.sleep(max(0.0, args.sleep))

            if processed % 50 == 0:
                print(f"Processed {processed}/{len(files)} files, wrote {written} chunks...")

    print("=" * 80)
    print(f"Done. Files processed: {processed}")
    print(f"Chunks written: {written}")
    print("=" * 80)


if __name__ == "__main__":
    main()
