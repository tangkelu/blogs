---
source_id: "kollmorgen-gantry-mode-page"
title: "Gantry Mode"
organization: "Kollmorgen"
source_type: "documentation_page"
url: "https://webhelp.kollmorgen.com/kas4.02/Content/AKD2G_User_Manual/Gantry%20Mode.htm"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-05"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["gantry", "dual-axis-drive", "synchronization", "motion-control", "limits", "homing"]
status: "active"
notes: "Official Kollmorgen gantry-mode documentation. Use for guarded wording around master/slave gantry behavior, shared limits, and command ownership; avoid turning it into universal no-delay or performance claims."
---

# Source Summary

## What It Covers

- Gantry mode for a dual-axis drive
- Master/slave command relationship
- Shared limit handling and homing behavior under gantry mode

## Why It Matters

- Supports the board-review idea that a gantry board is not just a motor-power board; it also owns synchronization behavior and coordinated stop conditions.
- Provides official support for writing about shared command ownership, coordinated limits, and dual-axis release burden.

## Extraction Notes

- Safe for statements that a gantry configuration can make one axis follow another as one machine axis with synchronized behavior.
- Safe for statements that limits and stop conditions on either side can affect the whole gantry pair.
- Do not use this page for absolute motion-performance, zero-latency, or accuracy guarantees.

## Refresh Notes

- Refresh before publication because vendor documentation can change.
