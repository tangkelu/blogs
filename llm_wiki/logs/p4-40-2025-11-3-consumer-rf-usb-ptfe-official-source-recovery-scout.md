# P4-40 Official-Source Recovery Scout

- date: 2026-04-28
- lane: `P4-40 official-source recovery scout`
- input_dir: `/code/blogs/tmps/2025.11.3/en`
- output_scope: `log only`
- status: `source_backed_fact_layer_partial`
- batch_status_note: `completed_at_claim_family_level` for the batch intake; only some claim families already have source-backed support in existing `llm_wiki`

## Purpose

Inspect the `2025.11.3/en` drafts as claim inventory only, cross-check existing `llm_wiki` coverage, and identify official-source candidates worth recovering next for:

- PTFE / Teflon / low-loss / ultra-low-loss PCB
- USB-C / Type-C charger / USB port taxonomy
- ESP32 / Raspberry Pi / DIY electronics
- RF / remote control / satellite / drone / smart-home application claims
- consumer-electronics company and ranking claims

## Input Files Inspected

- `/code/blogs/tmps/2025.11.3/en/high-frequency-ptfe-pcb.md`
- `/code/blogs/tmps/2025.11.3/en/low-loss-pcb.md`
- `/code/blogs/tmps/2025.11.3/en/ptfe-circuit-board.md`
- `/code/blogs/tmps/2025.11.3/en/ptfe-pcb-manufacturing.md`
- `/code/blogs/tmps/2025.11.3/en/satellite-ptfe-pcb.md`
- `/code/blogs/tmps/2025.11.3/en/teflon-circuit-board.md`
- `/code/blogs/tmps/2025.11.3/en/ultra-low-loss-pcb.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger-pcb.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger.md`
- `/code/blogs/tmps/2025.11.3/en/types-of-usb-ports.md`
- `/code/blogs/tmps/2025.11.3/en/esp32-projects.md`
- `/code/blogs/tmps/2025.11.3/en/raspberry-pi-projects.md`
- `/code/blogs/tmps/2025.11.3/en/diy-drone.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/remote-control-car-circuits.md`
- `/code/blogs/tmps/2025.11.3/en/smart-home-diy-automation.md`
- `/code/blogs/tmps/2025.11.3/en/top-8-consumer-electronics-companies-in-the-World.md`
- `/code/blogs/tmps/2025.11.3/en/kicad-vs-eagle.md`

## Existing `llm_wiki` Support Found

### PTFE / low-loss / RF material layer

- Wiki:
  - `/code/blogs/llm_wiki/wiki/processes/ptfe-processing-and-manufacturability.md`
    - `topic_id: processes-ptfe-processing-and-manufacturability`
  - `/code/blogs/llm_wiki/wiki/processes/hybrid-rf-stackup-strategy.md`
    - `topic_id: processes-hybrid-rf-stackup-strategy`
  - `/code/blogs/llm_wiki/wiki/materials/rogers-ro3000-family.md`
    - `topic_id: materials-rogers-ro3000-family`
  - `/code/blogs/llm_wiki/wiki/materials/rf-material-selector-by-application-band.md`
    - `topic_id: materials-rf-selector-by-application-band`
  - `/code/blogs/llm_wiki/wiki/materials/high-speed-material-family-selection.md`
    - `topic_id: materials-high-speed-material-family-selection`
- Facts:
  - `/code/blogs/llm_wiki/facts/materials/ptfe-rf-material-processing-posture.md`
    - `fact_id: materials-ptfe-rf-material-processing-posture`
  - `/code/blogs/llm_wiki/facts/materials/rf-material-selector-by-application.md`
    - `fact_id: materials-rf-material-selector-by-application`
  - `/code/blogs/llm_wiki/facts/materials/parameter-scope-rogers-rf-laminate-values.md`
    - `fact_id: materials-parameter-scope-rogers-rf-laminate-values`
  - `/code/blogs/llm_wiki/facts/materials/taconic-official-source-coverage-gap.md`
    - `fact_id: materials-taconic-official-source-coverage-gap`
