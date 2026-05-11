# P4-295 PCB资料 PCBA Anomaly Taxonomy Evidence Batch 3

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the next clean `PCBA` anomaly-taxonomy image batch inside `pdf_evidence/pcb_ziliao/pcba/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New PCBA evidence records

- `pdf_evidence/pcb_ziliao/pcba/side-mounted-chip-placement-example.md`
- `pdf_evidence/pcb_ziliao/pcba/upside-down-chip-placement-example.md`
- `pdf_evidence/pcb_ziliao/pcba/tombstone-defect-example.md`
- `pdf_evidence/pcb_ziliao/pcba/coplanarity-defect-example.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- side-mounted chip placement image from page `150`
- upside-down chip placement image from page `150`
- tombstone defect image from page `151`
- coplanarity defect image from page `151`

Reason:

- the safe reusable value is anomaly-family naming and visual taxonomy
- the admitted wording already exists in the current `pcba-defect-photo-taxonomy` fact layer
- these images remain too close to handbook `best / acceptable / unacceptable` framing to justify `local_pdf_fact` promotion

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- side-mounted chip placement taxonomy wording
- upside-down chip placement taxonomy wording
- tombstone defect taxonomy wording
- coplanarity defect taxonomy wording

### Still not directly consumable from the local images themselves

- severity ranking
- accept/reject or release decisions
- process-window or root-cause conclusions
- any standards-equivalent workmanship judgment

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-295` is the next `PCBA` anomaly-taxonomy evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
