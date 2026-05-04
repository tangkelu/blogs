# P4-70 Defense EW Surveillance Targeting Topic Aggregation

Date: 2026-04-30

## Purpose

Convert the remaining reusable slice of the `P4-67` batch into prompt-consumable `llm_wiki` data by aggregating the `2026.4.27/en` defense, EW, surveillance, and targeting drafts into one conservative review-boundary page with explicit go / refresh classifications.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated jammer bandwidth, ESM/EA architecture authority, encrypted-link claims, SAR / EO / IR system proof, laser-designator or fire-control performance, environmental-qualification outcomes, export-control posture, customer-program history, or HILPCB-specific defense capability claims.

## Inputs Reviewed

- `logs/p4-67-2026-4-27-application-computing-sensor-defense-controller-summary.md`
- `/code/blogs/tmps/2026.4.27/en/electronic-warfare-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/surveillance-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- existing application, UAV control-stack, RF build-planning, RF validation, first-article, and qualification-boundary layers already present in `llm_wiki`

## Source Records Reused

No new source-record files were required in this pass.

This aggregation reuses the strongest existing source layers already in `llm_wiki`:

- internal aerospace-defense, drone-UAV, and security-equipment application framing
- internal antenna, high-frequency, microwave, quality-system, NPI, and first-article records
- existing public phased-array radar context
- existing public PX4 / MAVLink / ExpressLRS control-stack identity sources
- existing public FAA and AS9102 qualification-boundary anchors

## Fact Cards Reused

No new fact-card files were required in this pass.

This topic page aggregates the already-landed reusable method and standards layer:

- `methods-internal-application-scenario-coverage-map`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-rf-validation-capability`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-phased-array-source-coverage`
- `methods-remote-control-and-drone-control-stack-boundary`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Topic Wiki Added

- `wiki/processes/defense-ew-surveillance-targeting-pcb-review-boundaries.md`

This page makes the defense/EW/surveillance/targeting slice of `2026.4.27/en` prompt-consumable for:

- `electronic-warfare-pcb.md`
- `surveillance-pcb.md`
- `targeting-pcb.md`

## What This Unlocks

- The defense-adjacent drafts can now be conservatively rewritten as board-role, RF-build, packaging, validation, and release-governance articles rather than as mission-system proof pages.
- `electronic-warfare-pcb.md` can now stay at RF front-end partitioning, shielding, stackup, and staged validation level without pretending to prove jammer, ESM, or military-program performance.
- `surveillance-pcb.md` can now stay at multi-sensor interface, processing-board, data-link coexistence, and UAV or fixed-site review posture without claiming ISR program, encrypted-link, or platform-endurance proof.
- `targeting-pcb.md` can now be routed as a guarded timing, isolation, and review-governance draft only if laser, fire-control, and weapon-accuracy claims are stripped or separately refreshed.

## Still Blocked

- exact jammer, ESM, SIGINT, COMINT, ELINT, SAR, EO / IR, fire-control, laser-designator, or precision-weapon authority claims without narrower owner or program sources
- exact bandwidth, frequency, isolation, timing, jitter, range, tracking, endurance, pulse-current, shock, vibration, or EMI numerics
- `MIL-STD-461`, `MIL-STD-810`, `DO-160`, export-control, defense-prime, customer, mission, or fielded-program claims used as supplier or board-readiness proof
- HILPCB-specific military, surveillance, targeting, qualification-support, or deployment claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2026.4.27` defense / EW / surveillance / targeting lane
- next likely residual lane:
  - narrower owner or standards authority only if future drafts must retain exact jammer, ISR, laser, or weapon-system language
  - targeted refresh for `targeting` if the slug must keep laser-driver, fire-control, or qualification framing beyond the current conservative boundary
