---
title: "Via-in-Pad Plated Over (VIPPO): Mastering Data Center Optical Module PCB Opto-Electronic Collaboration and Thermal Power Consumption Challenges"
description: "In-depth analysis of core technologies for via-in-pad plated over (VIPPO), covering high-speed signal integrity, thermal management, and power/interconnect design to help you build high-performance data center optical module PCBs."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad plated over (VIPPO)", "Microvia/stacked via", "Heavy copper 3oz+", "Hybrid stack-up (Rogers+FR-4)", "Controlled impedance", "Copper pillar"]
---

With data center traffic growing exponentially, demands for higher bandwidth, lower power consumption interconnection solutions become urgent. Co-packaged optics (CPO) technology, integrating optical engines and switch ASICs on same substrate, viewed as key breakthrough overcoming traditional pluggable optical module bottlenecks. However, this unprecedented integration also brings severe PCB design and manufacturing challenges. As CPO engineer, I deeply understand that in opto-electronic collaboration and thermal power consumption tradeoffs, advanced PCB interconnection technology is success foundation. Among these, **via-in-pad plated over (VIPPO)** technology is core for mastering this complexity. It's not merely ultra-high-density routing realization key, but signal integrity and thermal management efficiency support point.

This article deeply analyzes **via-in-pad plated over (VIPPO)** application in CPO optical module PCB design, combining **microvia/stacked via**, **heavy copper 3oz+**, **hybrid stack-up (Rogers+FR-4)**, **controlled impedance**, and **copper pillar** key technologies, revealing how building stable, efficient, manufacturable CPO systems.

## CPO Board-Level Routing and Opto-Electronic Interface Collaboration: VIPPO Core Value

In CPO architecture, high-speed electrical signal paths (like 224G PAM4) from ASIC to optical engine drastically shortened, but requiring PCB substrates unprecedented routing density and signal integrity. Traditional "dog-bone" via structures occupy valuable routing space, introducing unnecessary signal path length and parasitic inductance, severely affecting high-frequency signal quality.

**Via-in-pad plated over (VIPPO)** technology places vias directly under solder pads, completely filling with conductive material (typically copper), finally performing planarization electroplating, thoroughly solving these problems. Core advantages manifest as:

1. **Extreme Routing Density:** VIPPO eliminates pad-external fan-out traces and via pads, allowing BGA high-density device pins direct inter-routing, providing ample space for parallel opto-electronic signal transmission. Combined with **microvia/stacked via** technology, achieving complex vertical interconnections in tiny areas, standard CPO substrate configuration.

2. **Shortest Signal Paths:** Signals directly from device pads through VIPPO structures enter inner layer traces, shortest paths, effectively reducing parasitic inductance and capacitance, providing ideal physical foundation for achieving precise **controlled impedance**. For PAM4 extremely noise and reflection-sensitive modulation signals, VIPPO is key ensuring eye diagram opening.

3. **Optimized Power Integrity (PI):** Through extensive VIPPO use on power and ground planes, significantly reducing power distribution network (PDN) impedance. This provides stable, low-noise power for ASICs and optical engines, reducing synchronous switching noise (SSN) interference with high-speed signals.

