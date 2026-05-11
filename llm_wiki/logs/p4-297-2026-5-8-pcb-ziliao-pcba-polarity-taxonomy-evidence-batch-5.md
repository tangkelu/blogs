# P4-297 PCB资料 PCBA Polarity Taxonomy Evidence Batch 5

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the next clean `PCBA` polarity-taxonomy image batch inside `pdf_evidence/pcb_ziliao/pcba/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New PCBA evidence records

- `pdf_evidence/pcb_ziliao/pcba/radial-capacitor-lead-orientation-example.md`
- `pdf_evidence/pcb_ziliao/pcba/reversed-polarity-example.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- radial capacitor lead-orientation diagram from page `46`
- reversed-polarity diagram from page `46`

Reason:

- the safe reusable value is polarity-direction and anomaly naming vocabulary
- the admitted wording already exists in the current `component-orientation-and-polarity` fact layer
- the local diagrams still do not justify `local_pdf_fact` promotion because they remain secondary visual examples rather than new body-ready authority

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- radial capacitor lead-orientation vocabulary
- reversed-polarity example vocabulary

### Still not directly consumable from the local diagrams themselves

- lead-length requirements
- universal polarity installation rules
- acceptability judgments
- field-failure certainty

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-297` is the next `PCBA` polarity-taxonomy evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
