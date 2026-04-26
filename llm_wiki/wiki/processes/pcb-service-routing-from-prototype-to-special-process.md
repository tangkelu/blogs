---
topic_id: "processes-pcb-service-routing-from-prototype-to-special-process"
title: "PCB Service Routing From Prototype To Special Process"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-pcb-prototype-quickturn-and-volume-routing"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-conformal-coating-source-coverage"
source_ids:
  - "frontendapt-pcb-pcb-prototype-page-en"
  - "frontendapt-pcb-quick-turn-pcb-page-en"
  - "frontendapt-pcb-npi-small-batch-pcb-manufacturing-page-en"
  - "frontendapt-pcb-mass-production-pcb-manufacturing-page-en"
  - "frontendapt-pcb-index-page-en"
  - "frontendapt-pcb-industry-solutions-page-en"
  - "frontendapt-pcb-fr4-pcb-page-en"
  - "frontendapt-pcb-high-tg-pcb-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "frontendapt-pcb-special-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-profiling-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
tags: ["pcb", "prototype", "quick-turn", "npi", "mass-production", "stackup", "special-process", "profiling", "conformal-coating"]
---

# Definition

> PCB service routing from prototype to special process is the internal planning frame that decides both operating mode and board family: whether a build is handled as prototype, quick-turn, NPI/small-batch, or mass production, and whether the construction itself stays within baseline FR-4/high-Tg work or moves into heavy-copper, multilayer, or specialty-process routing.

## Why This Topic Matters

- Internal PCB pages become hard to reuse if `prototype`, `quick-turn`, `stackup`, `special PCB`, and `heavy copper` are all treated as one generic manufacturing claim.
- The APT PCB corpus now separates operating-speed routes from construction-family routes, which is more useful for prompts and planning than a flat product list.
- This topic page gives one stable frame for choosing the right service language before drafting customer-facing PCB manufacturing content.

## Stable Facts

- The internal PCB routing pages separate `prototype`, `quick-turn`, `NPI/small-batch`, and `mass production` as different operating postures with different ramp and scale language.
- The PCB index page acts as the top-level taxonomy that keeps those routes inside one unified PCB portfolio.
- The industry-solutions page adds application segmentation, connecting stackup and rollout framing to different end markets.
- FR-4 acts as the baseline fabrication family while high-Tg adds a thermally stronger laminate posture for more demanding multilayer or lead-free contexts.
- Heavy copper is treated as a separate power and thermal route rather than just a thicker version of standard FR-4.
- Stackup and multilayer-lamination pages define construction planning, including multilayer sequencing and hybrid-material routing.
- The special-PCB page widens the taxonomy to ceramic, metal-core, flex, rigid-flex, RF, carbon-ink, gold-finger, and other non-standard constructions.
- Profiling and conformal coating extend the manufacturing route into edge-finish/singulation decisions and downstream protection steps.

## Engineering Boundaries

- Keep service speed or volume routing separate from board-family selection.
- Do not treat FR-4, high-Tg, heavy copper, rigid-flex, ceramic, RF, and other special constructions as interchangeable substitutions.
- Keep stackup planning, lamination route, profiling method, and protection chemistry as separate engineering decisions.
- Treat industry-solution framing as support for application fit, not as proof of certification or customer qualification.
- Refresh all exact values for layer count, copper weight, Tg/Td, turnaround, profiling tolerance, and coating chemistry before publication.

## Common Misreadings

- `Quick-turn` does not mean every special-process family is available on the same delivery posture.
- `Prototype` does not automatically mean low-control or non-production-like fabrication.
- `High-Tg` does not replace the need to discuss actual stackup, lamination route, or thermal constraints.
- `Heavy copper` is not just a material adjective; it changes current-path and manufacturability framing.
- `Conformal coating` is not a substitute for laminate choice, stackup design, or environmental qualification planning.

## Must Refresh Before Publishing

- Lead-time claims for prototype, quick-turn, NPI, and mass-production routing
- Exact unit-count or volume thresholds between service routes
- Copper-weight, layer-count, Tg/Td, and impedance-tolerance claims
- Special-process availability, profiling tolerances, and coating-process specifics
- Industry certification, qualification, and experience claims

## Related Fact Cards

- `methods-pcb-prototype-quickturn-and-volume-routing`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-conformal-coating-source-coverage`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-prototype.json
- /code/hileap/frontendAPT/public/static/pcb/en/quick-turn-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/npi-small-batch-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcb/en/mass-production-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcb/en/index.json
- /code/hileap/frontendAPT/public/static/pcb/en/industry-solutions.json
- /code/hileap/frontendAPT/public/static/pcb/en/fr4-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-tg-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/heavy-copper-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-stack-up.json
- /code/hileap/frontendAPT/public/static/pcb/en/multi-layer-laminated-structure.json
- /code/hileap/frontendAPT/public/static/pcb/en/special-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-profiling.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
