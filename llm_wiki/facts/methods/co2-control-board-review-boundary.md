---
fact_id: "methods-co2-control-board-review-boundary"
title: "CO2 control writing is safest as a board-review boundary around sensor integration, enclosure airflow, and staged validation"
topic: "CO2 control board review boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-05"
source_ids:
  - "sensirion-scd4x-co2-sensor-page"
  - "fcc-equipment-authorization-page"
  - "methods-pcba-validation-handoff-package"
  - "methods-pcba-evt-dvt-pvt-gated-ramp-boundary"
tags: ["co2", "gas-sensor", "ndir", "abc", "ventilation", "validation", "board-review"]
---

# Canonical Summary

> CO2 control articles are safest when written as board-review and release-boundary content: sensor family identity, enclosure airflow, heat separation, contamination control, calibration ownership, and staged validation. The current source layer does not support universal sensor rules, fixed calibration schedules, field accuracy proof, or product-level performance promises.

## Stable Facts

- Sensirion's SCD4x product family supports `CO2 sensor` and `NDIR` identity-level wording.
- CO2 board content naturally includes enclosure airflow, heat-source separation, contamination control, and calibration-access planning.
- Manufacturing handoff should stay separate from later functional gas testing and field validation.
- If a CO2 board includes wireless connectivity, FCC-equipment-authorization context still belongs to the final host-product path rather than to the PCB alone.

## Conditions And Methods

- Use this card when a draft mentions `CO2 control PCB`, `CO2 sensor PCB`, `air quality sensor`, or similar language but the safest output is still a release-review article.
- Keep `NDIR` as sensor-family identity and board-integration context, not as proof of any specific sensor performance.
- Treat `ABC`, calibration, airflow, and enclosure fit as project-specific review points rather than universal guarantees.
- Pair this card with `methods-pcba-validation-handoff-package` and `methods-pcba-evt-dvt-pvt-gated-ramp-boundary` when the draft needs staged release language.

## Limits And Non-Claims

- This card does not authorize exact ppm accuracy, drift, warm-up, response time, or calibration interval claims.
- It does not authorize universal washability, conformal-coating, or outgassing claims.
- It does not authorize certification, safety, or field-performance proof.
- It does not convert sensor-family identity into supplier-readiness or system-readiness claims.

## Source Links

- https://www.sensirion.com/products/catalog/SCD4x/
- https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization
- /code/blogs/llm_wiki/facts/methods/pcba-validation-handoff-package.md
- /code/blogs/llm_wiki/facts/methods/pcba-evt-dvt-pvt-gated-ramp-boundary.md
