---
source_id: "mavlink-overview-page"
title: "MAVLink Overview"
organization: "MAVLink"
source_type: "software_official_docs"
url: "https://mavlink.io/en/about/overview.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-29"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["mavlink", "telemetry", "protocol", "ground-control", "autopilot", "uav", "drone"]
status: "active"
notes: "Official MAVLink overview page. Use for protocol identity between vehicles, ground stations, and companion systems; do not generalize link quality, latency, or mission reliability from this page alone."
---

# Source Summary

## What It Covers

- Official MAVLink protocol identity
- Project-owned overview of MAVLink as a communication protocol for drones and related vehicles
- Vocabulary for communication among vehicles, onboard components, and ground-control / companion systems

## Why It Matters

- Supports a conservative telemetry / command-link identity layer for `diy-drone.md`.
- Helps separate protocol identity from receiver-brand, RF-band, and control-link performance claims.

## Extraction Notes

- Safe to say MAVLink is a communication protocol used in drone and related vehicle ecosystems.
- Safe to use `ground station`, `vehicle`, `companion computer`, `telemetry`, and protocol vocabulary at architecture level.
- Do not use this page alone for bandwidth, latency, security, reliability, or compatibility guarantees.

## Refresh Notes

- Refresh before publication if a draft cites current protocol versions, ecosystem support, or feature-extension status.
