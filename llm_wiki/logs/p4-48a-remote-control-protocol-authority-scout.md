# P4-48A Remote-Control Protocol Authority Scout

- date: 2026-04-29
- lane: `P4-48A remote-control protocol authority scout`
- output_scope: `log only`
- status: `scout_only`

## Purpose And Scope

Treat the assigned `2025.11.3` drafts as claim inventory only, cross-check current `llm_wiki` support for remote-control / RF-control / drone-control authority, and identify only the next official-source lanes worth recovering.

This scout does not create facts, wiki pages, source records, or tracker edits. It is conservative about temporally unstable protocol, band, range, latency, telemetry, and compatibility claims.

## Exact Files Reviewed

### Claim-inventory inputs

- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`
- `/code/blogs/llm_wiki/logs/p4-40-2025-11-3-consumer-rf-usb-ptfe-official-source-recovery-scout.md`

### Existing `llm_wiki` support and handoff files cross-checked

- `/code/blogs/llm_wiki/logs/p4-33-lane-g-delta-2025-11-3-and-2025-11-17.md`
- `/code/blogs/llm_wiki/logs/p4-41-2025-12-29-power-automotive-drone-wireless-assembly-official-source-recovery-scout.md`
- `/code/blogs/llm_wiki/logs/p4-46-source-backed-integration.md`
- `/code/blogs/llm_wiki/logs/p4-47-source-backed-integration.md`
- `/code/blogs/llm_wiki/wiki/applications/industry-application-scenarios-and-boundaries.md`
- `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`
- `/code/blogs/llm_wiki/facts/methods/maker-platform-official-identity-boundary.md`
- `/code/blogs/llm_wiki/facts/standards/smart-home-protocol-identity-boundary.md`
- `/code/blogs/llm_wiki/facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-industry-drone-uav-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/standards/bluetooth-core-specification-page.md`
- `/code/blogs/llm_wiki/sources/registry/methods/espressif-esp32-c6-product-page.md`
- `/code/blogs/llm_wiki/sources/registry/methods/espressif-esp32-h2-product-page.md`

## Existing `llm_wiki` Support Worth Reusing

The current corpus has some reusable boundary support, but not a real remote-control protocol authority layer.

1. Drone / UAV application framing only
   - `wiki/applications/industry-application-scenarios-and-boundaries.md`
   - `sources/registry/internal/frontendapt-industry-drone-uav-page-en.md`
   - Useful for scenario wording such as flight-control, RF, navigation, and lightweight-integration context.
   - Not enough for autopilot, radio-link, telemetry, or flight-performance claims.

2. Wireless / interface identity only
   - `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
   - `sources/registry/standards/bluetooth-core-specification-page.md`
   - Useful for Bluetooth identity and product-level boundary wording.
   - Not enough for range, latency, qualification, compatibility, or finished-device behavior.

3. ESP32 and smart-home identity only
   - `facts/methods/maker-platform-official-identity-boundary.md`
   - `facts/standards/smart-home-protocol-identity-boundary.md`
   - `sources/registry/methods/espressif-esp32-c6-product-page.md`
   - `sources/registry/methods/espressif-esp32-h2-product-page.md`
   - Useful only if the drafts keep ESP32 / Matter / Thread / Zigbee / BLE identity vocabulary.
   - Not enough for remote-control responsiveness, interoperability, RF performance, or app compatibility claims.

4. RF test vocabulary only
   - `wiki/testing/rf-validation-and-test-coverage.md`
   - Useful for guarded testing language if a rewrite needs generic TDR / VNA / OTA boundary wording.
   - Not enough for consumer RC protocol behavior, anti-interference claims, or control-link performance.

5. Prior scout and integration support
   - `p4-33`, `p4-40`, `p4-41`, `p4-46`, and `p4-47` already treat this family as residual source-recovery work, not source-backed integration.

## Claim-Family Disposition For Remote-Control / RC-Car / Drone-Control

| Claim family | Current disposition | Reuse posture | Why it is still blocked |
| --- | --- | --- | --- |
| `remote-control-circuits.md` general wireless-control framing | `boundary_only_with_major_gaps` | transmitter / receiver / control-loop taxonomy only | no authoritative IR, sub-GHz, 2.4 GHz, Bluetooth-control, Wi-Fi-control, latency, range, or interoperability layer |
| `remote-control-car-circuits.md` RC-car radio and control stack | `blocked_pending_official_source` | very limited module nouns such as transmitter, receiver, ESC, servo | no official support for `2.4 GHz` defaulting, FHSS claims, telemetry, protocol families, ESC signaling, or RC-car compatibility claims |
| `diy-drone.md` drone-control and flight-stack language | `blocked_pending_official_source` | generic drone / UAV application framing only | no official PX4 / ArduPilot / MAVLink / Betaflight / receiver-protocol source layer in current corpus |
| smartphone / app / IoT control sections inside the family | `partial_identity_only` | BLE / Matter / Thread / Zigbee / ESP32 identity vocabulary only | current support does not prove app compatibility, cloud control, OTA quality, or final-device interoperability |

