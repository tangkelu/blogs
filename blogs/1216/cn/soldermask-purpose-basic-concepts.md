---
title: "Soldermask Purpose: Top 20 PCB Basics FAQs"
description: "Answers to the 20 most common questions about soldermask purpose, providing definitions, examples, metrics, and prevention checklists, along with learning paths, document checklists, and HILPCB assistance."
category: technology
date: "2025-12-16"
featured: true
image: ""
readingTime: 9
tags: ["soldermask purpose", "pcb terminology glossary", "gerber file basics", "double layer pcb tutorial", "trace width calculator intro", "pcb design checklist beginner"]
---
Understanding the **soldermask purpose** is fundamental to PCB design and manufacturing. It is not merely the "green paint" that makes a circuit board look finished; it is a critical functional layer that ensures assembly reliability, prevents short circuits, and protects the copper circuitry from environmental factors. Whether you are designing a simple **double layer PCB** or a complex HDI board, mastering soldermask constraints is essential.

This comprehensive FAQ guide covers the 20 most critical questions regarding soldermask, ranging from basic definitions to complex manufacturing scenarios. We also provide actionable checklists and risk assessments to help you deliver perfect production files to **HILPCB**.

---

### FAQ Index: Quick Navigation

The following table summarizes the key topics covered in this guide. Use this to quickly locate the specific **PCB terminology glossary** items or metrics you need.

| FAQ # | Topic | Key Metric / Concept | Recommended Action |
| :--- | :--- | :--- | :--- |
| 1 | **Definition** | Insulation & Protection | Define clearly in CAD. |
| 2 | **Material** | Epoxy / LPI | Choose based on application. |
| 3 | **Color** | Green vs. Others | Green offers best inspection contrast. |
| 4 | **Clearance** | 2-4 mil (0.05-0.1mm) | Check global expansion rules. |
| 5 | **Solder Dam** | Min 4 mil (0.1mm) | Critical for SMT assembly. |
| 6 | **Bridging** | Short Circuits | Increase dam width. |
| 7 | **Tented Vias** | Covered vs. Open | Specify in fabrication notes. |
| 8 | **Plugged Vias** | Type VI / VII | Use for BGA designs. |
| 9 | **SMD vs NSMD** | Pad Definition | NSMD is preferred for generic SMT. |
| 10 | **Thickness** | 10-25 microns | Verify for impedance control. |
| 11 | **High Voltage** | Dielectric Strength | Check CTI values. |
| 12 | **Coverlay** | Flex PCB Insulation | Use Polyimide for Flex. |
| 13 | **Peelable Mask** | Temporary Protection | Use for selective wave soldering. |
| 14 | **Gerber Files** | GTS / GBS layers | Inspect using a **Gerber viewer**. |
| 15 | **SMOBC** | Bare Copper | Standard industry process. |
| 16 | **Undercut** | Etching Defects | Monitor trace width/mask alignment. |
| 17 | **Fiducials** | Optical Alignment | Ensure large mask opening. |
| 18 | **Test Points** | Probe Access | Do not tent test points. |
| 19 | **Heat Dissipation** | Thermal impact | Mask can slightly insulate heat. |
| 20 | **Repair** | UV Curable Pen | Fix scratches post-assembly. |

---

### Part 1: The Fundamentals of Soldermask Purpose

#### 1. What is the primary purpose of soldermask on a PCB?
**Scenario:** A beginner designer asks why the copper isn't just left exposed, or why the board needs to be covered in polymer.
**Metrics/Example:** Without soldermask, molten solder during the wave soldering or reflow process would flow onto traces, causing massive short circuits.
**Solution:** The soldermask acts as an electrical insulator and a mechanical barrier. Its primary purpose is to prevent solder bridges between closely spaced pads and traces.
**Prevention Checklist:**
*   [ ] Verify that the entire board is covered except for pads.
*   [ ] Ensure the mask layer is active in your CAD export settings.

