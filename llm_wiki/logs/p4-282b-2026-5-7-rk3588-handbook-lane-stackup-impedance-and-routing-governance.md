# P4-282B RK3588 Handbook Lane D2: Stackup Impedance And Routing Governance

Date: 2026-05-07
Parent: `P4-282`
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Execution mode: `claim_family_lane_learning_only`

## Purpose

Learn the `D2` bounded lane from the `194-page RK3588 handbook` as English canonical claim families only.

This log does not promote handbook numerics, tables, or formulas into `facts/`.

## Lane Scope

Indicative page cluster:

- `11-75`

Lane focus:

- stackup and impedance governance
- routing-rule governance
- via fanout and BGA escape
- differential and length-matching governance
- ultra-high-speed routing boundary families

## Safe Claim Families Learned

- stackup selection should be based on reference-plane adjacency, symmetry, and manufacturability
- impedance planning is stackup-dependent and must be recalculated for the selected board structure
- routing-rule setup depends on fabricator capability and signal class
- crosstalk governance relies on spacing, reference continuity, and adjacent-layer planning
- route continuity should avoid sharp corners, unnecessary stubs, and abrupt width changes
- differential routing requires symmetry, coupling preservation, and nearby return-via support
- via governance is a channel-management problem, not a numeric cookbook
- BGA escape planning is about preserving escape corridors and plane continuity
- length matching is a timing-alignment technique with orderly local meanders only
- ultra-high-speed routing adds pad/via parasitic, glass-weave, and transition-optimization families

## Blocked Classes

- all exact impedance targets, widths, spaces, board thicknesses, dielectric builds, and copper weights
- all stackup tables and derived geometry tables
- all spacing thresholds, current-carry heuristics, and via-size recommendations
- all length-matching dimensions and formula-like geometry variables
- all `8Gbps+` design-rule values
- all EVB-scoped reference dimensions and vendor/tool example outputs

## Preservation Notes

Preserve locally as evidence-bearing references:

- stackup and impedance tables and figures from pages `13-25`
- routing governance figures from pages `41`, `46-49`
- return-via and BGA escape figures from pages `52-59`, `63-67`
- ultra-high-speed local optimization figures and tables from pages `70-75`

Exclude as reusable authority:

- repeated promo footer
- Rockchip-specific recipes presented as universal
- vendor tool output screenshots
- pages `26-37` that belong to adjacent placement material

## Status

`D2` is complete at claim-family level only. It is ready for later exact-data gating, but no numeric or table promotion was performed.

