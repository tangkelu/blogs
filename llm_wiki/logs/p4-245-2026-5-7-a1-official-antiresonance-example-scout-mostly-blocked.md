# P4-245 A1 Official Antiresonance Example Scout Mostly Blocked

Date: 2026-05-07
Parent state: `after P4-244`
Execution mode: `a1_official_antiresonance_example_scout`

## Purpose

Test whether `/code/blogs/tmps/PCB资料` can now absorb a real official `A1 capacitor` antiresonance example with:

- named parts or named families
- stated setup or operating conditions
- recoverable exact values or printed comparison results

The target pressure came from the handbook's `Figure 3-12` and `Figure 3-15` style `parallel capacitor impedance / antiresonance` discussion.

## Inputs Used

- `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- `logs/p4-244-2026-5-7-murata-part-level-impedance-lane-verified-as-ready-but-not-landed.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`
- official TDK `Solution Guide: Replacing Electrolytic Capacitor with MLCC, Revised Guide`
- official Murata article `How can the mounting area be reduced? - Methods of using low-ESL capacitors -`

## Evaluation Result

Current result:

- `mostly_blocked_for_exact_antiresonance_landing`

No new antiresonance-specific exact-data fact card is landed in this pass.

## Why TDK Was A No-Go

The TDK `MLCC replace guide` remains valid owner-backed material for:

- `SRF`
- antiresonance vocabulary
- impedance-peak risk framing

It still did not qualify as the next `A1` exact-data artifact because:

- the page did not provide a clean named-part antiresonance example
- it did not provide a recoverable exact setup plus printed antiresonance result pair at the needed level
- it reinforces the already-landed boundary card more than it creates a new exact-data card

## Why Murata Was A No-Go For Antiresonance

The Murata low-ESL article is real and useful.

It gives recoverable values for:

- relative `ESL` comparison
- package/size examples
- component-count and area-reduction examples
- loop-impedance-oriented setup framing

It still did not qualify for the requested antiresonance artifact because:

- it is not a direct antiresonance or impedance-peak example
- it does not provide exact antiresonance peak data
- it does not provide exact named-part antiresonance setup/results in the form needed for this lane

## Safe Conclusion

- the official-source search did not yet recover a clean one-to-one replacement for the handbook antiresonance figure
- the current best official antiresonance coverage remains the already-landed boundary layer
- exact antiresonance numerics from the handbook remain blocked

## What This Pass Did Clarify

- the antiresonance lane is not empty because the boundary card is already real
- the missing piece is not general vendor vocabulary
- the missing piece is one stronger official example with:
  - named part or family scope
  - stated measurement or simulation conditions
  - printed exact comparison output or peak behavior in reusable form

## Next Step

1. Keep `official antiresonance example` as a valid future `A1` continuation lane.
2. Do not reopen handbook antiresonance numerics without that stronger official replacement.
3. In the near term, prefer the stronger fallback lane that actually has recoverable exact data now:
   - Murata `low-ESL / loop-impedance` method example
   - or a later re-opened Murata `part-level impedance` lane when the payload chain is reproducible.
