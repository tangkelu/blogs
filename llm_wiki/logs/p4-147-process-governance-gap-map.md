---
task_id: "p4-147-process-governance-gap-map"
status: "completed"
owner: "cascade-subagent"
lane: "process-governance gap map"
input_paths:
  - /code/blogs/llm_wiki/facts/processes/
  - /code/blogs/llm_wiki/facts/methods/
  - /code/blogs/llm_wiki/wiki/processes/
  - /code/blogs/llm_wiki/logs/backlog.md
output_paths:
  - /code/blogs/llm_wiki/facts/processes/process-governance-gap-map.md (NEW)
  - /code/blogs/llm_wiki/wiki/processes/hil-pcb-product-family-capability-map.md (NEW)
  - /code/blogs/llm_wiki/logs/p4-147-process-governance-gap-map.md
write_scope:
  - /code/blogs/llm_wiki/wiki/processes/
  - /code/blogs/llm_wiki/facts/processes/
  - /code/blogs/llm_wiki/logs/p4-147-process-governance-gap-map.md
blocked_claims:
  - process windows, acceptance thresholds, certification proof
  - supplier-proof claims
  - numeric performance claims without source
  - yield, DPPM, throughput commitments
completed_at: "2026-05-03"
---

# P4-147 Process-Governance Gap Map

## Scope

Map process governance coverage across `facts/processes/`, `facts/methods/`, and `wiki/processes/` to identify which domains have full wiki-layer aggregation and which remain at boundary-card or fact-only level. Produce reusable local knowledge — a coverage map fact card and a missing wiki aggregation page — rather than only listing URLs or timestamps.

## Pre-Execution Collision Check

- Checked `logs/p4-145-process-governance-gap-map.md`: that log used the p4-145 task ID and addressed PCBA inspection/screening/release governance cards. It was completed by a prior agent.
- `p4-147` (this task card) appears in ASSESSMENT.md section 8 as a separate queued lane with distinct `task_id` and `output_paths`. No collision detected.
- No existing `logs/p4-147-*` file found. Lane is clear.

## What Was Found

### PCBA Governance: Already Covered (Prior Lanes)

The three governance boundary cards created in a prior lane (logged as p4-145) already provide:
- `methods-pcba-inspection-process-governance-boundary` — SPI→AOI→X-ray→ICT→FCT gate sequencing
- `methods-pcba-screening-qualification-governance-boundary` — ESS / Qualification / FAI three-layer separation
- `methods-pcba-release-traceability-governance-boundary` — IQC→Production→Test→Release evidence chain

These are absorbed into `wiki/processes/pcba-npi-to-mass-production-flow.md`.

### APT PCB Capability Families: Already Covered

All 6 APT capability fact cards (`apt-rigid`, `apt-flex`, `apt-hdi`, `apt-rigid-flex`, `apt-metal-core`, `apt-ceramic`) are aggregated in:
- `wiki/processes/apt-capability-family-map-and-boundaries.md`
- `wiki/processes/apt-pcb-manufacturing-capabilities.md`

### HIL PCB Product Family: **GAP IDENTIFIED**

**15 HIL capability fact cards** exist in `facts/processes/`:
- `hil-single-double-layer`, `hil-multilayer`, `hil-fr4`, `hil-high-tg`, `hil-heavy-copper`, `hil-halogen-free`, `hil-high-speed`, `hil-high-thermal`, `hil-high-frequency`, `hil-rogers`, `hil-teflon-pcb`, `hil-hdi`, `hil-rigid-flex`, `hil-backplane`, `hil-ic-substrate`

**Zero HIL PCB product-family wiki aggregation pages** existed in `wiki/processes/` before this task. Every HIL capability fact card was an isolated island with no routing frame for prompt consumption.

This is the primary governance gap: the knowledge base had symmetrical APT wiki coverage but asymmetrical HIL wiki coverage.

## Changes Made

### New: `facts/processes/process-governance-gap-map.md`

A fact card that:
- Maps which process governance domains have full wiki-layer aggregation vs. fact-only coverage
- Explicitly names the 15 HIL PCB fact cards as the missing wiki layer
- Documents all PCBA governance coverage (inspection, screening/qualification, release/traceability, NPI flow, DFM/DFT, mixed-tech, conformal coating, low-void BGA, selective solder)
- Documents all APT capability family coverage
- Maintains blocked-claims discipline for process windows, certification proof, supplier proof, numerics without source

### New: `wiki/processes/hil-pcb-product-family-capability-map.md`

A wiki aggregation page that:
- References all 15 HIL capability fact cards
- Organizes them into four governance groups: Layer-Count Entry, Thermal/Reliability, Signal-Integrity/RF, Density/Advanced Structure
- Provides a product-family selection table with key parameters and governance boundary notes for each family
- States explicit engineering boundaries (e.g., RF families ≠ High-Speed Digital, MCPCB ≠ Ceramic, IC Substrate ≠ standard HDI)
- Lists common misreadings that could cause cross-contamination between families
- Mirrors the structure of `wiki/processes/apt-capability-family-map-and-boundaries.md` for consistency
- References all 15 HIL source JSON files

## Blocked Claims (Maintained)

- ❌ Process windows, acceptance thresholds, coverage percentages
- ❌ Certification pass/fail status for any specific HIL product
- ❌ Supplier-proof or qualification proof
- ❌ Yield, DPPM, throughput commitments
- ❌ Lead-time commitments as universal claims (cited only as fact-card level refresh-sensitive items)
- ❌ VNA frequency-range guarantees beyond published product page scope

## Residual Gaps

- HIL assembly capability fact cards (`hil-smt-assembly`, `hil-through-hole-assembly`, `hil-small-batch-assembly`, `hil-large-volume-assembly`, `hil-turnkey-assembly`, `hil-box-build-assembly`) are absorbed into the PCBA NPI wiki page; a dedicated HIL assembly wiki aggregation may be warranted in a future lane if divergence from APT assembly posture requires separate framing
- The process-governance gap map fact card itself should be refreshed when new fact cards are added to `facts/processes/` or new wiki pages are added to `wiki/processes/`
- No `sources/registry/` update was required for this lane: all source IDs already existed from prior indexing; no new source records were needed

## Task Status

**completed** — reusable local knowledge has been written to disk:
1. `facts/processes/process-governance-gap-map.md` (NEW fact card, 19 source IDs, comprehensive coverage table)
2. `wiki/processes/hil-pcb-product-family-capability-map.md` (NEW wiki page, 15 fact IDs, 15 source IDs)
3. This lane log

All outputs are within the declared `write_scope`. No shared trackers modified. No collision detected.
