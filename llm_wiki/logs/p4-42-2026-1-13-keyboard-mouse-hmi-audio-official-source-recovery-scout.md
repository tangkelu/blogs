Date: 2026-04-28
Lane: `P4-42 official-source recovery scout`
Input: `/code/blogs/tmps/2026.1.13/en`
Output: `/code/blogs/llm_wiki/logs/p4-42-2026-1-13-keyboard-mouse-hmi-audio-official-source-recovery-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `source_backed_fact_layer_partial`

# Purpose

This scout log inventories the `2026.1.13/en` keyboard, mouse, HMI, MIDI, and audio drafts as claim inventory only, checks current `llm_wiki` support for the relevant claim boundaries, and records which claim families can be reused safely versus which remain blocked pending official sources or dated capability records.

This lane does not absorb the batch into reusable facts. It preserves a deletion-safe map for future source recovery.

# Input File Inventory

Total drafts inspected: `40`

Keyboard general / enthusiast:

- `custom-keyboard-circuit-board.md`
- `custom-pcb-for-keyboards.md`
- `keyboard-pcb-assembly.md`
- `key-switch-pcb-for-keyboards.md`
- `mechanical-keyboard-pcb.md`
- `mechanical-keyboard-pcb-manufacturing.md`
- `multi-layer-pcb-for-keyboards.md`
- `pcb-for-mechanical-keyboards.md`
- `rgb-backlit-keyboard-pcb.md`
- `rgb-keyboard-pcb.md`
- `wireless-keyboard-pcb.md`

Industrial / rugged / HMI / special-environment keyboards:

- `automation-keyboard-pcb.md`
- `custom-industrial-keyboard-design.md`
- `heavy-duty-keyboard-pcb.md`
- `high-density-pcb-for-keyboards.md`
- `hmi-control-panel-pcb.md`
- `industrial-keyboard-pcb.md`
- `industrial-panel-mount-keyboard-pcb.md`
- `ip67-keyboard-pcb-for-harsh-environments.md`
- `medical-keyboard-pcb.md`
- `military-grade-keyboard-pcb.md`
- `rugged-keyboard-pcb-for-industrial-use.md`

Mouse / peripheral:

- `flexible-pcb-for-mouse-design.md`
- `gaming-mouse-pcb.md`
- `gaming-mouse-pcb-assembly.md`
- `mouse-button-pcb-design.md`
- `mouse-sensor-pcb.md`
- `pcb-for-optical-mouse.md`
- `pcb-for-wireless-mouse.md`

Flex / architecture crossover:

- `flexible-pcb-for-keyboards.md`

Music / MIDI / audio / control-panel:

- `digital-audio-workstation-keyboard-pcb.md`
- `electronic-music-keyboard-design.md`
- `electronic-piano-pcb.md`
- `midi-controller-pcb.md`
- `midi-keyboard-pcb.md`
- `midi-keypad-pcb.md`
- `music-equipment-control-panel-pcb.md`
- `music-production-keyboard-pcb.md`
- `music-synthesizer-pcb.md`
- `soundboard-keyboard-pcb.md`

# Existing `llm_wiki` Support Checked

## Primary existing boundary layer

- `methods-hilpcb-blog1-13-input-device-draft-consumption-boundary`
  Path: `/code/blogs/llm_wiki/facts/methods/hilpcb-blog1-13-input-device-draft-consumption-boundary.md`
  Status: `source_backed_fact_layer_partial`
  Use: canonical batch-level rule that input-device drafts are topic inventory, not product-performance or capability proof.

- `p4-30-hilpcb-blog1-13-ingestion-map`
  Path: `/code/blogs/llm_wiki/logs/p4-30-hilpcb-blog1-13-ingestion-map.md`
  Status: `completed_at_claim_family_level`
  Use: prior lane map covering the same 40-draft family under a different temporary directory lineage.

## Flex / rigid-flex / HDI support

- `materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries`
  Path: `/code/blogs/llm_wiki/wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
  Status: `source_backed_fact_layer_partial`
  Use: keeps `PI`, `LCP`, `flex PCB`, and `rigid-flex` in the correct buckets.

