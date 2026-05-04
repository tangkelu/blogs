---
source_id: "ti-high-speed-layout-guidelines"
title: "High Speed Layout Guidelines"
organization: "Texas Instruments"
source_type: "application_report"
url: "https://www.ti.com/lit/an/scaa082a/scaa082a.pdf"
jurisdiction: "global"
published_at: "2017-08"
checked_at: "2026-05-02"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["texas-instruments", "high-speed", "pcb-layout", "return-current", "plane-split", "ground-plane", "stitching-vias"]
status: "active"
notes: "Official TI application report. Use for return-current continuity, plane-split avoidance, and via-transition grounding posture; do not use it as a universal routing-rule table."
---

# Source Summary

## What It Covers

- Return current following the lowest-impedance path at higher frequencies
- Signal-routing problems created by slots or splits in the reference plane
- Need for return current to stay directly under or beside the signal trace
- Use of nearby ground vias when changing signal layers

## Why It Matters

- Gives the lane a current primary-source anchor for reusable return-path continuity language without relying on draft-originated telecom prose.

## Extraction Notes

- Safe for guarded statements that plane discontinuities create loop area and that return-current continuity must be preserved through routing and layer changes.
- Safe for wording about avoiding slots in the ground reference plane and using ground vias near signal vias when the reference path changes.
- Do not use this source for numeric EMI limits, exact via counts, or proof that a specific product layout passes validation.

## Refresh Notes

- Refresh before publication if TI updates the report revision or URL.
