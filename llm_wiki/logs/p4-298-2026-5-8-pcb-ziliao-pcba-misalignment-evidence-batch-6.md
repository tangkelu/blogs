# P4-298 PCB资料 PCBA Misalignment Evidence Batch 6

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing a clean `PCBA` chip-misalignment image inside `pdf_evidence/pcb_ziliao/pcba/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New PCBA evidence record

- `pdf_evidence/pcb_ziliao/pcba/chip-component-misalignment-example.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- chip component misalignment image from page `131`

Reason:

- the safe reusable value is anomaly-family naming and visual taxonomy
- the admitted wording already exists in the current `pcba-defect-photo-taxonomy` fact layer
- the local image still does not justify `local_pdf_fact` promotion because handbook offset and acceptability thresholds remain blocked

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- chip component misalignment taxonomy wording

### Still not directly consumable from the local image itself

- offset percentages
- terminal overhang limits
- acceptability or release decisions

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-298` is the next `PCBA` misalignment evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
