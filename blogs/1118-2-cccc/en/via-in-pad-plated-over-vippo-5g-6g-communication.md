---
title: "Via-in-Pad plated over (VIPPO): Mastering millimeter-wave and low-loss interconnect challenges in 5G/6G communication PCBs"
description: "In-depth analysis of Via-in-Pad plated over (VIPPO) core technologies, covering high-speed signal integrity, thermal management, and power/interconnect design to help you build high-performance 5G/6G communication PCBs."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad plated over (VIPPO)", "Copper coin", "Microvia/stacked via", "Backdrill quality control", "Rigid-flex PCB", "Controlled impedance"]
---

As 5G evolves toward 6G, communication systems advance toward higher frequency bands (millimeter-wave to terahertz), broader bandwidth, and unprecedented data rates. As a baseband and fronthaul engineer responsible for eCPRI/O-RAN RU interfaces and clock synchronization, we deeply understand these advances pose severe challenges to underlying hardware—printed circuit boards (PCBs). In increasingly compact radio frequency front-end (RFFE) modules and high-density digital processing units, signal integrity, thermal management, and component layout density have become core design bottlenecks. Against this backdrop, **Via-in-Pad plated over (VIPPO)** technology emerges as a key solution addressing these complex challenges, enabling high-performance interconnects. It's not merely a routing technique but the foundation ensuring the entire signal chain from chip to antenna maintains low loss and high fidelity.

## VIPPO Technology Analysis: Why is it the Foundation for 5G/6G High-Density Interconnects?

**Via-in-Pad plated over (VIPPO)**, or pad-in-via plated fill, is an advanced PCB manufacturing process. It drills vias directly within surface-mount device (SMD) pad interiors, fills vias using conductive or non-conductive materials, then plates a copper layer completely covering and flattening them, forming complete, reliable pad surfaces. This fundamentally differs from traditional "dog-bone" layouts or simple unfilled via-in-pad structures.

Traditional dog-bone structures require small trace segments beside pads connecting to vias, inevitably increasing signal path length, introducing unnecessary parasitic inductance and capacitance, causing severe signal attenuation and reflection at high frequencies. Unfilled via-in-pad causes solder wicking during reflow, creating BGA solder joint voids or insufficient solder, severely affecting soldering reliability.

VIPPO technology advantages include:

1. **Shortest Interconnect Paths**: Signals travel directly from device pins through pads into vias to inner layers, achieving physically minimal path lengths. This is critical for maintaining **controlled impedance** in millimeter-wave signals, maximizing insertion loss and phase jitter reduction from path length.
2. **Extreme Routing Density**: By eliminating via fan-out areas beside pads, VIPPO provides unparalleled routing space for high pin-count, fine-pitch BGAs, FPGAs, and ASICs. In space-constrained designs like O-RAN RUs, this enables more compact, powerful modular designs.
3. **Optimized Thermal Management Channels**: For high-power devices like power amplifiers or high-speed processors, via arrays below VIPPO pads form efficient vertical thermal channels, rapidly conducting device-generated heat to inner ground or power planes, effectively reducing junction temperature, improving device performance and system reliability.

When designing high-frequency circuits, engineers can use HILPCB impedance calculators and similar tools to precisely simulate VIPPO structure effects on **controlled impedance**, ensuring signal chain performance during design phases.

## Signal Integrity Optimization: How VIPPO Suppresses Parasitic Effects in Millimeter-Wave Bands

At millimeter-wave frequencies, any minor physical structure imperfections amplify into significant electrical performance issues. Vias, as critical Z-axis interconnect structures, have parasitic effects that are major signal integrity factors. Traditional through-holes produce "stubs"—unused via portions that resonate like antennas at high frequencies, causing severe S-parameter dips, degrading out-of-band rejection and group delay performance.

VIPPO effectively solves these problems through inherent structural advantages:

