# P4-129 2026-05-02 HILPCB Blog1-13 Source-Recovery Queue Note

Date: 2026-05-02
Scope: `HILPCB Blog1-13 source_recovery_now remainder decomposition`
Status: `controller_queue_defined`

## Purpose

Convert the three `source_recovery_now` residual lanes from `P4-127` into one bounded next-batch source-recovery queue.

This note is queue design only. It does not perform source recovery, fact promotion, wiki promotion, draft rewriting, or tracker expansion outside this file.

## Read Basis

- `llm_wiki/logs/p4-127-2026-5-2-hilpcb-blog1-13-input-device-closure-controller.md`
- `llm_wiki/logs/p4-30-hilpcb-blog1-13-lane-a-keyboard-general.md`
- `llm_wiki/logs/p4-30-hilpcb-blog1-13-lane-c-mouse-peripherals.md`
- `llm_wiki/logs/p4-30-hilpcb-blog1-13-lane-d-music-midi-audio.md`
- `llm_wiki/logs/p4-42-2026-1-13-keyboard-mouse-hmi-audio-official-source-recovery-scout.md`
- `llm_wiki/logs/p4-125-2026-5-2-knowledge-base-distance-and-subagent-roadmap.md`

## Queue Contract

- Queue scope is limited to the three `source_recovery_now` lanes named in `P4-127`.
- Allowed source classes:
  - official protocol-owner documentation
  - official regulator documentation
  - official vendor documentation from the exact component, module, or platform owner
- Disallowed source classes:
  - reseller pages
  - distributor summaries unless they host the vendor's original datasheet as a mirror accepted later by main review
  - third-party blogs
  - forums
  - media coverage
  - market reports
  - user wikis
- Recovery target is bounded source inventory and claim-boundary reduction only.
- Stop before numeric performance, HILPCB capability proof, market positioning, or broad rewrite enablement.

## Ranked Next-Batch Queue

| Priority | Queue lane | Exact source scope | Primary recovery target | Stop condition |
| --- | --- | --- | --- | --- |
| 1 | keyboard firmware / hot-swap / wireless / consumer-compliance boundary | `QMK` official docs, `VIA` official docs, Bluetooth `SIG`, `FCC`, EU `RED` / `CE` entry-point regulator pages, `USB-IF` if connector or USB terminology boundary is required, and exact hot-swap socket vendor docs only if a named socket family becomes necessary | reduce unsupported keyboard compatibility and compliance wording into protocol-owner or regulator-backed boundary language | stop once source map covers firmware-compatibility vocabulary, wireless terminology, and consumer-compliance entry points; do not continue into performance, battery-life, latency, or universal design rules |
| 2 | mouse sensor / switch / wireless boundary | exact optical-sensor vendor docs, exact switch vendor docs, Bluetooth `SIG`, `FCC`, EU `RED` / `CE` entry-point regulator pages, and exact wireless-module vendor docs only if a named module appears in draft recovery scope | reduce unsupported mouse sensor, switch, and wireless wording into vendor-backed or regulator-backed boundary language | stop once source map covers sensor-family identity, switch-family identity, wireless terminology, and product-level compliance entry points; do not continue into DPI/CPI, polling rate, debounce timing, click life, battery life, or esports-performance claims |
| 3 | MIDI / USB-MIDI / BLE-MIDI compatibility boundary | `MIDI Association`, `USB-IF` or official USB class references already used by protocol owners, Bluetooth `SIG` for `BLE` terminology, and official OS-vendor class-support pages only if transport wording cannot be bounded from protocol-owner material alone | reduce unsupported MIDI interoperability wording into protocol-owner compatibility and terminology boundaries | stop once source map covers `MIDI`, `USB-MIDI`, and `BLE-MIDI` naming, transport identity, and compatibility-boundary language; do not continue into DAW support, latency, pad sensitivity, keybed performance, audio fidelity, or platform-specific workflow claims |

## Lane Decomposition

### Lane 1

Lane name:
`keyboard firmware / hot-swap / wireless / consumer-compliance boundary`

Priority:
`1`

Exact source scope:

- official `QMK` documentation
- official `VIA` documentation
- official Bluetooth `SIG` terminology and qualification-boundary pages
- official `FCC` equipment-authorization or labeling entry-point pages relevant to wireless consumer input devices
- official EU `RED` / `CE` entry-point pages relevant to wireless consumer input devices
- official `USB-IF` pages only if keyboard USB or `USB-C` wording must be bounded
- official hot-swap socket vendor documentation only for exact named socket families if the recovery pass must distinguish socket-vendor identity from generic hot-swap prose

What this lane may recover:

- bounded `QMK` and `VIA` compatibility vocabulary
- protocol-owner wording for Bluetooth and wireless-keyboard terminology
- regulator-backed entry-point wording for `FCC` and EU wireless consumer-device compliance references
- exact vendor identity for named hot-swap socket families if the draft family later requires vendor-specific distinction

What remains blocked even if this lane runs:

