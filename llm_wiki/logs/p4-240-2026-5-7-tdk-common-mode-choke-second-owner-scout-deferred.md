# P4-240 TDK Common-Mode Choke Second-Owner Scout Deferred

Date: 2026-05-07
Parent state: `after P4-239`
Execution mode: `second_owner_scout_and_defer`

## Purpose

Test whether `EMC` should immediately land a second owner-backed `common-mode choke` source after the Murata reinforcement in `P4-239`.

This pass evaluates:

- generic TDK FAQ material for `Signal Line Common Mode Chokes/Filters`
- a narrower TDK application note for `10BASE-T1S`

The goal is to decide whether the next safe move is:

- `source_only`
- `source_plus_fact_delta`
- or
- `defer`

## Inputs Used

- `logs/p4-239-2026-5-7-common-mode-choke-vendor-mode-behavior-boundary-reinforcement.md`
- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`
- TDK FAQ pages:
  - `Why are common mode filters / chokes necessary?`
  - `What is the difference between common mode and differential mode?`
  - `What is differential insertion loss?`
  - `What is the difference between common mode impedance, differential mode impedance and characteristic impedance?`
- TDK application note:
  - `Common Mode Chokes and Chip Varistors for 10BASE-T1S`

## Evaluation Result

Decision:

- `defer`

No new local `source` or `fact` record is landed in this pass.

## Why Generic TDK FAQ Was Not Landed Now

The generic TDK FAQ set is real owner-backed material and would be additive at the vendor-coverage level.

However, at the current `EMC` lane state it does not justify a new local record yet because:

- the current Murata article already gives the strongest needed correction against the handbook's `differential current passes without attenuation` wording
- the current boundary card already has:
  - family distinction
  - intended-use vocabulary
  - vendor-scoped `Sdd21 / Scc21` framing
  - the warning that vendor reference heuristics are not universal thresholds
- the TDK FAQ set mostly adds parallel vocabulary and definition coverage rather than a materially stronger new boundary

In other words:

- the TDK FAQ cluster is useful
- but landing it immediately would add more indexing surface than actual new knowledge

## Why The 10BASE-T1S Note Was Not Landed

The `10BASE-T1S` note is even less suitable as the next general `EMC` move.

Reason:

- it is application-specific
- it is tied to automotive Ethernet context and `OPEN Alliance` framing
- it increases the risk of accidental overreach into:
  - interface-specific suitability
  - parasitic-capacitance limits
  - S-parameter targets
  - recommended parts
  - Ethernet-specific outcome claims

That note should be reconsidered only if a future lane explicitly needs:

- `10BASE-T1S`
- automotive Ethernet
- or a dedicated interface-scoped common-mode choke fact card

## Safe Conclusion Preserved Locally

After this scout, the safest active `EMC` posture remains:

- keep `Murata` plus `Coilcraft` as the current landed `common-mode choke` boundary stack
- keep `TDK` as a plausible future second-owner supplement, but not yet worth local record expansion
- keep `BLA3216A102SG4` closed at the existing blocker ceiling

## What This Pass Prevents

- adding a second-owner source merely because it exists
- expanding local index surface without increasing claim quality
- drifting from generic `EMC` boundary work into `10BASE-T1S` or automotive Ethernet application specificity

## Next Step

1. Do not land TDK common-mode-choke source material by default right now.
2. Reopen TDK only if:
   - a future prompt explicitly needs second-owner reinforcement beyond current Murata/Coilcraft wording, or
   - a narrower interface-scoped lane such as `10BASE-T1S` is intentionally opened.
3. Keep the default `EMC` continuation on higher-yield owner-backed lanes rather than on parallel-vendor duplication.
