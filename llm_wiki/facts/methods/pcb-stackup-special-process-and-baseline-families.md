---
fact_id: "methods-pcb-stackup-special-process-and-baseline-families"
title: "Internal APT PCB pages separate baseline laminate families, stackup planning, and special-process routes"
topic: "PCB stackup planning and special-process family routing"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-fr4-pcb-page-en"
  - "frontendapt-pcb-high-tg-pcb-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "frontendapt-pcb-special-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-profiling-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
tags: ["internal", "pcb", "fr4", "high-tg", "heavy-copper", "stackup", "lamination", "profiling", "conformal-coating", "special-process"]
---

# Canonical Summary

> The internal APT PCB pages describe board planning in layers: FR-4 and high-Tg act as baseline laminate families, heavy copper acts as a power and thermal platform, stackup and lamination pages define construction planning, and profiling plus conformal coating extend the route into finishing and protection steps.

## Stable Facts

- The FR-4 page treats mainstream FR-4 fabrication as the baseline manufacturing family while still linking it to HDI, impedance, and surface-finish positioning.
- The high-Tg page adds a thermally tougher laminate posture for multilayer and lead-free reliability contexts rather than replacing FR-4 as the default label for every board.
- The heavy-copper page frames thick-copper construction as a separate current and thermal route tied to bus-bar, thermal-via, and power-electronics language.
- The PCB stack-up page frames custom layer construction, impedance planning, and board-family mapping as an early architecture decision.
- The multilayer-laminated-structure page extends that architecture into sequential lamination, hybrid material combinations, and higher-complexity multilayer build planning.
- The special-PCB page broadens the taxonomy into ceramic, metal-core, flex, rigid-flex, RF, gold-finger, carbon-ink, heavy-copper, and other non-standard build routes.
- The PCB profiling page treats depaneling, V-score, tab routing, laser singulation, edge plating, and castellation as downstream manufacturing-route choices rather than generic afterthoughts.
- The PCB conformal-coating page places board protection after fabrication or assembly as a separate chemistry and application-method choice.

## Conditions And Methods

- Use this card when content needs one internal frame for deciding whether a board is baseline FR-4/high-Tg work, a heavy-copper thermal-current build, a special-process construction, or a stackup-driven hybrid route.
- Keep material family, stackup architecture, lamination route, edge/profile finishing, and protection chemistry as separate planning layers.
- Treat conformal coating as a protection step that may occur after assembly, not as proof of a bare-board material property.
- Refresh all numeric capability claims such as copper weight, layer count, Tg/Td, turnaround, and tolerance before publication.

## Limits And Non-Claims

- This card does not define exact material-property values for FR-4, high-Tg, or heavy-copper constructions.
- It does not prove that every special-process family is available in every quick-turn or volume route.
- It does not replace official laminate datasheets, project stackups, or coating qualification documents.

## Open Questions

- Add a later bridge card if more evidence is needed on when profiling method choice materially changes flex, PTFE, metal-core, or ceramic manufacturability.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/fr4-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-tg-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/heavy-copper-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-stack-up.json
- /code/hileap/frontendAPT/public/static/pcb/en/multi-layer-laminated-structure.json
- /code/hileap/frontendAPT/public/static/pcb/en/special-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-profiling.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
