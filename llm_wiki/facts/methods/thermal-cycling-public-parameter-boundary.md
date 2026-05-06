---
fact_id: "methods-thermal-cycling-public-parameter-boundary"
title: "Public IPC thermal-cycling methods expose reusable parameter patterns, but those patterns remain application-scoped"
topic: "thermal cycling public parameter boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-06"
source_ids:
  - "ipc-tm650-2626a-dc-current-induced-thermal-cycling-page"
  - "ipc-tm650-2672c-thermal-shock-cycle-continuity"
tags: ["ipc", "thermal-cycling", "thermal-shock", "continuity", "ist", "reliability", "methods"]
---

# Canonical Summary

> IPC public thermal-cycling methods do expose concrete parameter examples, but they are method-family and application scoped, not universal PCB reliability defaults. They can support blog-level parameter tables when the article clearly labels them as method conditions, qualification examples, or application-specific defaults.

## Stable Facts

- IPC-TM-650 `2.6.26A` publishes a DC-current-induced thermal-cycling method for interconnect evaluation.
- Its public text includes method-family example conditions such as default `150 °C`, `10%` resistance-change threshold, `250` cycles, and `6` samples for the default condition.
- The same public text includes microvia and survivability example conditions, including `190 °C` microvia testing and `230 / 245 / 260 °C` survivability examples.
- IPC-TM-650 `2.6.7.2C` publishes a board-level thermal shock / thermal cycle / continuity method.
- Its public text includes qualification and conformance example conditions such as `6` hours of conditioning at `105 to 125 °C`, `6` reflow simulation cycles, `15` minute dwell at extremes, `100` thermal cycles for quality conformance, and a `5%` maximum allowable resistance change unless otherwise specified.

## Conditions And Methods

- Use these values when the article needs a concrete parameter table or process example for thermal cycling.
- Label them as IPC method conditions, not universal industry requirements.
- Preserve the distinction between qualification / conformance examples and application-specific AABUS values.
- Keep thermal cycling separate from thermal shock when discussing change rate, dwell, and intended stress behavior.

## Limits And Non-Claims

- This fact card does not authorize universal temperature, cycle-count, or pass/fail tables for every PCB.
- It does not prove board-level qualification, supplier capability, or field-life correlation.
- It does not replace customer drawings, licensed standard text, or project-specific acceptance criteria.

## Source Links

- https://www.ipc.org/sites/default/files/test_methods_docs/2-6_2-6-26a.pdf
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.7.2c.pdf