- Source records:
  - `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-series-product-page.md`
    - `source_id: rogers-ro3000-series-product-page`
  - `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-fabrication-guidelines.md`
    - `source_id: rogers-ro3000-fabrication-guidelines`
  - `/code/blogs/llm_wiki/sources/registry/materials/rogers-rt-duroid-5870-5880-datasheet.md`
    - `source_id: rogers-rt-duroid-5870-5880-datasheet`
  - `/code/blogs/llm_wiki/sources/registry/materials/taconic-divisions-page.md`
    - `source_id: taconic-divisions-page`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-teflon-pcb-page-en.md`
    - `source_id: frontendapt-materials-teflon-pcb-page-en`

### USB-C / Type-C charger layer

- Wiki:
  - `/code/blogs/llm_wiki/wiki/processes/usb-c-charger-readiness-classification.md`
    - `topic_id: processes-usb-c-charger-readiness-classification`
  - `/code/blogs/llm_wiki/wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
    - `topic_id: processes-power-energy-pcb-pcba-review-boundaries`
- Facts:
  - `/code/blogs/llm_wiki/facts/methods/charger-pcb-pcba-manufacturing-boundary.md`
    - `fact_id: methods-charger-pcb-pcba-manufacturing-boundary`
- Source records:
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-type-c-cable-connector-spec-r2-0.md`
    - `source_id: usb-if-type-c-cable-connector-spec-r2-0`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-type-c-functional-test-spec-2024-03-03.md`
    - `source_id: usb-if-type-c-functional-test-spec-2024-03-03`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-pd-compliance-updates-page.md`
    - `source_id: usb-if-pd-compliance-updates-page`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-type-c-compliance-updates-page.md`
    - `source_id: usb-if-type-c-compliance-updates-page`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-type-c-language-guidelines-2023.md`
    - `source_id: usb-if-type-c-language-guidelines-2023`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-connector-qbs-guidelines-page.md`
    - `source_id: usb-if-connector-qbs-guidelines-page`
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-qbs-information-page.md`
    - `source_id: usb-if-qbs-information-page`

### RF validation / application-boundary layer

- Wiki:
  - `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`
    - `topic_id: testing-rf-validation-and-test-coverage`
  - `/code/blogs/llm_wiki/wiki/applications/industry-application-scenarios-and-boundaries.md`
    - `topic_id: applications-industry-application-scenarios-and-boundaries`
- Facts:
  - `/code/blogs/llm_wiki/facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`
    - `fact_id: standards-automotive-medical-aerospace-application-qualification-boundary`
  - `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
    - `fact_id: methods-controlled-impedance-tdr-verification-posture`
  - `/code/blogs/llm_wiki/facts/methods/high-speed-interface-system-context.md`
    - `fact_id: methods-high-speed-interface-system-context`
