---
source_id: "infineon-ap24026-emc-and-system-esd-design-guidelines-board-layout"
title: "AP24026 EMC and System-ESD Design Guidelines for Board Layout"
organization: "Infineon Technologies"
source_type: "application_note"
url: "https://www.infineon.com/dgdl/Infineon-AP2402635_General_PCB-ApplicationNotes-v03_05-EN.pdf?fileId=5546d46261ff5777016229f8523036f1"
jurisdiction: "global"
published_at: "2021-09"
checked_at: "2026-05-10"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["infineon", "emc", "esd", "pcb-layout", "return-path", "ground", "connector", "board-edge"]
status: "active"
notes: "Official Infineon application note. Use for narrow wording about maintaining continuous low-impedance return/ground paths, avoiding interrupted or split reference regions near entry and exposed zones, and separating externally exposed routing regions from cleaner internal routing. Do not use it for exact plane setbacks, via counts, compliance results, or interface-specific recipe claims."
---

# Source Summary

## What It Covers

- board-layout guidance for EMC and system-level ESD
- continuous ground / return path posture
- avoiding discontinuities, large loop areas, and exposed-zone coupling problems
- general entry-region and exposed-region layout discipline

## Why It Matters

- gives the `194页` handbook `D5` lane a current-public owner anchor for `surface-ground continuity + exposed-zone isolation`, which is adjacent to but not the same as the already-landed entry-path interception lane

## Extraction Notes

- Safe for guarded statements that connector-near or exposed regions should keep a continuous local return/ground path.
- Safe for wording that split, slot, or interrupted reference regions can enlarge loop area or weaken the local return path.
- Safe for wording that exposed routing regions should be kept apart from cleaner internal sensitive traces.
- Do not use this source for exact keepout numbers, copper dimensions, via counts, shield distances, or EMC/ESD pass guarantees.

## Refresh Notes

- Refresh before publication if exact Infineon revision or figure wording matters.
