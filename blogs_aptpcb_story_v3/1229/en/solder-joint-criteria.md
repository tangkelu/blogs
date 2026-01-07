---
layout: post
title: "Solder Joint Criteria: IPC Standards and Acceptance Rules for PCB Assembly"
date: 2023-10-25
image: /assets/img/about/about-pcba-SPI-Solder-Paste-Inspection.webp
description: "A comprehensive guide to solder joint criteria based on IPC-A-610 standards. Learn the acceptance limits for SMT, THT, and BGA components to ensure Class 3 reliability."
keywords: "solder joint criteria, IPC-A-610, PCB assembly standards, SMT acceptance, THT solder fill, BGA voiding limits"
---

# Solder Joint Criteria: IPC Standards and Acceptance Rules for PCB Assembly

![Solder Joint Criteria: IPC Standards and Acceptance Rules for PCB Assembly](/assets/img/about/about-pcba-SPI-Solder-Paste-Inspection.webp)

### Contents

- [Understanding IPC Classifications](#understanding-ipc-classifications)
- [General Solder Physics and Wetting](#general-solder-physics-and-wetting)
- [Surface Mount (SMT) Chip Components](#surface-mount-smt-chip-components)
- [Gull-Wing Lead Criteria (Soic, QFP, Sot)](#gull-wing-lead-criteria-soic-qfp-sot)
- [J-Lead Component Criteria](#j-lead-component-criteria)
- [Bottom Termination Components (Btc/qfn)](#bottom-termination-components-btcqfn)
- [Through-Hole (THT) Criteria](#through-hole-tht-criteria)
- [Common Defects and Rejection Criteria](#common-defects-and-rejection-criteria)
- [Inspection Technologies and Verification](#inspection-technologies-and-verification)
- [Design for Manufacturability (DFM) Impact](#design-for-manufacturability-dfm-impact)
- [Summary of Critical Numeric Ranges](#summary-of-critical-numeric-ranges)





<!-- COMPONENT: BlogQuickQuoteInline -->



















### Highlights
- **IPC Class Definitions:** Differences between Class 1, 2, and 3 acceptance levels.
- **SMT Rules:** Specific limits for overhang, fillet height, and joint width.
- **THT Requirements:** Vertical fill percentages and circumferential wetting rules.
- **Defect Identification:** How to distinguish between cosmetic anomalies and functional failures.
- **Inspection Metrics:** Concrete numeric ranges for BGA voiding and pin protrusion.

## Quick Answer: Key Acceptance Thresholds

The following table summarizes the most critical numeric limits for solder joints across different component technologies and IPC classes.

| Feature | Class 2 (Industrial) | Class 3 (High Reliability) |
| :--- | :--- | :--- |
| **THT Vertical Fill** | Minimum 50% | Minimum 75% |
| **THT Circumferential Wetting** | 180° (Destination Side) | 270° (Destination Side) |
| **Chip Component Side Overhang** | Max 50% of Pad Width | Max 25% of Pad Width |
| **Gull-Wing Heel Fillet** | Solder Thickness (G) + 50% Lead Thickness (T) | G + 100% T (or Lead Thickness) |
| **BGA Voiding (X-Ray)** | < 25% of Ball Area | < 25% of Ball Area |
| **Maximum Solder Ball Size** | Must maintain electrical clearance | Must maintain electrical clearance |
| **Wetting Angle** | $\le$ 90° | $\le$ 90° |




## Understanding IPC Classifications

Before applying specific solder joint criteria, you must establish the target classification for the [PCB assembly](/en/pcba/). The IPC-A-610 standard divides electronic assemblies into three classes.

### Class 1: General Electronic Products
These are consumer products where the primary requirement is function. Cosmetic imperfections are generally acceptable if the device works. Examples include toys and cheap consumer electronics.

### Class 2: Dedicated Service Electronic Products
This class includes communications equipment, business machines, and instruments where high performance and extended life are required. Uninterrupted service is desired but not critical.

### Class 3: High Performance/harsh Environment Electronic Products
This category covers equipment where downtime cannot be tolerated, or the environment is exceptionally harsh. Examples include [aerospace and defense PCBs](/en/industries/aerospace-defense-pcb/), medical life support systems, and automotive safety components. The solder joint criteria for Class 3 are the strictest to ensure joints survive thermal cycling and vibration.

## General Solder Physics and Wetting

Regardless of the component type, all solder joints must exhibit proper wetting. Wetting indicates that the molten solder has formed an intermetallic compound (IMC) with the base metal of the pad and the component lead.

### The 90-Degree Rule
*   **Rule:** The contact angle between the solder fillet and the termination or pad must be **$\le$ 90°**.
*   **Why it matters:** An angle greater than 90° (non-wetting or de-wetting) indicates that the solder is sitting on top of the surface rather than bonding with it. This leads to weak mechanical connections and potential open circuits.
*   **How to verify:** Visual inspection using magnification. The solder should feather out to a thin edge.
*   **Common Failure:** Contaminated pads or oxidized leads prevent the solder from flowing, resulting in a convex "bead" shape rather than a concave fillet.

### Imc Thickness
*   **Range:** A proper IMC layer is typically **1 to 4 µm** thick.
*   **Why it matters:** Too thin, and the bond is weak. Too thick (often caused by excessive heat or multiple reflows), and the joint becomes brittle and prone to fracture under shock.

## Surface Mount (SMT) Chip Components

Chip components (resistors, capacitors, inductors) are the most common parts on a board. Their rectangular shape relies on a 5-sided termination. The criteria focus on how the component aligns with the pad and the volume of solder connecting them.

### 1. Side Overhang (a)
Side overhang occurs when the component width extends beyond the side of the pad.
*   **Class 2 Limit:** Maximum **50%** of the component termination width (W) or 50% of the pad width (P), whichever is less.
*   **Class 3 Limit:** Maximum **25%** of the component termination width (W) or 25% of the pad width (P).
*   **Why it matters:** Excessive overhang reduces the contact area, weakening the shear strength of the joint.

### 2. End Overhang (B)
End overhang refers to the component extending off the end of the pad (longitudinally).
*   **Rule:** Not permitted for any class. The component termination must overlap the pad.
*   **How to verify:** The component termination must be fully seated on the pad metallization.

### 3. End Joint Width (C)
This is the width of the solder joint at the narrowest point.
*   **Class 2:** Minimum **50%** of the component termination width.
*   **Class 3:** Minimum **75%** of the component termination width.
*   **Why it matters:** This dimension ensures there is enough solder volume to handle current and mechanical stress.

### 4. Side Joint Length (D)
This measures the length of the solder fillet along the side of the component termination.
*   **Class 2:** Not required (optional).
*   **Class 3:** Minimum length is required. It must be distinguishable.
*   **Why it matters:** For high-reliability environments, side fillets add significant mechanical stability against twisting forces.

### 5. Fillet Height (E)
*   **Maximum:** Solder can cover the top of the termination but should not touch the component body (top side).
*   **Minimum:** The solder must wet at least **25%** of the termination height (H) or **0.5 mm**, whichever is less.
*   **Common Failure:** "Insufficient solder" where the fillet is concave but too low, failing to grasp the vertical face of the termination.

## Gull-Wing Lead Criteria (Soic, QFP, Sot)

Gull-wing leads are common on Integrated Circuits (ICs). The critical feature here is the "heel fillet," which bears the brunt of thermal expansion stress.

### Heel Fillet Requirements
The heel is the inner bend of the lead.
*   **Class 2:** The solder fillet must reach at least the solder thickness (G) plus **50%** of the lead thickness (T) at the heel.
*   **Class 3:** The solder fillet must reach at least the solder thickness (G) plus **100%** of the lead thickness (T).
*   **Why it matters:** Cracks almost always initiate at the heel. A robust heel fillet extends the fatigue life of the joint.

### Side Overhang for Gull-Wing
*   **Class 2:** Maximum **50%** of lead width.
*   **Class 3:** Maximum **25%** of lead width.
*   **Note:** The toe (end of the lead) can overhang the pad provided the minimum joint length is met, but side overhang is strictly controlled to prevent bridging.

## J-Lead Component Criteria

J-leads (common on PLCCs and some tantalum capacitors) have the termination rolled under the body.

*   **Heel Fillet:** Similar to gull-wing, the heel is critical. Class 3 requires the fillet to extend to **100%** of the lead thickness.
*   **Side Joint Length:** For Class 3, the side joint length must be at least **150%** of the lead width (W).
*   **Verification:** These are harder to inspect visually because the lead is under the body. Often requires tilted inspection angles or X-ray.

## Bottom Termination Components (Btc/qfn)

[BGA, QFN, and fine-pitch](/en/pcba/bga-qfn-fine-pitch/) components present unique challenges because the connections are hidden underneath the package.

![HDI PCB with Fine Pitch Components](/assets/img/pcb/hdi/pcb-hdi-pcb-hero.webp)

### Voiding Limits
Voids are air pockets trapped inside the solder joint.
*   **Rule:** For BGA and BTC components, the projected void area must be **< 25%** of the total ball/pad area.
*   **Why it matters:** While small voids can actually stop cracks from propagating, large voids reduce thermal conductivity and electrical cross-section.
*   **How to verify:** This requires [X-ray inspection](/en/pcba/xray-inspection/). Visual inspection cannot detect voiding.

### Wettable Flanks
Many modern QFNs feature "wettable flanks"—exposed copper on the side of the package.
*   **Requirement:** If the manufacturer specifies wettable flanks, a visible side fillet is required for Class 3 acceptance.
*   **Benefit:** This allows for [AOI inspection](/en/pcba/aoi-inspection/) of the joint, reducing the reliance on X-ray for every single board.

## Through-Hole (THT) Criteria

Despite the dominance of SMT, [Through-Hole Technology](/en/pcba/smt-tht/) remains vital for connectors and heavy components. The criteria focus on how well the solder fills the plated through-hole (barrel).

### Vertical Fill of Barrel
*   **Class 2:** Minimum **50%** vertical fill.
*   **Class 3:** Minimum **75%** vertical fill.
*   **Why it matters:** The barrel fill provides the mechanical anchor. Incomplete fill leaves air pockets that can expand during operation, causing "blow holes" or barrel cracks.
*   **Common Failure:** Insufficient heat applied to the pin, causing the solder to freeze before it flows up the barrel.

### Circumferential Wetting
This measures how much of the lead and barrel circumference is wetted by solder.
*   **Source Side (Solder Side):** Class 2 and 3 require **270°** wetting.
*   **Destination Side (Component Side):**
    *   **Class 2:** Minimum **180°** wetting.
    *   **Class 3:** Minimum **270°** wetting.
*   **Verification:** You must see the solder rise through the board and wet the pad on the top side.

### Pin Protrusion
*   **Class 2 & 3 Min:** The lead end must be visible in the solder fillet.
*   **Class 3 Max:** Typically **1.5 mm** (unless otherwise specified by design).
*   **Why it matters:** Long leads can cause shorts to chassis or interfere with subsequent assembly steps.

## Common Defects and Rejection Criteria

Understanding what constitutes a defect is as important as knowing the acceptance criteria.

### 1. Cold Solder
*   **Appearance:** Dull, grainy, porous surface.
*   **Cause:** Insufficient heat or movement during cooling.
*   **Status:** **Defect** for all classes. The electrical connection is unreliable.

### 2. Disturbed Solder
*   **Appearance:** Wrinkled surface, similar to cold solder but often with distinct cooling lines.
*   **Cause:** The joint moved while the solder was solidifying.
*   **Status:** **Defect** for all classes.

### 3. Solder Bridging
*   **Appearance:** Solder connecting two conductors that should be electrically isolated.
*   **Cause:** Excessive solder paste volume, poor stencil design, or component misalignment.
*   **Status:** **Defect** for all classes (Short circuit).

### 4. Solder Balls
*   **Rule:** Solder balls are defects if they are not encapsulated (stuck in conformal coating) or if they violate minimum electrical clearance (MEC).
*   **Numeric Limit:** Generally, loose balls larger than **0.13 mm** are flagged, but any loose ball is a risk in high-vibration environments.
*   **Why it matters:** Loose balls can dislodge and cause shorts elsewhere on the board.

### 5. Tombstoning
*   **Appearance:** A chip component standing vertically on one end.
*   **Cause:** Uneven wetting forces (one pad melts before the other).
*   **Status:** **Defect** for all classes (Open circuit).

## Inspection Technologies and Verification

To enforce these criteria, manufacturers use a combination of inspection methods.

### Automatic Optical Inspection (AOI)
AOI systems use cameras and lighting algorithms to check for:
*   Component presence/absence.
*   Polarity.
*   Solder fillet shape (meniscus).
*   Bridging.
*   **Limitation:** Cannot see hidden joints (BGA, QFN) or measure internal barrel fill accurately.

### X-Ray Inspection (Axi)
Essential for [BGA and QFN inspection](/en/pcba/bga-qfn-fine-pitch/).
*   **Checks:** Void percentage, head-in-pillow defects, and shorting under the package.
*   **Metric:** Calculates the exact void percentage per ball (e.g., 12% voiding is Pass, 28% is Fail).

### Solder Paste Inspection (SPI)
Occurs before component placement.
*   **Range:** Paste volume should typically be **40% to 160%** of the theoretical stencil aperture volume.
*   **Why it matters:** Most solder defects (up to 70%) originate from the printing process. Catching volume issues here prevents bridging or opens later.

## Design for Manufacturability (DFM) Impact

Meeting solder joint criteria starts with design. If the [PCB layout](/en/pcb/pcb-quality/) does not follow DFM guidelines, even the best assembly process will fail.

1.  **Pad Size:** Pads must be large enough to allow the required heel and side fillets. A pad that is exactly the size of the lead often results in insufficient fillets.
2.  **Thermal Relief:** For THT components connected to large copper planes, thermal relief spokes are mandatory. Without them, the heat dissipates into the plane, preventing the solder from flowing up the barrel to meet the **75% fill** requirement.
3.  **Aspect Ratio:** For THT, the ratio of board thickness to hole diameter should ideally be less than **8:1** to ensure proper plating and solder flow.

## Summary of Critical Numeric Ranges

To achieve Class 3 reliability, keep these 12 ranges in mind:

1.  **Wetting Angle:** $\le$ 90°.
2.  **IMC Thickness:** 1–4 µm.
3.  **THT Vertical Fill (Class 3):** $\ge$ 75%.
4.  **THT Circumferential Wetting (Class 3):** 270°.
5.  **Chip Side Overhang (Class 3):** $\le$ 25% of pad width.
6.  **Chip End Joint Width (Class 3):** $\ge$ 75% of termination width.
7.  **Gull-Wing Heel Fillet (Class 3):** Lead thickness + Solder thickness.
8.  **BGA Voiding:** < 25% of area.
9.  **Solder Ball Diameter:** < 0.13 mm (general guideline for clearance).
10. **Pin Protrusion (Class 3):** Max 1.5 mm.
11. **Solder Paste Volume:** 40%–160% of aperture.
12. **Maximum Bow/Twist:** 0.75% (for SMT assembly).

By strictly adhering to these solder joint criteria, manufacturers ensure that the final PCBA will withstand the rigors of its operating environment. Whether you are building a simple IoT device or a complex aerospace controller, the quality of the solder joint is the foundation of product success.

For more information on ensuring quality in your builds, explore our [quality control systems](/en/pcb/pcb-quality/) or review our [DFM guidelines](/en/resources/dfm-guidelines/) to optimize your layout for perfect soldering.
