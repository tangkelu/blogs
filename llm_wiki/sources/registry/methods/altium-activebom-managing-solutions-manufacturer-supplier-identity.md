---
source_id: "altium-activebom-managing-solutions-manufacturer-supplier-identity"
title: "Altium Designer ActiveBOM Managing Solutions"
organization: "Altium"
owner: "Altium"
source_type: "software_vendor_documentation"
url: "https://www.altium.com/documentation/altium-designer/activebom/managing-solutions"
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
scope_type: "bom_identity_fields_manufacturer_and_supplier_linkage"
source_origin_path: "official Altium documentation page"
source_page_range: "manufacturer part and supplier part identity sections"
confidence: "high"
topic_tags: ["altium", "activebom", "bom", "manufacturer-part", "supplier-part", "identity-fields", "boundary"]
status: "active"
notes: "Official Altium documentation. Safe for the narrow software-vendor boundary that BOM solutions can distinguish manufacturer part identity from supplier part identity. Do not generalize this into universal ERP/PLM schema law or procurement outcome claims."
---

# Source Summary

## What It Covers

- Altium ActiveBOM solution handling
- manufacturer part identity versus supplier part identity
- BOM-side linking between design part, manufacturer part, and supply entries

## Why It Matters

- Gives the `E6` BOM lane one current-public official source for separating electrical/design identity from purchasing-facing identity
- Supports a narrower BOM identity-field boundary than the existing route-only article note

## Extraction Notes

- Safe for the documentation surface that ActiveBOM manages `Manufacturer Part` and linked `Supplier Part` identities as separate objects
- Safe for the boundary that sourcing review depends on explicit manufacturer and supplier identity rather than an undifferentiated BOM string
- Safe for the idea that one design item can require explicit solution selection and identity reconciliation
- Do not rewrite this page into universal sourcing sufficiency, availability, price, or lead-time claims

## Refresh Notes

- Refresh before publication because Altium documentation pages are dynamic
- Preserve the `identity-field separation` framing whenever reusing this source
