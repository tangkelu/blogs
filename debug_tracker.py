
import csv
from pathlib import Path

csv_path = Path("d:/website/blogs/blog_tracker.csv")

try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if "aes-ebu-pcb" in row["Filename"] or "aes-ebu-pcb" in row["Keyword"]:
                print(f"FOUND ROW: {row}")
                found = True
        
        if not found:
            print("NOT FOUND in CSV.")
            
except Exception as e:
    print(f"Error: {e}")
