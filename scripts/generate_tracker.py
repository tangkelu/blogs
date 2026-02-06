
import os
import json
import csv
import re
from pathlib import Path

# Config
BLOGS_ROOT = Path("d:/website/blogs")
V5_DIR = BLOGS_ROOT / "prompts_aptpcb/blogs_prompt_v5"
V6_MAP_FILE = BLOGS_ROOT / "prompts_aptpcb/v6_content_map.md"
V6_STAGING_DIR = BLOGS_ROOT / "blogs_aptpcb_v6_staging"
FRONTEND_BLOGS_DIR = Path("d:/website/hileap/frontendAPT/public/static/blogs/2025")

TRACKER_CSV = BLOGS_ROOT / "blog_tracker.csv"
TRACKER_MD = BLOGS_ROOT / "blog_tracker.md"

def get_v5_used_keywords():
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

def parse_v6_map():
    """Returns dict: keyword -> {category, filename}"""
    mapping = {}
    if not V6_MAP_FILE.exists():
        print(f"Error: map file {V6_MAP_FILE} not found")
        return {}
        
    content = V6_MAP_FILE.read_text(encoding='utf-8')
    # Row format: | Category | Keyword | Filename | ...
    for line in content.splitlines():
        if "|" in line and "---" not in line and "Category" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4:
                cat = parts[1]
                kw = parts[2]
                fname = parts[3].replace('`', '')
                if kw:
                    mapping[kw.lower()] = {
                        "category": cat,
                        "keyword": kw, # maintain original case if needed, but key is lower
                        "filename": fname
                    }
    return mapping

def check_v6_generated(filename):
    # Determine which month folder it would be in? 
    # Actually, the staging dir structure is `0108/en/filename.md` ?
    # Or just recursive search in V6_STAGING_DIR
    # Based on previous ls, it looks like `blogs_aptpcb_v6_staging/0108/en/...`
    # But usually these are organized by month/date. 
    # Let's simple search for the filename in the staging dir recursively.
    
    found_paths = list(V6_STAGING_DIR.rglob(filename))
    return len(found_paths) > 0

def check_deployment(filename):
    # Frontend structure: public/static/blogs/2025/MM/en/filename.md
    # We need to search `public/static/blogs/2025` recursively
    
    found_paths = list(FRONTEND_BLOGS_DIR.rglob(filename))
    
    is_deployed = False
    only_en = True # Assumed true unless we find non-en siblings
    
    if found_paths:
        is_deployed = True
        # Check siblings for the first found path
        # If path is .../12/en/file.md
        # Parent is .../12/en
        # Grandparent is .../12
        # We check grandparent for other folders
        
        # However, there might be multiple deployments? Let's assume one unique location for now.
        file_path = found_paths[0]
        lang_dir = file_path.parent # 'en'
        month_dir = lang_dir.parent # '12'
        
        if month_dir.exists():
            for child in month_dir.iterdir():
                if child.is_dir() and child.name != 'en':
                    # Check if this language folder ALSO contains the file
                    if (child / filename).exists():
                        only_en = False
                        break
    else:
        only_en = None # Not applicable if not deployed
        
    return is_deployed, only_en

