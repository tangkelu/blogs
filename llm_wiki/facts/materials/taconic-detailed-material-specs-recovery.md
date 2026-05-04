---
fact_id: "materials-taconic-detailed-material-specs-recovery"
title: "Taconic RF/PTFE material specifications recovered via APTPCB internal JSON: TLY-5A (Dk 2.17/Df 0.0009), TLX (Dk 2.55/Df 0.0019), RF-35 (Dk 3.50/Df 0.0018), CER-10 (Dk 10.0/Df 0.0035), fastRise 27 (Dk 2.72/Df 0.0014)"
topic: "Taconic RF laminate material specifications - internal recovery"
category: "materials"
status: "recovered"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-materials-taconic-pcb-page-en"
tags: ["taconic", "ptfe", "rf", "tly", "tlx", "rf-35", "cer-10", "fastrise", "recovery", "internal-source"]
---

# Canonical Summary

> Taconic RF/PTFE material specifications have been **RECOVERED** via APTPCB internal JSON source. This fact card extracts exact Dk/Df, thermal, and mechanical properties for 6 Taconic series while maintaining blocked-claims discipline due to absence of official Taconic-controlled product pages.

## Recovery Status: ⚠️ INTERNAL-ONLY

| Series | Recovery Source | Official Source Status | Use Constraint |
|--------|-----------------|------------------------|----------------|
| **TLY / TLY-5A** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |
| **TLX** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |
| **TLC** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |
| **RF-35** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |
| **CER-10** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |
| **fastRise 27** | APTPCB internal JSON | ❌ No current Taconic product page | Internal use only |

## Stable Facts (Internal Recovery)

### TLY / TLY-5A Series - Ultra-Low Loss

| Property | Value | Test Method |
|----------|-------|-------------|
| Dk @ 10 GHz | 2.17 ±0.02 | IPC-TM-650 2.5.5.5 |
| Df @ 10 GHz | 0.0009 | IPC-TM-650 2.5.5.5 |
| Thermal Conductivity | 0.23 W/m·K | ASTM E1461 |
| CTE X/Y | 25 ppm/°C | IPC-TM-650 2.4.41 |
| CTE Z | 280 ppm/°C | IPC-TM-650 2.4.41 |
| Moisture Absorption | 0.02% | IPC-TM-650 2.6.2.1 |
| Peel Strength | 6 lb/in | IPC-TM-650 2.4.8 |
| Tg | N/A (PTFE) | IPC-TM-650 2.4.25 |
| Dielectric Strength | 800 V/mil | IPC-TM-650 2.5.6.2 |
| Flammability | V-0 | UL 94 |

**Key Characteristics**: Lowest-loss Taconic laminate, woven fiberglass reinforcement, plasma desmear required, 0.02% moisture

**Applications**: Satellite LNA boards, Ka-band phased-array antenna feeds, military EW wideband receivers, stripline power combiners, VNA calibration substrates

### TLX Series - Moderate Loss

| Property | Value |
|----------|-------|
| Dk @ 10 GHz | 2.55 ±0.04 |
| Df @ 10 GHz | 0.0019 |
| Thermal Conductivity | 0.26 W/m·K |
| CTE X/Y | 15 ppm/°C |
| CTE Z | 280 ppm/°C |
| Moisture Absorption | 0.02% |
| Peel Strength | 8 lb/in |

**Key Characteristics**: Moderate-loss PTFE enabling more compact microstrip geometries, good dimensional stability

**Applications**: Base-station duplexers, Wilkinson power dividers, GPS/GNSS patch arrays, radar T/R modules

### TLC Series - Economy PTFE

| Property | Value |
|----------|-------|
| Dk | 2.95-3.20 |
| Df @ 10 GHz | 0.0020 |
| Key Characteristics | Cost-reduced PTFE entry point, better-than-FR-4 RF performance |
| Applications | Wi-Fi 6/7 front-end, Bluetooth antennas, ISM-band radios, automotive V2X |

### RF-30 / RF-35 Series - Ceramic-Filled

| Property | Value |
|----------|-------|
| Dk @ 10 GHz | 3.50 ±0.05 |
| Df @ 10 GHz | 0.0018 |
| Thermal Conductivity | 0.62 W/m·K |
| CTE X/Y | 14 ppm/°C |
| CTE Z | 30 ppm/°C |
| Moisture Absorption | 0.06% |
| Peel Strength | 8 lb/in |
| Tg | >280°C |
| Dielectric Strength | 750 V/mil |

**Key Characteristics**: Df lower than Rogers RO4350B (0.0018 vs 0.0037), plasma desmear recommended, lead-free compatible

**Applications**: Sub-6 GHz 5G macro/small-cell antennas, power amplifier pallets, GPS receivers, WLAN access points

### CER-10 Series - High-Dk

| Property | Value |
|----------|-------|
| Dk @ 10 GHz | 10.0 ±0.25 |
| Df @ 10 GHz | 0.0035 |
| Thermal Conductivity | 0.42 W/m·K |
| CTE X/Y | 8 ppm/°C |
| CTE Z | 20 ppm/°C |
| Moisture Absorption | 0.05% |
| Peel Strength | 5 lb/in |

**Key Characteristics**: Extremely high Dk enables physically small antennas and filters, ceramic loading provides excellent Dk stability

**Applications**: Dielectric resonator antennas (DRA), compact cavity filters, horn antenna feeds, miniaturized GPS patch antennas

### fastRise 27 Series - Hybrid Bonding

| Property | Value |
|----------|-------|
| Dk @ 10 GHz | 2.72 ±0.04 |
| Df @ 10 GHz | 0.0014 |
| Thermal Conductivity | 0.28 W/m·K |
| CTE X/Y | 12 ppm/°C |
| CTE Z | 40 ppm/°C |
| Tg | >250°C |
| Moisture Absorption | 0.03% |
| Peel Strength | 6 lb/in |

**Key Characteristics**: Low-loss thermoset bonding prepreg, designed for hybrid PTFE/FR-4 multilayers

**Applications**: Hybrid Taconic/FR-4 multilayers, high-speed digital with integrated RF sections

## Stocked at APTPCB (Internal)

| Series | Thickness | Copper |
|--------|-----------|--------|
| RF-35 | 10-60 mil | 1/2 oz, 1 oz ED |
| TLY-5A | 5-31 mil | 1/2 oz, 1 oz ED |
| CER-10 | 20-40 mil | 1/2 oz, 1 oz ED |
| fastRise 27 | Bonding prepreg | - |

## Conditions And Methods

- Use this card for **internal material comparison and stackup planning only**
- Pair with `taconic-official-source-coverage-gap.md` when citing externally
- All values sourced from APTPCB internal JSON, not official Taconic datasheets
- Test methods are cited per internal source (IPC-TM-650, ASTM E1461, UL 94)

## Limits And Non-Claims

- ❌ **NOT** official Taconic-published datasheet values
- ❌ Does not establish current Taconic product availability or corporate status
- ❌ Does not validate Taconic product-line continuity
- ❌ Not for external publication without explicit source-gap pairing
- ❌ Does not replace need for official Taconic-controlled source discovery

## Open Questions

- When will official Taconic RF laminate product pages or datasheets become available?
- Is Taconic Advanced Dielectric Division still actively supporting RF laminate production?
- Should these recovered values be treated as historical reference or current capability?

## Source Links

- Internal: `/code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json`
- Source Record: `sources/registry/internal/frontendapt-materials-taconic-pcb-page-en.md`
