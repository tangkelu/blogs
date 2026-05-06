---
topic_id: "thermal-cycling-public-parameter-path"
title: "Thermal cycling blog writing can use IPC public method parameters, but must label them as method-scoped examples"
category: "testing"
status: "draft"
last_reviewed_at: "2026-05-06"
fact_ids:
  - "methods-thermal-cycling-public-parameter-boundary"
  - "methods-pcb-environmental-and-solderability-test-method-boundary"
source_ids:
  - "ipc-tm650-2626a-dc-current-induced-thermal-cycling-page"
  - "ipc-tm650-2672c-thermal-shock-cycle-continuity"
tags: ["thermal-cycling", "ipc", "reliability", "methods", "parameters"]
---

# Definition

> Thermal cycling articles can use public IPC method examples for temperature, cycle count, dwell, and resistance-change language, but they must label those values as method-scoped examples and keep qualification / conformance / AABUS boundaries visible.

## Stable Facts

- IPC public methods now provide a usable parameter lane for thermal-cycling writing.
- `2.6.26A` supports default and microvia/survivability example conditions for coupon-based interconnect evaluation.
- `2.6.7.2C` supports board-level thermal shock / thermal cycle / continuity examples for qualification and quality-conformance language.

## Writing Boundaries

- Do not flatten method examples into universal PCB reliability defaults.
- Do not omit the AABUS distinction when the source text makes values application-specific.
- Do not use these values as supplier capability proof.
- Do not present them as lot-level pass/fail proof for every board family.

## Common Misreads

- A thermal-cycle example condition is not a universal board standard.
- A conformance example is not the same as qualification proof.
- A method family name is not a guarantee of field life.

## Related Fact Cards

- `methods-thermal-cycling-public-parameter-boundary`
- `methods-pcb-environmental-and-solderability-test-method-boundary`
