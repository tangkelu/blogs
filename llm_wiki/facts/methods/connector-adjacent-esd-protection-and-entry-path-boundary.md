---
fact_id: "methods-connector-adjacent-esd-protection-and-entry-path-boundary"
title: "Connector-adjacent ESD protection may be reused as an entry-path and short-discharge boundary, not as a universal rule table"
topic: "Connector-adjacent ESD protection and entry-path boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_esd_layout_boundary"
canonical_unit_policy: "Preserve source wording such as close to the connector, other entry point, short path, and protected IC. Do not normalize this into exact keepout numbers, via-count rules, or compliance thresholds."
source_ids:
  - "st-an5686-pcb-layout-tips-to-maximize-esd-protection-efficiency"
  - "ti-slva680-esd-protection-layout-guide"
  - "nexperia-pesd-layout-close-to-connector-boundary"
  - "ti-high-speed-layout-guidelines"
  - "analog-devices-mixed-signal-pcb-layout-guidelines"
tags: ["esd", "connector", "entry-point", "tvs", "return-path", "ground", "pcb-layout", "methods"]
---

# Canonical Summary

> Current public owner-backed guidance is strong enough to support one narrow ESD layout boundary: place the protection element close to the connector or other external entry point so the discharge or overvoltage path is intercepted early, route from the source to the protection element before the protected IC, keep the local reference / return path continuous and short, and keep exposed protected traces away from clean unprotected traces. This supports guarded board-review wording only. It does not authorize exact geometry, via-count, resistor-value, capacitor-value, or compliance-pass claims.

## Stable Facts

- ST states that the protection device should be placed as close as possible to the ESD source or connector.
- ST states that routing should go from the ESD source to the protection component and then to the chip to protect.
- ST states that protected tracks exposed to ESD should be separated from other clean tracks.
- TI states that the TVS should be placed near the connector as design rules allow.
- TI states that the protected line should run directly from the ESD source to the TVS and that stubs between the TVS and the protected line should be avoided.
- TI states that unprotected traces should not be adjacent to the exposed path between the ESD source and the TVS.
- Nexperia explicitly says the protection should be close to the connector or other entry point.
- Nexperia explicitly frames this placement as a way to prevent overvoltage from reaching the protected IC before the protection element acts.
- TI supports keeping return current local and continuous, especially when routing or layer changes could enlarge loop area.
- ADI supports treating board-layer planning and return-path continuity as upstream layout constraints rather than afterthought routing cleanup.

## Exact Data Scope

- exact for:
  - connector-adjacent or entry-point-adjacent ESD-protection placement wording
  - `ESD source -> protection -> protected IC` routing order
  - no-stub / no-branch-first routing posture between source and protection
  - short-entry-path / early-intercept framing before the protected IC
  - exposed-trace separation from nearby clean unprotected traces
  - local reference / return continuity as supporting layout posture
- not exact for:
  - exact distances from connector to TVS
  - exact ground-via counts or stitching intervals
  - exact series-resistor or capacitor values
  - IEC pass levels, surge guarantees, or EMC certification outcomes

## Conditions And Methods

- Use this card when a prompt needs safe wording for interface-entry ESD layout review.
- Keep the language at layout-boundary level:
  - protection close to the connector or other entry point
  - route from source to protection and then to the protected IC
  - short and direct exposure path before the protected IC
  - separation between exposed protected traces and clean unprotected traces
  - local return / reference continuity
  - avoid drifting into universal recipe language

## Safe Blog Usage

- Explain that connector-adjacent ESD protection is a placement and path-control topic, not only a component-selection topic.
- Explain that the protection device should intercept the event near the entry point rather than after a longer on-board exposure path.
- Explain that the line should reach the protection path before it reaches the protected IC, and avoid branch-first or stub-first routing language.
- Explain that ESD-exposed protected traces should be kept away from nearby clean unprotected traces when describing coupling-risk posture.
- Explain that local reference continuity matters because the clamp path is only part of the layout story.

## Limits And Non-Claims

- This card does not authorize exact connector-to-TVS length limits.
- It does not authorize exact via-count, keepout, or stitching rules.
- It does not authorize component values, package choices, or compliance claims.
- It does not prove that any specific layout passes IEC, surge, EMI, or field-reliability testing.
