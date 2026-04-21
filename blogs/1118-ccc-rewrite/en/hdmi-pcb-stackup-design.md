---
title: "How to Define an HDMI PCB Stackup: 100 Ohm Differential, Loss Budget, and Connector Transitions"
description: "A direct answer to the version target, 100 ohm differential impedance, reference planes, material loss, and connector-transition issues that should be reviewed first in HDMI PCB stackup design, helping HDMI 2.0 and 2.1 video links preserve margin in a manufacturable stack."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# How to Define an HDMI PCB Stackup: 100 Ohm Differential, Loss Budget, and Connector Transitions

- **The core of HDMI stackup planning is not "how many layers the board should have," but "how much manufacturing margin the link still has at the target rate."** The official HDMI 2.1b overview gives total bandwidth capability up to **48Gbps**, while TI's TMDS1204 datasheet shows HDMI 2.1 FRL lane rates of **3/6/8/10/12Gbps**. At those speeds, stackup, vias, and connector transitions can no longer be reviewed separately.
- **The basic target is still 100 ohm differential impedance, but the real difficulty is whether production can still hold that target.** Multiple TI HDMI layout documents explicitly call for **100 ohm differential impedance**, and actual laminated thickness, etch compensation, and copper roughness directly change the hardware result.
- **Reference-plane continuity and launch transitions often consume eye margin before the straight traces do.** Plane splits, layer changes, stubs, and poor anti-pad geometry can turn an otherwise acceptable pair into mode conversion and EMI trouble.
- **Not every HDMI board needs premium low-loss materials, but not every project is safe on ordinary FR-4 either.** The better sequence is to calculate link margin from rate, length, and transition count first, then choose material and stackup, instead of choosing board layers first and hoping the link fits.
- **Validation needs real fabrication data.** The value of impedance coupons, microsections, TDR, or insertion-loss tests is proving that the manufactured geometry still resembles the model, not merely proving that a 100 ohm differential pair was drawn in simulation.

> **Quick Answer**  
> The point of HDMI PCB stackup design is to make 100 ohm differential pairs, continuous reference planes, low-loss geometry, and connector transitions all work together at the target version and lane rate. A stackup is only truly useful when it still preserves link margin after lamination, etching, and assembly, not only when impedance can be calculated in software.

## Table of Contents