def main():
    print("Gathering data...")
    v5_kws = get_v5_used_keywords()
    v6_map = parse_v6_map()
    
    print(f"Found {len(v5_kws)} used keywords in v5.")
    
    rows = []
    
    rows = []
    
    # Track which keywords we've processed to avoid duplicates
    processed_keywords = set()

    # 1. Process V5 Used Keywords
    for kw in v5_kws:
        kw_lower = kw.lower()
        processed_keywords.add(kw_lower)
        
        record = {
            "Keyword": kw,
            "Category": "Unknown",
            "Filename": "Unknown",
            "V6 Generated": "No",
            "Deployed": "No",
            "Only EN": "N/A",
            "Status": "Pending Generation"
        }
        
        if kw_lower in v6_map:
            info = v6_map[kw_lower]
            record["Category"] = info["category"]
            record["Filename"] = info["filename"]
            
            # Check Generation
            is_generated = check_v6_generated(info["filename"])
            record["V6 Generated"] = "Yes" if is_generated else "No"
            
            # Check Deployment
            is_deployed, only_en = check_deployment(info["filename"])
            record["Deployed"] = "Yes" if is_deployed else "No"
            
            if is_deployed:
                record["Only EN"] = "Yes" if only_en else "NO (Cleanup Req)"
                
            # Determine Action
            if not is_generated:
                record["Status"] = "Needs Gen"
            elif not is_deployed:
                record["Status"] = "Needs Deploy"
            elif not only_en:
                record["Status"] = "Needs Cleanup"
            else:
                # Deployed and Only EN. Check if content matches.
                try:
                    staging_paths = list(V6_STAGING_DIR.rglob(info["filename"]))
                    deployed_paths = list(FRONTEND_BLOGS_DIR.rglob(info["filename"]))
                    
                    if staging_paths and deployed_paths:
                        staging_path = staging_paths[0]
                        deployed_path = deployed_paths[0]
                        
                        # Compare content
                        s_content = staging_path.read_text(encoding='utf-8', errors='ignore')
                        d_content = deployed_path.read_text(encoding='utf-8', errors='ignore')
                        
                        # Normalize line endings just in case
                        if s_content.replace('\r\n', '\n').strip() != d_content.replace('\r\n', '\n').strip():
                            record["Status"] = "Needs Update"
                        else:
                            record["Status"] = "Done"
                    else:
                        # Should not happen given logic above
                        record["Status"] = "Done" 
                except Exception as e:
                    # On error, default to Needs Update to be safe? Or log?
                    print(f"Error comparing content for {info['filename']}: {e}")
                    record["Status"] = "Needs Update"

        else:
             record["Status"] = "Missing in V6 Map"
             
        rows.append(record)

    # 2. Process V6 Map items that exist in Staging but were NOT in V5 Used
    # This covers `small batch pcb fabrication` which is used: false but generated.
    for kw_lower, info in v6_map.items():
        if kw_lower in processed_keywords:
            continue
            
        # Only add if it is actually generated/staging exists
        # We don't want to add all 1000 items from map if they aren't generated and not requested.
        filename = info["filename"]
        if check_v6_generated(filename):
            record = {
                "Keyword": info["keyword"], # Use original casing from map
                "Category": info["category"],
                "Filename": filename,
                "V6 Generated": "Yes",
                "Deployed": "No",
                "Only EN": "N/A",
                "Status": "Unknown"
            }
            
            # Check Deployment
            is_deployed, only_en = check_deployment(filename)
            record["Deployed"] = "Yes" if is_deployed else "No"
            
            if is_deployed:
                record["Only EN"] = "Yes" if only_en else "NO (Cleanup Req)"
            
            # Determine Action
            if not is_deployed:
                record["Status"] = "Needs Deploy"
            elif not only_en:
                record["Status"] = "Needs Cleanup"
            else:
                 # Check content match
                try:
                    staging_paths = list(V6_STAGING_DIR.rglob(filename))
                    deployed_paths = list(FRONTEND_BLOGS_DIR.rglob(filename))
                    
                    if staging_paths and deployed_paths:
                        s_content = staging_paths[0].read_text(encoding='utf-8', errors='ignore')
                        d_content = deployed_paths[0].read_text(encoding='utf-8', errors='ignore')
                        if s_content.replace('\r\n', '\n').strip() != d_content.replace('\r\n', '\n').strip():
                            record["Status"] = "Needs Update"
                        else:
                            record["Status"] = "Done"
                    else:
                         record["Status"] = "Done"
                except:
                     record["Status"] = "Needs Update"

            rows.append(record)

    # 3. Process ORPHAN files in Staging (Generated but not in V5 Used or V6 Map)
    processed_filenames = {r["Filename"] for r in rows}
    
    generated_files = list(V6_STAGING_DIR.rglob("*.md"))
    print(f"DEBUG: Scanning {len(generated_files)} staged files for orphans...")
    
    for file_path in generated_files:
        filename = file_path.name
        
        if filename == "aes-ebu-pcb.md":
             print(f"DEBUG: Found aes-ebu-pcb.md. In processed? {filename in processed_filenames}")

        if filename in processed_filenames:
            continue
            
        # It's an orphan file!
        print(f"DEBUG: Adding orphan {filename}")
        record = {
            "Keyword": "(Orphan File)", 
            "Category": file_path.parent.parent.name, 
            "Filename": filename,
            "V6 Generated": "Yes",
            "Deployed": "No",
            "Only EN": "N/A",
            "Status": "Unknown"
        }
        
        # Try to infer category from v5 if possible, or just leave as Unknown
        record["Category"] = "Orphan/Unknown"

        # Check Deployment
        is_deployed, only_en = check_deployment(filename)
        record["Deployed"] = "Yes" if is_deployed else "No"
        
        if is_deployed:
            record["Only EN"] = "Yes" if only_en else "NO (Cleanup Req)"
        
        # Determine Action
        if not is_deployed:
            record["Status"] = "Needs Deploy"
        elif not only_en:
            record["Status"] = "Needs Cleanup"
        else:
             # Check content match
            try:
                deployed_paths = list(FRONTEND_BLOGS_DIR.rglob(filename))
                if deployed_paths:
                    s_content = file_path.read_text(encoding='utf-8', errors='ignore')
                    d_content = deployed_paths[0].read_text(encoding='utf-8', errors='ignore')
                    if s_content.replace('\r\n', '\n').strip() != d_content.replace('\r\n', '\n').strip():
                        record["Status"] = "Needs Update"
                    else:
                        record["Status"] = "Done"
                else:
                     record["Status"] = "Needs Deploy" # Should be covered above
            except:
                 record["Status"] = "Needs Update"

        rows.append(record)
        processed_filenames.add(filename)

    # Write CSV
    headers = ["Category", "Keyword", "Filename", "V6 Generated", "Deployed", "Only EN", "Status"]
    with open(TRACKER_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    # Write MD (Status Table)
    with open(TRACKER_MD, 'w', encoding='utf-8') as f:
        f.write("# Blog Status Tracker\n\n")
        f.write("| " + " | ".join(headers) + " |\n")
        f.write("| " + " | ".join(["---"] * len(headers)) + " |\n")
        for row in rows:
            line = f"| {row['Category']} | {row['Keyword']} | {row['Filename']} | {row['V6 Generated']} | {row['Deployed']} | {row['Only EN']} | {row['Status']} |"
            f.write(line + "\n")
            
    print(f"✅ Tracker generated at {TRACKER_CSV}")
    print(f"✅ Markdown report at {TRACKER_MD}")
    
    # 3. Print Progress Summary
    stats = {}
    total = len(rows)
    for r in rows:
        s = r["Status"]
        stats[s] = stats.get(s, 0) + 1
        
    print("\n" + "="*40)
    print(f"📊 Progress Summary (Total: {total})")
    print("="*40)
    
    # Define order for display
    display_order = ["Done", "Needs Gen", "Needs Deploy", "Needs Cleanup", "Needs Update", "Missing in V6 Map", "Pending Generation"]
    
    for status in display_order:
        if status in stats:
            count = stats[status]
            pct = (count / total) * 100 if total > 0 else 0
            if status == "Done":
                icon = "✅"
            elif status == "Needs Gen":
                icon = "⏳"
            elif status in ["Needs Deploy", "Needs Cleanup", "Needs Update"]:
                icon = "🚧"
            else:
                icon = "⚠️"
            
            print(f"{icon} {status:<20}: {count:>4} ({pct:>5.1f}%)")
            
    # Print any others not in expected list
    for s, c in stats.items():
        if s not in display_order:
            print(f"❓ {s:<20}: {c:>4}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
