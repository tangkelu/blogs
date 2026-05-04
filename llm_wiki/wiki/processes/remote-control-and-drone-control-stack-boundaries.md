---
topic_id: "processes-remote-control-and-drone-control-stack-boundaries"
title: "Remote-Control And Drone Control-Stack Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-29"
fact_ids:
  - "methods-remote-control-and-drone-control-stack-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"
source_ids:
  - "vishay-ir-receiver-modules-page"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
tags: ["remote-control", "drone", "px4", "mavlink", "expresslrs", "ir", "receiver", "autopilot", "telemetry", "draft-boundary"]
---

# Definition

> The `remote-control-circuits`, `remote-control-car-circuits`, and `diy-drone` family is now safe only at a conservative control-stack boundary level: transmitter / receiver architecture, IR receiver-module role, RC link identity, autopilot / flight-controller identity, actuator-output context, and telemetry / ground-station protocol identity. The current corpus is still not strong enough for universal performance, compatibility, or autonomy claims.

## Why This Topic Matters

- The `2025.11.3` remote-control and drone drafts currently read like broad authority pieces, but most of their strongest claims were still unsupported after `P4-48`.
- A narrow official-source recovery pass can still unlock useful rewrite posture if it focuses on component and control-stack identity rather than performance narratives.
- This page makes that safe posture prompt-consumable for future rewrite work.

## Stable Facts

- Consumer IR remote-control writing can now use official manufacturer-scoped IR receiver-module identity from Vishay.
- Drone and robotic-vehicle writing can now use PX4 as an official autopilot / flight-controller identity anchor at high level.
- Drone communication-stack writing can now use MAVLink as an official communication-protocol identity anchor between vehicle and ground / companion systems.
- RC transmitter / receiver ecosystem writing can now use ExpressLRS as an official open-source RC link identity anchor at high level.
- Existing internal drone / UAV scenario framing remains usable for aircraft-context hardware clustering such as flight control, RF communication, navigation, and lightweight integration.
- The newly supported architecture layer is:
  `transmitter or user input -> receiver / control link -> controller or autopilot -> actuator outputs`,
  with telemetry / command protocol context treated as a separate but related layer.

## Engineering Boundaries

- Keep `remote-control-circuits.md` at architecture and component-role level unless a future source pass adds narrower wireless-stack sources.
- Keep `remote-control-car-circuits.md` at transmitter / receiver / ESC / servo topology level; do not present one RF band or protocol family as the universal default.
- Keep `diy-drone.md` at workflow and control-stack identity level when it mentions PX4, MAVLink, or ExpressLRS.
- Route Bluetooth, Wi-Fi, and GPS identity claims through the existing interface / wireless boundary card instead of stretching drone or RC sources beyond scope.
- Treat exact radio behavior, telemetry quality, autonomy capability, and real-world responsiveness as separate evidence lanes that still need narrower sources.

## Common Overclaims To Block

- `2.4 GHz is the standard for modern RC systems`
- `FHSS` or similar anti-interference language as a universal fact
- `multiple vehicles can operate simultaneously without interference`
- `ExpressLRS is the best / fastest / lowest-latency protocol`
- `MAVLink proves reliable long-range telemetry`
- `PX4 supports autonomous avoidance / return-to-home / AI navigation` without narrower feature sources
- `IR remotes normally use 38 kHz` or fixed line-of-sight distance rules without exact component docs
- `smartphone app`, `cloud`, `OTA`, `voice assistant`, `AI remote`, or `semi-autonomous` wording as if already supported by this lane

## Must Refresh Before Publishing

- Current PX4, MAVLink, or ExpressLRS version-specific claims
- Current hardware support lists, setup flows, or ecosystem compatibility statements
- Any claim framed as `latest`, `today`, `modern standard`, or `current best choice`
- Any supplier-specific manufacturing, certification, lead-time, or deployment claim

## Supported Draft Families

- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`

## Related Fact Cards

- `methods-remote-control-and-drone-control-stack-boundary`
- `standards-interface-wireless-positioning-product-level-boundary`

## Primary Sources

- https://www.vishay.com/en/ir-receiver-modules/
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
