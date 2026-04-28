---
fact_id: "methods-parameter-scope-pcba-inspection-stack-for-low-void-coating-tht-and-power"
title: "Inspection-stack parameter cards may use method scope and local page metrics only as source-context examples"
topic: "PCBA parameter scope for inspection stack in low-void, coating, THT, and charger or inverter contexts"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "koh-young-spi-technology"
  - "koh-young-aoi-technology"
  - "keysight-ict-systems"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
tags: ["parameter-scope", "pcba", "inspection", "spi", "aoi", "x-ray", "ict", "fct", "charger", "inverter"]
---

# Canonical Summary

> The reusable inspection parameter layer is method scope, sequencing, and measured attribute names. Real metrics may be cited only as local page or vendor-context examples. They do not become general acceptance numbers for low-void BGA, conformal coating, selective solder, THT, charger, or inverter builds.

## Source-Backed Parameters

- Koh Young supports `3D` SPI framing and confirms that paste inspection is fundamentally about volumetric measurement rather than flat visual checking alone.
- The APT SPI page supports concrete measured attributes: `volume`, `height`, `area`, `offset`, `bridging`, and `missing paste`.
- Koh Young AOI and the APT AOI page support AOI as optical inspection of placement, polarity, solder appearance, and geometry-related defects.
- The APT X-ray page supports `2D`, `2.5D`, and `3D CT` as named X-ray inspection modes in that local page context.
- Keysight supports ICT as a production-line electrical method and the internal FCT page supports powered functional verification after assembly.
- The quality-system page supports sequencing across SPI, AOI, AXI / X-ray, ICT, FCT, burn-in, final inspection, and cleaning, while also warning that not every project necessarily uses every gate.

## Scope And Applicability Limits

- Use this card when low-void BGA, conformal coating, selective solder / THT, charger, or inverter drafts name the inspection stack.
- Safe broad reuse: method names, sequence positioning, and attribute names each method inspects.
- Safe page-scoped examples: `2D/2.5D/3D CT` from the APT X-ray page, `volume/height/area/offset` from the APT SPI page, and `ICT` versus `FCT` role separation from Keysight plus the APT FCT page.
- If a later draft needs exact coverage percentages, defect-detection rates, acceptance percentages, or test-time metrics, refresh them from the exact named page and keep them source-scoped.

## Explicit Blocked Uses

- Do not convert SPI, AOI, X-ray, ICT, or FCT page examples into universal acceptance criteria or mandatory inspection coverage rules.
- Do not derive void thresholds, coating defect thresholds, barrel-fill thresholds, or charger / inverter release thresholds from this card.
- Do not use local or vendor inspection metrics as HIL capability claims, yield claims, cost claims, or lead-time claims.
- Do not convert one method's scope into a claim that it replaces the rest of the inspection stack.
- Do not use inspection-mode vocabulary as proof of product reliability, compliance, or field outcome.

## Blog Usage

- empty-image slugs:
  - `low-void-bga-reflow-data-center-optical-module`
  - `low-void-bga-reflow-high-speed-si`
  - `low-void-bga-reflow-industrial-robotics-control`
  - `low-void-bga-reflow-medical-imaging-wearable`
  - `conformal-coating-automotive-adas-ev-power`
  - `type-c-charger`
  - `ultra-fast-charger-power-energy`
  - `central-inverter-power-energy`
  - `selective-wave-soldering-medical-imaging-wearable`
  - `tht-through-hole-soldering-renewable-energy-inverter`
- families supported:
  - `pcba-inspection-stack`
  - `test-and-inspection-sequencing`
  - `power-board-validation-context`

## Open Questions

- The current source layer is still weak for neutral acceptance thresholds. If later drafts need class-specific or lot-release thresholds, they need licensed standards or customer-spec anchors instead of vendor or internal service pages.
- A future split card may be useful if charger / inverter drafts start mixing powered FCT claims with hidden-joint X-ray claims too aggressively.

## Source Links

- https://kohyoung.com/en/solder-paste-inspection-technology/
- https://kohyoung.com/en/automated-optical-inspection-technology/
- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
