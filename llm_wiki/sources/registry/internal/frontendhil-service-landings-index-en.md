---
source_id: "frontendhil-service-landings-index-en"
title: "HILPCB English Service Landings JSON Index"
organization: "HILPCB"
source_type: "internal_json_group"
url: "/code/hileap/frontendHIL/data/service-landings/en"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-04-24"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "hilpcb", "service-landings", "prototype", "quick-turn", "surface-finish"]
status: "active"
notes: "Directory-level registry record for HIL English service landing JSON files."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendHIL/data/service-landings/en/pcb-prototype.json`
- `/code/hileap/frontendHIL/data/service-landings/en/quick-turn-pcb.json`
- `/code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json`

## Why It Matters

- Captures HIL landing-page support for prototype, quick-turn, and surface-finish service framing.

## Extraction Notes

- `pcb-surface-finish.json` already has a more specific source record for finish-related facts.
- Use this grouped record as service-framing support for prototype and quick-turn prompts.
- Refresh turnaround-time claims before publication.

## Refresh Notes

- Re-check before using any quick-turn timing, lead-time, or availability claim externally.
