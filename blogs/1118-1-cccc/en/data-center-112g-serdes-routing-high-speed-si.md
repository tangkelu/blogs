---
title: "data-center 112G SerDes routing: Ultra-high-speed channel design and low-loss SI constraints"
description: "A deep dive into data-center 112G SerDes routing: channel budget, materials, stack-up, impedance control, via/connector transitions, DFM, and compliance validation for high-performance high-speed SI PCBs."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---
With the explosive growth of AI, ML, and cloud computing, intra–data-center traffic is rising at unprecedented speed. To keep up, the industry is rapidly migrating from 56G NRZ/PAM4 to 112G PAM4 SerDes. This jump not only doubles per-lane rate, it also pushes PCB SI into a new regime. Successful **data-center 112G SerDes routing** is no longer “just connect it”—it’s system engineering across materials, electromagnetics, thermals, and precision manufacturing. From a measurement and compliance-validation perspective, this article breaks down the core challenges of 112G SerDes channels and practical ways to address them.

From BGA pads at the package, through PCB traces and vias, across connectors/backplanes, to the receiver—channel behavior determines whether 112G can be recovered reliably. Small impedance discontinuities, excessive dielectric loss, or unoptimized vias can collapse margin and cause catastrophic BER. A complete **high-speed 112G SerDes routing** strategy must consider materials, stack-up, impedance control, and manufacturing tolerances from day one so the final build meets electrical targets and remains manufacturable and reliable.

### Why is the 112G channel budget so tight?

Moving from 56G to 112G is not just “double the clock.” For 112G PAM4, Nyquist reaches 28 GHz, making loss and noise far more critical. Compared with NRZ, PAM4 eyes are vertically compressed to one third, and SNR margin drops sharply. That makes total Insertion Loss (IL) budget one of the most binding constraints in **data-center 112G SerDes routing**.

A typical 112G long-reach (LR) channel may be limited to ~30–35 dB @ 28GHz total loss, shared across package, PCB traces, vias, connectors, and receiver packaging.

- **Insertion Loss (IL):** the dominant challenge. At 28 GHz, conventional materials like FR-4 are too lossy; energy dissipates as heat, amplitude decays, and the eye closes.
- **Return Loss (RL):** caused by impedance discontinuities at vias, connectors, BGA pads, etc. Reflections create ISI and further degrade signal quality.
- **Crosstalk:** high-density routing increases coupling; NEXT/FEXT directly reduce receive SNR.
- **Channel Operating Margin (COM):** a modern scalar metric combining IL, RL, crosstalk, and Equalizer capability. COM-based optimization has become a de facto standard for 112G design.

Meeting budget requires accurate, end-to-end modeling in simulation and close collaboration with an experienced manufacturer such as Highleap PCB Factory (HILPCB) so the model matches real builds.

### Low-loss material selection: the foundation of 112G links

Materials set the physical limit for high-speed channels. At 28 GHz, Dk and Df strongly determine attenuation. Selecting appropriate low-loss materials is step one for **data-center 112G SerDes routing**.

- **Dk and Df:** Df is the key indicator of dielectric loss. For 112G, ultra low-loss materials are often required (e.g., Df < 0.004 @ 10GHz), such as Tachyon 100G, Megtron 6/7/8, Rogers RO4000. Dk stability and consistency are critical to **112G SerDes routing impedance control**.
- **Skin Effect:** at 28 GHz, current crowds to conductor surfaces, raising effective resistance and conductor loss.
- **Copper Roughness:** rough copper increases current path length and worsens skin-effect loss. VLP/HVLP copper is recommended for 112G to minimize conductor loss.
- **Fiber Weave Effect:** glass cloth (Dk≈6) and resin (Dk≈3) create local Dk variation; when routing aligns with fiber bundles, effective Dk shifts, causing impedance variation and skew. Mitigate with Spread Glass and/or routing at a small angle (e.g., 1–5°).

Material choice is also about cost and manufacturability. A good **112G SerDes routing guide** should recommend early alignment with the PCB supplier to balance performance, cost, and supply risk.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">High-speed PCB material performance comparison</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Material class</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Typical materials</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Loss factor (Df @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dielectric constant (Dk @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Typical data rate</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standard loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Medium loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Precision impedance control and routing discipline

Impedance control is the core of high-speed SI. In **high-speed 112G SerDes routing**, any deviation from target impedance (commonly 90Ω or 100Ω differential) increases reflections, jitter, and ISI. Achieving accurate **112G SerDes routing impedance control** requires both design and manufacturing execution.

