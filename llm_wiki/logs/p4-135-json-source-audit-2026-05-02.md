# JSON Source Audit: frontendAPT vs frontendHIL vs llm_wiki

**Date**: 2026-05-02
**Purpose**: Verify all frontend JSON sources are registered in llm_wiki sources/registry

---

## Executive Summary

| Source Location | Total JSON Files | Registered in llm_wiki | Coverage |
|-----------------|------------------|------------------------|----------|
| frontendAPT | ~500+ (62 unique types × 8 languages) | Partial | ~30% |
| frontendHIL | ~200+ (24 product types × 8 languages) | Minimal | ~10% |

**Status**: ⚠️ **PARTIAL** - Many JSON sources not yet registered

---

## frontendAPT JSON Inventory

### Materials (10 files × 8 languages = 80 total)

| File | EN Path | Registered |
|------|---------|------------|
| taconic-pcb.json | ✅ | ✅ `frontendapt-taconic-pcb-json` |
| arlon-pcb.json | ✅ | ✅ `frontendapt-arlon-pcb-json` |
| isola-pcb.json | ✅ | ❌ **MISSING** |
| megtron-pcb.json | ✅ | ❌ **MISSING** |
| rf-rogers.json | ✅ | ❌ **MISSING** |
| rogers-pcb-manufacturing.json | ✅ | ❌ **MISSING** |
| teflon-pcb.json | ✅ | ❌ **MISSING** |
| spread-glass-fr4.json | ✅ | ❌ **MISSING** |
| controlled-impedance-stackups.json | ✅ | ❌ **MISSING** |
| index.json | ✅ | ❌ **MISSING** |

### Capabilities (7 files × 8 languages = 56 total)

| File | EN Path | Registered |
|------|---------|------------|
| rigid-pcb.json | ✅ | Partial (via index) |
| flex-pcb.json | ✅ | Partial (via index) |
| hdi-pcb.json | ✅ | Partial (via index) |
| ceramic-pcb.json | ✅ | Partial (via index) |
| metal-pcb.json | ✅ | Partial (via index) |
| rigid-flex-pcb.json | ✅ | Partial (via index) |
| index.json | ✅ | ❌ **MISSING** |

### PCB Pages (33 files × 8 languages = 264 total)

| Category | Status |
|----------|--------|
| Manufacturing pages | Partial coverage |
| Process pages (drilling, plating, etc.) | Minimal coverage |
| Product pages | Partial coverage |

### PCBA Pages (32 files × 8 languages = 256 total)

| Category | Status |
|----------|--------|
| Testing methods (ICT, X-ray, AOI) | ✅ Covered in T4A |
| Assembly services | Minimal coverage |
| NPI processes | Partial coverage |

### Industries (10 files × 8 languages = 80 total)

| Industry | EN Path | Registered |
|----------|---------|------------|
| aerospace-defense | ✅ | Partial |
| automotive | ✅ | Partial |
| communication | ✅ | Partial |
| medical | ✅ | Partial |
| server-data-center | ✅ | Partial |
| drone-uav | ✅ | Partial |
| robotics | ✅ | Partial |
| security | ✅ | Partial |
| power-energy | ✅ | Partial |
| industrial-control | ✅ | Partial |

### Resources (6 files × 8 languages = 48 total)

| File | EN Path | Registered |
|------|---------|------------|
| downloads-materials.json | ✅ | ❌ **MISSING** |
| faq.json | ✅ | ❌ **MISSING** |
| glossary-terms.json | ✅ | ❌ **MISSING** |
| dfm-guidelines.json | ✅ | ❌ **MISSING** |

---

## frontendHIL JSON Inventory

### Products (24 files × 8 languages = 192 total)

