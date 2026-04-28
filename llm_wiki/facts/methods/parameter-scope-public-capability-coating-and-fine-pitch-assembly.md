---
fact_id: "methods-parameter-scope-public-capability-coating-and-fine-pitch-assembly"
title: "English public coating and fine-pitch assembly pages expose page-scoped post-assembly and hidden-joint parameter claims"
topic: "Public-site capability parameter scope for coating and fine-pitch assembly"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendhil-smt-assembly-product-page-en"
tags: ["internal", "public-site-claim", "parameters", "conformal-coating", "fine-pitch", "bga", "qfn", "smt", "assembly"]
---

# Canonical Summary

> The English public conformal-coating, fine-pitch assembly, and SMT assembly pages contain explicit parameter claims for coating thickness and methods, BGA/QFN pitch, component size, placement accuracy, void targets, rework cycles, and inline inspection scope. These are prompt-support facts only at `public-site claimed capability` level.

## Extracted Public-Site Claimed Parameters

- APT PCB and PCBA conformal-coating pages:
  `acrylic`, `silicone`, `urethane`, and `parylene` coating-family vocabulary;
  `manual spray`, `automated spray`, and `robotic selective coating`;
  `1–5 mil (25–127 μm)` typical coating thickness;
  cure families including `evaporative`, `moisture`, `heat`, and `UV`.
  Source:
  `frontendapt-pcb-pcb-conformal-coating-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json`
  and `frontendapt-pcba-pcb-conformal-coating-page-en` -> `/code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json`
- APT fine-pitch PCBA page:
  `0.3 mm BGA/QFN pitch`, `01005 placement`, `±25 μm placement`, `80–120 μm step stencil`, `BTC void <10%`, `BGA voids below 15%`, `rework ≤3 cycles`, `100% 3D AOI`, and `risk-based 3D AXI`.
  Source:
  `frontendapt-pcba-bga-qfn-fine-pitch-page-en` -> `/code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json`
- HIL SMT assembly page:
  `±25 μm @ 3σ` standard placement, `±8 μm @ 3σ` advanced placement, `0.4 mm standard fine pitch`, `0.2–0.25 mm advanced BGA/CSP`, `0201 standard component size`, `01005 / 008004 advanced`, `3D SPI`, `2D/3D AOI`, `X-ray (AXI), ICT, flying probe, FCT`, and `ionic cleanliness ≤1.56 μg/cm² NaCl eq.`.
  Source:
  `frontendhil-smt-assembly-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/smt-assembly.json`

## Scope

- Claim class:
  `public website claim`
- Page context:
  English APT coating pages, English APT fine-pitch PCBA page, English HIL SMT assembly page
- Language:
  `en`
- Checked date:
  `2026-04-27`

## Consumption Rules

- Keep coating-family vocabulary separate from process-window numbers and separate again from qualification claims.
- Use fine-pitch assembly values only for hidden-joint, stencil, placement, inspection, and rework planning context.
- Treat inline inspection coverage and cleanliness figures as page claims for assembly-service framing, not universal release criteria.
- If a draft enters medical, automotive, RF, or optical territory, pair these parameters with the relevant boundary cards before use.

## Non-Generalization

- These claims are not supplier-independent proof.
- They are not lot capability or shipment-release proof.
- They are not qualification or compliance evidence.
- They are not acceptance thresholds for coating thickness, void percentage, cleanliness, or rework disposition.
- They do not prove every coated board uses the same chemistry or every fine-pitch assembly receives the same AXI or rework scope.

## Blog Usage

- Supports `conformal-coating` empty-image families across telecom, optical-module-adjacent, medical-adjacent, and automotive/EV contexts only when paired with the matching boundary cards.
- Supports `low-void BGA`, `hidden-joint inspection`, and `fine-pitch SMT` families for conservative assembly-process and inspection wording.
- Supports `medical imaging / wearable`, `industrial robotics / control`, and `ai-server / optical high-speed` families for assembly-control vocabulary only.
- Does not unlock compliance, release authority, universal void limits, or chemistry-selection proof.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendHIL/public/static/products/en/smt-assembly.json
