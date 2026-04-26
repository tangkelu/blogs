---
fact_id: "methods-hdi-microvia-and-vippo-process-posture"
title: "Internal HDI pages consistently frame microvia, any-layer build-up, and VIPPO as standard HDI process posture"
topic: "HDI microvia and VIPPO process posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
tags: ["internal", "hdi", "microvia", "any-layer", "vippo", "stackup", "methods"]
---

# Canonical Summary

> Across APT and HIL internal pages, HDI is repeatedly described as a standard build-up discipline rather than a niche exception: laser microvias, any-layer or sequential build-up, and VIPPO are presented as normal process elements for dense interconnect work.

## Stable Facts

- The APT HDI page positions high-density interconnect as a microvia and any-layer service with impedance-verification language.
- The APT advanced manufacturing page includes HDI / ELIC, sequential lamination, and VIPPO in its capability framing.
- The HIL HDI page likewise frames HDI around 1+N+1 through any-layer architecture, microvias, VIPPO, and impedance validation.

## Conditions And Methods

- Use this card as internal posture support for HDI capability summaries.
- Treat the microvia size, impedance tolerance, and turn-time figures as refresh-sensitive internal claims.
- If a customer-facing page needs exact drill geometry or stack-up limits, refresh against current engineering data first.

## Limits And Non-Claims

- This card does not prove every HDI topology is available on every line.
- It does not claim that any specific microvia, fill, or lamination window is universal.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/advanced-pcb-manufacturing.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
