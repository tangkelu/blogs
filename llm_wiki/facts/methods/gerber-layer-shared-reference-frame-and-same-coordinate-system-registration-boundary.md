---
fact_id: "methods-gerber-layer-shared-reference-frame-and-same-coordinate-system-registration-boundary"
title: "Gerber layer graphics can be reused as shared-reference-frame and same-coordinate-system registration only, not as UI or whole-package alignment proof"
topic: "Gerber layer shared-reference-frame and same-coordinate-system registration boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "method_boundary"
scope_type: "gerber_shared_reference_frame_registration_boundary"
canonical_unit_policy: "Preserve Ucamco wording such as same coordinate system, .SameCoordinates, ident, ProjectId, same offset, no mirroring, and 1:1 scale. Do not normalize this into UI-shell workflow authority, whole-package correctness, or universal alignment-readiness doctrine."
source_ids:
  - "ucamco-gerber-layer-format-specification-revision-2024-05"
tags: ["gerber", "ucamco", "graphic-alignment", "shared-reference-frame", "same-coordinate-system", "registration", "revision-id", "project-id"]
---

# Canonical Summary

> Current public format-owner coverage is strong enough to land one narrow graphics-registration boundary. Ucamco's Gerber Layer Format Specification 2024.05 explicitly says all PCB fabrication-data layers must share the same coordinate system, `.SameCoordinates` means the files align, `ident` and `ProjectId` help distinguish revision / coordinate-system context, and the files should align with the same offset, no mirroring, and 1:1 scale. Together, these support conservative wording that graphic alignment can be treated as a shared-reference-frame and same-coordinate-system registration problem. They do not authorize UI-step sequences, auto-fix sufficiency, whole-package readiness, or branded tool superiority.

## Stable Facts

- Ucamco explicitly states that all layers in a PCB fabrication-data set must use the same coordinate system.
- Ucamco states that `.SameCoordinates` means the files align.
- Ucamco uses `ident` and `ProjectId` as revision / coordinate-system identity aids.
- Ucamco states that files must align with the same offset, without mirroring, and at 1:1 scale.
- These rules are enough to support guarded wording that imported graphics or layers are only aligned when they share a coordinate system and registration posture.

## Conditions And Methods

- Use this card when a prompt needs a format-owner explanation for graphic alignment, imported layer mismatch, or revision-comparison registration.
- Use it to keep graphics alignment inside shared-reference-frame and same-coordinate-system language.
- Use it to distinguish registration from UI operation sequence.
- Do not generalize this card into component-placement, package-origin, or installation-mark doctrine.
- Keep local correction, shortcut keys, and button sequences outside this fact unless a separate owner source is added.

## Safe Blog Usage

- Explain that graphic alignment failures are often shared-reference-frame problems first.
- Explain that matching coordinate systems, offsets, and scale is part of registration, not a convenience feature.
- Explain that revision identifiers help check whether files belong to the same aligned set.

## Limits And Non-Claims

- This card does not authorize any UI shortcut or menu-path workflow.
- It does not authorize one-click alignment sufficiency or auto-fix guarantees.
- It does not authorize whole-package correctness, manufacturability, or assembly-readiness claims.
- It does not authorize local-subregion move workflows, package-library authority, or coordinate-to-footprint doctrine.

## Relationship To Local PCB资料 Intake

- This card upgrades `简单好用！再也不用担心PCB图形对齐问题.pdf` above the older route-only ceiling for:
  - shared-reference-frame correction
  - single-layer and multi-layer same-coordinate-system registration
  - revision-comparison alignment
- It does not upgrade the article's local-subregion move workflow, UI-step sequence, or library-adjustment residue.

## Source Links

- https://www.ucamco.com/files/downloads/file_en/456/gerber-layer-format-specification-revision-2024-05_en.pdf?062f499e1049b8398b808f46167629ee=
