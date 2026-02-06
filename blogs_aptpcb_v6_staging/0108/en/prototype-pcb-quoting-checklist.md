---
title: "Prototype PCB Quoting Checklist: Practical Rules, Specs, and Troubleshooting Guide"
description: "A practical guide to prototype pcb quoting checklist: clear rules, recommended design parameters, manufacturing verification steps, and common failure fixes."
category: technology
date: "2026-01-08"
featured: true
image: "/assets/img/blogs/2025/04/quick-turn-pcb-prototype.webp"
readingTime: 9
tags: ["prototype pcb quoting checklist"]
---

# Prototype PCB Quoting Checklist: Practical Rules, Specs, and Troubleshooting Guide


![prototype pcb quoting checklist: Practical Rules, Specs, and Troubleshooting Guide](/assets/img/blogs/2025/04/quick-turn-pcb-prototype.webp)

### Contents

- [Highlights](#highlights)
- [Prototype PCB Quoting Checklist: Definition and Scope](#prototype-pcb-quoting-checklist-definition-and-scope)
- [Prototype PCB Quoting Checklist Rules and Specifications](#prototype-pcb-quoting-checklist-rules-and-specifications)
- [Prototype PCB Quoting Checklist Implementation Steps](#prototype-pcb-quoting-checklist-implementation-steps)
- [Prototype PCB Quoting Checklist Troubleshooting](#prototype-pcb-quoting-checklist-troubleshooting)
- [6 Essential Rules for Prototype PCB Quoting Checklist (Cheat Sheet)](#6-essential-rules-for-prototype-pcb-quoting-checklist-cheat-sheet)
- [FAQ](#faq)
- [Request a Quote / DFM Review for Prototype PCB Quoting Checklist](#request-a-quote--dfm-review-for-prototype-pcb-quoting-checklist)
- [Conclusion](#conclusion)


A **prototype PCB quoting checklist** is the critical bridge between your CAD design and the manufacturing floor. It is a systematic validation set used by engineers and procurement teams to ensure all design files (Gerbers, BOMs, Drill files) and fabrication specifications (Stackup, Material, Finish) are complete, accurate, and manufacturable before submitting them to a factory. A robust checklist prevents the dreaded "Engineering Query" (EQ) hold, ensures accurate pricing, and guarantees that the boards delivered match your design intent.

## Quick Answer
To get an accurate quote and rapid fabrication start, your submission package must be complete. Here are the essential checkpoints:

*   **File Format Rule**: Always submit **Gerber RS-274X** or **ODB++** files. Ensure all layers (copper, solder mask, silkscreen, drill, and board outline) are included.
*   **Drill File Pitfall**: A common error is missing the NC Drill file or failing to distinguish between plated (PTH) and non-plated (NPTH) holes.
*   **Material Specification**: Clearly define the material type (e.g., FR4 TG150) and board thickness (e.g., 1.6mm). "Standard" can be interpreted differently by different factories.
*   **Stackup Verification**: If impedance control is required, provide a specific stackup table or request the manufacturer's standard stackup for your layer count.
*   **Quantity & Lead Time**: Explicitly state the quantity (e.g., 5, 10, 50 pcs) and desired turnaround time (e.g., 24h, 3-day, standard).
*   **Surface Finish**: Specify the finish (HASL, ENIG, OSP) in the README or quote form, as this significantly affects cost and shelf life.
*   **Verification Method**: Before zipping your files, use a [Gerber Viewer](https://aptpcb.com/en/tools/gerber-viewer/) to visually confirm the board outline and layer alignment.




## Highlights
*   **Reduces EQ Delays**: A complete checklist eliminates back-and-forth emails, potentially saving 2-3 days of pre-production time.
*   **Cost Accuracy**: Specifying tolerances and materials upfront prevents surprise upcharges later in the process.
*   **Manufacturability**: Catching DFM issues (like trace width vs. copper weight) during the quoting phase ensures the design is viable.
*   **Sourcing Speed**: For turnkey orders, a formatted BOM with manufacturer part numbers (MPN) allows for instant component availability checks.

---

## Prototype PCB Quoting Checklist: Definition and Scope

The scope of a prototype PCB quoting checklist extends beyond just the file list. It encompasses the technical "handshake" between the designer and the CAM engineer. When you submit a quote, you are essentially defining the contract of manufacturing. If the data is ambiguous, the factory must guess or stop to ask—both of which introduce risk.

At APTPCB, we see thousands of quote requests. The ones that move to production fastest are those where the "Readme" file or quote form aligns perfectly with the Gerber data. Discrepancies (e.g., the Gerber says 1oz copper, but the note says 2oz) are the number one cause of delays.


![PCB Validation Documentation](/assets/img/pcb/common/pcb-validation-documentation.webp)


### Tech / Decision Matrix
The following matrix illustrates how specific decisions in your checklist impact the practical outcome of your quote and manufacturing process.

<div style="background-color:#F5F7FA;padding:18px;border-radius:10px;margin:20px 0;">
    <h3 style="margin:0 0 12px 0;color:#000000;">Tech / Decision Lever → Practical Impact</h3>
    <table style="width:100%;border-collapse:collapse;text-align:left;color:#000000;">
        <thead style="background-color:#D1E7D1; color:#000000;">
            <tr>
                <th style="padding:10px;border:1px solid #ccc;">Decision Lever / Spec</th>
                <th style="padding:10px;border:1px solid #ccc;">Practical Impact (Yield/Cost/Reliability)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding:10px;border:1px solid #ccc; font-weight:bold;">Material Selection (FR4 vs. Rogers)</td>
                <td style="padding:10px;border:1px solid #ccc;">High-frequency materials (Rogers) increase material cost by 3-10x but are essential for RF signal integrity. Standard FR4 is cost-effective for general logic.</td>
            </tr>
            <tr>
                <td style="padding:10px;border:1px solid #ccc; font-weight:bold;">Via Technology (HDI vs. Through-Hole)</td>
                <td style="padding:10px;border:1px solid #ccc;">Adding blind/buried vias increases lamination cycles, raising cost and lead time significantly. Through-hole is the standard baseline.</td>
            </tr>
            <tr>
                <td style="padding:10px;border:1px solid #ccc; font-weight:bold;">Surface Finish (HASL vs. ENIG)</td>
                <td style="padding:10px;border:1px solid #ccc;">ENIG provides a flat surface for fine-pitch BGAs but costs more. HASL is cheaper but uneven, unsuitable for fine-pitch components.</td>
            </tr>
            <tr>
                <td style="padding:10px;border:1px solid #ccc; font-weight:bold;">Turnaround Time (24h vs. Standard)</td>
                <td style="padding:10px;border:1px solid #ccc;">[Quick Turn services](https://aptpcb.com/en/pcb/quick-turn-pcb/) incur expediting fees (often +50-100%) but are crucial for tight R&D deadlines.</td>
            </tr>
        </tbody>
    </table>
</div>

---

## Prototype PCB Quoting Checklist Rules and Specifications

To ensure your quote is processed immediately, adhere to these specific rules. This table breaks down the critical data points required by CAM engineers.

| Rule | Recommended Value | Why it matters | How to verify |
| :--- | :--- | :--- | :--- |
| **File Format** | Gerber RS-274X or ODB++ | Industry standard; prevents scaling and aperture errors common in older formats. | Open files in a 3rd party viewer; check for "Undefined Apertures". |
| **Board Outline** | Mechanical Layer (GM1) | Defines the exact routing path. Without it, we cannot panelize or quote material usage. | Ensure the outline is a closed, continuous line (0 width or 10mil). |
| **Drill Chart** | Embedded or Separate File | Specifies hole sizes, tolerances, and plating status (PTH/NPTH). | Check that the drill count matches your CAD software report. |
| **Copper Weight** | 1oz (35µm) Outer / 0.5oz Inner | Affects trace width calculations for impedance and current capacity. | Specify in the "Readme" text file included in the zip. |
| **Solder Mask** | Green (Standard) | Non-standard colors (Matte Black, Purple) may add 1-2 days to lead time. | Confirm color choice in the quote form. |
| **Silkscreen** | White; Min text height 30mil | Legibility. Text smaller than 30mil (0.76mm) often becomes unreadable. | Visual check: Is text overlapping pads? |

For complex designs involving controlled impedance, it is highly recommended to consult our [PCB Stackup](https://aptpcb.com/en/pcb/pcb-stack-up/) guide to select a standard construction that meets your requirements without custom material ordering delays.

---

## Prototype PCB Quoting Checklist Implementation Steps

Implementing a rigorous checklist process is not just about checking boxes; it's about preparing a data package that flows seamlessly through the factory.

<div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 24px; padding: 40px 30px; margin: 30px 0; box-shadow: 0 15px 45px rgba(49, 27, 146, 0.1);">
    <h3 style="text-align: center; color: #311b92; margin: 0 0 10px 0;">Implementation Process</h3>
    <p style="text-align: center; color: #673ab7; margin-bottom: 40px;">Step-by-step execution guide for a perfect quote package</p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 18px;">
        <!-- CARD 01 -->
        <div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
            <strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">01. Data Export & Organization</strong>
            <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">Generate your Gerber files (RS-274X), NC Drill files, and IPC-356 Netlist. Organize them into a single folder. Include a "README.txt" detailing layer stackup, finish, and special requirements.</p>
        </div>
        <!-- CARD 02 -->
        <div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
            <strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">02. DFM Pre-Check</strong>
            <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">Run a Design for Manufacturing (DFM) check within your CAD tool or using our [DFM Guidelines](https://aptpcb.com/en/resources/dfm-guidelines/). Verify minimum trace/space (e.g., 4/4mil) and annular rings meet the manufacturer's capabilities.</p>
        </div>
         <!-- CARD 03 -->
        <div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
            <strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">03. Specification Definition</strong>
            <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">Clearly define non-Gerber specs: Quantity, Material (TG rating), Copper Weight, Surface Finish, and Color. If assembly is needed, ensure the BOM includes Manufacturer Part Numbers (MPN).</p>
        </div>
         <!-- CARD 04 -->
        <div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
            <strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">04. Submission & Review</strong>
            <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">Upload the ZIP file to the [Quote Portal](https://aptpcb.com/en/quote/). Monitor your email for the EQ (Engineering Query) report. Rapid response to EQs is the key to maintaining your lead time.</p>
        </div>
    </div>
</div>

---

## Prototype PCB Quoting Checklist Troubleshooting

Even with a checklist, issues can arise. Here are common failure modes during the quoting phase and how to fix them.

### 1. Missing Board Outline
**Symptom:** The manufacturer puts the quote on hold asking for dimensions.
**Fix:** Ensure the "Keep-Out" or "Mechanical 1" layer contains a continuous, closed polyline defining the board edge. Do not rely on the copper pour to define the edge.

### 2. Ambiguous Plating Specs
**Symptom:** The quote assumes all holes are plated, increasing cost, or non-plated holes are plated shut.
**Fix:** Provide separate drill files for PTH (Plated Through Hole) and NPTH (Non-Plated Through Hole), or ensure your drill chart explicitly labels them.

### 3. Impossible Tolerances
**Symptom:** The quote is rejected as "No Bid" or requires a custom quote.
**Fix:** Avoid specifying tolerances tighter than standard (e.g., +/- 3mil on routing) unless absolutely necessary. Standard routing tolerance is typically +/- 0.2mm (+/- 8mil).

### 4. Conflicting Information
**Symptom:** The Gerber file implies one thing (e.g., square pads for fiducials), but the Readme says another.
**Fix:** The Gerber data is the master. Ensure your notes match the physical design files. If you change the design, update the Readme.

---

## 6 Essential Rules for Prototype PCB Quoting Checklist (Cheat Sheet)

<div style="background-color:#F5F7F5; padding:20px; border-radius:8px; margin-top:20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<table style="width:100%; border-collapse:collapse; text-align:left; font-family:sans-serif; color:#333333;">
<thead style="background-color:#E0E8E0; color:#2E7D32;">
<tr>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Rule / Guideline</th>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Why It Matters (Physics/Cost)</th>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Target Value / Action</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Complete Layer Set</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Missing layers prevent CAM processing.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Include Outline & Drill</strong></td>
</tr>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Trace/Space Width</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Going below standard capabilities increases cost/risk.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>≥ 4mil / 0.1mm</strong></td>
</tr>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Min Mechanical Drill</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Smaller drills break easily; laser drilling is expensive.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>≥ 0.2mm (8mil)</strong></td>
</tr>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Annular Ring</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Ensures the drill hits the pad (registration tolerance).</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>≥ 4mil (0.1mm)</strong></td>
</tr>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Solder Mask Expansion</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Prevents mask from covering the pad.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>2-3mil (0.05-0.075mm)</strong></td>
</tr>
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Clear Material Spec</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Prevents using wrong Tg or dielectric constant.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Specify TG150 or TG170</strong></td>
</tr>
</tbody>
</table>
<div style="margin-top:10px; font-size:0.9em; color:#666; text-align:right;">
<em>Save this table for your design review checklist.</em>
</div>
</div>

## FAQ

**Q: What files are absolutely required for a PCB quote?**

A: At a minimum, we need Gerber files (RS-274X) for all copper layers, solder mask, silkscreen, and board outline, plus an NC Drill file. A "Readme" text file with specs (thickness, finish, copper weight) is highly recommended.

**Q: How does layer count affect the prototype price?**

A: Price increases with layer count due to the complexity of lamination and plating. A 4-layer board is typically 2x the cost of a 2-layer board. Jumping to 6 or 8 layers adds further cost, especially if blind/buried vias are used.

**Q: What is the standard lead time for prototypes?**

A: Standard lead time for 2-layer prototypes is often 2-3 days. For 4-6 layers, it is typically 4-5 days. [Quick turn options](https://aptpcb.com/en/pcb/quick-turn-pcb/) (24h or 48h) are available for an expedited fee.

**Q: Do I need to panelize my design before quoting?**

A: No. It is usually better to send the single unit design and let the manufacturer handle panelization (V-score or tab-route) based on their production panel sizes. Just specify "Panelize as X by Y" in your notes if you need it for assembly.

**Q: What is NRE cost?**

A: NRE (Non-Recurring Engineering) covers the setup costs (CAM tooling, E-test fixtures, stencils). For prototypes, this is a one-time fee. If you reorder the exact same revision, you typically do not pay NRE again. ---

## Request a Quote / DFM Review for Prototype PCB Quoting Checklist

<!-- COMPONENT: BlogQuickQuoteInline -->


Ready to move from design to fabrication? Ensure your data package is ready using the checklist above, then send it to our engineering team.

**Checklist for Submission:**
*   [ ] Zipped Gerber Files (RS-274X)
*   [ ] NC Drill File (Excellon)
*   [ ] Readme / Spec Sheet (Material, Finish, Thickness)
*   [ ] BOM (if Assembly is required)
*   [ ] Pick & Place File (if Assembly is required)

**[Submit Your Files for Instant Quote](https://aptpcb.com/en/quote/)**

## Conclusion

A well-structured **prototype pcb quoting checklist** is the secret weapon of efficient hardware teams. It transforms a chaotic submission process into a streamlined workflow, ensuring that the boards you receive are the boards you designed—delivered on time and within budget. By validating your files, clarifying your specs, and understanding the manufacturing levers, you eliminate the friction that typically slows down R&D.

Signed,
**The Engineering Team at APTPCB**
