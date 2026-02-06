---
title: "X-Ray Inspection Checklist: PCB Manufacturing and Quality Management White Paper"
description: "Detailed explanation of x-ray inspection checklist process capability indices, yield improvement, quality tools, test coverage and traceability practices, with DFM/DFT/DFR checklists helping customers establish collaboration mechanisms."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 9
tags: ["x ray inspection checklist", "BGA inspection", "void detection", "non-destructive testing", "IPC-A-610", "pcb manufacturing whitepaper"]
---
## 1. Executive Summary: Quality Objectives and Business Metrics

In today’s highly complex and miniaturized electronics market, PCB manufacturing and assembly quality is the foundation that determines a product’s final performance, reliability, and lifecycle. Even a tiny manufacturing defect—especially hidden defects under bottom-terminated components such as BGA and QFN—can trigger catastrophic field failures, leading to costly recalls and reputational damage.

HILPCB’s operational excellence philosophy is: **quality is designed and manufactured, not inspected into existence**. This white paper systematically explains how HILPCB puts that philosophy into practice through data-driven process control, advanced quality tools, comprehensive test strategies, and collaborative design mechanisms. With “**x ray inspection checklist**” as the core lens, we will take a deep look at how we ensure quality-critical items that cannot be reached by the naked eye or traditional optical inspection.

Our quality system is not only built for compliance, but also to exceed customer expectations. All operations are driven by the following core business metrics:

*   **First Pass Yield (FPY):** > 99.5%
*   **Critical process capability index (CPK):** > 1.67 (6-Sigma level)
*   **Customer complaint rate (PPM):** < 100
*   **On-Time Delivery (OTD):** > 98%

This white paper will show how HILPCB turns these metrics from goals into reality through a closed-loop quality system that integrates manufacturing, inspection, traceability, and collaborative design—helping your products achieve a strong competitive advantage in the market.

<div class="div-style-6">
    <h4>HILPCB Manufacturing Capability Overview</h4>
    <p>We integrate full-stack services from bare PCB fabrication to component sourcing, SMT assembly, and functional testing. With a unified quality management system and data platform, we eliminate information silos and accountability gaps typical of multi-supplier models, providing customers with a transparent, efficient, and reliable end-to-end manufacturing solution. This enables us to take full responsibility for final product quality and continuously optimize the entire value chain.</p>
</div>

## 2. Manufacturing Capability Data: From Specification to Mass-Production Commitment

Process capability has true business value only when it is validated in sustained, stable mass production. HILPCB’s manufacturing capability is not just reflected in limit specifications, but in precise control of the process window at scale. The table below shows selected core processes, key performance indicators (KPI), and real mass-production references.

| Process/Category | HILPCB Core Capability | Key Performance Indicators (KPI) | Mass-Production Reference |
| :--- | :--- | :--- | :--- |
| **Bare PCB fabrication** | Min trace/space: 2.5/2.5 mil | Etch uniformity: ±5% | 28-layer server motherboard; impedance control accuracy ±7% |
| | Min mechanical drilling: 0.15mm | Hole position accuracy: ±0.05mm | Medical endoscope HDI board; laser drilling |
| | Max layer count: 32 layers | Lamination registration accuracy: ±3 mil | 5G base-station antenna boards |
| | Surface finish: ENIG, OSP, HASL, Immersion Silver/Tin | ENIG gold thickness: 2-5μ" | Automotive radar sensors requiring high-reliability soldering |
| **SMT assembly** | Min component size: 01005 | Placement accuracy: ±25μm @ 6σ | Wearable health monitoring devices |
| | Min BGA/CSP pitch: 0.35mm | Solder voiding (X-Ray): <10% (IPC Class 3) | High-performance computing GPU modules |
| | PoP (Package on Package) stacking | Stack coplanarity: <0.05mm | Smartphone main processor boards |
| | Automated solder paste inspection (3D SPI) | Volume/area/height repeatability: <3% | Standard across all lines to prevent solder defects |
| **Quality inspection** | 3D Automated Optical Inspection (AOI) | False Call Rate: <200 PPM | Covers 100% SMT solder joints |
| | 3D Automated X-ray Inspection (AXI) | Defect capture rate: >99.5% (for BGA/QFN) | High-reliability products such as automotive electronics and aerospace |
| | In-Circuit Test (ICT) / Flying probe test | Test coverage: >90% (for net connectivity) | Industrial control motherboards to ensure correct component parameters |
| | Functional Test (FCT) | FPY: >98% | Consumer electronics finished products; simulating end-user scenarios |

