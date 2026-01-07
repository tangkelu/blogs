#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate blogs/1111-2/cn/*.md into en/de/it/fr/ru.

Goals:
- Preserve Markdown structure.
- Preserve HTML markup (tags/attributes) exactly; translate only text content.
- Do not translate PCB manufacturing / electronics industry technical terms.
- Avoid translating anything inside code fences, inline code, or LaTeX blocks.

This script uses an OpenAI-compatible Chat Completions endpoint.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import requests


TARGET_LANGS: Dict[str, str] = {
    "en": "English",
    "de": "German",
    "it": "Italian",
    "fr": "French",
    "ru": "Russian",
}


DEFAULT_BASE_URL = os.environ.get("OPENAI_BASE_URL") or os.environ.get("GEMINI_API_URL") or "https://max.openai365.top/v1"
DEFAULT_MODEL = os.environ.get("OPENAI_MODEL") or os.environ.get("MODEL") or "[满血Pro] gemini-3-pro-preview-maxthinking"


TECH_TERMS = [
    # General PCB / manufacturing / inspection
    "PCB",
    "PCBA",
    "DFM",
    "DFT",
    "DFR",
    "IPC",
    "SMT",
    "THT",
    "BGA",
    "QFN",
    "QFP",
    "LGA",
    "SPI",
    "AOI",
    "X-ray",
    "AXI",
    "ICT",
    "FCT",
    "FAI",
    "MES",
    "SOP",
    "NPI",
    "CTE",
    "Tg",
    "Dk",
    "Df",
    "CAF",
    "SIR",
    "FR-4",
    "Prepreg",
    "Core",
    "Stackup",
    "microstrip",
    "Microstrip",
    "stripline",
    "Stripline",
    "via",
    "Via",
    "microvia",
    "Microvia",
    "backdrill",
    "Back-Drilling",
    "back-drilling",
    "stub",
    "Stub",
    # Surface finish / materials
    "ENIG",
    "OSP",
    "HASL",
    "Immersion Silver",
    "Immersion Tin",
    # Metal core
    "MCPCB",
    "Metal Core PCB",
    "IMS",
    "Hybrid Stack",
    # Documentation / data / test & manufacturing artifacts
    "Gerber",
    "ODB++",
    "BOM",
    "Netlist",
    "Stencil",
    "Pick and Place",
    "BSDL",
    "JTAG",
    "Boundary Scan",
    "SPC",
    "Cpk",
    "Ppk",
    "CAPA",
    "ECO",
    "EDA",
    "DRC",
    "CAM",
    "FAI",
    "ICT",
    "FCT",
    "ATE",
    # Signal / RF / measurement
    "RF",
    "SI",
    "PI",
    "EMI",
    "EMC",
    "TDR",
    "VNA",
    "S-parameter",
    "S-parameters",
    "mmWave",
    "5G",
    "6G",
    # Common process/material terms
    "reflow",
    "Reflow",
    "wave soldering",
    "Wave soldering",
    "Selective wave soldering",
    "Selective Wave Soldering",
    "Hi-Pot",
    "Hipot",
    "MSL",
    "MSD",
    "ESD",
    "SAC305",
    # Common vendor / proper nouns found in this repo
    "HILPCB",
    "Ansys Icepak",
    "Polar Si9000",
]


PLACEHOLDER_PREFIX = "[[__PRESERVE_"
PLACEHOLDER_SUFFIX = "__]]"


@dataclass
class PreserveMap:
    mapping: Dict[str, str]
    order: List[str]


def _make_placeholder(i: int) -> str:
    return f"{PLACEHOLDER_PREFIX}{i}{PLACEHOLDER_SUFFIX}"


def extract_and_preserve(text: str) -> Tuple[str, PreserveMap]:
    """
    Replace code blocks, LaTeX blocks, inline code, and HTML tags with placeholders.
    """
    mapping: Dict[str, str] = {}
    order: List[str] = []

    def _store(chunk: str) -> str:
        key = _make_placeholder(len(order))
        mapping[key] = chunk
        order.append(key)
        return key

    # 1) Fenced code blocks ```...```
    code_fence_re = re.compile(r"```[\s\S]*?```", re.MULTILINE)
    text = code_fence_re.sub(lambda m: _store(m.group(0)), text)

    # 2) LaTeX blocks $$...$$
    latex_block_re = re.compile(r"\$\$[\s\S]*?\$\$", re.MULTILINE)
    text = latex_block_re.sub(lambda m: _store(m.group(0)), text)

    # 3) Inline code `...` (avoid matching across newlines)
    inline_code_re = re.compile(r"`[^`\n]+`")
    text = inline_code_re.sub(lambda m: _store(m.group(0)), text)

    # 4) HTML tags <...> (including <br>, </div>, etc.)
    # Keep tag bytes exactly; translate only the surrounding text.
    html_tag_re = re.compile(r"<[^>]+>")
    text = html_tag_re.sub(lambda m: _store(m.group(0)), text)

    return text, PreserveMap(mapping=mapping, order=order)


