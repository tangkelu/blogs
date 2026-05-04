---
fact_id: "methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity"
title: "Grounding and return-path guidance stays at reference-plane continuity, partitioning, and routing discipline"
topic: "Grounding and return-path execution boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "analog-devices-mixed-signal-pcb-layout-guidelines"
  - "ti-high-speed-layout-guidelines"
tags: ["grounding", "return-path", "reference-plane", "partitioning", "high-speed", "mixed-signal", "methods"]
---

# Canonical Summary

> Current official guidance supports a narrow execution boundary for grounding and return paths: keep a continuous low-impedance reference plane where possible, partition functional regions before routing, avoid routing signals across plane splits or slots, and preserve return-current continuity when layers change.

## Stable Facts

- ADI treats board-layer planning as upstream of routing because layer structure determines allowable return-current paths.
- ADI supports using a ground plane as the low-impedance return reference and ties grounding quality to overall mixed-signal layout integrity.
- TI states that return current follows the lowest-impedance path at higher frequencies and that splits or slots in the reference plane force larger loop areas.
- TI supports keeping the return-current path directly under or beside the signal trace and using nearby ground vias when signal layers change.

## Conditions And Methods

- Use this card when a draft needs safe language about grounding or return-path planning without claiming RF, EMC, or telecom outcomes.
- Keep the wording at execution-boundary level: reference-plane continuity, partitioning, routing discipline, and layer-transition handling.
- Pair this card with narrower cards on shielding, inspection access, or validation only when those claims have their own current authority.

## Limits And Non-Claims

- This card does not authorize telecom-specific shield-contact strategy claims.
- It does not authorize numeric grounding, EMI, impedance, or via-density rules.
- It does not prove that a specific grounding layout achieves compliance, field performance, or cross-domain isolation by itself.

## Open Questions

- A later lane could add a narrower shield-can or partition-bridge card if a current official source is found for that exact assembly-execution context.

## Source Links

- https://www.analog.com/en/resources/analog-dialogue/articles/what-are-the-basic-guidelines-for-layout-design-of-mixed-signal-pcbs.html
- https://www.ti.com/lit/an/scaa082a/scaa082a.pdf
