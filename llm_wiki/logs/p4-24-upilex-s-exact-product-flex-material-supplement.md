# P4-24 UPILEX-S Exact-Product Flex-Material Supplement

Date: 2026-04-27

## Purpose

This supplement follows `P4-23` and closes another narrow flex-material source gap from the layer-count and rigid-flex material tail.

The goal is to add UBE `UPILEX-S` as an exact-product polyimide film fact without promoting it into a generic `UPILEX`, generic `PI`, rigid-flex stackup, or bend-life authority.

It does not write or rewrite blogs.

## Starting Gap

From earlier layer-count and flex-material governance:

- generic `PI / Kapton / UPILEX` numeric rows remained held
- `Kapton HN` was upgraded in `P4-23`, but `UPILEX-S` still needed a source-scoped product lane

## Landed Source Records

- `sources/registry/materials/ube-upilex-grade-details.md`
- `sources/registry/materials/ube-upilex-advantages-page.md`

## Landed Fact Card

- `facts/materials/ube-upilex-s.md`

## Claim-Family Impact

### UBE `UPILEX-S`

Disposition changes from `held generic UPILEX / PI name` to narrow `source_scoped_fact` for exact product `UPILEX-S`.

Allowed use:

- exact-product UBE polyimide film context
- source-scoped film values such as grade thicknesses, tensile strength, tensile modulus, density, thermal expansion, heat shrinkage, and thermal conductivity when grade, temperature, condition, and method remain attached
- FPC / TAB-tape substrate application context as UBE page wording

Blocked use:

- generic `UPILEX`, generic `polyimide`, generic `PI`, `Kapton`, `LCP`, or rigid-flex material substitution
- bend-radius, bend-cycle, coverlay, copper-type, adhesive, stackup, or transition-zone rules
- HIL/APT production use, IPC-6013 compliance, Class 3 status, finished-board reliability proof, cost, lead time, or yield

## Net Result

This batch improves rigid-flex and flex-material writing support in one narrow way:

- `UPILEX-S` can now be used as a verified exact-product polyimide film example alongside `Kapton HN`.

The batch still does not unlock generic PI comparison tables, bend-life tables, transition-tolerance tables, dynamic-flex guarantees, IPC acceptance thresholds, or rigid-flex recipe defaults.
