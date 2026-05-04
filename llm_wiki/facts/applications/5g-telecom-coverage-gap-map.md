---
fact_id: "applications-5g-telecom-coverage-gap-map"
title: "5G Telecom application coverage gap map: which board families and execution layers have wiki-level routing and which remain overview-only"
topic: "5G telecom PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-181 initial build; sourced from wiki/applications/5g-telecom-pcb-execution-boundary-map.md (active as of P4-174), related 5G/RF/telecom fact cards in facts/methods/ and facts/standards/"
source_ids:
  - "3gpp-38-series"
  - "3gpp-ts-38104-archive"
  - "frontendapt-industry-communication-equipment-page-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
tags: ["5g", "telecom", "mmwave", "base-station", "rf-front-end", "antenna", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-181 initial build, the 5G telecom application family has a dedicated wiki boundary page (`wiki/applications/5g-telecom-pcb-execution-boundary-map.md`) and that page is now `active`. This fact card maps what the current internal and public source layer supports, which execution layers are addressable, and which standards/performance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

All entries below are supported by a combination of the Tier-2 internal source (`frontendapt-industry-communication-equipment-page-en`) and public 3GPP identity-level sources. They support PCB/PCBA board-class vocabulary and execution context. They do NOT prove RF-system performance, standards compliance, or operator qualification.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **5G Base Station** | Macro/distributed telecom equipment with mixed RF, digital, power, and control hardware | Partition review (RF/digital/power/control zones), hybrid stackup, material selection review, connector and backplane transitions, validation-structure planning |
| **5G NSA Hardware** | NSA deployment label as interface-density and synchronization context | Interface density review, reference-plane continuity, revision-control framing, NPI bring-up vocabulary |
| **5G Pico Cell** | Compact telecom node with tight area, enclosure, connector, and thermal constraints | Small-form-factor stackup tradeoffs, RF/digital coexistence in compact layout, shielded-structure planning, fine-pitch assembly review |
| **Antenna System Board** | Feed networks, grounded structures, RF interfaces for active/passive antenna systems | Feed-network routing, return-path discipline, hybrid stackup, drilled-transition control, connector footprint review, coupon-based validation |
| **mmWave Front-End** | High-sensitivity RF hardware at millimeter-wave frequencies | Laminate selection review, drilled-transition discipline, shield/cavity/ground-continuity coordination, fab-note discipline, sample-based validation access |
| **Turnkey Telecom Build** | PCB-to-PCBA managed flow for telecom hardware | Build-package completeness, revision control, stackup review, BOM/AVL/lifecycle checks, SMT/THT integration, inspection gates, traceability |
| **NPI / EVT / DVT / PVT Ramp** | Staged prototype-to-volume gating for telecom programs | Gate-separated ramp stages, early validation structure reservation, bring-up discipline, change-control vocabulary |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-5g-telecom-empty-image-rewrite-boundary` | General 5G rewrite boundary: what is safe and what is blocked |
| `methods-5g-rf-system-context-vs-pcb-execution-boundary` | RF system context vs PCB execution boundary translation rules |
| `methods-beamforming-mmwave-conservative-generation-gate` | mmWave and beamforming conservative generation gate |
| `standards-5g-nr-identity-and-revision-boundary` | 3GPP 5G NR identity and revision claims boundary |
| `methods-rf-isolator-component-class-vs-pcb-execution-boundary` | RF isolator component class vs PCB execution boundary |
| `methods-pcba-evt-dvt-pvt-gated-ramp-boundary` | EVT/DVT/PVT gated ramp boundary |
| `methods-rf-validation-capability` | RF validation (TDR/VNA/coupon) capability vocabulary |
| `methods-hybrid-rf-stackup-capability` | Hybrid RF stackup capability language |
| `methods-backdrill-control-capability` | Backdrill control capability vocabulary |
| `methods-cavity-machining-capability` | Cavity machining capability vocabulary |

### Standards Context Supported (Public Sources)

| Standard/Technology | What It Supports |
|---|---|
| `3GPP 38-series (5G NR)` | Standard-family identity; 5G system-context framing vocabulary; NOT latest-version wording, protocol compliance claims |
| `FR1 (Sub-6 GHz)` | Frequency range context; RF front-end board pressure vocabulary; NOT exact frequency values, coverage, radio performance numerics |
| `FR2 (mmWave)` | mmWave sensitivity context; high-frequency execution risk vocabulary; NOT FR2 values, mmWave ranges, insertion loss, phase error, OTA |
| `PCIe Gen 5/6` | Interface naming as system-context pressure only | NOT exact lane counts, throughput, transfer rate, board-capability proof |
| `DDR5` | Memory interface naming as design pressure only | NOT performance claims, timing, signal-integrity proof |
| `112G/400G/800G Ethernet` | High-speed interconnect naming as stackup pressure only | NOT interface speed proof, link budget claims |
| `Beamforming/MIMO` | Architecture-level antenna system context only | NOT beam shape, phase alignment, EIRP, antenna efficiency claims |

## Stable Facts

- The Tier-2 internal source supports 7 distinct 5G telecom board families: base station, NSA, pico cell, antenna system, mmWave front-end, turnkey build, and NPI/EVT/DVT/PVT ramp.
- The source supports board-class and execution-context vocabulary, not RF-system performance or standards-compliance claims.
- 3GPP sources support identity-level naming for 5G NR system families; they do not support recency claims, version-specific features, or protocol behavior at board level.
- The current source layer does NOT support OTA validation results, field performance proof, or operator qualification claims.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a 5G telecom PCB/PCBA article.
- For RF validation vocabulary (TDR/VNA), route to `facts/methods/rf-validation-capability`.
- For hybrid RF stackup vocabulary, route to `facts/methods/hybrid-rf-stackup-capability`.
- For mmWave and beamforming conservative framing, route to `facts/methods/beamforming-mmwave-conservative-generation-gate`.
- For 3GPP version recency checks, route to `facts/standards/5g-nr-identity-and-revision-boundary`.
- Update `last_reconciled_at` when a new 5G-specific wiki boundary page is created.

## Limits And Non-Claims

- mmWave performance (insertion loss, phase error, beamforming accuracy, OTA outcomes) is NOT supported.
- 3GPP protocol compliance, standards-latest version claims, or NR release specifics are NOT supported.
- Operator qualification, deployment proof, or field-proven claims are NOT supported.
- Exact RF metrics (gain, EIRP, S-parameters at production level) are NOT supported.
- PCIe Gen 5/6, DDR5, 112G/400G/800G performance or throughput proof is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated 5G telecom wiki boundary page | Closed — created and promoted to `active` in P4-174 |
| Companion fact card (this file) | Closed — created in P4-181 |
| 3GPP exact clause-level vocabulary | Official 3GPP document page with stable public URL |
| FR1/FR2 exact frequency band tables | Official 3GPP or ITU frequency-plan source recovery |
| OTA / antenna-performance vocabulary | Project-specific RF validation records, not wiki-layer |
| 5G mmWave substrate/stackup depth | Official Isola, Panasonic, or Rogers mmWave-material owner page |
| mmWave connector / transition validation depth | Vendor-controlled connector/launch datasheet with public stable URL |
