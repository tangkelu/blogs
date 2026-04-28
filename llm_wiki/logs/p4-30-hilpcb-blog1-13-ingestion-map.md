# P4-30 HILPCB Blog1-13 Input-Device Draft Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the 40 English input-device drafts under `/code/blogs/tmps/HILPCB-blog1-13/en` and defines how the batch may be consumed by `llm_wiki`.

The batch is useful as a topic-intent, outline-shape, and blocked-claim inventory. It is not a primary source for HILPCB capability, keyboard or mouse performance, MIDI/audio compatibility, wireless behavior, certification status, durability, compliance, cost, lead time, yield, or qualification proof.

## Target Drafts

Lane A, keyboard-general:

- `pcb-for-mechanical-keyboards.md`
- `mechanical-keyboard-pcb.md`
- `mechanical-keyboard-pcb-manufacturing.md`
- `keyboard-pcb-assembly.md`
- `custom-keyboard-circuit-board.md`
- `custom-pcb-for-keyboards.md`
- `key-switch-pcb-for-keyboards.md`
- `rgb-keyboard-pcb.md`
- `rgb-backlit-keyboard-pcb.md`
- `wireless-keyboard-pcb.md`
- `flexible-pcb-for-keyboards.md`
- `multi-layer-pcb-for-keyboards.md`
- `high-density-pcb-for-keyboards.md`

Lane B, industrial / rugged / HMI keyboard:

- `industrial-keyboard-pcb.md`
- `heavy-duty-keyboard-pcb.md`
- `rugged-keyboard-pcb-for-industrial-use.md`
- `ip67-keyboard-pcb-for-harsh-environments.md`
- `industrial-panel-mount-keyboard-pcb.md`
- `custom-industrial-keyboard-design.md`
- `automation-keyboard-pcb.md`
- `hmi-control-panel-pcb.md`
- `medical-keyboard-pcb.md`
- `military-grade-keyboard-pcb.md`

Lane C, mouse / peripherals:

- `gaming-mouse-pcb.md`
- `gaming-mouse-pcb-assembly.md`
- `pcb-for-wireless-mouse.md`
- `pcb-for-optical-mouse.md`
- `mouse-sensor-pcb.md`
- `mouse-button-pcb-design.md`
- `flexible-pcb-for-mouse-design.md`

Lane D, music / MIDI / audio:

- `midi-controller-pcb.md`
- `midi-keyboard-pcb.md`
- `midi-keypad-pcb.md`
- `music-synthesizer-pcb.md`
- `electronic-music-keyboard-design.md`
- `electronic-piano-pcb.md`
- `soundboard-keyboard-pcb.md`
- `music-production-keyboard-pcb.md`
- `digital-audio-workstation-keyboard-pcb.md`
- `music-equipment-control-panel-pcb.md`

## Lane Logs

- `logs/p4-30-hilpcb-blog1-13-lane-a-keyboard-general.md`
- `logs/p4-30-hilpcb-blog1-13-lane-b-industrial-rugged-hmi.md`
- `logs/p4-30-hilpcb-blog1-13-lane-c-mouse-peripherals.md`
- `logs/p4-30-hilpcb-blog1-13-lane-d-music-midi-audio.md`

## Baseline Finding

Current `llm_wiki` has adjacent support for this batch through:

- generic PCBA mixed SMT / THT assembly, NPI, FAI/FQI, inspection, ICT, and FCT framing
- flex and rigid-flex stackup / bend-governance posture
- HDI, microvia, multilayer, controlled-impedance, and advanced stackup vocabulary
- USB Type-C / USB-C connector and compliance-boundary vocabulary
- industrial-control, robotics, medical, hi-rel, traceability, and conformance-governance metadata
- conformal-coating and protection-workflow boundaries

Current `llm_wiki` does not yet have direct authoritative support for most product-specific claims in this batch:

- keyboard matrix, hot-swap, QMK, VIA, RGB, or wireless keyboard claims
- mouse sensor, switch, debounce, polling, DPI/CPI, latency, battery, RF-range, or gaming-performance claims
- MIDI, USB-MIDI, BLE-MIDI, DAW compatibility, velocity, aftertouch, audio, DSP, DAC, SNR, THD, or polyphony claims
- IP67/IP68/IP69K, MIL, medical, FCC, CE, Bluetooth, RED, IEC 60601, IEC 60529, or product qualification claims
- HILPCB-specific capability, durability, yield, cost, lead-time, MOQ, stock, or production-scale claims

Therefore this pass absorbs the batch at `claim-family disposition` level only.

## Disposition Contract

Use these dispositions for the batch:

- `process_support_only`: generic PCB / PCBA / inspection / flex / HDI / USB-C / industrial-control vocabulary can be recovered only through existing source-backed `llm_wiki` cards.
- `topic_inventory_only`: draft sections and reader intents are useful for future rewrite prompts, evidence-pack planning, and query clustering.
- `needs_official_source`: protocol, compliance, certification, performance, electrical, RF, audio, firmware, software, or product-qualification claims require official standards, vendor, regulator, or dated capability records.
- `needs_dated_capability_record`: HILPCB capability, commercial, quality, volume, lead-time, yield, or test-coverage claims require a scoped and dated internal capability record before reuse.
- `draft_only_blocked`: numeric tables, design rules, tolerances, cycle counts, battery life, RF range, latency, DPI/CPI, polling, audio-performance values, lead-time, cost, and durability claims stay out of reusable facts.