#### 2. What materials are used for soldermask?
**Scenario:** A client requires a board for a high-temperature environment and asks if standard "green" mask is sufficient.
**Metrics/Example:** The most common type is Liquid Photoimageable (LPI) ink. It is epoxy-based.
**Solution:** LPI is cured using UV light. For specific applications, dry film soldermask is used (though less common now). Standard LPI is suitable for most FR4 boards.
**Prevention Checklist:**
*   [ ] Specify "LPI Soldermask" in fabrication notes.
*   [ ] For [High TG PCB](https://hilpcb.com/en/products/high-tg-pcb) applications, confirm the mask can withstand higher reflow profiles.

#### 3. Why is soldermask usually green?
**Scenario:** A designer wants a red board for aesthetic reasons but is warned about inspection difficulties.
**Metrics/Example:** Green has the highest contrast with copper and gold/HASL finishes, reducing eye strain for manual inspection.
**Solution:** While HILPCB offers Red, Blue, Black, White, and Yellow, Green is the standard because it cures the fastest and most reliably due to optimized chemical formulations.
**Prevention Checklist:**
*   [ ] Use Green for prototypes to ensure fastest turnaround.
*   [ ] Use White only for LED boards (high reflectivity).
*   [ ] Avoid Black for beginners (hardest to troubleshoot traces).

#### 4. What is Soldermask Clearance (Expansion)?
**Scenario:** The manufactured board has soldermask covering the edges of the copper pads, making soldering difficult.
**Metrics/Example:** Standard clearance is usually **2 to 4 mils (0.05mm - 0.1mm)** larger than the copper pad.
**Solution:** This expansion accounts for misalignment tolerances during manufacturing. If the mask opening is exactly the same size as the pad (1:1), a slight shift might cover the copper.
**Prevention Checklist:**
*   [ ] Set global design rules to 3 mil expansion.
*   [ ] Check for "Sliver" warnings in DRC (Design Rule Check).

#### 5. What happens if the Soldermask Clearance is too large?
**Scenario:** To be "safe," a designer sets a 10 mil expansion. During assembly, solder flows off the pad onto the bare laminate or adjacent traces.
**Metrics/Example:** Excessive exposure of the laminate can lead to solder bridges if traces run near the pads.
**Solution:** Keep expansion tight (approx 2-3 mils). This creates a "Solder Dam" between pads.
**Prevention Checklist:**
*   [ ] Verify that the mask opening does not expose adjacent copper traces.
*   [ ] Use a **Gerber viewer** to visually inspect openings.

#### 6. What is a Solder Dam and why is it critical?
**Scenario:** On a fine-pitch IC (like a QFP), pins are shorted together after wave soldering.
**Metrics/Example:** The "Solder Dam" is the bridge of soldermask material *between* two mask openings. The minimum reliable width is usually **4 mil (0.1mm)** for standard colors (Green) and **5-6 mil** for other colors.
**Solution:** If the gap between pads is too small to fit a 4 mil dam, the manufacturer might remove the dam entirely (gang opening), increasing bridging risk.
**Prevention Checklist:**
*   [ ] Check pitch of components.
*   [ ] If pitch is < 0.5mm, consult HILPCB DFM engineers.
*   [ ] Prioritize Green mask for fine pitch designs.

#### 7. What is the difference between Tented and Untented Vias?
**Scenario:** A designer sees exposed copper rings on vias where they didn't expect them, or conversely, wants to test a signal on a via but it's covered.
**Metrics/Example:**
*   **Tented:** The via is covered by soldermask (Mask opening = 0).
*   **Untented:** The via is exposed (Mask opening > Via size).
**Solution:** Tenting protects vias from oxidation and accidental shorts. Untenting allows for testing and rework.
**Prevention Checklist:**
*   [ ] Tent all vias under BGA components.
*   [ ] Untent vias intended for test points.
*   [ ] Review your CAD software's "Force Tenting" option.

#### 8. When should I use Plugged Vias (Via-in-Pad)?
**Scenario:** Designing a high-density board where vias must be placed directly inside component pads.
**Metrics/Example:** Simply tenting a via in a pad is dangerous; solder will wick down the hole, leaving the component leg with insufficient solder (starved joint).
**Solution:** Use **Via Plugging (IPC-4761 Type VII)**. The via is filled with epoxy and plated over. This is essential for [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) designs.
**Prevention Checklist:**
*   [ ] Clearly mark plugged vias in a separate drill file or layer.
*   [ ] Expect higher manufacturing costs for plugged vias.

#### 9. SMD vs. NSMD Pads: Which is better?
**Scenario:** A BGA component datasheet recommends "NSMD" pads, but the designer uses "SMD".
**Metrics/Example:**
*   **SMD (Solder Mask Defined):** The mask opening is smaller than the copper pad. The mask defines the solderable area. Good for pad anchoring.
*   **NSMD (Non-Solder Mask Defined):** The mask opening is larger than the copper pad. The copper defines the area. Good for solder joint reliability.
**Solution:** NSMD is generally preferred for BGAs as it allows solder to grip the sides of the copper pad.
**Prevention Checklist:**
*   [ ] Follow the component datasheet strictly.
*   [ ] For generic R/C components, NSMD is standard.

---

<!-- COMPONENT: BlogQuickQuoteInline -->

---

### Part 2: Advanced Soldermask Scenarios

#### 10. How does soldermask thickness affect Impedance?
**Scenario:** A high-speed USB line fails impedance testing. The calculator didn't account for the dielectric constant of the mask.
**Metrics/Example:** Soldermask is usually 10-25 microns thick over traces. It has a Dielectric Constant (Dk) of ~3.5 - 4.0.
**Solution:** Soldermask reduces the impedance of surface microstrips by 2-3 Ohms compared to bare copper.
**Prevention Checklist:**
*   [ ] Use an impedance calculator that includes a "Coating" or "Soldermask" field.
*   [ ] Consult HILPCB for exact stackup data before routing.

#### 11. Soldermask in High Voltage Applications
**Scenario:** A power supply board experiences arcing between traces despite having soldermask.
**Metrics/Example:** While soldermask is an insulator (500V+ per mil), it can contain micro-voids. It should not be the *primary* isolation for safety-critical high voltage.
**Solution:** Rely on physical spacing (Creepage/Clearance) rather than just soldermask. Refer to IPC-2221 standards.
**Prevention Checklist:**
*   [ ] Use slots (cut-outs) in the PCB for high voltage isolation.
*   [ ] Do not rely solely on mask for voltages > 50V if spacing is tight.

#### 12. Soldermask vs. Coverlay (for Flex PCBs)
**Scenario:** A designer submits a [Flex PCB](https://hilpcb.com/en/products/flex-pcb) design with standard LPI soldermask files. The mask cracks when the board is bent.
**Metrics/Example:** Standard LPI is brittle. Flex PCBs require **Coverlay** (Polyimide film with adhesive) or flexible LPI.
**Solution:** Specify "Coverlay" for the flexible sections of the board.
**Prevention Checklist:**
*   [ ] Ensure coverlay openings are larger (10 mil+) than standard mask openings due to alignment difficulty.
*   [ ] Use flexible LPI only for semi-static flex applications.

#### 13. What is Peelable Soldermask?
**Scenario:** A board requires both SMT assembly and Through-Hole assembly. The Through-Hole pads need to be protected during the initial reflow or wave soldering of other parts.
**Metrics/Example:** A thick layer of temporary blue/red mask is applied over specific holes.
**Solution:** This mask is manually peeled off after the assembly process to expose clean copper for the final connector soldering.
**Prevention Checklist:**
*   [ ] Define peelable mask on a separate Gerber layer.
*   [ ] Ensure the peelable area is large enough to grip and pull.

#### 14. How do I check Soldermask in Gerber Files?
**Scenario:** The board arrives with mask covering the connector fingers. The designer only checked the CAD view, not the Gerbers.
**Metrics/Example:** Look for files with extensions like `.GTS` (Top Solder) and `.GBS` (Bottom Solder).
**Solution:** Use a [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer). Remember: In mask layers, **shapes represent openings** (absence of mask).
**Prevention Checklist:**
*   [ ] Verify that Gold Fingers have a mask opening.
*   [ ] Verify that fiducials are not covered.

#### 15. What is SMOBC (Solder Mask Over Bare Copper)?
**Scenario:** An old specification calls for "SMOBC".
**Metrics/Example:** This is the industry standard. It means the mask is applied over the copper *before* the surface finish (HASL/ENIG) is applied to the exposed pads.
**Solution:** This prevents solder from flowing under the mask and causing it to peel (flaking) during reflow.
**Prevention Checklist:**
*   [ ] No action needed; this is the standard process at HILPCB.

#### 16. Soldermask Undercut and Adhesion Issues
**Scenario:** The soldermask is peeling off in narrow slivers between traces.
**Metrics/Example:** If the copper trace is very thick (e.g., [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb)), the mask may not fully encapsulate the vertical sidewalls of the trace.
**Solution:** Ensure sufficient spacing between thick copper traces to allow the mask to flow and adhere to the laminate substrate.
**Prevention Checklist:**
*   [ ] For 2oz+ copper, increase spacing between traces to >8 mil.

#### 17. Fiducials and Soldermask
**Scenario:** The Pick and Place machine cannot locate the board alignment marks.
**Metrics/Example:** Fiducials are copper circles used for optical alignment.
**Solution:** The soldermask opening around a fiducial must be large enough to provide a high-contrast "quiet zone." Usually, the opening is twice the diameter of the copper dot.
**Prevention Checklist:**
*   [ ] Ensure a 1mm opening for a 0.5mm fiducial.
*   [ ] Do not route traces through the fiducial's mask opening.

#### 18. Test Points and Soldermask
**Scenario:** The ICT (In-Circuit Test) fixture cannot make contact with the board.
**Metrics/Example:** Test points were accidentally tented in the design.
**Solution:** Create a specific "Test Point" property in your CAD tool that automatically forces a mask opening.
**Prevention Checklist:**
*   [ ] Generate a test point report.
*   [ ] Visually verify openings on the Bottom Solder layer (GBS).

#### 19. Thermal Impact of Soldermask
**Scenario:** A high-power LED board is overheating.
**Metrics/Example:** Soldermask is a polymer and acts as a slight thermal insulator.
**Solution:** For extreme heat dissipation, some designers leave the copper planes exposed (and tinned) or use a very thin white mask (high reflectivity).
**Prevention Checklist:**
*   [ ] Consider [Metal Core PCB](https://hilpcb.com/en/products/metal-core-pcb) for better thermals.
*   [ ] Remove mask from large thermal pads to allow heatsink attachment.

#### 20. Can Soldermask be repaired?
**Scenario:** During manual assembly, a technician scratches the mask, exposing a trace.
**Metrics/Example:** Exposed copper can corrode or short.
**Solution:** Use a UV-curable soldermask repair pen. Apply the liquid, expose it to UV light (or sunlight) to cure.
**Prevention Checklist:**
*   [ ] Handle boards by edges.
*   [ ] Keep a repair pen in the rework station.

---

### Part 3: Essential Checklists & Resources

<div style="background-color: #f8d7da; border-left: 5px solid #721c24; padding: 15px; margin-bottom: 20px;">
<strong>Type 4: Risk Warning - The "Sliver" Danger</strong><br>
One of the most common manufacturing defects related to soldermask is the "Sliver." This occurs when the gap between two mask openings is too small (e.g., < 3 mil). During manufacturing, this tiny strip of mask may not adhere to the board. It can flake off during assembly and land on a pad, preventing the component from soldering correctly. <strong>Always ensure your minimum solder dam is at least 4 mil (0.1mm).</strong>
</div>

<div style="background-color: #d1ecf1; border-left: 5px solid #0c5460; padding: 15px; margin-bottom: 20px;">
<strong>Type 5: Learning Value - Gerber Inspection</strong><br>
Never trust your CAD view 100%. The CAD view is an interpretation; the Gerber file is the instruction. Learning to read the "Negative" nature of mask layers (where drawn shapes = holes) is a vital skill. Use the <a href="https://hilpcb.com/en/tools/gerber-viewer">HILPCB Gerber Viewer</a> to verify your files before ordering.
</div>

<div style="background-color: #d4edda; border-left: 5px solid #155724; padding: 15px; margin-bottom: 20px;">
<strong>Type 6: Manufacturing Collaboration</strong><br>
If you are designing a board with tight constraints (e.g., 0.4mm pitch BGAs), standard design rules may not apply. HILPCB offers <strong>DFM (Design for Manufacturing)</strong> checks. We can advise if your soldermask dams need to be adjusted or if you should switch to plugged vias to ensure high yield during <a href="https://hilpcb.com/en/products/smt-assembly">SMT Assembly</a>.
</div>

#### Data Delivery Checklist: What to Send to HILPCB

Before submitting your order, run through this checklist to ensure your soldermask data is interpreted correctly.

| Item | Focus Area | Responsibility | Status |
| :--- | :--- | :--- | :--- |
| **GTS File** | Top Soldermask Layer present? | Designer | [ ] |
| **GBS File** | Bottom Soldermask Layer present? | Designer | [ ] |
| **Clearance** | Is expansion set to 2-4 mil globally? | Designer | [ ] |
| **Solder Dams** | Are dams between IC pins > 4 mil? | Designer | [ ] |
| **Tenting** | Are vias tented/untented as intended? | Designer | [ ] |
| **Fiducials** | Do fiducials have mask openings? | Designer | [ ] |
| **Color** | Is the mask color specified in notes? | Designer | [ ] |
| **Finish** | Matte vs. Glossy specified? | Designer | [ ] |
| **Via Plugging** | Are plugged vias identified (if any)? | Designer | [ ] |
| **Peelable** | Is peelable mask layer separate? | Designer | [ ] |
| **Gold Fingers** | Is mask removed from gold fingers? | Designer | [ ] |
| **Antenna** | Is mask removed from RF antenna (if req)?| Designer | [ ] |
| **Text** | Is silkscreen clipped from mask openings? | Designer | [ ] |
| **NPTH** | Is mask removed from mounting holes? | Designer | [ ] |
| **BGA** | Are BGA pads NSMD (usually)? | Designer | [ ] |
| **QFN** | Is the center thermal pad segmented? | Designer | [ ] |
| **Version** | Do file names match the revision? | Designer | [ ] |
| **Format** | RS-274X (Extended Gerber)? | Designer | [ ] |
| **Netlist** | IPC-356 included for verification? | Designer | [ ] |
| **Readme** | Special instructions text file included? | Designer | [ ] |
| **Stackup** | Impedance requirements noted? | Designer | [ ] |
| **Material** | Tg rating specified? | Designer | [ ] |
| **Quantity** | Prototype vs Production volume? | Procurement | [ ] |
| **Lead Time** | Standard vs Expedited? | Procurement | [ ] |
| **DFM Check** | Has HILPCB performed DFM? | Manufacturer | [ ] |

### Conclusion

The **soldermask purpose** extends far beyond aesthetics. It is the guardian of your circuit's integrity, preventing bridges during [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) and protecting the copper from the environment. By understanding the nuances of clearance, dams, and via handling, you can design boards that are not only functional but also manufacturable at scale.

From simple [Single/Double Layer PCBs](https://hilpcb.com/en/products/single-double-layer-pcb) to complex [Rigid-Flex PCBs](https://hilpcb.com/en/products/rigid-flex-pcb), HILPCB is your partner in navigating these technical details. Our engineering team is ready to review your stackup and soldermask constraints to ensure a flawless production run.

<!-- COMPONENT: BlogQuickQuoteInline -->