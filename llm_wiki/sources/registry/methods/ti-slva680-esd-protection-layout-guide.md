---
source_id: "ti-slva680-esd-protection-layout-guide"
title: "ESD Protection Layout Guide"
organization: "Texas Instruments"
source_type: "application_note"
url: "https://www.ti.com/lit/pdf/slva680"
jurisdiction: "global"
published_at: "2022-04"
checked_at: "2026-05-10"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["texas-instruments", "esd", "tvs", "connector", "layout", "emi", "vias", "ground"]
status: "active"
notes: "Official TI application note for ESD layout. Use for narrow wording about placing the TVS near the connector, routing directly from ESD source to TVS without stubs, keeping the protected IC further from the TVS than the connector is, and avoiding adjacent unprotected traces in the exposed ESD path. Do not use it for exact inductance numbers, via geometry, or compliance guarantees."
---

# Source Summary

## What It Covers

- PCB layout guidelines for optimizing ESD dissipation
- TVS placement near the connector or ESD source
- direct source-to-TVS routing without stubs or branch-first geometry
- avoiding adjacent unprotected traces in the exposed ESD path
- low-impedance ground path and careful via usage

## Why It Matters

- provides a current-public owner source that states the `connector -> TVS -> protected IC` order and clean-trace separation more explicitly than the handbook

## Extraction Notes

- Safe for guarded statements that the TVS should be placed near the connector as design rules allow.
- Safe for wording that the protected line should run directly from the ESD source to the TVS and should not use stubs between the TVS and the protected line.
- Safe for wording that unprotected traces should not be adjacent to the exposed path between the ESD source and the TVS.
- Do not use this source for exact inductance calculations, exact via rules, exact trace-angle thresholds, or ESD-pass guarantees.

## Refresh Notes

- Refresh before publication if exact TI revision or figure numbering matters.
