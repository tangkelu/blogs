---
fact_id: "methods-power-pin-and-decoupling-dedicated-plane-connection-boundary"
title: "Power-pin and decoupling guidance may be reused only as a dedicated plane-connection and non-shared-via boundary"
topic: "Power-pin and decoupling dedicated plane connection boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_power_pin_ground_pin_and_decoupling_dedicated_plane_connection_boundary"
canonical_unit_policy: "Preserve wording such as each power or ground pin having its own dedicated connection into the plane, decoupling capacitor power and ground terminals using dedicated vias or direct local plane entry, avoiding shared vias where they add spreading inductance, and connecting vias directly at capacitor lands rather than through extra trace segments. Do not normalize this into exact via counts, one-via-per-pin universals, or rail-specific sufficiency claims."
source_ids:
  - "intel-pdn-dedicated-power-ground-pin-connections"
  - "amd-ug583-dedicated-via-and-land-connection-boundary"
tags: ["power-pins", "ground-pins", "decoupling", "dedicated-vias", "shared-vias", "plane-connection", "spreading-inductance", "methods"]
---

# Canonical Summary

> Current public semiconductor-owner guidance is strong enough to support one narrow local power-connection boundary: power pins, ground pins, and decoupling capacitor terminals should enter the relevant plane structure through dedicated local connections rather than through shared-via bottlenecks or extra trace segments between lands and vias. This supports guarded layout-review wording only. It does not authorize exact via counts, exact via geometry, universal one-via-per-pin doctrine, or rail-specific sufficiency claims.

## Stable Facts

- Intel supports each power or ground pin having its own dedicated connection into the plane structure it uses.
- Intel also supports decoupling capacitor power and ground terminals using dedicated vias rather than shared vias, because shared vias add spreading inductance.
- AMD supports connecting decoupling vias directly to capacitor lands rather than through a section of trace.
- AMD also treats sharing vias across multiple decoupling capacitors as poor practice in this local inductive-cleanup context.

## Exact Data Scope

- exact for:
  - dedicated local plane entry for power pins or ground pins
  - dedicated local plane entry for decoupling capacitor terminals
  - avoiding shared vias where they add spreading inductance in local power connections
  - avoiding extra trace segments between capacitor lands and their vias
- not exact for:
  - exact via counts or `one via per pin` universal rules
  - exact via diameter, antipad, drill, fill, or cap rules
  - exact copper width, current capacity, or voltage-drop closure
  - exact PDN, transient, EMI, or rail-specific sufficiency outcomes
  - RK3588-specific recipes or exact CPU-rail fanout patterns

## Conditions And Methods

- Use this card when a prompt needs safe wording for `power-pin plane entry`, `dedicated breakout via`, `non-shared decoupling via`, or `direct land-to-via decoupling connection`.
- Keep the language at boundary level:
  - each power or ground pin should have its own dedicated connection into the relevant plane structure
  - decoupling capacitor terminals should use dedicated vias or direct local plane entry
  - shared vias are discouraged because they add spreading inductance
  - avoid a trace segment between a decoupling capacitor land and its via when owner guidance treats that trace as added inductive burden
- Pair this card with `methods-processor-power-pin-local-decoupling-capacitor-placement-boundary` only when the draft also needs the separate `place it near the load` posture.
- Pair this card with `methods-current-carrying-trace-width-and-copper-boundary` only when the draft separately needs conductor-sizing or copper-width consequences.
- Pair this card with `methods-via-transition-return-path-continuity-boundary` only when the draft separately needs signal-layer return-path cleanup language.

## Safe Blog Usage

- Explain that local decoupling quality is not only a placement problem but also a dedicated plane-entry problem.
- Explain that shared vias can add spreading inductance in the local power connection and are therefore discouraged in owner guidance.
- Explain that direct land-to-via connection is part of keeping the local inductive path tight.
- Explain that this lane supports guarded connection posture, not proof of PDN closure or exact via recipes.

## Limits And Non-Claims

- This card does not authorize exact via counts, exact via sizes, or universal one-via-per-pin doctrine.
- It does not authorize exact fanout geometry, exact copper widths, or exact current-capacity rules.
- It does not authorize RK3588 rail-specific sufficiency, exact voltage-drop closure, or exact package-shadow recipes by itself.
- It does not prove transient-response, EMI, EMC, compliance, or production-readiness outcomes by itself.

## Source Links

- https://www.intel.com/content/www/us/en/docs/programmable/683883/current/general-rules-for-capacitor-and-power.html
- https://docs.amd.com/r/en-US/ug583-ultrascale-pcb-design/Possibility-2-Parasitic-Inductance-of-Planes-Vias-or-Connecting-Traces