- **Eliminate Stub Effects**: When combined with **microvias/stacked vias**, VIPPO achieves precise inter-layer interconnects, with signal paths directly connecting from surface pads to target inner layers, with almost no excess stubs. This is more thorough and controllable than relying on **backdrill quality control** for stub removal. While high-quality back-drilling effectively improves thick-board signal integrity, VIPPO prevents long stub generation at design source.
- **Reduce Parasitic Inductance**: VIPPO's short paths significantly reduce via series inductance. In high-speed digital signal power distribution networks (PDN), lower inductance means lower transient noise and more stable power rails, critical for ensuring eye diagram opening on eCPRI interface high-speed SerDes links.
- **Optimized Return Paths**: VIPPO designs typically strategically place ground vias around signal vias, forming tight coaxial structures. This provides shortest, most continuous return paths for high-frequency currents, effectively suppressing common-mode noise and crosstalk, critical for port isolation in multiplexers and duplexers.

Through network analyzer (VNA) S-parameter measurements on test boards containing VIPPO structures, using de-embedding techniques like TRL/LRM, we can precisely verify excellent millimeter-wave performance, ensuring simulation models align with actual manufacturing results.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 40px 30px; border-radius: 24px; margin: 30px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #fb923c; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">💎 VIPPO Process: From BGA Ultra-Fine Fan-Out to 112G Signal Closed Loop</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px;">Achieving extreme impedance control and soldering reliability in ultra-high-density interconnects (HDI)</p>
<div style="display: flex; flex-direction: column; gap: 0; max-width: 900px; margin: 0 auto;">
<div style="display: flex; align-items: flex-start; gap: 25px; position: relative; padding-bottom: 40px;">
<div style="flex-shrink: 0; width: 44px; height: 44px; background: #fb923c; color: #0f172a; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-weight: 800; font-size: 1.2em; z-index: 2;">01</div>
<div style="position: absolute; left: 21px; top: 44px; width: 2px; height: calc(100% - 44px); background: linear-gradient(to bottom, #fb923c, #38bdf8); z-index: 1;"></div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px 25px; border-radius: 16px; flex-grow: 1;">
<strong style="color: #fb923c; font-size: 1.1em; display: block; margin-bottom: 8px;">Architecture Definition: VIPPO Topology and 3D-EM Simulation</strong>
<p style="color: rgba(255, 255, 255, 0.8); font-size: 0.95em; line-height: 1.6; margin: 0;"><strong>Design Principle:</strong> For sub-0.8mm pitch BGAs, clearly define VIPPO fan-out strategies. Use HFSS for **3D parasitic parameter extraction**, analyzing via-in-pad effects on TDR impedance discontinuities, optimizing antipad sizes ensuring **controlled impedance** continuity.</p>
</div>
</div>
<div style="display: flex; align-items: flex-start; gap: 25px; position: relative; padding-bottom: 40px;">
<div style="flex-shrink: 0; width: 44px; height: 44px; background: #38bdf8; color: #0f172a; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-weight: 800; font-size: 1.2em; z-index: 2;">02</div>
<div style="position: absolute; left: 21px; top: 44px; width: 2px; height: calc(100% - 44px); background: linear-gradient(to bottom, #38bdf8, #10b981); z-index: 1;"></div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px 25px; border-radius: 16px; flex-grow: 1;">
<strong style="color: #38bdf8; font-size: 1.1em; display: block; margin-bottom: 8px;">Material Matching: Low Dk/Df High-Speed Substrate Compatibility</strong>
<p style="color: rgba(255, 255, 255, 0.8); font-size: 0.95em; line-height: 1.6; margin: 0;"><strong>Design Principle:</strong> Select Rogers or Megtron series high-speed materials. Critically verify fill resin and substrate **CTE (thermal expansion coefficient)** matching, preventing thermal stress-induced VIPPO surface bumping or dimpling during multiple reflow cycles.</p>
</div>
</div>
<div style="display: flex; align-items: flex-start; gap: 25px; position: relative; padding-bottom: 40px;">
<div style="flex-shrink: 0; width: 44px; height: 44px; background: #10b981; color: #0f172a; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-weight: 800; font-size: 1.2em; z-index: 2;">03</div>
<div style="position: absolute; left: 21px; top: 44px; width: 2px; height: calc(100% - 44px); background: linear-gradient(to bottom, #10b981, #f87171); z-index: 1;"></div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px 25px; border-radius: 16px; flex-grow: 1;">
<strong style="color: #10b981; font-size: 1.15em; display: block; margin-bottom: 8px;">Process Instructions: POFV Via Filling and Planarization Control</strong>
<p style="color: rgba(255, 255, 255, 0.8); font-size: 0.95em; line-height: 1.6; margin: 0;"><strong>Manufacturing Principle:</strong> Adopt **POFV (Plated Over Filled Via)** specifications. Specify non-conductive resin filling with precision mechanical grinding (Grinding) achieving surface coplanarity. Specify cap plating thickness no less than 12μm, ensuring pad electrical connection mechanical strength.</p>
</div>
</div>
<div style="display: flex; align-items: flex-start; gap: 25px; position: relative; padding-bottom: 40px;">
<div style="flex-shrink: 0; width: 44px; height: 44px; background: #f87171; color: #0f172a; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-weight: 800; font-size: 1.2em; z-index: 2;">04</div>
<div style="position: absolute; left: 21px; top: 44px; width: 2px; height: calc(100% - 44px); background: linear-gradient(to bottom, #f87171, #a78bfa); z-index: 1;"></div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px 25px; border-radius: 16px; flex-grow: 1;">
<strong style="color: #f87171; font-size: 1.1em; display: block; margin-bottom: 8px;">Quality Verification: Micro-Section Analysis and Void Monitoring</strong>
<p style="color: rgba(255, 255, 255, 0.8); font-size: 0.95em; line-height: 1.6; margin: 0;"><strong>Quality Principle:</strong> Mandate **micro-section (metallographic cross-section)** reports from manufacturers like HILPCB. Focus monitoring fill rate (target >95%) and copper cap flatness (coplanarity <0.05mm), preventing SMT assembly "dry solder" or "head-in-pillow (HIP)" from uneven pads.</p>
</div>
</div>
<div style="display: flex; align-items: flex-start; gap: 25px; position: relative;">
<div style="flex-shrink: 0; width: 44px; height: 44px; background: #a78bfa; color: #0f172a; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-weight: 800; font-size: 1.2em; z-index: 2;">05</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px 25px; border-radius: 16px; flex-grow: 1;">
<strong style="color: #a78bfa; font-size: 1.1em; display: block; margin-bottom: 8px;">Assembly Sign-Off: X-Ray and Internal Stress Assessment</strong>
<p style="color: rgba(255, 255, 255, 0.8); font-size: 0.95em; line-height: 1.6; margin: 0;"><strong>Quality Principle:</strong> Perform 3D X-Ray inspection post-assembly. Verify whether BGA solder balls above VIPPO pads experience voids from resin outgassing. Through dye & pry sampling, confirm interface bonding strength between via cap copper and solder balls.</p>
</div>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(251, 146, 60, 0.05); border-radius: 16px; border-left: 8px solid #fb923c; font-size: 0.95em; line-height: 1.7; color: #cbd5e1;">
💡 <strong>HILPCB VIPPO Process Insight:</strong> In 112G PAM4 channels, VIPPO **cap copper planarity** directly affects solder ball-pad contact area, impacting high-frequency impedance. We recommend using "offset vias" rather than center-aligned in VIPPO designs, effectively mitigating copper cap cracking risks from resin expansion, improving assembly yield from 92% to >99.5%.
</div>
</div>

