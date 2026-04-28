# P4-21 Layer-Count Material Exact-Product Supplement

Date: 2026-04-27

## Purpose

This supplement follows the `P4-20` layer-count claim ingestion closeout and targets the highest-value material exact-product gaps that can safely become reusable source-scoped facts.

It does not write or rewrite blogs.

## Inputs

Starting gap list from `logs/p4-20-layer-count-claim-coverage-map.md`:

- `Shengyi S1150G` exact-product material support
- `Isola P95` exact-product support
- `IT-988SE` naming verification

## Landed Source Records

- `sources/registry/materials/shengyi-s1150g-product-page.md`
- `sources/registry/materials/isola-p95-p25-datasheet.md`
- `sources/registry/materials/isola-p95-p25-dk-df-tables.md`

## Landed Fact Cards

- `facts/materials/shengyi-s1150g.md`
- `facts/materials/isola-p95-p25.md`
- `facts/materials/iteq-it-988se-naming-boundary.md`

## Claim-Family Impact

### Shengyi `S1150G`

Disposition changes from `needs_source` / `held` to `source_scoped_fact`.

Allowed use:

- exact-product halogen-free mid-`Tg` FR-4 material parameter context
- source-scoped values such as `Tg`, `Td`, `CTE`, `T260`, `T288`, `Dk`, and `Df`

Blocked use:

- generic halogen-free FR-4 averages
- HIL capability, stackup, lamination, lead-time, cost, or yield claims
- automotive / communication application proof

### Isola `P95/P25`

Disposition changes from `needs_source` to `source_scoped_fact`.

Allowed use:

- exact-product polyimide laminate/prepreg material context
- source-scoped high-temperature material values
- construction-aware dielectric discussion only with the Dk/Df table context preserved

Blocked use:

- Class 3 / 3A, aerospace, defense, medical, space, outgassing, supplier approval, lot acceptance, or release proof
- HIL or APT availability, stocking, cost, lead-time, or capability claims

### ITEQ `IT-988SE`

Disposition remains `needs_source`, but the boundary is now explicit.

Allowed use:

- state that current reusable evidence supports verified exact rows such as `IT-988G`, `IT-988GL`, `IT-988GSE`, and `IT-988GLSE`
- replace old-blog `IT-988SE` with a verified exact grade only when the selected grade is semantically intended and separately cited

Blocked use:

- treating `IT-988SE` as a synonym for any verified `IT-988*` grade
- suffix-based performance inference or procurement substitution

## Net Result

This batch improves the layer-count material lane without weakening P4-20's governance:

- two held material names are now exact-product source-scoped facts
- one ambiguous old-blog material name is now explicitly blocked from silent reuse
- no capability, standards-threshold, high-speed performance, commercial, or supplier-proof claim class was unlocked
