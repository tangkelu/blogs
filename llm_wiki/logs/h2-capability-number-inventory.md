# H2 Capability Number Inventory

Date: 2026-04-25

## Purpose

This file converts H0 class-`B` fabrication-capability claims into governed H2 execution buckets.

It is an inventory and prioritization document.

It is not:

- a fact card
- a final reusable capability table
- permission to reintroduce fabrication numbers into blog drafts

## Relation To H0 And H2

- `H0` identified where layer-count blogs depend on fabrication-capability numerics and labeled those claims `needs_source`, `downgrade`, or `delete`.
- `H2` is the next control layer: it groups those claims by bucket, defines provisional sourceability posture, and sets handling rules before any recovery work starts.
- This file therefore sits between `h0-numeric-claim-inventory.md` and any future dated capability-source schema or capability fact card.

Core distinction for H2:

- `shop capability numbers`: fabricator-specific process limits or tolerance promises
- `process vocabulary`: terms such as backdrill, sequential lamination, coupon, laser via, stacked via
- `standards thresholds`: IPC or qualification acceptance limits
- `system / high-speed context`: interface, channel, SI, RF, or platform interpretation numbers

Only the first category belongs in this inventory, and even then only as a governed recovery target.

## Core Bucket Taxonomy

### `trace_space`

- typical claim shapes:
  - minimum line / space capability
  - standard vs advanced feature-size ladders
  - outer-layer vs inner-layer feature windows
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `12-layer`
  - `14-layer`
  - `16-layer`
  - `20-layer`
  - `24-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - recover only if a dated internal capability record exists with explicit scope and refresh discipline
  - do not infer from marketing prose, laminate datasheets, or HDI vocabulary pages
- major risks:
  - stale fine-line claims presented as universal defaults
  - confusion between standard production windows and special-process demonstrations
  - leakage into board-loss or impedance-geometry interpretation

### `drill_and_via_geometry`

- typical claim shapes:
  - minimum mechanical drill
  - minimum laser via
  - blind / buried / stacked-via geometry windows
  - hole-size-count constraints
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `18-layer`
  - `20-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - split mechanical drill, laser via, and HDI build-up geometry into separate subclaims during recovery
  - keep architecture vocabulary if sourceable numerics are absent
- major risks:
  - mixing ordinary rigid-board capability with HDI-specific process windows
  - copying one stackup example as a general shop rule
  - accidental drift into reliability thresholds

### `aspect_ratio`

- typical claim shapes:
  - finished-hole aspect-ratio limits
  - via-depth-to-diameter guidance presented as universal capability
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `16-layer`
  - `20-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - treat as a pure shop-capability bucket, not as standards or design-rule doctrine
  - require explicit distinction between mechanical-through-hole and microvia contexts
- major risks:
  - standards leakage
  - reliability interpretation masquerading as a fabrication limit
  - family-wide overclaim from one process note

### `annular_ring`

- typical claim shapes:
  - minimum annular ring targets
  - breakout margin rules
  - class-linked annular-ring tables
- likely blogs affected:
  - `6-layer`
  - `10-layer`
  - `14-layer`
  - `20-layer`
  - `22-layer`
- provisional sourceability posture:
  - `mixed_with_standards_threshold_risk`
- target handling rule:
  - do not recover any annular-ring numeric unless the source clearly states it as a current internal capability number rather than an IPC acceptance threshold
  - default to gap-control when the source language is class-based
- major risks:
  - IPC class thresholds being restated as factory capability
  - confusion between design target, acceptance criterion, and manufacturable minimum

### `registration`

- typical claim shapes:
  - layer-to-layer registration tolerance
  - drill-to-pad registration claims
  - transition-zone alignment tolerances in rigid-flex contexts
- likely blogs affected:
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `18-layer`
  - `20-layer`
  - `24-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - recover only from current capability records with explicit measurement context
  - keep general registration-posture prose if numeric recovery fails
- major risks:
  - standards-threshold substitution
  - measurement-method ambiguity
  - rigid-board and rigid-flex contexts collapsing into one number

### `impedance_tolerance`

