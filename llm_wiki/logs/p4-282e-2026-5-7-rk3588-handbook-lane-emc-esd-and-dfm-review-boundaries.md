# P4-282E RK3588 Handbook Lane D5: EMC ESD And DFM Review Boundaries

Date: 2026-05-07
Parent: `P4-282`
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Execution mode: `claim_family_lane_learning_only`

## Purpose

Learn the `D5` bounded lane from the `194-page RK3588 handbook` as English canonical claim families only.

This log does not promote handbook numerics, tables, or formulas into `facts/`.

## Lane Scope

Indicative page cluster:

- `165-188`

Lane focus:

- ESD / EMI / EMC review vocabulary
- interface protection and board-edge isolation posture
- routing and stackup review boundaries for EMC
- PCB fabrication DFM review families
- PCBA assembly DFM review families
- rule-template and manufacturability-governance framing

## Safe Claim Families Learned

- ESD, EMI, and EMC should be treated as separate but related review families
- ESD protection is a source-adjacent protection-placement family
- sensitive-circuit placement should reduce exposure to board-edge and connector-adjacent discharge regions
- shielding is an enclosure-grounding family, not a standalone fix
- surface-ground continuity and return-path continuity are core EMC / ESD layout families
- board-edge copper, stitching, and isolation patterns are discharge-management families
- critical reset / clock / interrupt paths are edge-exposure and reference-plane families
- EMI mitigation is a source-control and coupling-path-control family
- filtering, grounding, balancing, impedance control, common-mode suppression, and shielding are mitigation-family categories
- differential symmetry and coupling preservation are EMC-relevant routing families
- clock routing is an EMC review family with source termination, return continuity, and layer-choice implications
- switch-mode power layout is an EMC-sensitive placement family
- capacitor and filter placement is a power-entry and local-loop family
- EMC review can be separated into layout review and routing review
- DFM review begins with net-consistency and gross manufacturability checks before fabrication release
- corner style, teardrop reinforcement, trace geometry, annular-ring margin, and via-in-pad treatment are fabrication-risk families
- drill selection, aspect-ratio awareness, hole-to-hole spacing, and special-hole communication are fabrication-governance families
- solder-mask bridge and solder-mask opening review are manufacturability and solderability families
- component spacing, board-edge clearance, SMT land-pattern proportion, THT hole-attribute correctness, chip land-pattern suitability, and fiducial governance are assembly-readiness families
- DFM rule management is a template-governance family rather than a universal fixed-rule table

## Blocked Classes

- all exact edge clearances, board-edge distances, keepout values, and shield-can spacing values
- all exact resistor values, capacitor values, grounding-via counts, via dimensions, and stitching intervals
- all exact clock-distance, line-spacing, creepage, and isolation thresholds
- all exact `20H`, `3W`, `5W`, inch, mil, millimeter, and ohmic rule values from this handbook
- all interface-protection orderings treated as universal compliance recipes
- all ESD, surge, lightning, EMI, or EMC pass/fail thresholds and test-acceptance implications
- all RK3588-specific spread-spectrum, reset-pin, connector, and interface implementation recipes
- all fabrication capability numbers for trace, space, drill, annular ring, mask bridge, or aspect ratio
- all assembly capability numbers for component spacing, edge clearance, pad ratio, or Mark geometry
- all branded DFM rule tables, red/yellow/green threshold tables, and software-scored manufacturability outputs

## Page-Level Evidence Map

- `page-0165`: final eMMC page from `D4`; not part of `D5`
- `page-0166`: chapter boundary for ESD / EMI / EMC material
- `page-0167` to `page-0170`: ESD protection scope, shielding / isolation posture, and source-adjacent protection family
- `page-0170` to `page-0172`: EMI mitigation families, filtering categories, coupling-path framing, and EMC overlap with ESD
- `page-0173` to `page-0176`: EMC layout-review and routing-review checklists, including clock, switching-power, stackup, bus, and isolation families
- `page-0177`: chapter boundary for DFM
- `page-0178` to `page-0183`: PCB fabrication DFM checks including opens / shorts, corner style, trace geometry, annular ring, via-in-pad, drill, hole spacing, special holes, and solder-mask bridge families
- `page-0184` to `page-0188`: PCBA assembly DFM checks including solder-mask opening, component spacing, board-edge clearance, SMT/THT land-pattern review, Mark-point governance, and rule-template management
- `page-0189` and later: appendix / reference matter outside the `D5` lane

## Image / Table Candidates Worth Preserving Locally

- figures `9-1` to `9-6`: ESD protection placement, board-edge grounding, reset-capacitor grounding, exposed-copper, and edge-isolation exemplars
- figures `9-7` to `9-10`: EMI three-element framing, differential-symmetry, plane-setback, and split-crossing illustrations
- figures `10-1` to `10-17`: DFM review exemplars for opens / shorts, routing geometry, annular ring, via-in-pad, drill, hole spacing, special holes, solder mask, assembly spacing, pad proportion, THT attribute, chip land pattern, Mark points, and rule-template screens

Branding-removal notes:

- crop out `Rockchip` promo footers, `华秋DFM` shells, `www.fany-eda.com`, QR codes, contact prompts, and price / discount CTA strips
- keep only the technical drawing area or neutral checklist content where separable
- do not preserve branded red / yellow / green software rule tables as reusable authority

## Contamination Patterns To Exclude

- promotional footer text and discount language
- vendor software marketing claims
- QR codes, customer-service prompts, and contact banners
- branded DFM dashboard screenshots treated as authority
- RK3588-specific interface recipes generalized into universal EMC / ESD rules
- exact manufacturing thresholds reframed as cross-fabricator guarantees

## Status

`D5` is complete at claim-family level only. It is ready for later exact-data gating, but no numeric or table promotion was performed.
