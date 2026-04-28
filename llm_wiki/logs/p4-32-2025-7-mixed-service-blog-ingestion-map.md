# P4-32 2025.7 Mixed Service Blog Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the five English / mixed-language drafts under `/code/blogs/tmps/2025.7/en` and defines how the batch may be consumed by `llm_wiki`.

The batch is useful as a small topic-intent and prompt-consumption inventory. Most reusable factual support already exists in `llm_wiki` for Rogers materials, PCBA service flow, SMT assembly, through-hole assembly, and generic keyboard-PCB process boundaries. The drafts themselves are not primary evidence for Highleap capability, service performance, cost, lead time, equipment, quality outcomes, market positioning, or keyboard product performance.

## Existing Coverage Check

No existing `llm_wiki` absorption record was found for `2025.7`, `2025.7/en`, or the exact `/code/blogs/tmps/2025.7/en` batch before this pass.

## Target Drafts

- `Rogers PCB.md`
- `keyboard-pcb-types.md`
- `pcba-service.md`
- `smt-assembly.md`
- `through-hole-assembly.md`

## Baseline Finding

Current `llm_wiki` already has source-backed layers for four of the five topics:

- Rogers PCB material and process support:
  official Rogers RO3000 / RO4000 / RT/duroid / TMM source-backed material cards, Rogers processing context, APT internal Rogers framing, RF validation, PTFE processing, and RF finish-selection boundaries.
- PCBA service:
  mixed SMT / THT assembly flow, turnkey assembly framing, BOM sourcing and traceability, layered inspection stack, ICT/FCT boundary, NPI / FAI gates, and box-build integration posture.
- SMT assembly:
  stencil / paste / placement / reflow / inspection flow, SPI/AOI/X-ray/ICT/FCT layering, fine-pitch / BGA / QFN controls, and reflow source-coverage boundaries.
- Through-hole assembly:
  THT versus press-fit versus cable / harness route boundaries, mixed-technology sequencing, selective solder framing, and inspection / validation posture.

Current `llm_wiki` only has claim-boundary support for `keyboard-pcb-types.md`:

- The P4-30 HILPCB input-device layer covers keyboard topic intent and generic PCB / PCBA / flex / HDI / USB-C process language.
- It does not support keyboard-market segmentation, QMK / VIA, hot-swap, RGB, wireless, consumer compliance, or keyboard performance claims as reusable facts.

## Per-Draft Coverage Table

| Draft | Current status | Safe reuse | Blocked / rejected content |
| --- | --- | --- | --- |
| `Rogers PCB.md` | `source_backed_existing_layer` | Rogers material-family intent, application buckets, material-selection and process-control sections when rewritten from official Rogers and existing `llm_wiki` cards | market claims, performance benefits not tied to product datasheets, design-rule numerics, process-control guarantees, cost optimization, partner-selection claims, Highleap capability |
| `keyboard-pcb-types.md` | `claim_family_only` | keyboard PCB type inventory, layout / feature / production-scaling questions, generic PCBA and input-device boundary language | market segmentation, technology trends, cost optimization, scalable production claims, Highleap end-to-end execution, hot-swap / RGB / wireless / firmware / compliance / performance claims |
| `pcba-service.md` | `source_backed_existing_layer_with_capability_blocks` | turnkey PCBA flow, PCB fabrication + assembly + component sourcing + test + scale-up outline, if sourced from existing PCBA cards | Highleap capability breadth, prototype-to-mass-production proof, sourcing strength, quality-control coverage, scalability, commercial positioning, lead time, yield |
| `smt-assembly.md` | `source_backed_existing_layer_with_capability_blocks` | SMT process-flow structure, stencil / placement / reflow / inspection / component-sourcing sections, if sourced from existing PCBA cards | precision / speed / reliability claims, equipment and automation proof, production scale, engineering-support promises, application qualification, quality outcomes |
| `through-hole-assembly.md` | `source_backed_existing_layer_with_capability_blocks` | THT definition, THT-vs-SMT distinction, process stages, challenges, DFM route planning, use-case categories, if sourced from existing THT / mixed-technology cards | universal THT advantages, soldering parameters, reliability guarantees, sector qualification, Highleap project-execution claims, quality or durability outcomes |

## Claim-Family Rules

### Can Be Consumed Now

- topic and outline shape for Rogers PCB, keyboard PCB types, PCBA service, SMT assembly, and through-hole assembly
- generic process wording only through existing source-backed `llm_wiki` cards
- Rogers material facts only through official Rogers cards and registered internal Rogers framing
- PCBA / SMT / THT workflow facts only through internal source-backed cards and standards metadata already in `llm_wiki`
- keyboard content only as claim inventory and generic process framing unless future official source lanes are added

### Needs Official Source Or Dated Capability Record

- Highleap-specific capability, equipment, production scale, quality coverage, inspection coverage, engineering support, sourcing capability, prototype-to-volume, or turnkey claims
- price, lead time, MOQ, yield, throughput, quality rate, defect rate, reliability, or delivery claims
- Rogers material numeric values not already present in official source-backed cards
- SMT or THT process parameters, placement accuracy, reflow windows, solder-joint criteria, inspection coverage, or acceptance thresholds
- keyboard market, firmware, hot-swap, RGB, wireless, compliance, or performance claims

### Reject From Draft-To-Data Promotion

- marketing CTAs and partner-selection language
- Highleap capability statements without a bounded dated source
- universal process advantages or outcome guarantees
- market strategy, trend, and cost-optimization claims without current official or dated support
- any draft-originated numeric value or implied performance outcome

## Prompt-Consumption Gate

Before rewriting or generating from this batch:

1. For `Rogers PCB.md`, pull material values from official Rogers fact cards and process framing from Rogers processing / PTFE / RF validation cards.
2. For `pcba-service.md`, `smt-assembly.md`, and `through-hole-assembly.md`, pull process flow from PCBA mixed-technology, inspection, NPI / FAI, ICT/FCT, stencil / selective solder, and THT route-boundary cards.
3. For `keyboard-pcb-types.md`, use P4-30 input-device boundary rules and avoid product-performance, firmware, market, cost, or Highleap execution claims unless later sourced.
4. Stop and require a dated capability record before writing Highleap-specific production, quality, equipment, commercial, or delivery promises.

## Source Gaps

- dated Highleap capability records for service-specific SMT, THT, turnkey PCBA, quality, inspection, sourcing, volume, and lead-time claims
- official or vendor sources for keyboard-specific firmware, hot-swap sockets, RGB electrical behavior, wireless, and compliance claims if keyboard articles will be written beyond generic process context
- current market sources if keyboard market segmentation or trend claims remain necessary

## Completion Status

This batch is absorbed at claim-family and existing-layer routing level.

No new Rogers material values, PCBA process parameters, SMT / THT capability claims, Highleap service claims, keyboard performance claims, cost, lead time, yield, or quality outcomes were created from temporary draft prose. Four drafts route to existing source-backed layers; `keyboard-pcb-types.md` remains claim-family-only pending additional official source lanes.