- Source records:
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-industry-drone-uav-page-en.md`
    - `source_id: frontendapt-industry-drone-uav-page-en`

### Existing prior scout covering this batch’s weaker zones

- `/code/blogs/llm_wiki/logs/p4-33-lane-g-delta-2025-11-3-and-2025-11-17.md`
  - already records that drone, smart-home, ESP32, Raspberry Pi, and remote-control drafts are usable mainly as application-taxonomy inventory only
  - already records that authoritative maker-platform and protocol sources are still missing for ESP32, Raspberry Pi, Matter, Thread, Zigbee, and smart-home feature claims
  - already records that consumer-electronics rankings and named-company comparison claims are blocked

## Claim-Family Disposition

| Claim family | Drafts | Current disposition | Notes |
| --- | --- | --- | --- |
| PTFE / Teflon / high-frequency PTFE | `high-frequency-ptfe-pcb.md`, `ptfe-circuit-board.md`, `ptfe-pcb-manufacturing.md`, `teflon-circuit-board.md` | `source_backed_fact_layer_partial` | Safe for PTFE-as-material-family framing, hybrid-stackup posture, processing discipline, and named official Rogers examples. Not safe for generic numeric tables, cost, yield, or supplier-proof claims. |
| Low-loss / ultra-low-loss PCB | `low-loss-pcb.md`, `ultra-low-loss-pcb.md` | `source_backed_fact_layer_partial` | Safe for family taxonomy and design/manufacturability framing. Draft tier ladders, exact Df thresholds, GHz cutoffs, and cost multipliers remain blocked unless tied to exact dated official sources. |
| Satellite PTFE / aerospace PTFE | `satellite-ptfe-pcb.md` | `blocked_pending_dated_capability_record` | Material/application context exists, but draft supplier claims about AS9100D systems, traceability, on-time delivery, project ownership, and end-to-end aerospace readiness are supplier-specific and not authorized from current support. |
| USB-C / Type-C charger PCB | `type-c-charger-pcb.md`, `type-c-charger.md` | `source_backed_fact_layer_partial` | Safe only for conservative connector vocabulary, compliance-program awareness, powered FCT context, board partitioning, and charger-board manufacturing framing. Exact PD/PPS behavior, wattage ladders, charger safety certifications, and device-compatibility claims remain blocked. |
| USB port taxonomy | `types-of-usb-ports.md` | `blocked_pending_official_source` | Existing support covers USB Type-C vocabulary and compliance boundaries, but not the broader USB-A/B/Mini/Micro/USB4/Thunderbolt ranking table, speed table, video claims, cable claims, or current 2025 ecosystem assertions. |
| Drone / UAV application framing | `diy-drone.md` | `completed_at_claim_family_level` | Safe as application-topic inventory plus generic drone/UAV board partition context. Flight-stack specifics, firmware ecosystem claims, EMI prescriptions, AI features, and sourcing claims need official recovery. |
| Remote-control / RC circuits | `remote-control-circuits.md`, `remote-control-car-circuits.md` | `completed_at_claim_family_level` | Safe for generic transmitter/receiver/control-loop topic clustering only. IR carrier specifics, RF bands, spread-spectrum behavior, latency, telemetry, AI features, and range/performance claims are unsupported. |
| ESP32 maker ecosystem | `esp32-projects.md` | `blocked_pending_official_source` | Current corpus does not provide authoritative Espressif support for module lineup, Matter/Thread positioning, AI capability, pre-certification, or production suitability claims. |
| Raspberry Pi ecosystem | `raspberry-pi-projects.md` | `blocked_pending_official_source` | Current corpus does not provide authoritative Raspberry Pi support for Pi 5 performance deltas, CM5 positioning, RP2040/Pico architecture claims, or popularity framing. |
| Smart-home DIY / Matter / Thread / Zigbee strategy | `smart-home-diy-automation.md` | `blocked_pending_official_source` | Current corpus lacks authoritative CSA/Thread/Raspberry Pi/Home Assistant/Espressif layer needed for interoperability, local-control, security, and ecosystem claims. |
| Consumer-electronics company ranking | `top-8-consumer-electronics-companies-in-the-World.md` | `blocked_pending_official_source` | Named-company ordering, market-leadership framing, and comparative business claims are unsupported and temporally unstable. |
| EDA comparison | `kicad-vs-eagle.md` | `blocked_pending_official_source` | Out of this lane’s main focus, but still unsupported for current 2025 feature parity, pricing, licensing, and ranking claims without official vendor sources. |

## Safe Reuse Classes

- PTFE / low-loss material-family taxonomy without promoting draft-originated numeric tables
- PTFE processing posture as a distinct manufacturing discipline
- hybrid RF stackup framing
- named exact-product Rogers / RT-duroid source-backed examples where the writing stays product-specific
- RF application framing as context only, not finished-board proof
- USB Type-C / USB-C naming discipline and connector-scope vocabulary
- USB-C charger board rewrite posture limited to connector-zone review, protection placement, control partitioning, assembly, and functional-test handoff
- drone / UAV / satellite / smart-home / maker topics as claim inventory and future source-recovery targets only

## Blocked Claim Classes

- unsupported numeric PTFE, low-loss, ultra-low-loss, RF, thermal, or electrical performance values copied from drafts
- flat material tier rankings such as “gold standard,” “best,” “only choice,” or cross-vendor superiority claims
- cost, lead-time, MOQ, yield, defect-rate, on-time-delivery, or production-scale claims
- generic supplier/manufacturer trustworthiness or “capable manufacturer” proof
- AS9100D, aerospace traceability, or mission-ready claims unless backed by dated supplier-specific records
- exact USB PD, PPS, USB4, Thunderbolt, cable, e-marker, Alt Mode, wattage, voltage, current, or charging-speed claims
- certification claims for USB-IF, UL, ETL, CE, FCC unless tied to current official program or listing evidence for the exact statement
- ESP32 module capability, AI, Matter/Thread support, pre-certification, or commercial-product readiness claims
- Raspberry Pi 5, CM5, RP2040, Pico, or popularity/performance claims
- IR `38 kHz`, RF `315 MHz`, `433 MHz`, `2.4 GHz`, `5.8 GHz`, spread-spectrum, range, latency, or anti-interference claims
- Betaflight, PX4, ArduPilot, Home Assistant, HomeKit, Google Home, Matter, Thread, Zigbee, and smart-home interoperability claims without official-source recovery
- consumer-electronics rankings, “top 8” ordering, market leadership, comparative innovation, or business-scale claims

## Official-Source Candidates Worth Recovering Next

### Highest-value next lanes

1. `USB general taxonomy and current capability lane`
   - Recover official USB-IF sources for broader USB connector taxonomy, USB4 version framing, PD 3.1 vocabulary, and dated speed/power tables.
   - Needed for `types-of-usb-ports.md`.
   - Current status: `blocked_pending_official_source`.

2. `Espressif official platform lane`
   - Recover Espressif official pages / datasheets / programming guides for `ESP32-WROOM`, `ESP32-S3`, `ESP32-C6`, `ESP32-H2`, ESP-NOW, ESP-IDF, and Espressif Matter examples.
   - Needed for `esp32-projects.md` and smart-home overlap.
   - Current status: `blocked_pending_official_source`.

3. `Raspberry Pi official platform lane`
   - Recover official Raspberry Pi pages for `Raspberry Pi 5`, `Compute Module 5`, `RP2040`, `Pico`, `Pico 2 W`, and carrier-board design guidance.
   - Needed for `raspberry-pi-projects.md` and `smart-home-diy-automation.md`.
   - Current status: `blocked_pending_official_source`.

4. `Smart-home standards and ecosystem lane`
   - Recover CSA Matter official pages, Thread Group official pages, and official platform pages for Home Assistant or other directly cited ecosystems if they must appear.
   - Needed for `smart-home-diy-automation.md`.
   - Current status: `blocked_pending_official_source`.

5. `Remote-control protocol lane`
   - Recover official/vendor primary sources for IR receiver modules, RF control modules, and protocol-family framing if remote-control posts must survive beyond generic taxonomy.
   - Needed for `remote-control-circuits.md` and `remote-control-car-circuits.md`.
   - Current status: `blocked_pending_official_source`.

### Secondary recovery lanes

1. `Drone open-source ecosystem lane`
   - Official PX4 and ArduPilot docs; Betaflight official documentation if needed.
   - Use only for firmware ecosystem description, not performance or compliance proof.

2. `Satellite / aerospace supplier-proof lane`
   - Requires dated supplier-specific capability records for claims such as AS9100D, traceability workflow, aerospace documentation, project ownership, and delivery posture.
   - Current status: `blocked_pending_dated_capability_record`.

3. `Consumer-electronics ranking lane`
   - Would require a dated methodology and authoritative market source set.
   - Low priority because ranking-style content remains high-risk and weakly reusable.

## Residual Source Gaps

- No authoritative maker-platform source layer yet for `ESP32`, `ESP32-S3`, `ESP32-C6`, `Raspberry Pi 5`, `CM5`, `RP2040`, `Pico`, or current 2025 popularity framing.
- No authoritative standards layer yet for `Matter`, `Thread`, or the draft’s smart-home interoperability and security posture.
- No general USB standards layer yet for the draft’s broader USB port evolution, USB4/Thunderbolt comparison, and cable capability tables.
- No authoritative source layer yet for remote-control protocol specifics, band usage, line-of-sight/range claims, or RC telemetry claims.
- No dated supplier-specific evidence layer for satellite/aerospace manufacturing proof claims.
- No admissible evidence for named-company ranking or ordering claims in consumer electronics.

## Recommended Next-Step Handling By Draft Group

- PTFE / low-loss group:
  - Reuse existing `llm_wiki` support now for conservative rewrite.
  - Recover missing exact-product official sources only where drafts require named material examples beyond current Rogers / AGC / Taconic coverage.
- USB-C charger group:
  - Reuse existing charger-boundary and USB-IF vocabulary support now.
  - Recover broader USB official sources before touching `types-of-usb-ports.md`.
- ESP32 / Raspberry Pi / smart-home group:
  - Do not draft as fact-backed yet.
  - Open dedicated official-source recovery lanes first.
- Drone / remote-control group:
  - Keep as topic inventory only unless official protocol and firmware sources are added.
- Consumer-electronics ranking group:
  - Keep blocked.
  - Do not promote ranking content into reusable facts or wiki.

## Lane Status

- lane_completion: `completed_at_claim_family_level`
- source_support_status: `source_backed_fact_layer_partial`
- blocked_families:
  - `blocked_pending_official_source`: USB taxonomy, ESP32, Raspberry Pi, smart-home protocols, remote-control protocol specifics, company ranking, EDA comparison
  - `blocked_pending_dated_capability_record`: satellite PTFE supplier-proof and aerospace-readiness claims

## Changed Files

- `/code/blogs/llm_wiki/logs/p4-40-2025-11-3-consumer-rf-usb-ptfe-official-source-recovery-scout.md`