- `standards-ipc-2223e-flex-rigid-flex-design-metadata`
  Path: `/code/blogs/llm_wiki/facts/standards/ipc-2223e-flex-rigid-flex-design-metadata.md`
  Status: `source_backed_fact_layer_partial`
  Use: metadata-only standards anchor for flex and rigid-flex design language.

- `methods-parameter-scope-public-capability-construction-windows`
  Path: `/code/blogs/llm_wiki/facts/methods/parameter-scope-public-capability-construction-windows.md`
  Status: `blocked_pending_dated_capability_record` for generalized supplier claims; usable only as page-scoped public-claim context.

- `standards-ecss-via-hdi-microvia-definitions`
  Path: `/code/blogs/llm_wiki/facts/standards/ecss-via-hdi-microvia-definitions.md`
  Status: `source_backed_fact_layer_partial`
  Use: official definition layer for `HDI`, blind vias, buried vias, and microvias.

- `standards-ipc-hdi-electrical-test-and-coating-metadata`
  Path: `/code/blogs/llm_wiki/facts/standards/ipc-hdi-electrical-test-and-coating-metadata.md`
  Status: `source_backed_fact_layer_partial`
  Use: metadata-only HDI and unpopulated-board test anchor.

## PCBA assembly / inspection / test support

- `testing-pcba-quality-gates-and-test-strategy`
  Path: `/code/blogs/llm_wiki/wiki/testing/pcba-quality-gates-and-test-strategy.md`
  Status: `source_backed_fact_layer_partial`
  Use: layered inspection, ICT, flying probe, FCT, FAI/FQI, and traceability framing.

- `methods-hidden-joint-xray-inspection-boundary`
  Path: `/code/blogs/llm_wiki/facts/methods/hidden-joint-xray-inspection-boundary.md`
  Status: `source_backed_fact_layer_partial`
  Use: hidden-joint coverage framing for dense assemblies.

- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  Path: `/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  Status: `source_backed_fact_layer_partial`
  Use: separates bare-board electrical test, assembly inspection, and higher-level validation.

- Source records checked:
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-ict-test-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-fct-test-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-flying-probe-testing-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-testing-quality-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-npi-assembly-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-smt-assembly-product-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-through-hole-assembly-product-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-turnkey-assembly-product-page-en.md`

## Industrial / medical / military boundary support

- `standards-high-reliability-program-and-outgassing-metadata`
  Path: `/code/blogs/llm_wiki/facts/standards/high-reliability-program-and-outgassing-metadata.md`
  Status: `source_backed_fact_layer_partial`
  Use: guarded aerospace, medical, military, and hi-rel program vocabulary only.

- `standards-ipc-6012-addendum-program-metadata`
  Path: `/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md`
  Status: `source_backed_fact_layer_partial`
  Use: procurement-triggered medical and space/military addendum framing for rigid boards.

- `methods-tht-pressfit-terminal-route-boundary`
  Path: `/code/blogs/llm_wiki/facts/methods/tht-pressfit-terminal-route-boundary.md`
  Status: `source_backed_fact_layer_partial`
  Use: electromechanical / control-module / medical-adjacent route framing without compliance proof.

- `processes-medical-imaging-wearable-empty-image-rewrite-gate`
  Path: `/code/blogs/llm_wiki/wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
  Status: `completed_at_claim_family_level`
  Use: blocks unsupported medical-device inflation.

- Source records checked:
  - `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-industry-medical-page-en.md`
  - `/code/blogs/llm_wiki/sources/registry/standards/iec-60601-1-medical-electrical-equipment-page.md`
  - `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012em-medical-addendum-page.md`
  - `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-space-military-addendum-page.md`
  - `/code/blogs/llm_wiki/sources/registry/standards/mil-prf-31032-general-spec-page.md`
  - `/code/blogs/llm_wiki/sources/registry/standards/ipc-validation-services-qml-j-std-001s-space-military-addendum-page.md`

## Interface / certification boundary support

- `standards-interface-wireless-and-positioning-product-level-boundary`
  Path: `/code/blogs/llm_wiki/facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
  Status: `source_backed_fact_layer_partial`
  Use: blocks product-level wireless claims without protocol-owner and certification evidence.

