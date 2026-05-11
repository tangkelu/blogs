# P4-244 Murata Part-Level Impedance Lane Verified As Ready But Not Landed

Date: 2026-05-07
Parent state: `after P4-243`
Execution mode: `a1_part_level_impedance_recheck`

## Purpose

Test whether the next `A1 capacitor` continuation can safely land a Murata `part-level impedance` artifact from:

- official Murata product detail page
- official Murata MLCC `S-parameter measurement conditions` page
- official Murata FAQ describing downloadable frequency-characteristic / `CSV` style access

The goal of this pass is not to force a landing. The goal is to decide whether the current source chain is strong enough and reproducible enough to create a new exact-data card now.

## Inputs Used

- `logs/p4-242-2026-5-7-a1-capacitor-output-capacitor-structure-exact-data-landing.md`
- `logs/p4-243-2026-5-7-a1-capacitor-frequency-characteristic-measurement-context-landing.md`
- `policies/exact-data-admission-policy.md`
- official Murata `S-parameter Measurement Conditions` page
- official Murata FAQ `char/0053`
- previously scouted Murata product-detail target:
  - `GRM188R71C104KA01#`

## What Was Verified

### Verified as strong enough

- Murata's official `S-parameter Measurement Conditions` page is real, owner-backed, and specific enough to support setup vocabulary such as:
  - land-pattern-based measurement framing
  - named analyzer / calibration method context
  - `2 port shunt mode`
  - frequency-range framing
- Murata FAQ `char/0053` is strong enough to support the claim that Murata exposes downloadable electrical-characteristic data through official tools such as SimSurfing

### Not yet strong enough for landing in this pass

The missing piece is not vendor authority. The missing piece is a stable, directly re-verifiable local capture of the exact part-level payload chain for the target part in the current execution environment.

Why it stayed below landing:

- the product-detail page and its downloadable payload path were not stably reproducible in this pass
- that means the controller can describe the lane as `ready_to_reopen`
- but it should not yet create a new `source` or `fact` that pretends the exact part-level payload was fully re-verified now

## Decision

Decision:

- `ready_but_not_landed`

This is not a policy blocker.

This is a reproducibility blocker for this exact pass.

## Safe Local Conclusion

- Murata part-level impedance remains a valid next-step lane
- the strongest safe shape remains:
  - `product detail page`
  - plus `S-parameter measurement conditions`
  - plus exact owner-hosted payload or directly quoted product-side behavior data
- until that full chain is re-verified in one pass, do not promote it into a new exact-data fact

## What This Pass Prevents

- treating a previously observed or partially observed Murata product page as fully re-verified when the current pass did not stably recover the exact payload chain
- landing a local fact card that would exceed the current evidence actually rechecked in this run
- confusing `lane is promising` with `artifact is landed`

## Next Step

1. Keep Murata `part-level impedance` in the `A1` next-step queue.
2. Reopen it only when the exact product page plus payload chain can be re-verified in one pass.
3. Until then, prefer the next official `antiresonance example with named parts + conditions` if it is easier to land cleanly.
