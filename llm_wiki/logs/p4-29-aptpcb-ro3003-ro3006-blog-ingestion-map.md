# P4-29 APTPCB RO3003 / RO3006 Blog Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the English RO3003 / RO3006 / Rogers draft batch under `/code/blogs/tmps/APTPCB_blog2603/en` and defines how the batch may be consumed by `llm_wiki`.

The batch is useful as a topic-intent and rewrite-gap inventory. It is not a primary source for Rogers laminate values, fabrication capability, certification status, cost, inventory, lead time, or finished-board RF performance.

## Target Drafts

- `ro3003-pcb.md`
- `ro3003-pcb-fabrication.md`
- `ro3003-pcb-manufacturing.md`
- `ro3003-pcb-manufacturer.md`
- `ro3003-pcb-supplier.md`
- `ro3003-pcb-cost.md`
- `ro3003-quick-turn-pcb.md`
- `ro3003-custom-pcb.md`
- `ro3003-pcb-assembly.md`
- `rogers-circuit-board-design.md`
- `rogers-ro3003-rf-pcb.md`
- `rogers-ro3003-high-frequency-pcb.md`
- `rogers-ro3003-low-loss-pcb.md`
- `rogers-ro3003-microwave-pcb.md`
- `rogers-ro3003-mmwave-pcb.md`
- `rogers-ro3006-pcb.md`
- `rogers-ro3006-pcb-fabrication.md`
- `rogers-ro3006-pcb-manufacturer.md`
- `rogers-ro3006-rf-pcb.md`
- `rogers-ro3006-microwave-pcb.md`

## Baseline Finding

Current `llm_wiki` already has the primary Rogers RO3000 material layer:

- `materials-rogers-ro3003`
- `materials-rogers-ro3006`
- `materials-rogers-ro3003-vs-ro3006`
- `materials-rogers-ro3003-vs-ro3006-vs-ro3010-vs-ro3035`
- `materials-rogers-ro3000-processing`
- `materials-rogers-material-selector`
- `materials-rogers-ro3000-family`

Therefore this pass should not create new Rogers numeric facts from draft prose. The correct result is claim-family disposition and prompt-consumption gating for the draft batch.

## Disposition Contract

Use these dispositions for the batch:

- `already_supported_by_official_ro3000_layer`: material-property claims must be pulled from existing Rogers source-backed cards.
- `rewrite_intent_candidate`: draft structure or reader question is useful for future rewrite prompts.
- `internal_positioning_only`: APT/HIL service framing may help with site-level handoff, but not with product values or proof of capability.
- `needs_source_or_project_data`: plausible engineering claim, but cannot be reused without official source, dated internal capability record, or project-specific evidence.
- `draft_only_blocked`: draft-derived formula, worked example, supplier claim, process window, threshold, or commercial claim that must not enter reusable facts.
- `reject_or_delete`: cost, lead-time, stock, certification, qualification, yield, accepted-lot, or performance-proof claim without a separate source lane.

## Per-Draft Coverage Table

