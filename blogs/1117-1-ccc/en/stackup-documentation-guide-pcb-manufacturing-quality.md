---
title: "stackup documentation guide: A process-driven playbook for PCB manufacturing and testing"
description: "Using a stackup documentation guide as the backbone, this end-to-end walkthrough covers manufacturing details, quality-control checkpoints, and DFM/DFT tips from materials and imaging to soldermask, SMT, and test validation."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["stackup documentation guide", "soldermask exposure tutorial", "smt stencil design tutorial", "pcb fabrication process steps", "yield improvement roadmap", "surface finish selection tips"]
---
Hello, I’m an instructor at the HILPCB Manufacturing Academy. In day-to-day work, I’ve noticed many design engineers treat a `stackup documentation guide` as “just” a document that defines lamination structure and impedance control. From a manufacturing-and-test perspective, however, it is the “genesis blueprint” and “execution constitution” of the entire production flow. It not only determines electrical performance, but also deeply influences yield, reliability, and cost at every stage—from incoming materials to final functional testing.

Today we’ll use this core document as a thread to walk through the full PCB manufacturing and test flow. This is not only a **pcb manufacturing tutorial**, but also a **yield improvement roadmap** that connects design intent to manufacturing reality. We’ll break complex processes into SOP-style steps and checklists so your team can truly internalize DFM (Design for Manufacturability) and DFT (Design for Testability).

## Manufacturing flow overview: from Stackup document to physical product

A detailed `stackup documentation guide` is the starting point for fabrication. It defines materials, thickness, copper weight, and tolerances—parameters that set the process window on the production line. The table below shows how major manufacturing steps map directly to information in the Stackup document.

| Process Step | Core Objective | Key Control Parameters | Related Stackup Info |
| :--- | :--- | :--- | :--- |
| **Laminate preparation** | Ensure materials meet design requirements | Material type, board thickness, copper thickness, dimensional accuracy | Core and prepreg (PP) types, Dk/Df, Tg, CAF resistance |
| **Inner-layer imaging** | Accurately replicate inner-layer patterns | Exposure energy, develop time, registration (±25 µm) | Inner-layer copper thickness (e.g., 0.5 oz, 1 oz), minimum line/space |
| **Lamination** | Press multilayer structure into one | Temperature/pressure/time profile, resin-flow control | Stack order, PP type/quantity, overall thickness tolerance (±10%) |
| **Drilling** | Create through holes and mounting holes | Spindle speed, feed rate, hole-position accuracy (±50 µm) | Hole size, hole type (PTH/NPTH/blind/buried), hole density, minimum annular ring |
| **Plating** | Build interlayer electrical connection | Rectifier current density, bath chemistry, copper thickness (>20 µm) | Aspect ratio, copper thickness requirements |
| **Outer-layer imaging** | Accurately replicate outer-layer patterns | Registration, etch-factor control | Outer-layer copper thickness, impedance-trace width, BGA/QFN pad sizes |
| **Soldermask** | Protect traces and define solderable areas | Ink type/thickness, exposure accuracy, curing conditions | Soldermask color, minimum Solder Mask Dam width |
| **Surface finish** | Provide solderability and protection | Plating thickness (e.g., ENIG: Au 0.03–0.08 µm), flatness | [Surface Finish](/blog/pcb-surface-finish/) (HASL, ENIG, OSP, etc.) |
| **SMT assembly** | Place and solder components | Paste volume, placement accuracy, reflow profile | BOM, packages, pad design |
| **Test & validation** | Ensure electrical function and reliability | Coverage, fault-diagnosis accuracy | Test-point layout, net connectivity |

## Precision control of imaging, etching, and soldermask

Trace width and spacing are directly tied to signal integrity and impedance control, and these are tightly defined in the Stackup document. The manufacturing challenge is to reproduce those numbers accurately on real boards.

### Etch process window: turning numbers into reality

Etching is a subtractive process: it removes unwanted copper and leaves traces behind. But etchant attacks not only downward; it also etches laterally, creating undercut. To compensate, we apply “etch compensation” to the design data—widening traces in the phototool in advance.

<div class="div-style-1">

#### Process window: trace etching

- **Target**: Achieve ±10% tolerance on designed trace width.
- **Input**: Stackup-defined copper thickness (e.g., 1 oz HTE Copper).
- **Key parameters**:
    - **Etch compensation**: 1 oz copper typically needs 25–35 µm compensation.
    - **Etch rate**: 1.2–1.8 m/min, controlled by chemistry concentration and temperature.
    - **Undercut control**: High-precision spray systems and dedicated etchants keep undercut within 12 µm.
- **Inspection method**: 100% AOI, with cross-section analysis for critical lines to measure line/space.
- **DFM tip**: When doing [impedance control design](/blog/what-is-impedance-control-in-pcb/), align with your fabricator on etch tolerance capability and leave sufficient design margin.

</div>

### Soldermask exposure tutorial: more than “green paint”

