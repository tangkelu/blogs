---
title: "HDI stackup tutorial: Your first lesson in understanding material parameters and stackup design"
description: "Centered on HDI stackup tutorial, this guide explains material parameters, stackup planning, impedance/thermal/cost trade-offs, and manufacturing considerations, with reference tables and case studies to help teams establish standard stackup libraries."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["HDI stackup tutorial", "HDMI PCB stackup guide", "thermal reliability stackup"]
---

Hello, I'm an instructor at HILPCB's Stackup and Materials Academy. In my daily work, I've found that many engineers feel confused when faced with cold parameters like Dk/Df, CTI, and Tg, uncertain how to transform them into a reliable, mass-producible PCB stackup. A poor stackup design can cause signal integrity issues at best, or trigger reliability disasters in mass production at worst.

Today, this **HDI stackup tutorial** will serve as your first lesson, taking you from zero to systematically building stackup design thinking. We'll transform abstract material science into concrete engineering decisions, enabling you not only to design stackups that meet performance requirements but also to foresee and avoid manufacturing pitfalls. Whether you're designing a high-speed `HDMI PCB stackup guide` or tackling a project with extreme `thermal reliability stackup` demands, the knowledge here will be your solid foundation.

## The Starting Point of Stackup Design: Clarifying Your "Constraints"

Before opening an EDA tool to draw the first trace, professional stackup design begins with comprehensive analysis of project requirements. It's like an architect understanding a building's purpose, budget, and geological conditions before designing blueprints. The input conditions for stackup design mainly include:

* **Signal Integrity (SI) Requirements:**
  * **Maximum data rate**: What's the highest signal rate in your design? Is it PCIe 3.0 at 10Gbps or SerDes at 28Gbps? Data rate determines your tolerance for material loss (Df).
  * **Impedance control**: Which impedances need control? 50Ω single-ended or 90/100Ω differential? Precise impedance is the prerequisite for stable high-speed signal transmission.
* **Power Integrity (PI) Requirements:**
  * **Core current**: How large is the instantaneous current of core devices like CPUs and FPGAs? This determines power plane copper thickness and layout, and whether low-inductance paths are needed.
  * **Plane capacitance**: Do you need to utilize adjacent power/ground planes to build plane capacitance for high-frequency decoupling?
* **Thermal Management and Reliability Requirements:**
  * **Power dissipation and environment**: What's the total board power dissipation, location of critical heat-generating devices, and the final product's operating temperature? This directly relates to material selection for glass transition temperature (Tg) and thermal decomposition temperature (Td).
  * **Safety standards**: Does the product have high-voltage sections? Are there explicit CTI (comparative tracking index) requirements (e.g., >400V)? This is critical in industrial and power supply products.
* **Cost and Supply Chain:**
  * **Target cost**: What's the budget per board? This directly determines whether you optimize within standard FR-4 ranges or can consider high-performance materials like Rogers.
  * **Production volume and lead time**: Estimated annual production and delivery schedule determine whether your chosen materials are readily available and if minimum order quantities (MOQ) are problematic.

These input conditions ultimately output a clear, PCB-factory-ready stackup structure diagram containing each layer's type, material, thickness, copper weight, impedance requirements, and all other critical information.

## Reading the "Material Language": Key Parameter Quick Reference

Selecting appropriate materials is the core of stackup design. Facing hundreds of board material models, we must learn to grasp key parameters. The following table summarizes core specifications of representative materials in HILPCB's material library.

<div class="div-style-1">
    <h4>Material Parameter Trade-offs: There's no perfect material, only suitable choices</h4>
    <p>In material selection, performance and cost are always contradictory. For example, pursuing extremely low Df (dielectric loss) typically means higher material costs. Similarly, high-Tg materials offer better thermal stability but have stricter processing windows (Press Cycle). An engineer's value lies in finding the optimal balance among these parameters based on project requirements. For a cost-sensitive consumer electronics product, S1141 or IT-180A may suffice; for a core board in a telecom base station, you may need S1000-2M or even higher-grade materials.</p>