- typical claim shapes:
  - controlled-impedance tolerance promises
  - standard vs tighter tolerance bands
  - thickness or geometry couplings presented as guaranteed outcomes
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `10-layer`
  - `12-layer`
  - `18-layer`
  - `24-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - separate `capability promise` from `TDR / coupon / verification posture`
  - recover numeric tolerance only if paired with dated capability evidence
  - keep verification-ladder framing even if tolerance numerics stay blocked
- major risks:
  - internal validation vocabulary being overread as a universal tolerance guarantee
  - geometry examples turning into unsupported default rules
  - channel-performance claims sneaking in through impedance sections

### `board_thickness`

- typical claim shapes:
  - finished-board thickness windows
  - common thickness assumptions used as manufacturing defaults
  - thickness tolerance promises
- likely blogs affected:
  - `8-layer`
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `16-layer`
  - `18-layer`
  - `24-layer`
- provisional sourceability posture:
  - `mixed_capability_and_recipe_risk`
- target handling rule:
  - separate board-family examples from actual supported capability windows
  - do not promote stackup examples or common commercial builds into reusable numerics
- major risks:
  - stackup recipe numbers being mistaken for general capability
  - tolerance language drifting into unsupported promise territory

### `copper_plating_process_windows`

- typical claim shapes:
  - copper weight windows
  - plating thickness or build allowances
  - resin-fill, heavy-copper, etch-compensation, or process-balance numbers
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `12-layer`
  - `14-layer`
  - `16-layer`
  - `20-layer`
- provisional sourceability posture:
  - `hold_until_bucket_split`
- target handling rule:
  - do not treat this as one reusable numeric bucket
  - split future recovery into narrower sub-buckets only if a real source base emerges
- major risks:
  - mixing shop capability, process recipe, IPC minima, and design guidance
  - high variance by stackup, copper weight, and panel design
  - overclaim from illustrative manufacturing notes

### `backdrill_and_stub`

- typical claim shapes:
  - backdrill depth accuracy
  - residual stub targets
  - triggers for when backdrill is required
- likely blogs affected:
  - `8-layer`
  - `12-layer`
  - `14-layer`
  - `18-layer`
  - `24-layer`
- provisional sourceability posture:
  - `needs_dated_internal_capability_source`
- target handling rule:
  - recover only pure capability numerics such as drill-control windows when explicitly sourced
  - keep SI rationale or validation posture in separate method cards
- major risks:
  - SI thresholds being smuggled in as fabrication facts
  - board-thickness dependence not being disclosed
  - mixing measurement claim with process recommendation

### `testing_and_verification_capability`

- typical claim shapes:
  - electrical-test coverage claims
  - TDR / coupon / VNA capability presence
  - verification-stage availability framed numerically
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `12-layer`
  - `18-layer`
  - `22-layer`
  - `24-layer`
- provisional sourceability posture:
  - `split_presence_from_numeric_scope`
- target handling rule:
  - capability existence may be governed as posture
  - numeric coverage, frequency ceilings, and guarantee language require dated capability evidence
  - standards acceptance percentages should not be imported through this bucket
- major risks:
  - conflating test availability with guaranteed lot coverage
  - converting method names into unsupported threshold claims
  - blending quality-assurance rhetoric with capability numerics

### `stackup_recipe_and_process_count_numbers`

- typical claim shapes:
  - sequential lamination count
  - drill-program count
  - buildup cycle count
  - hole-family-count limits
  - recommended signal / plane-count recipes framed as defaults
- likely blogs affected:
  - `6-layer`
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `18-layer`
  - `20-layer`
  - `24-layer`
- provisional sourceability posture:
  - `hold_excluded_for_reusable_numeric_work`
- target handling rule:
  - keep only as architecture or planning vocabulary
  - do not promote to reusable numerics in H2
- major risks:
  - one example stackup becoming an implied factory-wide rule
  - process-count values varying too strongly by design and materials
  - leakage into reliability or commercial claims

### `turnaround_and_commercial_numbers`

- typical claim shapes:
  - prototype lead time
  - production lead time
  - quick-turn promises
  - yield or cost uplift
- likely blogs affected:
  - `6-layer`
  - `8-layer`
  - `10-layer`
  - `12-layer`
  - `14-layer`
  - `16-layer`
  - `18-layer`
  - `20-layer`
  - `22-layer`
  - `24-layer`
- provisional sourceability posture:
  - `excluded_dynamic_numbers`
- target handling rule:
  - exclude from reusable H2 capability numerics
  - hand off only to a separate dynamic-number policy if ever needed
- major risks:
  - rapid staleness
  - sales-language contamination of technical evidence packs
  - blocking high-density readiness for the wrong reason

## Priority Order For Recovery And Governance

1. `impedance_tolerance`
   - highest reuse value across layer-count blogs and already adjacent to existing method posture cards
2. `trace_space`
   - appears widely and often anchors the most visible capability-table rows
3. `drill_and_via_geometry`
   - tightly coupled to multilayer and HDI claims but still separable from reliability if handled carefully
4. `aspect_ratio`
   - common capability-table field with relatively clear scope if separated by via type
5. `backdrill_and_stub`
   - high impact for high-layer and high-speed articles, but must stay separated from SI interpretation
6. `registration`
   - important but method-sensitive and often standards-adjacent
7. `testing_and_verification_capability`
   - useful once numeric scope is disentangled from mere method presence
8. `board_thickness`
   - lower priority because recipe/context contamination is common
9. `annular_ring`
   - defer until standards-threshold handling is clearer
10. `copper_plating_process_windows`
    - defer until this bucket is broken into narrower, governable sub-buckets
11. `stackup_recipe_and_process_count_numbers`
    - hold
12. `turnaround_and_commercial_numbers`
    - exclude

## Held / Excluded Buckets

These buckets should not become reusable capability numerics yet:

- `stackup_recipe_and_process_count_numbers`
  - reason: highly design-specific and too easy to flatten into false defaults
- `turnaround_and_commercial_numbers`
  - reason: dynamic business data, not stable technical capability facts
- `copper_plating_process_windows`
  - reason: currently too mixed to govern as one reusable numeric class

These sub-patterns should also remain blocked unless a narrower policy is written:

- IPC or qualification thresholds restated as shop capability
- board-loss, skew, stub-resonance, or channel-budget numbers inside fabrication sections
- rigid-flex bend-life or reliability thresholds presented as fabrication capability
- stackup examples converted into default manufacturability tables

## Per-Blog Impact Summary

### `6-layer`

- main H2 effect:
  - trace / space, impedance tolerance, via-rule, and testing-coverage claims stay blocked until capability sources exist
- practical implication:
  - conservative drafts can keep process posture and material numerics, but not capability tables

### `8-layer`

- main H2 effect:
  - impedance tolerance, drill / via windows, lamination-adjacent fabrication numbers, and plating / testing numerics remain governed buckets
- practical implication:
  - HDI and rigid-flex vocabulary may stay, but capability numerics remain under gap-control

### `10-layer`

- main H2 effect:
  - blind-via geometry, registration, annular ring, and impedance numbers remain blocked pending dated capability sources
- practical implication:
  - exact-product material cards help, but fabrication numerics still cannot be restored directly

### `12-layer`

- main H2 effect:
  - backdrill, impedance, drill-program, board-thickness, manufacturability geometry, and DFM-rule numbers remain governed recovery targets
- practical implication:
  - this blog will benefit early from `impedance_tolerance` and `backdrill_and_stub` recovery, but many tables still stay out

### `14-layer`

- main H2 effect:
  - transition-zone machining, via geometry, trace / space, annular-ring-adjacent rules, and closing capability bundles remain blocked
- practical implication:
  - this is one of the densest fabrication-number blogs and remains high risk without bucket-by-bucket governance

### `16-layer`

- main H2 effect:
  - heavy-copper, process-window, feature-size, and thickness-style fabrication numerics remain controlled
- practical implication:
  - article framing can stay, but reusable fabrication numbers are still thin

### `18-layer`

- main H2 effect:
  - registration, impedance, backdrill, and high-layer capability promises remain governed even though material framing improved
- practical implication:
  - conservative rewrite support stays stronger than high-density numeric support

### `20-layer`

- main H2 effect:
  - drill / via geometry, aspect ratio, stackup-process counts, and build-up capability numerics remain heavily blocked
- practical implication:
  - H2 alone will not unlock this blog unless later reliability and HDI-specific workstreams succeed

### `22-layer`

- main H2 effect:
  - fabrication-capability recovery remains secondary to standards and acceptance risk, especially where annular ring or testing numbers overlap class-based language
- practical implication:
  - H1 and H2 posture should remain conservative; many numbers belong in exclusion rather than recovery

### `24-layer`

- main H2 effect:
  - backdrill, impedance, registration, and high-layer measurement-capability promises remain governed buckets
- practical implication:
  - material and system-context support may improve article structure, but fabrication numerics still need dedicated capability governance

## Operating Notes For H2 Execution

- Recover numerics by bucket, not by blog.
- Do not use vendor laminate datasheets to back fabrication capability claims.
- Do not use internal process-vocabulary pages as proof of current numeric capability.
- When a source mixes capability posture with standards thresholds, default to `hold`.
- When a source mixes fabrication capability with SI interpretation, split the claim and recover only the fabrication portion if explicitly supported.

## Current Decision

H2 should proceed as governed capability-number inventory and policy work, not as broad numeric restoration.

The near-term reusable targets are the buckets with clear shop-capability shape and high blog reuse:

- `impedance_tolerance`
- `trace_space`
- `drill_and_via_geometry`
- `aspect_ratio`
- `backdrill_and_stub`

Everything else should remain held, split further, or excluded until narrower source policy exists.
