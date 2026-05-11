---
topic_id: "processes-package-library-governance-and-footprint-review-map"
title: "Package Library Governance And Footprint Review Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-11"
fact_ids:
  - "methods-package-family-and-footprint-governance-vocabulary-boundary"
  - "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
  - "methods-connector-origin-and-installation-mark-boundary"
  - "methods-cad-owner-footprint-reference-point-and-layer-role-boundary"
  - "methods-iec-zero-orientation-cad-library-construction-boundary"
  - "methods-iec-smd-component-marking-boundary"
  - "methods-bga-1p50mm-pitch-standards-existence-boundary"
  - "methods-iec-square-bga-1mm-or-larger-outline-and-variation-boundary"
  - "methods-iec-area-array-land-pattern-geometry-family-boundary"
  - "methods-nxp-1p50mm-bga225-reflow-footprint"
  - "methods-renesas-1p50mm-bga-package-drawing-prbg0225cb-a"
  - "methods-renesas-1p50mm-bga-lga-mount-pad-dimensions-row"
  - "methods-amd-bg225-bgg225-1p50mm-bga-footprint-row"
  - "methods-nxp-bga-footprint-pitch-and-pcb-land-pad-examples"
  - "methods-ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch"
  - "methods-microchip-csp-bga-solder-land-and-pitch-examples"
  - "methods-microchip-0p75mm-tfbga-land-pattern-4lx"
  - "methods-microchip-0p75mm-tfbga-land-pattern-7g"
  - "methods-microchip-0p75mm-tfbga-land-pattern-bab"
  - "methods-renesas-0p75mm-fbga-package-land-pattern-bcg48d1"
  - "methods-nxp-0p75mm-fbga448-reflow-footprint"
  - "methods-intel-0p75mm-ubga-csp-pcb-design-guidelines-table"
  - "methods-intel-bga-land-pad-guidelines-common-pitches-and-vbga"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-internal-resource-layer-prompt-support-corpus"
source_ids:
  - "infineon-package-family-and-package-detail-identity-grammar"
  - "kicad-library-conventions-package-family-and-footprint-naming"
  - "frontendapt-glossary-terms-resource-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-resources-index-en"
  - "kicad-library-conventions-footprint-orientation-and-marking"
  - "altium-designer-pcb-footprint-reference-point-and-layer-boundary"
  - "molex-105133-0002-micro-b-recommended-pcb-layout"
  - "samtec-mb1-recommended-pcb-layout-and-mating-card"
  - "amphenol-10122424-sfp-board-connector-recommended-pcb-layout"
  - "iec-61188-7-zero-orientation-cad-library-page"
  - "iec-61760-1-smd-specification-page"
  - "iec-61760-1-component-marking-preview-page"
  - "iec-60191-6-2-ball-column-package-design-guide-page"
  - "iec-60191-6-18-square-bga-design-guide-page"
  - "iec-61188-5-8-area-array-land-pattern-page"
  - "iec-61188-6-2-land-pattern-design-smd-page"
  - "nxp-sot648-1-bga225-1p50mm-reflow-footprint"
  - "renesas-prbg0225cb-a-1p50mm-bga-package-drawing"
  - "renesas-bga-lga-mount-pad-dimensions-common-pitches"
  - "amd-ug112-bg225-bgg225-1p50mm-bga-footprint-row"
  - "nxp-an10778-bga-footprints"
  - "ti-an1126-bga-pad-geometry-guidelines"
  - "microchip-ac243-csp-pcb-design-guidelines"
  - "microchip-176b-tfbga-4lx-package-drawing-0p75mm-land-pattern"
  - "microchip-169b-tfbga-7g-package-drawing-0p75mm-land-pattern"
  - "microchip-196b-tfbga-bab-package-drawing-0p75mm-land-pattern"
  - "renesas-bcg48d1-48-fbga-package-land-pattern-0p75mm"
  - "nxp-sot1908-1-fbga448-0p75mm-reflow-footprint"
  - "intel-0p75mm-ubga-csp-pcb-design-guidelines-table"
  - "intel-an114-bga-land-pad-dimensions"
