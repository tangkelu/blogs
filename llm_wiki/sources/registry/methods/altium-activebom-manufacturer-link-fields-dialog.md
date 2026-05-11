---
source_id: "altium-activebom-manufacturer-link-fields-dialog"
title: "Altium Designer Manufacturer Link Fields Dialog"
organization: "Altium"
owner: "Altium"
source_type: "software_vendor_documentation"
url: "https://www.altium.com/documentation/altium-designer/activebom-dlg-manufacturerlinkfieldsdialogdefine-manufacturer-link-fields-ad"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "software_vendor_documentation"
exact_data_class: "boundary_convention"
scope_type: "bom_parameter_mapping_manufacturer_name_and_part_number"
source_origin_path: "official Altium documentation page"
source_page_range: "dialog description for manufacturer link fields"
confidence: "high"
topic_tags: ["altium", "activebom", "manufacturer-link-fields", "manufacturer-name", "manufacturer-part-number", "parameter-mapping", "bom"]
status: "active"
notes: "Official Altium documentation. Safe for the narrow boundary that BOM parameter mapping can explicitly bind `Manufacturer Name` and `Manufacturer Part Number` fields. Do not convert this into universal PLM normalization doctrine or automatic matching guarantees."
---

# Source Summary

## What It Covers

- Altium manufacturer-link field mapping
- explicit parameter mapping for `Manufacturer Name`
- explicit parameter mapping for `Manufacturer Part Number`

## Why It Matters

- Gives the `E6` BOM identity lane one stronger current-public anchor that manufacturer identity fields should stay explicit instead of collapsed into free-text BOM notes
- Helps separate identity-field hygiene from branded article workflow claims

## Extraction Notes

- Safe for the existence of explicit link fields for `Manufacturer Name` and `Manufacturer Part Number`
- Safe for the boundary that manufacturer identity is a mapped BOM parameter surface, not just an informal comment field
- Do not rewrite this page into universal schema sufficiency, full data-model closure, or automatic matching success claims

## Refresh Notes

- Refresh before publication because Altium documentation pages are dynamic
- Preserve the `explicit mapped manufacturer fields` framing whenever reusing this source
