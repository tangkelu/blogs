---
fact_id: "methods-parameter-scope-public-capability-impedance-and-validation"
title: "English public impedance, PTFE, and HDI pages expose page-scoped impedance and validation parameter claims"
topic: "Public-site capability parameter scope for impedance and validation"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendhil-high-speed-product-page-en"
tags: ["internal", "public-site-claim", "parameters", "impedance", "tdr", "vna", "validation", "rf", "high-speed"]
---

# Canonical Summary

> The English public impedance, PTFE, HDI, and high-speed pages contain repeated parameter claims for impedance tolerance, TDR coverage, VNA availability, frequency range, and backdrill-stub validation posture. These are usable only as `public-site claimed capability` in prompt support.

## Extracted Public-Site Claimed Parameters

- `±5Ω / ±7% impedance tolerance` and `100% TDR` on the APT controlled-impedance page.
  Source:
  `frontendapt-pcb-pcb-impedance-control-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json`
- `±5Ω (≤50Ω), ±7% (>50Ω)` on the APT controlled-impedance capability table.
  Source:
  `frontendapt-pcb-pcb-impedance-control-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json`
- `50Ω, 90Ω, 100Ω` standard targets on the APT controlled-impedance page.
  Source:
  `frontendapt-pcb-pcb-impedance-control-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json`
- `±3–5% impedance control with TDR`, `sample-based VNA`, and `up to 40 GHz` on the HIL PTFE page.
  Source:
  `frontendhil-teflon-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json`
- `sample-based VNA S11/S21 and coupon-based TDR` on the HIL PTFE FAQ.
  Source:
  `frontendhil-teflon-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json`
- `±7% standard` and `±3–5% advanced with TDR` on the HIL PTFE specification table.
  Source:
  `frontendhil-teflon-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json`
- `±5% impedance with TDR validation` and `TDR/VNA measurement across production lots` on the HIL HDI page.
  Source:
  `frontendhil-hdi-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json`
- `backdrill`, `low-loss stackup`, and `TDR/VNA` framing also appear on the HIL high-speed page and may be used only as corroborating page context.
  Source:
  `frontendhil-high-speed-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json`

## Scope

- Claim class:
  `public website claim`
- Page context:
  English APT controlled-impedance service page, English HIL PTFE product page, English HIL HDI product page, English HIL high-speed product page
- Language:
  `en`
- Checked date:
  `2026-04-27`

## Consumption Rules

- Use these values to keep prompts anchored to the source page’s own public wording about impedance and verification.
- Keep `100% TDR`, `coupon-based TDR`, `sample-based VNA`, and `with TDR` separate because they imply different page-level verification postures.
- Do not collapse PTFE-specific validation language into a universal statement for all PCB families.
- When a draft needs RF or channel-performance proof, route to stronger standards or official measurement sources; these page claims only support manufacturing and validation posture.

## Non-Generalization

- These claims are not supplier-independent proof.
- They are not lot capability or shipment-release evidence beyond the page wording itself.
- They are not qualification evidence or telecom/RF performance certification.
- They are not acceptance thresholds for impedance coupons, S-parameters, or SI pass/fail.
- They do not prove every board receives VNA, TDR, or identical tolerance control.

## Blog Usage

- Supports `rf-5g`, `mmwave`, `antenna-system`, and `high-speed digital` empty-image families for conservative impedance-control and validation vocabulary.
- Supports `ai-server / optical high-speed` families for coupon, TDR, and backdrill-aware channel-control context.
- Supports `charger / power interface` or `industrial control` families only when impedance is a side topic, not the central product claim.
- Does not unlock protocol performance, insertion-loss guarantee, BER, eye-diagram, or qualification language.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