At HILPCB, we possess mature VIPPO manufacturing processes, achieving precise micro-hole filling and perfect planarization, ensuring subsequent SMT assembly reliability, providing solid [high-density interconnection (HDI) PCB](https://hilpcb.com/en/products/hdi-pcb) manufacturing foundation for your CPO projects.

## Thermal Design: CPO Power Distribution and Cooling Structure

CPO places massive-power ASICs (reaching hundreds of watts) and temperature-sensitive optical engines (lasers, modulators) in close proximity, forming severe "hot spot" challenges. Thermal management no longer merely system-level problem but multi-level collaboration spanning chips, substrates to heatsinks. **Via-in-pad plated over (VIPPO)** plays critical thermal conduction channel role here.

- **Vertical Heat Conduction Paths:** Copper-filled VIPPO structures essentially efficient thermal columns, rapidly conducting heat from device bottoms to PCB inner thermal planes or directly to back-side heatsinks. Compared to traditional hollow vias, thermal efficiency increases several-fold.

- **Collaboration with Heavy Copper Layers:** Handling enormous currents and heat, CPO substrates typically employ **heavy copper 3oz+** technology. VIPPO seamlessly connects with these thick copper layers, forming three-dimensional, efficient heat dissipation networks. Heat conducts vertically through VIPPO, then disperses laterally through **heavy copper 3oz+** planes, effectively reducing hot spot temperatures, guaranteeing optical device operating stability and lifespan.

- **Supplementary Cooling Technologies:** Under extreme cooling demands, **copper pillar** (copper pillar) technology used for chip-level interconnection and cooling. These micrometer-scale copper pillars directly connect chips and substrates, providing superior electrical and thermal performance compared to traditional solder balls. Board-level VIPPO and chip-level **copper pillar** jointly build complete, low-thermal-resistance paths from chips to heatsinks.

## Low CTE and Material Stacking: Reliability and Warping Control

CPO module long-term reliability largely depends on mechanical stability during operating temperature cycling. Silicon-based ASICs and photonic integrated circuits (PICs) thermal expansion coefficients (CTE) approximately 2.6 ppm/°C, while traditional FR-4 substrates reach 14-18 ppm/°C. This enormous CTE mismatch produces massive stress on solder joints (like BGA solder balls or **copper pillar**), ultimately causing fatigue failure.

Therefore, CPO substrate material selection and stackup design are critical:

- **Hybrid stack-up (Rogers+FR-4):** Common cost-performance balanced strategy. Near CPO chip critical signal layers, use low-CTE, low-loss special materials (like Rogers or Tachyon series) matching chip CTE and guaranteeing signal integrity. For performance-non-critical power or peripheral circuit layers, use lower-cost FR-4 materials. This **hybrid stack-up (Rogers+FR-4)** design imposes extreme lamination process requirements.

- **Low-CTE Core Materials and Prepregs:** Selecting substrates with better CTE matching to chips is fundamental solution. For example, certain special resin system materials can reduce CTE to 6-8 ppm/°C. This significantly reduces thermal stress, improving entire component reliability.

- **Symmetric Stacking and Warping Control:** Designing **hybrid stack-up (Rogers+FR-4)** structures must strictly follow symmetry principles, balancing internal stress from different materials during lamination and reflow soldering, preventing PCB warping. Warping not only affects SMT assembly precision but causes catastrophic fiber array alignment impact. HILPCB possesses rich experience handling complex [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) and hybrid material stacking, controlling warping to industry-leading levels.

## CPO Testing/Calibration and Online Monitoring

CPO module complexity determines test and verification processes far exceed traditional PCBs. Testing involves not only electrical signal bit error rate (BER) and eye diagram analysis, but optical power, wavelength, and signal-to-noise ratio optical performance measurements.

1. **Loopback Testing (Loopback):** During PCB design phase, must reserve electrical and optical loopback test paths. This enables ASIC SerDes and optical engine electrical-optical/optical-electrical conversion function preliminary verification without external equipment connection.

2. **Online Monitoring and CMIS:** CPO modules must comply with common module management interface specifications (CMIS), real-time reporting module health status through I2C interfaces, like laser temperature, bias current, received optical power. PCB design must provide clear, isolated routing paths for these monitoring circuits.

3. **High-Frequency Test Interfaces:** For precise eye diagram and BER testing, need extracting signals reaching 112GHz from CPO substrates. Usually through board-mounted miniature coaxial connectors (like 2.92mm or 1.85mm). These connector layout and routing themselves are challenges, strictly following **controlled impedance** principles, avoiding test result distortion.

4. **ATE (Automated Test Equipment) Compatibility:** PCB design must consider ATE probe station compatibility, reserving sufficient test points (Test Pad). VIPPO technology test points have flat surfaces, high contact reliability, very suitable for high-density probe testing.

## Manufacturability: Tolerances, Fixtures, and Assembly Processes

Excellent designs worthless if not economically, reliably manufactured. CPO substrate manufacturability design (DFM) and assembly design (DFA) are project success keys.

- **Manufacturing Tolerances:** CPO substrates impose extremely stringent requirements on line width/spacing, inter-layer alignment, drilling precision. For example, **controlled impedance** precision directly depends on dielectric thickness and line width control capability. HILPCB through advanced AOI (automatic optical inspection) and LDI (laser direct imaging) equipment can control manufacturing tolerances to micrometer levels.

- **Fiber Array Alignment:** Achieving sub-micrometer precision alignment between fiber arrays (Fiber Array) and photonic integrated circuits (PIC) optical grating or edge couplers is most challenging CPO assembly step. PCB must design high-precision fiducials (Fiducials), potentially integrating V-groove (V-groove) auxiliary alignment structures. PCB flatness and dimensional stability are critical.

- **Assembly Fixtures and Curing:** After alignment completion, use ultraviolet (UV) or thermal curing adhesives permanently fixing fiber arrays. This requires specially designed assembly fixtures maintaining alignment precision during curing without shifting. PCB design must reserve sufficient space and support points for these fixtures.

- **One-Stop Solutions:** CPO complexity makes design, manufacturing, assembly step communication costs extremely high. Selecting partners like HILPCB providing PCB manufacturing through [one-stop PCBA assembly](https://hilpcb.com/en/products/turnkey-assembly) services greatly simplifies supply chains, reducing multi-party coordination problems, accelerating product time-to-market. Our professional engineer teams intervene from design initial stages, providing DFM/DFA recommendations ensuring smooth mass production.

<div style="background: linear-gradient(135deg, #020617 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a5b4fc; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🚀 CPO Packaging: 224G Era Signal Integrity (SI) Physical Layer Guidelines</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Addressing Extreme Link Budget Challenges in Silicon Photonic Engine and ASIC Co-Packaging</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">01. Impedance Tolerance Extreme Control (Z-Accuracy)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Core Logic:</strong>At 224Gbps rates, impedance drops directly close eye diagrams. Must control differential impedance within <strong>±5%</strong>. Utilize HILPCB precise second-order etch compensation models, eliminating manufacturing line width variation effects on signal reflection.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">02. Ultra-Low Loss Material System (UL-Loss)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Core Logic:</strong>Select Megtron 8 or Rogers <strong>Ultra-Low Loss</strong> level dielectric materials, paired with HVLP3 (hyper-low profile) copper foil, offsetting skin effect-produced loss. Ensure millimeter-level link insertion loss (IL) complies with CPO stringent energy efficiency standards.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">03. VIPPO Structure and Resonance Suppression</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Core Logic:</strong>Employ <strong>VIPPO (Via-in-Pad Plated Over)</strong> technology combined with full-depth back-drilling, completely eliminating via stubs (Stub). Reduce parasitic capacitance, shifting resonance points outside working bandwidth.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">04. 3D Full-Wave Crosstalk Simulation (X-Talk)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Core Logic:</strong>In high-density routing areas, must perform 3D electromagnetic full-wave simulation. Optimize <strong>GND shielding</strong> via arrays and differential pair spacing, suppressing FEXT and NEXT below -40dB.</p>
</div>
</div>

<div style="margin-top: 35px; padding: 25px; background: rgba(165, 180, 252, 0.1); border-radius: 16px; border-right: 8px solid #818cf8; font-size: 0.95em; line-height: 1.7; color: #c7d2fe;">💡 <strong>HILPCB Expert Recommendation:</strong>In CPO design, thermal vias under optical engines often conflict with high-speed signal paths. We recommend <strong>Non-uniform Grid</strong> layout technique, securing thermal conductivity while 3D simulation optimizes signal return paths, preventing ground plane reference integrity damage.</div>
</div>

## CPO 224G Era Signal Integrity (SI) Physical Layer Guidelines

| Guideline | Core Logic | Implementation |
| :--- | :--- | :--- |
| **01. Impedance Tolerance Extreme Control (Z-Accuracy)** | At 224Gbps rates, impedance drops directly close eye diagrams. Must control differential impedance within **±5%**. | Utilize HILPCB precise second-order etch compensation models, eliminating manufacturing line width variation effects on signal reflection. |
| **02. Ultra-Low Loss Material System (UL-Loss)** | Select Megtron 8 or Rogers **Ultra-Low Loss** level dielectric materials, paired with HVLP3 (hyper-low profile) copper foil, offsetting skin effect-produced loss. | Ensure millimeter-level link insertion loss (IL) complies with CPO stringent energy efficiency standards. |
| **03. VIPPO Structure and Resonance Suppression** | Employ **VIPPO (via-in-pad plated over)** technology combined with full-depth back-drilling, completely eliminating via stubs (Stub). | Reduce parasitic capacitance, shifting resonance points outside working bandwidth, significantly improving Nyquist frequency signal quality. |
| **04. 3D Full-Wave Crosstalk Simulation (X-Talk)** | In high-density routing areas, must perform 3D electromagnetic full-wave simulation. | Optimize **GND shielding** via arrays and differential pair spacing, suppressing FEXT (far-end crosstalk) and NEXT (near-end crosstalk) below -40dB. |

<div style="background-color: #1A237E; color: #ffffff; padding: 25px; border-radius: 10px; margin: 30px 0;">
    <h3 style="color: #ffffff; text-align: center; border-bottom: 2px solid #42A5F5; padding-bottom: 10px;">HILPCB CPO Substrate Core Manufacturing Capability</h3>
    <table style="width: 100%; margin-top: 15px; border-collapse: collapse; color: #000000;">
        <thead style="background-color: #42A5F5;">
            <tr>
                <th style="padding: 12px; text-align: left;">Technical Parameter</th>
                <th style="padding: 12px; text-align: left;">HILPCB Capability</th>
                <th style="padding: 12px; text-align: left;">CPO Value</th>
            </tr>
        </thead>
        <tbody style="background-color: #ffffff;">
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Via-in-Pad Plated Over</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Electroplated copper/resin filling, flatness &lt; 15µm</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Achieves maximum routing density, optimizes signal/thermal paths</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Microvia/Stacked Via</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Supports up to 4+N+4 stage stacked/interleaved blind buried vias</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Builds complex 3D interconnections, shortens signal paths</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Heavy Copper 3oz+</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Inner/outer layers support 3-10oz copper thickness</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Carries large currents, efficient heat dissipation, improves power integrity</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Hybrid Stack-up</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Expert in Rogers/Megtron/Tachyon and FR-4 hybrid lamination</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Balances cost, performance, reliability, controls CTE mismatch</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Controlled Impedance</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Tolerance control ±5%, provides TDR test reports</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Guarantees high-speed signal transmission quality, reduces bit error rate</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**Via-in-pad plated over (VIPPO)** technology is not merely single via manufacturing process; it's support point for entire CPO ecosystem. Through providing unparalleled routing density, excellent signal integrity, efficient heat dissipation channels, perfectly addressing CPO opto-electronic collaboration and thermal power consumption core challenges. When VIPPO combines with **microvia/stacked via** high density, **heavy copper 3oz+** high-current heat dissipation capability, **hybrid stack-up (Rogers+FR-4)** cost-effective material solutions, and **controlled impedance** precise signal control, high-performance, high-reliability CPO optical module substrates realize.

On path toward 800G, 1.6T and higher bandwidth, PCB technology requirements only increase. As your trusted partner, HILPCB leveraging deep accumulation in [heavy copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb) and complex high-frequency board manufacturing, commits providing cutting-edge CPO substrate solutions to global customers. We deeply understand every technology iteration success stems from extreme detail pursuit. Choosing HILPCB means choosing professionalism, reliability, and innovation, jointly mastering data center futures.