- Source records checked:
  - `/code/blogs/llm_wiki/sources/registry/standards/usb-if-type-c-functional-test-spec-2024-03-03.md`

# High-Risk Draft Claim Families Observed

The draft set repeatedly asks for facts in these classes:

- keyboard matrix, anti-ghosting, NKRO, hot-swap, QMK, VIA, RGB behavior, and wireless keyboard behavior
- optical mouse sensor performance, debounce timing, switch lifetime, DPI/CPI, polling rate, latency, RF behavior, charging, and battery life
- MIDI, USB-MIDI, BLE-MIDI, DAW compatibility, velocity sensing, aftertouch, fader precision, encoder precision, DSP, DAC/ADC, THD, SNR, dynamic range, and polyphony
- flex, rigid-flex, bend-radius, LCP/PI material choices, and HDI/microvia architecture for compact peripherals
- HMI display interfaces, touchscreen buses, industrial protocols, e-stop wording, and safety-system framing
- IP67 / washdown / gasket / sealing / harsh-environment / lifecycle / shock / vibration durability claims
- medical, military, IEC 60601, ISO 13485, MIL-STD, AS9100, ITAR, FCC, CE, RED, Bluetooth, USB-IF, RoHS, and REACH claims
- HILPCB-specific capability, inspection coverage, quality rate, lead time, MOQ, cost, volume, and yield statements

# Per-Claim-Family Disposition

## 1. Keyboard general

Drafts:
`pcb-for-mechanical-keyboards.md`, `mechanical-keyboard-pcb.md`, `mechanical-keyboard-pcb-manufacturing.md`, `keyboard-pcb-assembly.md`, `custom-keyboard-circuit-board.md`, `custom-pcb-for-keyboards.md`, `key-switch-pcb-for-keyboards.md`, `rgb-keyboard-pcb.md`, `rgb-backlit-keyboard-pcb.md`, `wireless-keyboard-pcb.md`

Status: `completed_at_claim_family_level`

Safe reuse classes:

- topic inventory and outline shape
- generic PCB / PCBA assembly flow
- generic inspection-stack language
- generic USB-C connector wording discipline
- generic HDI / multilayer / rigid-flex framing where already source-backed as architecture vocabulary only

Blocked claim classes:

- `blocked_pending_official_source` for QMK, VIA, hot-swap socket behavior, anti-ghosting/NKRO implementation, RGB electrical behavior, wireless protocol behavior, battery life, latency, range, firmware support, and consumer-performance claims
- `blocked_pending_dated_capability_record` for HILPCB manufacturing capability, production scale, test coverage, quality, lead time, MOQ, and commercial claims

Disposition:

- Treat as `topic_inventory_only` plus `process_support_only`
- Do not promote switch-footprint dimensions, RGB current budgets, matrix rules, firmware compatibility, or wireless claims from draft prose

## 2. Industrial / rugged / HMI keyboard

Drafts:
`industrial-keyboard-pcb.md`, `heavy-duty-keyboard-pcb.md`, `rugged-keyboard-pcb-for-industrial-use.md`, `ip67-keyboard-pcb-for-harsh-environments.md`, `industrial-panel-mount-keyboard-pcb.md`, `custom-industrial-keyboard-design.md`, `automation-keyboard-pcb.md`, `medical-keyboard-pcb.md`, `military-grade-keyboard-pcb.md`, `hmi-control-panel-pcb.md`

