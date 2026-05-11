# P4-242 A1 Capacitor Output-Capacitor Structure Exact-Data Landing

Date: 2026-05-07
Parent state: `after P4-241`
Execution mode: `narrow_a1_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` again on the `A1 capacitor` lane by landing a second real official exact-data artifact.

This pass targets handbook-adjacent capacitor-combination and transient-response discussion, but only through stronger owner-backed evidence with named parts and stated conditions.

## Inputs Used

- `logs/p4-241-2026-5-7-a1-capacitor-low-esl-and-insertion-loss-exact-data-landing.md`
- `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`
- official TDK `MLCC Solutions for Power Supply Circuits (Verification of Optimal Structures for Output Capacitors)` solution guide
- Murata official product-page scout for `GRM188R71C104KA01#`

## What Landed

### New source record

- `sources/registry/methods/tdk-mlcc-output-capacitor-structure-solution-guide.md`

Reason:

- it is an official TDK owner-backed source
- it gives a named-part MLCC output-capacitor example using `CGA6P1X7T0G107M250AC`
- it states explicit converter and load-transient conditions
- it prints exact summary values for fixed-load and rising-load voltage fluctuation
- it adds a narrow before/after phase-compensation example without forcing universal compensation language

### New exact-data fact card

- `facts/methods/tdk-mlcc-output-capacitor-structure-method-example.md`

Reason:

- this is a valid `method_scoped_exact_data` landing
- it gives the batch a second real `A1 capacitor` exact-data artifact rather than more boundary-only wording
- it keeps the data tied to vendor scope, named part, stated operating conditions, and one specific method example

## What Did Not Land

### Murata part-page scout remained a no-go

Murata's official page for `GRM188R71C104KA01#` is useful and should remain remembered as a future lane candidate because:

- it proves owner-hosted per-part metadata
- it exposes availability of owner-hosted `S parameter (S2P type)` data

It still did not qualify for a new exact-data card in this pass because:

- the page itself did not state the measurement conditions for the downloadable behavior data
- that leaves the exact-data scope too under-specified under the current admission policy

## What Remains Blocked

- handbook antiresonance peak numbers and frequency-band claims
- handbook generic package-to-ESL tables
- handbook universal `smaller ESL is better` rules
- generic polymer-versus-MLCC replacement rules
- generic compensation recipes or required phase-margin thresholds

## Result Status

- `A1 capacitor lane`:
  - `source_backed_fact_layer_partial`
  - `two_exact_data_artifacts_landed`
- artifact shape:
  - `vendor_scoped_named_part_method_examples_only`

## Why This Was The Right A1 Landing

- it learns real capacitor-structure and transient-response data from an official owner-backed source
- it gives later blog-writing agents named-part and condition-scoped numbers they can directly compose
- it avoids pretending that handbook capacitor-combination graphics are already admissible exact data

## Next Step

1. Reopen `A1` again only for:
   - a true official antiresonance example with named parts and stated conditions, or
   - a part-scoped impedance/S-parameter lane whose owner source also exposes enough measurement context.
2. Keep Murata part pages with downloadable `S2P` availability in the scout queue, but do not promote them until the measurement-context gap is closed.