**At design:**
1.  **Accurate stack-up:** use a 2D field solver (e.g., Polar Si9000) or EDA-integrated solvers. Based on material Dk, dielectric thickness, trace width/spacing, and copper thickness, calculate differential impedance with manufacturing tolerances and confirm capability with the fab.
2.  **Trace geometry:**
    *   **In-pair matching:** P/N length must be tightly matched to avoid mode conversion and skew; at 112G, typical match targets are within 1–2 mil.
    *   **Avoid sharp corners:** use arcs or 45° bends; avoid 90° corners to reduce impedance discontinuity.
    *   **Reference-plane continuity:** routes must stay over continuous ground/power reference; crossing splits causes major discontinuities.

**At manufacturing:**
Fab process control determines final impedance accuracy. Leading manufacturers such as HILPCB ensure consistency via:
- **Advanced etching:** line/space tolerance control to ±5% or tighter.
- **Tight lamination control:** stable Core and PP thickness.
- **TDR testing:** sampling or 100% on test coupons to verify impedance is within spec (e.g., ±7%).

### Vias and connector transitions: the biggest discontinuities

In multilayer PCBs, vias are essential—but they’re also among the largest impedance discontinuities in **data-center 112G SerDes routing**. A poorly optimized via can kill a 112G channel.

- **Via Stub:** unused via barrel length becomes a stub and resonates at high frequency, creating deep notches in S21. At 28 GHz, even tens of mil stubs can be fatal. Use **Back-drilling** to keep stub length within ~5–10 mil.
- **Via impedance optimization:** via impedance depends on pad, anti-pad, and barrel geometry. Use 3D EM simulation (Ansys HFSS, CST) to tune anti-pad and match trace impedance, reducing reflections.
- **Connector footprint optimization:** board connectors (QSFP-DD, OSFP) are critical transitions. Their BGA/SMT pad patterns must be co-optimized with PCB routing for smooth impedance transitions—often using Non-Circular Pad shapes and local ground removal as advanced **112G SerDes routing layout** techniques.

For complex backplanes and system boards, Microvias and blind/buried vias in [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) shorten paths and reduce parasitics, enabling high-density **high-speed 112G SerDes routing**.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes PHY optimization: via and transition rules</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Impedance continuity and common-mode suppression under PAM4 modulation</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Stub elimination and Back-drill accuracy</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Rule:</strong> 112G is extremely sensitive to <strong>stub resonance</strong>. Use full-depth back-drilling and keep stub length strictly **&lt;8 mil** (tighter than the common 10 mil) to push the first resonance above 40GHz.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Antipad EM compensation</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Rule:</strong> do not rely on heuristics. Use <strong>3D full-wave EM simulation</strong> to co-optimize antipad diameter and signal-pad geometry, compensating via parasitic capacitance and holding differential impedance variation within **±5%** of target.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Shadowing Vias strategy</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Rule:</strong> place **2–4 ground return vias** symmetrically around each differential via pair. This shrinks return-loop area, lowers interconnect inductance, and improves inter-layer crosstalk isolation beyond **-40dB** for sensitive channels.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. BGA breakout and process selection</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Rule:</strong> for 0.8mm and below pitch BGA, use **VIPPO** to save space and reduce inductance. If using “dog-bone” breakout, apply width compensation on the short segment to avoid creating a localized HF discontinuity.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>HILPCB manufacturing note:</strong> 112G success often hinges on <strong>Back-drill Tolerance</strong>. Beyond checking Gerber parameters, confirm the fab’s capability for <strong>Laser Back-drilling</strong> or controlled-depth drilling (T-Control) so production variation does not create unexpected frequency-domain notches.
</div>
</div>

### Core layout considerations for 112G SerDes routing

A successful **112G SerDes routing layout** is not just “connecting lines”—it’s an art of space, isolation, and timing. In high-density designs, crosstalk is the #2 constraint after insertion loss.

- **Spacing and crosstalk control:** larger separation reduces coupling. Common guidance is the “3W” or “5W” rule (W = single-trace width): maintain center-to-center spacing ≥ 3W/5W. In tight regions, insert a ground Guard Trace between pairs to improve isolation.
- **Stack-up and routing strategy:**
    *   **Stripline vs. Microstrip:** inner-layer Stripline (sandwiched between two reference planes) provides better EMI shielding/isolation and is preferred for long 112G runs. Outer-layer Microstrip can have slightly lower loss (field partly in air) but is more susceptible to external interference.
    *   **Orthogonal routing:** route adjacent signal layers orthogonally (e.g., L3 horizontal, L4 vertical) to reduce inter-layer crosstalk.
- **BGA breakout:** high-pin-count ASIC/FPGA BGA fields have the highest density. Breakout strategy directly impacts SI and manufacturability. Plan via placement, routing paths, and layer assignment carefully; avoid dense via farms that heavily split reference planes. This is where a detailed **112G SerDes routing guide** is essential.
- **Power Integrity (PI):** a stable low-noise PDN is required for SerDes. PDN noise converts into clock jitter and degrades signal quality. Use sufficient decoupling and PDN impedance simulation to keep supply impedance low across frequency.

