#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script to run v6 blog generation based on the content map.
Usage:
    python run_v6_generation.py --category 04-HighSpeed-Impedance
    python run_v6_generation.py --keyword "impedance"
    python run_v6_generation.py --limit 5  (runs first 5 pending)
"""

import argparse
import subprocess
import sys
import re
import os
from pathlib import Path

MAP_FILE = Path("prompts_aptpcb/v6_content_map.md")
GENERATOR_SCRIPT = "batch_blog_generation_aptpcb.py"

def parse_map_file():
    """Parses the markdown map file and returns a list of tasks."""
    if not MAP_FILE.exists():
        print(f"Error: Map file not found at {MAP_FILE}")
        sys.exit(1)
        
    content = MAP_FILE.read_text(encoding='utf-8')
    tasks = []
    
    # Regex to parse table rows: | Category | Keyword | Filename | Status |
    # Matches: | 01-Cost | advanced pcb | `file.md` | ... |
    pattern = re.compile(r"\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*`?([^`|]+)`?\s*\|\s*([^|]+)\s*\|")
    
    for line in content.splitlines():
        if "---" in line or "Category" in line:
            continue
        m = pattern.match(line.strip())
        if m:
            cat, kw, filename, status = m.groups()
            tasks.append({
                "category": cat.strip(),
                "keyword": kw.strip(),
                "filename": filename.strip(),
                "status": status.strip()
            })
    return tasks

def update_task_status(keyword, new_status="✅ Done"):
    """Updates the status of a specific keyword in the map file."""
    if not MAP_FILE.exists():
        return
        
    lines = MAP_FILE.read_text(encoding='utf-8').splitlines()
    new_lines = []
    updated = False
    
    # Simple matching logic: find line containing keyword and pipe separators
    for line in lines:
        if "|" in line and keyword in line and not updated:
            # Check if it's the specific keyword column (2nd column)
            # Row format: | Category | Keyword | ...
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3 and parts[2].lower() == keyword.lower():
                # Reconstruct the line with new status
                # We assume status is the last column usually, but let's be robust
                # Current format: | Cat | Kw | File | Status |
                # split gives ['', 'Cat', 'Kw', 'File', 'Status', '']
                if len(parts) >= 5:
                    # Update the 4th functional column (index 4 in split array)
                     parts[4] = f" {new_status} "
                     line = "|".join(parts)
                     updated = True
        new_lines.append(line)
        
    if updated:
        MAP_FILE.write_text("\n".join(new_lines), encoding='utf-8')
        print(f"📝 Updated status for '{keyword}' in map file.")

def main():
    parser = argparse.ArgumentParser(description="Run v6 generation based on content map.")
    parser.add_argument("--category", help="Filter by category name (partial match)")
    parser.add_argument("--keyword", help="Filter by keyword (partial match)")
    parser.add_argument("--limit", type=int, default=0, help="Max number of blogs to generate")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without running")
    parser.add_argument("--random-template", action="store_true", help="Randomly select a template kind (query, pillar, playbook, story)")
    
    args = parser.parse_args()
    
    all_tasks = parse_map_file()
    selected_tasks = []
    
    print(f"Loaded {len(all_tasks)} entries from map.")
    
    for task in all_tasks:
        # Filter logic
        if args.category and args.category.lower() not in task["category"].lower():
            continue
        if args.keyword and args.keyword.lower() not in task["keyword"].lower():
            continue
            
        is_done = "✅" in task["status"] or "Done" in task["status"] or "Completed" in task["status"]
        
        # If specific keyword is requested, we allow re-running even if done (override).
        if args.keyword:
             pass
        elif is_done:
             continue
            
        selected_tasks.append(task)
        
    if args.limit > 0:
        selected_tasks = selected_tasks[:args.limit]
        
    print(f"Selected {len(selected_tasks)} tasks to run.")
    
    if not selected_tasks:
        print("No tasks matched your filters.")
        return

    for i, task in enumerate(selected_tasks):
        print(f"\n[{i+1}/{len(selected_tasks)}] Processing: {task['keyword']} ({task['category']})")
        
        # Construct command
        # Use --keyword-search to target one specific keyword even if used.
        # Use --ignore-sitemap to overwrite filenames.
        cmd = [
            sys.executable, "-u", GENERATOR_SCRIPT,
            "--prompts-dir", "prompts_aptpcb/blogs_prompt_v6",
            "--keyword-search", task["keyword"],
            "--output-base-dir", "blogs_aptpcb_v6_staging",
            "--ignore-sitemap"
        ]
        
        if args.random_template:
            import random
            template_kind = random.choice(["query", "pillar", "playbook", "story"])
            print(f"🎲 Randomly selected template: {template_kind}")
            cmd.extend(["--template-kind", template_kind])
        
        # Optimization: REMOVED. The generator script expects PROMPTS_DIR to be the parent of category directories.
        
        cmd_str = " ".join(cmd)
        if args.dry_run:
            print(f"DRY RUN: {cmd_str}")
        else:
            # Capture output to verify actual generation success
            # We look for "✅ 博客生成成功" or "Generated blog successfully" (depending on script output)
            # Based on logs: "✅ 博客生成成功"
            
            try:
                env = os.environ.copy()
                env["PYTHONIOENCODING"] = "utf-8"
                
                process = subprocess.Popen(
                    cmd, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, # Merge stderr to stdout
                    text=True, 
                    encoding='utf-8',
                    errors='replace',
                    env=env,
                    bufsize=1
                )
                
                success_marker_found = False
                
                # Stream output for user visibility
                while True:
                    line = process.stdout.readline()
                    if not line and process.poll() is not None:
                        break
                    if line:
                        print(line, end='')
                        if "✅ 博客生成成功" in line:
                            success_marker_found = True
                            
                ret = process.poll()
                
                if ret != 0:
                     print(f"❌ Script failed (Exit code {ret})")
                elif not success_marker_found:
                     print(f"⚠️ Script finished but no blog was generated (Keyword not found or skipped).")
                else:
                     print(f"✅ Finished {task['keyword']}")
                     update_task_status(task["keyword"])
                     
            except Exception as e:
                print(f"❌ Execution error: {e}")

if __name__ == "__main__":
    main()
