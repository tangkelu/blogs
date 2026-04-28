# P4-23 Rigid-Flex Flex-Material And Bend-Guidance Supplement

Date: 2026-04-27

## Purpose

This supplement follows `P4-22` and targets the `rigid-flex numeric lane` from the `P4-20` layer-count coverage map.

The goal is to add narrow flex-material and bend-guidance support without promoting design-guide examples into universal bend-radius, cycle-life, or acceptance thresholds.

It does not write or rewrite blogs.

## Starting Gap

From `logs/p4-20-layer-count-claim-coverage-map.md`:

- Rigid-flex bend / transition / cycle numerics were only partially covered.
- Generic `PI / Kapton / UPILEX` numeric rows remained held.
- `14-layer` and rigid-flex drafts needed better separation between material examples and bend/reliability claims.

## Landed Source Records

- `sources/registry/materials/dupont-kapton-hn-product-page.md`
- `sources/registry/materials/dupont-kapton-hn-data-sheet.md`
- `sources/registry/methods/minco-flex-circuits-design-guide-2019.md`
- `sources/registry/methods/minco-designing-flex-circuit-for-flexibility.md`

## Landed Fact Cards

- `facts/materials/dupont-kapton-hn.md`
- `facts/methods/parameter-scope-rigid-flex-bend-guidance.md`

## Claim-Family Impact

### Kapton HN

Disposition changes from `held generic Kapton / PI name` to narrow `source_scoped_fact` for exact product `Kapton HN`.

Allowed use:

- exact-product DuPont all-polyimide film context
- source-scoped film values such as temperature-use context, tensile strength, density, and tensile modulus when film thickness, temperature, and method remain attached

Blocked use:

- generic `Kapton`, `polyimide`, `UPILEX`, `LCP`, or rigid-flex material substitution
- bend-radius, bend-cycle, coverlay, copper-type, adhesive, or stackup rules
- HIL/APT production use, IPC-6013 compliance, Class 3 status, or finished-board reliability proof

### Bend Guidance

Disposition changes from `partially_covered` to `design_guidance_scoped`.

Allowed use:

- bend-ratio explanation as design-guide context
- static versus dynamic bend separation
- Minco example ratios only with source and design-guide scope
- design-review wording around thickness, layer count, coverlay, adhesive, copper layout, forming, and manufacturer review

Blocked use:

- universal bend-radius tables
- cycle-life and survival-count promises
- IPC threshold reconstruction
- HIL/APT capability, warranty, acceptance, or released-lot claims

## Net Result

This batch improves rigid-flex writing support in two ways:

- `Kapton HN` can now be used as a verified exact-product polyimide film example instead of a generic name.
- Bend-ratio numbers can now be discussed as design-guide examples while remaining blocked as universal thresholds or reliability proof.

The batch still does not unlock bend-life tables, transition-tolerance tables, dynamic-flex guarantees, IPC acceptance thresholds, or rigid-flex recipe defaults.
