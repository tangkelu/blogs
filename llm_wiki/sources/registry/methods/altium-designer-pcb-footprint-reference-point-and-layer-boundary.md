---
source_id: "altium-designer-pcb-footprint-reference-point-and-layer-boundary"
title: "Altium Designer creating a PCB footprint"
organization: "Altium"
owner: "Altium"
source_type: "software_official_docs"
url: "https://www.altium.com/documentation/altium-designer/creating-pcb-footprint?version=21.0"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "software_official_docs"
exact_data_class: "boundary_convention"
scope_type: "cad_owner_footprint_reference_point_and_layer_role_conventions"
source_origin_path: "official Altium Designer documentation page"
source_page_range: "creating a PCB footprint workflow page"
confidence: "high"
topic_tags: ["altium", "footprint", "reference-point", "overlay", "mechanical-layer", "designator", "comment", "pin-1", "courtyard", "library-convention"]
status: "active"
notes: "Official Altium documentation anchor for footprint reference-point handling and layer-role separation. Safe for guarded CAD-owner boundary wording only. Do not convert this into one universal connector-origin doctrine, one mandatory pin-1 origin rule, or one universal board-level installation-mark geometry rule."
---

# Source Summary

## What It Covers

- official Altium workflow for creating a PCB footprint
- explicit footprint workspace `reference point` handling, including `Set Reference`
- layer-role separation across `Top Overlay`, mechanical layers, and `Designator and Comment`
- official footprint-construction context for component outline, courtyard, and body-center handling

## Why It Matters

- Gives the doctrine lane one second current-public CAD-owner surface above `KiCad/KLC` alone.
- Helps state more cleanly that footprint origin and visible/documentation marks are CAD-library construction choices with tool-owner conventions, not one universal package-owner law.

## Extraction Notes

- Safe for the Altium workflow identity that a footprint is built around a workspace `reference point`.
- Safe for the documented rule that the reference point can be changed with `Set Reference`.
- Safe for the documented examples that the reference point may be aligned to a meaningful construction location such as the component center or another user-chosen point.
- Safe for the documented layer split:
  - `Top Overlay` carries visible component overlay graphics
  - mechanical layers can carry courtyard or body-outline style documentation content
  - `Designator and Comment` are separate component-detail objects
- Safe for guarded wording that CAD-owner footprint construction can separate visible marking, body/courtyard documentation, and reference-point handling into different controlled objects.
- Do not rewrite this as a standards-owner doctrine, universal `pin 1` origin law, or universal connector-family marking geometry rule.

## Refresh Notes

- Refresh before publication if a draft depends on exact Altium UI wording, current layer names, or version-specific screenshots.
- Preserve the `CAD-owner footprint-construction boundary` framing whenever reusing this source.
