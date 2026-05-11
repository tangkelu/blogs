---
source_id: "infineon-package-family-and-package-detail-identity-grammar"
title: "Infineon Package Family And Package Detail Identity Grammar"
organization: "Infineon Technologies"
owner: "Infineon"
source_type: "package_owner_web_pages"
url: "https://www.infineon.com/package-family/PG-BGA"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "package_owner_naming_authority"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_package_family_and_identifier_field_grammar"
source_origin_path: "official Infineon package-family and package-detail pages"
source_page_range: "PG-BGA family page; PG-VQFN and PG-TQFP package detail pages"
confidence: "high"
topic_tags: ["infineon", "package-family", "package-identifier", "bga", "vqfn", "tqfp", "legacy-alias", "terminals", "variant", "identity-grammar"]
status: "active"
notes: "Official Infineon package pages. Safe for the narrow owner-scoped boundary that package identifiers can be decomposed into material, family, terminal-count, and variant fields, and that some family qualifiers or legacy aliases are explicitly documented by the owner. Do not convert this owner naming scheme into universal cross-vendor package grammar or geometry doctrine."
---

# Source Summary

## What It Covers

- Infineon package-family pages such as `PG-BGA`
- Infineon package-detail pages such as `PG-BGA-49-800`, `PG-VQFN-34-900`, and `PG-TQFP-80-800`
- explicit package-detail fields including `Package Material`, `Package Family`, `Terminals`, and `Variant`

## Why It Matters

- Gives the `E6 package identity grammar` lane a real package-owner source rather than only CAD-library convention
- Supports a stronger boundary that package names can function as compositional identifiers while still remaining owner-scoped

## Extraction Notes

- Safe for Infineon's `PG-BGA` family statement that BGA families may be designated by qualifiers such as low (`L`), thin (`T`), very thin (`V`), finepitch (`F`), and flip-chip (`FC`)
- Safe for Infineon's statement that legacy designations may include `UFBGA` or `WFBGA`
- Safe for Infineon package-detail pages that expose separate fields for:
  - `Package Material`
  - `Package Family`
  - `Terminals`
  - `Variant`
- Safe for `PG-VQFN` package-detail wording that legacy designations may include `MLPQ`
- Safe for `PG-TQFP` package-detail wording that legacy designations may include `TEQFP` or `PQFP`
- Do not rewrite these pages into universal naming law, JEDEC clause-level truth, or any exact footprint geometry default

## Refresh Notes

- Refresh before publication because Infineon package pages are dynamic
- Preserve the `owner-scoped package identity grammar` framing whenever reusing this source
