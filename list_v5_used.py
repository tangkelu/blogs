
import os
import json
from pathlib import Path

V5_DIR = Path("prompts_aptpcb/blogs_prompt_v5")
# Adjust path to where I am running this, simplified for now assuming running from d:\website\blogs
# But actually I will run this via python tool so CWD is likely the workspace root?
# No, run_command Cwd arg. I'll assume d:\website\blogs is the CWD.

def find_used_keywords():
    used_keywords = []
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
                                        used_keywords.append(kw_obj["keyword"])
            except Exception as e:
                print(f"Error reading {json_path}: {e}")
    return used_keywords

if __name__ == "__main__":
    kws = find_used_keywords()
    print(json.dumps(kws, indent=2))
    print(f"Total used keywords in v5: {len(kws)}")