Status: `completed_at_claim_family_level`

Safe reuse classes:

- industrial-control context labels
- panel / enclosure / control-module topic clustering
- generic DFM / DFT / NPI / FAI / traceability language
- generic gasket / sealing / protection discussion only as a design or validation planning topic, not as a rating claim
- hi-rel and medical wording only as guarded program-metadata vocabulary

Blocked claim classes:

- `blocked_pending_official_source` for IEC 60529 IP ratings, IEC 60601 applicability, military qualification, medical-device compliance, industrial-protocol conformance, environmental test results, and safety-circuit conclusions
- `blocked_pending_dated_capability_record` for supplier-specific ruggedization, environmental validation, regulated-program readiness, panel-mount tolerancing capability, lifecycle validation, and quality-system scope claims

Disposition:

- `topic_inventory_only` with `workflow_context_only`
- Strongest existing support is boundary language explaining what cannot be claimed

## 3. Mouse / peripheral

Drafts:
`gaming-mouse-pcb.md`, `gaming-mouse-pcb-assembly.md`, `pcb-for-wireless-mouse.md`, `pcb-for-optical-mouse.md`, `mouse-sensor-pcb.md`, `mouse-button-pcb-design.md`, `flexible-pcb-for-mouse-design.md`

Status: `completed_at_claim_family_level`

Safe reuse classes:

- compact multi-board architecture discussion
- generic flex and rigid-flex routing posture
- generic inspection and test planning language
- generic RF-validation planning boundaries

Blocked claim classes:

- `blocked_pending_official_source` for optical sensor performance, DPI/CPI, tracking, polling rate, latency, debounce timing, switch-cycle claims, Bluetooth / 2.4 GHz behavior, antenna claims, charging, battery life, and esports-grade performance
- `blocked_pending_dated_capability_record` for HILPCB capability, production quality, inspection coverage, and mouse-specific assembly assertions

Disposition:

- `boundary_only_with_major_gaps`
- Mouse-family drafts should not be mined for numeric or product-performance facts

## 4. Music / MIDI / audio / control-panel

Drafts:
`midi-controller-pcb.md`, `midi-keyboard-pcb.md`, `midi-keypad-pcb.md`, `music-synthesizer-pcb.md`, `electronic-music-keyboard-design.md`, `electronic-piano-pcb.md`, `soundboard-keyboard-pcb.md`, `music-production-keyboard-pcb.md`, `digital-audio-workstation-keyboard-pcb.md`, `music-equipment-control-panel-pcb.md`

Status: `completed_at_claim_family_level`

Safe reuse classes:

- multi-board partitioning topic intent
- mixed SMT/THT assembly framing
- generic UI/control-panel clustering
- generic HDI / interconnect / display-integration vocabulary at architecture level only

Blocked claim classes:

- `blocked_pending_official_source` for MIDI / USB-MIDI / BLE-MIDI compatibility, DAW protocol compatibility, velocity / aftertouch, pad sensitivity, fader or encoder performance, DAC / ADC, THD, SNR, dynamic range, DSP performance, memory, storage, and polyphony claims
- `blocked_pending_dated_capability_record` for HILPCB audio-grade manufacturing, control-panel precision, rework capability, and production-readiness claims

Disposition:

- `topic_inventory_only` with `partial_process_support_only`
- Existing `llm_wiki` support is almost entirely process and boundary layer, not instrument-performance layer

## 5. Flex / rigid-flex / HDI crossover

Drafts:
`flexible-pcb-for-keyboards.md`, `flexible-pcb-for-mouse-design.md`, `high-density-pcb-for-keyboards.md`, plus flex/HDI sections inside multiple keyboard, HMI, and music drafts

Status: `source_backed_fact_layer_partial`

Safe reuse classes:

- flex / rigid-flex / HDI definitions and family vocabulary
- architecture framing that separates material class from board form factor
- page-scoped public-claim context for rigid-flex and HDI construction windows, with qualifiers preserved

