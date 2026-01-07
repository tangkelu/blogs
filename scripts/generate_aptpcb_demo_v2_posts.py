#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import batch_blog_generation_openai as gen  # noqa: E402


PROMPTS_DIR = Path("/code/blogs/prompts_aptpcb/blogs_prompt_v5")
BASE_TEMPLATES_DIR = PROMPTS_DIR / "_base_templates_v2"
MODULES_DIR = PROMPTS_DIR / "_modules_v1"
INTERNAL_LINK_POOL = Path("/code/blogs/prompts_aptpcb/internal_link_pool.md")
ASSETS_IMAGE_CATALOG = Path("/code/hileap/frontendAPT/docs/assets-img-filenames.md")
OUT_DIR = Path("/code/blogs/blogs_aptpcb_demo/en")


@dataclass(frozen=True)
class DemoPost:
    filename: str
    base_template: str
    keyword: str
    lsi: list[str]
    modules: list[str]


DEMO_POSTS: list[DemoPost] = [
    DemoPost(
        filename="ict-vs-flying-probe-demo.md",
        base_template="aptpcb-query.md",
        keyword="ICT vs Flying Probe Testing",
        lsi=[
            "in-circuit test coverage",
            "flying probe test lead time",
            "test fixture cost",
            "NPI test strategy",
            "AOI and functional test",
            "DFM files for test",
            "acceptance criteria for test",
        ],
        modules=["comparison"],
    ),
    DemoPost(
        filename="pcb-traceability-and-lot-control-demo.md",
        base_template="aptpcb-pillar.md",
        keyword="PCB Traceability and Lot Control",
        lsi=[
            "lot traceability",
            "serialization and UID",
            "IATF 16949 traceability",
            "CoC and test records",
            "change control",
            "incoming inspection",
            "RMA root-cause analysis",
        ],
        modules=["application"],
    ),
    DemoPost(
        filename="rigid-flex-pcb-manufacturing-demo.md",
        base_template="aptpcb-playbook.md",
        keyword="Rigid-Flex PCB Manufacturing",
        lsi=[
            "rigid-flex stackup planning",
            "bend radius rules",
            "coverlay vs solder mask",
            "controlled impedance rigid-flex",
            "moisture management",
            "prototype vs production",
            "DFM checklist rigid-flex",
        ],
        modules=["capability"],
    ),
]


def _load_internal_link_pool_text() -> str:
    if not INTERNAL_LINK_POOL.exists():
        return ""
    raw = INTERNAL_LINK_POOL.read_text(encoding="utf-8", errors="ignore")
    urls: list[str] = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("-"):
            s = s[1:].strip()
        if s.startswith("http://") or s.startswith("https://"):
            urls.append(s)
    return "\n".join(f"- {u}" for u in urls) + ("\n" if urls else "")


def _load_modules_text(modules: list[str], keyword: str, lsi: list[str]) -> str:
    chunks: list[str] = []
    for m in modules:
        p = MODULES_DIR / f"{m}.md"
        if not p.exists():
            continue
        raw = p.read_text(encoding="utf-8", errors="ignore")
        chunks.append(gen.fill_template_variables(raw, keyword, lsi).strip())
    return "\n\n".join(chunks) + ("\n" if chunks else "")


def _inject_modules(prompt: str, modules_text: str) -> str:
    if not modules_text.strip():
        return prompt
    if "{{modules}}" in prompt:
        return prompt.replace("{{modules}}", modules_text)
    m = re.search(r"^---\\s*$", prompt, flags=re.MULTILINE)
    if not m:
        return prompt + "\n\n" + modules_text
    insert_pos = m.start()
    return prompt[:insert_pos].rstrip() + "\n\n" + modules_text + "\n\n" + prompt[insert_pos:]


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pool_text = _load_internal_link_pool_text()
    written: list[Path] = []
    catalog_paths = (
        gen.load_assets_image_catalog_paths(ASSETS_IMAGE_CATALOG) if ASSETS_IMAGE_CATALOG.exists() else []
    )

    for spec in DEMO_POSTS:
        template_path = BASE_TEMPLATES_DIR / spec.base_template
        template_content = template_path.read_text(encoding="utf-8", errors="ignore")
        prompt = gen.fill_template_variables(template_content, spec.keyword, spec.lsi)

        if "{{internal_link_pool}}" in prompt:
            prompt = prompt.replace("{{internal_link_pool}}", pool_text)

        if "{{assets_image_pool}}" in prompt:
            img_pool = gen.select_assets_image_pool(
                catalog_paths=catalog_paths,
                keyword=spec.keyword,
                lsi_keywords=spec.lsi,
                pool_size=18,
            )
            prompt = prompt.replace("{{assets_image_pool}}", gen.format_assets_image_pool_text(img_pool))

        prompt = _inject_modules(prompt, _load_modules_text(spec.modules, spec.keyword, spec.lsi))

        print(f"=== Generating: {spec.filename} ===")
        content = gen.generate_blog_with_gemini(prompt)
        if not content:
            raise SystemExit(f"Generation failed for: {spec.filename}")

        content = gen.post_process_content(content)
        out_path = OUT_DIR / spec.filename
        out_path.write_text(content, encoding="utf-8")
        written.append(out_path)
        print(f"✅ wrote: {out_path}")

    print("\nDone. Files:")
    for p in written:
        print(f"- {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