def restore_preserved(text: str, preserved: PreserveMap) -> str:
    for key in preserved.order:
        text = text.replace(key, preserved.mapping[key])
    return text


def split_front_matter(md: str) -> Tuple[str, str]:
    if not md.startswith("---\n"):
        return "", md
    # front matter ends at the next --- on its own line
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return "", md
    front = parts[0] + "\n---\n"
    body = parts[1]
    return front, body


def translate_front_matter(front: str, target_lang: str, call_llm) -> str:
    """
    Only translate YAML string values for title/description; keep everything else untouched.
    """
    lines = front.splitlines(True)
    out: List[str] = []
    for line in lines:
        m = re.match(r'^(title|description):\s*"(.*)"\s*$', line.strip("\n"))
        if not m:
            out.append(line)
            continue
        key = m.group(1)
        val = m.group(2)
        if not val.strip():
            out.append(line)
            continue
        translated = call_llm(
            user_text=val,
            target_lang=target_lang,
            content_kind=f"front-matter {key}",
        ).strip()
        translated = translated.replace('"', '\\"')
        out.append(f'{key}: "{translated}"\n')
    return "".join(out)


def translate_front_matter_multi(front: str, lang_codes: List[str], call_llm_multi) -> Dict[str, str]:
    """
    Only translate YAML string values for title/description; keep everything else untouched.
    Returns a mapping lang -> translated front matter.
    """
    lines = front.splitlines(True)
    out: Dict[str, List[str]] = {lc: [] for lc in lang_codes}

    for line in lines:
        m = re.match(r'^(title|description):\s*"(.*)"\s*$', line.strip("\n"))
        if not m:
            for lc in lang_codes:
                out[lc].append(line)
            continue

        key = m.group(1)
        val = m.group(2)
        if not val.strip():
            for lc in lang_codes:
                out[lc].append(line)
            continue

        translations = call_llm_multi(
            user_text=val,
            lang_codes=lang_codes,
            content_kind=f"front-matter {key}",
        )
        for lc in lang_codes:
            translated = (translations.get(lc) or "").strip()
            translated = translated.replace('"', '\\"')
            out[lc].append(f'{key}: "{translated}"\n')

    return {lc: "".join(out[lc]) for lc in lang_codes}


def build_system_prompt(target_lang: str) -> str:
    terms = ", ".join(TECH_TERMS)
    return (
        "You are a senior technical translator specializing in PCB manufacturing and electronics.\n"
        f"Translate Simplified Chinese into {target_lang}.\n\n"
        "Hard rules:\n"
        f"- Do NOT translate these technical terms / acronyms / proper nouns; keep them exactly as written: {terms}\n"
        "- Additionally, keep ALL-CAPS acronyms and slash-joined acronyms unchanged (e.g., DFM, SMT, SPI/AOI, EVT/DVT/PVT).\n"
        "- Do NOT translate any placeholder tokens of the form [[__PRESERVE_<number>__]]. Keep them unchanged.\n"
        "- Do NOT add or remove content.\n"
        "- Keep punctuation, numbering, and Markdown structure consistent.\n"
        "- Output ONLY the translated text, no extra commentary.\n"
    )


def build_system_prompt_multi(lang_codes: List[str]) -> str:
    terms = ", ".join(TECH_TERMS)
    langs = ", ".join(lang_codes)
    return (
        "You are a senior technical translator specializing in PCB manufacturing and electronics.\n"
        "Translate Simplified Chinese into multiple target languages.\n\n"
        "Hard rules:\n"
        f"- Target language codes: {langs}\n"
        f"- Do NOT translate these technical terms / acronyms / proper nouns; keep them exactly as written: {terms}\n"
        "- Additionally, keep ALL-CAPS acronyms and slash-joined acronyms unchanged (e.g., DFM, SMT, SPI/AOI, EVT/DVT/PVT).\n"
        "- Do NOT translate any placeholder tokens of the form [[__PRESERVE_<number>__]]. Keep them unchanged.\n"
        "- Do NOT add or remove content.\n"
        "- Keep punctuation, numbering, and Markdown structure consistent.\n"
        "- Output MUST be a single JSON object with keys exactly matching the target language codes.\n"
        "- Do NOT wrap JSON in Markdown.\n"
    )


