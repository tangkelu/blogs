---
task_id: "p4-143-taconic-arlon-rf-ptfe-detailed-recovery"
status: "completed"
owner: "cascade-agent"
lane: "Taconic / Arlon RF-PTFE Detailed Recovery via Internal JSON"
input_paths:
  - /code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json
  - /code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
output_paths:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-taconic-pcb-page-en.md (UPDATED)
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-arlon-pcb-page-en.md (UPDATED)
  - /code/blogs/llm_wiki/facts/materials/taconic-detailed-material-specs-recovery.md (NEW)
  - /code/blogs/llm_wiki/facts/materials/arlon-detailed-material-specs-recovery.md (NEW)
  - /code/blogs/llm_wiki/logs/p4-143-taconic-arlon-rf-ptfe-detailed-recovery.md
write_scope:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-taconic-pcb-page-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-arlon-pcb-page-en.md
  - /code/blogs/llm_wiki/facts/materials/taconic-detailed-material-specs-recovery.md
  - /code/blogs/llm_wiki/facts/materials/arlon-detailed-material-specs-recovery.md
blocked_claims:
  - official Taconic datasheet authority (current site shows industrial PTFE fabrics only)
  - official Arlon/AGC datasheet authority for CLTE-XT, TC350, AD250/300/1000, CuClad/DiClad/IsoClad
  - current Taconic/Arlon product availability or lead times
  - Taconic/Arlon factory-direct technical support channels
  - external publication without source-gap pairing
completed_at: "2026-05-03"
---

# P4-143 Taconic / Arlon RF-PTFE Detailed Recovery

## Scope

Detailed recovery of Taconic and Arlon RF/PTFE material specifications via APTPCB internal JSON, while maintaining strict blocked-claims discipline.

## Changes Made

### Updated Source Records (2 files)

**`frontendapt-materials-taconic-pcb-page-en.md`** (UPDATED)
- Added complete 8-series material portfolio table
- Added detailed properties matrix (6 products × 10 properties)
- Added stocked materials at APTPCB
- Added explicit extraction notes with blocked claims
- Updated `checked_at` to 2026-05-03, `must_refresh` to true

**`frontendapt-materials-arlon-pcb-page-en.md`** (UPDATED)
- Added complete 8-series material portfolio table (polyimide, epoxy, Thermount, PTFE)
- Added detailed properties matrix (6 products × 12 properties)
- Added critical process notes (polyimide pre-bake, PTFE plasma requirements)
- Added stocked materials at APTPCB
- Added explicit extraction notes with blocked claims
- Updated `checked_at` to 2026-05-03, `must_refresh` to true

### Created Fact Cards (2 files) - Knowledge Increment

**`taconic-detailed-material-specs-recovery.md`** (NEW)
- Recovery status: INTERNAL-ONLY for all 6 Taconic series
- Detailed specs for TLY-5A (Dk 2.17/Df 0.0009), TLX (Dk 2.55/Df 0.0019), TLC (Dk 2.95-3.20/Df 0.0020)
- Detailed specs for RF-35 (Dk 3.50/Df 0.0018), CER-10 (Dk 10.0/Df 0.0035), fastRise 27 (Dk 2.72/Df 0.0014)
- Thermal properties: conductivity (0.23-0.62 W/m·K), CTE X/Y/Z
- Mechanical properties: peel strength, dielectric strength, moisture
- Test methods: IPC-TM-650, ASTM E1461, UL 94

**`arlon-detailed-material-specs-recovery.md`** (NEW)
- Recovery status: INTERNAL-ONLY for RF/PTFE families
- Polyimide series (33N/35N/85N): Tg >250°C, Dk 4.20/Df 0.015 @ 1 MHz, 1.20% moisture
- Epoxy series (45N/47N/49N): Tg 175°C, Dk 4.30/Df 0.015 @ 1 MHz
- Thermount (55NT/85NT): CTE X/Y 7-9 ppm/°C, Tg 260°C
- **RECOVERED CLTE-XT**: Dk 2.94/Df 0.0012 @ 10 GHz, Z-CTE 20 ppm/°C (matched to copper)
- **RECOVERED TC350**: Thermal conductivity 1.0 W/m·K, Dk 3.50/Df 0.0020
- **RECOVERED AD250**: Dk 2.50/Df 0.0014, peel strength 12.0 lb/in
- **RECOVERED CuClad/DiClad/IsoClad**: Dk 2.17-2.60/Df 0.0009

