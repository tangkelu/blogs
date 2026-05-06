---
title: "CO2 Control PCB Evidence Pack"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-05"
tags: ["co2", "gas-sensor", "ndir", "air-quality", "validation", "review-boundary"]
---

# CO2 Control PCB Evidence Pack

**Pack ID**: `consumption-co2-control-pcb`  
**Date**: 2026-05-05  
**Status**: `go_now_conservative`  
**Template**: `blog-rewrite`

## 1. Traceability Core

```yaml
topic: "CO2 control PCB"
scope: |
  Conservative evidence pack for CO2 control / air-quality sensor boards.

  Supports board-review language around CO2 sensor family identity, heat
  separation, airflow, contamination control, calibration ownership, enclosure
  fit, and staged validation.

  Does not support universal ppm accuracy claims, drift guarantees, fixed
  calibration intervals, or product-level safety/compliance proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/aptpcb/query-overlay.md"

fact_ids:
  - "methods-co2-control-board-review-boundary"
  - "methods-pcba-validation-handoff-package"
  - "methods-pcba-evt-dvt-pvt-gated-ramp-boundary"

source_ids:
  - "sensirion-scd4x-co2-sensor-page"
  - "fcc-equipment-authorization-page"

must_refresh:
  - claim: "Any exact ppm, drift, response-time, or calibration-interval claim"
    value: true
  - claim: "Any wireless authorization or compliance wording"
    value: true

excluded_claim_classes:
  - "exact sensor accuracy, drift, or warm-up claims"
  - "universal washability, outgassing, or coating claims"
  - "product-level compliance, safety, or field-performance proof"
  - "cost, lead-time, yield, or supplier-readiness claims"
```

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `CO2 control PCB` |
| **Reader intent** | Understand what must be reviewed before releasing a CO2 / air-quality sensor board |
| **Safe angle** | Sensor integration, airflow, contamination control, calibration ownership, and staged validation |
| **Unsafe angle** | Sensor-performance brochure, safety certification page, or universal design-rule table |

## 3. Handoff Summary

> A safe CO2 control PCB rewrite should read like a board-review guide, not a generic air-quality checklist. The board can be described through sensor-family identity, enclosure airflow, heat separation, contamination control, calibration ownership, and staged validation. It must not drift into accuracy, drift, or certification proof.

**Verdict**: ✅ `go_now_conservative`