def call_chat_completions(
    *,
    base_url: str,
    api_key: str,
    model: str,
    system_prompt: str,
    user_text: str,
    timeout_s: int = 180,
) -> str:
    endpoint = f"{base_url.rstrip('/')}/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.2,
    }
    r = requests.post(endpoint, headers=headers, json=payload, timeout=timeout_s)
    r.raise_for_status()
    data = r.json()
    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:  # pragma: no cover
        raise RuntimeError(f"Unexpected response schema: {data}") from e


def resolve_api_keys(cli_key: str | None) -> List[str]:
    keys: List[str] = []
    if cli_key:
        keys.append(cli_key)
    # Prefer GEMINI_API_KEY / OPENAI_API_KEY if present.
    for env_name in ("GEMINI_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        v = os.environ.get(env_name)
        if v and v not in keys:
            keys.append(v)
    # Also fallback to legacy name
    v = os.environ.get("API_KEY")
    if v and v not in keys:
        keys.append(v)

    # Repo fallback (used by existing generation script). Do not print this value.
    try:
        generation_script = Path(__file__).resolve().parent.parent / "batch_blog_generation_openai.py"
        if generation_script.exists():
            m = re.search(r'^API_KEY\s*=\s*"([^"]+)"\s*$', generation_script.read_text(encoding="utf-8"), re.M)
            if m:
                v = m.group(1)
                if v and v not in keys:
                    keys.append(v)
    except Exception:
        pass
    return keys


def translate_body(body: str, target_lang: str, call_llm) -> str:
    # Preserve structures before translation
    preserved_body, preserved = extract_and_preserve(body)
    return restore_preserved(_translate_large_text(preserved_body, target_lang, call_llm), preserved)


def translate_body_multi(body: str, lang_codes: List[str], call_llm_multi, *, max_chars: int = 9000) -> Dict[str, str]:
    preserved_body, preserved = extract_and_preserve(body)
    chunks = _chunk_text(preserved_body, max_chars=max_chars)
    per_lang_parts: Dict[str, List[str]] = {lc: [] for lc in lang_codes}

    for i, ch in enumerate(chunks, 1):
        translations = call_llm_multi(
            user_text=ch,
            lang_codes=lang_codes,
            content_kind=f"body chunk {i}/{len(chunks)}",
        )
        for lc in lang_codes:
            per_lang_parts[lc].append(translations.get(lc, ""))

    out: Dict[str, str] = {}
    for lc in lang_codes:
        joined = "".join(per_lang_parts[lc])
        out[lc] = restore_preserved(joined, preserved)
    return out


def _chunk_text(text: str, *, max_chars: int) -> List[str]:
    """
    Split text into chunks <= max_chars, preferring paragraph boundaries.
    """
    if len(text) <= max_chars:
        return [text]

    # Keep paragraph separators so we don't lose blank lines.
    tokens = re.split(r"(\n\n+)", text)
    chunks: List[str] = []
    buf = ""
    for tok in tokens:
        if not tok:
            continue
        if len(buf) + len(tok) <= max_chars:
            buf += tok
            continue
        if buf:
            chunks.append(buf)
            buf = ""
        # If a single token is too large, hard-split it.
        if len(tok) > max_chars:
            start = 0
            while start < len(tok):
                chunks.append(tok[start : start + max_chars])
                start += max_chars
        else:
            buf = tok
    if buf:
        chunks.append(buf)
    return chunks


def _translate_large_text(text: str, target_lang: str, call_llm, *, max_chars: int = 9000) -> str:
    chunks = _chunk_text(text, max_chars=max_chars)
    out_parts: List[str] = []
    for i, ch in enumerate(chunks, 1):
        translated = call_llm(
            user_text=ch,
            target_lang=target_lang,
            content_kind=f"body chunk {i}/{len(chunks)}",
        )
        out_parts.append(translated)
    return "".join(out_parts)


def _extract_json_object(text: str) -> Dict[str, str]:
    text = text.strip()
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj  # type: ignore[return-value]
    except Exception:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        obj = json.loads(text[start : end + 1])
        if isinstance(obj, dict):
            return obj  # type: ignore[return-value]
    raise ValueError("Model did not return a valid JSON object.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="blogs/1111-2/cn", help="Source directory (cn)")
    ap.add_argument("--dst-base", default="blogs/1111-2", help="Destination base dir")
    ap.add_argument("--base-url", default=DEFAULT_BASE_URL, help="OpenAI-compatible base URL")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Model name")
    ap.add_argument("--api-key", default=None, help="API key (optional; otherwise from env)")
    ap.add_argument("--langs", default="en,de,it,fr,ru", help="Comma-separated target languages")
    ap.add_argument("--sleep", type=float, default=0.8, help="Sleep between requests (seconds)")
    ap.add_argument("--max-chars", type=int, default=9000, help="Max characters per request chunk")
    ap.add_argument("--langs-per-call", type=int, default=2, help="How many target languages to request per LLM call")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing translated files")
    args = ap.parse_args()

    src_dir = Path(args.src)
    dst_base = Path(args.dst_base)
    if not src_dir.exists():
        print(f"Source dir not found: {src_dir}", file=sys.stderr)
        return 2

    md_files = sorted([p for p in src_dir.glob("*.md") if p.is_file()])
    if not md_files:
        print(f"No .md files found in: {src_dir}", file=sys.stderr)
        return 2

    langs = [s.strip() for s in args.langs.split(",") if s.strip()]
    for lang in langs:
        if lang not in TARGET_LANGS:
            print(f"Unsupported lang: {lang}", file=sys.stderr)
            return 2

    api_keys = resolve_api_keys(args.api_key)
    if not api_keys:
        print("No API key provided via --api-key or env (GEMINI_API_KEY/OPENAI_API_KEY).", file=sys.stderr)
        return 2

    def _call_llm_multi(*, user_text: str, lang_codes: List[str], content_kind: str) -> Dict[str, str]:
        sys_prompt = build_system_prompt_multi(lang_codes)
        user_prompt = (
            "Return JSON only.\n"
            f"Translate the following text into: {', '.join(lang_codes)}.\n"
            f"JSON keys (exact): {', '.join(lang_codes)}.\n"
            "Text:\n"
            "<<<\n"
            f"{user_text}\n"
            ">>>\n"
        )
        last_err: Exception | None = None
        for key_idx, key in enumerate(api_keys):
            for attempt in range(1, 4):
                try:
                    raw = call_chat_completions(
                        base_url=args.base_url,
                        api_key=key,
                        model=args.model,
                        system_prompt=sys_prompt,
                        user_text=user_prompt,
                    )
                    obj = _extract_json_object(raw)
                    out: Dict[str, str] = {}
                    for lc in lang_codes:
                        v = obj.get(lc, "")
                        out[lc] = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
                    return out
                except Exception as e:
                    last_err = e
                    # brief backoff; also helps transient gateway disconnects
                    time.sleep(min(6.0, 1.5 * attempt))
            # try next key
            if key_idx < len(api_keys) - 1:
                continue
        assert last_err is not None
        raise last_err

    for lang in langs:
        (dst_base / lang).mkdir(parents=True, exist_ok=True)

    for src_path in md_files:
        missing_langs = []
        for lang in langs:
            dst_path = dst_base / lang / src_path.name
            if not dst_path.exists() or args.overwrite:
                missing_langs.append(lang)

        if not missing_langs:
            print(f"[skip] {src_path.name} (all languages exist)")
            continue

        md = src_path.read_text(encoding="utf-8")
        front, body = split_front_matter(md)
        if not front:
            print(f"[warn] no front matter: {src_path}", file=sys.stderr)
            front = ""

        # Prepare body once (placeholders + chunks), then translate in smaller language batches
        preserved_body, preserved = extract_and_preserve(body)
        body_chunks = _chunk_text(preserved_body, max_chars=args.max_chars)

        def _lang_groups(all_langs: List[str], n: int) -> List[List[str]]:
            n = max(1, int(n))
            return [all_langs[i : i + n] for i in range(0, len(all_langs), n)]

        groups = _lang_groups(missing_langs, args.langs_per_call)
        print(f"[multi] translating: {src_path.name} -> {','.join(missing_langs)} (groups={len(groups)})")

        for group in groups:
            new_front_map = translate_front_matter_multi(front, group, _call_llm_multi) if front else {lc: "" for lc in group}
            time.sleep(args.sleep)

            per_lang_parts: Dict[str, List[str]] = {lc: [] for lc in group}
            for i, ch in enumerate(body_chunks, 1):
                translations = _call_llm_multi(
                    user_text=ch,
                    lang_codes=group,
                    content_kind=f"body chunk {i}/{len(body_chunks)}",
                )
                for lc in group:
                    per_lang_parts[lc].append(translations.get(lc, ""))
                time.sleep(args.sleep)

            for lang in group:
                dst_path = dst_base / lang / src_path.name
                joined = "".join(per_lang_parts[lang])
                new_body = restore_preserved(joined, preserved)
                out = new_front_map.get(lang, "") + new_body
                dst_path.write_text(out, encoding="utf-8")
                time.sleep(args.sleep)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
