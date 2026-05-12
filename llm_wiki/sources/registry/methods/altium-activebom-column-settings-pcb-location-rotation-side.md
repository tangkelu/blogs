---
source_id: "altium-activebom-column-settings-pcb-location-rotation-side"
title: "Altium Designer Dialog Column Settings"
organization: "Altium"
owner: "Altium"
source_type: "software_vendor_documentation"
url: "https://www.altium.com/documentation/altium-designer/activebom-dlg-dialogcolumnsettingsselect-columns-activebom-ad?version=18.0"
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
scope_type: "bom_columns_with_pcb_location_rotation_and_side_metadata"
source_origin_path: "official Altium documentation page"
source_page_range: "Data Sources and available columns for PCB-derived metadata"
confidence: "medium"
topic_tags: ["altium", "activebom", "bom-columns", "pcb-location", "rotation", "side-of-board", "bom"]
status: "active"
notes: "Official Altium documentation. Safe for the narrow boundary that BOM-column configuration can expose PCB-derived location, rotation, and side-of-board metadata. Do not generalize this into placement correctness, package alignment closure, or assembly-progress tracking."
---

# Source Summary

## What It Covers

- ActiveBOM column settings
- PCB-derived BOM columns
- component location, rotation, and side-of-board metadata

## Why It Matters

- Gives the `E7` visual-BOM lane one second current-public official source for BOM-visible board-position context
- Strengthens the narrow boundary that a BOM review surface can expose PCB-context metadata without proving assembly correctness

## Extraction Notes

- Safe for the boundary that BOM columns can include PCB location, rotation, and side-of-board data
- Safe for the idea that board-position context may be reviewed from the BOM surface
- Do not rewrite this page into pad-level geometry closure, one-pin identification guarantees, or progress-marking claims

## Refresh Notes

- Refresh before publication because Altium documentation pages are dynamic
- Preserve the `PCB-derived metadata columns` framing whenever reusing this source
