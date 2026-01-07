#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reset 'used' flags in prompts/blogs_prompt_v2/*/keywords.json and enrich with
manufacturing & assembly English keywords per category, keeping existing structure.
"""
import json
from pathlib import Path

BASE = Path('prompts/blogs_prompt_v2')

GLOBAL_SUBSECTIONS = {
    "Manufacturing & Assembly": [
        "Turnkey PCBA",
        "SMT assembly",
        "THT/through-hole soldering",
        "Selective wave soldering",
        "Low-void BGA reflow",
        "SPI/AOI/X-Ray inspection",
        "DFM/DFT/DFA review",
        "First Article Inspection (FAI)",
        "NPI EVT/DVT/PVT",
        "Fixture design (ICT/FCT)",
        "Flying probe test",
        "Boundary-Scan/JTAG",
        "Conformal coating",
        "Potting/encapsulation",
        "Traceability/MES"
    ],
    "Advanced PCB Process": [
        "HDI any-layer",
        "Microvia/stacked via",
        "Via-in-Pad plated over (VIPPO)",
        "Backdrill quality control",
        "Controlled impedance",
        "Heavy copper 3oz+",
        "Copper coin",
        "Copper pillar",
        "ENIG/ENEPIG/OSP",
        "Hybrid stack-up (Rogers+FR-4)",
        "Rigid-flex PCB",
        "Press-fit technology"
    ],
}

CATEGORY_EXTRAS = {
    '20-AI-Server-Backplane-PCB': {
        "High-Speed Backplane Manufacturing": [
            "PCIe Gen5/Gen6 controlled impedance",
            "CXL 3.0 retimer placement",
            "Backplane connector launch tuning",
            "Backdrill stub removal",
            "Low-loss materials (Megtron 6/7)",
            "Backplane rework & repair",
            "Low-void heatsink attach"
        ]
    },
    '21-AI-Chip-Interconnect-PCB': {
        "IC Substrate & Packaging": [
            "CoWoS substrate manufacturing",
            "ABF core materials",
            "RDL fan-out",
            "Microvia reliability",
            "SiP assembly",
            "Warpage control",
            "Underfill/flux selection"
        ]
    },
    '22-High-Speed-SI-PCB': {
        "Signal Integrity Readiness": [
            "112G/224G SerDes stack-up",
            "Weave effect mitigation",
            "Copper roughness control",
            "Backdrill verification",
            "Low-loss laminate sourcing",
            "Fixture de-embedding (TRL/LRM)"
        ]
    },
    '23-Power-Cooling-Systems-PCB': {
        "Power & Thermal": [
            "Heavy copper 2–6oz",
            "Thermal via arrays",
            "Press-fit terminals",
            "Cold plate/heatsink integration",
            "TIM selection & voiding control",
            "Power cycling reliability"
        ]
    },
    '24-Automotive-ADAS-EV-Power-PCB': {
        "Automotive Manufacturing": [
            "IATF 16949 PCBA",
            "PPAP/APQP documentation",
            "AEC-Q component sourcing",
            "CISPR 25/ISO 11452 EMC",
            "Conformal coating (acrylic/silicone)",
            "Potting polyurethane",
            "Full traceability (barcoding/MES)"
        ]
    },
    '25-5G-6G-Communication-PCB': {
        "RF & mmWave": [
            "Rogers/PTFE hybrid lamination",
            "CPWG/microstrip/stripline",
            "Via fence & cavity",
            "Backdrill for connectors",
            "Probe station de-embedding",
            "Antenna-in-Package (AiP) assembly"
        ]
    },
    '26-Data-Center-Optical-Module-PCB': {
        "Optical Module Manufacturing": [
            "QSFP-DD/OSFP cage & heatsink",
            "PAM4 equalization & SI",
            "CPO substrate & low CTE materials",
            "CTE match & warpage control",
            "CMIS/EEPROM programming",
            "Low-void thermal attach"
        ]
    },
    '27-Industrial-Robotics-Control-PCB': {
        "Industrial PCBA": [
            "EtherCAT/PROFINET magnetics",
            "Isolation creepage/clearance",
            "ICT/FCT fixture design",
            "Conformal coating IPC-CC-830",
            "ESD/EFT/Surge protection",
            "Functional safety diagnostics"
        ]
    },
    '28-Renewable-Energy-Inverter-PCB': {
        "Inverter Manufacturing": [
            "SiC/GaN gate driver layout",
            "Creepage ≥8mm high voltage",
            "LCL filter assembly",
            "Busbar crimping & terminals",
            "UL 1741/IEEE 1547 compliance",
            "Heavy copper soldering"
        ]
    },
    '29-Medical-Imaging-Wearable-PCB': {
        "Medical PCBA": [
            "ISO 13485 quality system",
            "IEC 60601 leakage/insulation",
            "Biocompatible materials (ISO 10993)",
            "Rigid-flex for wearables",
            "DHR/device history record",
            "Parylene coating"
        ]
    },
}


def ensure_subsection(data: dict, name: str):
    subs = data.setdefault('subsections', [])
    for s in subs:
        if s.get('name') == name:
            return s
    new = {'name': name, 'keywords': []}
    subs.append(new)
    return new


def add_keywords(subsection: dict, keywords: list):
    existing = {k.get('keyword', '').lower() for k in subsection.get('keywords', [])}
    for kw in keywords:
        if kw.lower() in existing:
            continue
        subsection.setdefault('keywords', []).append({'keyword': kw, 'used': False})


def process_file(path: Path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"Skip {path}: load error {e}")
        return

    # Reset all used flags and clean transient fields
    for subsection in data.get('subsections', []):
        for kw in subsection.get('keywords', []):
            # reset usage flags
            kw['used'] = False
            # remove transient fields accidentally persisted by generators
            for trash in ('subsection', 'template', 'usage_date', 'notes'):
                if trash in kw:
                    kw.pop(trash, None)

    # Reset template usage stats (optional, safer rotation)
    data['template_usage_stats'] = {}

    # Add global subsections
    for name, kws in GLOBAL_SUBSECTIONS.items():
        add_keywords(ensure_subsection(data, name), kws)

    # Add category specific extras
    category_dir = path.parent.parent.name  # e.g., '20-AI-Server-Backplane-PCB'
    extras = CATEGORY_EXTRAS.get(category_dir, {})
    for name, kws in extras.items():
        add_keywords(ensure_subsection(data, name), kws)

    # Save back
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Updated: {path}")


def main():
    for keywords_file in BASE.glob('*/keywords.json'):
        process_file(keywords_file)

if __name__ == '__main__':
    main()