Blocked claim classes:

- `blocked_pending_official_source` for bend-life, exact bend-radius tables, copper / PI / LCP / coverlay parameter promotion, microvia geometry rules, impedance claims, and finished-product reliability conclusions
- `blocked_pending_dated_capability_record` for generalized supplier capability extrapolation from public HIL/APT pages

Disposition:

- Reuse only as `family vocabulary with strict non-generalization`

## 6. PCBA assembly / test

Drafts:
assembly and test sections across `keyboard-pcb-assembly.md`, `gaming-mouse-pcb-assembly.md`, `midi-controller-pcb.md`, `digital-audio-workstation-keyboard-pcb.md`, `music-equipment-control-panel-pcb.md`, and related drafts

Status: `source_backed_fact_layer_partial`

Safe reuse classes:

- layered inspection stack
- ICT / FCT / flying-probe / FAI-FQI separation
- NPI, traceability, and release-gate vocabulary
- hidden-joint inspection framing for dense packages

Blocked claim classes:

- `blocked_pending_official_source` for exact defect-coverage claims, test-program depth, impedance / SI / audio validation outcomes, environmental validation, and assembly reliability conclusions
- `blocked_pending_dated_capability_record` for current HILPCB inspection coverage, fixture lead time, test development lead time, and customer-facing guarantees

Disposition:

- Generic process wording is reusable; product-specific performance proof is not

## 7. Medical / military / rugged / compliance overlay

Drafts:
`medical-keyboard-pcb.md`, `military-grade-keyboard-pcb.md`, `ip67-keyboard-pcb-for-harsh-environments.md`, `rugged-keyboard-pcb-for-industrial-use.md`, and compliance language scattered across wireless / HMI / music drafts

Status: `completed_at_claim_family_level`

Safe reuse classes:

- program-metadata vocabulary such as `medical applications addendum`, `space/military addendum`, `quality-system context`, and guarded hi-rel procurement framing

Blocked claim classes:

- `blocked_pending_official_source` for actual certification, qualification, approval, product compliance, EMC compliance, device safety, ingress rating, or legal/export-control conclusions
- `blocked_pending_dated_capability_record` for supplier certification status, audited scope, or active qualified-program participation

Disposition:

- Use only as `guardrail and governance vocabulary`

# Safe Reuse Classes

These classes are safe to carry forward from this scout:

- file and topic inventory
- heading and outline shape
- query clustering across keyboard, mouse, HMI, flex, HDI, MIDI, audio, and control-panel families
- generic PCB / PCBA assembly, inspection, NPI, and traceability wording already backed by existing `llm_wiki` records
- generic flex / rigid-flex / HDI vocabulary already backed by standards metadata or class-level source records
- guarded industrial, medical, and military program vocabulary that stays explicitly below qualification or compliance claims

# Blocked Claim Classes

These classes remain blocked across the batch:

- draft-originated numbers of any kind
- process limits, material parameters, bend-radius tables, impedance claims, audio metrics, RF metrics, and thermal claims
- supplier capability, certification, qualification, audit, readiness, quality, yield, or production-scale claims
- prices, MOQs, lead times, stock, throughput, and commercial commitments
- IP ratings, MIL-STD, IEC 60601, FCC, CE, RED, Bluetooth qualification, USB-IF certification, RoHS, REACH, and legal/export claims
- protocol compatibility and product interoperability claims
- product-performance claims for keyboards, mice, MIDI, audio, or HMI systems

# Official-Source Gaps

No current `llm_wiki` support was found that is sufficient to source-back the following claim classes for this batch:

- keyboard firmware and ecosystem claims:
  QMK, VIA, hot-swap socket vendor behavior, NKRO / anti-ghosting implementation boundaries
- mouse hardware and wireless claims:
  optical sensor vendors, switch vendors, debounce-performance references, 2.4 GHz / Bluetooth compliance and behavior
