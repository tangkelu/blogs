---
fact_id: "methods-thermal-pcb-platform-selection-posture"
title: "Internal thermal PCB pages present MCPCB, heavy copper, and ceramic as distinct platform choices for thermal-path design"
topic: "Thermal PCB platform selection posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendhil-metal-core-pcb-product-page-en"
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-heavy-copper-pcb-product-page-en"
tags: ["internal", "thermal", "mcpcb", "heavy-copper", "ceramic", "methods"]
---

# Canonical Summary

> The thermal-oriented internal pages do not collapse every heat problem into one material. They present metal-core, heavy copper, and ceramic as distinct thermal platforms, each with different conductivity windows, mechanical tradeoffs, and validation language.

## Stable Facts

- The APT high-thermal page explicitly frames MCPCB, heavy copper, and ceramic as thermal-path engineered platforms.
- The APT metal-core page positions aluminum and copper IMS stackups as a thermal platform for power electronics.
- The APT ceramic page frames Al2O3, AlN, and Si3N4 as separate ceramic substrate options.
- The HIL high-thermal page also presents MCPCB, ceramic, and heavy copper as the main thermal options.
- The HIL metal-core and ceramic pages reinforce the same platform split with their own capability framing.
- The HIL heavy-copper page adds a separate power-current posture for copper-heavy boards.

## Conditions And Methods

- Use this card to support internal platform-selection guidance, not blanket recommendations.
- Treat conductivity, temperature, and load figures as refresh-sensitive internal claims.
- If a customer-facing page needs exact thermal-resistance, flatness, or cycling criteria, refresh first.

## Limits And Non-Claims

- This card does not say one platform is universally better than the others.
- It does not convert page-level positioning into a guaranteed design outcome.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/high-thermal-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/metal-core-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-thermal-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/metal-core-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/heavy-copper-pcb.json