## 3. Quality Tools: Building a Data-Driven Prevention System

Prevention is better than correction. HILPCB’s quality management system deeply integrates industry-leading statistical and analytical tools, shifting quality control from “after-the-fact inspection” to “prevention in advance” and “in-process control”.

*   **Statistical Process Control (SPC):** We deploy SPC monitoring points at key processes such as solder paste printing, reflow soldering, and wave soldering. By plotting X-bar, R-chart and other control charts in real time, we can detect small process drifts immediately and intervene before they evolve into defects. For example, reflow oven temperature profiles are monitored continuously, and any fluctuation beyond preset control limits triggers an alert.

*   **Process Capability Index (CPK):** CPK is the gold standard for measuring whether our manufacturing process can meet specification tolerances. We set an internal target of CPK > 1.67 for critical dimensions and parameters (e.g., placement accuracy, solder paste volume). This means the process is tightly centered relative to the specification and has minimal variation, providing sufficient margin to handle normal material and environmental fluctuation.

*   **Measurement System Analysis (MSA):** “If you cannot measure it, you cannot improve it.” MSA ensures that our measurement tools (e.g., AOI, AXI, CMM) are accurate and reliable. We regularly conduct Gage R&R (repeatability and reproducibility) studies to ensure that measurement-system variation is far smaller than process variation, thereby ensuring SPC and CPK data is valid.

*   **8D problem solving:** Although we focus on prevention, when an anomaly occurs a structured and efficient resolution process is critical. We use the 8D methodology to form a cross-functional team and go from problem description and containment to root cause analysis (RCA), permanent corrective actions, and verification. This creates a complete closed loop, and we feed lessons learned into our FMEA (Failure Mode and Effects Analysis) database to prevent recurrence.

*   **Digital quality dashboards:** In our production workshops, large digital boards show real-time FPY, overall equipment effectiveness (OEE), PPM, and other key metrics for each line. This transparency empowers on-site engineers and operators to make decisions based on real-time data, and also demonstrates our commitment to quality and efficiency to visiting customers.

## 4. SMT/Assembly Process Capability and Defect Control: Focus on the X-Ray Inspection Checklist

As bottom-terminated packages with thermal pads such as BGA, QFN, and LGA become common, their solder joints are hidden under the package and traditional AOI can no longer address them. As a result, X-ray inspection has shifted from an “optional” item to a “must-have” in high-reliability electronics manufacturing. HILPCB treats X-ray inspection as a core process for ensuring hidden solder-joint quality, and has established a detailed internal checklist.

**Our inspection strategy is the “SPI + AOI + AXI” triad:**
1.  **3D SPI (Solder Paste Inspection):** Control at the source. Inspect solder paste volume, area, height, and offset at 100% to ensure the “raw material” for soldering is perfect.
2.  **3D AOI (Automated Optical Inspection):** After reflow, inspect all visible joints at 100%, including component offset, wrong parts, tombstoning, polarity errors, etc.
3.  **AXI (Automated X-ray Inspection):** For all invisible solder joints, execute our strict `x ray inspection checklist`.

