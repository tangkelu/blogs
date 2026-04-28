# P4-30 HILPCB Blog1-13 Lane A Keyboard General Audit

Date: 2026-04-28

## Purpose

Audit the `HILPCB-blog1-13` keyboard/general lane for `llm_wiki` data learning only.

Treat the input drafts as claim inventories, not as facts.

Do not write blogs, fact cards, sources, wiki pages, prompts, or global trackers in this round.

## Input Files

- `/code/blogs/tmps/HILPCB-blog1-13/en/pcb-for-mechanical-keyboards.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/mechanical-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/mechanical-keyboard-pcb-manufacturing.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/keyboard-pcb-assembly.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/custom-keyboard-circuit-board.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/custom-pcb-for-keyboards.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/key-switch-pcb-for-keyboards.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/rgb-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/rgb-backlit-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/wireless-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/flexible-pcb-for-keyboards.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/multi-layer-pcb-for-keyboards.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/high-density-pcb-for-keyboards.md`

## Baseline Finding

`llm_wiki` already covers some reusable upstream support for this lane:

- generic SMT assembly and inspection posture
- surface-finish selection posture
- flex and rigid-flex material / bend-governance posture
- multilayer and HDI vocabulary
- USB Type-C connector review posture

`llm_wiki` does not yet appear to have keyboard-specific governance for:

- mechanical-keyboard architecture and matrix framing
- hot-swap socket claims and switch-change durability
- QMK / VIA compatibility language
- per-key RGB / underglow implementation boundaries
- wireless keyboard Bluetooth / 2.4 GHz positioning
- keyboard-specific USB-C daughterboard and ESD framing
- consumer-device compliance language such as `FCC` / `CE`

Net: this lane is only partially covered. Generic PCB/PCBA/process support exists, but keyboard-specific claim control is still thin.

## Per-Draft Disposition

| Draft | Status | Safe Reuse In `llm_wiki` | Blocked / Rejected Content |
| --- | --- | --- | --- |
| `pcb-for-mechanical-keyboards.md` | partial | Topic intent, layout families, switch/stabilizer compatibility as inventory only | Thickness, copper, layer-count defaults; case-dimension tables; hot-swap durability; RGB current; universal suitability claims |
| `mechanical-keyboard-pcb.md` | partial | Keyboard PCB architecture intent, matrix/controller/layout vocabulary as inventory only | NKRO, latency, controller recommendations, QMK/VIA compatibility, reinforced-pad durability, production/timeline claims |
| `mechanical-keyboard-pcb-manufacturing.md` | partial | Fabrication and assembly workflow intent; finish-family and inspection-stage vocabulary if mapped to existing generic sources | All numeric process values, tolerances, hole sizes, finish recommendations, quality/yield/cost/lead-time claims |
| `keyboard-pcb-assembly.md` | partial | Assembly-stage intent, component-class inventory, test-flow intent | Placement accuracy, stencil thickness, reflow profile, defect-rate, throughput, reliability, traceability, test-coverage guarantees |
| `custom-keyboard-circuit-board.md` | partial | Custom-layout and product-definition intent | Any dimensional, commercial, compatibility, or capability promises stated as general fact |
| `custom-pcb-for-keyboards.md` | partial | Custom keyboard project framing and feature-scope inventory | Service promises, manufacturing capability, pricing, MOQ, timeline, or design-success claims |
| `key-switch-pcb-for-keyboards.md` | partial | Switch-footprint / hot-swap / stabilizer topic inventory | Socket-brand performance, insertion-cycle durability, pad-strength, universal 3-pin/5-pin claims, switch-feel outcomes |
| `rgb-keyboard-pcb.md` | partial | RGB and lighting-control topic inventory | LED current, voltage-drop, thermal, brightness, driver suitability, animation performance, power-budget claims |
| `rgb-backlit-keyboard-pcb.md` | partial | Backlight / underglow topic inventory | Shine-through performance, illumination uniformity, power draw, durability, or manufacturing-ease claims |
| `wireless-keyboard-pcb.md` | mostly blocked | Wireless / RF / battery / antenna topic inventory only | Bluetooth versioning, latency, battery life, RF range, dual-mode performance, certification/compliance, module recommendations |
| `flexible-pcb-for-keyboards.md` | partial | Split-keyboard, internal interconnect, rigid-flex use-case framing | Bend radius, dynamic-flex life, material rankings, reliability, connector-elimination benefits stated as universal fact |
| `multi-layer-pcb-for-keyboards.md` | partial | Multilayer routing / plane-separation topic intent | Layer thresholds, USB high-speed necessity claims, EMC benefits, current capacity, cost/performance assertions |
| `high-density-pcb-for-keyboards.md` | partial | HDI, microvia, compact-feature topic inventory | HDI threshold numbers, geometry tables, via dimensions, fine-pitch support, reliability/cost/manufacturability claims |

