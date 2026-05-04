---
wiki_id: "wiki-materials-specialty-and-colored-pcb-material-boundaries"
title: "Specialty and colored PCB material boundaries"
topic: "Specialty / colored PCB material routing"
category: "materials"
status: "active"
reviewed_at: "2026-05-03"
fact_ids:
  - "materials-colored-solder-resist-product-specific-boundary"
  - "materials-transparent-stretchable-biodegradable-electronics-material-system-boundary"
  - "methods-2025-7-22-specialty-materials-rogers-draft-consumption-boundary"
source_ids:
  - "peters-elpepcb-solder-resists"
  - "peters-elpepcb-overview"
  - "peters-led-optical-requirements-paper"
  - "corning-willow-glass"
  - "henkel-loctite-eci-1501-ec"
  - "qnity-activegrid-products"
  - "jiva-soluboard-technology"
tags: ["colored-pcb", "solder-mask", "transparent-pcb", "stretchable-pcb", "biodegradable-pcb", "printed-electronics", "specialty-materials"]
---

# Use This Page For

- Routing drafts that say `black PCB`, `white PCB`, `transparent PCB`, `stretchable PCB`, `biodegradable PCB`, `printed electronics`, or generic `special PCB material`.
- Separating named material systems from unsupported finished-board manufacturing claims.
- Preventing article titles from turning color, transparency, formability, or sustainability language into fake capability claims.

# Core Boundary Rule

- Start with the material system, not the headline label.
- `Colored PCB` usually means colored solder resist or coating, not a colored laminate.
- `Transparent PCB`, `stretchable PCB`, and `biodegradable PCB` currently route to named substrate, conductor, ink, or laminate systems, not to a proven standard PCB factory capability.

# Material-System Routing

## Colored PCB: usually a solder-resist or coating lane

- Route `black PCB`, `white PCB`, `red PCB`, `blue PCB`, `yellow PCB`, `green PCB`, or `transparent PCB color` language to colored solder resist unless the source explicitly says the substrate itself is colored.
- Peters provides product-family anchors for colored solder resist and printed-circuit coatings.
- Reflectivity, yellowing resistance, flexibility, thick-copper suitability, and LED-related optical wording stay tied to named Peters product lines only.

## Transparent Electronics: substrate and conductor-system lane

- Route `transparent PCB` drafts to transparent electronics material-system framing first.
- Current local support is for named transparent substrate or optoelectronic systems such as Willow Glass and Qnity transparent/conductive film contexts.
- Do not convert transparent-material evidence into generic multilayer transparent-PCB capability.

## Stretchable / Formable Electronics: conductive-ink lane

- Route `stretchable PCB` drafts to formable printed electronics or conductive-ink framing.
- Henkel and Qnity support named printed-electronics and formable-circuit material systems.
- Do not rewrite those systems as proof of repeated stretch-cycle PCB reliability or ordinary SMT-board manufacturability.

## Biodegradable PCB: named laminate lane

- Route `biodegradable PCB` drafts to named biodegradable laminate context such as Soluboard.
- Jiva provides the current local named-laminate anchor, including process-compatibility framing and source-scoped sustainability comparisons.
- Do not generalize one named biodegradable laminate into a universal biodegradation or lifecycle claim for all PCB builds.

# Safe Selection Language

- Write `colored solder resist` or `colored solder mask` instead of `colored FR-4` unless the substrate is explicitly the colored product.
- Write `transparent electronics material system`, `transparent substrate/conductor system`, or the exact product name when discussing transparent builds.
- Write `formable printed electronics`, `conductive ink`, or `IME material system` instead of `stretchable PCB` unless the source proves a PCB process and reliability context.
- Write `Soluboard-specific biodegradable laminate` or another exact product name instead of generic biodegradable-board guarantees.
- Keep every optical, elongation, environmental, or process statement tied to the exact source owner and product family.

# Unsafe Selection Language

- Do not claim board color alone improves heat dissipation, LED efficiency, inspection yield, emissivity, or reliability.
- Do not claim transparent-material examples prove transparent multilayer PCB fabrication, plated transparent vias, or standard rigid-board assembly compatibility.
- Do not claim formable or conductive-ink systems prove wearable, medical, automotive, or repeated stretch-cycle suitability.
- Do not claim vendor sustainability comparisons prove universal compostability, biodegradation timing, or lifecycle superiority across all board designs.
- Do not turn topic-inventory drafts into supplier capability statements.

# When To Route Each Draft

| Draft signal | Route to | Reason |
| --- | --- | --- |
| `white PCB`, `black PCB`, `red PCB`, `blue PCB` | colored solder-resist boundary | current support is product-specific coating context |
| `transparent PCB`, `transparent circuit board` | transparent electronics material-system framing | current support is substrate / conductor-system evidence, not generic PCB capability |
| `stretchable PCB`, `flexible stretch circuit` | formable printed-electronics framing | current support is ink / film / IME context |
| `biodegradable PCB`, `eco PCB substrate` | named biodegradable laminate framing | current support is Soluboard-specific, not universal |
| mixed draft that also mentions Rogers / FR-4 / gold finger / edge plating | `2025.7.22` specialty draft-consumption boundary | topic inventory and routing rules already exist locally |

# Blocked Claims

- finished-board capability claims
- optical, stretch, biodegradation, and lifecycle guarantees
- supplier-capability claims
- cost, lead-time, and yield claims

# Must Refresh Before Publishing

- Any current product availability, compliance, or current color-series wording
- Any optical, thermal, electrical, elongation, fatigue, biodegradation, compostability, density, carbon-footprint, or lifecycle number reused outside its exact source context
- Any supplier-specific manufacturing, stock, MOQ, quote, quality, certification, or delivery claim

# Related Fact Cards

- `materials-colored-solder-resist-product-specific-boundary`
- `materials-transparent-stretchable-biodegradable-electronics-material-system-boundary`
- `methods-2025-7-22-specialty-materials-rogers-draft-consumption-boundary`

# Local Source Records

- `peters-elpepcb-solder-resists`
- `peters-elpepcb-overview`
- `peters-led-optical-requirements-paper`
- `corning-willow-glass`
- `henkel-loctite-eci-1501-ec`
- `qnity-activegrid-products`
- `jiva-soluboard-technology`
