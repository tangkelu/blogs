---
fact_id: "methods-tht-pressfit-terminal-route-boundary"
title: "THT, press-fit, and cable or harness handoff are separate route choices for board interfaces"
topic: "THT versus press-fit versus cable or harness route boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-cable-assembly-page-en"
  - "frontendapt-pcba-harness-assembly-page-en"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-backplane-pcb-page-en"
tags: ["tht", "press-fit", "connector", "cable", "harness", "medical", "inverter", "route-boundary", "methods"]
---

# Canonical Summary

> The current internal source layer supports a practical split: use `THT` when the board-level story is soldered retention for connectors, transformers, relays, and other mechanically stressed or larger hardware; use `press-fit` when the story is a connector-zone insertion problem tied to hole control and finish choice; use `cable` or `harness` framing when the discussion moves beyond the PCB joint into routed wires, mating connectors, and box-build integration.

## Stable Facts

- The HIL through-hole assembly page frames THT as a board-assembly route for connectors, transformers, power parts, and other hardware that benefits from mechanical retention inside a mixed-technology flow.
- The same through-hole page places `press-fit` next to THT, inspection, and electrical validation, which supports treating press-fit as an adjacent but distinct board-interface route rather than as generic THT soldering.
- The internal press-fit finish and backplane cards already show that press-fit depends on finish selection, tight hole control, and connector-zone planning, not just on choosing a connector family.
- The power and new-energy page supports inverter, converter, storage, charging, and protection-electronics contexts where boards align with busbars, cable connections, contactors, heatsinks, and enclosures.
- The medical page supports imaging, monitoring, wearable, medical power, and interface or control-module context, including mechanical, shielding, cooling, and enclosure constraints.
- The cable-assembly and harness-assembly pages place cables and harnesses in a broader electromechanical and box-build path, which means off-board wiring should not be collapsed into the same claim set as plated-hole board soldering.

## Conditions And Methods

- Use this card for `tht-through-hole-soldering-medical-imaging-wearable` and `tht-through-hole-soldering-renewable-energy-inverter`, and as an adjacent boundary card for `selective-wave-soldering-medical-imaging-wearable`.
- Safe `THT` posture: write about plated-hole soldered attachment on the PCB for connectors, relays, transformers, inductive or larger power hardware, shielding attachments, or other mechanically stressed board interfaces.
- Safe `press-fit` posture: write about solder-free connector insertion when the important story is finished-hole control, connector-zone preparation, finish compatibility, seating verification, and system integration around the connector interface.
- Safe `cable` or `harness` posture: switch to cable or harness framing when the important work is wire routing, connector mating, labeling, off-board power or signal distribution, enclosure routing, or box-build integration.
- Safe renewable-energy inverter posture: explain that route choice depends on whether the interface is a soldered board component, a press-fit connector zone, or an off-board cable or harness connection near busbars, contactors, and enclosure-level power paths.
- Safe medical imaging and wearable posture: explain that route choice depends on compact mixed-signal neighborhoods, control or interface modules, battery or charging subcircuits, shielding or enclosure constraints, and whether the connection remains on the PCB or exits into product-level wiring.
- If the draft names `terminal blocks`, keep the wording generic unless the source layer is refreshed with a page that explicitly discusses that connector family. The current corpus is stronger for `connectors`, `cable connections`, `contactors`, and `board-to-system interfaces` than for terminal-block-specific details.

## Limits And Non-Claims

- This card does not authorize current ratings, contact-resistance values, temperature-rise values, insertion-force values, pull-force values, torque values, or service-life numbers for any connector, terminal, press-fit, cable, or harness interface.
- It does not prove that press-fit is better than soldered THT for every power or medical program.
- It does not prove that a wearable should use flying leads, a harness, or a board-mounted connector by default.
- It does not prove that an inverter power interface must be press-fit, must be THT, or must leave the board through a harness.
- It does not support medical compliance, device-safety, sterilization, or patient-risk claims.

## Open Questions

- Add a stronger public source if future articles need explicit `terminal block` family language instead of generic connector and cable-interface language.
- Add a later card if future inverter articles need a tighter split between board-edge connector hardware and full box-build power-distribution assemblies.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/cable-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/harness-assembly.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/power-energy-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json
