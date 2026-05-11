# P4-223 Ferrite-Bead Exact-Part Recovery Blocked At Family-Equivalent Ceiling

Date: 2026-05-07
Parent lane: `P4-222 ferrite-bead exact-part recovery`
Execution mode: `owner_only_blocker_closeout`

## Purpose

Close the current `BLA3216A102SG4` exact-part recovery attempt at a clear blocker state instead of leaving it as an open-ended scout.

This log records that the current Murata owner-only recovery ceiling is:

- `exact_part_unresolved`
- `family_equivalent_fallback_only`

## Inputs Used

- `logs/p4-215a2-2026-5-6-emc-lane-a2-ferrite-bead-vs-common-mode-choke.md`
- `logs/p4-220a-2026-5-7-emc-authority-recovery-queue-and-source-priority.md`
- `logs/p4-222-2026-5-7-emc-owner-curve-recovery-controller-integration.md`
- `facts/methods/ferrite-bead-vendor-guidance-boundary.md`
- Murata owner endpoint checks already recorded during `P4-222`

## What Was Rechecked

The current pass rechecked only Murata owner surfaces and adjacent Murata naming variants, including:

- `BLA3216A102SG4`
- `BLA3216A102S`
- `BLA3216A102SG`
- current-public `BLA31AG102SN4#` fallback surfaces

## Result

No Murata owner-backed alias, archived exact datasheet, or published cross-reference was recovered that proves:

- `BLA3216A102SG4`
- and
- `BLA31AG102SN4#`

are the same exact part.

Additional owner-backed evidence from the current pass:

- Murata owner API returned no current-public hit for `BLA3216A102SG4#`
  - `cross-categories` result:
    - empty
  - `products/search` result:
    - `totalNum: 0`
- Murata owner API did return a current-public live hit for `BLA31AG102SN4#`
  - this confirms only that the fallback part exists on current Murata owner surfaces
  - it does not establish an alias or exact historical equivalence

What remains true:

- `BLA31AG102SN4#` is still the strongest current-public Murata family-equivalent fallback candidate
- that fallback remains useful only when it is explicitly labeled as:
  - `family_equivalent_fallback_only`
- exact-part curve promotion for `BLA3216A102SG4` remains blocked

## Safe Local Posture

Keep the ferrite-bead lane at:

- `exact_part_recovery_not_reached`
- `exact_part_unresolved`
- `family_equivalent_fallback_only`

Safe local reuse:

- Murata ferrite-bead FAQ vocabulary
- Murata family-equivalent fallback clarification
- explicit statement that no owner-backed exact alias has yet been recovered

Unsafe and still blocked:

- presenting `BLA31AG102SN4#` as an exact replacement for `BLA3216A102SG4`
- promoting the handbook ferrite-bead curve as exact part data
- inferring exact `Z / R / X` curve ownership for `BLA3216A102SG4`
- universal attenuation, filter-selection, or EMC-outcome claims

## Decision

Do not continue spending immediate effort on this exact-part scout unless one of the following appears:

1. a Murata owner alias or archived exact-part cross-reference
2. a Murata owner datasheet or archive page explicitly using `BLA3216A102SG4`
3. a controlled internal legacy source that can be admitted under a separate policy lane

Relevant owner endpoints rechecked in this closeout include:

- `https://www.murata.com/en-us/products/productdetail?partno=BLA3216A102SG4%23`
- `https://pim.murata.com/en-us/pim/details/?partNum=BLA3216A102SG4%23`
- `https://pimapi.murata.com/public/api/pim/v1/products/search/cross-categories?partNum=BLA3216A102SG4%23&languageRegion=en-us`
- `https://pimapi.murata.com/public/api/pim/v1/products/search/cross-categories?partNum=BLA3216A102SG4%23&languageRegion=en-global`
- `https://www.murata.com/en-us/products/productdetail?partno=BLA31AG102SN4%23`
- `https://pim.murata.com/en-us/pim/details/?partNum=BLA31AG102SN4%23`
- `https://pimapi.murata.com/public/api/pim/v1/products/search/cross-categories?partNum=BLA31AG102SN4%23&languageRegion=en-us`
- `https://pimapi.murata.com/public/api/pim/v1/products/search/cross-categories?partNum=BLA31AG102SN4%23&languageRegion=en-global`

Until then, treat the ferrite-bead exact-part lane as closed at the current ceiling.

## Next Step

- keep `common-mode choke` recovery active where owner-backed family curves already exist
- keep ferrite-bead exact-part recovery closed unless exact new owner evidence appears
