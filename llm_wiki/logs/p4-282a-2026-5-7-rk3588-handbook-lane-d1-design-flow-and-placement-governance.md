# P4-282A RK3588 Handbook Lane D1: Design Flow And Placement Governance

Date: 2026-05-07
Parent: `P4-282`
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Execution mode: `claim_family_lane_learning_only`

## Purpose

Learn the `D1` bounded lane from the `194-page RK3588 handbook` as English canonical claim families only.

This log does not promote handbook numerics, tables, or formulas into `facts/`.

## Lane Scope

Indicative page cluster:

- `4-36`

Lane focus:

- design-flow governance
- module-driven placement
- class and rule setup
- verification governance
- placement hygiene and clearance families

## Safe Claim Families Learned

- PCB design flow as a staged process from input review to routing and verification
- module extraction and module-by-module placement
- signal grouping into classes before routing
- DRC / Gerber / project-check / archive workflow identity
- placement hygiene for keepouts, symmetry, thermal spacing, rework access, connector clearance, BGA clearance, and mechanical clearance

## Blocked Classes

- all spacing numbers
- all widths, heights, thicknesses, angles, counts, and tables
- all stackup and impedance outputs
- all board-specific numeric placement rules

## Preservation Notes

Preserve locally as evidence-bearing references:

- process flow diagrams on early pages
- module flow / power-tree / split-plane illustrations
- placement governance diagrams for keepout and clearance families

Exclude as reusable authority:

- repeated sales footer
- `华秋DFM` branding
- `fany-eda.com` promo banner
- `RK3588 PCB设计视频`
- `DFM/DFA检测工具`

## Status

`D1` is complete at claim-family level only. It is ready for later exact-data gating, but no numeric or table promotion was performed.

