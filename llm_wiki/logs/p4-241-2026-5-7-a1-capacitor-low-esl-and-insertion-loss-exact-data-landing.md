# P4-241 A1 Capacitor Low-ESL And Insertion-Loss Exact-Data Landing

Date: 2026-05-07
Parent state: `after P4-240`
Execution mode: `narrow_a1_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` beyond `EMC common-mode choke` by landing one real `A1 capacitor` exact-data artifact.

This pass targets the handbook's `package / ESL` and `insertion-loss` candidate class, but only through stronger owner-backed evidence.

## Inputs Used

- `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- `logs/p4-210a-2026-5-6-emc-source-lane-capacitor-parasitic-resonance.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`
- official TDK `YFF Series` solution guide

## What Landed

### New source record

- `sources/registry/methods/tdk-yff-series-low-esl-and-insertion-loss-solution-guide.md`

Reason:

- it is an official TDK owner-backed source
- it gives a printed `low-ESL` comparison by structure
- it gives named-part example results for `YFF18AC1A104M` and `YFF18AC0G106M`
- it gives explicit `insertion loss`, `Vpp`, and `dBuVmax` example values under stated converter conditions

### New exact-data fact card

- `facts/methods/tdk-yff-series-low-esl-and-insertion-loss-method-example.md`

Reason:

- this is a valid `method_scoped_exact_data` landing
- it converts one `A1` candidate family into reusable exact data without promoting the handbook's generic package/ESL table
- it keeps the data tied to vendor scope, named parts, and stated test/setup conditions

## What Remains Blocked

- the handbook `Table 3-1` generic package-to-ESL table as a reusable cross-vendor fact
- the handbook generic insertion-loss comparison across unnamed capacitor technologies
- dielectric recommendations such as `X7R / Y5V / Z5U`
- universal `small ESL is always better` rules
- generic multi-capacitor value-pair recipes from the handbook
- exact antiresonance peak frequencies from the handbook figures

## Result Status

- `A1 capacitor lane`:
  - `source_backed_fact_layer_partial`
  - `one_exact_data_artifact_landed`
- artifact shape:
  - `vendor_scoped_structure_and_named_part_example_only`

## Why This Was The Right A1 Landing

- it learns real numbers from official owner-backed material
- it lands data that actually resembles the user's requested `图 / 参数 / 曲线 / 表格` direction
- it avoids the unsafe shortcut of copying the handbook's generic package/ESL table into the knowledge base

## Next Step

1. Reopen `A1` again only for:
   - a method-scoped antiresonance example with stronger published curve-specific detail, or
   - a family-scoped MLCC part/source lane with explicit SRF / impedance data.
2. Keep the handbook generic capacitor tables and recipes blocked unless exact official family or part provenance is recovered.
