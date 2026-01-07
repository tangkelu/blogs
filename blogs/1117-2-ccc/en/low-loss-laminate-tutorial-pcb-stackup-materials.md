---
title: "low loss laminate tutorial: Your first lesson in material parameters and stackup planning"
description: "A low loss laminate tutorial that explains key material parameters, stackup planning, impedance/thermal/cost trade-offs, and manufacturing considerations—with comparison tables and examples to help teams build a standard stackup library."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["low loss laminate tutorial", "hdI stackup tutorial", "hdmi pcb stackup guide", "surface finish comparison", "cti requirement explanation", "thermal reliability stackup"]
---
Hi, I’m an instructor from the HILPCB Stackup & Materials Academy. In day-to-day conversations with engineers, I see a common pain point: when you face a high-speed design, how do you choose the right low loss laminate from hundreds of PCB materials—and plan a stackup that hits performance targets while balancing cost and manufacturability?

Many teams either over-spec (using expensive Megtron 6 for 5Gbps) or under-spec (trying to push standard FR-4 to 28Gbps), and end up with Signal Integrity (SI) issues. This **low loss laminate tutorial** is the first lesson for you and your team: we’ll turn abstract parameters like Dk/Df, CTI, and fiber weave effect into actionable stackup-planning steps, backed by HILPCB production data, so you can make smarter trade-offs.

## 1. The starting point of stackup design: define inputs and expected outputs

A professional stackup is not guesswork—it’s a systematic process based on clear engineering requirements. Before you start, collect the following inputs:

*   **Signal requirements:**
    *   What is the highest data rate? (e.g., 5Gbps, 10Gbps, 28Gbps+)
    *   What impedance-control targets are required? (e.g., 50Ω single-ended, 90Ω/100Ω differential)
    *   What is the total insertion-loss budget (dB)?
*   **Power Integrity (PI) requirements:**
    *   How much current does the core device need? (drives copper thickness for power planes)
    *   What is the PDN target impedance? (affects power/ground coupling)
*   **Thermal requirements:**
    *   Power and location of major heat sources?
    *   Ambient temperature and cooling approach? This directly determines whether you need a **thermal reliability stackup**.
*   **Safety and reliability requirements:**
    *   Does the product need to meet specific standards? (e.g., UL, CE)
    *   **CTI requirement explanation**: Is there a specific Comparative Tracking Index requirement? For example, industrial or power products often require CTI ≥ 175V (PLC=2), or higher.
    *   Target lifetime and operating environment? (drives whether high Tg is needed)
*   **Mechanical and cost constraints:**
    *   Maximum PCB thickness limit?
    *   Target cost range?

**Your final output should be a professional stackup file containing:**

1.  Layer function definitions (signal, ground, power).
2.  Specific material part numbers per layer (Core & Prepreg).
3.  Dielectric thickness and copper thickness per layer (inner/outer).
4.  Overall finished thickness and tolerance.
5.  Impedance targets plus width/spacing recommendations per layer.
6.  Special process notes (backdrill, resin fill, etc.).

## 2. Material parameter cheat sheet: from FR-4 to low loss laminate

Picking the right material is half the job. To help you build a fast mental model, we summarized commonly used laminates from the HILPCB library by loss class. This is a simplified `dk df table`; real values vary with frequency and resin content.

<div class="div-type-1">
    <div class="div-type-1-title">PCB material performance comparison</div>
    <div class="div-type-1-content">
        <p>The table below covers key parameters from standard FR-4 to extremely low-loss materials to help you do a first-pass selection based on project needs (data rate, operating temperature, safety requirements).</p>
    </div>
</div>

| Material grade | Common HILPCB options | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Typical applications |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard FR-4** | S1141, KB-6160 | ~4.2 | ~0.020 | 140 | 315 | 175 | Low-frequency digital/analog, consumer electronics |
| **Mid Tg FR-4** | IT-158, S1155 | ~4.1 | ~0.018 | 150 | 330 | 175 | Multilayer boards, lead-free assembly |
| **High Tg FR-4** | IT-180A, S1000 | ~4.0 | ~0.015 | 180 | 345 | 175 | Servers, automotive, high-reliability |
| **Medium loss** | TU-768, S7439 | ~3.8 | ~0.009 | 190 | 360 | 175 | < 10Gbps high-speed, storage |
| **Low Loss (Low Loss)** | TU-872SLK, S1000-2M | ~3.6 | ~0.005 | 190 | 360 | 175 | 10-25Gbps, server backplanes, **hdmi pcb stackup guide** |
| **Very Low Loss (Very Low Loss)** | I-Speed, M4S | ~3.3 | ~0.003 | 200 | 380 | 175 | 25-56Gbps, RF communications, test equipment |
| **Ultra Low Loss (Ultra Low Loss)** | Megtron 6, Tachyon 100G | ~3.0 | ~0.002 | 210 | 400 | 175 | > 56Gbps, core networking, optical modules |
| **RF** | Rogers RO4350B | 3.48 | 0.0037 | 280 | 390 | 600 | RF/microwave circuits, antennas |

