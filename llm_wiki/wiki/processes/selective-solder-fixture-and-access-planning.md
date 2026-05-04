---
topic_id: "processes-selective-solder-fixture-and-access-planning"
title: "Selective Solder Fixture and Access Planning"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-selective-solder-design-access-checks"
  - "methods-selective-wave-solder-and-mixed-technology-sequencing"
  - "methods-tht-heavy-assemblies-power-and-medical-context"
  - "methods-pcba-mixed-technology-assembly-flow"
  - "methods-mixed-technology-lane-b-rewrite-gate"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-blog-selective-solder-design-en"
  - "frontendapt-blog-wave-solder-fixture-intro-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
tags: ["selective-solder", "wave-solder", "fixture", "access-planning", "mixed-technology", "medical", "inverter", "routing-boundary"]
---

# Governance Summary

> Selective-solder fixture and access planning is a reachability and support problem, not a general soldering tutorial. The safe active posture in this corpus is: decide whether the target joints are reachable, whether nearby SMT needs protection, whether the board needs fixture or carrier support, whether thermal demand changes the route, and whether inspection and electrical handoff remain feasible after soldering. This page is a fixture/access-planning boundary page, not a universal process-window or reliability guarantee page.

## Planning Sequence

| Step | Safe question | What this page allows |
|---|---|---|
| 1. Reachable joints | "Which through-hole joints actually need automated access?" | Sort the joint population by accessibility and route need |
| 2. Nearby SMT protection | "What nearby parts or overhangs can be harmed or shadowed?" | Review SMT density, tall bodies, shields, and nearby sensitive devices |
| 3. Board support | "Does the board need fixture, pallet, carrier, or hold-down support?" | Review support strategy and shadowing risk |
| 4. Thermal demand | "Do heavy copper, large pins, magnets, or chassis-linked hardware change the route?" | Review thermal demand as a reachability-adjacent constraint |
| 5. Inspection handoff | "Can the resulting joints still be inspected and validated?" | Keep visual review, X-ray sampling, ICT/FCT access, and release handoff in view |

## What This Page Controls

- Use this page when a draft needs to explain why a joint group is or is not a candidate for selective solder or a supported wave route.
- Treat access, shielding, support, thermal demand, and inspection handoff as the real planning variables.
- Keep the page on reachability and tooling constraints rather than on generic solder chemistry or process-window detail.
- Use medical and inverter context only as hardware-mix and release-workflow framing.

## Stable Facts

- Selective solder is supported in the corpus as a targeted mixed-technology route for through-hole joints that should not be exposed to blanket wave conditions.
- Wave solder remains supported where through-hole populations and layout make broader exposure practical, especially when fixtures can shield vulnerable areas and support the board.
- Fixtures and pallets can protect bottom-side SMT and stabilize the board, but poor opening geometry or wall placement can create shadowing and incomplete solder reach.
- Access review is both geometric and thermal. A reachable joint can still be a poor candidate if nearby mass, copper attachment, or hardware overhang makes localized heating uneven.
- Inspection and electrical validation remain part of the same process route; the solder plan should be checked against how joints will later be inspected, sampled, and electrically verified.
- THT-heavy power and medical hardware often stays in the route discussion because of connectors, transformers, relays, inductors, shields, and mechanically stressed interfaces, not because it starts a separate quality regime.

## Access-Planning Boundary

### Safe Route Logic

- selective solder is a strong candidate when only part of the board needs through-hole soldering and nearby SMT or thermal concerns make blanket wave exposure unattractive
- wave solder with fixture or pallet remains a candidate when through-hole populations are broader and the shielding, board support, and opening geometry can be engineered without severe shadowing
- manual solder stays relevant for low-count exceptions, unstable pilot revisions, or inaccessible joints that do not justify a dedicated automated route

### Safe Review Inputs

- exact through-hole population
- nearby SMT density and tall-body obstacles
- support needs from thin sections, mixed top/bottom population, or panel rails
- thermal-demand grouping from heavy copper ties, large pins, magnetic parts, or chassis-linked hardware
- downstream inspection and electrical-validation access

### Stop Line

- do not turn reachability review into a universal solder recipe or a fixed process window

## Medical And Inverter Context

- Medical context here means compact mixed-technology neighborhoods, sensitive adjacent components, and release-workflow discipline.
- Inverter context here means larger terminals, magnetic hardware, and copper-linked thermal demand.
- Neither context authorizes compliance proof, performance proof, or universal reliability proof from this page.

## Common Overclaims To Block

- `use selective solder for dense boards`
- `fixture design alone guarantees success`
- `the access check proves reliability`
- `the route choice proves medical suitability`
- `the route choice proves inverter performance`
- `access planning guarantees yield or release readiness`

## Explicit Blocked Claims

- `exact process-window claims`: do not publish nozzle sizes, keep-out dimensions, wall thickness, chamfer angles, preheat values, dwell times, or pot settings from this page.
- `universal reliability guarantees`: do not claim that one fixture or access route guarantees reliability or success for all boards.
- `medical or inverter performance claims`: do not claim medical compliance, sterilization compatibility, current rating, efficiency, thermal-rise, or lifetime performance.
- `cost, lead-time, and yield claims`: do not publish commercial, schedule, throughput, or yield conclusions from this page.

## Must Refresh Before Publishing

- any dimensioned keep-out, fixture-opening, nozzle, or wall specification
- any hole-fill, plating-thickness, cleanliness, or IPC class-specific threshold
- any claim that selective solder or wave solder is universally best
- any medical compliance or inverter performance claim
- any cost, lead-time, throughput, or yield statement

## Related Facts

- `methods-selective-solder-design-access-checks`
- `methods-selective-wave-solder-and-mixed-technology-sequencing`
- `methods-tht-heavy-assemblies-power-and-medical-context`
- `methods-mixed-technology-lane-b-rewrite-gate`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/selective-solder-design.md
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/wave-solder-fixture-intro.md
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
