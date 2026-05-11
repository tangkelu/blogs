---
source_id: "st-an5686-pcb-layout-tips-to-maximize-esd-protection-efficiency"
title: "AN5686 PCB layout tips to maximize ESD protection efficiency"
organization: "STMicroelectronics"
source_type: "application_note"
url: "https://www.st.com/resource/en/application_note/an5686-pcb-layout-tips-to-maximize-esd-protection-efficiency-stmicroelectronics.pdf"
jurisdiction: "global"
published_at: "2021-07"
checked_at: "2026-05-10"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["stmicroelectronics", "esd", "tvs", "connector", "layout", "ground", "emi", "pcb"]
status: "active"
notes: "Official ST application note for system-level ESD layout. Use for narrow wording about placing protection close to the ESD source or connector, routing from source to TVS to protected IC, minimizing ground-path impedance, and separating exposed protected traces from clean unprotected traces. Do not use it for exact geometry, via counts, package-specific examples, or compliance guarantees."
---

# Source Summary

## What It Covers

- PCB layout guidance to maximize ESD protection efficiency
- placing the protection component where surges appear, near the connector or source
- routing order from ESD source to protection to the protected IC
- low-impedance ground path and exposed-trace separation from clean traces

## Why It Matters

- gives the `194页` handbook `D5` lane a current-public owner layout note that directly mirrors the handbook's source-adjacent protection and path-order claims without relying on RK3588-specific prose

## Extraction Notes

- Safe for guarded statements that TVS placement should be as close as possible to the connector or ESD source.
- Safe for wording that the path should run from source to protection and then to the protected IC, avoiding branch-first routing.
- Safe for local low-impedance ground language and separating ESD-exposed tracks from clean unprotected traces.
- Do not use this source for exact lengths, via counts, package-layout examples, or IEC pass promises.

## Refresh Notes

- Refresh before publication if exact ST revision or package examples matter.
