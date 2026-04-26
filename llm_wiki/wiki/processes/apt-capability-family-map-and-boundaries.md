---
topic_id: "processes-apt-capability-family-map-and-boundaries"
title: "APT Capability Family Map And Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-internal-capability-family-map"
  - "methods-hdi-microvia-and-vippo-process-posture"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "methods-mcpcb-ims-and-reflow-source-coverage"
source_ids:
  - "frontendapt-capabilities-index-page-en"
  - "frontendapt-ceramic-pcb-capability-page-en"
  - "frontendapt-flex-pcb-capability-page-en"
  - "frontendapt-hdi-pcb-capability-page-en"
  - "frontendapt-metal-pcb-capability-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendapt-rigid-pcb-capability-page-en"
tags: ["processes", "internal-source", "capabilities", "pcb", "hdi", "flex", "rigid-flex", "thermal-platform"]
---

# Definition

> The APT capability family map is the internal site layer that separates broad PCB manufacturing work into six reusable families: rigid, flex, HDI, rigid-flex, metal-core, and ceramic. Its main value is scope control. It helps prompts choose the right engineering frame before they start making claims about materials, process limits, or qualification.

## Why This Topic Matters

- Prompt outputs get unreliable when every build is described as the same generic "advanced PCB" problem.
- The APT capabilities layer already separates general rigid work, bend-oriented work, density-driven work, hybrid rigid-flex work, and thermal-platform work.
- That separation is useful only if the wiki keeps the boundaries clear and does not collapse all six families into one capabilities bucket.

## Stable Facts

- The overview page presents six core capability families and ties them to a prototype-to-production service frame.
- `Rigid PCB` is the broadest family and is the right default only when the design does not require a more specific thermal, bend, or density frame.
- `Flex PCB` centers on thin flexible circuits, bend-oriented design, and dynamic or compact packaging contexts.
- `HDI PCB` is the density-first family, with microvia, build-up, fine-line, and impedance-oriented language.
- `Rigid-flex PCB` combines mechanical integration and bend-zone concerns with multilayer stackup and often HDI-adjacent complexity.
- `Metal-core PCB` and `Ceramic PCB` are both thermal-platform families, but they should not be treated as interchangeable because the internal pages frame different material systems, process routes, and application posture.

## Engineering Boundaries

- Choose the capability family before discussing parameters.
- Keep `HDI` separate from `rigid-flex`; they can coexist, but one is not a synonym for the other.
- Keep `thermal platform` work separate from standard rigid-board language; MCPCB and ceramic should not be collapsed into generic high-power multilayer wording.
- Treat trust-bar figures, FAQ windows, and table limits on the capability pages as refresh-sensitive internal claims.
- Use deeper process or material sources before publishing exact stackups, material properties, or validation promises.

## Common Misreadings

- A capability page is not a standing promise that every mentioned option is routinely available.
- `Rigid PCB` coverage does not mean all rigid projects should be framed as HDI or heavy-copper projects.
- `Flex PCB` content does not automatically authorize rigid-flex claims.
- `Metal-core` and `ceramic` both support thermal narratives, but they are not the same process family.
- A capabilities overview page is a routing map, not a manufacturing specification.

## Must Refresh Before Publishing

- Layer-count, copper-weight, drill, line/space, and impedance-limit claims
- Bend-radius, flex-life, and rigid-flex mechanical claims
- Thermal-conductivity, dielectric, or ceramic-process numeric claims
- Lead-time, volume, or prototype-availability language
- Any certification, quality-system, or sector-approval statement

## Related Fact Cards

- `methods-internal-capability-family-map`
- `methods-hdi-microvia-and-vippo-process-posture`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`
- `methods-mcpcb-ims-and-reflow-source-coverage`

## Primary Sources

- /code/hileap/frontendAPT/public/static/capabilities/en/index.json
- /code/hileap/frontendAPT/public/static/capabilities/en/ceramic-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/metal-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json