## Claim-Family Rules

Allowed as data inventory only:

- keyboard topic clustering such as layout, switch matrix, hot-swap, RGB, wireless, flex, multilayer, HDI, assembly
- feature vocabulary that can later be mapped to existing generic wiki/source coverage
- product-intent distinctions such as wired vs wireless, soldered vs hot-swap, rigid vs flex, 2-layer vs more complex routing contexts

Allowed for future conservative reuse only when already supported elsewhere:

- generic SMT / inspection flow from existing HIL or APT assembly sources
- generic surface-finish selection posture from existing finish sources
- guarded flex / rigid-flex framing from existing flex material and bend-guidance work
- guarded HDI and multilayer vocabulary from existing internal/public source records
- guarded USB Type-C connector review posture from existing USB-IF source records

Needs official source or dated capability record before use:

- numeric values of any kind
- cost, MOQ, lead time, yield, defect rate, quality rate, or durability-cycle claims
- hot-swap socket life, pad-strength, or insertion-cycle claims
- QMK, VIA, controller, firmware, or software compatibility claims
- USB-C electrical, mechanical, certification, or high-speed compliance claims
- Bluetooth version, RF range, latency, polling rate, coexistence, and battery-life claims
- FCC, CE, RoHS, REACH, USB-IF, or other compliance / certification claims
- RGB current, brightness, thermal, or power-budget claims
- exact stackup, layer-count threshold, HDI geometry, flex bend-radius, or reliability claims

Reject from draft-to-data promotion:

- supplier capability statements stated without bounded source and date
- consumer-performance promises
- universal design rules presented as if they are standards-backed
- keyboard-market trend or demand claims

## Candidate Future Fact / Source / Wiki Needs

High-value source needs:

- official QMK documentation source record
- official VIA documentation source record
- official Bluetooth SIG vocabulary / trademark / version context source
- official FCC equipment-authorization or labeling guidance source for intentional radiators
- official CE / RED entry-point source for wireless consumer keyboards sold into the EU
- official hot-swap socket manufacturer sources if switch-socket durability is ever needed
- official LED driver / addressable LED family sources if RGB electrical claims are needed

High-value fact or wiki needs:

- keyboard matrix and anti-ghosting / NKRO boundary note
- hot-swap vs soldered keyboard PCB governance note
- keyboard RGB and underglow power / routing boundary note
- wireless keyboard PCB architecture boundary note
- keyboard USB-C daughterboard / connector-zone review note
- keyboard-specific QMK / VIA compatibility governance note
- keyboard-general rewrite gate tying generic PCB support to consumer-device claim blocks

## Completion Status

Complete for this round:

- all listed drafts were reviewed enough to inventory topic intent and claim families
- existing `llm_wiki` support was checked for keyboard-adjacent coverage
- lane disposition and claim-family rules are now recorded in this log only

Not done in this round:

- no facts, sources, wiki pages, prompts, blog drafts, or global tracking files were edited
- no draft claims were elevated into authoritative `llm_wiki` facts
