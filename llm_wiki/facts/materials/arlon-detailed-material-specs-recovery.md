---
fact_id: "materials-arlon-detailed-material-specs-recovery"
title: "Arlon polyimide and PTFE material specifications recovered via APTPCB internal JSON: 33N (Tg>250°C, Dk 4.20/Df 0.015), CLTE-XT (Dk 2.94/Df 0.0012), TC350 (1.0 W/m·K), AD250 (Dk 2.50/Df 0.0014)"
topic: "Arlon polyimide and RF laminate material specifications - internal recovery"
category: "materials"
status: "recovered"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-materials-arlon-pcb-page-en"
tags: ["arlon", "polyimide", "ptfe", "rf", "33n", "35n", "clte-xt", "tc350", "ad250", "recovery", "internal-source"]
---

# Canonical Summary

> Arlon polyimide and PTFE material specifications have been **RECOVERED** via APTPCB internal JSON source. This fact card extracts exact Dk/Df, thermal, and mechanical properties for 8 Arlon series (polyimide, epoxy, Thermount, PTFE) while maintaining blocked-claims discipline due to absence of official Arlon-controlled datasheets for CLTE-XT, TC350, AD250, CuClad families.

## Recovery Status: ⚠️ INTERNAL-ONLY for RF/PTFE Families

| Series | Chemistry | Recovery Source | Official Source Status | Use Constraint |
|--------|-----------|-----------------|------------------------|----------------|
| **33N / 35N / 85N** | Polyimide | APTPCB internal JSON | ✅ Official Arlon product pages exist | Standard use |
| **45N / 47N / 49N** | Epoxy | APTPCB internal JSON | ✅ Official Arlon product pages exist | Standard use |
| **Thermount 55NT/85NT** | Polyimide/Aramid | APTPCB internal JSON | ⚠️ Limited official info | Internal preferred |
| **CLTE-XT / CLTE-AT** | PTFE/Ceramic | APTPCB internal JSON | ❌ No current Arlon datasheet | Internal only |
| **TC350 / TC600** | PTFE/Ceramic | APTPCB internal JSON | ❌ No current Arlon datasheet | Internal only |
| **AD250 / AD300 / AD1000** | PTFE/Ceramic | APTPCB internal JSON | ❌ No current Arlon datasheet | Internal only |
| **CuClad / DiClad / IsoClad** | PTFE/Glass | APTPCB internal JSON | ❌ No current Arlon datasheet | Internal only |
| **37N / 38N / HF-50** | Bondply | APTPCB internal JSON | ⚠️ Limited official info | Internal preferred |

## Stable Facts (Internal Recovery)

### Polyimide Series - 33N / 35N / 85N (High-Temperature)

| Property | 33N Value | Test Method |
|----------|-----------|-------------|
| Dk @ 1 MHz | 4.20 | IPC-TM-650 |
| Df @ 1 MHz | 0.015 | IPC-TM-650 |
| Thermal Conductivity | 0.20 W/m·K | ASTM E1461 |
| CTE X/Y | 14 / 14 ppm/°C | IPC-TM-650 2.4.41 |
| CTE Z | 45 ppm/°C | IPC-TM-650 2.4.41 |
| Moisture Absorption | 1.20% | IPC-TM-650 2.6.2.1 |
| Peel Strength | 8.0 lb/in | IPC-TM-650 2.4.8 |
| Tg (DSC) | >250°C | IPC-TM-650 2.4.25 |
| Dielectric Strength | 1200 V/mil | IPC-TM-650 2.5.6.2 |
| Flammability | V-0 | UL 94 |
| Plasma Desmear | No (Standard) | - |

**Key Characteristics**: Industry benchmark for extreme temperature survival, Tg >250°C, standard desmear, **highly hygroscopic (1.20%)**, mandatory pre-bake required

**Operating Temperature**: −55°C to +260°C continuous

**Applications**: Commercial/military avionics, downhole drilling (MWD/LWD) boards, extreme-temp burn-in boards, engine control modules

### Epoxy Series - 45N / 47N / 49N (High-Reliability)

| Property | 45N Value |
|----------|-----------|
| Dk @ 1 MHz | 4.30 |
| Df @ 1 MHz | 0.015 |
| Thermal Conductivity | 0.25 W/m·K |
| CTE X/Y | 14 / 14 ppm/°C |
| CTE Z | 45 ppm/°C |
| Moisture Absorption | 0.15% |
| Peel Strength | 9.0 lb/in |
| Tg (DSC) | 175°C |
| Dielectric Strength | 1200 V/mil |
| Flammability | V-0 |
| Plasma Desmear | No (Standard) |

**Key Characteristics**: High-Tg 175-200°C, excellent CAF resistance, lead-free compatible, standard PCB workflows

**Applications**: High-layer-count digital backplanes, military/commercial aerospace communications, demanding industrial controls

### Thermount Series - 55NT / 85NT (Aramid-Reinforced)

| Property | 55NT Value |
|----------|------------|
| Dk @ 1 MHz | 3.50 |
| Df @ 1 MHz | 0.017 |
| Thermal Conductivity | 0.15 W/m·K |
| CTE X/Y | 7 / 9 ppm/°C |
| CTE Z | 40 ppm/°C |
| Moisture Absorption | 1.00% |
| Peel Strength | 6.0 lb/in |
| Tg (DSC) | 260°C |
| Dielectric Strength | 1000 V/mil |
| Flammability | V-0 |
| Plasma Desmear | No (Standard) |

**Key Characteristics**: Non-woven aramid reinforcement (no glass-weave skew), very low in-plane CTE, significantly lighter, specialized routing/drilling required

**Applications**: Surface mount military boards with ceramic LCC packages, space-constrained avionics, dense multilayer designs

