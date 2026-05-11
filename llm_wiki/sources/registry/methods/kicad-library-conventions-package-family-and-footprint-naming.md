---
source_id: "kicad-library-conventions-package-family-and-footprint-naming"
title: "KiCad Library Conventions Package Family And Footprint Naming"
organization: "KiCad"
owner: "KiCad Libraries Team"
source_type: "software_library_conventions"
url: "https://klc.kicad.org/footprint/f2/f2.1/"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "software_library_conventions"
exact_data_class: "boundary_convention"
scope_type: "cad_owner_package_family_and_footprint_naming_conventions"
source_origin_path: "official KiCad Library Conventions pages"
source_page_range: "F2.1 general footprint naming conventions; F3.4 SMD IC package naming conventions; F3.5 THT IC package naming conventions"
confidence: "high"
topic_tags: ["kicad", "klc", "package-family", "footprint-naming", "qfn", "qfp", "soic", "dip", "je-dec", "pin-count", "identity-grammar"]
status: "active"
notes: "Official KiCad library-convention documentation. Safe for the narrow CAD-owner boundary that package-family labels, pin-count fields, and common industry / JEDEC package naming can be used as footprint identity grammar. Do not convert these library conventions into universal package standards truth or supplier-neutral geometry doctrine."
---

# Source Summary

## What It Covers

- official KiCad general footprint naming conventions
- package-family-first naming patterns such as `QFN-48` and `DIP-20`
- SMD and THT IC package naming templates with package label, pin count, and optional modifiers

## Why It Matters

- Gives the `E6 package identity grammar` lane one clean current-public official source beyond internal glossary wording
- Supports a narrow boundary that package-family labels and pin-count naming belong to CAD-library identity grammar, not universal package-geometry law

## Extraction Notes

- Safe for the boundary that the specific package type is written first in footprint naming
- Safe for examples such as `QFN-48` and `DIP-20`
- Safe for the rule that package name and number of pins are separated by a hyphen
- Safe for KiCad's SMD/THT package naming templates where `PKG` means package name and pin count is a distinct field
- Safe for the note that the `PKG` field refers to the name most commonly used in the industry and generally implies JEDEC naming, while other standards may be used as required
- Do not rewrite these conventions into universal package standards, exact geometry rules, or cross-vendor default grammar for all organizations

## Refresh Notes

- Refresh before publication because KLC pages are dynamic
- Preserve the `CAD-owner library naming convention` framing whenever reusing this source