- MIDI / audio protocol and performance claims:
  MIDI Association, USB-MIDI class references, BLE-MIDI references, DAW/control-surface protocol owners, audio converter and analog front-end vendors
- rugged / ingress / medical / military product claims:
  IEC 60529 ingress-rating method and scope, IEC 60601 device-safety scope, MIL environmental / EMC framework boundaries relevant to input devices
- HMI display and industrial bus claims:
  display-interface owners, touch-controller vendors, protocol-owner references for Profinet, EtherNet/IP, Modbus, and safety-interface boundaries
- dated supplier capability evidence:
  any HILPCB-specific input-device, ruggedization, test, or regulated-program capability record

# Recommended Next Recovery Lanes

## Lane 1: Keyboard ecosystem official sources

Priority: high
Status if opened: `source_recovery_in_progress`

Targets:

- QMK official docs
- VIA official docs
- Kailh / Gateron / Cherry / hot-swap-socket vendor sources where needed
- USB-IF / Bluetooth SIG / FCC / RED sources for keyboard connectivity claims

Purpose:

- recover only official compatibility and scope boundaries
- block unsourced firmware, wireless, and consumer-performance inflation

## Lane 2: Mouse sensor / switch / wireless official sources

Priority: high
Status if opened: `source_recovery_in_progress`

Targets:

- PixArt or other official sensor vendor pages / datasheets
- Omron or optical-switch vendor sources
- Bluetooth SIG and wireless compliance sources
- protocol-owner or regulator sources for product-level wireless claims

Purpose:

- separate true vendor-backed sensor/switch facts from draft-originated gaming-performance marketing

## Lane 3: MIDI / audio protocol-owner source recovery

Priority: high
Status if opened: `source_recovery_in_progress`

Targets:

- MIDI Association official resources
- USB class or protocol-owner references relevant to USB-MIDI
- official BLE-MIDI references
- protocol-owner references for DAW / control-surface compatibility if needed

Purpose:

- recover only protocol identity and interoperability boundaries first
- leave DAC/ADC/audio-performance numerics blocked until component-vendor evidence exists

## Lane 4: HMI / industrial protocol boundary recovery

Priority: medium
Status if opened: `source_recovery_in_progress`

Targets:

- official industrial protocol-owner pages for Profinet, EtherNet/IP, Modbus
- official display-interface or touch-interface references where drafts invoke LVDS, MIPI DSI, and touchscreen buses

Purpose:

- recover high-level protocol identity and boundary vocabulary
- prevent unsupported control-safety and system-integration claims

## Lane 5: Rugged / ingress / medical / military boundary recovery

Priority: medium
Status if opened: `source_recovery_in_progress`

Targets:

- IEC 60529 metadata or official ingress-rating references
- official IEC 60601 metadata already partly present, extended only if device-scope clarification is needed
- official military / EMC metadata where drafts invoke MIL-STD language

Purpose:

- keep application-context writing from drifting into qualification claims

## Lane 6: HILPCB dated capability record recovery

Priority: high if business wants supplier-specific claims
Status if opened: `blocked_pending_dated_capability_record`

Targets:

- dated internal capability records for input-device assembly, ruggedization, inspection coverage, regulated-program scope, and commercial/service commitments

Purpose:

- recover only scope-bounded supplier claims that public sources cannot prove

# Lane Conclusion

This batch already has a conservative `llm_wiki` boundary layer for generic process, flex / rigid-flex / HDI vocabulary, PCBA test-stack framing, and guarded medical / military metadata. It does not have enough current official-source support for keyboard-, mouse-, MIDI-, audio-, HMI-, rugged-, medical-, or military-specific product claims.

The correct lane result is:

- batch status: `completed_at_claim_family_level`
- evidence posture: `source_backed_fact_layer_partial`
- blocked families: mostly `blocked_pending_official_source`
- supplier-specific blocked families: `blocked_pending_dated_capability_record`

No tracker updates were made. No reusable fact cards were created.
