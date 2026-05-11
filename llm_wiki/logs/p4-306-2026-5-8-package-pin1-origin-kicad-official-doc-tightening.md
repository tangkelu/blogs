# P4-306 Package Pin-1 Origin KiCad Official Doc Tightening

Date: 2026-05-08
Parent lane: `P4-305`
Execution mode: `controller_owned_external_official_source_tightening`

## Purpose

Follow `P4-305` by checking whether an already-registered official KiCad documentation source can safely strengthen the `pin-1 / origin` lane without overstating it as package-owner or standards-owner authority.

## Inputs

- `sources/registry/methods/kicad-getting-started-guide.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- KiCad official documentation page already registered under `kicad-getting-started-guide`

## What Landed

### Existing official source widened for this lane

Updated:

- `sources/registry/methods/kicad-getting-started-guide.md`

What changed safely:

- the source record now explicitly captures that the KiCad guide documents a through-hole footprint convention with `pin 1` placed at `(0,0)`
- the source record now explicitly captures that the guide points to `KLC` as the basis for official KiCad symbol and footprint libraries

### Method-layer tightening

Updated:

- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

What changed safely:

- the method card now includes one official CAD-owner support point for guarded `origin / pin-1` convention wording
- the `pin 1 @ (0,0)` pattern is now treated as software-library convention support for through-hole footprints, not as universal package truth

## What Did Not Land

No new package-owner source, connector-owner source, or standards-owner rule landed in this pass.

Reason:

- KiCad is a CAD/library owner, not the owner of every package family or connector convention
- the guide supports controlled library convention and review posture, not universal origin defaults across all package families

## Updated Boundary

- `pin-1 / origin` lane: `source_backed_fact_layer_partial` with one official CAD-owner support point
- `through-hole pin 1 @ (0,0)`: now supported as guarded KiCad library convention
- `connector-origin defaulting`: still blocked
- `installation mark` conventions: still below standards-grade authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `package_owner_or_standards_owner_authority_still_needed`