tags: ["package-library", "footprint", "governance", "dfm", "review", "padstack", "pin-1", "origin", "polarity", "processes"]
---

# Governance Summary

> Package-library governance should be written as a controlled review-and-documentation process: normalize package-family vocabulary, select or verify the footprint library object, preserve origin and polarity intent, review footprint dimensions using non-numeric geometry language first, and route exact geometry to stronger package-owner or standards-backed sources. This page exists to keep prompts from turning secondary-PDF examples or local UI screenshots into universal footprint rules.

## Why This Page Exists

The current local coverage is strong enough to support package / footprint governance language, but it is split across:

- internal APT glossary and DFM resource pages
- package-family taxonomy inventory from `C1`
- pad / origin / pin-1 / keepout inventory from `C2`
- review-dimension and governance inventory from `C3`

Without a process map, prompts are likely to make three mistakes:

1. Turn handbook naming grammar into universal package taxonomy
2. Turn review dimensions into numeric acceptance standards
3. Treat vendor `DFM` screens as neutral footprint-design authority

This page closes those failure modes by routing package-library work into the right boundary cards.

## Quick Navigation: Find The Right Card

| Question | Fact Card | Safe Depth |
|---|---|---|
| What package-family names are safe to use? | `methods-package-family-and-footprint-governance-vocabulary-boundary` | Taxonomy and governance vocabulary |
| What padstack, origin, pin-1, and review-dimension terms are safe? | `methods-padstack-origin-pin1-and-footprint-review-governance-boundary` | Review vocabulary and blocked numerics |
| What official support exists for connector origin or installation-mark wording? | `methods-connector-origin-and-installation-mark-boundary` | CAD-library convention plus multiple series-specific owner drawings only |
| What official CAD-owner support exists for footprint reference-point handling and visible/documentation layer separation? | `methods-cad-owner-footprint-reference-point-and-layer-role-boundary` | Cross-tool CAD-owner construction boundary only |
| What standards-owner support exists for zero-orientation wording in CAD library construction? | `methods-iec-zero-orientation-cad-library-construction-boundary` | Standards-owner orientation-description boundary only |
| What public IEC support exists for `pin-1` and polarity identification? | `methods-iec-smd-component-marking-boundary` | Component-specification marking boundary only |
| What official support exists for `1.50 mm` coarse-pitch BGA wording if exact geometry is still missing? | `methods-bga-1p50mm-pitch-standards-existence-boundary`, `methods-iec-square-bga-1mm-or-larger-outline-and-variation-boundary` | Standards-owner existence plus square-BGA family framing only |
| What stronger IEC support exists for area-array land-pattern design without a public `1.50 mm` row? | `methods-iec-area-array-land-pattern-geometry-family-boundary` | Standards-owner area-array land-pattern family and lifecycle framing only |
| What official support exists for current-public `1.50 mm` owner-scoped package evidence? | `methods-nxp-1p50mm-bga225-reflow-footprint`, `methods-renesas-1p50mm-bga-package-drawing-prbg0225cb-a`, `methods-renesas-1p50mm-bga-lga-mount-pad-dimensions-row`, `methods-amd-bg225-bgg225-1p50mm-bga-footprint-row` | Multiple owner-scoped exact rows plus one Renesas named-package drawing |
| What official BGA / CSP land-pattern examples can replace handbook table pressure? | `methods-nxp-bga-footprint-pitch-and-pcb-land-pad-examples`, `methods-ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch`, `methods-microchip-csp-bga-solder-land-and-pitch-examples`, `methods-microchip-0p75mm-tfbga-land-pattern-4lx`, `methods-microchip-0p75mm-tfbga-land-pattern-7g`, `methods-microchip-0p75mm-tfbga-land-pattern-bab`, `methods-renesas-0p75mm-fbga-package-land-pattern-bcg48d1`, `methods-nxp-0p75mm-fbga448-reflow-footprint`, `methods-intel-0p75mm-ubga-csp-pcb-design-guidelines-table`, `methods-intel-bga-land-pad-guidelines-common-pitches-and-vbga` | Vendor-scoped exact geometry only |
| Where does footprint review sit in broader DFM review? | `methods-pcba-dfm-dft-dfa-review-gate-positioning` | DFM gate placement |
| Which internal APT resource pages support this topic? | `methods-internal-resource-layer-prompt-support-corpus` | Resource-layer routing |

