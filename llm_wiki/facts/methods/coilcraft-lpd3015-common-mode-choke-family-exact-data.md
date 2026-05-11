---
fact_id: "methods-coilcraft-lpd3015-common-mode-choke-family-exact-data"
title: "Coilcraft LPD3015 common-mode choke family exact data is reusable only at family-scoped and part-row-scoped level"
topic: "Coilcraft LPD3015 common-mode choke family exact data"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "coilcraft-lpd3015-common-mode-chokes-datasheet"
tags: ["common-mode-choke", "coilcraft", "lpd3015", "exact-data", "common-mode", "differential-mode", "impedance-curve", "attenuation-curve"]
---

# Canonical Summary

> Coilcraft's official `LPD3015 Series` datasheet is strong enough to support a narrow exact-data layer for one named common-mode choke family: the local corpus may reuse the published family and part identities, the datasheet's directly tabulated electrical fields and condition notes, and the existence of both `common-mode` and `differential-mode` curves on the same owner-backed source path. This card is family-scoped and part-row-scoped only. It does not authorize universal selection, placement, attenuation, compliance, or signal-integrity claims.

## Stable Facts

- The datasheet title is `Common Mode Chokes - LPD3015 Series`.
- The family is presented as low-profile common-mode chokes with a stated package size of `3 mm square` and `1.4 mm height`.
- The published table includes named `LPD3015-...` family members and orderable part rows.
- The published table includes directly reusable fields for:
  - `common-mode peak impedance`
  - `differential-mode cutoff frequency`
  - `inductance` per winding
  - `DCR max` per winding
  - `interwinding isolation`
  - `Irms`
- The datasheet note defines the listed differential-mode cutoff frequency as the frequency where differential-mode attenuation equals `3 dB`.
- The inductance note states values are measured at `100 kHz`, `0.1 Vrms`, and `0 Adc`.
- The isolation note states interwinding isolation is tested at `100 Vrms` for one minute.
- The datasheet includes `Typical Impedance vs Frequency` plots with both `Common mode` and `Differential mode` traces.
- The datasheet includes `Typical Attenuation (Ref: 50 Ohms)` plots with both `Common mode` and `Differential mode` traces.

## Safe Usage Boundary

- Use this card when a prompt needs owner-backed exact-data identity for the `LPD3015 Series`.
- Reuse the published table fields only at family scope or explicit part-row scope.
- Reuse the curve existence and mode distinction only as owner-backed evidence that this named family publishes both `common-mode` and `differential-mode` behavior.
- Keep every claim tied to the Coilcraft family and the datasheet's own measurement conditions.

## Conditions And Methods

- When a specific row is cited, keep the wording tied to the exact published `LPD3015-...` member.
- When the family is cited, use only what the datasheet publishes for the family as a family.
- Treat `Irms` as a datasheet reference current with the owner's stated temperature-rise framing, not as a universal application guarantee.
- Treat the plotted figures as owner-backed curves, not as permission to infer additional point-by-point numeric series unless a separate provenance-bound digitization lane is intentionally opened later.

## Must Stay Blocked

- `differential current passes without attenuation` as a universal statement
- universal common-mode choke selection or placement rules
- interface-suitability claims for USB, CAN, Ethernet, audio, power, or any other application beyond the datasheet's narrow published context
- any cross-vendor generalization from this single Coilcraft family
- any per-frequency numeric point series sampled visually from the plots
- any derived bandwidth, peak-frequency, insertion-loss, or cutoff summaries not explicitly printed by Coilcraft
- claims about family members that are not explicitly plotted or tabulated
- compliance, emissions-pass, signal-integrity, reliability, or certification outcomes inferred from this datasheet alone

## Relationship To Other Cards

- Use [common-mode-choke-vs-ferrite-bead-vendor-boundary.md](/code/blogs/llm_wiki/facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md) for conservative family distinction and non-exact vendor boundary wording.
- Use this card only when the prompt specifically benefits from owner-backed `LPD3015 Series` family or part-row exact data.
- Keep [ferrite-bead-vendor-guidance-boundary.md](/code/blogs/llm_wiki/facts/methods/ferrite-bead-vendor-guidance-boundary.md) separate; this card does not repair the blocked `BLA3216A102SG4` exact-part lane.

## Source Links

- https://www.coilcraft.com/getmedia/1003995d-683a-4e70-9051-f551c755e012/lpd3015_cm.pdf