- hot-swap durability cycles, pad-strength, and insertion-life claims
- anti-ghosting or `NKRO` performance claims
- RGB electrical, thermal, brightness, or power-budget claims
- battery-life, range, latency, coexistence, polling, and dual-mode wireless claims
- HILPCB production capability, lead time, quality, inspection-coverage, or certification-status claims

Lane stop conditions:

- stop when the queue has enough official-source anchors to separate:
  - firmware-ecosystem identity
  - wireless terminology
  - product-level compliance entry points
  - named socket-vendor identity if needed
- stop if the next remaining claim requires numeric engineering proof, consumer performance proof, or HILPCB internal capability evidence
- stop without opening general keyboard architecture, market, or broad USB implementation recovery

### Lane 2

Lane name:
`mouse sensor / switch / wireless boundary`

Priority:
`2`

Exact source scope:

- official optical-sensor vendor product pages, datasheets, or integration notes for exact named sensor families only
- official switch-vendor documentation for exact named switch families only
- official Bluetooth `SIG` terminology and qualification-boundary pages
- official `FCC` equipment-authorization or labeling entry-point pages relevant to wireless mouse products
- official EU `RED` / `CE` entry-point pages relevant to wireless mouse products
- official wireless-module vendor documentation only if a draft-recovery pass introduces a named module family that must be identified or bounded

What this lane may recover:

- exact vendor identity and bounded family vocabulary for named mouse sensors
- exact vendor identity and bounded family vocabulary for named mouse switches
- protocol-owner wording for Bluetooth / low-power wireless terminology
- regulator-backed entry-point wording for wireless peripheral compliance references

What remains blocked even if this lane runs:

- DPI / CPI, IPS, acceleration, lift-off, surface-tracking, or tracking-accuracy claims
- polling-rate, latency, debounce, zero-latency, or click-response claims
- switch lifetime, tactile-feel, or reliability-outcome claims
- battery-life, charging speed, antenna performance, range, and coexistence claims
- HILPCB supplier capability, yield, scale, lead-time, or QA-proof claims

Lane stop conditions:

- stop when the queue has enough official-source anchors to separate:
  - sensor-family identity
  - switch-family identity
  - wireless terminology
  - product-level compliance entry points
- stop if remaining draft language depends on benchmarks, user-experience claims, or unnamed generic gaming-performance adjectives
- stop without opening peripheral battery, charger, or RF-layout numerics recovery

### Lane 3

Lane name:
`MIDI / USB-MIDI / BLE-MIDI compatibility boundary`

Priority:
`3`

Exact source scope:

- official `MIDI Association` documentation for `MIDI` and `BLE-MIDI`
- official `USB-IF` or other protocol-owner USB class materials only where needed to bound `USB-MIDI` transport wording
- official Bluetooth `SIG` terminology pages for `BLE` naming and qualification boundary
- official OS-vendor class-support pages only if protocol-owner sources do not sufficiently bound host-compatibility wording and the need is limited to class-support identity rather than workflow claims

What this lane may recover:

- protocol-owner wording for `MIDI`, `USB-MIDI`, and `BLE-MIDI` identity
- bounded compatibility language for transport-level interoperability references
- protocol-owner terminology that separates standards identity from unsupported DAW or platform promises

What remains blocked even if this lane runs:

- DAW support matrices, driver behavior, or workflow-performance claims
- latency, jitter, timing-resolution, pad-sensitivity, velocity, or aftertouch claims
- DSP, DAC, ADC, noise, `THD`, `SNR`, dynamic-range, or audio-quality claims
- battery-life, RF range, or BLE performance claims
- HILPCB capability, manufacturing readiness, or audio-product qualification claims

Lane stop conditions:

- stop when the queue has enough official-source anchors to separate:
  - transport identity
  - compatibility-boundary wording
  - `BLE` terminology
- stop if remaining claims require workstation, instrument, audio-path, OS-behavior, or application-integration proof beyond protocol identity
- stop without opening synthesizer, converter, control-surface, or audio-fidelity recovery

## Queue Outcome

This next batch should run in the following order:

1. keyboard firmware / hot-swap / wireless / consumer-compliance boundary
2. mouse sensor / switch / wireless boundary
3. MIDI / USB-MIDI / BLE-MIDI compatibility boundary

Reason for order:

- keyboard has the highest concentration of repeated unsupported compatibility and compliance wording across the draft family
- mouse is similarly recoverable, but depends more heavily on exact vendor family identity and remains more exposed to performance-claim spillover
- MIDI is the cleanest protocol-identity lane, but it unlocks narrower compatibility wording than the keyboard lane does for the current batch

## Non-Goals

- no source recovery execution
- no facts or wiki promotion
- no blog rewrite planning
- no reopening of rugged / HMI / medical / military hold families
- no reopening of HILPCB internal capability proof

## Status

- controller result: `three-lane next-batch queue defined`
- source scope posture: `official_only`
- recovery posture: `boundary reduction only`
- blocked remainder after queue design: `performance claims, numerics, and HIL capability proof remain out of scope`
