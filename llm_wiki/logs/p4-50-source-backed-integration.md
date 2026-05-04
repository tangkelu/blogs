# P4-50 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the strongest remaining `P4-48` residual lane into reusable `llm_wiki` data by adding narrow official authority for remote-control and drone control-stack identity.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated RF band defaults, spread-spectrum claims, latency, telemetry quality, ESC electrical performance, app-control, AI/autonomy, supplier capability, or finished-product readiness claims.

## Inputs Reviewed

- `logs/p4-48-parallel-scout-controller-summary.md`
- `logs/p4-48a-remote-control-protocol-authority-scout.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`
- existing interface / wireless, drone-application, and maker-platform boundary layers already present in `llm_wiki`

## Parallel Work Pattern

- Main agent owned official-source recovery, final integration, and tracker updates.
- A `mini` bounded explorer re-checked the smallest safe local claim set and confirmed most performance / compatibility language must stay blocked.
- A stronger bounded explorer re-checked local `P4-47` / `P4-49` file patterns so `P4-50` follows the same `1 log + source records + 1 fact + 1 wiki` integration shape.
- Explorer conclusions aligned with main-agent source recovery:
  - `remote-control-circuits.md` can now use conservative IR receiver-module and control-chain identity only
  - `remote-control-car-circuits.md` can now use transmitter / receiver / ESC / servo topology plus guarded named RC-link identity only
  - `diy-drone.md` can now distinguish autopilot, telemetry protocol, and RC-link layers without promoting autonomous-flight or performance claims

## Source Records Added

- `sources/registry/methods/vishay-ir-receiver-modules-page.md`
- `sources/registry/methods/px4-basic-concepts-guide.md`
- `sources/registry/methods/mavlink-overview-page.md`
- `sources/registry/methods/expresslrs-getting-started.md`

These source records add:

- official Vishay IR receiver-module identity for remote-control reception context
- official PX4 autopilot / actuator / vehicle-control vocabulary
- official MAVLink communication-protocol identity for vehicle / ground / companion communication
- official ExpressLRS RC control-link ecosystem identity for transmitter / receiver setup context

## Fact Card Added

- `facts/methods/remote-control-and-drone-control-stack-boundary.md`

This fact card upgrades the `remote-control-circuits` / `remote-control-car-circuits` / `diy-drone` family from scout-only into a conservative source-backed control-stack boundary.

What is now source-backed:

- IR remote-control writing at receiver-module and signal-chain identity level
- transmitter -> receiver / control-link -> controller or autopilot -> actuator-output architecture language
- drone control-stack separation among RC input path, autopilot / flight-controller role, and telemetry / ground / companion protocol role
- project-owned identity for named ecosystems such as PX4, MAVLink, and ExpressLRS at high level only

## Topic Wiki Added

- `wiki/processes/remote-control-and-drone-control-stack-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`

## What This Unlocks

- `remote-control-circuits.md` can now be conservatively rewritten as a control-architecture article:
  - transmitter / encoded signal / receiver role
  - IR receiver-module identity
  - guarded separation between control link and higher-level smart-device claims
- `remote-control-car-circuits.md` can now route through a conservative RC architecture layer:
  - transmitter, receiver, ESC, steering-servo, and controller topology
  - optional named RC-link ecosystem identity without performance ranking
- `diy-drone.md` can now route through a conservative drone control-stack layer:
  - autopilot / flight-controller identity
  - RC-link identity
  - telemetry / command protocol identity
  - existing internal drone / UAV scenario framing

## Still Blocked

- universal IR carrier claims such as `38 kHz` without exact component-level documentation
- universal RF band defaults such as `315 MHz`, `433 MHz`, `2.4 GHz`, or `5.8 GHz`
- FHSS, DSSS, anti-interference, coexistence, range, latency, update-rate, throughput, RSSI, LQ, or telemetry-quality claims
- cross-brand transmitter / receiver compatibility claims
- ESC current, PWM-rate, thermal, braking, torque, BMS, USB-C PD, or exact hardware-performance claims
- Bluetooth / Wi-Fi / cloud / OTA / smartphone / voice-assistant control claims in this draft family unless separately routed to narrower official sources
- PX4 / MAVLink / ExpressLRS language used as proof of autonomy quality, return-to-home, GPS hold, FPV quality, object avoidance, route planning, or AI-control capability
- supplier capability, certification, deployment, yield, quality, lead-time, or production-readiness claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.3` remote-control and drone control-stack lane
- next likely residual lane:
  - HDI / BOM cost-driver official-source or dated capability recovery
  - narrower RC transceiver or exact receiver-protocol recovery only if future rewrite scope still needs it
