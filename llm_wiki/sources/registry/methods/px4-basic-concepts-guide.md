---
source_id: "px4-basic-concepts-guide"
title: "PX4 Basic Concepts"
organization: "PX4"
source_type: "software_official_docs"
url: "https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-29"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["px4", "autopilot", "flight-controller", "uav", "drone", "actuators", "sensors", "telemetry"]
status: "active"
notes: "Official PX4 documentation page for basic platform concepts. Use for autopilot, vehicle, sensor, actuator, and control-stack identity only; refresh before current firmware-feature or version-specific claims."
---

# Source Summary

## What It Covers

- Official PX4 platform identity and terminology
- Documentation-owned vocabulary for autopilot, vehicles, sensors, actuators, and control-stack concepts
- High-level framing of how PX4 fits into drone and robotic vehicle systems

## Why It Matters

- Supports a conservative drone control-stack identity layer for `diy-drone.md`.
- Helps separate autopilot / flight-control concepts from receiver-link and telemetry-protocol claims.

## Extraction Notes

- Safe to say PX4 is an open-source autopilot platform used in drone and robotic-vehicle contexts.
- Safe to use autopilot, flight-controller, actuator, sensor, and vehicle terminology at high level.
- Do not use this page alone for autonomous-feature quality, navigation accuracy, return-to-home, obstacle-avoidance, or flight-performance claims.

## Refresh Notes

- Refresh before publication if a draft cites current PX4 version, exact feature support, or current vehicle/platform coverage.
