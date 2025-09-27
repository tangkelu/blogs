import json
import re
from pathlib import Path
from typing import Dict, List

BASE_DIR = Path('prompts/blogs_prompt_v1')
KEYWORD_SOURCE = BASE_DIR / 'enhanced_pcb_keywords.md'

SECTION_PATTERN = re.compile(r'^##\s+(\d+)\.\s+(.*)')
SUBSECTION_PATTERN = re.compile(r'^###\s+(.*)')


def parse_keywords() -> Dict[str, Dict[str, List[str]]]:
    if not KEYWORD_SOURCE.exists():
        raise FileNotFoundError(f'Keyword source not found: {KEYWORD_SOURCE}')

    sections: Dict[str, Dict[str, List[str]]] = {}
    current_section_key: str | None = None
    current_subsection: str | None = None

    for line in KEYWORD_SOURCE.read_text(encoding='utf-8').splitlines():
        section_match = SECTION_PATTERN.match(line)
        if section_match:
            number = int(section_match.group(1))
            name = section_match.group(2).strip()
            key = f'{number:02d}'
            sections[key] = {
                '__meta__': {
                    'title': name,
                    'section_number': number,
                }
            }
            current_section_key = key
            current_subsection = None
            continue

        subsection_match = SUBSECTION_PATTERN.match(line)
        if subsection_match and current_section_key:
            subsection_name = subsection_match.group(1).strip()
            sections[current_section_key][subsection_name] = []
            current_subsection = subsection_name
            continue

        if current_section_key and current_subsection and line.strip():
            keywords = [kw.strip() for kw in line.split(',') if kw.strip()]
            sections[current_section_key][current_subsection].extend(keywords)

    return sections


def slugify(text: str) -> str:
    text = re.sub(r'[^A-Za-z0-9]+', '-', text)
    text = re.sub(r'-{2,}', '-', text)
    return text.strip('-')


def ensure_category_dirs(sections: Dict[str, Dict[str, List[str]]]):
    instruction_files = {}
    for md_file in BASE_DIR.glob('*-Instruction.md'):
        match = re.match(r'^(\d+)-(.*)-Instruction\.md$', md_file.name)
        if match:
            prefix = match.group(1)
            body = match.group(2)
            instruction_files[prefix] = {
                'path': md_file,
                'folder_name': f'{prefix}-{body}',
            }

    for key, data in sections.items():
        title = data['__meta__']['title']
        info = instruction_files.get(key)
        folder_name = info['folder_name'] if info else f'{key}-{slugify(title)}'
        category_dir = BASE_DIR / folder_name
        templates_dir = category_dir / 'templates'
        category_dir.mkdir(parents=True, exist_ok=True)
        templates_dir.mkdir(exist_ok=True)

        # Move instruction file to templates/primary.md
        if info:
            instruction_path = info['path']
            primary_template = templates_dir / 'primary.md'
            if instruction_path.exists() and not primary_template.exists():
                instruction_path.rename(primary_template)

        # Write keywords.json
        keywords_path = category_dir / 'keywords.json'
        if keywords_path.exists():
            old_content = json.loads(keywords_path.read_text(encoding='utf-8'))
        else:
            old_content = None

        payload = {
            'section_number': data['__meta__']['section_number'],
            'section_title': title,
            'subsections': [
                {
                    'name': subsection,
                    'keywords': keywords,
                }
                for subsection, keywords in data.items()
                if subsection != '__meta__'
            ],
        }

        if payload != old_content:
            keywords_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    sections = parse_keywords()
    ensure_category_dirs(sections)


if __name__ == '__main__':
    main()