## Package-Library Review Flow

```
Package identity appears
  ↓
Normalize to safe package-family vocabulary
  ↓
Locate the footprint-library object
  ↓
Check documentation completeness
  → assembly drawing
  → polarity marking
  → pin-1 / orientation information
  → zero-orientation discipline when stronger standards wording is needed
  → origin handling
  ↓
Check footprint review dimensions at vocabulary level
  → leaded package review:
    toe / heel / side clearance
  → chip package review:
    pad length / pad width / inner spacing
  ↓
Check process-sensitive notes
  → keep-out areas
  → special pad or thermal-pad attention
  ↓
If exact geometry is needed:
  stop using this map
  route to stronger package-owner or standards-backed authority
```

## Exact-Geometry Route

When a prompt needs real BGA or CSP pad geometry rather than vocabulary-only footprint review language, route to existing package-owner cards instead of reopening the local handbook table:

- `methods-nxp-bga-footprint-pitch-and-pcb-land-pad-examples`
  - use for named-package NXP `1.0`, `0.8`, `0.65`, and `0.5 mm` BGA footprint rows
- `methods-ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch`
  - use for TI `1.27 mm` and `1.0 mm` `NSMD/SMD` BGA pad-geometry rows
- `methods-microchip-csp-bga-solder-land-and-pitch-examples`
  - use for Microchip CSP/BGA `0.4`, `0.5`, and `0.8 mm` package-scoped rows
- `methods-nxp-1p50mm-bga225-reflow-footprint`
  - use for one NXP owner-scoped `1.50 mm` `BGA225 / SOT648-1` reflow-footprint row
- `methods-renesas-1p50mm-bga-package-drawing-prbg0225cb-a`
  - use for one Renesas owner-scoped `1.50 mm` `PRBG0225CB-A` named-package drawing with direct pitch identity only
- `methods-renesas-1p50mm-bga-lga-mount-pad-dimensions-row`
  - use for one Renesas owner-scoped `1.50 mm` exact row `Lead pitch(mm) 1.50 -> φ(mm) 0.55 to 0.65`
- `methods-amd-bg225-bgg225-1p50mm-bga-footprint-row`
  - use for one AMD-hosted `UG112` owner-scoped `1.50 mm` exact row `BG225 / BGG225` with same-table footprint geometry values
- `methods-iec-square-bga-1mm-or-larger-outline-and-variation-boundary`
  - use for one tighter official IEC package-family boundary that `all square BGA packages, terminal pitch 1 mm or larger` have formal outline, dimension, and recommended-variation framing, while keeping exact public PCB land-pattern geometry blocked
- `methods-iec-area-array-land-pattern-geometry-family-boundary`
  - use for official IEC standards-owner framing that area-array land-pattern geometry is a formal design family, while keeping exact `1.50 mm` geometry blocked unless a public owner row or paid-standard content is separately available
- `methods-microchip-0p75mm-tfbga-land-pattern-4lx`
  - use for one Microchip owner-scoped `0.75 mm` `176-ball 4LX TFBGA` package-drawing row
- `methods-microchip-0p75mm-tfbga-land-pattern-7g`
  - use for one additional Microchip owner-scoped `0.75 mm` `169-ball 7G TFBGA` package-drawing row
