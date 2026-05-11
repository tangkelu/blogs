# P4-243 A1 Capacitor Frequency-Characteristic Measurement-Context Landing

Date: 2026-05-07
Parent state: `after P4-242`
Execution mode: `narrow_a1_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` again on the `A1 capacitor` lane by landing a third official exact-data artifact.

This pass targets the handbook's pressure to talk about capacitor frequency curves and impedance behavior, but it only lands a narrower owner-backed SimSurfing measurement-context example rather than pretending the handbook's antiresonance curve numbers are already admissible.

## Inputs Used

- `logs/p4-242-2026-5-7-a1-capacitor-output-capacitor-structure-exact-data-landing.md`
- `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`
- official Murata `The capacitance-frequency characteristics displayed by SimSurfing differ from the nominal capacitance. What is the reason for this?` FAQ

## What Landed

### New source record

- `sources/registry/methods/murata-mlcc-simsurfing-capacitance-frequency-measurement-context-faq.md`

Reason:

- it is an official Murata owner-backed source
- it gives a named-part MLCC example `GRM155B30J225KE95`
- it explicitly states that SimSurfing `capacitance-frequency` data is measured at low signal voltage
- it prints a nominal-versus-curve example and an AC-voltage example at `10 mVrms`

### New exact-data fact card

- `facts/methods/murata-mlcc-simsurfing-low-signal-measurement-method-example.md`

Reason:

- this is a valid `method_scoped_exact_data` landing
- it adds real curve-reading and low-signal measurement-context knowledge for later blog writing
- it converts one recurring capacitor-curve ambiguity into a reusable owner-backed local artifact

## What Did Not Land

- no handbook antiresonance peak frequency was promoted
- no universal dielectric ranking was promoted
- no generic `package -> impedance` or `package -> ESL` rule was promoted

## What Remains Blocked

- handbook antiresonance peak numbers and frequency-band claims
- handbook generic package-to-ESL tables
- universal dielectric-family selection rules
- unnamed-part SRF or antiresonance values

## Result Status

- `A1 capacitor lane`:
  - `source_backed_fact_layer_partial`
  - `three_exact_data_artifacts_landed`
- artifact shape:
  - `vendor_scoped_named_part_method_examples_only`

## Why This Was The Right A1 Landing

- it adds exact named-part measurement context instead of rephrasing generic handbook curve lore
- it gives future writing agents a safe way to talk about why SimSurfing `capacitance-frequency` plots can sit below nominal capacitance
- it keeps the corpus moving toward real capacitor-curve literacy without overclaiming antiresonance numbers

## Next Step

1. Reopen `A1` next only for:
   - an official antiresonance example with named parts and stated conditions, or
   - a part/family impedance lane with explicit measurement setup and downloadable owner data.
2. Keep blocking handbook antiresonance numerics until a stronger one-to-one official replacement appears.
