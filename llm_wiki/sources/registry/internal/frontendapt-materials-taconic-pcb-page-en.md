---
source_id: "frontendapt-materials-taconic-pcb-page-en"
title: "APTPCB English Taconic PCB Materials JSON - Detailed RF/PTFE Specifications"
organization: "APTPCB"
source_type: "internal_material_page"
url: "/code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-05-03"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: true
topic_tags: ["internal", "aptpcb", "materials", "taconic", "ptfe", "rf", "microwave", "tly", "tlx", "tlc", "rf-35", "cer-10", "fastrise", "recovery"]
status: "active"
notes: "Recovered Taconic RF/PTFE material specifications via internal JSON. Contains exact Dk/Df, thermal, mechanical properties for TLY, TLX, TLC, RF-35, CER-10, fastRise 27 series. Use with blocked-claims discipline."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json`

### Material Portfolio (8 Series)

| Series | Chemistry | Dk @ 10 GHz | Df @ 10 GHz | Key Characteristics |
|--------|-----------|-------------|-------------|---------------------|
| **TLY / TLY-5A** | PTFE / woven E-glass | 2.17 ±0.02 | 0.0009 | Lowest-loss Taconic laminate, plasma desmear required, 0.02% moisture |
| **TLX** | PTFE / woven E-glass | 2.55 ±0.04 | 0.0019 | Moderate-loss, compact microstrip geometries |
| **TLC** | PTFE / woven E-glass (economy) | 2.95-3.20 | 0.0020 | Cost-reduced PTFE entry point |
| **RF-30 / RF-35** | PTFE / ceramic filler | 3.50 ±0.05 | 0.0018 | Ceramic-filled, Df lower than Rogers RO4350B (0.0018 vs 0.0037), lead-free compatible |
| **CER-10** | PTFE / ceramic (high-Dk) | 10.0 ±0.25 | 0.0035 | Extreme miniaturization, DRA, compact filters |
| **fastRise 27** | Low-loss thermoset prepreg | 2.72 ±0.04 | 0.0014 | Hybrid bonding prepreg for PTFE/FR-4 multilayers |
| **TacLam** | Pure PTFE bonding film | 2.10-2.35 | 0.0008 | Ultra-low-loss, all-PTFE multilayer constructions |
| **TF-260 / TF-290** | PTFE / ceramic (thermal) | 2.60-2.90 | 0.0015-0.0020 | Thermally enhanced for power amplifiers |

### Detailed Properties (Test Methods)

| Property | TLY-5A | TLY-3 | TLX-8 | RF-35A2 | CER-10 | fastRise 27 | Test Method |
|----------|--------|-------|-------|---------|--------|-------------|-------------|
| **Dk @ 10 GHz** | 2.17 ±0.02 | 2.33 ±0.02 | 2.55 ±0.04 | 3.50 ±0.05 | 10.0 ±0.25 | 2.72 ±0.04 | IPC-TM-650 2.5.5.5 |
| **Df @ 10 GHz** | 0.0009 | 0.0009 | 0.0019 | 0.0018 | 0.0035 | 0.0014 | IPC-TM-650 2.5.5.5 |
| **Thermal Cond. (W/m·K)** | 0.23 | 0.26 | 0.26 | 0.62 | 0.42 | 0.28 | ASTM E1461 |
| **CTE X/Y (ppm/°C)** | 25 | 18 | 15 | 14 | 8 | 12 | IPC-TM-650 2.4.41 |
| **CTE Z (ppm/°C)** | 280 | 280 | 280 | 30 | 20 | 40 | IPC-TM-650 2.4.41 |
| **Moisture Absorption (%)** | 0.02 | 0.02 | 0.02 | 0.06 | 0.05 | 0.03 | IPC-TM-650 2.6.2.1 |
| **Peel Strength (lb/in)** | 6 | 8 | 8 | 8 | 5 | 6 | IPC-TM-650 2.4.8 |
| **Tg (°C, DSC)** | N/A (PTFE) | N/A (PTFE) | N/A (PTFE) | >280 | N/A (PTFE) | >250 | IPC-TM-650 2.4.25 |
| **Dielectric Strength (V/mil)** | 800 | 800 | 800 | 750 | 600 | 700 | IPC-TM-650 2.5.6.2 |
| **Flammability (UL 94)** | V-0 | V-0 | V-0 | V-0 | V-0 | V-0 | UL 94 |

### Stocked at APTPCB

- RF-35: 10-60 mil, 1/2 oz and 1 oz ED copper
- TLY-5A: 5-31 mil, 1/2 oz and 1 oz ED copper
- CER-10: 20-40 mil, 1/2 oz and 1 oz ED copper
- fastRise 27: Bonding prepreg

## Why It Matters

- **Recovery**: Recovers Taconic RF/PTFE specifications while official Taconic product pages are unavailable
- **Internal validation**: APTPCB factory-validated processing recipes for all listed series
- **Gap-filling**: Provides exact material parameters for TLY, TLX, TLC, RF-35, CER-10, fastRise families

## Extraction Notes

- ✅ Safe for material specifications (Dk, Df, thermal, mechanical)
- ✅ Safe for stocked thicknesses and copper cladding
- ✅ Safe for process requirements (plasma desmear, lamination profiles)
- ✅ Safe for test methods (IPC-TM-650, ASTM E1461, UL 94)
- ⚠️ **BLOCKED**: Do not claim these are official Taconic-published datasheet values
- ⚠️ **BLOCKED**: Do not cite current Taconic availability or lead times
- ⚠️ **BLOCKED**: Do not use for external publication without pairing with source-gap card

## Refresh Notes

- **CRITICAL**: Refresh if/when official Taconic product pages or datasheets become available
- Verify current stock status at APTPCB before procurement references
- Confirm test method versions are current

## Blocked Claims

- Official Taconic datasheet authority (current site shows industrial PTFE fabrics only)
- Current Taconic corporate status or product-line continuity
- Real-time material availability or pricing
- Taconic factory-direct technical support channels