## Per-Lane Coverage Table

| Lane | Current status | Safe reuse | Blocked / rejected content |
| --- | --- | --- | --- |
| Keyboard-general | `partial_process_support_only` | Keyboard topic clustering; layout, matrix, RGB, flex, HDI, multilayer, assembly, and USB-C section intent; generic SMT / inspection / flex / HDI / surface-finish / USB-C posture from existing cards | Hot-swap durability, QMK/VIA compatibility, RGB power/current/thermal, wireless performance, Bluetooth, RF range, latency, battery life, certification, cost, lead-time, yield, and HIL capability claims |
| Industrial / rugged / HMI | `workflow_context_only` | Industrial-control / HMI / panel / rugged-context labels; DFM/DFT/DFA, NPI, FAI, inspection, traceability, coating, sealing, gasket, and test-vs-reliability vocabulary | IP-rating proof, IEC 60529, MIL-STD-810/461, IEC 60601, ISO 13485 status, AS9100, ITAR, ATEX/IECEx, protocol support, environmental performance, durability, MTBF, and supplier qualification |
| Mouse / peripherals | `boundary_only_with_major_gaps` | Compact multi-board, flex/rigid-flex, SMT/inspection, RF-validation planning, USB-C connector context, and generic test-gate vocabulary | Optical-sensor capability, DPI/CPI, polling rate, latency, switch lifetime, debounce timing, Bluetooth / 2.4 GHz behavior, battery life, charging performance, RF range, FCC/CE, Bluetooth qualification, and gaming-performance claims |
| Music / MIDI / audio | `partial_process_support_only` | MIDI/audio-control topic clustering; pads, faders, encoders, displays, multi-board partitioning, mixed SMT/THT, USB-C, HDI, and rigid-flex vocabulary | MIDI/USB-MIDI/BLE-MIDI compatibility, DAW support, velocity/aftertouch, latency/jitter, DAC/ADC/audio performance, THD/SNR, DSP/CPU/memory/polyphony, wireless behavior, component recommendations, and compliance claims |

## Claim-Family Rules

### Can Be Consumed Now

- topic clusters and article-intent signals for keyboards, industrial keyboards, HMI panels, mice, MIDI controllers, synthesizers, electronic pianos, and music-control panels
- outline shapes that separate product role, PCB architecture, assembly flow, test planning, interconnects, enclosure / panel integration, and compliance gaps
- generic manufacturing vocabulary when mapped back to existing `llm_wiki` facts rather than to the drafts
- blocked-claim inventories for future source-gap planning

### Needs Official Source Or Dated Capability Record

- any numeric value
- any HILPCB capability, lead-time, cost, MOQ, production-scale, yield, inspection-coverage, or commercial promise
- keyboard-specific firmware / software compatibility such as QMK or VIA
- mouse sensor, polling, latency, RF, button, switch, debounce, charging, or battery claims
- MIDI, USB-MIDI, BLE-MIDI, DAW, audio-interface, synthesizer, DSP, memory, velocity, aftertouch, fader, encoder, or pad-performance claims
- Bluetooth, FCC, CE, RED, USB-IF, RoHS, REACH, IP rating, IEC 60529, IEC 60601, MIL, AS9100, ISO 13485, ITAR, ATEX, IECEx, or other compliance / certification language
- durability, lifecycle, bend-life, switch-cycle, insertion-cycle, environmental, washdown, antimicrobial, shock, vibration, salt-fog, humidity, reliability, or MTBF claims

### Reject From Draft-To-Data Promotion

- universal design rules presented without a standard or vendor source
- consumer-performance promises
- supplier capability statements without bounded source and date
- protocol-interoperability claims without official source support
- exact process windows, tolerances, geometry tables, current budgets, power budgets, acoustic / audio metrics, or RF metrics copied from draft prose

## Prompt-Consumption Gate

Before rewriting or generating from this batch:

1. Pull process support from existing PCBA, inspection, NPI, FAI/FQI, HDI, flex, rigid-flex, USB-C, industrial-control, medical, and hi-rel boundary cards.
2. Use this ingestion map and the four lane logs to remove unsupported product-specific and numeric claims before drafting.
3. Treat every draft-originated claim as unverified unless it already resolves to an existing source-backed fact card.
4. If the target article needs protocol, certification, compliance, product performance, HIL capability, cost, lead time, or durability statements, stop and require a separate source lane.

## Candidate Future Source Needs

- official QMK and VIA documentation if keyboard firmware compatibility needs to be recovered
- official Bluetooth SIG, FCC, EU RED / CE, and USB-IF source layers for wireless and USB claims
- official IEC 60529, IEC 60601, and relevant MIL / industrial-protocol source layers if rugged, medical, or military keyboard articles need more than context labels
- official mouse-sensor, switch, hot-swap-socket, LED-driver, fader, encoder, MIDI, and audio-component vendor sources if product-performance claims are needed
- dated HILPCB capability records for any shop-specific capability, test, inspection, quality, commercial, or regulated-sector claim

## Completion Status

This batch is absorbed at claim-family disposition level.

No keyboard, mouse, MIDI, audio, wireless, rugged, medical, military, or HIL capability fact was created from temporary draft prose. The only reusable output is the conservative consumption boundary captured here, in the lane logs, and in `methods-hilpcb-blog1-13-input-device-draft-consumption-boundary`.
