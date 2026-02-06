---
title: "CTI requirement explanation: Materials and stackup strategy whitepaper"
description: "Providing a comprehensive material selection decision tree, stackup templates, impedance/thermal modeling methods and manufacturing verification processes, with DFM/DFT/DFR checklists to help engineering teams standardize stackup design."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 9
tags: ["cti requirement explanation", "thermal reliability stackup", "hdi stackup tutorial", "surface finish comparison", "hdmi pcb stackup guide"]
---

## 1. Executive Summary: Scenarios, Challenges, and Benefits

**Scenario:** In modern electronic product design, from high-speed data centers to power management units in new energy vehicles, PCBs are no longer just carriers for components but rather the foundation of system performance and safety reliability. Hardware and systems engineers must face a complex multi-variable problem early in projects: how to ensure electrical safety throughout the product lifecycle while meeting signal integrity, thermal management, and mechanical strength requirements?

**Challenge:** The core of this challenge lies in material and stackup strategy selection. Incorrect materials can lead to signal attenuation, impedance mismatches, and even catastrophic electrical breakdown under harsh conditions (such as high voltage, high humidity). Among these, **CTI (Comparative Tracking Index)** as a critical electrical safety indicator is becoming increasingly important but is often overlooked in early design stages. A comprehensive `cti requirement explanation` is not only about compliance but directly impacts product long-term reliability.

**Benefits:** This whitepaper aims to provide a systematic solution. As the official guide from HILPCB's materials laboratory, we will deliver a complete strategy from material selection to manufacturing verification. Through standardized decision trees, stackup template libraries, modeling methods, and DFM/DFR checklists, this whitepaper will help your team:
- **Reduce design risk:** Make data-driven material decisions based on clear CTI requirements and performance metrics.
- **Accelerate development cycles:** Leverage pre-validated stackup templates to quickly launch new projects.
- **Improve product reliability:** Ensure `thermal reliability stackup` and electrical safety through scientific modeling and verification processes.
- **Optimize manufacturing costs:** Balance performance and cost, avoiding over-design or costly rework due to improper materials.

---

## 2. Material Decision Tree: Systematic Path from Specifications to Selection

Selecting the correct PCB material is the first and most critical step in stackup design. CTI is the starting point for safety considerations, but must be coordinated with other performance indicators (such as Dk, Tg, CTE). The table below provides a simplified decision framework.

<div class="div-type-1">

### CTI Requirement Explanation: Core Safety Indicator

CTI measures an insulating material's ability to resist leakage tracking formation on its surface under electric field and electrolytic contamination. Its grade is defined by PLC (Performance Level Category), with higher values indicating stronger anti-tracking ability.
- **PLC 0:** CTI ≥ 600V (highest grade, suitable for industrial, power, automotive high-voltage systems)
- **PLC 1:** 400V ≤ CTI < 600V
- **PLC 2:** 250V ≤ CTI < 400V
- **PLC 3:** 175V ≤ CTI < 250V (standard FR-4 materials typically fall in this range)

When designing high-voltage or safety-critical products, you must clearly specify the required CTI grade and select corresponding materials.

</div>

### Material Selection Decision Tree

| Key Metric | Recommended Material/Grade | Typical Application Scenarios | Design Constraints/Considerations |
| :--- | :--- | :--- | :--- |
| **CTI ≥ 600V (PLC 0)** | High CTI FR-4 (e.g., S1170G), phenolic resin, some polyimide (PI) | Industrial power supplies, inverters, EV BMS/OBC, medical devices | Relatively high cost; limited material options, advance confirmation with HILPCB required. |
| **Low Dk/Df** | Rogers (RO4350B, Dk≈3.48), Megtron 6 (Dk≈3.6), Isola FR408HR | 5G/6G RF, high-speed servers (≥25Gbps), `hdmi pcb stackup guide` | High processing requirements (e.g., plasma desmear); significantly higher cost than standard FR-4. |
| **High Tg > 170°C** | S1000-2M, IT-180A, TU-768 | Automotive electronics, high-power density modules, multi-layer thick copper boards | More brittle material, drilling parameters need optimization; higher lamination temperature (≈190-210°C). |
| **Low Z-axis CTE** | Low CTE FR-4, polyimide (Polyimide) | HDI boards, BGA/LGA dense packaging, thick boards (>3.0mm) | Significantly improves PTH reliability, preventing via cracks under thermal cycling. |
| **High Thermal Conductivity** | Aluminum-based boards (MCPCB, 1-3 W/m·K), ceramic-based boards (AlN, >150 W/m·K) | LED lighting, power MOSFET modules, IGBT drivers | Usually single or dual-layer structures, limited routing; requires specialized `thermal reliability stackup` design. |
| **Flexibility/Bending Requirements** | Polyimide (Polyimide, PI) | Wearable devices, rigid-flex boards, dynamic bending applications | More complex impedance control, requires stiffener design consideration. |

