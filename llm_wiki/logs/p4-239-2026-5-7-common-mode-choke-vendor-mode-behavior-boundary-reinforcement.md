# P4-239 Common-Mode Choke Vendor Mode-Behavior Boundary Reinforcement

Date: 2026-05-07
Parent state: `after P4-235`
Execution mode: `minimal_owner_backed_boundary_reinforcement`

## Purpose

Tighten the `common-mode choke` wording boundary after `P4-235`.

This turn does not reopen handbook figures, ferrite-bead alias recovery, or a new exact-data family card.

It only adds a stronger owner-backed explanation source so future prompts do not drift back to the overly absolute handbook wording that `differential current passes without attenuation`.

## Inputs Used

- `logs/p4-220a-2026-5-7-emc-authority-recovery-queue-and-source-priority.md`
- `logs/p4-222-2026-5-7-emc-owner-curve-recovery-controller-integration.md`
- `logs/p4-223-2026-5-7-ferrite-bead-exact-part-recovery-blocked-at-family-equivalent-ceiling.md`
- `logs/p4-235-2026-5-7-emc-common-mode-choke-minimal-owner-curve-fact-integration.md`
- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`
- `facts/methods/coilcraft-lpd3015-common-mode-choke-family-exact-data.md`
- Murata official technical article:
  - `Characteristics of common mode choke coils for signal lines and how to choose one`

## What Landed

### New source record

- `sources/registry/methods/murata-common-mode-choke-signal-lines-characteristics-and-selection-article.md`

Why it landed:

- it is an owner-backed Murata technical article
- it explains common-mode choke behavior on differential signal lines through `differential mode insertion loss Sdd21` and `common mode insertion loss Scc21`
- it explicitly says real differential-mode signals are also attenuated to some extent
- it marks the `cutoff frequency at least 3 times the signal frequency` rule as a reference guideline rather than a universal threshold

### Narrow fact delta

Updated:

- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`

What changed:

- the card now has a stronger owner-backed correction against `differential current passes without attenuation` wording
- the card now carries Murata's vendor-scoped `Sdd21 / Scc21` insertion-loss framing
- the card now marks the `3x signal frequency` cutoff heuristic as vendor guidance only

## What Did Not Land

- no new `common-mode choke` exact-data fact card
- no new ferrite-bead exact-part recovery
- no reopening of `BLA3216A102SG4`
- no handbook-only curve promotion
- no universal interface-suitability, compliance, or wireless-performance claims

## Result Status

- `common-mode choke` lane:
  - `owner_backed_family_curve_recovered`
  - `minimal_exact_data_fact_landed`
  - `vendor_mode_behavior_boundary_reinforced`
- `ferrite bead` lane:
  - `exact_part_unresolved`
  - `family_equivalent_fallback_only`

## Why This Was The Right Next Step

- it advances the already recoverable `common-mode choke` lane without reopening blocked ferrite-bead alias work
- it improves downstream prompt safety where the current failure mode is wording drift, not missing family identity
- it stays within the exact-data admission policy because the new source is reused only as vendor-scoped method guidance, not as a universal rule set

## Next Step

1. Keep reusing `Coilcraft LPD3015` only when family-scoped exact data is actually needed.
2. Keep `BLA3216A102SG4` closed unless exact new Murata owner evidence appears.
3. If future prompts need more than vendor-scoped `Sdd21 / Scc21` framing, recover a second owner-backed common-mode choke application note before broadening wording.
