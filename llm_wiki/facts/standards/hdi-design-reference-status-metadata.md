---
fact_id: "standards-hdi-design-reference-status-metadata"
title: "Public IPC records support current-vs-legacy HDI design-reference framing, not publishable geometry tables"
topic: "HDI design reference status metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "ipc-document-revision-table"
  - "ipc-board-design-standards-page"
  - "ipc-2226a-hdi-standard-page"
  - "ipc-2315-legacy-hdi-guide-page"
  - "ipc-tm650-test-methods-index"
tags: ["ipc", "ipc-2226", "ipc-2315", "hdi", "microvia", "design-guide", "legacy", "metadata"]
---

# Canonical Summary

> Public IPC records now give `llm_wiki` a cleaner HDI reference hierarchy for `20-layer` writing: `IPC-2226A` is the current public HDI design-standard anchor, `IPC/JPCA-2315` is a legacy design guide that should not be treated as a current rules table, and the `IPC TM-650` index confirms that named test-method families exist without exposing pass/fail limits.

## Stable Facts

- `IPC-2226A` is publicly identified as the current IPC HDI printed-board design standard and is positioned around `HDI` and microvia design considerations.
- IPC's public board-design standards family page still lists `HDI` printed-board design as an active standards-family topic alongside other board-design standards.
- The public `IPC-2226A` product page explicitly frames the document around HDI constructions, routing-density factors, and feature-size recommendation topics.
- `IPC/JPCA-2315` is publicly identified as a design guide for `HDI` and microvias, but the IPC revision table marks it as `No Longer Maintained`.
- The public `IPC TM-650` index confirms that IPC test-method families exist for relevant thermal and interconnect testing, but the index does not publish requirements or thresholds.

## Conditions And Methods

- Use this card when a `20-layer` or HDI article needs to explain which public IPC references are current and which are legacy.
- Pair it with the microvia-reliability context layer before discussing stacked microvia risk, and with licensed standards or customer requirements before discussing geometry or qualification.
- Use this card to block unsupported reuse of old `IPC/JPCA-2315` values as if they were current universal design rules.

## Limits And Non-Claims

- This card does not provide microvia diameter tables, capture-pad rules, aspect-ratio limits, stacked-height limits, or `IST` cycle thresholds.
- It does not establish `ELIC`, `any-layer`, or stacked-microvia capability for any specific factory.
- It does not prove that a given HDI construction is compliant with current IPC design or qualification requirements.

## Open Questions

- Add a separate public metadata card for `IPC-6012` addendums or HDI performance-specification families if future drafts need clearer separation between design references and qualification references.
- Decide whether a guarded `RCC / ABF / build-up dielectric` source batch is now the highest-leverage next move for `20-layer`.

## Source Links

- https://www.ipc.org/ipc-document-revision-table
- https://www.electronics.org/ipc-board-design-standards
- https://shop.electronics.org/ipc-2226/ipc-2226-standard-only/Revision-a/english
- https://shop.electronics.org/ipc-2315/ipc-2315-standard-only/Revision-0/english
- https://www.electronics.org/test-methods