- [What should engineers review first in HDMI PCB stackup design?](#overview)
- [Summary table of key rules and parameters](#rules)
- [Why should HDMI stackup start with a loss budget based on rate and length?](#loss-budget)
- [Why must 100 ohm differential impedance be tied to real fabrication?](#impedance)
- [Why are connectors, layer changes, and stubs more dangerous than straight traces?](#transitions)
- [How should HDMI stackups be validated before production?](#validation)
- [Next steps with HILPCB](#next-steps)
- [Frequently Asked Questions (FAQ)](#faq)
- [Public references](#references)
- [Author and review information](#author)

<a id="overview"></a>
## What should engineers review first in HDMI PCB stackup design?

Start with **the target HDMI version, lane rate, board-level trace length, reference planes, and connector transitions**.

This is not the same as saying "route the differential pair using standard high-speed rules," and it is not enough to reuse a generic HDMI line-width rule set. The official HDMI 2.1b overview states that total link capability rises to **48Gbps**, and TI's TMDS1204 datasheet gives the actual HDMI 2.1 FRL lane-rate levels as **3/6/8/10/12Gbps**. In practice, that means the first questions are:

1. **Is the current link really HDMI 2.0 TMDS, or has it entered HDMI 2.1 FRL territory?**
2. **Do board length and connector placement force layer changes or long stubs?**
3. **Is ordinary FR-4 still enough, or is a lower-loss material system needed?**
4. **Can the reference plane stay continuous through the full launch and routing path?**
5. **Can the fabricator repeatedly build the target 100 ohm differential geometry?**

If the project is already entering pre-layout review, it is usually safer to bring [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) stackup direction and the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) into the discussion early instead of routing first and reverse-engineering the material choice later.

<a id="rules"></a>
## Summary table of key rules and parameters

| Rule / parameter | Recommended range or judgment method | Why it matters | How to verify | What happens if ignored |
|---|---|---|---|---|
| HDMI version and rate | Confirm whether the link is TMDS up to 6Gbps or FRL up to 12Gbps/lane | Speed directly defines the loss budget and material window | Specification, chip datasheet, protocol settings | Wrong stackup choice leads to tight eye and EMI margin later |
| Differential impedance | Control HDMI pairs around a 100 ohm differential target | Basic transmission-structure requirement | Impedance calculation, coupon, TDR | More reflection and reduced eye opening |
| Reference plane | Keep the pair adjacent to a continuous reference plane along the full path | Return continuity affects SI and EMI | Layout review, layer-change check | More mode conversion and radiation risk |
| Material and copper | Judge material family from length, rate, and copper roughness together | Both loss and fabrication variation rise at higher speed | Stackup review, microsection, insertion-loss test | Prototypes work, but production margin shrinks |
| Connector / via transition | Launch, anti-pad, stub, and layer changes need separate review | Transitions usually fail before straight traces do | 3D transition modeling, TDR, measured waveform | Black screen, image noise, intermittent instability |
| Manufacturing consistency | Design values must map to real factory geometry | Lamination and etch shift the actual dimensions | Microsection, coupon, lot comparison | Link margin drifts from lot to lot |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 and HDMI 2.1 should not share one vague stackup strategy. Confirm the lane rate first, then decide material, layers, and length budget.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100 Ohm Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100 ohm is not just a software target value. It has to remain stable after lamination, etching, and copper-surface effects are added together in real manufacturing.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">On HDMI boards, the first place that often loses margin is not the long straight route, but transitions such as connectors, layer changes, and stubs.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">A mature HDMI stackup is proven by coupons, microsections, and TDR or insertion-loss data showing that the built geometry still resembles the model.</div>
    </div>
  </div>
</div>

<a id="loss-budget"></a>
## Why should HDMI stackup start with a loss budget based on rate and length?

Conclusion: **Because the right material family and stackup are determined by actual lane rate, route length, and transition count, not by what boards of this interface "usually" use.**

The official context is clear enough. HDMI 2.1b raises total link capability to **48Gbps**. TI's TMDS1204 datasheet lists FRL lane rates up to **12Gbps**. For HDMI 2.0, TI's TDP158 public material states support for HDMI 2.0b and TMDS data rates up to **6Gbps**. In stackup decisions, the real questions are therefore:

- **How long is the on-board path?**
- **How many connectors, ESD devices, re-drivers, and layer changes are inserted?**
- **Does ordinary FR-4 still leave enough margin at the current lane rate?**
- **Has the design already reached a region where lower-loss copper and tighter dielectric control are needed?**

If the route is short and transitions are few, standard or mid-loss material systems may still be sufficient. But if the HDMI path is longer, connector placement is poor, and vias and protection devices are added, the more reliable move is usually to converge the [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) stackup first and only then freeze the routing.

<a id="impedance"></a>
## Why must 100 ohm differential impedance be tied to real fabrication?

Conclusion: **Because 100 ohm differential impedance in HDMI is not an abstract target. It is the physical result of lamination thickness, etch compensation, and real copper geometry.**

Multiple TI HDMI documents state 100 ohm differential as an explicit requirement. TI layout guidance directly states "**TRACE IMPEDANCE: 100 OHM DIFFERENTIAL IMPEDANCE**," and processor documentation also calls for TMDS differential traces at **100 ohm +/-10% differential impedance**. The basic design rule is therefore clear. The actual challenge is whether production still holds it.

Common production-side error sources include:

- Laminated dielectric thickness not matching the nominal model exactly
- Etched line width differing from the drawn geometry because of compensation
- Copper roughness changing both loss and effective impedance
- Solder mask, reference-plane shape, and nearby copper moving the real structure away from the simulation model

A safer stackup flow usually is:

1. Back-calculate geometry using the target material family and real factory parameters  
2. Use a field solver or the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) for early geometry evaluation  
3. Confirm actual coupons, TDR, and microsections during prototype stage  
4. Feed the factory compensation values back into the final stackup definition

Without that loop, the common outcome is "100 ohm in simulation, close to target on the board, but with too little real margin."

<a id="transitions"></a>
## Why are connectors, layer changes, and stubs more dangerous than straight traces?

Conclusion: **Because straight HDMI routing is often controllable, while launches, vias, and layer changes introduce local impedance steps, mode conversion, and extra loss much more easily.**

TI's TPD12S016 HDMI protection layout note gives concrete routing rules: TMDS differential pairs should be routed at **100 ohm differential impedance**, pair skew should stay within a small window, and spacing between pairs should remain adequate. The real value of those rules is not only cleaner straight routing. It is the reminder that transition structures are usually the most fragile region.

For HDMI stackups, the areas that most deserve separate review are:

- Whether a continuous reference plane still exists under the connector launch
- Whether via pad and anti-pad geometry were optimized around the target launch structure
- Whether ground vias help the return current close at layer changes
- Whether through-hole stubs need shortening or back-drilling
- Whether the pair remains symmetric after breakout

If the board also carries denser breakouts or modular connector regions, it is often worth reviewing those launch problems together with the breakout capability of [HDI PCB](https://hilpcb.com/en/products/hdi-pcb), rather than treating HDMI as just another video port.

<a id="validation"></a>
## How should HDMI stackups be validated before production?

Conclusion: **Useful HDMI validation does not prove that the drawing contains a 100 ohm pair. It proves that the fabricated board still preserves the target.**

A more practical validation path usually includes:

| Validation item | What it mainly answers | Recommended observation points |
|---|---|---|
| Impedance coupon | Can the factory repeatedly build the target geometry? | 100 ohm target and lot-to-lot spread |
| Microsection | Did lamination and etching shift the structure? | Dielectric thickness, line width, copper profile |
| TDR or insertion-loss test | Are the transitions and the full path electrically healthy? | Local discontinuities, difference between straight and transition regions |
| Multi-board comparison | Is the process window wide enough? | Consistency of eye, impedance, and loss across boards |
| System-level test | Does the stackup still work with real connectors and devices? | Resolution, refresh rate, black-screen threshold, image artifacts, EMI behavior |

If the project is about to move into prototypes or a validation lot, bringing stackup, coupons, launch review, and test items directly into the [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) stage is usually the highest-value move. Many HDMI issues cannot be fully hidden later by simply tuning equalization.

<a id="next-steps"></a>
## Next steps with HILPCB

If you are now moving an HDMI board toward stackup definition, the better next step is to convert interface requirements into manufacturable inputs:

- Converge target material, copper foil, and stackup direction first through [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- Use the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) early to back-calculate the geometry range for 100 ohm differential routing.
- If the board also includes connector breakout, layer changes, and denser local fan-out, review the practical windows of [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) or [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) at the same time.
- Once stackup, coupon planning, and launch review have converged, write them directly into [Quote / RFQ](https://hilpcb.com/en/quote/) or the [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) notes.

<a id="faq"></a>
## Frequently Asked Questions (FAQ)

<!-- faq:start -->

### Does every HDMI 2.1 board require premium low-loss materials?

Not necessarily. The decision depends on actual lane rate, on-board length, and transition count. If the path is short and the structure is compact, standard or mid-loss systems may be enough. If the route is longer, the transitions are worse, and the speed is higher, the material window tightens quickly.

### Is drawing the pair at 100 ohm enough for HDMI?

No. One hundred ohms is only the target. The real result also depends on laminated thickness, etch compensation, copper roughness, solder mask, and reference-plane continuity.

### Do HDMI differential pairs still need a continuous reference plane?

Yes. Differential routing does not eliminate the need for a stable return path. When launches, layer changes, or plane splits interrupt the return current, both mode conversion and EMI risk increase.

### Do HDMI problems happen more often in the trace itself or in the connector transition?

Very often in the connector launch, layer-change via, or stub. Straight segments are usually easier to control, while transition structures more easily create local impedance steps and mode conversion.

### Why are coupons or TDR checks necessary for HDMI stackups?

Because they show whether the manufactured geometry still resembles the model. Without coupons, microsections, or TDR, "100 ohm differential" often remains only a design number rather than a hardware result.

<!-- faq:end -->

<a id="references"></a>
## Public references

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   Supports the official context cited here for HDMI 2.1b capability up to 48Gbps and higher-resolution / higher-refresh operation.

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   Supports the public data used here on HDMI 2.1 FRL lane rates of 3/6/8/10/12Gbps and related sink redriver context.

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   Supports the public context used here for HDMI 2.0b / 6Gbps TMDS links.

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   Supports the conclusions here around 100 ohm HDMI differential pairs, layout near connector protection devices, and the need to control transition structures carefully.

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   Supports the explanation that layer stack, controlled impedance, reference planes, vias, and routing guidelines need to be reviewed together.

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   Supports the official wording cited here that TMDS differential traces should meet 100 ohm +/-10% differential impedance.

<a id="author"></a>
## Author and review information

- Author: HILPCB high-speed interface and stackup content team
- Technical review: PCB process, SI, and high-speed connector engineering team
- Last updated: 2025-11-18
