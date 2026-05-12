---
fact_id: "methods-fiducial-optical-alignment-global-local-scope-and-local-correction-boundary"
title: "Fiducials can be reused as optical alignment references with board-global versus footprint-local scope and local-correction posture, but not as universal geometry or count doctrine"
topic: "Fiducial optical-alignment global/local scope and local-correction boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "machine_owner_plus_cad_owner_fiducial_boundary"
canonical_unit_policy: "Preserve source-owner wording such as fiducial mark, global to board, local to footprint, local marks, and local correction. Do not rewrite these into universal geometry, count, corner-placement, or package-specific mandatory local-mark doctrine."
source_ids:
  - "yamaha-smt-glossary-fiducial-mark"
  - "yamaha-yrm-d-multiple-marks-and-local-correction"
  - "kicad-pcb-editor-fiducial-fabrication-property"
tags: ["fiducial", "mark", "optical-alignment", "global-to-board", "local-to-footprint", "local-correction", "yamaha", "kicad"]
---

# Canonical Summary

> Current public machine-owner and CAD-owner coverage is strong enough to land one narrow fiducial boundary. Yamaha's SMT glossary supports `fiducial mark` as a board reference point used by placement and printing equipment for high-precision alignment. Yamaha's YRM-D feature page supports `multiple marks`, `individual local marks`, and `local correction` posture, including the guarded context that local marks improve accuracy on poor-accuracy PCBs. KiCad's PCB Editor reference explicitly distinguishes `Fiducial, global to board` from `Fiducial, local to footprint`. Together, these sources support conservative wording that fiducials can be treated as optical alignment references, that board-global and footprint-local scope are real controlled distinctions, and that local marks belong to local-correction posture. They do not authorize geometry values, count defaults, mandatory package-specific local marks, or outcome guarantees.

## Stable Facts

- Yamaha's SMT glossary defines a fiducial mark as a printed mark used as a board reference point.
- Yamaha's glossary states that chip mounters and printing presses use fiducial marks for high-precision alignment.
- Yamaha's YRM-D feature page states that the equipment detects multiple marks to maintain accuracy.
- Yamaha's YRM-D feature page states that the equipment detects individual local marks and locally corrects positions.
- Yamaha's YRM-D feature page states that individual local marks improve accuracy on poor-accuracy PCBs.
- KiCad's PCB Editor reference exposes `Fabrication_Property` options `Fiducial, global to board` and `Fiducial, local to footprint`.
- KiCad states that this fabrication property affects Gerber X2 output only.
- The combined source layer is strong enough for guarded wording that fiducials can be discussed at `board-global` versus `footprint-local` scope and that local fiducials can belong to local-correction posture.

## Conditions And Methods

- Use this card when a prompt needs stronger public support than article language alone for `fiducial` or `Mark` as optical alignment reference.
- Use `board-global` versus `footprint-local` scope split rather than rewriting this lane into universal `board / panel / component` doctrine.
- Use `local correction` only as a machine-owner posture showing why local marks can matter.
  Do not rewrite it as a mandatory rule for every package or every assembly line.
- Use Yamaha as machine-owner alignment vocabulary and local-correction support.
  Use KiCad as CAD-owner scope-label support.
- Keep exact series- or machine-specific behavior tied to the cited owner source instead of converting it into cross-vendor law.
- Pair this card with [cam-data-exchange-format-boundary.md](/code/blogs/llm_wiki/facts/methods/cam-data-exchange-format-boundary.md) only when the prompt needs separate Gerber attribute vocabulary.
  Do not collapse CAM vocabulary and SMT alignment posture into one doctrine card.

## Safe Blog Usage

- Explain that fiducials are alignment references rather than arbitrary decorative marks.
- Explain that a controlled distinction can exist between board-global fiducials and footprint-local fiducials.
- Explain that local fiducials can support local correction posture in higher-accuracy or poor-accuracy board contexts.
- Explain that exact geometry and mandatory rules still depend on stronger owner or standards authority than this card provides.

## Limits And Non-Claims

- This card does not authorize fiducial diameter, opening, copper-clearance, or keepout numbers.
- It does not authorize required mark count, diagonal corner arrangement, panel defaults, or board-edge distance rules.
- It does not authorize universal `QFP`, `BGA`, or other package-specific mandatory local-fiducial rules.
- It does not authorize asymmetry, visual cleanliness, contamination avoidance, or obstruction criteria as official reusable doctrine.
- It does not authorize no-mark workaround guidance such as fixture-added marks or stencil / pad substitutions.
- It does not authorize machine-precision, efficiency, throughput, quality, cost, or schedule outcome claims.

## Relationship To Local PCB资料 Intake

- This card upgrades `PCB板的Mark点设计对SMT重要性.pdf` above pure route-only status for one narrow sub-surface:
  - `fiducial / Mark` as optical alignment reference
  - `board-global` versus `footprint-local` scope split
  - `local marks` as local-correction posture
- It does not yet promote the same article's:
  - panel-level scope wording
  - asymmetry as orientation-disambiguation wording
  - visibility / cleanliness recognition conditions
  - geometry, count, or workaround claims

## Source Links

- https://global.yamaha-motor.com/business/smt/glossary/
- https://global.yamaha-motor.com/business/smt/dispenser/yrm-d/feature/
- https://docs.kicad.org/master/en/pcbnew/pcbnew.html
