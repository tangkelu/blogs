---
title: "How to Route PCB Differential Pairs: Practical Rules for Impedance, Reference Planes, Skew, and Via Structures"
description: "A direct answer to the target impedance, reference-plane continuity, symmetry, length compensation, via stubs, and production validation that should be reviewed first in PCB differential pair routing, helping USB, PCIe, LVDS, Ethernet, and display interfaces preserve signal integrity in real stackups."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# How to Route PCB Differential Pairs: Practical Rules for Impedance, Reference Planes, Skew, and Via Structures

- **The first thing to lock in for differential-pair routing is not whether the two traces are exactly the same length, but which standard or datasheet target the pair is supposed to meet.** Different interfaces do not share one universal target. NXP's PTN3222 eUSB2 guidance calls for **85 ohm differential impedance**, while NXP AN13335 for automotive Ethernet clearly routes the MDI as **100 ohm** edge-coupled microstrip or stripline.
- **Symmetry matters more than simply keeping the traces close together.** Intel AN528 states that an ideal differential pair requires both lines to look electrically the same; otherwise differential-to-common-mode conversion appears. In other words, the core of a good pair is not cosmetic neatness but structural symmetry.
- **Reference-plane continuity and layer-transition treatment often damage the link faster than the straight segment itself.** NXP AN13462 explicitly says high-speed differential traces should not cross plane splits and should stay on one layer with as few vias as possible, while Intel's via discontinuity guidance stresses enough nearby, symmetric GND vias for return current during layer changes.
- **Serpentine compensation, anti-pads, and via stubs cannot be copied from a template.** Intel's P/N de-skew guidance shows that trombone compensation can create impedance ripple and mode conversion. That means length tuning should stay close to the mismatch point and must account for coupling changes.
- **Whether a differential pair is manufacturable depends on stackup, tolerance, breakout, and validation being defined together.** Intel's 82566 checklist and NXP's high-speed layout notes repeat the same principle: target impedance, same-layer routing, via count, symmetry, and return-path treatment must be delivered to the factory as one package, not as a single note saying "100 ohm differential."

> **Quick Answer**  
> The core of PCB differential-pair routing is keeping the two traces in a symmetric propagation environment across the real stackup, real copper thickness, and real transition structures. First freeze the interface target impedance and skew budget, then control same-layer routing, continuous reference planes, symmetric vias, and disciplined length compensation, and finally verify the manufactured result with coupons, TDR, or system testing.

## Table of Contents