| Product | EN Path | Registered |
|---------|---------|------------|
| multilayer-pcb | ✅ | ❌ **MISSING** |
| hdi-pcb | ✅ | ❌ **MISSING** |
| high-frequency-pcb | ✅ | ❌ **MISSING** |
| high-speed-pcb | ✅ | ❌ **MISSING** |
| rogers-pcb | ✅ | ❌ **MISSING** |
| teflon-pcb | ✅ | ❌ **MISSING** |
| rigid-flex-pcb | ✅ | ❌ **MISSING** |
| flex-pcb | ✅ | ❌ **MISSING** |
| metal-core-pcb | ✅ | ❌ **MISSING** |
| ceramic-pcb | ✅ | ❌ **MISSING** |
| fr4-pcb | ✅ | ❌ **MISSING** |
| high-tg-pcb | ✅ | ❌ **MISSING** |
| halogen-free-pcb | ✅ | ❌ **MISSING** |
| heavy-copper-pcb | ✅ | ❌ **MISSING** |
| high-thermal-pcb | ✅ | ❌ **MISSING** |
| ic-substrate-pcb | ✅ | ❌ **MISSING** |
| backplane-pcb | ✅ | ❌ **MISSING** |
| single-double-layer-pcb | ✅ | ❌ **MISSING** |
| smt-assembly | ✅ | ❌ **MISSING** |
| through-hole-assembly | ✅ | ❌ **MISSING** |
| small-batch-assembly | ✅ | ❌ **MISSING** |
| large-volume-assembly | ✅ | ❌ **MISSING** |
| box-build-assembly | ✅ | ❌ **MISSING** |
| turnkey-assembly | ✅ | ❌ **MISSING** |

---

## Critical Missing Registrations

### High Priority (Materials)

| File | Impact | Action |
|------|--------|--------|
| isola-pcb.json | High-speed FR4/HF materials | Register source + extract facts |
| megtron-pcb.json | Panasonic Megtron 4/6/7/8 | Register source + extract facts |
| rf-rogers.json | Rogers RO3000/RO4000 | Register source + extract facts |

### High Priority (Capabilities)

| File | Impact | Action |
|------|--------|--------|
| rigid-pcb.json | Core capability | Register source |
| flex-pcb.json | Flex capability | Register source |
| hdi-pcb.json | HDI capability | Register source |
| ceramic-pcb.json | Ceramic capability | Register source |
| metal-pcb.json | Metal core capability | Register source |
| rigid-flex-pcb.json | Rigid-flex capability | Register source |

### Medium Priority (HIL Products)

| File | Impact | Action |
|------|--------|--------|
| multilayer-pcb.json | Layer count specs | Register source |
| high-frequency-pcb.json | RF specs | Register source |
| high-speed-pcb.json | SI specs | Register source |

---

## Registered Sources Summary

### ✅ Complete Registrations

| Source ID | Local Path | Status |
|-----------|------------|--------|
| `frontendapt-taconic-pcb-json` | materials/en/taconic-pcb.json | ✅ Complete + facts |
| `frontendapt-arlon-pcb-json` | materials/en/arlon-pcb.json | ✅ Complete + facts |
| `frontendapt-ict-testing-page-en` | pcba/en/ict-testing.json | ✅ Complete |
| `frontendapt-flying-probe-testing-page-en` | pcba/en/flying-probe-testing.json | ✅ Complete |
| `frontendapt-xray-inspection-page-en` | pcba/en/xray-inspection.json | ✅ Complete |

### ⚠️ Partial Registrations (Index-only)

| Source ID | Coverage | Action |
|-----------|----------|--------|
| `frontendapt-materials-remaining-index-en` | Materials index only | Expand to individual files |
| `frontendapt-pcb-remaining-index-en` | PCB index only | Expand to individual files |
| `frontendapt-pcba-remaining-index-en` | PCBA index only | Expand to individual files |
| `frontendapt-capabilities-index-en` | Capabilities index only | Expand to individual files |
| `frontendapt-industries-index-en` | Industries index only | Expand to individual files |
| `frontendapt-resources-index-en` | Resources index only | Expand to individual files |
| `frontendhil-products-remaining-index-en` | HIL products index | Expand to individual files |
| `frontendhil-service-landings-index-en` | HIL services index | Expand to individual files |

---

## Recommended Next Actions

1. **Register all 10 materials JSONs** with fact extraction (Taconic/Arlon done, 8 remaining)
2. **Register all 7 capabilities JSONs** for complete capability coverage
3. **Register critical HIL product JSONs** (multilayer, high-frequency, high-speed)
4. **Expand index-only sources** to full individual registrations
5. **Create missing fact cards** for Rogers, Isola, Panasonic Megtron series

---

*This audit follows ASSESSMENT.md Tier-1 internal source policy*