- `methods-microchip-0p75mm-tfbga-land-pattern-bab`
  - use for one additional Microchip owner-scoped `0.75 mm` `196-ball BAB TFBGA` package-drawing row
- `methods-renesas-0p75mm-fbga-package-land-pattern-bcg48d1`
  - use for one current-public second-owner `0.75 mm` named-package `BCG48D1` land-pattern page with visible page geometry and note context only
- `methods-nxp-0p75mm-fbga448-reflow-footprint`
  - use for one current-public third-owner `0.75 mm` named-package `FBGA448 / SOT1908-1` reflow-footprint page set with visible page-scoped values and stencil-thickness note context only
- `methods-intel-0p75mm-ubga-csp-pcb-design-guidelines-table`
  - use for one Intel-hosted `.75mm µBGA CSP Package` owner-scoped exact table with PCB design guideline values
- `methods-intel-bga-land-pad-guidelines-common-pitches-and-vbga`
  - use for Intel owner-scoped `1.27`, `1.00`, `0.80`, `0.50`, and `0.4 mm VBGA/WLCSP` guidance rows

These cards are stronger than the local handbook table because they preserve package-owner scope and printed row context.
They are still not a universal cross-vendor `pitch -> pad diameter` law.

## Safe Vocabulary Layer

### Package-Family Vocabulary

- `BGA`
- `QFN`
- `QFP`
- `SOIC`
- `DIP`
- `footprint`

Use these as classification and routing language, not as proof that one default geometry fits every part in the family.

### Footprint-Governance Vocabulary

- `pad`
- `drill`
- `via`
- `solder mask`
- `paste mask`
- `thermal relief`
- `anti pad`
- `keepout`
- `assembly drawing`
- `polarity`
- `origin`
- `pin-1 mark`

Use these as review and documentation terms.

### Review-Dimension Vocabulary

- Leaded-package review:
  `toe`, `heel`, `side clearance`
- Chip-package review:
  `pad length`, `pad width`, `inner spacing`

Use these to explain what is being reviewed, not to publish handbook thresholds.

## Process Rules

### Use This Page When

- a prompt needs safe package / footprint governance vocabulary
- a draft needs to explain why verified footprint libraries matter
- a draft needs to explain what kind of geometry is reviewed without giving exact values
- a prompt needs to keep polarity, origin, or pin-1 information inside controlled documentation

### Do Not Use This Page For

- exact pad or drill design values
- BGA land-pattern dimension tables
- package-family-specific formulas
- keepout offsets or silkscreen clearances
- vendor workflow screenshots or UI-derived rule settings

If a draft specifically needs package-scoped BGA/CSP geometry, leave this map and use the exact-data cards listed in `Exact-Geometry Route`.

## Provenance Inventory Boundary

The following logs informed this map but are not authority:

- `/code/blogs/llm_wiki/logs/p4-215c1-2026-5-6-package-lane-c1-package-taxonomy-and-naming.md`
- `/code/blogs/llm_wiki/logs/p4-215c2-2026-5-6-package-lane-c2-pad-origin-pin1-keepout-drawings.md`
- `/code/blogs/llm_wiki/logs/p4-215c3-2026-5-6-package-lane-c3-library-governance-and-hole-pad-examples.md`
- `/code/blogs/llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`

Use them as provenance inventory for:

- what the secondary PDF exposed
- which images were technically useful
- which claims were blocked

Do not use them as authority for exact geometry or universal package rules.

## Must Refresh Before Publishing

- Any claim about universal package naming grammar
- Any exact land-pattern or compensation formula
- Any exact keepout, silkscreen, or grouped-pin-mark offset
- Any threshold behind `optimal`, `general`, `risk`, or `danger`
- Any claim tied to vendor `DFM` workflow or rule-management screens
- Any attempt to collapse the NXP, TI, and Microchip rows into one generic pitch table

## Primary Sources

- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/resources/en/index.json
