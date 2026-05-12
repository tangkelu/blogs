---
source_id: "altium-bomdoc-cross-select-and-cross-probe-between-bom-and-pcb"
title: "Altium Designer Creating the BOM Document"
organization: "Altium"
owner: "Altium"
source_type: "software_vendor_documentation"
url: "https://www.altium.com/documentation/altium-designer/activebom/creating-document"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "software_vendor_documentation"
exact_data_class: "boundary_convention"
scope_type: "bomdoc_cross_select_and_cross_probe_to_schematic_and_pcb"
source_origin_path: "official Altium documentation page"
source_page_range: "Working Between the BomDoc, the Schematic and the PCB section"
confidence: "medium"
topic_tags: ["altium", "activebom", "bomdoc", "cross-probe", "cross-select", "pcb", "schematic", "bom"]
status: "active"
notes: "Official Altium documentation. Safe for the narrow boundary that a BOM-document selection can navigate to corresponding design objects in schematic and PCB views. Do not generalize this into assembly correctness, package-match sufficiency, or tool-workflow guarantees."
---

# Source Summary

## What It Covers

- BomDoc interaction with schematic and PCB documents
- cross-select behavior between design domains
- cross-probe navigation from BOM items to corresponding design objects

## Why It Matters

- Gives the `E7` visual-BOM lane one current-public official source for BOM-linked navigation between the part list and board-context views
- Supports a narrower neutral review boundary than the branded article's workflow-pitch framing

## Extraction Notes

- Safe for the boundary that selecting a BOM item can select or navigate to corresponding objects in schematic and PCB documents
- Safe for the idea that BOM-side review can be connected to board-context inspection without becoming assembly-proof or repair-proof authority
- Do not rewrite this page into automatic matching correctness, hand-soldering correctness, or inventory-checking guarantees

## Refresh Notes

- Refresh before publication because Altium documentation pages are dynamic
- Preserve the `navigation and corresponding-design-object` framing whenever reusing this source
