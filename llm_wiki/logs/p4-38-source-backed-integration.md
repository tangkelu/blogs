# P4-38 Source-Backed Integration

Date: 2026-04-28

## Purpose

This controller pass converts the strongest P4-38 scout findings into reusable `llm_wiki` source records, fact cards, and topic wiki aggregation. It does not promote draft-originated price, lead time, MOQ, stock, supplier capability, equipment, certification, process-window, yield, quality-rate, RF / thermal / optical performance, or legal conclusions.

## Inputs Reviewed

- `logs/p4-38-2025-7-mixed-service-official-source-recovery-scout.md`
- `logs/p4-38-2025-7-22-specialty-materials-official-source-recovery-scout.md`
- `logs/p4-38-2025-10-13-commercial-fr4-procurement-official-source-recovery-scout.md`
- Existing Rogers, FR-4, PCBA, surface-finish, IPC metadata, and topic wiki layers

## Source Records Added

### International procurement / shipping

- `sources/registry/compliance/icc-incoterms-rules.md`
- `sources/registry/compliance/dhl-customs-clearance-documents.md`
- `sources/registry/compliance/dhl-customs-duties-and-taxes.md`
- `sources/registry/compliance/fedex-international-transit-notes.md`
- `sources/registry/compliance/cbp-basic-import-export.md`
- `sources/registry/compliance/cbp-importer-exporter-tips.md`

The CBP records are candidate-only because controller fetch returned `403`; they are preserved as official-source targets, not cited in the new fact card.

### Specialty / colored material systems

- `sources/registry/materials/peters-elpepcb-solder-resists.md`
- `sources/registry/materials/peters-elpepcb-overview.md`
- `sources/registry/materials/peters-led-optical-requirements-paper.md`
- `sources/registry/materials/jiva-soluboard-technology.md`
- `sources/registry/materials/corning-willow-glass.md`
- `sources/registry/materials/henkel-loctite-eci-1501-ec.md`
- `sources/registry/materials/qnity-activegrid-products.md`

## Fact Cards Added

- `facts/methods/international-pcb-shipping-customs-document-boundary.md`
- `facts/materials/colored-solder-resist-product-specific-boundary.md`
- `facts/materials/transparent-stretchable-biodegradable-electronics-material-system-boundary.md`
- `facts/standards/edge-contact-gold-finger-standards-metadata-boundary.md`

## Topic Wiki Added Or Updated

- Added `wiki/materials/specialty-and-colored-pcb-material-boundaries.md`
- Added `wiki/processes/international-pcb-procurement-shipping-boundaries.md`
- Updated `wiki/processes/finish-zoning-and-selective-multi-finish.md` to include the new gold-finger / edge-contact IPC metadata boundary.

## What This Unlocks

- `2025.10.13` shipping / delivery / procurement drafts can now use official-source-backed Incoterms, customs-document, duty/tax dependency, and carrier transit-estimate caveats.
- `2025.10.13` colored PCB drafts can now distinguish solder-resist color availability from unsupported substrate or board-performance claims.
- `2025.7.22` transparent / stretchable / biodegradable drafts now have named material-system anchors: Corning Willow Glass, Henkel LOCTITE ECI 1501 E&C, Qnity Activegrid, and Jiva Soluboard.
- `2025.7.22` gold-finger / edge-contact drafts now have a stricter IPC metadata route without inventing finish thickness or durability rules.

## Still Blocked

- Current HILPCB / APTPCB / Highleap capability, equipment, certification, quote speed, lead time, MOQ, stock, delivery, yield, quality-rate, and service promises.
- PCB-specific HS codes, tariff rates, country-specific tax outcomes, customs broker advice, or legal conclusions.
- Colored-board claims about thermal behavior, LED efficiency, medical / automotive suitability, inspection yield, or reliability from color alone.
- Transparent, stretchable, or biodegradable finished-board capability claims, optical / electrical tables, fatigue life, compostability, and qualification claims unless exact official sources or dated capability records are added.
- Gold-finger thickness, bevel, nickel underplate, insertion-cycle life, contact resistance, or class acceptance criteria without licensed standard text, customer drawings, or dated process records.

## Status

- integration status: `source_backed_fact_layer_partial`
- reusable data added: `yes`
- dynamic / supplier-specific claims: `blocked_pending_dated_capability_record`
- remaining source recovery: `P4-39 tool/CAM source owner pages`, `P4-40 November 2025 batch scouts`, and second-vendor solder-mask color sources
