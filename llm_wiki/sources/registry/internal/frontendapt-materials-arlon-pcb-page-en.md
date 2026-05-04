---
source_id: "frontendapt-materials-arlon-pcb-page-en"
title: "APTPCB English Arlon PCB Materials JSON - Detailed Polyimide & PTFE Specifications"
organization: "APTPCB"
source_type: "internal_material_page"
url: "/code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-05-03"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: true
topic_tags: ["internal", "aptpcb", "materials", "arlon", "polyimide", "ptfe", "rf", "33n", "35n", "clte-xt", "tc350", "recovery"]
status: "active"
notes: "Recovered Arlon polyimide and PTFE material specifications via internal JSON. Contains exact Dk/Df, thermal, mechanical properties for 33N, 35N, 45N, Thermount, CLTE-XT, TC350, AD250 series. Use with blocked-claims discipline."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json`

### Material Portfolio (8 Series)

| Series | Chemistry | Dk Range | Df (Typ.) | Key Characteristics |
|--------|-----------|----------|-----------|---------------------|
| **33N / 35N / 85N** | Polyimide Resin | 4.2-4.3 @ 1 MHz | 0.015 @ 1 MHz | Tg >250°C, standard desmear, highly hygroscopic (1.20% moisture) |
| **45N / 47N / 49N** | Multifunctional Epoxy | 4.3-4.4 @ 1 MHz | 0.015 @ 1 MHz | High-Tg 175-200°C, CAF resistant, standard PCB workflows |
| **Thermount (55NT/85NT)** | Polyimide / Aramid | 3.5-4.0 @ 1 MHz | 0.017 @ 1 MHz | Low CTE, lightweight, no glass-weave skew, specialized routing |
| **CLTE-XT / CLTE-AT** | PTFE / Ceramic / Glass | 2.94-3.00 @ 10 GHz | 0.0012 @ 10 GHz | Z-CTE matched to copper, plasma desmear required, low-PIM |
| **TC350 / TC600** | PTFE / Glass / Ceramic | 3.50-6.15 @ 10 GHz | 0.0020 @ 10 GHz | Thermally enhanced (1.0 W/m·K for TC350), plasma desmear |
| **AD250 / AD300 / AD1000** | PTFE / Glass / Ceramic | 2.50-10.2 @ 10 GHz | 0.0014 @ 10 GHz | Antenna-grade, extreme miniaturization, plasma desmear |
| **CuClad / DiClad / IsoClad** | PTFE / Glass | 2.17-2.60 @ 10 GHz | 0.0009 @ 10 GHz | Legacy ultra-low loss, plasma desmear, mature military programs |
| **37N / 38N / HF-50** | Bondply & Prepreg | - | - | Low-flow polyimide prepregs, microwave bondplys |

### Detailed Properties (Test Methods)

| Property | 33N (Polyimide) | 45N (Epoxy) | 55NT (Thermount) | CLTE-XT (PTFE) | TC350 (PTFE) | AD250 (PTFE) | Test Method |
|----------|-----------------|-------------|------------------|----------------|--------------|--------------|-------------|
| **Dk** | 4.20 @ 1 MHz | 4.30 @ 1 MHz | 3.50 @ 1 MHz | 2.94 @ 10 GHz | 3.50 @ 10 GHz | 2.50 @ 10 GHz | IPC-TM-650 |
| **Df** | 0.015 @ 1 MHz | 0.015 @ 1 MHz | 0.017 @ 1 MHz | 0.0012 @ 10 GHz | 0.0020 @ 10 GHz | 0.0014 @ 10 GHz | IPC-TM-650 |
| **Thermal Cond. (W/m·K)** | 0.20 | 0.25 | 0.15 | 0.45 | 1.00 | 0.22 | ASTM E1461 |
| **CTE X/Y (ppm/°C)** | 14 / 14 | 14 / 14 | 7 / 9 | 8 / 8 | 8 / 8 | 24 / 24 | IPC-TM-650 2.4.41 |
| **CTE Z (ppm/°C)** | 45 | 45 | 40 | 20 | 10 | 190 | IPC-TM-650 2.4.41 |
| **Moisture Absorption (%)** | 1.20 | 0.15 | 1.00 | 0.02 | 0.02 | 0.02 | IPC-TM-650 2.6.2.1 |
| **Peel Strength (lb/in)** | 8.0 | 9.0 | 6.0 | 8.0 | 8.0 | 12.0 | IPC-TM-650 2.4.8 |
| **Tg (°C, DSC)** | >250 | 175 | 260 | N/A (PTFE) | N/A (PTFE) | N/A (PTFE) | IPC-TM-650 2.4.25 |
| **Dielectric Strength (V/mil)** | 1200 | 1200 | 1000 | 600 | 600 | 800 | IPC-TM-650 2.5.6.2 |
| **Flammability (UL 94)** | V-0 | V-0 | V-0 | V-0 | V-0 | V-0 | UL 94 |
| **Plasma Desmear** | No | No | No | Yes | Yes | Yes | - |

### Critical Process Notes

**Polyimide (33N, 55NT)**:
- High moisture absorption (1.20%, 1.00%)
- **Mandatory pre-bake** before lamination and assembly
- Standard desmear chemistry (no plasma)

**PTFE Materials (CLTE, TC350, AD)**:
- Plasma desmear **required** for via metallization
- No meaningful Tg (PTFE-based)
- Very low moisture (0.02%)

### Stocked at APTPCB

- 33N: 10-60 mil, 1/2 oz and 1 oz ED copper
- 45N: 5-31 mil, 1/2 oz and 1 oz ED copper
- CLTE-XT: 10-60 mil, 1/2 oz and 1 oz ED copper

### Operating Temperature

- Polyimide series: −55°C to +260°C continuous

## Why It Matters

- **Recovery**: Recovers Arlon RF/PTFE and polyimide specifications while official Arlon product pages lack current datasheets for CLTE-XT, TC350, AD250, CuClad families
- **Internal validation**: APTPCB factory-validated processing recipes for all listed series
- **Dual chemistry**: Unique portfolio covering both high-temp polyimide (260°C) and low-loss PTFE (Df 0.0012)

## Extraction Notes

- ✅ Safe for material specifications (Dk, Df, thermal, mechanical)
- ✅ Safe for stocked thicknesses and copper cladding
- ✅ Safe for process requirements (plasma desmear, baking protocols)
- ✅ Safe for test methods (IPC-TM-650, ASTM E1461, UL 94)
- ⚠️ **BLOCKED**: Do not claim these are official Arlon/AGC-published datasheet values
- ⚠️ **BLOCKED**: Do not cite current Arlon availability or lead times
- ⚠️ **BLOCKED**: Do not use for external publication without pairing with source-gap card

## Refresh Notes

- **CRITICAL**: Refresh if/when official Arlon product pages or datasheets for CLTE-XT, TC350, AD series become available
- Verify current stock status at APTPCB before procurement references
- Confirm test method versions are current

## Blocked Claims

- Official Arlon/AGC datasheet authority for CLTE-XT, TC350, AD250/300/1000, CuClad/DiClad/IsoClad
- Current Arlon/AGC corporate status or product-line continuity for RF/PTFE families
- Real-time material availability or pricing
- Arlon factory-direct technical support channels
