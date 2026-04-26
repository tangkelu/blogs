---
source_id: "frontendapt-capabilities-index-en"
title: "APTPCB English Capabilities JSON Index"
organization: "APTPCB"
source_type: "internal_json_group"
url: "/code/hileap/frontendAPT/public/static/capabilities/en"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-04-24"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "aptpcb", "capabilities", "pcb", "hdi", "flex", "rigid-flex", "metal-core", "ceramic"]
status: "active"
notes: "Directory-level registry record for APT English capabilities JSON files not needing one fact card per page."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendAPT/public/static/capabilities/en/index.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/flex-pcb.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/metal-pcb.json`
- `/code/hileap/frontendAPT/public/static/capabilities/en/ceramic-pcb.json`

## Why It Matters

- Captures the top-level internal capability taxonomy for APT PCB fabrication pages.
- Useful as a breadth source when prompts need to confirm that a capability family exists before selecting deeper fact cards.

## Extraction Notes

- Treat these pages as internal support for capability existence and category coverage.
- Use the more specific PCB/product source records and official sources for numeric limits, material parameters, standards, or customer-facing claims.

## Refresh Notes

- Re-check when the capabilities navigation or top-level capability pages are revised.
