---
topic_id: "processes-pcb-service-routing-from-prototype-to-special-process"
title: "PCB Service Routing From Prototype To Special Process"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
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

> PCB service routing from prototype to special process is a planning boundary that separates operating mode from construction family. It decides whether a build is handled as prototype, quick-turn, `NPI/small-batch`, or mass production, and whether the board remains in baseline `FR-4` or `high-Tg` routing or moves into heavy-copper, thermal-platform, multilayer-lamination, profiling, coating, or broader special-process routing. This lane does not authorize universal availability across every service route, exact capability numerics, certification or qualification proof, or customer-program approval claims.

## Routing Guidance

- Use this page when a draft mixes service posture and board-family wording into one flat `PCB manufacturing` claim.
- Route `prototype`, `quick-turn`, `NPI/small-batch`, and `mass production` through the operating-posture fact card before discussing any board-family choice.
- Route `FR-4`, `high-Tg`, heavy copper, multilayer stackup, lamination planning, and special-process board families through the stackup and baseline-family fact card rather than through speed or volume language.
- Route metal-core, ceramic, and other heat-driven platform choices through the thermal-platform-selection fact card instead of treating `high thermal` as one interchangeable material route.
- Route profiling and conformal-coating wording as downstream finishing or protection steps after the main board family and service posture are established.
- Route industry-fit or market-segmentation language as context only, not as proof that a service route or board family is qualified for a specific customer program.

## Why This Topic Matters

- Internal PCB pages become misleading when `prototype`, `quick-turn`, stackup class, thermal platform, profiling, and coating are all treated as one generic service promise.
- The already-landed facts separate operating posture from material family, stackup planning, thermal-platform selection, and downstream protection steps.
- This page turns that separation into an active routing surface so future rewrites can choose the right service lane without implying universal availability or qualification proof.

## Stable Facts

- The landed routing card separates `prototype`, `quick-turn`, `NPI/small-batch`, and `mass production` as distinct operating postures with different speed, release-readiness, scale-up, and industry-fit framing.
- The PCB index page provides a top-level portfolio route that keeps these service postures inside one broader PCB offering.
- The industry-solutions page adds application-fit context, but does not change the need to keep service route and board-family selection separate.
- The landed stackup and special-process card treats `FR-4` and `high-Tg` as baseline laminate families, heavy copper as a separate current and thermal route, and multilayer stackup or sequential lamination as distinct planning layers.
- The same landed card treats special-process routes such as ceramic, metal-core, flex, rigid-flex, RF, gold-finger, carbon-ink, and related non-standard constructions as separate board-family branches rather than interchangeable variants of standard rigid boards.
- The landed thermal-platform card treats `MCPCB`, heavy copper, and ceramic as distinct thermal-path platforms with different tradeoff posture rather than as one merged `high thermal` family.
- The landed conformal-coating card treats coating as a separate protection step with its own standards metadata, chemistry context, and internal process framing rather than as a bare-board material property.
- Profiling and singulation choices such as `V-score`, tab routing, laser singulation, edge plating, and castellation belong to downstream manufacturing-route selection after the main construction path is chosen.

## Engineering Boundaries

### 1. Service-Posture Boundary

- Safe wording: the build is being routed as `prototype`, `quick-turn`, `NPI/small-batch`, or `mass production` depending on validation, urgency, and release posture.
- Safe companion fact: `methods-pcb-prototype-quickturn-and-volume-routing`.
- Keep service posture separate from board-family identity, exact lead-time promises, and program-readiness claims.

### 2. Baseline Versus Special-Process Family Boundary

- Safe wording: the board stays in baseline `FR-4` or `high-Tg` routing, or escalates into heavy-copper, multilayer-lamination, or broader special-process routing.
- Safe companion fact: `methods-pcb-stackup-special-process-and-baseline-families`.
- Keep laminate family, stackup architecture, lamination sequence, and special-process family selection as separate planning layers.

### 3. Thermal-Platform Boundary

- Safe wording: thermal-driven builds should be routed by platform class such as heavy copper, `MCPCB`, or ceramic rather than by a generic `high thermal PCB` label.
- Safe companion fact: `methods-thermal-pcb-platform-selection-posture`.
- Keep thermal-platform selection separate from generic rigid-board stackup language and from claims that one thermal material solves every heat problem.

### 4. Downstream Profiling And Protection Boundary

- Safe wording: depaneling, profile finish, castellation, edge plating, and conformal coating are downstream route choices after the core build family is chosen.
- Safe companion facts: `methods-pcb-stackup-special-process-and-baseline-families`, `methods-conformal-coating-source-coverage`.
- Keep coating chemistry, masking, process planning, and profile method separate from laminate identity or qualification claims.

## Blocked Claims

- Universal availability claims remain blocked, including wording that every special-process family is available in every prototype, quick-turn, `NPI`, or volume route.
- Exact capability numerics remain blocked, including lead times, quantity thresholds, copper weights, layer counts, `Tg/Td`, profiling tolerances, coating thickness, cure windows, or material-property figures.
- Certification or qualification claims remain blocked, including industry certification, standards compliance, qualified-process, qualified-board, or approved-environment wording.
- Customer-program or market-approval claims remain blocked, including sector-proven, deployment-proven, customer-approved, or program-qualified route language.

## Common Misreadings

- `Quick-turn` is sometimes misread as proof that every special-process family inherits the same accelerated path; here it only supports a schedule posture that must remain separate from board-family complexity.
- `Prototype` is sometimes misread as a low-control or non-production-like path; here it only supports a validation-stage service route.
- `High-Tg` is sometimes misread as a complete thermal-platform answer; here it remains a baseline laminate-family decision that does not replace stackup or platform planning.
- `Heavy copper` is sometimes misread as just a thicker version of standard rigid board work; here it remains a separate current and thermal route.
- `Conformal coating` is sometimes misread as proof of environmental qualification or as a substitute for laminate and stackup choice; here it only supports downstream protection-process framing.

## Safe Draft Routing

### `pcb manufacturing` mixed-route drafts

- Supported route: separate operating mode first, then baseline versus special-process family, then thermal-platform choice, then downstream profiling or coating steps.
- Keep blocked: exact service thresholds, universal special-process availability, certification or qualification claims, and customer-program approval claims.

## Must Refresh Before Publishing

- Any exact turnaround window, rush commitment, or unit-count threshold between prototype, quick-turn, `NPI`, and volume routing.
- Any exact numeric for copper weight, layer count, `Tg/Td`, impedance tolerance, profile tolerance, coating thickness, cure schedule, or thermal performance.
- Any statement that turns industry-solution or market-segmentation language into qualification, certification, or sector-acceptance proof.
- Any statement that claims every special-process family is available under the same schedule, release, or production posture.

## Related Facts And Source Scope

- `methods-pcb-prototype-quickturn-and-volume-routing`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-conformal-coating-source-coverage`

## Source Scope

- Service-posture authority comes from already-landed internal APT routing pages for prototype, quick-turn, `NPI/small-batch`, and mass-production framing.
- Board-family, stackup, special-process, profiling, and coating-routing authority comes from already-landed internal APT PCB family and process pages referenced by the linked fact cards.
- Thermal-platform separation comes from already-landed internal APT and HIL thermal board pages referenced by the linked thermal-platform fact card.
- Outside current scope: exact capability commitments, universal service coverage across all board families, certification or qualification evidence, and customer-program approval proof.

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
