# P4-300 PCB资料 PCBA Jumper Clearance Evidence Batch 7

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the remaining safe `PCBA` jumper-clearance structural-context image inside `pdf_evidence/pcb_ziliao/pcba/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New PCBA evidence record

- `pdf_evidence/pcb_ziliao/pcba/jumper-wire-path-clearance-context.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- jumper-wire path-clearance context image from page `121`

Reason:

- the safe reusable value is local route-shape and clearance-context vocabulary only
- the admitted wording already exists in the current `board-warpage-and-jumper-wire-inspection-vocabulary-boundary` fact layer
- the local image still does not justify `local_pdf_fact` promotion because handbook gauge, insulation, and repair-prescription claims remain blocked

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- jumper-wire path-clearance context vocabulary

### Still not directly consumable from the local image itself

- wire gauge prescriptions
- insulation rules
- approved repair claims
- dimensional spacing rules

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-300` is the next `PCBA` jumper-clearance evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
