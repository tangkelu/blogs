---
layout: post
title: "Flying Probe Best Practice a Technical Guide for PCB Testing"
date: 2023-10-25
image: /assets/img/pcba/test-fct.webp
description: "Flying Probe Testing (FPT) represents the industry standard for verifying Printed Circuit Board Assembly (PCBA) integrity without the high upfront cost of test"
---


# Flying Probe Best Practice a Technical Guide for PCB Testing

![Flying Probe Best Practice A Technical Guide for PCB Testing](/assets/img/pcba/test-fct.webp)

### Contents

- [1. Design for Test (DFT) Accessibility Rules](#1-design-for-test-dft-accessibility-rules)
- [2. Probe Pressure and Surface Interaction](#2-probe-pressure-and-surface-interaction)
- [3. Electrical Test Parameters and Vectorless Test](#3-electrical-test-parameters-and-vectorless-test)
- [4. Optimizing Throughput and Speed](#4-optimizing-throughput-and-speed)
- [5. High Voltage and Isolation (Hipot) Criteria](#5-high-voltage-and-isolation-hipot-criteria)
- [6. FCT Coverage Planning and Hybrid Strategies](#6-fct-coverage-planning-and-hybrid-strategies)
- [7. Handling False Failures and Troubleshooting](#7-handling-false-failures-and-troubleshooting)
- [8. Data Requirements for Programming](#8-data-requirements-for-programming)
- [9. Maintenance of the Flying Probe System](#9-maintenance-of-the-flying-probe-system)
- [Summary of Acceptance Criteria](#summary-of-acceptance-criteria)





<!-- COMPONENT: BlogQuickQuoteInline -->




### Highlights
- **Fixtureless Flexibility:** Eliminates the $2,000–$10,000 cost typical of ICT fixtures, enabling immediate testing upon design completion.
- **Precision Targeting:** Capable of probing pads as small as 0.15 mm (6 mil) with positioning accuracy often exceeding ±50 µm.
- **Dynamic Adaptation:** Allows for rapid program changes during the prototyping phase without hardware re-spins.

## 1. Design for Test (DFT) Accessibility Rules

The efficiency of a flying probe test is determined during the PCB layout phase. While FPT is more forgiving than In-Circuit Test (ICT), physical access limitations remain the primary cause of reduced test coverage.

### Pad Size and Spacing
To guarantee a reliable contact, the probe tip must land on a flat, conductive surface.
*   **Rule:** Maintain a minimum test pad diameter of **0.15 mm to 0.20 mm (6–8 mil)**.
*   **Why it matters:** Probes have a finite tip radius. Hitting a target smaller than 6 mil requires slowing the machine down significantly, reducing throughput, or risking a "glancing" contact that produces false open results.
*   **How to verify:** Run a DFT analysis in your CAD software (e.g., Altium, Cadence) specifically checking for "Testpoint Size."
*   **Common Pitfall:** Relying on component leads for probing. Probing directly on component legs (especially fine-pitch ICs) can cause bent leads or solder joint stress. Always prioritize dedicated test pads or vias.

### Via Tenting and Exposure
*   **Rule:** Do not tent vias intended for testing. The solder mask opening should be **0.05 mm (2 mil)** larger than the pad.
*   **Why it matters:** Tented vias are covered in insulating solder mask. The probe cannot penetrate this layer reliably without using excessive force, which damages the board.
*   **How to verify:** Check the Gerber solder mask layer. Ensure vias marked as test points have corresponding clearings.
*   **Common Pitfall:** Assuming the probe can pierce the mask. While "spearing" probes exist, they create debris and potential micro-fractures in the mask, leading to long-term reliability issues.

### Component Height and Shadowing
Flying probes move at high speeds and low angles. Tall components can block access to nearby pads.
*   **Rule:** Maintain a "keep-out" zone. For components taller than **15 mm**, ensure adjacent test points are spaced at least **2.0 mm** away.
*   **Why it matters:** The probe arm angle (typically 4° to 8°) creates a "shadow" behind tall capacitors or connectors where the probe cannot reach.
*   **How to verify:** Use 3D modeling tools to simulate probe angles against the [PCBA](https://aptpcb.com/en/pcba/) height profile.

## 2. Probe Pressure and Surface Interaction


![HDI PCB Close Up](/assets/img/pcb/hdi/pcb-hdi-pcb-hero.webp)


Physical interaction between the steel needle and the PCB surface is a critical variable. Excessive force damages pads; insufficient force yields unstable resistance readings.

### Managing Witness Marks
A "witness mark" is the small indentation left by the probe.
*   **Rule:** Witness marks should be visible under 10x magnification but must not expose the underlying copper substrate through the plating.
*   **Range:** Standard probe pressure is typically set between **10 g and 15 g**.
*   **Why it matters:** Deep indentations can compromise the planarity of the pad for future rework or assembly steps.
*   **How to verify:** Perform a visual inspection on the first article (FAI) using a microscope.
*   **Common Pitfall:** Using standard pressure on [HDI PCB](https://aptpcb.com/en/pcb/hdi-pcb/) micro-vias or soft finishes like Immersion Gold (ENIG), which can deform easily.

### Special Handling for Flex and Rigid-Flex
Flexible circuits require distinct mechanical settings.
*   **Rule:** Reduce probe pressure to **5 g – 8 g** and utilize a vacuum plate or specialized clamping system.
*   **Why it matters:** Flex materials (Polyimide) are compliant. Without proper support, the board moves away from the probe, causing intermittent contact.
*   **How to verify:** Monitor the "Z-axis over-travel" metric during setup.
*   **Common Pitfall:** Testing flex boards without a stiffener or vacuum fixture, leading to false "open" failures due to board deflection.

## 3. Electrical Test Parameters and Vectorless Test

Flying probe testers do not just check for shorts and opens; they perform in-circuit measurement of passive components.

### Resistance, Capacitance, and Inductance (R/l/c)
*   **Rule:** Set tolerance bands based on component datasheets, typically **±5% to ±10%**.
*   **Range:**
    *   **Resistance:** 1 Ω to 10 MΩ.
    *   **Capacitance:** 1 pF to 100 mF.
    *   **Inductance:** 1 µH to 10 H.
*   **Why it matters:** Verifies that the correct component value was placed.
*   **How to verify:** Compare measured values against the Bill of Materials (BOM).
*   **Common Pitfall:** Measuring small capacitors in parallel with low-impedance circuits. This requires "guarding" techniques (see below).

### Guarding and Phase Difference Measurement
In-circuit testing is complicated by parallel paths. If Resistor A is in parallel with Resistor B, the probe measures the equivalent resistance, not the individual value.
*   **Rule:** Apply guard points (virtual grounds) to isolate the component under test.
*   **Why it matters:** Without guarding, a 10kΩ resistor might read as 5kΩ if a parallel path exists, triggering a false failure.
*   **How to verify:** Review the test program's "Guard" list. Ensure the software has automatically identified parallel nets.

### Diode and Transistor Testing
*   **Rule:** Use junction verification tests.
*   **Range:** Forward voltage drop typically **0.3 V – 0.7 V**.
*   **Why it matters:** Confirms the orientation and functionality of active silicon.
*   **Common Pitfall:** LED testing requires specific current settings to avoid lighting the LED (which changes its resistance) or to verify it actually lights up (if using optical sensors).

## 4. Optimizing Throughput and Speed


![Rigid Flex PCB](/assets/img/pcb/rigid-flex/pcb-rigid-flex-pcb-hero-w480.webp)


One of the main criticisms of FPT is cycle time. While an ICT fixture tests a board in 30 seconds, a flying probe might take 15 minutes. Optimizing speed is essential for cost control.

### Adjacency and Net Grouping
*   **Rule:** Limit isolation testing to "adjacent" nets rather than testing every net against every other net.
*   **Why it matters:** Testing N nets against N nets creates N² combinations. Testing only physically adjacent nets (based on CAD data) reduces steps by 90%+.
*   **How to verify:** Ensure the CAD import (ODB++ or IPC-D-356) includes accurate X-Y coordinate data for adjacency calculation.

### Probe Travel Optimization
*   **Rule:** Sort test steps to minimize total probe travel distance.
*   **Range:** Efficient machines achieve **40 – 80 tests per second**.
*   **Why it matters:** Random test ordering forces the arm to traverse the entire board repeatedly.
*   **How to verify:** Run the "path optimization" algorithm in the FPT software suite before finalizing the program.

## 5. High Voltage and Isolation (Hipot) Criteria

For power electronics, standard isolation testing is insufficient. You must validate dielectric strength.

### Hipot Criteria Explained
High Potential (HiPot) testing applies high voltage to stress the insulation.
*   **Rule:** Apply voltage between primary (high voltage) and secondary (low voltage) circuits.
*   **Range:** Typically **250 V DC to 1000 V DC** for PCB level testing.
*   **Leakage Limit:** Fail if leakage current exceeds **1 mA** (or specific safety standard).
*   **Why it matters:** Detects solder balls, flux residue, or compromised laminate that might arc under load.
*   **How to verify:** Use a dedicated HiPot sequence within the FPT program.
*   **Common Pitfall:** Applying HiPot voltage to nets containing sensitive low-voltage ICs. These nets must be strictly excluded or guarded.

## 6. FCT Coverage Planning and Hybrid Strategies

Flying probe is rarely a standalone solution for complex digital products. It is best used in a hybrid strategy.

### FCT Coverage Planning
Functional Circuit Test (FCT) verifies the board actually *works*, whereas FPT verifies it was *built correctly*.
*   **Rule:** Offload power-up tests and firmware flashing to [FCT Test](https://aptpcb.com/en/pcba/fct-test/) stations.
*   **Why it matters:** FPT is slow at functional logic testing. Using FPT for simple structural integrity (shorts/opens/values) and FCT for performance creates the most efficient line.
*   **Strategy:**
    1.  **FPT:** 100% Shorts/Opens, Passive Values, Diode orientation.
    2.  **FCT:** Voltage rail verification, communication protocols (I2C/SPI), memory read/write.

### The "Cluster" Test Approach
*   **Rule:** If individual component access is impossible (e.g., BGA bypass caps), test the "cluster" functionality.
*   **Why it matters:** You cannot probe under a BGA.
*   **How to verify:** Use boundary scan (JTAG) integration if the FPT machine supports it, or rely on X-ray inspection for the hidden joints.

## 7. Handling False Failures and Troubleshooting

False failures (pseudofailures) kill efficiency by forcing operators to re-test good boards.

### Oxidation and Contact Resistance
*   **Rule:** Implement an automatic "retry" with increased pressure or a "scrub" motion.
*   **Why it matters:** Oxidized pads (common on OSP finishes stored improperly) present high resistance.
*   **Range:** Retry limit usually set to **3 attempts**.
*   **Solution:** Ensure proper storage of bare boards or use [HASL/ENIG finishes](https://aptpcb.com/en/pcb/pcb-surface-finishes/) which are more resistant to oxidation than OSP.

### Component Tolerance Drift
*   **Rule:** Adjust test limits for specific batches if the manufacturer tolerance is wide.
*   **Why it matters:** A 10kΩ resistor with ±1% tolerance is different from one with ±5%. If the BOM specifies 1%, but the procurement team bought 5% (with approval), the program must be updated.
*   **How to verify:** Review the Approved Vendor List (AVL) deviations before production.

## 8. Data Requirements for Programming

Garbage in, garbage out. The quality of the FPT program depends entirely on the input data.

### Preferred Formats
1.  **ODB++:** The gold standard. Contains intelligent data on net names, component layers, and drill files.
2.  **IPC-D-356:** Essential for netlist comparison.
3.  **Gerber (RS-274X):** Visual data only; requires manual definition of test points (slow and error-prone).

### Bom Integration
*   **Rule:** The BOM must match the CAD reference designators exactly.
*   **Why it matters:** If the CAD says R101 is 10kΩ but the BOM says DNI (Do Not Install), the tester will fail the board for an "Open" circuit.
*   **How to verify:** Perform a BOM-to-CAD cross-check prior to programming. Use tools like a [BOM Viewer](https://aptpcb.com/en/tools/bom-viewer/) to visualize placement.

## 9. Maintenance of the Flying Probe System

To maintain the **±50 µm** accuracy required for modern electronics, the machine itself requires strict maintenance.

*   **Probe Tip Replacement:** Tips wear out. Replace them every **50,000 – 100,000 hits** or if visual inspection shows blunting.
*   **Camera Calibration:** Optical alignment systems drift. Recalibrate fiducial recognition cameras weekly.
*   **Rail Cleaning:** Dust and debris on the motion rails affect speed and accuracy. Clean and lubricate according to OEM schedules (usually monthly).

## Summary of Acceptance Criteria

When evaluating a Flying Probe Test process, use this checklist to ensure A-grade quality control:

1.  **Coverage Report:** Does the report explicitly state the % of nets tested vs. untestable? (Target > 90%).
2.  **Witness Marks:** Are they centered on pads and non-destructive?
3.  **False Call Rate:** Is the false failure rate below **5%**? (Higher rates indicate poor programming or dirty fixtures).
4.  **Cycle Time:** Is the test time consistent with the estimated steps/second?
5.  **Data Logging:** Are test results serialized and logged for traceability?

By strictly following these parameters—ranging from the **6 mil** pad limit to the **1000 V** isolation threshold—manufacturers can leverage flying probe technology to deliver defect-free PCBAs. This balance of design foresight (DFT) and operational precision ensures that even the most complex [Aerospace and Defense PCBs](https://aptpcb.com/en/industries/aerospace-defense-pcb/) meet rigorous reliability standards.
