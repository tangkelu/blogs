# P4-92 2026.4.29 Conservative Rewrite Consumption Batch 3

Date: 2026-05-01

## Purpose

Consume three more already-routed `/code/blogs/tmps/2026.4.29/en` drafts directly in the draft layer by rewriting them into conservative, prompt-usable versions.

This pass does not add new authority. It only removes unsupported claims and rewrites each draft so it stays inside the already-landed power-energy, lidar, and compute/high-speed review boundaries plus generic board-review posture.

## Inputs Reviewed

- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
- `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- `wiki/processes/laser-time-of-flight-and-pulsed-driver-boundaries.md`
- `facts/methods/laser-time-of-flight-pulsed-driver-and-safety-boundary.md`
- `wiki/processes/compute-infrastructure-pcb-review-boundaries.md`
- `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
- `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
- `tmps/2026.4.29/en/inverter-pcb.md`
- `tmps/2026.4.29/en/lidar-pcb.md`
- `tmps/2026.4.29/en/fpga-pcb.md`

## Draft Consumption Result

Rewritten drafts:

- `tmps/2026.4.29/en/inverter-pcb.md`
- `tmps/2026.4.29/en/lidar-pcb.md`
- `tmps/2026.4.29/en/fpga-pcb.md`

What changed:

- removed unsupported compliance, qualification, deployment-readiness, supplier-proof, and program-readiness claims
- removed unsupported exact numerics for power, current, voltage, creepage, surge, hi-pot, range, accuracy, timing, optical power, jitter, skew, lane rate, and thermal behavior
- kept only already-routed subsystem, workflow, and guarded ecosystem-context nouns
- rewrote each article around conservative board-review posture, section partitioning, validation staging, and practical manufacturing or integration review questions
- rewrote frontmatter `description` and `tags` where needed to remove blocked proof language

Per-draft safe noun handling:

- `inverter-pcb.md`
  - kept guarded `central inverter`, `UPS`, `heavy copper`, `high thermal`, `metal core`, `DFM`, `DFT`, `DFA`, and `functional test` only as board-family, material-route, or workflow context
  - removed or downgraded exact `IEC 61851`, `UL`, grid-code, `IATF 16949`, supplier-capability, and exact power-performance claims
- `lidar-pcb.md`
  - kept guarded `time-of-flight`, `pulsed laser driver`, and `laser safety control` only at subsystem and validation-posture level
  - removed or downgraded exact `IEC 60825-1`, `IATF 16949`, `PPAP`, `AEC-Q100`, range, accuracy, detector-performance, point-cloud, FPGA-processing, supplier-proof, and program-readiness claims
- `fpga-pcb.md`
  - kept guarded `FPGA`, `BGA`, `controlled impedance`, `TDR`, and `first-article inspection` at board-review and validation-posture level; exact `Xilinx Versal`, `Intel Agilex`, `Kintex`, `PCIe`, `DDR4`, `DDR5`, and `LVDS` are allowed only as guarded ecosystem or design-pressure context where retained
  - removed or downgraded exact jitter, skew, lane-rate, power, thermal, supplier-proof, and deployment-readiness claims

## What Is Now Prompt-Usable

These three drafts are now usable as conservative drafts for:

- inverter board partitioning, thermal-route selection, connector handoff, and staged manufacturing-validation workflow
- lidar timing-path, pulsed-driver, isolation-boundary, and safety-control board-review framing
- FPGA-oriented dense-digital board review around escape planning, stackup discipline, controlled-impedance routing, power-path review, and staged validation

## Still Blocked

- any exact compliance, field-performance, or supplier-readiness claim in `inverter-pcb.md`
- any exact range, accuracy, detector, eye-safety, automotive qualification, or program-readiness claim in `lidar-pcb.md`
- any exact named-platform capability proof, interface validation proof, jitter/skew/lane-rate numeric, or supplier-readiness claim in `fpga-pcb.md`
- any HILPCB-specific validated performance, qualification, or sector-readiness claim across these drafts

## Status

- draft status: `conservative_rewrite_ready`
- supporting authority status: `unchanged_from_existing_p4_83_routes`
- next likely action:
  - continue conservative rewrite consumption with `endoscope` and possibly `gaming` if they can be stripped back to existing boundaries
  - do not pull `dna-computing` or `biological-computing` forward without narrower owner or regulator authority recovery
