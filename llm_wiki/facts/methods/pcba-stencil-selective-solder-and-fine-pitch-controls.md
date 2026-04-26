---
fact_id: "methods-pcba-stencil-selective-solder-and-fine-pitch-controls"
title: "Internal PCBA pages link stencil, selective solder, and fine-pitch controls into one process-control chain"
topic: "PCBA stencil, selective solder, and fine-pitch controls"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendapt-pcba-bga-reballing-page-en"
  - "frontendapt-pcba-smt-tnt-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
tags: ["internal", "pcba", "stencil", "selective-solder", "fine-pitch", "bga", "qfn", "methods"]
---

# Canonical Summary

> The internal PCBA pages connect stencil printing, selective solder, and dense-package controls as a single process-control chain for mixed-technology and fine-pitch assemblies.

## Stable Facts

- The stencil page frames solder-paste printing setup and aperture control as upstream process controls.
- The SMT/THT page links mixed-technology assembly, paste handling, selective solder, and test as one workflow.
- The selective-solder page frames targeted soldering as a way to protect nearby SMDs while finishing through-hole joints.
- The fine-pitch page centers BGA and QFN density as a control and inspection challenge.
- The BGA reballing page adds hidden-joint recovery, pad conditioning, ball placement, and post-rework inspection as a related fine-pitch process-control case.
- The X-ray page covers hidden-joint visibility for BGA and other dense packages.
- The conformal-coating page extends the process chain into board protection after assembly.

## Conditions And Methods

- Use this card when explaining why print control, soldering strategy, package density, and post-assembly protection should be planned together.
- Treat X-ray and coating steps as program-dependent rather than universal.
- Refresh any aperture, thermal, or inspection-coverage number before publication.

## Limits And Non-Claims

- This card does not claim every assembly requires selective solder or conformal coating.
- It does not claim BGA/QFN builds always need X-ray at every step.
- It does not replace a board-specific DFM or process window review.

## Open Questions

- Add a later topic page for `pcba-print-to-protection-process-window`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-reballing.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tnt.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
