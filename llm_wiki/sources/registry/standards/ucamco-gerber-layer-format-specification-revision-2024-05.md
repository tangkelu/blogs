---
source_id: "ucamco-gerber-layer-format-specification-revision-2024-05"
title: "Gerber Layer Format Specification Revision 2024.05"
organization: "Ucamco"
owner: "Ucamco"
source_type: "format_owner_specification"
url: "https://www.ucamco.com/files/downloads/file_en/456/gerber-layer-format-specification-revision-2024-05_en.pdf?062f499e1049b8398b808f46167629ee="
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "format_owner_specification"
exact_data_class: "method_boundary"
scope_type: "gerber_layer_coordinate_registration_boundary"
source_origin_path: "official Ucamco Gerber Layer Format Specification revision 2024.05"
source_page_range: "same-coordinate-system and registration sections"
confidence: "high"
topic_tags: ["ucamco", "gerber", "layer-format", "coordinate-system", "registration", "samecoordinates", "projectid"]
status: "active"
notes: "Official Ucamco format-owner specification. Safe for the narrow boundary that Gerber layer data must stay in the same coordinate system for aligned PCB fabrication-data registration, including same-offset and no-mirroring posture. Do not convert this into universal tool workflow law, component-placement UI authority, or manufacturing-readiness claims."
---

# Source Summary

## What It Covers

- Gerber layer format registration and coordinate-system rules
- shared coordinate-system posture for PCB fabrication data
- `.SameCoordinates` and revision-identification vocabulary
- same offset, no mirroring, and 1:1 scale registration posture

## Why It Matters

- Gives the `E7` graphic-alignment lane one stronger public format-owner surface than route-only workflow wording.
- Supports the idea that imported fabrication layers are only aligned when they share a coordinate system and consistent registration posture.

## Extraction Notes

- Safe for the specification wording that all layers in a PCB fabrication-data set must use the same coordinate system.
- Safe for the specification wording that `.SameCoordinates` means the files align.
- Safe for the revision-identification wording around `ident` and `ProjectId` as alignment / revision-check aids.
- Safe for the registration wording that files must align with the same offset, without mirroring, and at 1:1 scale.
- Do not rewrite this spec into UI workflow steps, one-click alignment claims, or universal manufacturing-readiness proof.
- Do not use this source alone to claim package-library authority or tool-shell operation authority.

## Refresh Notes

- Refresh before publication because Ucamco spec downloads are dynamic.
- Preserve the `format-owner coordinate-registration boundary` framing whenever reusing this source.
