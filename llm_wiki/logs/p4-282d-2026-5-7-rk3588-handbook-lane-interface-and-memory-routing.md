# P4-282D RK3588 Handbook Lane D4: Interface And Memory Routing

Date: 2026-05-07
Parent: `P4-282`
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Execution mode: `claim_family_lane_learning_only`

## Purpose

Learn the `D4` bounded lane from the `194-page RK3588 handbook` as English canonical claim families only.

This log does not promote handbook numerics, tables, or formulas into `facts/`.

## Lane Scope

Indicative page cluster:

- `103-164`

Lane focus:

- DRAM interface architecture and topology
- DRAM-variant-coupled power and connection selection
- stackup / impedance / routing template governance
- return-path / via / reference-plane continuity
- timing matching / serpentine control
- eMMC interface connection and matching context

## Safe Claim Families Learned

- memory-interface routing rules depend on DRAM generation and topology choice
- vendor DDR templates are routing-governance artifacts, not universal recipes
- DDR routing quality depends on continuous reference planes and explicit return-path management at layer transitions
- ground-return vias near signal vias are a core return-path family
- serpentine routing is a timing-compensation tool of last resort
- timing matching for memory buses should be framed as equal-delay, not raw equal-length
- sensitive memory clocks and strobes merit extra shielding / ground-containment treatment
- eMMC connection guidance is platform-scoped and should not genericize exact pull-up / pull-down recipes

## Blocked Classes

- all handbook impedance targets, tolerances, line-width / spacing recipes, layer-stack prescriptions, via counts, spacing rules, and timing tables
- all DDR power-rail tables, PMIC feedback-divider settings, resistor values, voltage selections, and LPDDR4 / LPDDR4x option-population details
- all eMMC pull-up / pull-down / matching tables
- all chip capability numerics, mode / version enumerations, bus widths, capacities, and throughput figures from this PDF

## Page-Level Evidence Map

- `page-0103`: interface chapter boundary / prelude; not a core D4 fact source
- `page-0110`: PCIe requirement table and generation comparison; exact data blocked, interface-family context only
- `page-0125`: SDMMC / SDIO routing guidance; safe routing-governance family
- `page-0143`: memory chapter opener
- `page-0144`: DDR scope opens; architecture / capability context only
- `page-0145`: DDR design invariants; variant-specific signal selection and pin-order caution
- `page-0146`: DDR topology and mode context; topology-dependent routing family
- `page-0147`: DDR power tables only; blocked exact-data class
- `page-0148` to `page-0150`: PMIC and variant-coupled power-selection guidance; keep only high-level coupling language
- `page-0150` to `page-0153`: stackup and impedance-design section; keep only reference-structure governance
- `page-0154` to `page-0156`: impedance targets and template-routing setup; prefer validated vendor template, block exact numbers
- `page-0157`: layer-by-layer DDR routing exemplars; preserve figures if clean
- `page-0158` to `page-0159`: return-via and reference-plane continuity claim families
- `page-0160`: serpentine-risk and via-delay-aware timing-match family
- `page-0161`: via optimization, nonfunctional-pad caution, and shielded clock/strobe family
- `page-0162`: DDR power-via counts and LPDDR4 timing table blocked; equal-delay family only
- `page-0163`: eMMC interface scope and capability context only
- `page-0164`: eMMC reference-connection and multiplexed-interface context; matching table blocked

## Image / Table Candidates Worth Preserving Locally

- figures `8-4` and `8-5`: DRAM point-to-point topology sketches
- figures `8-22` to `8-29`: DDR layer-routing exemplars
- figures `8-30` to `8-33`: return-ground-via placement and reference-plane repair examples
- figures `8-34` and `8-35`: serpentine and via-delay illustrations
- figures `8-36` and `8-37`: via optimization and shielded clock / strobe routing
- figure `8-41`: eMMC reference connection, treated as platform-scoped only

Branding-removal notes:

- crop out `Rockchip` promo footers, `华秋DFM` shells, QR codes, and `www.fany-eda.com` contact strips
- keep only the technical drawing area where separable

## Contamination Patterns To Exclude

- promo footer text and CTA copy
- QR codes, customer-service prompts, and WeChat contact prompts
- `华秋DFM` / `dfm.elecfans.com` branded shells
- any exact-width or exact-delay figure interpreted as a universal rule
- extraction bleed from adjacent connector or appendix pages

## Status

`D4` is complete at claim-family level only. It is ready for later exact-data gating, but no numeric or table promotion was performed.