</div>

| Material Model | Supplier | Category | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Core Applications |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S1141** | Shengyi | Standard FR-4 | 4.2 | 0.020 | 140 | 315 | >175 | Consumer electronics, low-frequency control boards |
| **IT-180A** | ITEQ | High-Tg FR-4 | 3.9 | 0.012 | 175 | 345 | >400 | Servers, industrial control, automotive |
| **S1000-2M** | Shengyi | Mid-Loss | 3.6 | 0.009 | 190 | 360 | >400 | High-speed computing, data centers |
| **EM-827** | EMC | Low-Loss | 3.4 | 0.006 | 200 | 370 | >600 | 25Gbps+ SerDes, network equipment |
| **RO4350B** | Rogers | RF/Microwave | 3.48 | 0.0037 | 280 | 390 | >400 | RF modules, antennas, 5G |

**Parameter Interpretation:**
* **Dk (Dielectric Constant)**: Affects signal propagation speed and impedance. Lower and more stable Dk is beneficial for high-speed signals. A Dk change from 3.66 to 3.2 can impact 100Ω differential impedance line width by over 10%.
* **Df (Dielectric Loss Tangent)**: The degree to which signal energy converts to heat in the dielectric. For long-distance, high-frequency signals, low Df is critical.
* **Tg (Glass Transition Temperature)**: The temperature at which material transitions from rigid glass state to flexible rubber state. High Tg (typically >170°C) means better high-temperature dimensional stability and reliability, especially after multiple reflow cycles.
* **Td (Thermal Decomposition Temperature)**: The temperature at which material decomposes due to high heat, causing 5% weight loss. Td is a key metric for assessing long-term heat resistance.
* **CTI (Comparative Tracking Index)**: The material's surface resistance to leakage current along the surface. High CTI (e.g., 600V) is essential for high-voltage and safety-critical applications.

## From 4 Layers to 10+ Layers: Classic Stackup Structure Paradigms

Having mastered materials, let's see how to "build" them. Stackup structure design isn't arbitrary combination but follows fundamental principles of electromagnetic compatibility (EMC) and signal integrity.

<div class="div-style-3">
    <h4>Three-Step Stackup Planning Method</h4>
    <ol>
        <li><strong>Determine layer count and function</strong>: Based on routing density, power distribution needs, and cost budget, initially determine total layer count. Assign initial function (signal, ground, power) to each layer.</li>
        <li><strong>Build reference planes</strong>: Prioritize placing complete, continuous GND planes. They serve as return paths for high-speed signals and natural shielding layers. Place critical signal layers adjacent to GND planes.</li>
        <li><strong>Optimize and symmetrize</strong>: Adjust dielectric thickness and copper weight to meet impedance requirements. Keep stackup structure symmetric top-to-bottom to prevent warping from uneven thermal stress during production.</li>
    </ol>
</div>

Below are several classic stackup paradigms and their application scenarios, which are also common templates HILPCB engineers use when providing [stackup solutions](/services/pcb-stack-up-design/) to customers.

| Layer Count | Classic Structure (Top to Bottom) | Typical Applications | Advantages | Disadvantages |
| :--- | :--- | :--- | :--- | :--- |
| **4-layer** | SIG/GND/PWR/SIG | IoT modules, simple controllers | Extremely low cost, simple structure | Poor EMC performance, unstable impedance control |
| **6-layer** | SIG/GND/SIG/SIG/PWR/SIG | Consumer electronics, industrial motherboards | Introduces complete ground plane, improved EMC | Poor reference planes for internal signal layers |
| **6-layer (Recommended)** | SIG/GND/PWR/GND/SIG/SIG | HDMI/USB3.0 applications | Excellent EMC and SI performance, moderate cost | Sacrifices one routing layer |
| **8-layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | Servers, high-performance computing | Multiple shielding layers, precise impedance control, suitable for high-speed differential pairs | Higher cost, slightly longer manufacturing cycle |
| **10-layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | Core network equipment, complex FPGA boards | Excellent power/ground isolation, ample routing space | High cost, high precision requirements |

