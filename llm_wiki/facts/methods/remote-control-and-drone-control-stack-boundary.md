---
fact_id: "methods-remote-control-and-drone-control-stack-boundary"
title: "Official IR, autopilot, telemetry, and RC-link sources support control-stack identity, not universal remote-control performance claims"
topic: "Remote-control and drone control-stack boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "vishay-ir-receiver-modules-page"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
tags: ["remote-control", "ir", "px4", "mavlink", "expresslrs", "drone", "autopilot", "receiver", "telemetry", "control-stack-boundary"]
---

# Canonical Summary

> Official Vishay, PX4, MAVLink, and ExpressLRS sources support a conservative remote-control and drone-control boundary at architecture level: IR remote-control writing can describe transmitter-to-receiver component roles; drone writing can distinguish RC control link, autopilot / flight-controller layer, actuator-output layer, and telemetry / companion / ground-station protocol context. These sources do not authorize universal band defaults, range, latency, anti-interference, compatibility, telemetry-quality, AI, or autonomy-performance claims.

## Stable Facts

- Vishay's official IR receiver-module page supports manufacturer-scoped identity for IR receiver modules used in remote-control applications.
- The Vishay source supports `IR receiver module` and remote-control component vocabulary at signal-chain level, not finished-system performance proof.
- PX4's official concepts page supports PX4 identity as an open-source autopilot platform and supports high-level terminology for vehicles, sensors, actuators, and flight-control stack context.
- MAVLink's official overview supports MAVLink identity as a communication protocol used in drone and related vehicle ecosystems, including vehicle and ground / companion communication vocabulary.
- ExpressLRS's official getting-started docs support ExpressLRS identity as an open-source RC control-link ecosystem with transmitter and receiver setup vocabulary.
- The internal drone / UAV page continues to support scenario framing for flight control, RF communication, power, and navigation context without proving current feature completeness or regulatory readiness.
- Together, these sources support a guarded architecture layer:
  `user input / transmitter -> receiver or control link -> autopilot / controller -> actuator outputs`,
  with telemetry / ground-station or companion-protocol context kept separate from the control-link identity.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`, `remote-control-car-circuits.md`, and `diy-drone.md` when the article needs control-stack vocabulary rather than protocol-performance claims.
- Safe posture for consumer IR: describe encoded transmission plus IR receiver-module role, but avoid fixing universal carrier values or distance claims without exact component documents.
- Safe posture for RC-car content: describe transmitter / receiver / ESC / steering-servo architecture and optional named ecosystem identity such as ExpressLRS only at project-documentation level.
- Safe posture for drone content: separate autopilot / flight-controller role, RC input path, telemetry / command protocol path, and actuator-output context.
- Pair with `standards-interface-wireless-positioning-product-level-boundary` when a draft also mentions Bluetooth, Wi-Fi, GPS, or related wireless/product-level interfaces.
- Require narrower vendor datasheets, protocol docs, customer requirements, or dated capability records before publishing exact performance, compatibility, or certification language.

## Limits And Non-Claims

- This card does not support universal `38 kHz`, `315 MHz`, `433 MHz`, `2.4 GHz`, or `5.8 GHz` default-band claims for remote control.
- It does not support range, latency, update-rate, jitter, packet-rate, throughput, anti-interference, FHSS, DSSS, or coexistence claims.
- It does not support cross-brand transmitter / receiver compatibility claims or protocol-ranking claims such as `best`, `modern standard`, or `lowest latency`.
- It does not support ESC current, PWM-rate, thermal, braking, torque, BMS, USB-C PD, or other hardware-performance claims from the drafts.
- It does not support GPS hold, return-to-home, FPV quality, obstacle avoidance, autonomous driving, AI-control quality, route planning, or swarm-control claims.
- It does not prove any supplier can build, test, or certify a drone, RC-car, or remote-control product for real deployment.

## Open Questions

- Add exact Vishay datasheets if a future pass needs narrow carrier-family or demodulating-receiver details tied to exact part numbers.
- Add ArduPilot, Betaflight, or exact receiver-protocol source records only if future rewrites need those named ecosystems after the current downgrade pass.
- Add transceiver-vendor sources such as TI, Silicon Labs, or Nordic only if future drafts must keep hardware-radio family language beyond current architecture-level identity.

## Source Links

- https://www.vishay.com/en/ir-receiver-modules/
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
