---
fact_id: "methods-conformal-coating-automotive-ev-power-boundary"
title: "Automotive and EV power coating rewrites should stay at environment, interface, and workflow boundary scope"
topic: "conformal coating automotive EV power boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-industry-automotive-electronics-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
tags: ["conformal-coating", "automotive", "ev", "adas", "inverter", "power-electronics", "functional-safety-boundary"]
---

# Canonical Summary

> For `conformal-coating-automotive-adas-ev-power`, the supported lane is harsh-environment protection workflow around vehicle or EV power electronics context: exposed environment, connector or service-access review, test and inspection handoff, and separation between protected areas and later functional validation. The current sources do not prove automotive qualification, ASIL, ISO 26262, creepage, clearance, dielectric-strength, or high-voltage safety outcomes.

## Stable Facts

- The automotive and EV page supports context for ADAS, ECU, BMS, inverter, motor-control, charger, and related vehicle electronics.
- The power and new-energy page supports adjacent context for inverter, storage, charging, and control-board families.
- The conformal-coating pages support protection workflow, coating-family vocabulary, and selective application methods.
- The PCBA quality, FCT, and final-inspection pages support staged validation and release workflow rather than one final universal capability promise.

## Safe Rewrite Posture

- Write the slug as an `environment and interface review` article for automotive-adjacent and EV-power-adjacent electronics.
- Focus on exposed environment, protected-versus-accessible regions, connector or mating-area review, service or calibration access, and powered-validation handoff.
- Use ADAS or EV power only as application context that increases review pressure on interfaces and workflow sequencing.
- Keep control-board and power-board nouns separate from safety-certification claims.

## Conditions And Methods

- Use this card with `methods-power-energy-inverter-charger-rewrite-boundary`, `methods-conformal-coating-lane-b-rewrite-gate`, and `processes-power-energy-pcb-pcba-review-boundaries`.
- Safe wording examples:
  `vehicle-side electronics may combine harsher exposure with interfaces that still need later access`
  and
  `coating decisions should be coordinated with inspection and powered validation rather than treated as proof of qualification`.
- If a draft starts discussing creepage, insulation, high-voltage margin, ASIL, or lifetime, stop and record a source gap.

## Limits And Non-Claims

- This card does not authorize ISO 26262, ASIL, PPAP, IATF, creepage, clearance, dielectric-strength, insulation, high-voltage safety, or automotive qualification claims.
- It does not authorize coating thickness, cure, masking dimensions, cleanliness windows, or pass/fail thresholds.
- It does not prove that conformal coating is universally required for ADAS, ECU, BMS, inverter, or charger electronics.

## Open Questions

- Add official automotive or EV qualification sources only if a future rewrite needs safety, qualification, or insulation-proof language rather than workflow containment.

## Source Links

- /code/hileap/frontendAPT/public/static/industries/en/automotive-electronics-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/power-energy-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
