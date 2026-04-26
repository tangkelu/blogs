---
fact_id: "methods-controlled-impedance-tdr-verification-posture"
title: "Internal PCB pages repeatedly pair controlled-impedance targets with TDR-style verification"
topic: "Controlled impedance and TDR verification posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
tags: ["internal", "impedance", "tdr", "validation", "high-speed", "methods"]
---

# Canonical Summary

> The internal PCB corpus consistently ties controlled impedance to verification, not just design intent: impedance targets are paired with TDR, coupon-style validation, or similar measurement language across high-speed, HDI, and PTFE-oriented pages.

## Stable Facts

- The APT impedance-control page explicitly couples ±5 ohm class targets with 100% TDR verification.
- The APT high-speed page presents impedance verification as part of the standard high-speed build flow.
- The APT multilayer page frames impedance verification as one of the controls that keeps high-speed and power planes stable.
- The HIL HDI page ties impedance control to TDR validation in its capability summary.
- The HIL PTFE page frames VNA and coupon-based TDR as part of the RF validation posture.

## Conditions And Methods

- Use this card to support internal pages about routing discipline, channel-control language, and validation staging.
- Treat the exact tolerance bands, verification percentages, and coupon scope as refresh-sensitive internal claims.
- If a blog needs explicit acceptance thresholds, verify them against current engineering data or stronger sources first.

## Limits And Non-Claims

- This card does not say every board is shipped with identical TDR coverage.
- It does not claim a universal impedance tolerance across all structures or programs.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-speed-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/multilayer-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
