# P4-292 PCB资料 Unified Knowledge Layer First Slice Landing

Date: 2026-05-08
Parent plan: `docs/superpowers/plans/2026-05-08-pcb-ziliao-unified-knowledge-layer-plan.md`
Execution mode: `controller_owned_schema_promotion_and_tracker_integration`

## Purpose

Land the first real `PCB资料` unified-knowledge slice inside `llm_wiki` by creating:

- `pdf_evidence/pcb_ziliao/`
- `facts/local_pdf/`
- the minimum policy and tracker updates required for downstream use

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.

## What Landed

### New evidence layer

- `pdf_evidence/pcb_ziliao/README.md`
- `pdf_evidence/pcb_ziliao/pcba/through-hole-solder-wetting-continuity-example.md`
- `pdf_evidence/pcb_ziliao/pcba/gold-finger-solder-contamination-example.md`
- `pdf_evidence/pcb_ziliao/pcba/flux-residue-visibility-example.md`
- `pdf_evidence/pcb_ziliao/pcba/adhesive-contamination-before-soldering-example.md`
- `pdf_evidence/pcb_ziliao/pcba/horizontal-component-orientation-example.md`
- `pdf_evidence/pcb_ziliao/pcba/vertical-component-polarity-orientation-example.md`
- `pdf_evidence/pcb_ziliao/package/padstack-layer-role-diagram.md`
- `pdf_evidence/pcb_ziliao/package/leaded-footprint-review-dimensions-diagram.md`
- `pdf_evidence/pcb_ziliao/package/chip-footprint-review-dimensions-diagram.md`
- `pdf_evidence/pcb_ziliao/package/bga-array-layout-context.md`

### New curated local-PDF fact layer

- `facts/local_pdf/README.md`
- `facts/local_pdf/padstack-layer-role-visual-boundary.md`
- `facts/local_pdf/footprint-review-dimensions-visual-boundary.md`

### Policy and tracker alignment

- `policies/prompt-consumption-specification.md`
- `policies/exact-data-admission-policy.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Promoted to `local_pdf_fact`

- package padstack layer-role diagram on page `23`
- leaded-package review-dimension diagram on page `36`
- chip-footprint review-dimension diagram on page `38`

Reason:

- these are structurally useful
- they are reusable in blog body with explicit non-numeric scope
- they can be phrased without pretending to be official standards, package-owner recommendations, or current supplier capability

### Kept as `blocked_evidence` / evidence-only

- PCBA defect-photo and orientation visuals from the `158-page` handbook
- BGA array layout context on page `28`

Reason:

- the safe blog wording for the PCBA slice already exists in the admitted boundary facts, so the local images add provenance rather than a new blog-body fact
- the BGA page remains too adjacent to blocked pitch-to-pad numerics for first-slice promotion

## Direct Blog-Consumable Outputs After This Pass

### Now directly consumable as `local_pdf_fact`

- non-numeric padstack layer-role explanation using the preserved local page-23 diagram
- non-numeric footprint-review dimension explanation using the preserved local page-36 and page-38 diagrams

### Still not directly consumable

- handbook thresholds, mil/mm values, and package-size rule rows
- BGA pitch-to-pad tables or any generic BGA land-pattern default
- PCBA accept/reject thresholds, percentages, or compliance-equivalent judgments
- any branded vendor `DFM` UI or workflow screenshots
- any dynamic capability, certification, price, lead-time, or supplier-proof claim

## Tracker Interpretation

- `P4-291 strong_complete` remains true as the old program-level learning closeout
- it must not be misread as meaning this unified-slice implementation was already landed before `P4-292`
- future continuation should restart from this log plus the `2026-05-08` unified-model plan