## Knowledge Value Added

| Brand | Series | Key Specs Recovered | Official Source Status |
|-------|--------|---------------------|------------------------|
| **Taconic** | TLY-5A | Dk 2.17 ±0.02, Df 0.0009, CTE Z 280 ppm/°C | ❌ No current product page |
| **Taconic** | TLX | Dk 2.55 ±0.04, Df 0.0019 | ❌ No current product page |
| **Taconic** | TLC | Dk 2.95-3.20, Df 0.0020 | ❌ No current product page |
| **Taconic** | RF-35 | Dk 3.50 ±0.05, Df 0.0018, thermal 0.62 W/m·K | ❌ No current product page |
| **Taconic** | CER-10 | Dk 10.0 ±0.25, Df 0.0035 | ❌ No current product page |
| **Taconic** | fastRise 27 | Dk 2.72 ±0.04, Df 0.0014, Tg >250°C | ❌ No current product page |
| **Arlon** | CLTE-XT | Dk 2.94, Df 0.0012, Z-CTE 20 ppm/°C | ❌ No current datasheet |
| **Arlon** | TC350 | Dk 3.50, Df 0.0020, **thermal 1.0 W/m·K** | ❌ No current datasheet |
| **Arlon** | AD250 | Dk 2.50, Df 0.0014, peel 12.0 lb/in | ❌ No current datasheet |
| **Arlon** | AD1000 | Dk 10.2, Df 0.0014 | ❌ No current datasheet |
| **Arlon** | CuClad/DiClad | Dk 2.17-2.60, Df 0.0009 | ❌ No current datasheet |

## Critical Process Specifications Recovered

### Taconic
- Plasma desmear required for all PTFE series
- Hybrid bonding: fastRise 27 for PTFE/FR-4 multilayers
- TacLam for all-PTFE multilayers

### Arlon Polyimide (33N, 55NT)
- **High moisture absorption (1.20%, 1.00%)**
- **Mandatory pre-bake before lamination**
- Standard desmear (no plasma)

### Arlon PTFE (CLTE, TC350, AD)
- **Plasma desmear required**
- No meaningful Tg
- Very low moisture (0.02%)

## Blocked Claims Summary

| Blocked Claim | Reason |
|---------------|--------|
| Official Taconic datasheet authority | Current `4taconic.com` shows industrial PTFE fabrics only |
| Official Arlon datasheet authority (RF/PTFE) | No current product pages for CLTE-XT, TC350, AD, CuClad families |
| Current product availability | Internal stock only, no manufacturer confirmation |
| Product-line continuity | No official Taconic/Arlon confirmation |
| External publication | Must pair with source-gap cards |

## Relation to P4-127

- P4-127 established the hold-first status for Taconic and partial status for Arlon
- P4-143 **does not change** the hold-first/partial status
- P4-143 **adds** detailed internal specifications for use when official sources are unavailable
- P4-143 **maintains** all blocked claims and source-gap discipline

## Recovery Classification

| Material | Recovery Status | Use Constraint |
|----------|-----------------|----------------|
| Taconic TLY/TLX/TLC/RF-35/CER-10/fastRise | RECOVERED (internal) | Internal stackup planning only |
| Arlon 33N/35N/45N/47N | VERIFIED (official exists) | Standard use with internal cross-check |
| Arlon Thermount | RECOVERED (internal) | Internal use preferred |
| Arlon CLTE-XT/TC350/AD/CuClad | RECOVERED (internal) | Internal stackup planning only |
| Arlon 37N/38N/HF-50 | RECOVERED (internal) | Internal use preferred |

## Residual Gaps

| Gap | P4-143 Status | Next Action |
|-----|---------------|-------------|
| Official Taconic RF laminate product pages | Still blocked | Monitor `4taconic.com` for changes |
| Official Arlon CLTE-XT/TC350/AD datasheets | Still blocked | Monitor `arlonemd.com` for changes |
| Current manufacturer support status | Still unknown | Contact AGC Inc. for confirmation |
| Test method version currency | Not verified | Verify IPC-TM-650 versions |

## Conclusion

P4-143 completes detailed material specification recovery for the "Taconic / Arlon RF-PTFE recovery" lane. The lane remains **hold-first for Taconic** and **partial for Arlon RF/PTFE families**, but now has **detailed internal specifications available** for constrained internal use.