- [What should engineers review first in PCB differential-pair routing?](#overview)
- [Summary table of key rules and parameters](#rules)
- [Why must differential pairs be defined from the standard and stackup first?](#standards-stackup)
- [Why are symmetry, skew, and serpentine tuning so often misused?](#symmetry-skew)
- [Why are reference planes, layer transitions, and via stubs high-risk areas?](#planes-vias)
- [How should differential-pair routing be validated before production?](#validation)
- [Next steps with HILPCB](#next-steps)
- [Frequently Asked Questions (FAQ)](#faq)
- [Public references](#references)
- [Author and review information](#author)

<a id="overview"></a>
## What should engineers review first in PCB differential-pair routing?

Start with **the interface impedance target, stackup, reference plane, symmetry, and layer-transition strategy**.

This question does not mean "just keep two traces parallel," and it does not mean "finish routing first and let the fabricator calculate impedance later." Different protocols, PHYs, and connectors do not share the same differential-pair rules. NXP AN13462 gives eUSB2 a layout target of **85 ohm differential impedance** and requires high-speed pairs not to cross plane splits. NXP AN13335 routes automotive Ethernet MDI as **100 ohm** differential and limits intra-pair matching between the connector and choke to **1 mm**. Intel's 82566 checklist adds another context by calling for gigabit Ethernet MDI at **100 ohm differential impedance (plus or minus 20%)** with pair mismatch kept within **50 mil**.

That means the first things to confirm are:

1. **Whether the interface target is 85 ohm, 90 ohm, 95 ohm, or 100 ohm differential**
2. **Where the allowed intra-pair skew budget comes from**
3. **Whether the routing layer is microstrip or stripline, and whether the reference plane stays continuous**
4. **Whether layer changes are allowed, and how return current and stubs will be handled**
5. **Whether the board shop can hold the required geometry on the intended stackup**

If the board includes several high-speed interfaces, it is usually better to converge the stackup direction for [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), the layer allocation for [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb), and the geometry window in the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) before layout starts rather than rewriting rules after DRC passes.

<a id="rules"></a>
## Summary table of key rules and parameters

| Rule / Parameter | Recommended range or judgment method | Why it matters | How to verify | What happens if ignored |
|---|---|---|---|---|
| Target impedance | Confirm it from the interface standard or chip documentation first, not from a default value | Differential pairs are not all 100 ohm | Standard, datasheet, stackup review | Width and spacing start wrong |
| Symmetry | Keep cross-section, reference environment, and transitions as consistent as possible | Intel AN528 shows asymmetry drives mode conversion | Layout review, 3D transition review | More common-mode noise and worse eye quality |
| Same-layer routing | Keep the full high-speed pair on one layer whenever possible | Layer changes add discontinuities | Post-route review, via count | More skew, reflection, and debug difficulty |
| Reference plane | Keep the full path continuous, close, and preferably under one reference | Plane splits break return current | Plane review, layer review | Worse EMI and mode conversion |
| Length compensation | Tune only to the interface budget and keep it near the mismatch point | Bad serpentine patterns create impedance ripple | Skew review, TDR, simulation | "Length matching" creates new problems |
| Via / stub | Minimize vias; if a layer change is required, use symmetric signal vias plus GND vias | Via discontinuity is a common high-speed risk | TDR, cross-section, backdrill review | Local reflection, ISI, return detours |

| Interface example | Typical requirement from public sources | Design reminder |
|---|---|---|
| eUSB2 | NXP AN13462: 85 ohm, same-layer symmetry, pair mismatch under 20 mil, no plane split | Even low-voltage high-speed links cannot use vague default rules |
| Automotive Ethernet MDI | NXP AN13335: 100 ohm, 1 mm intra-pair match from connector to choke, symmetric ground vias | Reference treatment and common-mode noise control matter as much as impedance |
| Gigabit Ethernet MDI | Intel 82566 checklist: 100 ohm ±20%, pair mismatch under 50 mil, GND vias within 40 mil near transitions | Production-oriented boards care about process details |
| FPGA true differential I/O | Intel Agilex guide: 100 ohm, consider backdrill where needed to reduce stub impact | The faster the link, the more via structures become a first-order design object |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef6f2 100%); border: 1px solid #d5e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365c7c; font-weight: 700;">Protocol Before Geometry</div>
      <div style="margin-top: 8px; color: #233546;">A differential pair is not automatically 100 ohm. Confirm the interface target and skew budget before defining width, spacing, and layer assignment.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7b72; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a6159; font-weight: 700;">Symmetry Beats Cosmetics</div>
      <div style="margin-top: 8px; color: #223630;">A working pair is not just "close together." The two lines must stay symmetric in cross-section, reference condition, and transitions.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #886847; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Return Path Is Part of the Pair</div>
      <div style="margin-top: 8px; color: #3a2f25;">Differential traces do not operate independently from the reference plane. Plane splits, cutouts, and asymmetric stitching turn return-path issues into SI and EMI problems.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5f7d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c4960; font-weight: 700;">De-skew Needs Discipline</div>
      <div style="margin-top: 8px; color: #392733;">Length tuning is not automatically beneficial. Poor serpentine placement, coupling changes, and anti-pad treatment can turn compensation into a fresh discontinuity.</div>
    </div>
  </div>
</div>

<a id="standards-stackup"></a>
## Why must differential pairs be defined from the standard and stackup first?

Conclusion: **Because the target impedance and geometry of a differential pair are not a universal template. They are the combined result of interface requirements and the production stackup.**

The public guidance from NXP and Intel is already clear. NXP AN13462 gives eUSB2 a target of **85 ohm**. NXP AN13335 explicitly requires **100 ohm** edge-coupled microstrip or stripline for automotive Ethernet MDI. Intel's true differential I/O guidance also uses a **100 ohm** target and recommends backdrill where needed to reduce stub influence. The normal order of work is therefore:

1. **Freeze the impedance target from the interface standard, chip manual, or reference design**
2. **Choose microstrip or stripline based on connector, loss, and EMI needs**
3. **Confirm actual material, dielectric thickness, copper thickness, and process compensation with the fabricator**
4. **Then write the resulting width, spacing, and tolerance back into layout rules**

Intel's 82566 checklist also reminds engineers that two 50 ohm single-ended traces do not automatically equal one 100 ohm differential pair. The answer depends on the real stackup and field solution. In engineering practice, the value of this step is that it turns theory into manufacturable geometry. If the interface stack is already under review, it is usually better to close the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) loop together with [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) stackup review before routing starts.

<a id="symmetry-skew"></a>
## Why are symmetry, skew, and serpentine tuning so often misused?

Conclusion: **Because many teams treat equal length as proof that the pair is correct while ignoring structural symmetry and local coupling changes.**

Intel AN528 gives two central conditions for an ideal differential pair: both lines should look electrically identical, and the skew between them should approach zero. The same material also states that asymmetry causes impedance discontinuity and differential-to-common-mode conversion. That means:

- **Symmetry is not only line length, but also cross-section, dielectric, nearby copper, and transitions**
- **Skew is not an isolated number; it is tied to changes in the reference environment**
- **If serpentine compensation is placed badly, the tuned segment can have worse impedance than the main route**

Intel's P/N de-skew guidance goes further and shows that trombone compensation can create two separate problems: loosely coupled regions that disturb impedance, and different delay per unit length from the straight segment, which then creates mode conversion. NXP AN13462 gives the practical layout rule more directly: if tuning is necessary, place it as close as possible to the location where the mismatch occurred, not as a remote pile of dense meanders.

The safer approach is usually:

- Remove asymmetry caused by component placement and breakout first
- Compensate only the skew that truly matters within the pair budget
- Keep tuning sections gentle and loosely coupled instead of packing dense serpentine for a report-friendly "perfect match"
- For long FR-4 channels sensitive to fiber weave, apply Intel AN528 style mitigation such as diagonal routing or other weave-risk reduction methods

If the board includes both BGA breakout and high-speed edge connectors, it is often worth reviewing [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) fanout capability together with [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) layer-transition strategy so that late length compensation does not create extra discontinuities.

<a id="planes-vias"></a>
## Why are reference planes, layer transitions, and via stubs high-risk areas?

Conclusion: **Because once a differential pair crosses layers, crosses a split, or leaves a stub, the first failure point is usually return current and local discontinuity rather than the main route itself.**

NXP AN13462 explicitly says high-speed differential traces should not cross plane splits and recommends routing the pair on the same layer with minimal vias and no unnecessary stubs. NXP AN13335 also stresses that ground connections next to the MDI pair must stay symmetric, otherwise rise-time skew becomes common-mode noise. Intel's via discontinuity guidance makes the manufacturing side even clearer:

- If the signal stops on an inner layer, the leftover via barrel behaves like a capacitive stub
- A layer change requires enough nearby GND vias for return current
- The via structures on both lines of the pair must stay symmetric, otherwise a differential-mode discontinuity appears

Intel's 82566 checklist makes the action still more explicit: when a differential pair changes layers, GND vias should stay within **40 mil** of the signal vias. If the route changes from a ground-referenced layer to a power-referenced layer, a nearby decoupling capacitor may be needed to bridge return current.

That means the highest-risk zones for a high-speed differential pair are usually:

1. **The BGA breakout root**
2. **Connector launches**
3. **Areas around AC-coupling capacitors and common-mode parts**
4. **Layer-transition vias and anti-pad zones**
5. **Untreated through-via stubs in thicker boards**

If the design is moving to higher data rate or greater board thickness, it is usually better to bring backdrill, blind or buried vias, or tighter transition design into the [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) review early rather than waiting for a weak first-board eye diagram.

<a id="validation"></a>
## How should differential-pair routing be validated before production?

Conclusion: **Useful validation does not prove only that "paired routing was completed" in CAD. It proves that the manufactured geometry and system behavior still hold after fabrication.**

A more practical validation path usually includes:

| Validation item | Main question answered | Recommended observation point |
|---|---|---|
| Stackup / impedance review | Does the target geometry fit the factory's manufacturable capability? | Width, spacing, copper thickness, dielectric thickness, tolerance |
| Coupon / TDR | Is the real impedance and transition behavior close to the design target? | Impedance plateau, local discontinuities, via influence |
| Cross-section check | Did lamination and etching shift the structure? | Actual trace width, copper thickness, dielectric thickness, anti-pad geometry |
| System link test | Is the pair healthy with real devices and connectors? | Eye diagram, link training, BER, EMI |
| Multi-board comparison | Is the risk from the design or from build variation? | Board-to-board spread, lot consistency, rework difficulty |

The shared message across Intel 82566, NXP AN13462, and NXP AN13335 is obvious: target impedance, pair mismatch, plane continuity, symmetric ground vias, stub treatment, and test-point strategy must all be written clearly before release to the factory rather than held only in the layout engineer's head.

If the project is close to prototyping, the safer move is usually to push stackup, the controlled-impedance table, key pair layers, via or backdrill requirements, and the validation method into [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) or [Quote / RFQ](https://hilpcb.com/en/quote/) input instead of sending Gerber alone.

<a id="next-steps"></a>
## Next steps with HILPCB

If you are moving forward with a high-speed differential-pair board, the next step is usually to convert routing rules into manufacturable inputs:

- Use the [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) and [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) paths first to close the stackup, layer assignment, and reference-plane strategy.
- Use the [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) before layout to back-calculate width and spacing for different interfaces instead of rewriting DRC after routing.
- If breakout density is high and layer changes are frequent, check the fanout and via-structure window of [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) in parallel.
- Once stackup, the controlled-impedance table, the key differential pairs, and the validation method are defined, package them directly into [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) or [Quote / RFQ](https://hilpcb.com/en/quote/) for a cleaner review.

<a id="faq"></a>
## Frequently Asked Questions (FAQ)

<!-- faq:start -->

### Are differential pairs always designed as 100 ohm by default?

No. Different interfaces use different targets. For example, NXP's eUSB2 guidance uses 85 ohm, while automotive Ethernet MDI and many general high-speed I/O interfaces commonly use 100 ohm. Check the standard or chip documentation first rather than applying one default value.

### Is it enough if the two traces are the same length?

No. Intel AN528 clearly states that an ideal differential pair must also stay electrically symmetric. If layer assignment, reference plane, nearby copper, vias, or anti-pad treatment differ, mode conversion can still appear even with equal length.

### Must differential pairs never change layers?

Not necessarily, but layer changes should be minimized. Every layer transition should be designed as one structure including signal vias, GND vias, anti-pads, and the return-current path. The faster the interface and the thicker the board, the more visible via discontinuity becomes.

### Is it better to put all serpentine compensation in one place later in the route?

Usually no. Public guidance from NXP and Intel suggests that length compensation should stay near the location where the mismatch occurred and should avoid turning the tuning section itself into a new impedance discontinuity. Dense serpentine added only to satisfy a length report is often counterproductive.

### Why do differential pairs still care about reference-plane splits? Don't they return through themselves?

They still care. Differential pairs do not work independently from the reference plane. Plane splits, ground openings, asymmetric ground vias, or switching to a power reference all change the return path and can increase common-mode noise and radiation.

<!-- faq:end -->

<a id="references"></a>
## Public references

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   Supports the article's explanation that ideal differential pairs should maintain electrical symmetry and near-zero skew, and that fiber weave can affect consistency in long high-speed channels.

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   Supports the engineering conclusion that trombone-style tuning can create impedance ripple and mode-conversion risk.

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   Supports the discussion of via stubs, symmetric signal-via configuration, and adding GND vias to manage return current during layer changes.

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   Supports the production-oriented checklist items on 100 ohm differential impedance, intra-pair mismatch, GND-via distance near layer transitions, and avoiding unused pads or stubs.

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   Supports the interface-level guidance for eUSB2: 85 ohm target, same-layer symmetry, length matching, avoiding plane splits, reducing vias, and avoiding stubs.

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   Supports the explanation of 100 ohm MDI routing, ground symmetry, connector-to-choke length matching, same-layer routing, and common-mode-noise risk.

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   Supports the context for 100 ohm true differential I/O and the recommendation to consider backdrill where needed to reduce stub effects.

<a id="author"></a>
## Author and review information

- Author: HILPCB high-speed interconnect and SI content team
- Technical review: PCB process, signal-integrity, and connector engineering team
- Last updated: 2025-11-18
