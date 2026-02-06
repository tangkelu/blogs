import re
import json
import random
import os

SITEMAP_PATH = r"d:\website\blogs\prompts_aptpcb\sitemap.xml"
MAP_FILE = r"d:\website\blogs\prompts_aptpcb\v6_content_map.md"
OUTPUT_JSON = r"d:\website\blogs\v6_upgrade_targets.json"

def main():
    # 1. Parse Sitemap for legacy slugs
    print(f"Reading sitemap: {SITEMAP_PATH}")
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
        
    # Regex to extract slugs from <loc>https://aptpcb.com/en/blog/{slug}</loc>
    slugs = set(re.findall(r'<loc>https://aptpcb.com/en/blog/([^<]+)</loc>', sitemap_content))
    print(f"Found {len(slugs)} legacy blog slugs in sitemap.")
    
    # 2. Parse Content Map to link Slugs -> Keywords & Categories
    print(f"Reading content map: {MAP_FILE}")
    with open(MAP_FILE, 'r', encoding='utf-8') as f:
        map_lines = f.readlines()
        
    # Map structure: | Category | Keyword | Expected Filename | Status |
    # We match slug == filename (without .md)
    
    targets = []
    
    intent_options = ["story", "playbook", "query"] # Weighted options could be better, but uniform is fine
    
    matched_count = 0
    
    for line in map_lines:
        line = line.strip()
        if not line.startswith("|") or "Category" in line or "---" in line:
            continue
            
        parts = line.split("|")
        if len(parts) < 5:
            continue
            
        category = parts[1].strip()
        keyword = parts[2].strip()
        filename = parts[3].strip().replace('`', '')
        
        # Expected filename is like "slug.md"
        file_slug = filename.replace(".md", "")
        
        if file_slug in slugs:
            matched_count += 1
            
            # Randomize intent
            # We assign intent to override keywords.json later
            intent = random.choice(intent_options)
            
            # Special case for "Cost" keywords -> maybe prioritize Playbook?
            # Special case for "Troubleshooting" -> Story
            if "troubleshoot" in keyword.lower() or "problem" in keyword.lower():
                intent = "story"
            elif "guide" in keyword.lower() or "checklist" in keyword.lower():
                intent = "playbook"
            elif "cost" in keyword.lower() or "price" in keyword.lower():
                 # Keep some random, but query works well for cost.
                 pass
            
            targets.append({
                "category": category,
                "keyword": keyword,
                "filename": filename,
                "intent": intent
            })
            
    print(f"Matched {matched_count} keywords from map that exist in sitemap.")
    
    # 3. Save to JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(targets, f, indent=2)
        
    print(f"Saved target list to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
