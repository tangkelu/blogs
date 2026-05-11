---
source_id: "nexperia-pesd-layout-close-to-connector-boundary"
title: "PESD1V0Y1BBSF extremely low capacitance unidirectional ESD protection diode in SOD962 package"
organization: "Nexperia"
source_type: "datasheet"
url: "https://assets.nexperia.com/documents/short-data-sheet/PESD1V0Y1BBSF_SDS.pdf"
jurisdiction: "global"
published_at: "2022-06-20"
checked_at: "2026-05-10"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["nexperia", "esd", "tvs", "connector", "layout", "pcb", "return-path", "entry-point"]
status: "active"
notes: "Official Nexperia short datasheet. Use only for the narrow PCB-layout boundary that system-level ESD protection should sit close to the external connector or other entry point so the surge path stays short before the protected IC. Do not use it for exact trace lengths, via counts, compliance guarantees, or universal TVS selection rules."
---

# Source Summary

## What It Covers

- ESD protection diode identity and system-level placement context
- explicit layout note that protection should be placed close to the connector or other entry point to limit overvoltage before the protected device
- short path framing between the entry point and the protection element

## Why It Matters

- gives the `194页` handbook `D5` lane one current-public semiconductor-owner anchor for source-adjacent / connector-adjacent ESD placement language
- supports a safer route than relying on RK3588-handbook-only ESD figures and branded layout prose

## Extraction Notes

- Safe for guarded statements that an ESD protection device should sit close to the external connector or other surge-entry point.
- Safe for wording that the exposure path into the protected IC should stay short and direct before the clamp path acts.
- Do not use this source for trace-length numbers, ground-via counts, clamping-performance guarantees, IEC pass claims, or universal connector prescriptions.

## Refresh Notes

- Refresh before publication if exact device family, revision, or layout-figure wording matters.
