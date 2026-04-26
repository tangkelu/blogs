# H1 Material Numeric Coverage Matrix

Date: 2026-04-25

## Purpose

This file converts the H0 material-gap output into an execution matrix for exact-product numeric recovery.

The goal is not generic prose coverage.

The goal is to recover official product-grade numeric anchors for the material families the 10 layer-count blogs keep reusing.

## Coverage Posture

- `covered_product_grade`: exact product page or datasheet already exists and is numerically usable with conditions
- `covered_family_only`: family-level or lineup-level anchor exists, but exact product-grade numeric recovery is still uneven
- `gap_control`: source-first hold; do not replace with mirrors or inferred numerics
- `missing`: no stable official product-grade anchor yet

## H1 Priority Matrix

- `Standard FR-4 generic rows`
  - posture: `gap_control`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `CTE`, `water absorption`, `peel strength`, `thermal conductivity`
  - gap: blogs still use one generic FR-4 row as if it had a single loss / CTE / temperature profile

- `Isola 370HR / FR408HR / FR408 / IS410`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `T288`, `CTE`, `water absorption`, `peel strength`, `flammability`
  - note: strongest mainstream FR-4 ladder for `6 / 8 / 10 / 14 / 16 / 20 / 22-layer`

- `ITEQ IT-180A`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Tg`, `Td`, `Dk`, `Df`, `CTE`, `T288`, `CTI`
  - note: exact-product page-backed baseline row now exists

- `Shengyi S1000-2 / S1000-2M`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Tg`, `Td`, `Dk`, `Df`, `CTE`, `T288`, `moisture`
  - note: both grades now have separate official exact-product baseline rows; keep them split rather than flattening Shengyi into one FR-4 average

- `Panasonic Megtron 4`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `T288`, `CTE`, `water absorption`, `peel strength`, `thermal conductivity`
  - note: `R-5725 / R-5620` now gives Panasonic a model-grade lower-loss baseline below `MEGTRON 6 / 7 / 8`

- `Panasonic Megtron 6 / 7 / 8`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `T288`, `CTE`, `water absorption`, `peel strength`, `thermal conductivity`
  - note: strongest digital low-loss ladder for `16 / 24-layer`

- `Isola I-Speed / I-Tera MT40 / Tachyon 100G`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `CTE`, `T288`, construction-aware dielectric tables
  - note: strong for `16 / 22 / 24-layer` low-loss ladders

- `ITEQ IT-150DA / IT-968 / IT-602G`
  - posture: all `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `CTE`, `T288`, with datasheet-side support for moisture, peel strength, flammability, and resistivity context
  - note: `IT-150DA`, `IT-968`, and `IT-602G` now each have product-grade official anchors; keep `IT-968` distinct from adjacent `IT-968G`, and use the ITEQ ladder normalization card for branch placement rather than flattening them into one row

- `ITEQ IT-988GLSE / IT-988GSE / IT-988GL / IT-988G / IT-968SE`
  - posture: all `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `CTE`, `T288`, with page-plus-datasheet posture for future density expansion
  - note: the current official public ultra-low-loss branch now supports multiple exact ITEQ grades; keep each grade isolated by exact name, use the ITEQ ladder normalization card for guarded ordering, and do not revive unconfirmed `IT-988SE` naming as a substitute

- `Ventec VT-464G / VT-870 / VTM1000i`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `Tg`, `Td`, `T288`, `thermal conductivity`, `CTE`
  - note: useful for low-loss and RF ladders

- `Rogers RO4350B / RO4003C / RO4835`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `CTE`, `thermal conductivity`, `moisture`, `peel strength`
  - note: strong for `8 / 10 / 18-layer` hybrid-RF rows

- `Rogers RT/duroid 5880 / RO3003 / RO3006 / RO3010 / RO3035`
  - posture: `covered_product_grade`
  - supportable numeric fields: `Dk`, `Df`, `CTE`, `thermal conductivity`, `moisture`, `peel strength`
  - note: strong for `6 / 18-layer` RF / PTFE constants

- `Taconic TLY / TLC and similar PTFE rows`
  - posture: `gap_control`
  - desired fields: `Dk`, `Df`, `CTE`, `thermal conductivity`, `thickness`, `copper options`
  - gap: remain source-first until official product datasheets are confirmed

- `Arlon 55NT / 85N / 85NT / hi-rel branch`
  - posture: `55NT = covered_product_grade`, `85N = covered_product_grade`, `85NT = covered_product_grade`
  - needed fields: `Tg`, `Td`, `Df`, `moisture`, `CTE`, `peel strength`
  - gap: `55NT`, `85N`, and `85NT` now all have official product-grade anchors; the remaining Arlon gap shifts from exact-product recovery to branch normalization and selector wording

- `Rigid-flex polyimide / Kapton / UPILEX / adhesiveless flex`
  - posture: `R-F705S = covered_product_grade`, broader branch `gap_control`
  - desired exact-product fields: `film thickness`, `Dk`, `Df`, `copper type`, `adhesion/peel`, bend-life context
  - gap: `Panasonic R-F705S` now covers one exact-product `LCP` row, but do not let that narrow flex exception turn generic rigid-flex process or reliability numerics into H1 coverage

- `RCC / FRCC / bondply / low-flow / no-flow build-up branch`
  - posture: `gap_control`
  - exact-product fields only: `Dk`, `Df`, `Tg`, `thickness`, `resin content`, foil options
  - gap: `RO4450F`, `RO4460G2`, and `R-FR10` now exist as narrow exact-product exceptions, but keep the branch-level posture at `gap_control` so supplier-side build-up materials do not turn into default stack recipes

- `IMS / aluminum-core / thermally conductive dielectric`
  - posture: `VT-4B7 = covered_product_grade`, remainder `covered_family_only`
  - supportable numeric fields: `thermal conductivity`, `dielectric thickness`, `base metal thickness`
  - gap: `VT-4B7` now gives one exact-product IMS anchor, but only material constants are safe, not board-level heat-spread outcomes

## Recommended Execution Split

- `Batch 1`: mainstream FR-4 / high-Tg FR-4 exact-product cleanup
- `Batch 2`: digital low-loss / very-low-loss exact-product cleanup
- `Batch 3`: RF / hybrid exact-product cleanup
- `Batch 4`: hi-rel / extreme-temp / special-material cleanup
- `Batch 5`: build-up / flex / special-thermal boundary cleanup

## H1 Success Rule

- No exact-product numeric table should rely on family-only prose when an official datasheet or product page is available.
- No Taconic or unresolved Arlon grade should be hard-written as numeric until an official stable source is registered.
- No rigid-flex or build-up numeric should be promoted from source-gap note to reusable fact without product-grade support.

## End State

- `H1` is complete as of `2026-04-25`.
- Use `logs/h1-material-numeric-coverage-closeout-summary.md` for the final hold/exception boundaries.
