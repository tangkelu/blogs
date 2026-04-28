# P4-19 PCBA Process Parameter Scope Supplement

Date: 2026-04-27

## Purpose

Continue the empty-image data-first program without writing blogs.

This round adds parameter-scope cards for PCBA process and product-level parameters that commonly drift into overclaim in four lanes:

- low-void BGA
- conformal coating
- selective solder / THT
- charger / inverter inspection and validation context

The objective is to preserve usable parameter vocabulary and narrowly scoped source-backed values while explicitly blocking generic process-window leakage.

## What Landed

New fact cards:

- `facts/methods/parameter-scope-pcba-low-void-bga-paste-profile-context.md`
- `facts/methods/parameter-scope-pcba-conformal-coating-family-and-application-context.md`
- `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`
- `facts/methods/parameter-scope-pcba-inspection-stack-for-low-void-coating-tht-and-power.md`

No existing fact cards, topic pages, or protected logs were edited in this round.

## Source Posture Used

This supplement reused existing registry records only:

- Indium and Kester reflow-profile records
- HumiSeal and Electrolube conformal-coating records
- IPC-CC-830C public metadata
- local APT and HIL PCBA product / service pages
- local selective-solder and wave-fixture explainers
- inspection-method records for SPI, AOI, X-ray, ICT, and FCT

No new registry records were introduced.

## Key Parameters Added

### Low-void BGA

- allowed parameter families:
  - ramp
  - soak
  - time above liquidus
  - peak
  - cooling
  - paste volume / height / area / offset
- allowed source posture:
  - named-paste or named-profile context only
  - no generic HIL recipe conversion

### Conformal Coating

- allowed family vocabulary:
  - acrylic
  - silicone
  - urethane
  - parylene
- allowed method vocabulary:
  - manual spraying
  - automated spraying
  - selective coating
- one narrow local numeric context preserved:
  - APT page-stated `1-5 mils` / `25-127 microns`
  - explicitly blocked from becoming a general default

### Selective Solder / THT

- allowed route-stage vocabulary:
  - flux application
  - preheating
  - soldering
  - post-solder cleaning
  - inspection
- allowed route-choice context:
  - selective versus wave versus manual versus reflow
  - access / shadowing / support / nearby-SMT protection
- HIL page numeric examples were quarantined as page-scoped only, not reusable defaults

### Inspection Stack For Charger / Inverter And Adjacent PCBA Topics

- allowed measured-attribute vocabulary:
  - SPI volume / height / area / offset
  - AOI placement / polarity / solder appearance
  - X-ray `2D`, `2.5D`, `3D CT`
  - ICT electrical-fault coverage role
  - FCT powered-function role
- allowed sequencing posture:
  - SPI -> AOI / X-ray -> ICT / FCT -> final inspection
  - with the existing quality-system warning that not every project uses every gate

## Explicitly Blocked Claim Classes

This round does not unlock:

- generic reflow recipes
- void thresholds or hidden-joint acceptance thresholds
- coating thickness defaults, cure defaults, cleanliness limits, or masking dimensions
- selective-solder or wave process defaults
- barrel-fill or press-fit acceptance defaults
- HIL capability claims
- yield, cost, or lead-time claims
- compliance, qualification, or release-authority claims

## Gaps

- Exact vendor PDF numbers for Indium and Kester were intentionally not copied into the new cards because local PDF text extraction was unavailable in this environment; those values remain refresh-required at source time.
- HumiSeal and Electrolube still need product-datasheet-level registry coverage if future drafts require chemistry-specific numeric properties.
- The HIL through-hole page contains many marketing-scope numbers that need future split treatment before any of them can be elevated beyond page-scoped examples.
- Inspection sources remain strong for method scope, but weak for neutral acceptance thresholds; licensed standards or customer specs would still be needed for pass/fail numbers.

## Verification Target

This round is complete when:

1. the four new fact cards resolve their `source_ids` against existing registry records
2. `git diff --check` passes for the new files
3. later prompt execution has explicit blocked-use language to prevent parameter drift into generic HIL process claims