---

## 3. Stackup Template Library: Starting Point for Standardized Design

HILPCB's laboratory has summarized the following standard stackup templates based on experience from thousands of production projects. These templates have been verified through simulation and measurement and can serve as reliable starting points for new designs.

### Standard Multi-layer Board Stackup Templates

| Layers | Structure (Example) | Description | Key Applications |
| :--- | :--- | :--- | :--- |
| **4 Layer** | SIG/GND/PWR/SIG | `Core(0.76mm) + PP + Core(0.76mm)` | Consumer electronics, IoT modules. High cost-effectiveness, but EMI control requires care. |
| **6 Layer** | SIG/GND/SIG/SIG/PWR/SIG | `Core + PP + Core + PP + Core` | Balance point between performance and cost. Provides good signal/power isolation. |
| **8 Layer** | SIG/GND/SIG/PWR/GND/SIG/PWR/SIG | `Core + PP + PP + Core + PP + PP + Core` | High-speed design (PCIe, USB 3.0). Multiple reference planes, easy to achieve 50Ω/100Ω impedance control. |
| **10 Layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | `Core + PP...` | Complex systems, server motherboards. Provides ultimate EMI shielding and power integrity. |

### Special Structure Stackup Templates

<div class="div-type-3">

#### HDI (High-Density Interconnect) Stackup Tutorial

Using a typical **1+N+1 (N=6) HDI** stackup as an example, this is a classic `hdi stackup tutorial` structure:
- **L1 (SIG):** Microvia (L1-L2)
- **L2 (GND):**
- **L3 (SIG):** Buried Via (L3-L6)
- **L4 (PWR):**
- **L5 (GND):**
- **L6 (SIG):**
- **L7 (GND):**
- **L8 (SIG):** Microvia (L8-L7)

**Core Process:** Using "sequential lamination," first fabricate the inner core board L2-L7, complete buried via drilling and plating, then laminate L1 and L8 dielectric and copper foil on both sides, finally perform laser drilling for microvias. This structure greatly improves routing density.

</div>

#### Rigid-Flex and MCPCB

- **Rigid-Flex Board:** Structure is `rigid area (FR-4) - flexible area (PI) - rigid area (FR-4)`. Key is transition area design, ensuring smooth stress transition and preventing copper foil fracture during bending.
- **MCPCB (Aluminum-based board):** Structure is `circuit layer (copper foil) - insulating layer (high thermal conductivity dielectric) - metal base layer (aluminum)`. Core is insulating layer thermal conductivity and voltage resistance, critical for `thermal reliability stackup`.

---

## 4. Impedance/Thermal/Mechanical Modeling Methods

Precise modeling ensures design intent realization. HILPCB's simulation team uses the following first-principles models for pre-analysis.

### Impedance Modeling

For high-speed signals like HDMI or DDR, impedance control is critical, with tolerances typically required within **±10%** or even **±5%**.
- **Microstrip - surface layer:**
  $$ Z_0 \approx \frac{87}{\sqrt{\epsilon_r + 1.41}} \ln\left(\frac{5.98H}{0.8W + T}\right) $$
- **Stripline - inner layer:**
  $$ Z_0 \approx \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{4B}{0.67\pi(0.8W + T)}\right) $$
  *Where:*
  - $Z_0$: Characteristic impedance (Ω)
  - $\epsilon_r$: Dielectric constant (Dk)
  - $H$: Dielectric layer thickness
  - $W$: Trace width
  - $T$: Copper thickness
  - $B$: Distance between two reference planes

**Example:** In a `hdmi pcb stackup guide`, to achieve 100Ω differential impedance using FR-4 material with Dk of 4.2, dielectric thickness of 0.1mm, copper thickness of 1oz (0.035mm), simulation calculates required line width of approximately 0.12mm.

### Thermal Modeling

Core of thermal reliability analysis is calculating thermal resistance paths.
- **One-dimensional steady-state thermal resistance (Rth):**
  $$ R_{th} = \frac{L}{k \cdot A} $$
  *Where:*
  - $R_{th}$: Thermal resistance (°C/W)
  - $L$: Thermal conduction path length (m)
  - $k$: Material thermal conductivity (W/m·K)
  - $A$: Thermal conduction cross-sectional area (m²)