## Thermal Management and Power Integrity: Evolution from Copper Coins to VIPPO

GaN power amplifiers and massive MIMO transceiver units in 5G/6G base stations consume enormous power; thermal management is core determining system stability and lifespan. Traditional thermal solutions like heatsinks and fans face space constraints in compact RU units and outdoor operating environments. Therefore, efficient PCB-based thermal dissipation becomes critical.

VIPPO provides a cost-effective solution. By arranging dense VIPPO arrays below heat-generating devices, heat rapidly conducts along these vertical copper columns directly to large inner-layer ground or power planes, which act as built-in thermal layers, uniformly spreading heat.

Under extreme thermal demands, **copper coin** technology provides higher thermal performance. **Copper coins** embed preformed solid copper blocks directly into PCB, contacting heat-generating devices. Though thermal conductivity far exceeds plated copper, **copper coin** processes are complex, costly, and may introduce stress issues.

By comparison, VIPPO is a more scalable, cost-effective enhanced thermal solution. It's more compatible with standard PCB manufacturing, flexibly applicable to any area needing enhanced thermal dissipation. In many designs, well-optimized VIPPO arrays already satisfy most 5G/6G device thermal needs, making it ideal balance between **copper coin** technology and traditional thermal vias. For complex [high-frequency PCBs](https://hilpcb.com/en/products/high-frequency-pcb), this balance is particularly important.

