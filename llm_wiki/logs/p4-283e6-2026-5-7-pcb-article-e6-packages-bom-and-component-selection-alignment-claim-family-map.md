# P4-283E6 PCB Article Cluster E6 Packages BOM And Component Selection Alignment Claim Family Map

Date: 2026-05-07
Parent: `P4-283`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Execution mode: `claim_family_boundary_mapping_only`

## Purpose

Map the `E6` packages / BOM / component-selection alignment cluster into English canonical claim families only.

This log does not promote article numerics, procurement promises, or vendor workflow tables into `facts/`.

## E6 Subclusters

- package identity and size-code grammar
- package-to-footprint alignment and pin-count matching
- BOM line-item normalization and reconciliation
- procurement risk and availability watch
- 0Ω resistor jumper / isolation / debug placeholder behavior
- FPC structure and layer-family comparison

## Safe Claim Families Learned

- package naming requires separating identity grammar from footprint geometry
- package-to-footprint alignment is a matching problem between BOM identity and PCB land pattern
- BOM normalization should separate electrical part identity from packaging and supplier metadata
- procurement decisions are constrained by package availability, but those risk stories are not universal rules
- 0Ω resistors can function as jumper, isolation, and debug placeholder
- FPC layer count changes structure, flexibility, and manufacturing complexity

## Blocked Classes

- all package dimensions, EIA / metric conversion tables, pin-count tables, footprint-dimension tables, and resistor size tables
- all BOM line counts, customer-order quantities, stock levels, lead times, cost claims, and supplier-availability claims
- all part-number examples used as authority rather than provenance
- all vendor-tool workflow claims, auto-matching promises, and procurement-service promises
- all exact BOM-matching rules presented as universal design law

## Per-PDF Evidence Map

- `电子元器件封装(Package).pdf`
  - package concept, standardization, and package-family evolution
  - resistor size-code table is blocked exact-data inventory only
  - component-letter taxonomy is useful for identity grammar
- `如何解决bom物料与焊盘不匹配问题.pdf`
  - BOM definition, footprint mismatch, and pin-count mismatch families
  - matching-library workflow is useful as a bounded matching context
  - the exact mismatch screenshot remains blocked as a reusable numeric authority
- `BOM查错助力元器件采购.pdf`
  - BOM整理 and lack of unified library are useful claim families
  - procurement workflow is mostly inventory-only, not authority for reusable facts
- `如何避免采购电子元器件入坑.pdf`
  - multiple-package-per-model risk
  - cold-material / shortage / supplier-selection failure stories
  - procurement advice remains mostly claim inventory only
- `0Ω电阻在PCB板中的5大常见作用.pdf`
  - jumper, isolation, and debug-flexibility families
  - exact size recommendations remain blocked
- `单层双面多层FPC有何区别.pdf`
  - single / double / multilayer FPC structure taxonomy
  - material and layer-family comparison context

## Image / Table Candidates Worth Preserving Locally

- `电子元器件封装(Package).pdf` p2: size-code table, preserved as blocked provenance only
- `如何解决bom物料与焊盘不匹配问题.pdf` p4: pin-count mismatch comparison
- `BOM查错助力元器件采购.pdf` p1-p2: BOM normalization and matching workflow panels
- `如何避免采购电子元器件入坑.pdf` p4: shortage / cold-material case narrative
- `0Ω电阻在PCB板中的5大常见作用.pdf` p2-p3: jumper and debug-isolation figures
- `单层双面多层FPC有何区别.pdf` p2-p4: FPC layer-structure diagrams

Branding-removal notes:

- crop out `华秋DFM` banners, QR codes, and footer CTAs
- keep only technical tables or figures where they are separable from the promo shell

## Contamination Patterns To Exclude

- repeated download banner text
- QR / join-group CTA surfaces
- procurement pitch language about省时省力, cost reduction, or service promises
- vendor-tool auto-matching claims treated as universal proof
- stock / shortage / supplier claims promoted beyond the local case-story level

## Status

`E6` is complete at claim-family level only. Package-to-footprint alignment is bounded, while procurement guidance stays mostly claim inventory only.