**Key parameter interpretations:**

*   **Dk (dielectric constant):** Lower Dk generally means faster propagation and makes it easier to use wider traces for the same impedance. Dk consistency matters more than the absolute value.
*   **Df (dissipation factor):** the key parameter. It directly determines attenuation. For >5Gbps signals, Df < 0.01 is a basic threshold.
*   **Tg (glass transition temperature):** the temperature where material transitions from rigid to rubbery. High Tg (≥170°C) means better heat resistance and dimensional stability—preferred for lead-free assembly and high-reliability products.
*   **Td (thermal decomposition temperature):** temperature at which the material loses 5% weight, reflecting long-term thermal reliability.
*   **CTI (Comparative Tracking Index):** resistance to surface tracking. Standard FR-4 is typically 175V (PLC=2); special applications may require 600V (PLC=0).

## 3. Core stackup patterns: 4/6/8/10-layer templates

Theory must meet practice. Below are several production-proven templates that are great starting points—you can fine-tune based on requirements.

| Layer count | Stackup (function) | Core | PP | Finished thickness (mm) | Typical use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4-layer** | SIG/GND/PWR/SIG | 1.0mm Core | 2x 1080 | 1.2 | IoT, MCU control, low-cost consumer |
| **6-layer** | SIG/GND/SIG/PWR/GND/SIG | 0.5mm Core | 3x 2116 | 1.6 | Embedded systems, DDR3/4 motherboards |
| **8-layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | 0.2mm Core | 4x 2116/1080 | 1.6 | PCIe, USB3.x, HDMI, HPC |
| **10-layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | 0.15mm Core | 5x 1080/106 | 1.6 | Server motherboards, complex **hdI stackup tutorial** cases, multi high-speed buses |

**Design notes:**

*   **4-layer:** lowest cost, but weaker EMI and SI—generally not suitable for high-speed.
*   **6-layer:** adds inner signal layers + solid reference planes; great cost/performance. Signal layers are shielded by ground planes, significantly improving EMI.
*   **8-layer:** adds two more reference planes and enables excellent Stripline structures—classic recommendation for **hdmi pcb stackup guide**. Supports multiple power-domain isolation and tight impedance control.
*   **10-layer and above:** for high-density, multi power-domain designs. More ground planes improve isolation and PI; for HDI, additional layers can accommodate more microvias.

## 4. Principles for coordinating signal/power/ground/copper thickness

The “soul” of a great stackup is how layers work together.

<div class="div-type-3">
    <div class="div-type-3-title">Golden rules for stackup planning</div>
    <ol>
        <li>
            <h6>Prioritize continuous reference planes</h6>
            <p>High-speed signal layers must be adjacent to a solid ground or power plane. Avoid routing across plane splits—this is a primary cause of crosstalk and EMI.</p>
        </li>
        <li>
            <h6>Route high-speed signals on inner layers</h6>
            <p>Inner-layer Stripline (GND-SIG-GND) generally provides better EMI shielding and more stable impedance than outer-layer Microstrip (SIG-GND).</p>
        </li>
        <li>
            <h6>Keep power and ground planes tightly coupled</h6>
            <p>Place primary power and ground planes adjacent to leverage plane capacitance, creating a low-impedance return path for high-frequency current and improving PI.</p>
        </li>
        <li>
            <h6>Trade-offs in copper thickness selection</h6>
            <p>Signal layers typically use 0.5oz (18μm) or 1oz (35μm) copper. 0.5oz supports finer line/space for high-density routing. High-current power planes may require 2oz (70μm) or thicker copper—often requiring a robust <strong>thermal reliability stackup</strong>.</p>
        </li>
        <li>
            <h6>Use symmetry to prevent warpage</h6>
            <p>Keep the stackup as symmetric as possible (materials, copper thickness, copper distribution). Asymmetry creates stress in lamination and reflow and increases warpage risk.</p>
        </li>
    </ol>
</div>

## 5. Hybrid lamination and special materials: when standard options are not enough

