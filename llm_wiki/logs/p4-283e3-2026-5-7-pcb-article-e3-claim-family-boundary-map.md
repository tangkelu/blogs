# P4-283E3 PCB Article Cluster E3 Boundary Map

Date: 2026-05-07
Parent: `P4-283`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Execution mode: `claim_family_boundary_mapping_only`

## Purpose

Map the `E3` fabrication-features cluster into English canonical claim families only.

This log does not promote article numerics, vendor rule tables, or threshold charts into `facts/`.

## E3 Subclusters

- `E3-A` hole and slot taxonomy
- `E3-B` hole and slot omission / export failure modes
- `E3-C` small-hole and small-slot manufacturability risk
- `E3-D` via solder-mask treatment
- `E3-E` solder-mask opening and mask-bridge control
- `E3-F` pad geometry and pad-mask relationship
- `E3-G` edge-feature structures such as half-hole and gold finger
- `E3-H` hole-spacing reliability

## Safe Claim Families Learned

- holes and slots carry both electrical-intent and manufacturing-intent metadata
- plated vs non-plated intent must be expressed clearly in CAD outputs
- export and configuration mistakes are major causes of missing holes, missing slots, and missing openings
- very small drilled or milled features create manufacturability risk
- via treatment is scenario-dependent and remains a taxonomy
- solder-mask bridge control is a defect-prevention family
- pad geometry drives skew, tombstoning, wetting, and bridging risk
- castellated / half-hole features need special array and routing handling
- hole-spacing is a reliability and failure-mode family

## Blocked Classes

- all dimensions, drill sizes, slot widths, annular-ring values, spacings, and tolerances
- all vendor rule tables and recommendation charts
- all process-window matrices and capability claims
- all yield, cost, lead-time, and acceptance-threshold statements

## Evidence And Asset Notes

Preserve locally:

- hole / slot ambiguity figures from `PCB可制造性设计及案例分析之孔槽篇`
- square-lead and small-slot representation diagrams
- missing-slot and zero-diameter-via failure screenshots
- via-mask treatment diagrams
- mask-bridge diagrams
- pad mismatch and equal-size pad-pattern diagrams
- half-hole / gold-finger / edge-connector visuals
- hole-spacing failure screenshots

Exclude as reusable authority:

- repeated `华秋DFM` CTA banners
- QR / community join prompts
- vendor rule screenshots that embed thresholds
- branded poster pages

## Status

`E3` is complete at claim-family level only. It is ready for later narrower lane execution, but no exact numeric or table promotion was performed.