<div class="div-style-1">
    <h4>Capability highlight: 3D AXI and the IPC-A-610 Class 3 standard</h4>
    <p>HILPCB invests in advanced 3D X-ray inspection equipment that can perform tomography on solder joints and accurately calculate void (Void) volume percentage, not just 2D area. For high-reliability applications such as automotive, medical, and aerospace, we strictly follow the <strong>IPC-A-610 Class 3</strong> standard to ensure that the maximum voiding in BGA joints does not exceed 10% of the solder ball area—far stricter than the common 25% industry practice. This is a concrete demonstration of our zero-defect commitment.</p>
</div>

**Core items in HILPCB’s X-Ray Inspection Checklist:**

*   **BGA/CSP solder joint quality:**
    *   **Voiding (Voiding):** Check bubble size and percentage inside each solder ball. Are microvoids present (Microvoids)? Does the maximum void exceed IPC limits?
    *   **Bridging/shorts (Bridging/Shorts):** Check whether unintended solder connections exist between adjacent solder balls.
    *   **Opens/head-in-pillow (Opens/Head-in-Pillow):** Check whether solder balls are fully wetted to pads and whether intermittent/partial connections exist.
    *   **Solder ball size and shape consistency:** Check whether all solder balls have uniform collapsed size and roundness, reflecting heating uniformity.
    *   **Alignment (Alignment):** Check alignment between BGA balls and PCB pads.

*   **QFN/LGA and bottom thermal pads:**
    *   **Center-pad voiding:** This is critical for heat dissipation and grounding. Check the overall voiding level of the large center pad and ensure it is below 25% or the customer-specified requirement to guarantee good thermal and electrical performance.
    *   **Side-joint wetting (Wetting):** For QFNs with wettable flanks, check whether solder wets and climbs properly.

*   **Through-hole fill (PTH/Via Fill):**
    *   For via-in-pad structures used for high-current conduction or PoP stacking, check the fill condition inside the via to ensure there is no voiding or under-fill, avoiding potential reliability risks.

*   **Internal structure and wire bonding:**
    *   During component failure analysis, X-ray can be used to check whether internal wire bonding (Wire Bonding) is broken or shifted.

This checklist is not only an inspection standard; it is also the basis for optimizing reflow profiles, stencil design, and solder paste selection. By continuously analyzing X-ray data, we can keep improving the process and reduce defect generation at the root.

## 5. Test Coverage: Building a Multi-Layer Quality Safety Net

No single test method can guarantee 100% defect coverage. HILPCB uses a layered, complementary testing strategy—from component-level checks to full functional validation—to build a comprehensive quality safety net and catch potential issues at every stage of the product lifecycle.

| Test Method | Description and Purpose | Typical Coverage | Primary Defects Detected | Applicable Stage/Product |
| :--- | :--- | :--- | :--- | :--- |
| **Automated Optical Inspection (AOI)** | Image-based comparison to check visible appearance defects after placement. | 99% (visible defects) | Missing parts, wrong parts, offset, polarity errors, tombstoning, visible cold joints | After SMT reflow |
| **Automated X-ray Inspection (AXI)** | Uses X-ray penetration to inspect invisible solder joints. | >99.5% (BGA/QFN) | BGA voiding, bridging, opens, head-in-pillow | After SMT reflow; high-density boards |
| **In-Circuit Test (ICT)** | Contacts predefined test points to check component values and net opens/shorts. | 85-95% (component level) | Wrong values, reversed parts, opens, shorts | After assembly; mass production |
| **Flying Probe** | No expensive fixture; movable probes contact test points. | 80-90% (net level) | Opens, shorts, basic component verification | NPI, prototyping, small batches |
| **Functional Test (FCT)** | Simulates the final operating environment to validate designed functions. | 100% (functional spec) | Software bugs, logic errors, performance failures, signal integrity issues | After final assembly |
| **Hipot Test** | Applies high voltage to verify insulation strength and electrical safety. | 100% (safety spec) | Dielectric breakdown, insufficient clearance | Power/high-voltage products |
| **Burn-in** | Runs for a long time under stress such as high temperature to trigger early-life failures. | N/A | Early component failures; latent solder issues | High-reliability products such as medical, defense, and servers |
| **Ongoing Reliability Test (ORT)** | Temperature cycling, vibration, drop, etc., to validate long-term reliability. | N/A | Insufficient design margin, material fatigue, structural issues | Design validation; sampling in mass production |