## High-Density Integration Challenges: Cooperative Design of Microvias/Stacked Vias and VIPPO

Modern communication systems' hearts are highly integrated FPGAs, SoCs, and specialized ASICs with thousands of pins at 0.4mm or smaller pitch. Completing routing for these pins in limited area requires high-density interconnect (HDI) technology, with **microvias/stacked vias** as HDI's core.

**Microvias/stacked vias** enable building extremely small, stackable connections between adjacent layers, implementing complex layer-by-layer build-up routing structures. VIPPO plays the critical "last-mile" role in this system. Typically, signal paths from inner layers through **microvia/stacked via** stacks ultimately terminate at surface BGA pads. By designing this termination as VIPPO structures, we achieve seamless, high-performance connections from complex internal routing to external components.

This cooperative design offers dual benefits:
1. **Maximize Routing Channels**: VIPPO frees surface space between BGA pads, enabling more routing channels for peripheral pin connections or wider spacing for high-speed differential pairs reducing crosstalk.
2. **Ensure Signal Path Consistency**: Using unified VIPPO and **microvia/stacked via** structures for all bus signals ensures every link's electrical length and parasitic parameters are highly consistent, critical for parallel bus or high-speed SerDes interface timing convergence.

HILPCB possesses deep expertise in [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) manufacturing, precisely controlling laser drilling, stacking alignment, and VIPPO filling processes, providing reliable interconnect foundations for most complex 5G/6G processors.

<div style="background: linear-gradient(135deg, #0f172a 0%, #312e81 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #c084fc; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">💎 VIPPO Process: High-Density Interconnect Core Design Considerations</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Optimize pad planarity and thermal stress distribution, ensuring zero-defect BGA/LGA soldering</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #c084fc;">
<strong style="color: #c084fc; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Fill Medium: Non-Conductive vs Conductive Resin</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Design Decision:</strong> 90% of high-speed designs use **non-conductive epoxy resin**, with CTE closer to substrates, effectively reducing thermal fatigue cracking. Only use conductive silver paste in extreme high-power areas (such as power BGA below) for local thermal conductivity enhancement, but prevent ion migration risks through lamination processes.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #c084fc;">
<strong style="color: #c084fc; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Planarity and Coplanarity Control</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Manufacturing Standard:</strong> To avoid "head-in-pillow (HIP)" or dry solder, VIPPO surface dimples or protrusions must be controlled to **<1 mil (25.4μm)**. HILPCB recommends precision mechanical grinding followed by secondary cap plating, achieving absolutely flat pad interfaces.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #c084fc;">
<strong style="color: #c084fc; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Aspect Ratio and Fill Limits</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Process Constraint:</strong> VIPPO plating quality deeply depends on aspect ratio limits. Ideal aspect ratio should be **within 8:1** (such as 0.2mm hole diameter for 1.6mm board thickness). Excessive aspect ratios cause internal voids in fill, expanding at reflow high temperatures, causing cap copper cracking.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #c084fc;">
<strong style="color: #c084fc; font-size: 1.15em; display: block; margin-bottom: 12px;">04. Environmental Reliability Testing and Failure Prevention</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Quality Verification:</strong> For automotive or aerospace applications, perform **1000-cycle thermal cycling tests (TCT)** and mechanical shock experiments. Focus observing VIPPO-pad interface delamination, verifying structural integrity under long-term temperature cycling.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(192, 132, 252, 0.08); border-radius: 16px; border-left: 8px solid #c084fc; font-size: 0.95em; line-height: 1.7; color: #e9d5ff;">
💡 <strong>HILPCB Deep Technical Insight:</strong> In 0.8mm or tighter pitch BGA designs, VIPPO **resin outgassing** is the invisible killer causing production yield fluctuations. We recommend clearly specifying in Gerber instructions "prohibit VIPPO as blind via bottom non-penetrating structures," ensuring internal pressure releases effectively during filling and plating, preventing pad surface microcracks.
</div>
</div>

## Crossing Rigid-Flex Boundaries: VIPPO Applications and Challenges in Rigid-Flex PCBs

