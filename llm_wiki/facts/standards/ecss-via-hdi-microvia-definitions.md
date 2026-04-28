---
fact_id: "standards-ecss-via-hdi-microvia-definitions"
title: "ECSS provides official blind via, buried via, HDI, and microvia definition context for PCB writing"
topic: "ECSS via and HDI definitions"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "ecss-q-st-70-12c-rev1-pcb-design-standard"
tags: ["ecss", "blind-via", "buried-via", "hdi", "microvia", "definitions", "2025-10-25"]
---

# Canonical Summary

> ECSS-Q-ST-70-12C Rev.1 gives `llm_wiki` an official standards-body definition layer for blind vias, buried vias, HDI, and microvias. Use it to define terms in HDI and via articles, but do not convert ECSS space-design rules into universal commercial PCB capability, price, yield, or lead-time claims.

## Stable Facts

- ECSS-Q-ST-70-12C Rev.1 is an official ECSS printed-circuit-board design-rule standard.
- The ECSS source defines a `blind via` as a via exposed only on one side of the PCB.
- The ECSS source defines a `buried via` as a via connecting internal layers without exposure on either surface.
- The ECSS source defines `HDI` as PCB technology that permits smaller surface-footprint pitch and higher internal routing density than conventional PCBs.
- The ECSS source defines a `microvia` as a blind via with diameter smaller than `250 um`.

## Conditions And Methods

- Use this card for `microvias-pcb.md`, `blind-via-pcb.md`, `buried-via-pcb.md`, and HDI drafts from `2025.10.25`.
- When using the `250 um` microvia definition, keep it tied to the ECSS source and do not present it as a universal commercial fabricator threshold unless another source supports that framing.
- Pair this card with IPC and supplier-specific sources before writing acceptance, reliability, or manufacturability rules.

## Limits And Non-Claims

- This card does not provide universal aspect-ratio, annular-ring, via-fill, laser-drill, copper-plating, yield, reliability, cost, or lead-time rules.
- It does not prove HILPCB, Highleap, or APTPCB can manufacture any given HDI, blind-via, buried-via, or microvia construction.
- It does not authorize application-readiness claims for aerospace, medical, automotive, RF, mmWave, AI, or server products.

## Open Questions

- Add IPC or fabricator-source boundary cards for commercial HDI / via manufacturability if future blogs need non-space-program context.

## Source Links

- https://ecss.nl/wp-content/uploads/2025/05/ECSS-Q-ST-70-12C-Rev.1%2830April2025%29.pdf