## Safe Reuse Classes

- generic transmitter / receiver / controller / actuator topic clustering
- drone / UAV / RC-car / smart-device application taxonomy
- Bluetooth identity at standards-owner level only
- ESP32-C6 / ESP32-H2 connectivity identity at vendor-page level only
- Matter / Thread / Zigbee identity and bridge-boundary wording only
- RF validation vocabulary only when clearly separated from protocol behavior

## Blocked Claim Classes

- IR `38 kHz` or other carrier-frequency claims unless tied to exact official component sources
- RF band defaults such as `315 MHz`, `433 MHz`, `2.4 GHz`, or `5.8 GHz` stated as generic RC norms
- spread-spectrum, FHSS, DSSS, anti-interference, or coexistence claims stated without exact protocol or vendor anchors
- range, latency, update-rate, packet-rate, jitter, throughput, link-budget, or responsiveness claims
- transmitter / receiver compatibility claims across brands or protocol families
- telemetry, RSSI, LQ, bidirectional feedback, or app-dashboard claims
- Wi-Fi remote control, cloud control, OTA, Alexa / Google / Home Assistant compatibility, or smartphone-control claims
- ESC protocol, servo protocol, PWM rate, current, thermal, or `100 A`-style hardware claims
- PX4, ArduPilot, Betaflight, iNav, MAVLink, ExpressLRS, SBUS, CRSF, FPort, i-BUS, Spektrum, FrSky, Futaba, FlySky, or Radiomaster claims without official-source recovery
- GPS, FPV, VTX, autonomous driving, obstacle avoidance, return-to-home, or AI-control claims
- any recommendation language such as `best protocol`, `modern standard`, `industry standard`, `better range`, or `lower latency`

## Best Official-Source Candidates Worth Recovering Next

### 1. Infrared remote-control component lane

Best source owners:

- `Vishay` IR receiver module product pages, datasheets, and remote-control application notes

Why this lane is worth recovering:

- supports consumer IR receiver identity, carrier-family vocabulary, demodulating-receiver role, and IR remote-control data-format framing
- can replace unsupported draft statements that treat `38 kHz` and line-of-sight behavior as generic universal facts without source anchoring

### 2. Low-power RC transceiver lane for sub-GHz and 2.4 GHz control links

Best source owners:

- `TI` transceiver pages such as `CC2500` and adjacent control-link parts
- `Silicon Labs` sub-GHz radio pages such as `Si4463`
- `Nordic Semiconductor` `nRF24` family pages

Why this lane is worth recovering:

- supports vendor-scoped RF band, modulation, packet, RSSI / LQI, and hopping-capable hardware vocabulary
- creates a safer basis for generic RC-car and remote-control hardware sections than the current draft prose

Boundary:

- still should not be turned into universal RC-car default-band, universal range, or cross-brand compatibility claims

### 3. Drone autopilot and telemetry protocol lane

Best source owners:

- `PX4` official docs
- `ArduPilot` official docs
- `MAVLink` official protocol docs

Why this lane is worth recovering:

- supports control-path separation between RC input, telemetry, mission control, and autopilot output
- supports official vocabulary for receiver input, output channels, ESC control context, and telemetry protocol identity
- directly addresses the weakest control-stack sections in `diy-drone.md`

### 4. Modern receiver-protocol lane for drone and RC ecosystems

Best source owners:

- `ExpressLRS` official docs
- `Betaflight` official receiver and setup docs
- exact vendor pages only if named brands must remain, for example `Spektrum`, `FrSky`, `Futaba`, or `Team BlackSheep`

Why this lane is worth recovering:

- supports official identity for current receiver protocol nouns such as `CRSF`, `ELRS`, `SBUS`, `FPort`, and `i-BUS`
- creates a narrower, more defensible path for receiver wiring and protocol-selection wording

Boundary:

- brand-specific compatibility and performance should remain exact-source only, not generalized

### 5. Secondary Wi-Fi / BLE app-control lane

Best source owners:

- `Bluetooth SIG`
- `Espressif` exact module / framework docs
- `Wi-Fi Alliance` only if certification or Wi-Fi product language must remain

Why this lane is lower priority:

- current `llm_wiki` already has partial BLE / Matter / Thread / ESP32 identity coverage
- this helps only if the drafts keep smartphone, app, or IoT-control sections after the core RC and drone protocol gaps are solved

## Recommendation

This lane is **not strong enough for immediate source-backed integration** as a remote-control protocol family.

Current `llm_wiki` support is good enough only for:

- generic control-system taxonomy
- drone / UAV application framing
- narrow Bluetooth / ESP32 / Matter / Thread identity wording

It is **not** good enough for the core claims that make these drafts read like remote-control protocol authority: band selection, protocol choice, latency, telemetry, receiver compatibility, RC-car radio behavior, or drone-control stack behavior.

Recommended handling: keep this family `scout_only` until at least lanes `1` through `4` above are recovered into real source records and boundary cards.
