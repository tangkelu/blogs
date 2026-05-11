---
source_id: "nxp-an11397-ptn3363-pcb-layout-guidelines"
title: "AN11397: PTN3363/65/66 PCB Layout Guidelines"
organization: "NXP Semiconductors"
source_type: "application_note"
url: "https://www.nxp.com/docs/en/application-note/AN11397.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-06"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["nxp", "via-transition", "return-path", "layer-change", "ground-vias", "pcb-layout"]
status: "active"
notes: "Official NXP application note. Use for via-transition discontinuity and nearby ground-via return-path language only; do not generalize into universal routing recipes."
---

# Source Summary

## What It Covers

- Via transitions can create discontinuity and parasitic capacitance/stub concerns
- Layer transitions should keep the return current local through nearby ground vias
- Via transitions should be treated as SI-sensitive structures rather than electrically invisible connectors

## Why It Matters

- Adds a direct primary-source anchor for the `via-transition` portion of the EMC lane
- Supports a narrower fact card that is more specific than generic return-path continuity alone

## Extraction Notes

- Safe for guarded wording about via discontinuity, parasitics, and local return-path cleanup
- Safe for phrases like `place ground vias near signal vias` when describing a layer transition
- Do not use this source for exact spacing, via-count, antipad, or universal bridging rules

## Refresh Notes

- Refresh before publication if NXP updates the note or URL structure
