# P4-283E PCB Article Cluster E4 Panelization Outline Edge Clearance And Marking Claim Family Map

Date: 2026-05-07
Parent: `P4-283`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Execution mode: `claim_family_boundary_mapping_only`

## Purpose

Map the `E4` panelization / outline / edge-clearance / marking cluster into English canonical claim families only.

This log does not promote article numerics, vendor rule tables, or threshold charts into `facts/`.

## E4 Subclusters

- panelization method selection
- outline and edge-connection manufacturability
- assembly-facing panel design
- board-edge component risk
- fiducial / Mark strategy

## Safe Claim Families Learned

- panelization method is constrained by outline regularity and depanel path shape
- irregular, circular, half-hole, and overhanging-edge boards create special panelization branches
- some panel layouts are safe for bare-board fabrication but unsafe for SMT assembly
- panel direction and orientation should be made explicit when symmetry can hide intent
- board-edge geometry may need relief features or alternate connection design
- edge-near components create machine interference, rail collision, depanel stress, and pad-damage risks
- taller or protruding components require stricter edge-awareness
- Mark points serve as optical alignment references at board, panel, and local-component scope
- Mark-point usefulness depends on placement, asymmetry, and visual cleanliness

## Blocked Classes

- all edge-clearance distances, V-CUT gaps, rail widths, keep-out widths, hole diameters, hole counts, and panel-center distances
- all aspect-ratio recommendations and mark-size/opening numbers
- all supplier-scoped rule tables and software-check outputs
- all pages that mix geometry guidance with pricing, lead time, capability, or quality promises

## Preservation Notes

Preserve locally as evidence-bearing references:

- shape-specific panelization examples
- no-gap vs gapped panel interference examples
- Mark-point placement and keep-out diagrams
- board-edge damage / depanel hazard illustrations
- corner-relief / slot-access / edge-connection visuals

Exclude as reusable authority:

- repeated download banners
- QR / join-group CTA surfaces
- vendor DFM pitch pages
- software screenshots with ads or nontechnical sidebars

## Status

`E4` is complete at claim-family level only. It is ready for later narrower lane execution, but no exact numeric or table promotion was performed.

