# P4-282C RK3588 Handbook Lane D3: Power Delivery And Grounding Layout

Date: 2026-05-07
Parent: `P4-282`
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Execution mode: `claim_family_lane_learning_only`

## Purpose

Learn the `D3` bounded lane from the `194-page RK3588 handbook` as English canonical claim families only.

This log does not promote handbook numerics, tables, or formulas into `facts/`.

## Lane Scope

Indicative page cluster:

- `76-102`

Lane focus:

- PMIC topology and placement
- BUCK / LDO / discrete DC-DC implementation posture
- remote-feedback topology
- SoC rail power-entry patterns
- power-pour and return-path governance
- grounding and reference-plane posture

## Safe Claim Families Learned

- PMIC placement is a topology-governance family
- switching stages are loop-minimization families
- capacitor GND handling matters together with the power path
- thermal-pad grounding serves thermal and impedance goals
- remote feedback is a sense-point family that must stay quiet
- SoC rail decoupling is a placement family
- power-pin escape is a fanout family
- high-current rail routing is a copper-pour family
- layer-transition planning is a resistance-drop family
- grounding is a reference-plane family

## Blocked Classes

- all rail current tables and peak-power tables
- all per-via current capacity rules
- all exact via dimensions, counts, and array patterns
- all exact trace-width, copper-width, and region-width prescriptions
- all exact placement distance targets
- all PDN target-impedance values and frequency tables
- all exact rail-specific recipes for `VDD_CPU_BIG`, `VDD_LOGIC`, `VDD_GPU`, `VDD_NPU`, `VDD_CPU_LIT`, `VDD_VDENC`, `VCC_DDR`, `VDDQ_DDR`, `VCC0V6_DDR`

## Preservation Notes

Preserve locally as evidence-bearing references:

- PMIC topology and BUCK/LDO/DC-DC layout figures
- remote-feedback figure set
- CPU_BIG, LOGIC, GPU, NPU, CPU_LIT, VDENC, and DDR power-entry figure families
- blocked PDN table and grounding figures for future source recovery only

Exclude as reusable authority:

- promotional footer and banner text
- Rockchip-specific rail names treated as universal rules
- PDN tables and exact-width figures
- extraction bleed from the adjacent connector-routing page

## Status

`D3` is complete at claim-family level only. It is ready for later exact-data gating, but no numeric or table promotion was performed.