Solder mask is the PCB’s “outer layer,” but its role goes far beyond aesthetics. It defines solderable areas and prevents solder bridging during assembly. HILPCB uses LDI (Laser Direct Imaging), which provides higher accuracy than traditional film exposure.

<div class="div-style-3">

#### Soldermask LDI process steps

1.  **Surface pretreatment**: Chemical cleaning plus mechanical brushing to increase surface roughness and ensure ink adhesion.
2.  **Ink coating**: In a cleanroom, apply liquid photoimageable soldermask evenly via automated screen printing or spray. Control thickness to 8–15 µm on pads and 20–30 µm on traces.
3.  **Pre-curing**: Short bake at 75–85°C to tack-dry the ink for LDI exposure.
4.  **LDI exposure**: Laser scans the soldermask directly (no film); registration can reach ±15 µm. This is critical for forming soldermask dams between fine-pitch parts (e.g., 0.4 mm BGA).
5.  **Developing**: Wash in developer; unexposed areas are removed to reveal pads.
6.  **Final curing**: Long bake in a tunnel oven at ~150°C to fully cure the soldermask for strong physical/chemical performance.

This is a classic **soldermask exposure tutorial**—the core is controlling energy and accuracy so soldermask dams don’t crack or shift.

## Drilling, plating, and PTH quality control

Vias are the “vertical highways” of multilayer boards, and their reliability is critical. The Stackup document defines via types (through, blind, buried) and sizes, which directly affect drilling and plating choices.

### Drilling: accuracy and hole-wall quality

High aspect-ratio holes (board thickness / hole diameter) are challenging for both drilling and plating. For example, drilling a 0.2 mm hole through a 2.0 mm board yields an aspect ratio of 10:1.

- **Drilling control**: HILPCB uses high-speed pneumatic spindles (>150k RPM) and X-Ray-assisted registration to ensure accurate inner-layer pad alignment in multilayer boards. For microvias (<0.15 mm), laser drilling is used.
- **Plasma de-smear**: Drilling heat can melt resin and form smear that covers inner-layer copper, degrading electrical connection. We use Plasma De-smear to remove resin residue from hole walls and ensure reliable copper adhesion in subsequent plating.

### PTH copper: the foundation of reliability

Copper thickness and uniformity inside holes largely determine whether a PCB survives thermal shock (e.g., soldering) and long-term operation. Industry standards such as IPC-6012 typically require average PTH copper thickness ≥ 20 µm.

- **Control method**: We build a conductive base layer with Electroless Copper, then thicken PTH and surface copper with Pattern Plating. HILPCB’s plating lines use advanced dynamic current control and high-circulation filtration to ensure dense, uniform deposits even in high-aspect-ratio holes.
- **Inspection**: Regular cross-section analysis with metallography microscopes measures PTH copper thickness and checks hole-wall quality to ensure there are no voids, cracks, or related defects.

## SMT soldering and assembly essentials

After the bare board is fabricated, the process moves into PCBA (Printed Circuit Board Assembly). Pad design, soldermask definition, and component placement—all defined in the Stackup document—directly affect SMT success.

### Stencil design: the origin of solder paste printing quality

Solder paste printing is the first SMT step and accounts for more than 60% of soldering defects. A good **smt stencil design tutorial** emphasizes that stencil design is decisive.

- **Aperture design**: Aperture size/shape determines paste volume. We follow area ratio (>0.66) and aspect ratio (>1.5) rules to prevent incomplete paste release. For fine parts such as 0201 and 0.4 mm BGA, electropolished or nano-coated stencils are used to improve release.
- **Thickness selection**: Stencil thickness (typically 100–150 µm) is chosen based on the smallest-pitch components on the board—a classic example of coupling design intent to process constraints.

### Reflow soldering: the art of temperature profiling

Reflow soldering permanently bonds components to the PCB. The core is precise profile control to activate flux, melt solder, and form reliable IMC.

<div class="div-style-1">

#### Process window: lead-free reflow temperature profile

- **Target**: Bright, full solder joints with no cold joints, opens, tombstoning, etc.
- **Input**: Solder paste datasheet (e.g., SAC305), PCB laminate/thickness, maximum component thermal mass.
- **Key parameters**:
    - **Preheat**: 150–180°C, 60–90 s, ramp gently to avoid thermal shock.
    - **Soak**: 180–210°C, 60–120 s, activate flux and equalize board temperature.
    - **Reflow**: Peak 240–250°C; time above liquidus (217°C) of 45–75 s.
    - **Cooldown**: Cooling rate < 4°C/s to form fine grain structure and ensure joint strength.
- **Inspection method**: HILPCB uses 3D SPI, 3D AOI, and X-Ray inspection for 100% monitoring of soldering quality.

</div>

## Cleaning, conformal coating, and reliability protection

For high-reliability applications (medical, automotive, aerospace), post-solder cleanliness and protection are critical.