## 6. Traceability System: From Data Lake to Visual Insights

When a quality issue occurs, fast and accurate root-cause localization is key to controlling losses and improving processes. HILPCB’s end-to-end traceability system treats each PCBA as an individual unit with a complete “lifecycle record”.

*   **Unique identity:** Each board (or panel) is assigned a unique QR code or barcode serial number at the start of production.
*   **Data capture and association:** At every key node—solder paste printing, placement, reflow, AOI/AXI inspection, ICT/FCT testing—all relevant equipment parameters, material lot IDs, operator information, inspection images, and test data are automatically captured and bound to the serial number.
*   **Centralized data lake:** All data is aggregated into a centralized data lake. This is not just static record-keeping, but a dynamic “data goldmine” for analysis.
*   **Visualization and analytics:** For a field-return unit, we can scan the serial number and, within seconds:
    *   **Trace its “genealogy”:** Which bare-PCB lot and which component reel/lot was used.
    *   **Replay its “health report”:** Review SPI data, reflow oven profiles, and the raw AOI and X-ray images.
    *   **Analyze peer performance:** Quickly query other products from the same build and determine whether the issue is systemic—precisely bounding risk and avoiding unnecessary expanded recalls.

This powerful traceability system is the foundation of transparency and accountability advocated in the `pcb manufacturing whitepaper`, and a strong tool for conducting joint root-cause analysis with customers.

## 7. DFM/DFT/DFR Checklist: Customer Collaboration Starts at Design

The most effective quality control starts in the design stage. A poorly considered design can lead to low manufacturing yield, test difficulty, and even long-term reliability risks. HILPCB strongly advocates early collaboration with customers. Through our detailed DFM/DFT/DFR checklist, we help customers identify and avoid potential risks before design release.

<div class="div-style-3">
    <h4>Improvement path: from manufacturability to exceptional reliability</h4>
    <p>We provide more than a checklist—we provide a collaborative improvement framework. Based on your Gerber and BOM files, our engineers deliver a detailed analysis report that highlights potential risks and provides actionable optimization recommendations. This early communication typically shortens prototyping by <strong>1-2 rounds</strong> and improves mass-production FPY by <strong>3-5%</strong>.</p>
</div>

Below is a summary of selected checklist items (over 100 check points in total):

| Category | Check Item | Design Recommendation/Purpose |
| :--- | :--- | :--- |
| **DFM (Manufacturability)** | **Component placement** | Avoid placing tall parts close to the board edge; leave enough clamping/transport clearance (≥3mm). |
| | | Place polarized components in consistent orientations to reduce placement head rotation and improve efficiency. |
| | | Distribute heavy components evenly to avoid PCB warpage. |
| | **Pad design** | Use NSMD pads for BGA to improve solder-ball self-alignment. |
| | | Slightly extend pads for 0402 and smaller components to prevent tombstoning. |
| | | Avoid placing vias directly in chip-component pads (Via-in-Pad requires special processing). |
| | **Silkscreen and marking** | Keep silkscreen clear and off pads; provide clear reference designators and polarity markings. |
| | | Clearly label critical test points and connectors. |
| | **Panelization** | Use V-cut or mouse-bite tabs to ensure easy depaneling with smooth edges. |
| | | Add tooling rails and at least 3 global fiducials (Fiducial Mark). |
| | **Copper and routing** | Avoid connecting large copper pours directly to small pads; use thermal relief (Thermal Relief). |
| | | Avoid acute-angle routing to reduce EMI issues. |
| **DFT (Testability)** | **Test points** | Provide test points with diameter ≥0.8mm for critical nets to enable probe contact. |
| | | Keep spacing between test points ≥2.0mm to prevent probe shorts. |
| | | Avoid covering test points with solder mask or silkscreen. |
| | **Test strategy** | Implement JTAG/Boundary Scan chains to test high-density connectors and BGA. |
| | | Isolate different power nets to enable independent testing. |
| | | Reserve connectors or test points for programming/debug interfaces (e.g., JTAG, SWD). |
| **DFR (Reliability)** | **Thermal management** | Use thermal via arrays under high-power devices, connecting to inner GND or power planes. |
| | | Ensure adequate airflow space around heat-generating devices. |
| | | Avoid placing sensitive analog circuits near heat sources. |
| | **Component selection** | Apply derating to critical components (voltage, current, power, etc.). |
| | | Avoid components near end-of-life (EOL) or with single-source supply risk. |
| | **Mechanical stress** | Avoid placing fragile parts such as ceramic capacitors in high-stress PCB areas (mounting holes, near connectors, etc.). |
| | | Add additional reinforcement for connectors that will be frequently plugged/unplugged. |
| | **Protection design** | Consider conformal coating (Conformal Coating) for humid or dusty environments. |
| | | In coating areas, ensure test points and connectors are properly protected. |

