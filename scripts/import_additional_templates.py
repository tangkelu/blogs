import shutil
from pathlib import Path
import re

BASE_V1 = Path('prompts/blogs_prompt_v1')
V2_DIR = Path('prompts/blogs_prompt_v2')
V3_DIR = Path('prompts/blogs_prompt_v3')

V2_MAPPING = {
    'datacenter-server': '01-DataCenter-ServerPCB',
    '5g-telecom': '02-5G-Telecom-PCB',
    'automotive-pcb': '03-Automotive-PCB',
    'consumer-electronics': '04-Consumer-Electronics-PCB',
    'industrial-automation': '05-Industrial-Automation-PCB',
    'led-lighting': '06-LED-Lighting-PCB',
    'power-energy': '07-Power-Energy-PCB',
    'medical-equipment': '08-Medical-Equipment-PCB',
    'iot-wireless': '09-IoT-Wireless-PCB',
    'security-surveillance': '10-Security-Surveillance-PCB',
    'aerospace-defense': '11-Aerospace-Defense-PCB',
    'test-measurement': '12-Test-Measurement-PCB',
    'smart-home': '13-SmartHome-Building-PCB',
    'audio-entertainment': '14-Audio-Entertainment-PCB',
    'display-technology': '15-Display-Technology-PCB',
    'environmental-monitoring': '16-Environmental-Monitoring-PCB',
    'transportation': '17-Transportation-PCB',
    'retail-commerce': '18-Retail-Commerce-PCB',
    'drone-uav': '19-Drone-UAV-PCB',
}

V3_MAPPING = {
    f'optimized_pcb_instruction_{i:02d}.md': f'{i:02d}-{name}'
    for i, name in enumerate([
        'DataCenter-ServerPCB',
        '5G-Telecom-PCB',
        'Automotive-PCB',
        'Consumer-Electronics-PCB',
        'Industrial-Automation-PCB',
        'LED-Lighting-PCB',
        'Power-Energy-PCB',
        'Medical-Equipment-PCB',
        'IoT-Wireless-PCB',
        'Security-Surveillance-PCB',
        'Aerospace-Defense-PCB',
        'Test-Measurement-PCB',
        'SmartHome-Building-PCB',
        'Audio-Entertainment-PCB',
        'Display-Technology-PCB',
        'Environmental-Monitoring-PCB',
        'Transportation-PCB',
        'Retail-Commerce-PCB',
        'Drone-UAV-PCB',
    ], start=1)
}


def slugify(text: str) -> str:
    text = re.sub(r'[^A-Za-z0-9]+', '-', text)
    text = re.sub(r'-{2,}', '-', text)
    return text.strip('-').lower()


def copy_template(src: Path, dest_dir: Path, prefix: str) -> str:
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)

    content = src.read_text(encoding='utf-8')
    slug = slugify(src.stem)
    candidate = dest_dir / f'{prefix}-{slug}.md'
    counter = 1

    while candidate.exists():
        if candidate.read_text(encoding='utf-8') == content:
            return 'skipped-exists'
        counter += 1
        candidate = dest_dir / f'{prefix}-{slug}-{counter}.md'

    candidate.write_text(content, encoding='utf-8')
    return 'copied'


def normalize_v2_key(stem: str) -> str:
    key = stem
    key = key.replace('_pcb_instruction', '')
    key = key.replace('-pcb_instruction', '')
    key = key.replace('_complete', '')
    key = key.replace('-complete', '')
    key = key.replace('_', '-')
    return key


def import_v2_templates() -> list[tuple[str, str, str]]:
    results = []
    for path in sorted(V2_DIR.glob('*.md')):
        base = path.stem
        target_key = V2_MAPPING.get(normalize_v2_key(base))
        if not target_key:
            results.append(('v2', str(path), 'unmapped'))
            continue
        dest_dir = BASE_V1 / target_key / 'templates'
        status = copy_template(path, dest_dir, 'v2')
        results.append(('v2', str(path), status))
    return results


def import_v3_templates() -> list[tuple[str, str, str]]:
    results = []
    for path in sorted(V3_DIR.glob('*.md')):
        target_key = V3_MAPPING.get(path.name)
        if not target_key:
            results.append(('v3', str(path), 'unmapped'))
            continue
        dest_dir = BASE_V1 / target_key / 'templates'
        status = copy_template(path, dest_dir, 'v3')
        results.append(('v3', str(path), status))
    return results


def main():
    results = import_v2_templates() + import_v3_templates()
    summary = {}
    for source, path, status in results:
        summary.setdefault(status, 0)
        summary[status] += 1
        print(f"[{source}] {path} -> {status}")
    print("\nSummary:")
    for status, count in summary.items():
        print(f"  {status}: {count}")


if __name__ == '__main__':
    main()
