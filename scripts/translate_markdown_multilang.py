#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Protocol

import requests
import yaml


GOOGLE_TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"


def _google_translate(text: str, *, source_lang: str, target_lang: str, timeout_s: int = 45) -> str:
    if not text.strip():
        return text

    last_error: Exception | None = None
    for attempt in range(5):
        try:
            resp = requests.post(
                GOOGLE_TRANSLATE_URL,
                params={
                    "client": "gtx",
                    "sl": source_lang,
                    "tl": target_lang,
                    "dt": "t",
                },
                data={"q": text},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=timeout_s,
            )
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, list) or not data:
                return text
            parts = data[0]
            if not isinstance(parts, list):
                return text
            return "".join(p[0] for p in parts if isinstance(p, list) and p and isinstance(p[0], str))
        except Exception as e:  # noqa: BLE001 - best-effort external service
            last_error = e
            time.sleep(0.7 * (attempt + 1))

    raise RuntimeError(f"Translation failed after retries: {last_error}")

_RE_HTML_TAG = re.compile(r"<[^>\n]*>")
_RE_CODE_INLINE = re.compile(r"`[^`\n]+`")
_RE_MD_LINK_TARGET = re.compile(r"\]\([^\)\n]+\)")
_RE_URL_BARE = re.compile(r"https?://\S+")
_RE_TECH_ACRONYM = re.compile(r"\b[A-Z]{2,}[A-Z0-9+./_-]*\b")
_RE_ALNUM_WITH_DIGIT = re.compile(r"\b[A-Za-z]*\d+[A-Za-z0-9+./_-]*\b")

# Common PCB / manufacturing terms to keep as-is across languages.
DEFAULT_GLOSSARY_TERMS: tuple[str, ...] = (
    "PCB",
    "PCBA",
    "SMT",
    "THT",
    "BGA",
    "QFN",
    "LGA",
    "DFM",
    "DFA",
    "DFT",
    "DVT",
    "PVT",
    "MP",
    "PDN",
    "SI",
    "PI",
    "EMI",
    "EMC",
    "ICT",
    "FCT",
    "AOI",
    "X-Ray",
    "X-ray",
    "Hi-Pot",
    "TDR",
    "VNA",
    "S-parameter",
    "S parameters",
    "S11",
    "S21",
    "CTE",
    "Tg",
    "Td",
    "Dk",
    "Df",
    "OSP",
    "ENIG",
    "ENEPIG",
    "VIPPO",
    "Via-in-Pad",
    "Microvia",
    "Microvias",
    "Back-drilling",
    "Backdrilling",
    "Impedance",
    "Coupon",
    "Prepreg",
    "Core",
    "Stackup",
    "Warpage",
    "CAF",
    "MSL",
    "ELIC",
    "HDI",
    "FR-4",
    "High-Tg",
    "LLM",
    "HPC",
    "PCIe",
    "CXL",
    "Chiplet",
    "Interposer",
    "ABF",
)


def _contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4E00-\u9FFF]", text))


