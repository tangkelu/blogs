---
fact_id: "methods-selective-solder-design-access-checks"
title: "Selective-solder DFM should be framed as access, keep-out, shielding, and thermal-shadowing review"
topic: "Selective solder design access checks"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-blog-selective-solder-design-en"
  - "frontendapt-blog-wave-solder-fixture-intro-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
tags: ["selective-solder", "wave-solder", "fixture", "dfm", "access", "keepout", "thermal-shadowing", "mixed-technology"]
---

# Canonical Summary

> The safe engineering posture for selective-solder layout guidance is to treat it as an access-planning problem: can flux, localized heat, solder, support tooling, and inspection reach the intended through-hole joints without colliding with nearby hardware, overheating adjacent SMT, or creating fixture-induced shadowing.

## Stable Facts

- The internal selective-solder, SMT/THT, and through-hole assembly pages support selective solder as a targeted route for through-hole content on mixed-technology boards rather than as a universal default.
- The public selective-solder design explainer reinforces that local soldering success depends on physical access to the joint area, not only on the existence of through-hole pins in the netlist.
- The same explainer supports treating nearby bottom-side components, tall bodies, connector overhang, and sensitive devices near the solder zone as first-pass DFM review inputs.
- The wave-fixture explainer supports a second access layer: shielding and support tooling can make wave solder feasible for mixed-technology builds, but fixture openings and walls can also create solder-flow shadowing or block access if planned poorly.
- Thermal demand is part of route planning. Heavy copper attachment, large terminals, shields, transformers, or other heat-sinking features can make localized soldering harder even when geometric access looks acceptable.
- Post-solder release still depends on inspection and electrical validation; access planning should not be separated from AOI, X-ray, ICT/FCT, or final-release considerations.

## Engineering Review Checklist

- Confirm which through-hole joints actually need automated soldering and which are likely exceptions, rework-only joints, or pilot-only manual steps.
- Check underside and topside neighborhoods for nearby SMT bodies, low-standoff parts, tall housings, clips, shields, and other obstacles that can interfere with fluxing, heating, solder flow, or tooling motion.
- Check whether the board needs fixture support, masking, or hold-down strategy because of thin sections, uneven mass, mixed top/bottom population, or exposure of bottom-side SMT during wave processing.
- Review whether large copper-connected pins, power terminals, magnetic parts, or chassis-linked hardware create thermal shadowing or uneven heat demand across the solder set.
- Check if panel rails, carrier references, board edge access, connector overhang, or depanel state change the reachable solder path.
- Review inspection and test access after soldering so that the chosen route does not isolate important joints from visual review, X-ray sampling, or downstream electrical validation.

## Conditions And Methods

- Use this card for `selective-wave-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-medical-imaging-wearable`, and `tht-through-hole-soldering-renewable-energy-inverter`.
- Safe route logic: selective solder is a strong candidate when only part of the board needs through-hole soldering and nearby SMT or localized thermal concerns make blanket wave exposure unattractive.
- Safe route logic: wave solder with fixture or pallet remains a candidate when through-hole populations are broader and the required shielding, board support, and opening geometry can be engineered without severe shadowing.
- Safe route logic: manual solder stays relevant for low-count exceptions, unstable pilot revisions, or inaccessible joints that do not justify a dedicated automated route.
- For medical imaging or wearable boards, emphasize compact mixed-technology neighborhoods, sensitive adjacent components, and release-workflow discipline rather than compliance or sterilization claims.
- For inverter and power boards, emphasize larger terminals, magnetic hardware, and copper-linked thermal demand rather than current, efficiency, or lifetime numerics.

## Limits And Non-Claims

- This card does not authorize exact keep-out dimensions, nozzle sizes, flux-spread limits, lead-protrusion targets, hole-fill thresholds, plating-thickness requirements, or thermal-profile settings.
- It does not prove that selective solder is always the best route for dense boards, medical wearables, or inverter hardware.
- It does not authorize fixture wall-thickness, chamfer-angle, material-temperature, cycle-life, cost, lead-time, or yield claims.
- It does not authorize medical compliance, inverter performance, or universal reliability claims tied to one soldering method.

## Open Questions

- Add stronger public sources if future rewrites need dimensioned access rules or formal fixture-design thresholds.
- Add a separate card if later inverter content needs a sharper split between soldered terminals, press-fit interfaces, and busbar hardware.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/selective-solder-design.md
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/wave-solder-fixture-intro.md
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
