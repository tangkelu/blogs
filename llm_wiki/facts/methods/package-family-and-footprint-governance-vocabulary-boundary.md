---
fact_id: "methods-package-family-and-footprint-governance-vocabulary-boundary"
title: "Package-family and footprint-governance vocabulary can be reused at boundary level without importing handbook naming grammar"
topic: "Package family and footprint governance vocabulary boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "infineon-package-family-and-package-detail-identity-grammar"
  - "kicad-library-conventions-package-family-and-footprint-naming"
  - "frontendapt-glossary-terms-resource-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-resources-index-en"
tags: ["package", "footprint", "governance", "vocabulary", "bga", "qfn", "qfp", "soic", "dip", "assembly-drawing", "polarity"]
---

# Canonical Summary

> Current internal APT resource coverage supports a conservative package-library vocabulary layer: standard package-family names, footprint as a reusable design object, and documentation-governance concepts such as verified footprint libraries, assembly drawings, and polarity markings. This support is strong enough for prompt routing and guarded blog writing, but it does not authorize handbook naming strings, family-specific geometry tables, or any universal package-default claim.

## Stable Facts

- Official Infineon package-family and package-detail pages show that one owner can structure package identity into explicit fields such as `Package Material`, `Package Family`, `Terminals`, and `Variant`.
- The same Infineon pages show that family qualifiers and legacy aliases can be owner-documented naming surfaces rather than geometry rules, for example BGA qualifier families and legacy aliases such as `UFBGA`, `WFBGA`, `MLPQ`, `TEQFP`, or `PQFP` in their documented owner contexts.
- Official KiCad library conventions support package-family-first footprint naming such as `QFN-48` and `DIP-20`, with package name and pin count kept as distinct identity fields.
- The same KiCad conventions treat SMD and THT package labels as reusable CAD-library naming grammar and say the package field generally follows the name most commonly used in the industry, usually JEDEC naming when appropriate.
- The internal glossary already supports standard English package and layout terms including `Ball Grid Array`, `BGA`, `QFN`, `QFP`, `SOIC`, `DIP`, `Footprint`, `Pad`, `Solder Mask`, `Assembly Drawing`, `Polarity`, `Keepout`, `Drill`, and `Via`.
- The internal DFM guideline treats `component packages and footprint libraries` as a manufacturability-review area rather than as a casual naming convenience.
- The internal DFM guideline treats `pad design` as a controlled review topic and directs designs toward `IPC standards` or `manufacturer-recommended specifications`.
- The internal DFM guideline expects assembly documentation to preserve component outlines, reference designators, and polarity markings.
- The internal DFM guideline uses a self-check posture where standardized and verified footprint libraries are preferred over ad hoc footprint creation.

## Conditions And Methods

- Use package-family names as neutral vocabulary:
  `BGA`, `QFN`, `QFP`, `SOIC`, `DIP`, and related family identities are safe for classification and routing.
- When a draft needs owner-scoped grammar examples, keep them at identifier-field level:
  package family, terminal count, variant, and documented owner alias surfaces.
- When a draft needs naming examples, keep them at CAD-library identity level:
  package-family label first, explicit pin-count field, and common industry / JEDEC naming when appropriate.
- Use `footprint` to mean the package-specific land-pattern and documentation object used for placement, assembly, and review.
- Use `assembly drawing`, `polarity marking`, and `verified footprint library` as governance concepts that belong to release readiness and review completeness.
- Treat footprint selection as family-aware and part-aware.
  The current corpus supports the posture that package identity matters during review, but it does not support one universal footprint geometry rule across all package families and part variants.

## Safe Blog Usage

- Explain that package-family identity helps route the right footprint and review logic.
- Explain that footprint libraries should be standardized, verified, and documented.
- Explain that polarity and assembly-mark information belongs in the documentation package, not just in designer memory.
- Explain that package review is part of manufacturability governance, not only naming.

## Provenance Inventory From Secondary-PDF Lanes

The following logs are provenance inventory only and do not act as authority:

- `/code/blogs/llm_wiki/logs/p4-215c1-2026-5-6-package-lane-c1-package-taxonomy-and-naming.md`
- `/code/blogs/llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`

What they contribute safely:

- package-family grouping examples
- naming-surface inventory
- evidence that handbook naming patterns exist and must be treated as local grammar rather than universal standards truth

## Limits And Non-Claims

- This card does not authorize handbook naming strings such as house-formatted package codes as universal package grammar.
- It does not authorize one universal package-family naming system for every vendor CAD library, package owner, or ERP environment.
- It does not authorize the Infineon owner naming scheme as a cross-vendor package-field standard.
- It does not authorize exact body-size tokens, pitch encodings, or suffix semantics as standards truth.
- It does not authorize family-specific land-pattern dimensions, exposed-pad sizes, or connector-footprint default geometry.
- It does not prove that all suppliers, CAD libraries, or component manufacturers use the same naming structure.

## Open Questions

- Add stronger source coverage later for package-family-specific naming conventions when a package-owner or standards-owner source is required.
- Add a narrower fact later if connector-footprint naming, orientation, and gender vocabulary become high-value enough to justify dedicated authority recovery.

## Source Links

- https://www.infineon.com/package-family/PG-BGA
- https://klc.kicad.org/footprint/f2/f2.1/
- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/resources/en/index.json