### Equalization and jitter: co-design from chip to channel

Even with best materials and routing, long (tens of inches) channels still produce significant ISI. Modern SerDes includes DSP and Equalization to compensate channel loss.

- **Tx EQ:** typically FFE using Pre-emphasis/De-emphasis to boost high-frequency content and pre-compensate the channel’s low-pass behavior.
- **Rx EQ:**
    *   **CTLE:** programmable analog high-pass boosting HF to “re-open” the eye.
    *   **DFE:** nonlinear equalizer that cancels post-cursor ISI using previous decisions. It’s powerful for strong reflections/ISI but sensitive to error propagation.

The PCB goal is to create a “well-behaved” channel that equalizers can compensate easily—not a highly lossy channel that over-relies on equalization. Overly complex equalization increases power, latency, and complexity. SI engineers should work closely with silicon vendors to obtain IBIS-AMI models and co-optimize the channel and equalizer settings in simulation to maximize COM margin.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4 channel simulation sign-off report</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">Channel Operating Margin (COM) summary</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Insertion Loss (IL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Channel Operating Margin (COM)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Status: PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE target: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Insertion Loss Deviation (ILD)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Ripple: good</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Effective Return Loss (ERL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Reflection: compliant</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
💡 <strong>Engineering note:</strong> current IL is -32dB, only 3dB above the budget floor (-35dB). Considering Dk/Df tolerances in volume production, run a dedicated Monte Carlo study on the material’s <strong>HVLP copper roughness</strong> before mass production.
</div>
</div>

### From prototype to mass production: DFM analysis

Even the best simulated design is worthless if it cannot be built economically and reliably. Design–manufacturing co-optimization is essential for **data-center 112G SerDes routing**, whether you are building **112G SerDes routing low volume** prototypes or scaling to volume.

- **Manufacturing tolerance impact:** etch variation in line/space and thickness variation in lamination can shift impedance from the design target. A reliable fab (e.g., HILPCB) provides a Process Capability Guide; incorporate tolerances into simulation early and run Monte Carlo to understand worst-case performance.
- **Surface finish:** different finishes affect high-frequency behavior. ENIG is often preferred for high-speed because of flatness and conductivity, but watch for “black pad.” ENEPIG improves reliability. Choose based on cost, performance, and soldering reliability trade-offs.
- **DFM checks:** before sending Gerber/ODB++ to the fab, run comprehensive DFM to catch issues (too-small drills, narrow annular rings, Acid Traps, etc.) and avoid expensive rework. Many advanced suppliers provide DFM analysis.

Whether for low-volume prototypes or mass production, selecting a partner with advanced equipment and strict process control is critical for first-build performance and lot-to-lot consistency. We recommend an integrated supplier like HILPCB that can provide one-stop services from [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) fabrication through assembly to simplify the supply chain and protect quality.

### Compliance testing and validation: proving channel performance

As a measurement engineer, I believe “no measurement, no truth.” The goal of design and simulation is validation with physical tests. 112G SerDes link validation is complex and demands professional methods and equipment.

1.  **S-parameter measurement:** use a VNA to measure test coupons or full channels and extract S-parameters (Sdd21 insertion loss, Sdd11 return loss, crosstalk, etc.). Compare measured S-parameters with simulation to validate models and compute COM.
2.  **TDR impedance measurement:** use a TDR to measure impedance profiles of differential traces and vias. It identifies discontinuity locations and severity and directly validates **112G SerDes routing impedance control**.
3.  **Eye diagram and BER:** connect a pattern generator and BERT, test under real conditions, observe Eye Diagram opening (height/width), and measure BER to confirm spec compliance (e.g., BER < 1E-6).

These tests are essential in R&D and remain key to production QC. Sampling tests on production output help ensure continued manufacturing consistency.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion: end-to-end collaboration is the success factor

In summary, successful **data-center 112G SerDes routing** is demanding system engineering requiring cross-domain depth and seamless collaboration with manufacturing partners. From ultra low-loss material selection, to precise stack-up/impedance control, to careful optimization of vias and connectors, every step is critical.

You must go beyond traditional PCB thinking and treat the channel as a single system. Early EM simulation, deep understanding of SerDes equalization, and putting DFM first are how teams find the best balance among performance, cost, and reliability.

For organizations aiming to win at 112G and beyond, choosing a partner like Highleap PCB Factory (HILPCB)—strong in both design understanding and manufacturing execution—is a practical way to master ultra-high-speed channel challenges and accelerate time-to-market. We provide one-stop support from material consulting and DFM analysis to high-precision manufacturing and compliance validation, turning your **data-center 112G SerDes routing** design into a high-performance, reliable product.