- **Cleaning**: Even with “no-clean” flux, residues can cause electrochemical migration (ECM) in humid or high-voltage environments and lead to shorts. HILPCB offers aqueous cleaning and uses ion chromatography (IC) to verify cleanliness, ensuring ionic residue is below industry limits (e.g., IPC J-STD-001 requires <1.56 µg/cm² NaCl equivalent).
- **Conformal coating**: After cleaning and drying, selectively spraying a transparent conformal coating provides strong protection against humidity, salt fog, and mold, significantly extending lifetime in harsh environments.

## Testing matrix: making sure every node is correct

DFT must be applied end-to-end. If a product cannot be adequately tested, quality cannot be guaranteed. We use a staged testing matrix to ensure coverage.

| Test Stage | Test Method | Primary Goal | Coverage / defect types |
| :--- | :--- | :--- | :--- |
| **After bare-board fab** | Flying Probe Test (FPT) / Bed of Nails | Validate opens/shorts | 100% net connectivity; etch/drill defects |
| **After SMT** | 3D AOI | Inspect soldering appearance | Wrong/missing parts, polarity, cold joints, bridging, tombstoning |
| **SMT critical parts** | 3D X-Ray | Inspect hidden joints (BGA, QFN) | BGA shorts, voids, Head-in-Pillow (HoP) |
| **PCBA circuit level** | ICT | Check component parameters and nets | Wrong values, opens/shorts, digital logic functions |
| **PCBA functional level** | FCT | Simulate end use and validate functions | Firmware programming, I/O, interfaces, power |
| **System level** | SLT / Burn-in | Validate stability and performance in real conditions | Compatibility issues, intermittent faults, early failures |
| **Reliability validation** | HALT/HASS, temp-humidity cycling, vibration | Evaluate long-term reliability and margin | Weak points, potential failure modes |

This **testing matrix** is the backbone of our quality assurance—from microscopic solder joints to system-level functionality.

## Quality and traceability: the power of data

In modern manufacturing, quality is not “inspected in”; it is “built in” and “managed in.”

- **SPC (Statistical Process Control)**: We deploy SPC monitoring points across key steps such as etching, plating, and reflow to track process parameters (e.g., chemistry concentration, oven temperature) in real time. If trends drift, the system alerts immediately so engineers can intervene before defects become systemic.
- **MES (Manufacturing Execution System)**: HILPCB lines are fully managed by MES. Every PCB/PCBA has a unique QR code as its “ID card.” From incoming materials (managed by our smart warehousing system) to final shipment, all process data, equipment parameters, personnel information, and test results are bound to that QR code. This enables true end-to-end traceability: when issues are found, impact can be localized within minutes—whether it’s a specific component lot or an equipment-parameter anomaly during a time window.

<div class="cta-box">
    <p>A perfect Stackup design needs an equally strong manufacturing and test partner to make it real. HILPCB’s MES system and comprehensive test capability ensure your design intent is executed precisely and provide fully transparent traceability data. Want to see how your next project can benefit?</p>
    Upload your Gerber files now to get a DFM/DFT evaluation
</div>

## HILPCB’s integrated manufacturing + test capability

Turning a `stackup documentation guide` into a high-reliability electronic product requires advanced equipment, strict processes, and specialized expertise. HILPCB provides more than fabrication—we deliver a one-stop solution from design optimization through test validation.

<div class="div-style-6">

#### HILPCB core manufacturing and test capabilities

- **Advanced PCB fabrication**:
    - **Materials**: Supports high-frequency/high-speed materials such as Rogers, Taconic, and Isola.
    - **Processes**: 20+ layers, 0.15 mm mechanical microvias, laser blind/buried vias, step copper/step slots, backdrilling, gold fingers, and other complex builds.
    - **Precision control**: LDI exposure, plasma cleaning, X-Ray registration to ensure yield for [HDI](/blog/what-is-hdi-pcb/) builds.

- **Smart PCBA assembly**:
    - **Automated lines**: Fully automated paste printers, high-speed placement, and 12-zone reflow ovens; supports 01005 placement.
    - **Closed-loop inspection**: 3D SPI + 3D AOI + 3D X-Ray close the data loop and optimize printing/placement parameters in real time.
    - **Smart storage**: Temperature/humidity controlled intelligent storage to protect components—especially MSD parts.

- **Comprehensive test lab**:
    - **In-house test capability**: ICT/FCT development plus flying probe testers, high-resolution X-Ray, environmental chambers (temperature/humidity), vibration tables, salt-spray chambers, etc.
    - **Reliability services**: Complete **reliability checklist** validation, including thermal shock, mechanical shock, vibration tests, and HALT/HASS accelerated life testing.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

`stackup documentation guide` is the bridge between design and manufacturing. Understanding how it influences every downstream step—from etch compensation and reflow profiles to test-point planning—is a required skill for every great engineer. At HILPCB, we are not only the executor of your document but also your DFM/DFT partner. With process-driven, data-driven, and intelligent manufacturing and test systems, we ensure your design intent is implemented precisely and reliably—ultimately turning into products with strong market competitiveness.

> Need fabrication and assembly support? Contact HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT recommendations.

