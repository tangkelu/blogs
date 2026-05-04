---
topic_id: "processes-remote-control-and-drone-control-stack-boundaries"
title: "Remote-Control And Drone Control-Stack Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-remote-control-and-drone-control-stack-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"
source_ids:
  - "vishay-ir-receiver-modules-page"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
tags: ["remote-control", "drone", "px4", "mavlink", "expresslrs", "ir", "receiver", "autopilot", "telemetry", "active-boundary"]
---

# Definition

> The `remote-control-circuits`, `remote-control-car-circuits`, and `diy-drone` family is active only at a conservative control-stack boundary level: transmitter / receiver architecture, IR receiver-module role, RC-link identity, autopilot / flight-controller identity, actuator-output context, and telemetry / ground-station protocol identity. This lane does not support universal performance, compatibility, autonomy, latency, RF-default, deployment, or manufacturing claims.

## Routing Guidance

- Route consumer IR discussion through IR transmitter / receiver-module vocabulary and keep it at signal-chain identity level.
- Route RC-car and general remote-control discussion through transmitter / receiver / ESC / steering-servo topology rather than universal RF-stack defaults.
- Route drone control-stack discussion through separate layers: RC input path, autopilot or flight-controller layer, actuator outputs, and telemetry or command protocol context.
- Route Bluetooth, Wi-Fi, GPS, and adjacent interface claims through `standards-interface-wireless-positioning-product-level-boundary` instead of stretching this page beyond control-stack scope.
- Route any version-specific setup, compatibility, performance, or deployment statement to a must-refresh evidence lane before publication.

## Stable Facts

- Vishay supports manufacturer-scoped IR receiver-module identity for remote-control applications and signal-chain vocabulary at component-role level.
- PX4 supports high-level autopilot and flight-controller identity for vehicles, sensors, actuators, and flight-control stack context.
- MAVLink supports communication-protocol identity between vehicle, ground-station, and companion-system contexts.
- ExpressLRS supports high-level identity as an open-source RC control-link ecosystem with transmitter and receiver setup vocabulary.
- Existing internal drone / UAV scenario framing remains usable for aircraft-context clustering such as flight control, RF communication, power, navigation, and lightweight integration, but not for proving current feature completeness.
- The supported architecture layer is:
  `transmitter or user input -> receiver / control link -> controller or autopilot -> actuator outputs`,
  with telemetry / command protocol context treated as a separate but related layer.

## Engineering Boundaries

- Keep `remote-control-circuits.md` at architecture and component-role level unless a future source pass adds narrower wireless-stack or part-specific evidence.
- Keep `remote-control-car-circuits.md` at transmitter / receiver / ESC / servo topology level; do not present one RF band, modulation family, or protocol family as the universal default.
- Keep `diy-drone.md` at workflow and control-stack identity level when it mentions PX4, MAVLink, or ExpressLRS.
- Separate control-link identity from telemetry identity. A named protocol or project page does not prove end-to-end field performance.
- Treat exact radio behavior, telemetry quality, autonomy capability, real-world responsiveness, and compliance posture as separate evidence lanes that still need narrower sources.

## Blocked Claims

- Universal performance and compatibility claims remain blocked, including claims about best protocol, lowest latency, superior range, anti-interference behavior, coexistence, update rate, jitter, throughput, or broad cross-brand compatibility.
- Autonomy or latency claims remain blocked, including autonomous avoidance, return-to-home, AI navigation, route planning, swarm behavior, or any statement that these sources prove responsiveness or control latency.
- RF default-band claims remain blocked, including fixed claims that modern RC systems default to `2.4 GHz`, `5.8 GHz`, `433 MHz`, `315 MHz`, or any other band without narrower evidence for the exact product class.
- Deployment or manufacturing claims remain blocked, including statements that a supplier can build, test, certify, qualify, deploy, or manufacture a production-ready drone, RC-car, or remote-control product from this lane alone.

## Common Misreadings

- `2.4 GHz is the standard for modern RC systems`
- `FHSS`, `anti-interference`, or simultaneous-multi-vehicle operation is universally proven from this lane
- `ExpressLRS is the best`, `fastest`, or `lowest-latency` protocol
- `MAVLink proves reliable long-range telemetry` or broad system compatibility
- `PX4 supports autonomous avoidance`, `return-to-home`, or `AI navigation` from this source set alone
- `IR remotes normally use 38 kHz` or fixed line-of-sight distance rules without exact component documentation
- `smartphone app`, `cloud`, `OTA`, `voice assistant`, `AI remote`, or `semi-autonomous` wording as if already supported by this lane

## Must Refresh Before Publishing

- Current PX4, MAVLink, or ExpressLRS version-specific claims
- Current hardware support lists, setup flows, or ecosystem compatibility statements
- Any claim framed as `latest`, `today`, `modern standard`, or `current best choice`
- Any supplier-specific manufacturing, certification, lead-time, or deployment claim

## Related Facts And Source Scope

- `methods-remote-control-and-drone-control-stack-boundary` is the primary fact card for control-stack identity, source limits, and non-claims.
- `standards-interface-wireless-positioning-product-level-boundary` is the routing card when drafts drift into Bluetooth, Wi-Fi, GPS, GNSS, or other product-level interface language.
- Source scope for this page is limited to the already-landed local source set: Vishay IR receiver modules, PX4 basic concepts, MAVLink overview, ExpressLRS getting started, and the internal drone / UAV scenario page.

## Supported Draft Families

- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`

## Primary Sources

- https://www.vishay.com/en/ir-receiver-modules/
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