### CLTE-XT / CLTE-AT Series (PTFE Microwave - RECOVERED)

| Property | CLTE-XT Value |
|----------|---------------|
| Dk @ 10 GHz | 2.94 |
| Df @ 10 GHz | 0.0012 |
| Thermal Conductivity | 0.45 W/m·K |
| CTE X/Y | 8 / 8 ppm/°C |
| CTE Z | 20 ppm/°C |
| Moisture Absorption | 0.02% |
| Peel Strength | 8.0 lb/in |
| Tg | N/A (PTFE) |
| Dielectric Strength | 600 V/mil |
| Flammability | V-0 |
| Plasma Desmear | **Yes (Required)** |

**Key Characteristics**: Z-CTE **perfectly matched to copper** for superior PTH reliability in multilayer RF boards, extremely low loss, phase stable

**Applications**: Phased-array radar antennas, low-PIM cellular base station feeds, collision avoidance radar, space communications

### TC350 / TC600 Series (Thermally Enhanced - RECOVERED)

| Property | TC350 Value |
|----------|-------------|
| Dk @ 10 GHz | 3.50 |
| Df @ 10 GHz | 0.0020 |
| Thermal Conductivity | **1.00 W/m·K** |
| CTE X/Y | 8 / 8 ppm/°C |
| CTE Z | 10 ppm/°C |
| Moisture Absorption | 0.02% |
| Peel Strength | 8.0 lb/in |
| Tg | N/A (PTFE) |
| Dielectric Strength | 600 V/mil |
| Flammability | V-0 |
| Plasma Desmear | **Yes (Required)** |

**Key Characteristics**: **Exceptional thermal conductivity (1.0 W/m·K)** to pull heat away from active RF components, maintains stable Dk and low loss

**Applications**: High-power amplifiers (PA), tower-mounted amplifiers (TMA), GaN and GaAs device mounting, broadcast transmitters

### AD250 / AD300 / AD1000 Series (Antenna-Grade - RECOVERED)

| Property | AD250 Value | AD1000 Value |
|----------|-------------|--------------|
| Dk @ 10 GHz | 2.50 | 10.2 |
| Df @ 10 GHz | 0.0014 | 0.0014 |
| Thermal Conductivity | 0.22 W/m·K | - |
| CTE X/Y | 24 / 24 ppm/°C | - |
| CTE Z | 190 ppm/°C | - |
| Moisture Absorption | 0.02% | - |
| Peel Strength | 12.0 lb/in | - |
| Tg | N/A (PTFE) | N/A (PTFE) |
| Dielectric Strength | 800 V/mil | - |
| Flammability | V-0 | V-0 |
| Plasma Desmear | **Yes (Required)** | **Yes (Required)** |

**Key Characteristics**: Wide Dk range (2.50-10.2) for antenna design flexibility, extreme miniaturization with AD1000

**Applications**: GPS/GNSS patch antennas, dielectric resonator antennas (DRA), miniaturized filters, broadband base station antennas

### CuClad / DiClad / IsoClad Series (Legacy Ultra-Low Loss - RECOVERED)

| Property | Value |
|----------|-------|
| Dk @ 10 GHz | 2.17-2.60 |
| Df @ 10 GHz | 0.0009 |
| Key Characteristics | Legacy PTFE materials, absolute lowest dielectric loss |
| Plasma Desmear | **Yes (Required)** |
| Applications | Legacy military radar, EW receivers, low-loss stripline networks, VNA test fixtures |

## Stocked at APTPCB (Internal)

| Series | Thickness | Copper |
|--------|-----------|--------|
| 33N | 10-60 mil | 1/2 oz, 1 oz ED |
| 45N | 5-31 mil | 1/2 oz, 1 oz ED |
| CLTE-XT | 10-60 mil | 1/2 oz, 1 oz ED |

## Critical Process Requirements

### Polyimide (33N, 55NT) - MANDATORY PRE-BAKE
- High moisture absorption (1.20%, 1.00%)
- **Strict pre-bake required** before lamination and assembly
- Standard desmear chemistry (no plasma)

### PTFE Materials (CLTE, TC350, AD, CuClad) - PLASMA REQUIRED
- Plasma desmear **required** for via metallization
- No meaningful Tg (PTFE-based)
- Very low moisture (0.02%)

## Conditions And Methods

- Use 33N/35N/45N/47N data for standard material comparison (official Arlon pages exist)
- Use Thermount, CLTE-XT, TC350, AD250, CuClad data for **internal stackup planning only**
- Pair with `arlon-official-source-coverage.md` when citing externally
- All RF/PTFE values sourced from APTPCB internal JSON, not official Arlon datasheets
- Test methods are cited per internal source

## Limits And Non-Claims

- ❌ **NOT** official Arlon/AGC-published datasheet values for CLTE-XT, TC350, AD series, CuClad/DiClad/IsoClad
- ❌ Does not establish current Arlon product availability for RF/PTFE families
- ❌ Does not validate Arlon RF/PTFE product-line continuity
- ❌ Not for external publication of CLTE-XT, TC350, AD, CuClad data without explicit source-gap pairing
- ❌ Does not replace need for official Arlon-controlled source discovery for RF/PTFE families

## Open Questions

- When will official Arlon/AGC product pages or datasheets for CLTE-XT, TC350, AD250/300/1000 become available?
- Is Arlon/AGC still actively supporting RF/PTFE laminate production under these brand names?
- Should Thermount, CuClad, DiClad, IsoClad be treated as active or legacy product lines?

## Source Links

- Internal: `/code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json`
- Source Record: `sources/registry/internal/frontendapt-materials-arlon-pcb-page-en.md`
- Official Arlon: https://www.arlonemd.com/arlon-products/
