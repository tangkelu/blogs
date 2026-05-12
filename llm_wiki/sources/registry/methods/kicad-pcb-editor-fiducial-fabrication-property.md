---
source_id: "kicad-pcb-editor-fiducial-fabrication-property"
title: "KiCad PCB Editor Reference Manual"
organization: "KiCad Documentation Team"
owner: "KiCad Documentation Team"
source_type: "software_official_docs"
url: "https://docs.kicad.org/master/en/pcbnew/pcbnew.html"
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
scope_type: "cad_owner_fiducial_scope_property"
source_origin_path: "official KiCad PCB Editor reference manual footprint properties section"
source_page_range: "Fabrication_Property options for footprint properties"
confidence: "high"
topic_tags: ["kicad", "pcbnew", "fiducial", "global-to-board", "local-to-footprint", "gerber-x2", "footprint-properties"]
status: "active"
notes: "Official KiCad PCB Editor documentation. Safe for the guarded CAD-owner distinction that footprint fabrication properties can mark fiducials as `global to board` or `local to footprint`, and that this affects Gerber X2 output only. Do not rewrite this source into universal fabrication doctrine, package-owner truth, or board-level geometry rules."
---

# Source Summary

## What It Covers

- official KiCad PCB Editor footprint-property documentation
- `Fabrication_Property` options for fiducials
- explicit distinction between board-global and footprint-local fiducials
- note that the property affects Gerber X2 output only

## Why It Matters

- Gives the `E4 Mark` lane one current-public CAD-owner source for a clean `global vs local` fiducial scope split
- Helps keep this lane grounded in explicit software-owner terminology rather than article-only paraphrase

## Extraction Notes

- Safe for the explicit property labels `Fiducial, global to board` and `Fiducial, local to footprint`.
- Safe for the note that this fabrication property affects Gerber X2 output only.
- Safe for guarded wording that CAD tooling can distinguish board-global from footprint-local fiducial scope.
- Do not rewrite this source into mandatory assembly-process rules, mark placement defaults, or universal panel / board / package doctrine.
- Do not use this source as proof that one CAD property setting alone guarantees manufacturing readiness.

## Refresh Notes

- Refresh before publication because the `master` documentation path is dynamic.
- Preserve the `CAD-owner fiducial-scope property` framing whenever reusing this source.
