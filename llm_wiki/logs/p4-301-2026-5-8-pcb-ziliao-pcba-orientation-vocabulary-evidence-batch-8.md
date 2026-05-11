# P4-301 PCB资料 PCBA Orientation Vocabulary Evidence Batch 8

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the remaining clean page-`44` orientation-vocabulary concept records inside `pdf_evidence/pcb_ziliao/pcba/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New PCBA evidence records

- `pdf_evidence/pcb_ziliao/pcba/component-polarity-visibility-example.md`
- `pdf_evidence/pcb_ziliao/pcba/readable-marking-direction-example.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- component-polarity-visibility diagram from page `44`
- readable-marking-direction diagram from page `44`

Reason:

- the safe reusable value is English-only orientation and polarity-marking vocabulary
- the admitted wording already exists in the current `component-orientation-and-polarity-inspection-vocabulary-boundary` fact layer
- the local diagram still does not justify `local_pdf_fact` promotion because handbook acceptability labels and universal install-rule implications remain blocked

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- component polarity visibility vocabulary
- readable marking direction vocabulary

### Still not directly consumable from the local diagram itself

- best/acceptable/unacceptable reconstruction
- universal polarity installation rules
- release or workmanship-compliance conclusions

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-301` is the next `PCBA` orientation-vocabulary evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
