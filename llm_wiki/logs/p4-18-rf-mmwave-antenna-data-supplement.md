# P4-18 RF mmWave Antenna Data Supplement

Date: 2026-04-27

## Purpose

Continue the empty-image data-first program without writing blogs.

This round targets the RF / 5G / antenna subset from:

- `/code/hileap/frontendHIL/docs/2026-04-23-empty-image-blog-rewrite-priority-list.md`

Primary target slugs:

- `5g-isolator-5g-telecom`
- `mmwave-5g-5g-telecom`
- `antenna-system-5g-telecom`
- `5g-base-station-5g-telecom`
- `5g-pico-cell-5g-telecom`

## Execution Contract

- Do not draft blogs.
- Use current local `llm_wiki` facts, topic pages, and source registry records first.
- Add only conservative evidence support for what the present source layer can prove.
- Record blocked claim classes explicitly where source support stops.

## Existing Source Layer Reused

No new source-registry records were required in this round.

Current reusable registry support already covered:

- 3GPP identity and revision-sensitive 5G standards context
- Smiths Interconnect isolator / circulator component-class context
- Analog Devices and Qorvo phased-array and phase-shifter context
- internal telecom, antenna, high-frequency, microwave, Rogers, NPI, PCBA quality, turnkey, and volume-assembly pages

This means the gap was mainly at the fact-card and readiness-map layer, not at raw source registration.

## New Support Added

New fact cards:

- `facts/methods/antenna-system-feed-network-vs-performance-boundary.md`
- `facts/methods/mmwave-routing-sensitivity-vs-metric-claims-boundary.md`
- `facts/methods/telecom-node-board-context-vs-radio-coverage-claims.md`

New process page:

- `wiki/processes/rf-5g-empty-image-rewrite-readiness-map.md`

These additions tighten three weak zones that were still under-specified:

- antenna-system language drifting into performance and chamber claims
- mmWave language drifting into metrics, bands, and qualification claims
- base-station / pico-cell language drifting into coverage, capacity, and deployment claims

## Readiness Impact

| slug | updated status | safe rewrite lane |
| --- | --- | --- |
| `5g-isolator-5g-telecom` | `ready_for_component-class-boundary_rewrite` | isolator-adjacent RF board execution only |
| `mmwave-5g-5g-telecom` | `ready_but_only_as_execution-sensitivity_context` | laminate / transition / shielding / validation sensitivity only |
| `antenna-system-5g-telecom` | `ready_for_feed-network_and_validation_planning` | feed network, launches, cavity or shield features, validation handoff |
| `5g-base-station-5g-telecom` | `ready_for_telecom-node_board_execution` | mixed-signal telecom-node partitioning, sourcing, inspection, validation |
| `5g-pico-cell-5g-telecom` | `ready_for_compact-node_manufacturing_scope` | compact-node coexistence, enclosure-aware placement, assembly and inspection access |

## Still Blocked

This round does not unlock:

- RF budgets, link budgets, insertion loss, return loss, gain, isolation, antenna efficiency, EIRP, phase balance, amplitude balance, or calibration claims
- FR1 / FR2 values, named frequency-band claims, range, coverage, capacity, throughput, latency, or protocol-compliance claims
- antenna-spacing rules, feed dimensions, launch dimensions, via-stub targets, backdrill numbers, cavity geometry, or stackup numerics
- chamber results, OTA results, environmental qualification, supplier qualification, operator approval, or deployment-success claims
- exact test-frequency ceilings or current latest standards-revision claims without a fresh dated source check

## Slug-Specific Residual Gaps

### `5g-isolator-5g-telecom`

Current posture:

- usable only if the article treats `isolator` as component-class context and keeps claims on the surrounding board

Blocked until narrower sources are added:

- part-selection criteria
- device behavior details
- ferrite-performance claims
- package-specific or band-specific claims

### `mmwave-5g-5g-telecom`

Current posture:

- usable only as execution sensitivity and validation-planning context

Blocked until narrower sources are added:

- mmWave standards-band detail
- RF metric claims
- chamber or OTA workflow claims
- qualification or supplier-proof claims

### `antenna-system-5g-telecom`

Current posture:

- usable only as feed-network, interface, grounding, shielding, and validation-handoff context

Blocked until narrower sources are added:

- antenna metrics
- chamber correlation
- array calibration
- performance comparisons

### `5g-base-station-5g-telecom` and `5g-pico-cell-5g-telecom`

Current posture:

- usable only as telecom-node board and PCBA execution context

Blocked until narrower sources are added:

- field coverage or capacity claims
- rollout or operator-proof claims
- architecture-detail claims beyond high-level context

## Verification Notes

- All new `source_ids` referenced in this round resolve to existing registry records.
- The new files remain under `llm_wiki` only.
- Shared tracking files were intentionally not modified.
