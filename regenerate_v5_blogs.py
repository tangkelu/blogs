
import os
import json
import sys
import subprocess
import time
from pathlib import Path

V5_DIR = Path("prompts_aptpcb/blogs_prompt_v5")
V6_MAP_FILE = Path("prompts_aptpcb/v6_content_map.md")
RUN_SCRIPT = "run_v6_generation.py"

def find_used_keywords():
    used_keywords = set()
    if not V5_DIR.exists():
        print(f"Error: {V5_DIR} does not exist.")
        return []

    for root, dirs, files in os.walk(V5_DIR):
        if "keywords.json" in files:
            json_path = Path(root) / "keywords.json"
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "subsections" in data:
                        for section in data["subsections"]:
                            if "keywords" in section:
                                for kw_obj in section["keywords"]:
                                    if kw_obj.get("used") == True:
                                        used_keywords.add(kw_obj["keyword"])
            except Exception as e:
                print(f"Error reading {json_path}: {e}")
    return sorted(list(used_keywords))

def get_v6_map_keywords():
    if not V6_MAP_FILE.exists():
        print(f"Error: {V6_MAP_FILE} does not exist.")
        return set()
    
    content = V6_MAP_FILE.read_text(encoding='utf-8')
    keywords = set()
    for line in content.splitlines():
        if "|" in line and "---" not in line and "Category" not in line:
            parts = [p.strip() for p in line.split("|")]
            # | Category | Keyword | ...
            if len(parts) >= 3:
                kw = parts[2]
                if kw:
                    keywords.add(kw.lower())
    return keywords

def main():
    print("🔍 Scanning v5 for used keywords...")
    v5_keywords = find_used_keywords()
    print(f"Found {len(v5_keywords)} unique used keywords in v5.")
    
    print("🔍 Reading v6 content map...")
    v6_map_keywords = get_v6_map_keywords()
    
    tasks_to_run = []
    missing_in_v6 = []
    
    for kw in v5_keywords:
        if kw.lower() in v6_map_keywords:
            tasks_to_run.append(kw)
        else:
            missing_in_v6.append(kw)
            
    print(f"✅ {len(tasks_to_run)} keywords match with v6 map.")
    if missing_in_v6:
        print(f"⚠️ {len(missing_in_v6)} keywords from v5 are NOT in v6 map (skipping these):")
        for m in missing_in_v6[:10]:
            print(f"  - {m}")
        if len(missing_in_v6) > 10:
            print(f"  ... and {len(missing_in_v6)-10} more.")
            
    if not tasks_to_run:
        print("No tasks to run.")
        return

    print("\n🚀 Starting regeneration process...")
    print("This will run sequentially to ensure map file integrity.")
    
    for i, kw in enumerate(tasks_to_run):
        print(f"\n[{i+1}/{len(tasks_to_run)}] Regenerating blog for: '{kw}'")
        
        # Invoke run_v6_generation.py
        # We pass --keyword explicitly. 
        # Using sys.executable ensures we use the same python interpreter.
        cmd = [sys.executable, "-u", RUN_SCRIPT, "--keyword", kw]
        
        start_time = time.time()
        try:
            # We run it and capture output to print it nicely or just let it flow to stdout
            # Let's let it flow to stdout so user sees progress
            result = subprocess.run(cmd, check=False)
            
            elapsed = time.time() - start_time
            if result.returncode == 0:
                print(f"✅ Completed '{kw}' in {elapsed:.1f}s")
            else:
                print(f"❌ Failed '{kw}' (Exit code {result.returncode})")
                
        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"❌ Error invoking script: {e}")
            
    print("\n✨ Batch regeneration complete.")

if __name__ == "__main__":
    main()