## Layer Harmony: "Symphony" of Signals, Power, Ground, and Copper Weight

An excellent stackup has internal elements coordinated like a symphony—harmonious and orderly.

### Signal Layers: Microstrip vs. Stripline
* **Microstrip**: Traces on outer layers with air on one side and dielectric/reference plane on the other. Advantages: simple processing, easy debugging. Disadvantages: susceptible to external interference, strong radiation.
* **Stripline**: Traces buried between two reference planes in inner layers. Advantages: excellent EMC performance, stable impedance. Disadvantages: slightly lower routing density, difficult to modify.
* **HILPCB Recommendation**: For critical signals exceeding 5Gbps, prioritize stripline structure and ensure complete reference plane integrity.

### Reference Planes: GND's "Dominant Position"
Solid, continuous GND planes are the foundation of high-speed design. They provide the shortest return path for signals, effectively suppressing crosstalk and radiation. Avoid splitting ground planes under high-speed signal paths. If splitting is necessary, use bypass capacitors to ensure continuous return paths.

### Copper Weight: 1 oz vs. 2 oz Trade-off
Copper weight selection directly impacts current-carrying capacity and impedance line width.
* **Current-carrying capacity**: 2 oz (70µm) copper carries approximately 1.5-1.8 times the current of 1 oz (35µm) copper. For high-current power layers, thick copper is necessary.
* **Impedance impact**: With the same dielectric thickness and impedance target, thick copper requires wider line width. For example, achieving 50Ω impedance on 4mil core material, 1 oz copper may need 7.2mil line width while 2 oz copper needs 9.5mil, consuming valuable routing space.
* **Manufacturing considerations**: Thick copper etching is more difficult, affecting yield for fine traces. When designing [high-density interconnect (HDI) boards](/technology/what-is-hdi-pcb/), inner layers typically use 0.5 oz or 1 oz copper.

## Beyond FR-4: Applications of Hybrid Stackups, Metal-Core, and Flexible Materials

When standard FR-4 cannot meet extreme performance requirements, we need to introduce special materials and processes.

### Hybrid Stackup
Hybrid stackup means using two or more different material types in a single PCB, common in RF designs. For example, using Rogers RO4350B for the RF section while using cost-effective IT-180A for the digital control section.

| Hybrid Solution | Advantages | Challenges and Considerations |
| :--- | :--- | :--- |
| **Rogers + FR-4** | Achieves high performance in critical areas, overall cost manageable | CTE (thermal expansion coefficient) mismatch may cause delamination or reliability issues; complex Press Cycle parameters require experienced manufacturers. |
| **High-speed material + Standard material** | Meets low-loss requirements for high-speed channels, reduces total cost | Resin flow differences between materials may affect dielectric thickness uniformity. |

HILPCB has extensive hybrid stackup production experience, capable of ensuring hybrid board reliability through precise lamination curve control and material characteristic analysis.

### Metal-Core PCB (MCPCB) and Flexible Boards
* **MCPCB**: Typically uses aluminum or copper base, with superior thermal dissipation as core advantage. This is critical for high-power LEDs, power modules, and other applications requiring high `thermal reliability stackup`.
* **Flexible/Rigid-flex boards**: Enable connections in 3D space and dynamic bending. Stackup design is more complex, requiring consideration of stress in flex regions, adhesive selection, and coverlay thickness.

## From Design to Mass Production: Manufacturing Process Impact Cannot Be Ignored

Your stackup design drawing is only a "theoretical model"; the final physical product is profoundly affected by manufacturing processes.

