---
fact_id: "methods-ipc-stencil-guideline-family-and-upstream-print-control-boundary"
title: "IPC public stencil-guideline metadata supports upstream print-control framing, not public stencil-rule extraction"
topic: "IPC stencil guideline family and upstream print-control boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-10"
source_ids:
  - "ipc-7525c-toc"
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
tags: ["ipc", "stencil", "solder-paste", "aperture", "fiducial", "step-stencil", "mixed-technology", "methods", "boundary"]
---

# Canonical Summary

> Public IPC-7525C metadata is strong enough to anchor stencil work to an official stencil-design guideline family and to keep stencil language inside upstream solder-paste print control. It is not strong enough to publish aperture rules, fiducial geometry, fabrication rankings, or process-window claims from the standard.

## Stable Facts

- IPC's public `IPC-7525C` table of contents establishes that stencil guidance exists as a named standards-owner document rather than only as article vocabulary or internal service-page language.
- The public `IPC-7525C` scope names stencil data, data format, Gerber format, aperture list, solder-paste layer, data transfer, panelized stencils, step-and-repeat, image orientation, image location, and identification as stencil-design surfaces.
- The public `IPC-7525C` scope names aperture design, mixed-technology intrusive-soldering context, step stencil design, fiducials, rework and repair stencils, fabrication technologies, mounting, inspection, verification, and cleaning as part of the stencil-guideline family.
- The public `IPC-7525C` front matter states that the document is a guideline and that printing performance depends on many variables, so no single set of design rules can be established.
- The internal stencil page is still the repo's direct upstream process-control support for solder-paste printing setup and aperture-control posture.
- The internal selective-solder page remains supporting context for mixed-technology sequencing and for keeping stencil discussion upstream of later solder-route decisions.

## Conditions And Methods

- Use this card when a rewrite needs guarded wording such as `IPC has a dedicated stencil-design guideline family` or `stencil design belongs to upstream solder-paste print control`.
- Use this card to keep `stencil`, `solder-paste layer`, `aperture list`, `step stencil`, `fiducials`, and `intrusive soldering` inside document-scope and process-surface language rather than article anecdotes.
- Pair this card with `methods-pcba-stencil-selective-solder-and-fine-pitch-controls` when a draft needs process-chain framing from print control into later assembly and inspection.
- Pair this card with `methods-selective-wave-solder-and-mixed-technology-sequencing` when the draft moves from stencil language into mixed-technology route selection.

## Limits And Non-Claims

- This card does not authorize aperture reduction defaults, area-ratio or aspect-ratio rules, home-plate or bow-tie recommendations, or paste-volume formulas as reusable public guidance.
- It does not authorize fiducial geometry, mark-point type, size, location, or equipment-fit conclusions.
- It does not authorize stencil thickness defaults, step-up or step-down selections, or process-window claims for intrusive soldering.
- It does not authorize fabrication-method precision, durability, release-performance, or cost-superiority comparisons across etch, laser, electroform, or hybrid stencils.
- It does not prove yield improvement, defect prevention certainty, delivery outcome, or supplier capability for a named stencil program.

## Source Links

- https://www.ipc.org/TOC/IPC-7525C_TOC.pdf
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