Sometimes one material system can’t satisfy everything—for example, when RF signals and digital control coexist. Then you should consider hybrid lamination.

| Option | Pros | Cons | HILPCB recommendation |
| :--- | :--- | :--- | :--- |
| **All Low Loss material** | Consistent performance, mature process | Higher cost | Best for communications/servers with aggressive SI requirements. |
| **Rogers + FR-4 hybrid** | RF performance + lower digital cost | Complex lamination, reliability risk, CTE mismatch | Ideal for antenna-integration designs. HILPCB has extensive hybrid experience and can optimize press cycles for reliability. |
| **MCPCB (metal core)** | Excellent heat dissipation | Typically limited to 1–2 layers; complex routing is difficult | High-power LED lighting, power modules, other thermal-critical applications. |
| **Rigid-Flex** | Enables 3D interconnect; high reliability | Complex design; very high cost | Wearables, aerospace, and products with special space/reliability constraints. |

## 6. Manufacturing impact: the “last mile” from drawing to physical PCB

A theoretically perfect stackup can still drive cost up or yield down if DFM is ignored.

<div class="div-type-6">
    <div class="div-type-6-title">HILPCB capability linked to stackup decisions</div>
    <div class="div-type-6-content">
        <ul>
            <li><strong>Resin Flow and Press Cycle:</strong> We tune lamination temperature/pressure profiles based on your chosen prepreg (PP). For example, high-resin 106 PP needs tight control to fill HDI laser microvias while avoiding excessive resin loss that destabilizes dielectric thickness.</li>
            <li><strong>Fiber Weave Effect:</strong> For 25Gbps+ signals, loose weave styles (e.g., 7628) can create local Dk non-uniformity and hurt impedance. HILPCB recommends and stocks Flat Glass low loss laminates to significantly improve signal quality.</li>
            <li><strong>Back-drilling:</strong> Via stubs are a high-speed “killer”. For >10Gbps signals, we provide precision depth-controlled backdrilling to remove unused stubs and reduce insertion loss by 1–2 dB.</li>
            <li><strong>Impedance coupons and TDR testing:</strong> Every production lot includes impedance coupons. HILPCB measures with TDR to ensure final impedance stays within your tolerance window (+/- 10% or tighter).</li>
            <li><strong>Surface finish comparison:</strong> Surface finish affects high-speed behavior too. ENIG is flat and suitable for high frequency, but has “black pad” risk and higher cost. OSP is low cost but has limited shelf-life for solderability. We will recommend the best [internal link: PCB surface finish] option based on application and cost targets.</li>
        </ul>
    </div>
</div>

## 7. How does HILPCB help you with stackup design?

After this **low loss laminate tutorial**, stackup planning may still feel challenging. That’s exactly why the HILPCB Stackup & Materials Academy exists. We’re not just a manufacturer—we’re your engineering partner.

We offer a **“Stackup quick claim”** service to free you from tedious material selection and stackup calculations.

<div class="cta-container">
    <div class="cta-text">
        <h5>Not sure how to start? Let HILPCB engineers customize your stackup</h5>
        <p>Share your design requirements (data rate, layer count, impedance, etc.). Our senior engineers will deliver a DFM-validated, inventory-optimized professional stackup proposal within 24 hours—plus a detailed impedance-calculation report. Completely free.</p>
    </div>
    Submit your stackup request now
</div>

**Why choose HILPCB?**

*   **200+ in-stock materials:** from standard FR-4 to Rogers and Megtron, avoiding delays caused by MOQ and multi-week lead times for special materials.
*   **Experienced engineering team:** thousands of high-speed, high-frequency, high-density projects—fast risk identification and cost/performance optimization.
*   **Advanced impedance test lab:** we don’t just promise impedance; we verify it with strict TDR testing so every board meets your spec.

### Summary

Great stackup design is a balance among performance, cost, and manufacturability. Start with clear inputs, use the parameter table for first-pass selection, reuse proven patterns, and keep close communication with your PCB manufacturer (like HILPCB). Bringing manufacturing constraints forward helps your team build a standardized, reliable stackup library and accelerate product development.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

In summary, this low loss laminate tutorial explains material parameters, stackup planning, impedance/thermal/cost trade-offs, and manufacturing considerations—with comparison tables and examples—to help teams build a standard stackup library and manage risk across design, materials, and test. By following the checklists and process windows described here—and involving HILPCB’s DFM/DFA team early—you can accelerate prototype and volume delivery while maintaining quality and compliance.

> For fabrication and assembly support, contact HILPCB via [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT suggestions.
