# P4-307 Package BGA Official Replacement Route Integration

Date: 2026-05-08
Parent lane: `P4-306`
Execution mode: `controller_owned_route_integration`

## Purpose

Integrate the already-landed package-owner BGA exact-data cards back into the active `package` governance route so the `PCB资料` handbook page-28 blocked table has an explicit official replacement path inside current `llm_wiki` navigation.

## Inputs

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md`
- `facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md`
- `facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`
- `logs/p4-299-2026-5-8-pcb-ziliao-package-blocked-exact-data-evidence-batch-2.md`

## What Landed

### Package-process route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`

What changed safely:

- the process map now includes an explicit `Exact-Geometry Route`
- the map now points BGA/CSP exact-geometry needs to the already-landed `NXP`, `TI`, and `Microchip` package-owner cards
- the route explicitly keeps those cards vendor-scoped and blocks any universal cross-vendor rewrite

### Method-boundary routing integration

Updated:

- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

What changed safely:

- the boundary card now gives concrete in-repo escape hatches for exact BGA/CSP geometry instead of stopping at a generic `route to stronger authority` instruction

## What Did Not Land

No new exact-data source or fact card landed in this pass.

Reason:

- the needed official replacements were already present in the repo
- the missing work was route integration, not fresh source recovery

## Updated Boundary

- `page-28 handbook BGA table`: still `blocked_evidence`
- official replacement route: now explicit and discoverable through current package-governance navigation
- `1.50 mm` and `0.75 mm` residual pitch classes: still not replaced by current owner cards

## Final Status

- lane result:
  - `route_integration_landed`
- continuation state:
  - `residual_pitch_classes_and_non_bga_authority_gaps_still_open`
