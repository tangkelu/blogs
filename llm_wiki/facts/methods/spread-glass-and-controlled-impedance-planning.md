---
fact_id: "methods-spread-glass-and-controlled-impedance-planning"
title: "Internal high-speed material pages connect spread-glass selection with controlled-impedance stackup planning"
topic: "Spread-glass and controlled-impedance planning"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "frontendapt-materials-megtron-pcb-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
tags: ["internal", "spread-glass", "controlled-impedance", "stackup", "high-speed", "tdr"]
---

# Canonical Summary

> Internal high-speed material content treats spread-glass selection and controlled-impedance stackup planning as linked decisions: glass style, resin system, copper profile, reference stackup, impedance coupon, and TDR/VNA validation all need to be planned together.

## Stable Facts

- The spread-glass FR-4 page frames fiber-weave skew mitigation as a material and stackup-design concern.
- The controlled-impedance stackups page provides internal planning language for standard, HDI, and hybrid reference stackups.
- The Megtron page connects high-speed material selection to spread-glass fabric and low-profile copper choices.
- The APT impedance-control page connects controlled-impedance fabrication to simulation, stackup design, and TDR verification.

## Conditions And Methods

- Use this card when creating prompts for high-speed stackup planning, SI preparation, or controlled-impedance quoting.
- Treat reference stackups as starting templates only.
- Final geometry should be simulated with actual material, copper, finish, and fabricator compensation data.

## Limits And Non-Claims

- This card does not guarantee a specific impedance tolerance for every stackup.
- It does not prove a universal skew reduction number for spread-glass materials.
- It does not replace SI simulation or production coupon measurement.

## Open Questions

- Add official or engineering-reference sources for fiber-weave effect and skew mitigation.
- Add a wiki page focused on high-speed stackup intake files and evidence-pack requirements.

## Source Links

- /code/hileap/frontendAPT/public/static/materials/en/spread-glass-fr4.json
- /code/hileap/frontendAPT/public/static/materials/en/controlled-impedance-stackups.json
- /code/hileap/frontendAPT/public/static/materials/en/megtron-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
