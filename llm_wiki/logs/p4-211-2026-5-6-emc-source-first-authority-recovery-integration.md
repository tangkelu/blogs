# P4-211 EMC Source-First Authority Recovery Integration

Date: 2026-05-06

## Purpose

Integrate the first source-recovery pass that follows `P4-210` for the `85页 PCB设计EMC设计指导书` residual lanes.

This pass aims to promote only those narrow boundaries that now have direct official or manufacturer-backed support. It does not authorize handbook numerics, cookbook formulas, or compliance claims.

## Inputs

- `logs/p4-210a-2026-5-6-emc-source-lane-capacitor-parasitic-resonance.md`
- `logs/p4-210b-2026-5-6-emc-source-lane-common-mode-choke-vs-ferrite-bead.md`
- `logs/p4-210c-2026-5-6-emc-source-lane-transmission-line-via-return-slot.md`
- Existing return-path / impedance facts and source records already landed under `facts/methods/*return-path*`, `*impedance*`, and `sources/registry/methods/ti-high-speed-layout-guidelines.md`

## What Landed

### Capacitor parasitic / resonance lane

Landed as reusable local knowledge:

- `sources/registry/methods/murata-capacitor-impedance-frequency-faq.md`
- `sources/registry/methods/tdk-mlcc-antiresonance-decoupling-guide.md`
- `sources/registry/methods/analog-devices-decoupling-capacitors-on-power-pins.md`
- `facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md`

Reason:

- the combined source mix is strong enough for `frequency-dependent impedance`, `ESR`, `SRF`, `antiresonance`, and guarded `decoupling / bypass / bulk` role language
- the combined source mix is not strong enough for universal value ladders, dielectric choices, or exact placement formulas

### Common-mode choke vs ferrite bead lane

Landed as reusable local knowledge:

- `sources/registry/methods/murata-common-mode-choke-coils-overview.md`
- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`

Reason:

- the existing Murata ferrite-bead records plus the new common-mode choke record are strong enough to preserve `separate component family` vocabulary and `common-mode noise` intent
- the source mix remains vendor-scoped and does not justify universal selection or placement rules

## What Did Not Land As New Fact Layer

### Transmission-line / via-return-path / slot-crossing lane

No new fact card was created in this pass.

Reason:

- the local corpus already has narrow source-backed support for:
  - `reference-plane continuity`
  - `return-current path discipline`
  - `avoid splits / slots under critical routes`
  - `TDR method identity`
  - guarded `microstrip` / `stripline` vocabulary
- the unresolved gap is more specific:
  - via-parasitic and slot-bridging detail still need stronger exact authority before another dedicated fact card would add net value

Current posture:

- keep reusing:
  - `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
  - `facts/methods/rf-transmission-line-structure-vocabulary-boundary.md`
  - `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
  - `facts/methods/controlled-impedance-tdr-verification-posture.md`
- do not promote handbook formulas, via parasitic numbers, or slot-crossing cookbook rules yet

## Next Recommended Moves

1. Recover one stronger public or vendor source for via-transition parasitic / return-path handling if a future prompt needs more than today's continuity-level wording.
2. Recover one stronger source for slot-crossing / bridging / quiet-ground handling if a future prompt needs more than today's split-avoidance posture.
3. Keep `RF shield-cavity` and `safety spacing` lanes queued behind these narrower EMC/source lanes unless publication demand changes.

## Final Status

- `P4-210A capacitor lane`: `source_backed_fact_layer_partial`
- `P4-210B common-mode-choke lane`: `source_backed_fact_layer_partial`
- `P4-210C transmission-line/via/slot lane`: `existing_fact_layer_reused_only`
