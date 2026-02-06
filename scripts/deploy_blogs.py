
import csv
import shutil
import os
from pathlib import Path

# Config
BLOGS_ROOT = Path("d:/website/blogs")
TRACKER_CSV = BLOGS_ROOT / "blog_tracker.csv"
V6_STAGING_DIR = BLOGS_ROOT / "blogs_aptpcb_v6_staging"
# Assuming standard deploy path.
FRONTEND_BLOGS_ROOT = Path("d:/website/hileap/frontendAPT/public/static/blogs/2025")

# Map of Month -> Folder Name (if needed, but structure suggests we just use whatever folder structure exists in staging?)
# Wait, staging structure is `blogs_aptpcb_v6_staging/0108/en/file.md`?
# Or does the generator put it in correct categories?
# Based on ls output: `blogs_aptpcb_v6_staging/0108` contains categories like `01`, `02` etc?
# Let's re-verify the staging structure. 
# Step 42 output showed `blogs_aptpcb_v6_staging/0108` has `01`, `02` dir... and `months_index.json`.
# AND Step 43 showed `blogs_aptpcb_v6_staging/0108/en` exists?
# The structure seems a bit mixed or I misread.
# Let's assume standard recursive search to find the source file in STAGING.

def find_source_file(filename):
    matches = list(V6_STAGING_DIR.rglob(filename))
    if matches:
        # Prefer the most recent one if duplicates? 
        return matches[0]
    return None

def main():
    with open(TRACKER_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    tasks = [r for r in rows if r["V6 Generated"] == "Yes" and (
        r["Deployed"] == "No" or 
        r["Only EN"] != "Yes" or 
        r["Status"] == "Needs Update"
    )]
    
    print(f"Found {len(tasks)} tasks needing deployment or cleanup.")
    
    deployed_count = 0
    cleaned_count = 0
    
    for i, task in enumerate(tasks):
        filename = task["Filename"]
        
        # 1. Find Source
        src_path = find_source_file(filename)
        if not src_path:
            print(f"❌ Source not found for {filename} (despite tracker saying Yes?)")
            continue
            
        # 2. Determine Destination
        # Check if it exists in frontend to preserve current month location.
        existing_matches = list(FRONTEND_BLOGS_ROOT.rglob(filename))
        
        dest_path = None
        
        # Prioritize finding an existing 'en' version
        en_matches = [p for p in existing_matches if p.parent.name == 'en']
        
        if en_matches:
            dest_path = en_matches[0]
        elif existing_matches:
            # Found matches but not in 'en' (e.g. only 'ar', 'de'...)
            # Use the directory of the first match to determine Month
            # e.g. .../2025/02/ar/file.md -> .../2025/02/en/file.md
            first_match = existing_matches[0]
            # Assumes structure .../Month/Lang/File
            month_dir = first_match.parent.parent
            dest_path = month_dir / "en" / filename
        else:
            # Default to 2025/12/en if no existing file found
            dest_path = FRONTEND_BLOGS_ROOT / "12/en" / filename
            
        # Ensure parent dir exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 3. Copy/Overwrite
        try:
            shutil.copy2(src_path, dest_path)
            # print(f"  -> Copied to {dest_path.relative_to(FRONTEND_BLOGS_ROOT)}")
            deployed_count += 1
        except Exception as e:
            print(f"❌ Copy failed for {filename}: {e}")
            continue
            
        # 4. Cleanup Siblings
        # Parent is `.../MM/en`. Grandparent `.../MM`.
        lang_dir = dest_path.parent
        # Should always be 'en' now due to above logic, but double check
        if lang_dir.name == 'en':
            month_dir = lang_dir.parent
            for child in month_dir.iterdir():
                if child.is_dir() and child.name != 'en':
                    # Check for file existence in other languages
                    sibling_file = child / filename
                    if sibling_file.exists():
                        try:
                            sibling_file.unlink()
                            print(f"  🗑️ Deleted {child.name}/{filename}")
                            cleaned_count += 1
                        except Exception as e:
                            print(f"❌ Delete failed: {e}")
                            
    print(f"\n✅ Deployed/Updated: {deployed_count} files.")
    print(f"✨ Cleaned non-en duplicates: {cleaned_count} files.")

if __name__ == "__main__":
    main()
