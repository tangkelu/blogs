# P4-246 A1 Murata Low-ESL Loop-Impedance Fallback Landing

Date: 2026-05-07
Parent state: `after P4-245`
Execution mode: `a1_fallback_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` again on the `A1 capacitor` lane after the official antiresonance-example scout remained mostly blocked.

This pass intentionally takes the strongest current fallback that still yields real exact data:

- Murata official `low-ESL / loop-impedance` method example

## Inputs Used

- `logs/p4-245-2026-5-7-a1-official-antiresonance-example-scout-mostly-blocked.md`
- `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`
- official Murata article `How can the mounting area be reduced? - Methods of using low-ESL capacitors -`

## What Landed

### New source record

- `sources/registry/methods/murata-low-esl-capacitors-loop-impedance-article.md`

Reason:

- it is an official Murata owner-backed English article
- it gives recoverable structure-scoped low-ESL comparison values
- it gives stated setup framing around `IC/LSI` bypass and `loop impedance`
- it gives recoverable component-count and board-area example results

### New exact-data fact card

- `facts/methods/murata-low-esl-loop-impedance-method-example.md`

Reason:

- this is a valid `method_scoped_exact_data` landing
- it creates a real fallback exact-data artifact when a cleaner official antiresonance example is not yet recoverable
- it adds reusable owner-backed data for low-ESL structure discussion without overstating antiresonance coverage

## What Did Not Land

- no official antiresonance peak values were landed
- no handbook antiresonance numerics were promoted
- no universal capacitor-count reduction rule was promoted

## Result Status

- `A1 capacitor lane`:
  - `source_backed_fact_layer_partial`
  - `four_exact_data_artifacts_landed`
- current best exact-data mix:
  - TDK `YFF` low-ESL / insertion-loss examples
  - TDK output-capacitor structure example
  - Murata low-signal measurement-context example
  - Murata low-ESL / loop-impedance example

## Why This Was The Right Fallback

- it learns more real vendor-backed capacitor behavior into the corpus right now
- it preserves momentum without pretending the blocked antiresonance lane is solved
- it gives later blog-writing agents a stronger base for high-frequency capacitor discussion than the handbook alone

## Next Step

1. Keep `official antiresonance example` open as a future lane, but do not force it without stronger source evidence.
2. Keep Murata `part-level impedance` open as a `ready_but_not_landed` lane for future reproducible recheck.
3. After this fallback, the next best move may be to shift from `A1` to another high-yield blocked exact-data lane if `A1` continues to stall on official antiresonance numerics.
