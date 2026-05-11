---
fact_id: "methods-clock-source-termination-and-crystal-routing-emc-boundary"
title: "Clock source termination and crystal routing may be reused as a clock-specific EMC boundary, not as a timing-closure recipe"
topic: "Clock source termination and crystal routing EMC boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_clock_layout_and_crystal_routing_boundary"
canonical_unit_policy: "Preserve wording such as series termination close to source, solid ground plane under clock traces, no routing near or under the clock source, keep crystal close to the device, keep traces short, avoid split crossing, and provide return continuity on layer change. Do not normalize this into exact resistor values, exact clock lengths, exact 1-inch thresholds, exact 5W spacing, or universal EMC-pass rules."
source_ids:
  - "sitime-an10006-best-design-and-layout-practices"
  - "ti-clock-source-series-termination-and-ground-plane-layout"
  - "ti-high-speed-layout-guidelines"
tags: ["clock", "series-termination", "crystal", "oscillator", "ground-plane", "return-path", "emc", "methods"]
---

# Canonical Summary

> Current public owner-backed guidance is strong enough to support one narrow clock-specific EMC boundary: clock or crystal sources should stay close to their associated device, source-series termination should sit close to the driving source when that topology is used, clock traces should remain short and direct with a solid ground/reference plane underneath, unrelated routing should stay away from or out from under the clock-source region, and any layer change should preserve return continuity rather than crossing split reference regions. This supports guarded clock-layout review wording only. It does not authorize resistor values, exact clock-distance rules, timing-closure claims, or EMC-pass guarantees.

## Stable Facts

- SiTime supports placing the clock source close to the load and keeping clock traces short.
- SiTime supports placing source-series termination close to the oscillator or resonator output for single-ended clock routing.
- SiTime supports avoiding unnecessary bends or branching on clock traces.
- SiTime supports keeping clock routing away from board edges and noisy or high-current modulated regions.
- SiTime supports using a continuous ground plane under signal layers in multilayer boards.
- TI supports placing source-series termination close to the clock source.
- TI supports keeping a solid ground plane under clock traces.
- TI supports avoiding routing unrelated signals near or under the clock source region.
- TI high-speed layout guidance supports avoiding split reference crossings and preserving return continuity when sensitive signals change layers.

## Exact Data Scope

- exact for:
  - source-series termination close to the driver or clock source
  - clock trace over a solid ground/reference plane
  - clock or oscillator placed close to the relevant load or IC
  - short and direct clock or crystal routing
  - avoid unnecessary bend or branch-first routing on clock paths
  - no unrelated routing near or under the clock source region
  - avoid split crossing and preserve return continuity on layer change
- not exact for:
  - exact resistor values
  - exact line lengths or board-edge distances
  - exact spacing rules such as `5W`
  - exact shielding-via counts or ground-fence recipes
  - timing margin, jitter, EMI-pass, or SI-signoff outcomes

## Conditions And Methods

- Use this card when a prompt needs safe wording for `clock routing`, `series termination near source`, `crystal placement`, or `oscillator keepout`.
- Keep the language at boundary level:
  - source termination near the driver
  - solid reference plane under clock routing
  - clock or crystal kept close to the relevant load or IC
  - short and direct routing
  - avoid unnecessary bends or branching
  - no unrelated routing under or near the clock source
  - no split crossing for clock paths
  - preserve return continuity on layer change
- Pair this card with broader return-path cards only when the draft also needs non-clock generic routing context.

## Safe Blog Usage

- Explain that clock EMC review is more specific than generic routing discipline because it also cares about the source region and source-side termination posture.
- Explain that the clock or crystal source region should be treated as a local quiet area rather than ordinary routing space.
- Explain that source-side termination, short routing, and stable reference handling belong to the same clock-review family.
- Explain that clock paths should avoid unnecessary bend-heavy or branch-first routing near the source region.
- Explain that clock paths should avoid split crossings and preserve return continuity when changing layers.

## Limits And Non-Claims

- This card does not authorize exact series-resistor values or exact placement distances.
- It does not authorize exact clock-spacing, shielding, or ground-via recipes.
- It does not authorize oscillator start-up, jitter, timing closure, or EMI-pass claims.
- It does not prove that any specific clock layout is production-ready by itself.
