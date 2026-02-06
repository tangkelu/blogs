#!/usr/bin/env python3
import os
import re
from pathlib import Path

base_dir = r'd:\website\blogs\blogs\1119-1-ccc'
languages = ['cn', 'ru', 'fr', 'it', 'de', 'en']

# Get all markdown files from cn directory
cn_dir = os.path.join(base_dir, 'cn')
cn_files = sorted([f for f in os.listdir(cn_dir) if f.endswith('.md')])

print("File Comparison: Lines and H2 Count")
print("=" * 100)

for filename in cn_files:
    cn_path = os.path.join(cn_dir, filename)
    
    # Read CN file
    with open(cn_path, 'r', encoding='utf-8') as f:
        cn_content = f.read()
    
    cn_lines = len(cn_content.split('\n'))
    cn_h2s = len(re.findall(r'^## ', cn_content, re.MULTILINE))
    
    print(f"\n{filename}")
    print(f"  CN: {cn_lines} lines, {cn_h2s} H2s")
    
    # Compare with other languages
    for lang in ['ru', 'fr', 'it', 'de', 'en']:
        lang_path = os.path.join(base_dir, lang, filename)
        if os.path.exists(lang_path):
            with open(lang_path, 'r', encoding='utf-8') as f:
                lang_content = f.read()
            
            lang_lines = len(lang_content.split('\n'))
            lang_h2s = len(re.findall(r'^## ', lang_content, re.MULTILINE))
            
            diff = abs(lang_lines - cn_lines)
            h2_match = "✓" if lang_h2s == cn_h2s else "✗"
            status = "OK" if diff <= 5 and lang_h2s == cn_h2s else "TRUNCATED"
            
            print(f"  {lang.upper()}: {lang_lines} lines, {lang_h2s} H2s {h2_match} | Diff: {diff} | {status}")