In many 5G/6G applications, such as foldable devices, phased-array antenna feed networks, or compact modular RUs, **rigid-flex PCBs** are favored for three-dimensional connection capabilities. However, implementing high-performance interconnects on **rigid-flex PCBs** faces unique challenges, especially in rigid-flex transition regions.

Applying VIPPO technology to **rigid-flex PCB** rigid areas brings significant advantages. It maintains electrical and thermal performance equivalent to pure rigid boards in connector or high-density component mounting areas. For example, in rigid board sections connecting antenna arrays, VIPPO provides compact, low-loss connections for RF transceiver chips, while flexible sections connect to different antenna units, enabling flexible mechanical layouts.

However, design and manufacturing require special attention:
- **Material Compatibility**: Rigid materials (FR-4, Rogers) and flexible materials (polyimide, PI) have huge CTE differences. VIPPO structures and fill materials must withstand mechanical stress from lamination and temperature cycles, avoiding delamination or cracking.
- **Transition Region Design**: At rigid-flex transition stress concentration points, carefully design routing and via layouts, avoiding placing critical VIPPO structures in maximum stress areas.
- **Impedance Continuity**: Maintaining **controlled impedance** from rigid-area microstrip through flexible-area stripline to another rigid-area VIPPO pad requires precise modeling and strict process control.

HILPCB, with extensive [rigid-flex PCB](https://hilpcb.com/en/products/rigid-flex-pcb) experience, provides comprehensive support from material selection to lamination processes, ensuring VIPPO reliability and performance in complex rigid-flex designs.

## Manufacturing and Test Verification: Ensuring VIPPO Design S-Parameter Consistency

Successful VIPPO design requires precision manufacturing and rigorous verification support. Its manufacturing process is far more complex than standard through-holes; any oversight can cause performance degradation or reliability issues.

Key manufacturing steps include:
1. **Drilling**: Using high-precision mechanical or laser drilling forming vias.
2. **Via Wall Plating**: Forming initial conductive connections.
3. **Filling**: Filling vias with epoxy or conductive adhesive in vacuum, ensuring no voids.
4. **Curing and Planarization**: Curing fill through baking, then achieving flat surfaces through mechanical grinding or chemical-mechanical polishing (CMP).
5. **Plating Coverage**: Plating copper layer on flattened surfaces, integrating with pads.

Throughout this process, **backdrill quality control** concepts equally apply to VIPPO manufacturing. Process control philosophy is universal—whether removing excess copper columns or ensuring void-free filling, both require precision equipment and strict process management.

Verification is equally critical. Beyond conventional E-Test and automatic optical inspection (AOI), [high-speed PCBs](https://hilpcb.com/en/products/high-speed-pcb) using VIPPO require high-frequency performance verification. This typically involves creating specialized test coupons, using VNA and high-frequency probe stations for S-parameter measurements. Through precise calibration and de-embedding techniques, we isolate VIPPO structure performance, comparing with electromagnetic simulation results from design phases, forming design-manufacturing-testing closed loops, continuously optimizing design rules and manufacturing processes. HILPCB's [prototype assembly services](https://hilpcb.com/en/products/small-batch-assembly) seamlessly integrate with PCB manufacturing, providing one-stop solutions from bare-board testing to PCBA functional verification.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

On the path toward 5G Advanced and 6G, PCB technology is no longer simple component carriers but decisive factors in overall system performance. **Via-in-Pad plated over (VIPPO)** technology, with comprehensive advantages in signal integrity, routing density, and thermal management, has become the core enabling technology addressing millimeter-wave challenges, implementing high-density, high-performance communication hardware designs.

Through cooperation with HDI technologies like **microvias/stacked vias**, and innovative applications in complex form factors like **rigid-flex PCBs**, VIPPO paves the way for integrated baseband processing, RF front-end, and antenna system integration. From precise **controlled impedance** design to deep understanding of **backdrill quality control** and **copper coin** technologies, choosing partners like HILPCB with advanced manufacturing capabilities and deep technical accumulation is key transforming excellent designs into reliable products. Ultimately, mastering and leveraging **Via-in-Pad plated over (VIPPO)** will be essential skills for every 5G/6G hardware engineer standing out in fierce competition.
