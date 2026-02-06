
import csv
import sys
import subprocess
import time
import argparse
from pathlib import Path

# Config
BLOGS_ROOT = Path("d:/website/blogs")
TRACKER_CSV = BLOGS_ROOT / "blog_tracker.csv"
RUN_SCRIPT = "run_v6_generation.py"

def read_tracker():
    with open(TRACKER_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    parser = argparse.ArgumentParser(description="Drive automated blog generation based on tracker.")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of blogs to generate in this run.")
    parser.add_argument("--random-template", action="store_true", help="Randomly select a template kind for each blog.")
    args = parser.parse_args()

    rows = read_tracker()
    
    # Filter for items that need generation
    tasks = [r for r in rows if r["V6 Generated"] == "No" and r["Status"] != "Missing in V6 Map"]
    
    print(f"Found {len(tasks)} tasks needing generation.")
    
    if not tasks:
        print("Nothing to run.")
        return

    # Apply Limit
    if args.limit and args.limit > 0:
        print(f"⚠️ Limit set to {args.limit}. processing first {args.limit} tasks only.")
        tasks = tasks[:args.limit]
    
    for i, task in enumerate(tasks):
        kw = task["Keyword"]
        print(f"\n[{i+1}/{len(tasks)}] Generating: {kw}")
        
        cmd = [sys.executable, "-u", RUN_SCRIPT, "--keyword", kw]
        if args.random_template:
            cmd.append("--random-template")
        
        try:
            start_time = time.time()
            result = subprocess.run(cmd, check=False) # Let it print to stdout
            elapsed = time.time() - start_time
            
            if result.returncode == 0:
                print(f"✅ Generated '{kw}' in {elapsed:.1f}s")
            else:
                print(f"❌ Failed '{kw}' (Exit code {result.returncode})")
                
        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            
    # After run, regenerate the tracker
    print("\n🔄 Updating tracker...")
    subprocess.run([sys.executable, "scripts/generate_tracker.py"], check=False)
    print("Done.")

if __name__ == "__main__":
    main()