<div class="div-style-6">
    <h4>HILPCB's Process Control Capability</h4>
    <p>At HILPCB, we don't just receive your design files. Our CAM engineers, based on our extensive material database and mature lamination models, perform manufacturing feasibility analysis on your stackup. Through simulating resin flow and thickness changes during lamination, we can predict and compensate in advance, ensuring final product impedance accuracy within ±5%, far exceeding industry standard ±10%.</p>
</div>

* **Resin Flow**: During lamination, resin in prepreg (PP) melts under heat and fills voids in copper foil patterns. This flow causes final dielectric thickness to be less than original PP thickness. Experienced manufacturers compensate precisely based on copper coverage.
* **Press Cycle**: Different materials require different lamination temperature, pressure, and time curves. For example, standard-Tg materials typically laminate at ~185°C, while high-Tg materials require over 200°C. Improper lamination causes delamination, warping, and other issues.
* **Warpage**: Asymmetric stackup structure and uneven copper foil distribution are main warping causes. Design should maintain stackup symmetry and add grid copper in large non-routed areas.
* **Back-drilling**: For signals above 10Gbps, unused via portions (stubs) resonate like antennas, severely degrading signal quality. Back-drilling precisely removes these excess stubs, a key technology for ensuring high-speed signal integrity.
* **Impedance Coupon**: Test coupons on the same production panel as the main board, used to measure actual produced trace impedance via time-domain reflectometry (TDR). Every impedance board from HILPCB includes detailed coupon test reports.

## HILPCB Stackup and Materials Academy: Your Engineering Partner

The ultimate purpose of theoretical learning is solving practical problems. HILPCB is not just your PCB manufacturer but your technical partner. We understand stackup design's importance and complexity, so we offer a series of services to simplify this process:

* **200+ Material Library**: We stock over 200 materials from global leading suppliers, from standard FR-4 to high-speed, RF, metal-core, and other specialty materials, all with detailed performance characterization data, providing the broadest selection.
* **Impedance Testing Laboratory**: Our in-house testing lab equipped with advanced TDR equipment ensures every impedance batch undergoes rigorous verification, providing reliable data support.

## Get Your Custom Stackup Solution Now

Rather than struggling through mountains of material datasheets, let professional engineers guide you. HILPCB's "Quick Stackup Claim" service aims to help you obtain a verified, mass-producible stackup solution early in your project.

<div class="cta-box">
    <h3>Struggling with stackup design?</h3>
    <p>Upload your project requirements (such as layer count, data rate, impedance requirements, special materials, etc.), and HILPCB's senior stackup engineers will provide you with a detailed, professional stackup recommendation within 24 hours, including material selection, thickness calculations, and impedance simulation results. Build your design on a solid foundation from the start!</p>
    Get Your Free Stackup Solution Now
</div>

## Conclusion: Successful Stackup is Consensus Between Design and Manufacturing

I hope this **HDI stackup tutorial** opens a new door for you. Remember, successful stackup design is never one-sided "closed-door engineering" by engineers alone, but deep integration of design intent and manufacturing capability. It begins with clear requirement definition, runs through deep understanding of material parameters, and ultimately rests on full respect for manufacturing processes.

When you start your next project, I hope you'll move beyond simple layer stacking and think from multiple dimensions—SI, PI, thermal reliability, and cost—while actively communicating with experienced manufacturers like HILPCB. Because an excellent stackup is the starting point of your excellent product.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Summary

In summary, this article, centered on **HDI stackup tutorial**, explains material parameters, stackup planning, impedance/thermal/cost trade-offs, and manufacturing considerations, with reference tables and case studies to help teams establish standard stackup libraries. The goal is to help teams systematically control risks in design, material, and testing phases. By following the checklists and process windows in this article and involving HILPCB's DFM/DFA teams early, you can accelerate prototype and mass production delivery while ensuring quality and compliance.

> For manufacturing and assembly support, contact HILPCB's [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT recommendations.