By stacking calculations from chip junction to PCB surface to heatsink, you can predict chip operating temperature, foundation of `thermal reliability stackup` design.

### Mechanical Modeling

Primarily focuses on stress from Z-axis CTE mismatch. During temperature cycling from -40°C to 125°C, if material Z-CTE is too high (> 50 ppm/°C), PTH copper experiences enormous tensile stress, potentially causing microcracks or fractures. Selecting materials with Z-CTE < 50 ppm/°C is critical for high-reliability design.

---

## 5. Hybrid Lamination/Back-drilling/Special Structures

To achieve optimal balance between cost and performance, HILPCB supports multiple advanced manufacturing processes.

<div class="div-type-6">

### Hybrid Stackup

**Rogers + FR-4 Hybrid Lamination:** This is the most common `hybrid stack` approach.
- **Structure:** Use expensive Rogers material (e.g., RO4350B) only for RF signal layers, while internal digital and power layers use lower-cost high-Tg FR-4.
- **Challenge:** Different CTE and lamination parameters (temperature, pressure) between materials require specialized lamination programs. FR-4 and Rogers material bonding is weaker, requiring plasma treatment after drilling to enhance hole wall bonding.
- **Benefit:** While ensuring RF performance, can save 30-50% in material costs.

</div>

### Back-drilling

- **Purpose:** Remove excess via stubs in high-speed signal paths, reducing signal reflection and attenuation, especially effective when rates exceed 10 Gbps.
- **Process:** After PCB lamination and via plating completion, use a larger diameter drill bit from the other side to remove excess via portions, with extremely high depth control precision.
- **Application:** Server backplanes, high-speed switches, optical modules.

### Surface Finish Comparison

Surface finish directly impacts soldering reliability and signal integrity.

| Surface Finish | Advantages | Disadvantages | Recommended Applications |
| :--- | :--- | :--- | :--- |
| **HASL (Hot Air Solder Leveling)** | Low cost, good solderability | Poor surface flatness, unsuitable for fine-pitch components | General consumer products without strict flatness requirements |
| **ENIG (Electroless Nickel Immersion Gold)** | Flat surface, corrosion resistant, suitable for BGA | Higher cost, potential "black pad" risk | High-speed boards, BGA/CSP packaging, key areas |
| **OSP (Organic Solderability Preservative)** | Low cost, extremely flat surface, environmentally friendly | Poor storage tolerance, performance degradation after multiple reflows | Consumer electronics requiring fast turnaround and low cost |
| **Immersion Silver** | Good flatness, excellent electrical performance | Prone to oxidation, high storage and handling environment requirements | High-frequency signals, communications equipment |

---

## 6. Verification Process: From Material Incoming to Final Reliability

A robust `stackup strategy` must have a closed-loop verification process for assurance.

1.  **Material Incoming Inspection (IQC):** Verify supplier-provided CTI, Dk, Tg specifications and test reports. Sample test critical materials.
2.  **Lamination Process Monitoring:** Real-time monitor lamination machine temperature and pressure curves, ensuring consistency with material specifications. Standard FR-4 lamination temperature approximately **180°C**.
3.  **Characteristic Impedance Coupon Testing:** Every batch of produced PCBs includes specialized coupon strips. Use TDR (time-domain reflectometry) to precisely measure 50Ω/100Ω characteristic impedance, ensuring fluctuation within **±10%** design tolerance. This is the core of `coupon test`.
4.  **Warpage (Warpage) Analysis:** Use optical methods (e.g., Shadow Moiré) to measure PCB warpage before and after reflow soldering, ensuring less than 0.75%.
5.  **Reliability Testing:**
    - **Thermal Shock Testing:** For example, 1000 cycles between -40°C and 125°C, then cross-section inspection of PTH and microvias for integrity.
    - **Interconnect Stress Testing (IST):** Accelerated simulation of thermal-mechanical stress through rapid heating and current loading on coupons, evaluating via reliability.

---

## 7. DFM/DFR/DFT Checklist

This checklist (≥35 items) helps engineers avoid common manufacturing, reliability, and testing issues during design phase.