## 8. HILPCB Collaboration Case: From 15% Voiding to Zero Field Failures

**Customer challenge:**
A leading medical imaging equipment manufacturer encountered intermittent crashes during a small-batch pilot build of the core processing board used in a portable ultrasound probe product. The board used two high-performance FPGAs in 0.4mm-pitch BGA packages. Preliminary analysis suggested a BGA soldering quality issue, but the existing assembler lacked effective inspection capability.

**HILPCB’s solution and collaboration workflow:**
1.  **Intake and analysis:** The customer sent design files and failed boards to HILPCB. Our engineers first performed a DFM/DFT review and found that some FPGA power-pin pads did not use thermal relief, and the center ground pad was oversized—both of which can cause uneven heating during soldering.
2.  **Deep inspection:** We inspected the failed boards using 3D AXI and strictly followed our `x ray inspection checklist`. We found an average voiding level of 15% on the FPGA center ground pad, and head-in-pillow defects on some joints. This severely impacted heat dissipation and high-speed signal grounding integrity, becoming the root cause of overheating-related crashes.
3.  **Collaborative optimization:** We provided a detailed X-ray analysis report and DFM optimization recommendations:
    *   Redesign the center ground pad into a “window” or “grid” pattern to increase outgassing paths.
    *   Optimize stencil apertures and adjust solder paste volume.
    *   Customize a staged reflow profile for the FPGA to ensure uniform heating of inner and outer joints.
4.  **Validation and mass production:** The customer adopted our recommendations and updated the design. In the next prototype round, X-ray verification showed BGA voiding consistently controlled below 5%, and head-in-pillow was fully eliminated. After rigorous functional and burn-in testing, the product performed stably. The project then transitioned to volume production at HILPCB, and to date there have been zero field failures caused by BGA soldering.

This case perfectly illustrates HILPCB’s value proposition: we are not just a manufacturer executing orders, but a partner that can deeply engage in customer designs and solve complex technical challenges using professional expertise and advanced tools.

**Are you also facing BGA soldering issues, high-density assembly challenges, or elusive quality problems?** Don’t let manufacturing become a bottleneck for product innovation.

**Upload your Gerber and BOM files now to receive a free professional DFM/DFT analysis report.** Let HILPCB’s expert team work with you to build excellent product quality from the source.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

In summary, this article explains the process capability indices, yield improvement, quality tools, test coverage, and traceability practices behind the `x ray inspection checklist`, and includes a DFM/DFT/DFR checklist to help establish a collaboration mechanism. The goal is to help teams systematically manage risks across design, materials, and testing. By executing according to the checklist and process window described here—and involving HILPCB’s DFM/DFA team early—you can accelerate prototype and mass-production delivery while maintaining quality and compliance.

> If you need manufacturing and assembly support, contact HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT guidance.
