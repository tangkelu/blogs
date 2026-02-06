#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates a markdown map of Keyword -> Slug/Filename for v6 migration planning.
"""

from pathlib import Path
import json
from slugify import slugify

def main():
    root_dir = Path("d:/website/blogs/prompts_aptpcb/blogs_prompt_v6")
    output_file = Path("d:/website/blogs/prompts_aptpcb/v6_content_map.md")
    
    if not root_dir.exists():
        print(f"Directory not found: {root_dir}")
        return

    md_lines = []
    md_lines.append("# v6 Content Map (Keyword -> Filename)")
    md_lines.append("")
    md_lines.append("Use this map to identify which files correspond to which keywords.")
    md_lines.append("")
    
    # Header
    md_lines.append("| Category | Keyword | Expected Filename | Status |")
    md_lines.append("|---|---|---|---|")

    categories = sorted([d for d in root_dir.iterdir() if d.is_dir() and not d.name.startswith("_")])
    
    count = 0
    for cat_dir in categories:
        keywords_file = cat_dir / "keywords.json"
        cat_name = cat_dir.name
        
        if not keywords_file.exists():
            continue
            
        try:
            data = json.loads(keywords_file.read_text(encoding='utf-8'))
            for subsection in data.get("subsections", []):
                for kw_obj in subsection.get("keywords", []):
                    kw = kw_obj.get("keyword")
                    used = kw_obj.get("used", False)
                    slug = slugify(kw)
                    filename = f"{slug}.md"
                    
                    status = "✅ Done" if used else "⬜ Pending"
                    md_lines.append(f"| {cat_name} | {kw} | `{filename}` | {status} |")
                    count += 1
        except Exception as e:
            md_lines.append(f"| {cat_name} | ERROR reading JSON | {e} | - |")

    output_file.write_text("\n".join(md_lines), encoding='utf-8')
    print(f"Generated map with {count} entries at: {output_file}")

if __name__ == "__main__":
    main()
