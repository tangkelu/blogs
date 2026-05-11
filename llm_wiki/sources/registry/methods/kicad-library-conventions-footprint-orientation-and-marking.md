---
source_id: "kicad-library-conventions-footprint-orientation-and-marking"
title: "KiCad Library Conventions"
organization: "KiCad"
owner: "KiCad Libraries Team"
source_type: "software_library_conventions"
url: "https://klc.kicad.org/"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-08"
retrieved_at: "2026-05-08"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "software_library_conventions"
exact_data_class: "boundary_convention"
scope_type: "cad_owner_library_orientation_and_marking_conventions"
source_origin_path: "official KiCad Library Conventions site"
source_page_range: "F4.2, F5.1, F5.2, F7.2, and related connector-footprint naming sections"
confidence: "high"
topic_tags: ["kicad", "klc", "connector", "pin-1", "orientation", "installation-mark", "f-silks", "f-fab", "library-convention"]
status: "active"
notes: "Official KiCad library-convention documentation. Safe for guarded CAD-owner library orientation and marking conventions only. Do not treat KLC as universal package-owner or standards-owner authority for every connector family."
---

# Source Summary

## What It Covers

- official KiCad library conventions for footprint orientation
- connector-footprint naming and orientation metadata
- `F.SilkS` and `F.Fab` marking expectations for pin-1 and polarity cues
- through-hole footprint anchor placement at pin 1

## Why It Matters

- Gives the package / connector lane one stronger official CAD-owner support point beyond the generic getting-started guide
- Helps separate `library convention` from `package-owner truth`, which is exactly the current connector-origin and installation-mark boundary problem

## Extraction Notes

- Safe for the KiCad library convention that footprints should place `Pin 1` in the upper-left corner when possible
- Safe for the stated exceptions:
  - two-terminal or single-line footprints align `pin 1` on the left side
  - multi-purpose connector footprints should be oriented horizontally with `pin 1` on the left side
- Safe for the marking expectations:
  - `F.SilkS` should draw a polarity marking or `pin-1` designator
  - `F.Fab` should show pin-1 location
  - for connectors, a small arrow indicator next to `pin-1` should be used on `F.Fab`
- Safe for the through-hole convention that the footprint anchor should be placed at the location of `pin 1`
- Do not rewrite these conventions as universal package-owner or all-vendor connector rules

## Refresh Notes

- Refresh before publication if a draft depends on the current KLC version, exact layer-style wording, or current contribution-policy language
- Preserve the `CAD-owner library convention` framing whenever reusing this source