| Category | Rule/Check Item | Recommended Parameters/Description | Verification Method |
| :--- | :--- | :--- | :--- |
| **Materials & Stackup** | Does CTI grade meet safety requirements? | Select PLC 0-3 based on application voltage | Design review |
| | Are Dk/Df/Tg/CTE clearly marked? | Annotate material model in stackup diagram | Design review |
| | Is stackup structure symmetric? | Maintain copper foil and dielectric layer symmetry to prevent warping | CAM software analysis |
| | Is Core/PP combination reasonable? | Avoid using single thick PP | CAM software analysis |
| **Drilling** | Minimum mechanical drill size | ≥ 0.20mm | DFM check |
| | Minimum laser drill size (HDI) | ≥ 0.10mm | DFM check |
| | Drill aspect ratio | < 10:1 (recommended), < 12:1 (limit) | DFM check |
| | Hole to copper distance | ≥ 0.20mm | DRC check |
| | NPTH to copper distance | ≥ 0.25mm | DRC check |
| **Routing** | Minimum line width/spacing | 3.5/3.5mil (inner), 4/4mil (outer) | DFM check |
| | Avoid sharp/right-angle traces | Use 45° or arc traces | DRC check |
| | BGA fanout | Prioritize Dog-bone or Via-in-Pad | Layout review |
| | Differential pair length matching | Length error < 5mil (adjust per speed) | Layout software |
| **Copper** | Via under BGA/QFN pads? | Recommend Via-in-Pad (requires resin plugging) | DFM check |
| | Thermal relief design | Connection width not less than 50% of pad width | DFM check |
| | Large copper to pad distance | ≥ 0.25mm | DRC check |
| | Remove copper islands? | Remove unconnected small copper pieces | CAM software analysis |
| | Stitching via density | Along board edge and near high-speed lines, spacing < λ/20 | Layout review |
| **Solder Mask** | Solder mask dam width | ≥ 0.10mm (4mil) | DFM check |
| | Solder mask opening size | Single side larger than pad by 0.05mm (2mil) | DFM check |
| | Via tenting/plugging | Decide per test requirements, default cover | Design specification |
| **Silkscreen** | Silkscreen line width | ≥ 0.15mm (6mil) | DFM check |
| | Silkscreen to pad spacing | ≥ 0.15mm (6mil) | DFM check |
| | Component designators and polarity clear? | Ensure readability | Layout review |
| **Reliability (DFR)** | Creepage/clearance in high-voltage areas | Follow IEC-62368-1 standards | Design review |
| | Board edge metal exposure | Distance from board edge ≥ 0.4mm | DFM check |
| | Gold finger chamfering | 30° or 45° chamfer | Design specification |
| | Stamp hole/V-Cut design | Ensure easy separation without component damage | DFM check |
| **Testability (DFT)** | Test point size/spacing | Diameter ≥ 0.8mm, spacing ≥ 1.27mm | DFM check |
| | Fiducial marks | At least 3 per board, diagonal distribution | DFM check |
| | ICT test points under components? | Avoid | Layout review |
| | JTAG/SWD interface exposed? | Facilitate debugging | Design review |
| **Other** | Board thickness tolerance | ±10% | Design specification |
| | Impedance tolerance | ±10% (standard), ±5% (strict) | Design specification |
| | Final copper thickness | Meet current carrying requirements | Current density simulation |

---

## 8. HILPCB Service Closed Loop: From Theory to Mass Production Partner

What this whitepaper presents is not just theoretical knowledge but practical experience accumulated by HILPCB across countless projects. We understand that every successful product stems from a solid physical foundation.

HILPCB's service forms a complete closed loop:
- **Material inventory and laboratory support:** We maintain rich inventory covering standard FR-4 to Rogers, Megtron and other premium materials, with internal laboratory capability to quickly verify CTI, Dk and other critical parameters.
- **Stackup simulation and design services:** Our engineering team uses industry-leading tools for impedance, thermal and signal integrity simulation, helping optimize stackup early in design.
- **Advanced process capability:** Whether complex `hybrid stack`, high-precision back-drilling, HDI or rigid-flex boards, we have mature mass production experience.
- **Mass production data feedback:** We continuously collect production line and `coupon test` data, continuously optimizing our DFM rule library and stackup templates, ensuring design recommendations always based on latest manufacturing capability.

<div class="div-type-1">

**Call to Action (CTA)**

Your next project deserves a more reliable, more optimized foundation. Contact HILPCB's materials laboratory now to **get a free stackup design review**. Our experts will provide customized material and stackup recommendations based on your project's specific `cti requirement explanation` and performance goals, helping you build core competitiveness from the source.

**[Contact our technical experts now to start your project optimization journey](#contact)**

</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

In summary, this article provides material selection decision trees, stackup templates, impedance/thermal modeling methods and manufacturing verification processes with DFM/DFT/DFR checklists around `cti requirement explanation`, helping engineering teams standardize stackup design and systematically control design, materials and testing phase risks. By following the checklists and process windows in this article and involving HILPCB's DFM/DFA teams early, you can accelerate prototype and mass production delivery while ensuring quality and compliance.

> For manufacturing and assembly support, contact HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT recommendations.