def _merge_spans(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not spans:
        return []
    spans.sort()
    merged: list[tuple[int, int]] = [spans[0]]
    for s, e in spans[1:]:
        ls, le = merged[-1]
        if s <= le:
            merged[-1] = (ls, max(le, e))
        else:
            merged.append((s, e))
    return merged


def _find_term_spans(text: str, terms: Iterable[str]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for term in sorted({t for t in terms if t}, key=len, reverse=True):
        start = 0
        while True:
            idx = text.find(term, start)
            if idx == -1:
                break
            spans.append((idx, idx + len(term)))
            start = idx + len(term)
    return spans


def _segment_text_preserving_markup(text: str, glossary_terms: Iterable[str]) -> list[tuple[str, object]]:
    """
    Return a list of parts:
      - ("lit", literal_text)
      - ("seg", (left_ws, core_text, right_ws)) for translatable parts
    """
    spans: list[tuple[int, int]] = []
    for pat in (
        _RE_CODE_INLINE,
        _RE_HTML_TAG,
        _RE_MD_LINK_TARGET,
        _RE_URL_BARE,
        _RE_TECH_ACRONYM,
        _RE_ALNUM_WITH_DIGIT,
    ):
        spans.extend((m.start(), m.end()) for m in pat.finditer(text))
    spans.extend(_find_term_spans(text, glossary_terms))
    spans = _merge_spans(spans)

    pieces: list[tuple[str, str]] = []
    last = 0
    for s, e in spans:
        if last < s:
            pieces.append(("t", text[last:s]))
        pieces.append(("k", text[s:e]))
        last = e
    if last < len(text):
        pieces.append(("t", text[last:]))

    out: list[tuple[str, object]] = []
    for kind, chunk in pieces:
        if kind == "k" or not chunk:
            out.append(("lit", chunk))
            continue

        m = re.match(r"^(\s*)(.*?)(\s*)$", chunk, flags=re.DOTALL)
        assert m
        left_ws, core, right_ws = m.groups()
        if not core or not _contains_cjk(core):
            out.append(("lit", chunk))
            continue
        out.append(("seg", (left_ws, core, right_ws)))

    return out


class TranslationEngine(Protocol):
    def translate_texts(self, texts: list[str]) -> list[str]: ...


@dataclass
class HFMarianEngine:
    model_id: str
    batch_size: int = 16
    device: str = "cpu"

    _tokenizer: object | None = None
    _model: object | None = None

    def _ensure_loaded(self) -> None:
        if self._tokenizer is not None and self._model is not None:
            return
        from transformers import MarianMTModel, MarianTokenizer  # local import

        self._tokenizer = MarianTokenizer.from_pretrained(self.model_id)
        self._model = MarianMTModel.from_pretrained(self.model_id)
        self._model.to(self.device)
        self._model.eval()

    def translate_texts(self, texts: list[str]) -> list[str]:
        self._ensure_loaded()
        assert self._tokenizer is not None
        assert self._model is not None

        import torch  # local import

        tokenizer = self._tokenizer
        model = self._model

        out: list[str] = []
        for start in range(0, len(texts), self.batch_size):
            batch = texts[start : start + self.batch_size]
            inputs = tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512,
            )
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            with torch.inference_mode():
                generated = model.generate(
                    **inputs,
                    max_new_tokens=512,
                    num_beams=1,
                    do_sample=False,
                )
                out.extend(tokenizer.batch_decode(generated, skip_special_tokens=True))
        return out


@dataclass
class HFChainEngine:
    first: TranslationEngine
    second: TranslationEngine

    def translate_texts(self, texts: list[str]) -> list[str]:
        if not texts:
            return []
        return self.second.translate_texts(self.first.translate_texts(texts))


@dataclass
class GoogleEngine:
    source_lang: str
    target_lang: str
    timeout_s: int = 45

    _marker: str = "@@@999999999@@@"

    def translate_texts(self, texts: list[str]) -> list[str]:
        if not texts:
            return []
        # Batch to reduce requests; fall back to per-item if marker gets mangled.
        joined = ("\n" + self._marker + "\n").join(texts)
        translated = _google_translate(
            joined, source_lang=self.source_lang, target_lang=self.target_lang, timeout_s=self.timeout_s
        )
        pieces = re.split(rf"\s*{re.escape(self._marker)}\s*", translated)
        if len(pieces) == len(texts):
            return pieces
        return [
            _google_translate(t, source_lang=self.source_lang, target_lang=self.target_lang, timeout_s=self.timeout_s)
            for t in texts
        ]


@dataclass
class BatchTranslator:
    engine: TranslationEngine
    glossary_terms: tuple[str, ...]
    cache: dict[str, str] = field(default_factory=dict)

    def translate_many(self, fragments: list[str]) -> list[str]:
        results: list[str] = [""] * len(fragments)
        segment_texts: list[str] = []
        fragment_structs: list[tuple[str, list[tuple]] | None] = [None] * len(fragments)

        for idx, fragment in enumerate(fragments):
            if not fragment.strip():
                results[idx] = fragment
                continue
            cached = self.cache.get(fragment)
            if cached is not None:
                results[idx] = cached
                continue

            parts = _segment_text_preserving_markup(fragment, self.glossary_terms)
            built: list[tuple] = []
            for kind, payload in parts:
                if kind == "lit":
                    built.append(("lit", payload))
                    continue
                if kind != "seg":
                    raise AssertionError(f"Unknown segment kind: {kind}")
                left_ws, core, right_ws = payload
                seg_idx = len(segment_texts)
                segment_texts.append(core)
                built.append(("seg", left_ws, seg_idx, right_ws))

            fragment_structs[idx] = (fragment, built)

        translated_segments: list[str] = []
        if segment_texts:
            translated_segments = self.engine.translate_texts(segment_texts)
            if len(translated_segments) != len(segment_texts):
                raise RuntimeError("Translation engine returned mismatched segment count")

        for idx, struct in enumerate(fragment_structs):
            if struct is None:
                continue
            original, built = struct
            out: list[str] = []
            for item in built:
                if item[0] == "lit":
                    out.append(item[1])
                    continue
                _kind, left_ws, seg_idx, right_ws = item
                out.append(left_ws + translated_segments[seg_idx] + right_ws)
            translated = "".join(out)
            self.cache[original] = translated
            results[idx] = translated

        return results


def _is_table_separator(line: str) -> bool:
    row = line.strip()
    if not row.startswith("|"):
        return False
    inner = row.strip("|").strip()
    return bool(re.fullmatch(r"[:\-\s\|]+", inner))


def _translate_markdown_body(
    body: str,
    *,
    translator: BatchTranslator,
) -> str:
    lines = body.splitlines(keepends=True)
    parts: list[tuple] = []
    fragments: list[str] = []

    def add_fragment(text: str) -> int:
        fragments.append(text)
        return len(fragments) - 1

    in_fence = False
    fence_marker = ""
    for line in lines:
        stripped = line.strip()

        if in_fence:
            parts.append(("raw", line))
            if stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            continue

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = True
            fence_marker = stripped[:3]
            parts.append(("raw", line))
            continue

        if stripped.startswith("|"):
            newline = "\n" if line.endswith("\n") else ""
            row = line.rstrip("\n")
            if _is_table_separator(row):
                parts.append(("raw", row + newline))
                continue

            # Translate per cell, preserving pipes and whitespace.
            if not row.startswith("|") or "|" not in row[1:]:
                parts.append(("raw", line))
                continue

            table_parts = row.split("|")
            leading = table_parts[0]
            trailing = table_parts[-1]
            cells = table_parts[1:-1]

            cell_specs: list[tuple] = []
            for cell in cells:
                m = re.match(r"^(\s*)(.*?)(\s*)$", cell, flags=re.DOTALL)
                if not m:
                    cell_specs.append(("raw", cell))
                    continue
                left_ws, content, right_ws = m.groups()
                if not content.strip():
                    cell_specs.append(("raw", cell))
                    continue
                frag_idx = add_fragment(content)
                cell_specs.append(("frag", left_ws, frag_idx, right_ws))

            parts.append(("table", leading, cell_specs, trailing, newline))
            continue

        if not stripped or stripped in {"---", "***"}:
            parts.append(("raw", line))
            continue

        newline = "\n" if line.endswith("\n") else ""
        raw = line.rstrip("\n")

        m = re.match(r"^(#{1,6}\s+)(.*)$", raw)
        if m:
            prefix, content = m.groups()
            frag_idx = add_fragment(content)
            parts.append(("line", prefix, frag_idx, newline))
            continue

        m = re.match(r"^(>+\s*)(.*)$", raw)
        if m:
            prefix, content = m.groups()
            frag_idx = add_fragment(content)
            parts.append(("line", prefix, frag_idx, newline))
            continue

        m = re.match(r"^(\s*(?:[-*+]|\d+\.)\s+)(.*)$", raw)
        if m:
            prefix, content = m.groups()
            frag_idx = add_fragment(content)
            parts.append(("line", prefix, frag_idx, newline))
            continue

        frag_idx = add_fragment(raw)
        parts.append(("line", "", frag_idx, newline))

    translated_fragments = translator.translate_many(fragments)
    out: list[str] = []
    for part in parts:
        kind = part[0]
        if kind == "raw":
            out.append(part[1])
        elif kind == "line":
            _kind, prefix, frag_idx, newline = part
            out.append(prefix + translated_fragments[frag_idx] + newline)
        elif kind == "table":
            _kind, leading, cell_specs, trailing, newline = part
            out_cells: list[str] = []
            for spec in cell_specs:
                if spec[0] == "raw":
                    out_cells.append(spec[1])
                    continue
                _s, left_ws, frag_idx, right_ws = spec
                out_cells.append(left_ws + translated_fragments[frag_idx] + right_ws)
            out.append("|".join([leading, *out_cells, trailing]) + newline)
        else:
            raise AssertionError(f"Unknown part kind: {kind}")

    return "".join(out)


def _translate_front_matter(front_matter: str, *, translator: BatchTranslator) -> str:
    lines = front_matter.splitlines(keepends=True)
    out: list[str] = []
    fragments: list[str] = []
    placeholders: list[tuple[int, str, str]] = []
    for line in lines:
        raw = line.rstrip("\n")
        m = re.match(r'^(title:\s*)(["\'])(.*)\2\s*$', raw)
        if m:
            prefix, quote, value = m.groups()
            idx = len(fragments)
            fragments.append(value)
            placeholders.append((idx, prefix, quote))
            out.append(f"{prefix}{quote}__FRAG_{idx}__{quote}\n")
            continue

        m = re.match(r'^(description:\s*)(["\'])(.*)\2\s*$', raw)
        if m:
            prefix, quote, value = m.groups()
            idx = len(fragments)
            fragments.append(value)
            placeholders.append((idx, prefix, quote))
            out.append(f"{prefix}{quote}__FRAG_{idx}__{quote}\n")
            continue

        out.append(line)

    if not fragments:
        return "".join(out)

    translated = translator.translate_many(fragments)
    rendered = "".join(out)
    for idx, _prefix, _quote in placeholders:
        rendered = rendered.replace(f"__FRAG_{idx}__", translated[idx])
    return rendered


def _extract_front_matter(md: str) -> tuple[str, str]:
    if not md.startswith("---\n"):
        return "", md
    end = md.find("\n---\n", 4)
    if end == -1:
        return "", md
    front = md[: end + len("\n---\n")]
    body = md[end + len("\n---\n") :]
    return front, body


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Translate a Markdown directory from zh-CN into multiple languages while preserving HTML tags and PCB terms."
    )
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--out-root", type=Path, required=True)
    parser.add_argument("--source-lang", default="zh-CN")
    parser.add_argument("--langs", default="en,de,it,fr,ru")
    parser.add_argument("--engine", choices=["hf", "google"], default="hf")
    parser.add_argument("--hf-batch-size", type=int, default=16)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source_dir: Path = args.source_dir
    out_root: Path = args.out_root
    langs = [s.strip() for s in args.langs.split(",") if s.strip()]

    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        raise SystemExit(f"No .md files found in {source_dir}")

    shared_zh_en: HFMarianEngine | None = None

    for lang in langs:
        out_dir = out_root / lang
        out_dir.mkdir(parents=True, exist_ok=True)

        if args.engine == "hf":
            if lang == "en":
                if shared_zh_en is None:
                    shared_zh_en = HFMarianEngine(model_id="Helsinki-NLP/opus-mt-zh-en", batch_size=args.hf_batch_size)
                engine = shared_zh_en
            elif lang == "de":
                engine = HFMarianEngine(model_id="Helsinki-NLP/opus-mt-zh-de", batch_size=args.hf_batch_size)
            elif lang == "it":
                engine = HFMarianEngine(model_id="Helsinki-NLP/opus-mt-zh-it", batch_size=args.hf_batch_size)
            elif lang == "fr":
                if shared_zh_en is None:
                    shared_zh_en = HFMarianEngine(model_id="Helsinki-NLP/opus-mt-zh-en", batch_size=args.hf_batch_size)
                engine = HFChainEngine(
                    first=shared_zh_en,
                    second=HFMarianEngine(model_id="Helsinki-NLP/opus-mt-en-fr", batch_size=args.hf_batch_size),
                )
            elif lang == "ru":
                if shared_zh_en is None:
                    shared_zh_en = HFMarianEngine(model_id="Helsinki-NLP/opus-mt-zh-en", batch_size=args.hf_batch_size)
                engine = HFChainEngine(
                    first=shared_zh_en,
                    second=HFMarianEngine(model_id="Helsinki-NLP/opus-mt-en-ru", batch_size=args.hf_batch_size),
                )
            else:
                raise SystemExit(f"No HF model configured for language: {lang}")
        else:
            engine = GoogleEngine(source_lang=args.source_lang, target_lang=lang)

        for md_path in md_files:
            out_path = out_dir / md_path.name
            if out_path.exists() and not args.overwrite:
                print(f"skip (exists): {out_path}")
                continue

            md_text = md_path.read_text(encoding="utf-8")
            front, body = _extract_front_matter(md_text)

            glossary_terms: set[str] = set()
            if front:
                try:
                    front_inner = front.strip()[3:-3].strip()
                    data = yaml.safe_load(front_inner) or {}
                    tags = data.get("tags") if isinstance(data, dict) else None
                    if isinstance(tags, list):
                        glossary_terms.update(str(t) for t in tags if isinstance(t, (str, int, float)))
                except Exception:
                    pass

            print(f"translating: {md_path.name} -> {lang}")
            combined_glossary = tuple(sorted({*DEFAULT_GLOSSARY_TERMS, *glossary_terms}, key=len, reverse=True))
            translator = BatchTranslator(engine=engine, glossary_terms=combined_glossary)

            translated_front = _translate_front_matter(front, translator=translator) if front else ""
            translated_body = _translate_markdown_body(body, translator=translator)

            out_text = translated_front + translated_body
            if args.dry_run:
                continue
            out_path.write_text(out_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