| Draft | Current status | Safe reuse | Blocked / rejected content |
| --- | --- | --- | --- |
| `ro3003-pcb.md` | `already_supported_by_official_ro3000_layer` | RO3003 material-selection intent, 77 GHz / ADAS topic framing, comparison need against RO3006 / RO4000 / FR-4. | Draft loss arithmetic as performance proof, copper-profile percentage claims, core-thickness availability, assembly profile values, and APT capability claims unless independently sourced. |
| `ro3003-pcb-fabrication.md` | `rewrite_intent_candidate` | PTFE-aware fabrication workflow topics: drilling, plasma preparation, imaging, hybrid lamination, plating, surface finish. | Drilling parameters, plasma recipes, IPC Class 3 numeric thresholds, validation requirements, or process sequence as universal recipe. |
| `ro3003-pcb-manufacturing.md` | `rewrite_intent_candidate` | Thermal-management and turnkey-manufacturing questions for RO3003 programs. | POFV design rules, finish-loss claims, nitrogen reflow windows, X-ray acceptance levels, IPC-1601 compliance proof. |
| `ro3003-pcb-manufacturer.md` | `internal_positioning_only` | Supplier-qualification checklist shape. | Certification baseline claims, IPC-6012 numeric plating values, ESS/NDI proof, supplier qualification, IATF status, accepted-lot language. |
| `ro3003-pcb-supplier.md` | `draft_only_blocked` | Procurement question inventory: material authenticity, cost, lead time, shelf life, supplier audit questions. | Cost reduction percentages, lead-time options, stocking claims, APT-specific audit answers, current inventory, commercial commitments. |
| `ro3003-pcb-cost.md` | `reject_or_delete` | Cost-driver categories only: material share, layer count, panel utilization, hybrid-stackup tradeoff. | `30-45%` savings, price multipliers, raw-material pricing, volume economics, guaranteed reduction strategies. |
| `ro3003-quick-turn-pcb.md` | `draft_only_blocked` | Prototype scheduling question inventory. | Quick-turn lead times, stock availability, material hold, shelf-life planning, prototype-to-production claims. |
| `ro3003-custom-pcb.md` | `rewrite_intent_candidate` | Custom stackup, impedance, via, cavity, and DFM checklist topics. | Geometry numbers, impedance closure claims, POFV / blind-via / cavity capability, quote promises. |
| `ro3003-pcb-assembly.md` | `needs_source_or_project_data` | Assembly control categories: moisture, stencil, reflow, placement, X-ray, first article. | Bake windows, stencil voiding rules, nitrogen profile values, 3D AXI acceptance criteria, FAI release proof. |
| `rogers-circuit-board-design.md` | `rewrite_intent_candidate` | Design-translation structure from stackup to trace geometry, vias, antenna feed, thermal, Gerbers, first hardware. | Trace-width tables, launch-performance claims, thermal rules, simulation-to-hardware promises. |
| `rogers-ro3003-rf-pcb.md` | `rewrite_intent_candidate` | RF design checklist and validation structure. | Transmission-line dimension values, surface-finish loss claims, power-handling rules, TDR/VNA production promises. |
| `rogers-ro3003-high-frequency-pcb.md` | `already_supported_by_official_ro3000_layer` | Frequency-band decision framework if paired with official material cards. | Hard frequency cutoffs for substrate viability, copper-profile loss percentages, production readiness claims. |
| `rogers-ro3003-low-loss-pcb.md` | `needs_source_or_project_data` | Low-loss explanation and measurement-topic inventory. | Link-budget deltas, receiver sensitivity / detection-range claims, realized insertion-loss statements, VNA/TDR proof. |
| `rogers-ro3003-microwave-pcb.md` | `rewrite_intent_candidate` | X/Ku/Ka-band topic structure: traces, filters, power, connectors, verification. | Power-handling values, filter-design guarantees, connector-interface performance, impedance verification promises. |
| `rogers-ro3003-mmwave-pcb.md` | `rewrite_intent_candidate` | mmWave sensitivity framing: surface roughness, via stubs, antennas, thermal, packaging. | Surface-wave / resonance / POFV / qualification claims without project-specific evidence. |
| `rogers-ro3006-pcb.md` | `already_supported_by_official_ro3000_layer` | RO3006 compactness-vs-loss tradeoff and RO3003 comparison intent. | Guided-wavelength and patch-size worked examples as reusable facts, availability claims, fabricator calibration claims. |
| `rogers-ro3006-pcb-fabrication.md` | `rewrite_intent_candidate` | RO3006-specific manufacturing question inventory around higher-Dk narrow traces. | Incoming inspection rules, drilling/plasma/LDI parameters, IPC Class 3 plating thresholds, final-inspection criteria. |
| `rogers-ro3006-pcb-manufacturer.md` | `internal_positioning_only` | Manufacturer qualification checklist structure for RO3006. | In-house equipment proof, LDI capability proof, material sourcing proof, certification status, ESS reliability proof. |
| `rogers-ro3006-rf-pcb.md` | `rewrite_intent_candidate` | RF design review topics for Dk 6.15 boards. | 50 ohm trace geometry values, differential-pair rules, insertion-loss budgets, via-resonance claims. |
| `rogers-ro3006-microwave-pcb.md` | `rewrite_intent_candidate` | Compact filter, diplexer, phase-shifter, and microwave-module topic intent. | Filter miniaturization percentages, high-power thermal claims, phase-shifter performance, APT program commitments. |

## Claim-Family Rules

### Material Values

Use only existing Rogers official source-backed cards for reusable numeric values:

- `RO3003`: Dk, Df, TcDk, CTE, thermal conductivity, moisture absorption, UL, and lead-free compatibility.
- `RO3006`: Dk, Df, design Dk, TcDk, CTE, thermal conductivity, moisture absorption, UL, and lead-free compatibility.
- `RO3003 vs RO3006`: directionality of lower-loss vs compact higher-Dk selection.

Do not promote values from the draft batch when they differ in wording, rounding, or context.

### Formulas And Worked Examples

Draft formulas and calculations may indicate what a future article needs to explain, but they are not facts in this wiki.

Blocked unless separately sourced or project-specific:

- dielectric-loss arithmetic
- guided-wavelength / patch-size calculations
- link-budget deltas
- trace-width estimates
- resonator length estimates
- center-frequency-shift examples
- copper-roughness loss percentages

### Fabrication And Assembly

Existing `llm_wiki` process cards can support guarded discussion of PTFE-compatible processing, hybrid stackups, surface-finish selection, RF validation, drilling / transition control, and assembly route planning.

Blocked unless tied to a dated capability record, official process guide, or project evidence:

- drilling speeds / feeds
- plasma recipes
- lamination cycles
- IPC acceptance thresholds
- plating thickness values
- bake / reflow / TAL windows
- X-ray void limits
- ESS / NDI / FAI proof
- TDR/VNA acceptance promises

### Supplier, Cost, Lead Time, And Certification

Default disposition: `reject_or_delete`.

This includes:

- stocking and quick-turn claims
- current material availability
- lead-time bands
- cost reduction percentages
- inventory or sourcing relationships
- IATF / defense / automotive qualification proof
- supplier approval or audit-passed language
- yield, scrap, throughput, or no-redesign claims

## Prompt-Consumption Gate

Before rewriting or generating from this batch:

1. Pull RO3003 / RO3006 values from `materials-rogers-ro3003`, `materials-rogers-ro3006`, and related selector cards.
2. Pull process framing from `materials-rogers-ro3000-processing`, `methods-hybrid-rf-stackup-capability`, `methods-ptfe-processing-capability`, and RF validation / surface-finish cards.
3. Use this ingestion map to remove blocked draft claims before creating the evidence pack.
4. If a target article needs cost, lead time, stock, certification, or acceptance criteria, stop and require a separate source lane.

## Completion Status

This batch is absorbed at claim-family disposition level.

No new Rogers material numeric fact was created from the draft batch because the official Rogers RO3000 layer already covers the reusable material facts.

Next useful execution step: build one rewrite gate for RO3003 / RO3006 article generation that consumes existing Rogers facts plus this batch's blocked-claim rules.
