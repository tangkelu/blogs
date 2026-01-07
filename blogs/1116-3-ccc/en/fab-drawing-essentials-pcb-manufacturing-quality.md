---
title: "Fab drawing essentials: 20 common manufacturing and testing questions"
description: "A curated list of 20 common fab drawing essentials issues across manufacturing/assembly/testing—covering symptoms, root causes, and fixes—plus a defect countermeasure matrix and quality audit checklist."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["fab drawing essentials", "smt stencil design tutorial", "soldermask exposure tutorial", "stackup documentation guide", "surface finish selection tips", "yield improvement roadmap"]
---
## Introduction: why Fab Drawing is the foundation of PCB production

In a complex PCB manufacturing ecosystem, **Fab Drawing** is the only “legal document” and the single source of truth for technical communication. A detailed and accurate Fab Drawing is the starting point for high yield and high reliability—and the core of any **yield improvement roadmap**. Conversely, any omission, ambiguity, or error in the drawing can trigger a cascade across fabrication, assembly, and test, leading to cost overruns, schedule slips, or even field failures.

Centered on **fab drawing essentials**, this article systematically summarizes 20 common issues across the end-to-end flow—from fabrication to quality assurance. For each issue we cover symptoms, measurable metrics, root causes, and practical corrective and preventive actions, helping you build a Fab Drawing that leaves no room for doubt.

---

## Part 1: Manufacturing FAQ

Manufacturing issues are often rooted in physical and chemical processes, and many can be traced back to how Fab Drawing defines materials, stack-up, and tolerances.

### 1. Issue: why does the PCB show severe warpage after reflow?

-   **Symptoms**: The board bends or twists after heating, making placement difficult; BGA joints may open or short.
-   **Metrics**: Warpage > 0.75% (IPC-A-610 Class 2/3). Formula: (max deformation / PCB diagonal length) × 100%.
-   **Root causes**:
    1.  **Asymmetric stack-up**: Copper distribution in the Fab Drawing stackup is unbalanced, creating CTE mismatch.
    2.  **Wrong material selection**: No high Tg material is specified, or materials with different CTE are mixed.
    3.  **Large copper areas**: Large copper pours are present but not cross-hatched/meshed, increasing internal stress.
-   **Fix**: Bake and press-flatten finished boards, but this is only a limited rework measure.
-   **Prevention**:
    -   In the **stackup documentation guide**, explicitly require a symmetric, copper-balanced stack-up.
    -   Specify all Core and PP types, thicknesses, and suppliers.
    -   Require copper areas > 500 mm² to be cross-hatched/meshed and document the rule in notes.

### 2. Issue: insufficient PTH copper thickness or voids in holes?

-   **Symptoms**: Poor via continuity, high resistance, opens after thermal shock or vibration.
-   **Metrics**: Per IPC-6012 Class 2, average hole copper thickness < 20 μm; Class 3 typically requires ≥ 25 μm. Void count > 1 or void length > 5% of hole diameter.
-   **Root causes**:
    1.  **Ambiguous drawing requirement**: Fab Drawing does not specify hole copper class (IPC Class 2/3) or numeric targets.
    2.  **High Aspect Ratio design**: Aspect Ratio > 10:1 makes plating difficult, but the drawing provides no special process requirement.
    3.  **Poor drilling quality**: Rough hole wall or smear/residue reduces copper deposition quality.
-   **Fix**: Micro-section analysis for the lot. If it fails requirements, the lot is typically scrap.
-   **Prevention**:
    -   In the Drill Table and notes, explicitly specify: “Hole copper thickness shall meet IPC-6012 Class 3; average thickness ≥ 25 μm.”
    -   For Aspect Ratio > 10:1 holes, require enhanced processes such as pulse plating.

### 3. Issue: solder mask bridge peeling or insufficient precision?

-   **Symptoms**: Solder mask dams between fine-pitch pads (e.g., QFP, BGA) peel off, causing solder bridging shorts.
-   **Metrics**: Solder Mask Dam width < 75 μm (3 mil), or physical peeling during SMT/reflow.
-   **Root causes**:
    1.  **Incorrect solder mask opening definition**: Solder Mask Opening in Fab Drawing is oversized relative to pads (often recommended +2–3 mil per side).
    2.  **Mask type not specified**: High-precision LDI mask ink/process is not specified, so conventional exposure cannot meet fine-pitch needs.
-   **Fix**: Manual mask repair (high cost/low reliability), or reduce solder paste via stencil adjustments.
-   **Prevention**:
    -   Define solder mask opening rules clearly in Fab Drawing, or provide accurate solder mask Gerber.
    -   Per **soldermask exposure tutorial**, specify in notes: “For pitch ≤ 0.4 mm components, solder mask must be made using LDI.”

### 4. Issue: insufficient cleanliness and ionic residue on the board?

-   **Symptoms**: Under high temperature/humidity, leakage, electrochemical migration (ECM), or dendritic growth appears, causing failures.
-   **Metrics**: Ion Chromatography result > 0.65 μg/cm² (NaCl equivalent), failing IPC-J-STD-001.
-   **Root causes**: Fab Drawing does not require a cleanliness class; the factory cleans only per baseline process without targeted reinforcement (e.g., under BGA).
-   **Fix**: Plasma cleaning or ultrasonic cleaning on finished boards.
-   **Prevention**: Specify in Fab Drawing: “Finished boards shall meet IPC-J-STD-001 Class 3 cleanliness and provide ionic contamination test report.”

### 5. Issue: uneven/oxidized surface finish plating thickness?

-   **Symptoms**: Poor solderability and low joint strength; gold fingers show poor contact. ENIG may show “Black Pad”.
-   **Metrics**: ENIG Au thickness < 1.27 μm (0.05 mil) or Ni thickness < 2.54 μm (0.1 mil). OSP film breaks down after multiple reflow cycles.
-   **Root causes**:
    1.  **Standard not specified**: Fab Drawing only says “ENIG” but does not specify a thickness/standard (e.g., IPC-4552).
    2.  **Wrong process choice**: Per **surface finish selection tips**, an unsuitable surface finish is selected for high-frequency or fine-pitch use (e.g., HASL).
-   **Fix**: Not recoverable; usually scrap.
-   **Prevention**:
    -   Specify surface finish type and standard, e.g.: “Surface finish: ENIG per IPC-4552A, Au 0.05–0.1 μm, Ni 3–6 μm.”
    -   For critical areas such as gold fingers, specify thicker plating (hard gold) separately.

### 6. Issue: Back Drilling depth is off and via stubs are too long?

-   **Symptoms**: Poor SI for high-speed channels, with severe reflections and insertion loss.
-   **Metrics**: Post-backdrill stub length > 10 mil, exceeding typical high-speed tolerance.
-   **Root causes**: Backdrill definition in Fab Drawing is unclear.
    1.  **Depth not defined**: Not specified whether drilling starts from top or bottom, and which layer to stop at.
    2.  **Stub tolerance is vague**: No maximum allowable stub length is given.
-   **Fix**: Not recoverable for already-built boards.
-   **Prevention**:
    -   Provide a dedicated backdrill layer and backdrill table in Fab Drawing.
    -   Clearly call out each backdrill hole’s “start layer”, “stop layer”, and “max stub” requirement (e.g., Max Stub = 8 mil).

<div class="custom-block-type-6">
    <h4>HILPCB capability showcase</h4>
    <p>HILPCB is equipped with advanced LDI exposure, pulse plating lines, and depth-controlled drilling equipment, enabling precise execution of stringent Fab Drawing requirements. From high-Aspect-Ratio holes up to 20:1 to backdrill depth control within ±5 mil, our automated manufacturing flow ensures every PCB aligns tightly with your design intent and protects product performance.</p>
</div>

---

## Part 2: Assembly FAQ

Assembly defects are closely related to pad design, solder mask opening, and stencil design—items that should be standardized at the Fab Drawing stage.

### 7. Issue: lots of solder balls after SMT?

-   **Symptoms**: Tiny solder balls scattered around chip components (capacitors/resistors), potentially causing shorts.
-   **Metrics**: In a 6.5 cm² area, more than 5 solder balls with diameter > 0.13 mm (IPC-A-610).
-   **Root causes**:
    1.  **Oversized solder mask opening**: Paste flows onto solder mask during heating and forms solder balls.
    2.  **Improper stencil apertures**: Violates **smt stencil design tutorial** best practices; aperture size/shape is not suitable.
    3.  **Moisture in laminate**: Fab Drawing does not specify packaging and storage requirements.
-   **Fix**: Manually remove solder balls and clean the board.
-   **Prevention**:
    -   Specify NSMD or SMD pad rules and define solder mask opening tolerances precisely in Fab Drawing.
    -   Require vacuum packaging meeting MSL needs from the PCB supplier.

### 8. Issue: tombstoning on chip components?

-   **Symptoms**: One end of small components like 0402/0201 lifts up, standing like a “tombstone”.
-   **Metrics**: One end completely detaches from the pad.
-   **Root causes**:
    1.  **Asymmetric pad design**: The two pads defined in Fab Drawing differ in size, or connected copper areas differ greatly, causing unbalanced surface tension during reflow.
    2.  **Solder mask contamination on pads**: Insufficient mask precision partially covers pads.
-   **Fix**: Rework the assembled components.
-   **Prevention**:
    -   Reference an internal pad library or IPC-7351 footprint standards in Fab Drawing.
    -   Explicitly require zero solder mask residue on pads and define the minimum mask-to-pad clearance.

### 9. Issue: excessive voids after BGA/QFN soldering?

-   **Symptoms**: X-Ray shows many voids in BGA balls or under QFN thermal pads, degrading thermal performance and long-term reliability.
-   **Metrics**: For a single joint, void area exceeds 25% of total area (IPC-7095B).
-   **Root causes**:
    1.  **Improper Via-in-Pad handling**: VIP is used, but Fab Drawing does not specify filling and capping, so outgassing forms voids.
    2.  **Stencil aperture design**: Large thermal pads are not apertured with window/grid patterns, limiting outgassing.
-   **Fix**: Not practically repairable; requires component replacement at high cost.
-   **Prevention**:
    -   Specify in Fab Drawing: “All Via-in-Pad must be filled with conductive/non-conductive resin and plated capped; surface flatness < 1 mil.”
    -   In assembly notes, refer to **smt stencil design tutorial** and recommend windowpane or dot-matrix stencil apertures for QFN thermal pads.

### 10. Issue: Head-in-Pillow (HIP) on BGA?

-   **Symptoms**: BGA balls appear to touch pads but do not fully coalesce, forming a weak “pillow” joint that fails easily under stress.
-   **Metrics**: 3D X-Ray or cross-section shows clear separation at the ball/paste interface.
-   **Root causes**:
    1.  **PCB warpage**: see Issue 1; warpage creates a gap between BGA center area and the PCB surface.
    2.  **Uneven surface finish on pads**: ENIG Ni corrosion or OSP oxidation reduces solderability.
-   **Fix**: Reballing or replacement.
-   **Prevention**:
    -   Strictly follow Fab Drawing requirements on stack-up symmetry and material selection to control warpage at the source.
    -   Specify reliable surface finish standards and require outgoing solderability test reports from the supplier.

<div class="custom-block-type-4">
    <h4>Risk warning: an unclear Fab Drawing is a “time bomb”</h4>
    <p>A seemingly small omission—such as not defining the Via-in-Pad filling process—can cause an entire lot of BGA soldering to fail, resulting in losses of tens of thousands of dollars. Investing time to perfect <strong>fab drawing essentials</strong> during design is the most effective way to avoid massive downstream risk.</p>
</div>

### 11. Issue: teardrop-shaped joints or spikes after Selective Soldering?

-   **Symptoms**: After Selective Soldering for THT parts, joints are not full, appear teardrop-like or have sharp spikes, failing IPC-A-610.
-   **Metrics**: Wetting angle does not form > 270°, or obvious solder spikes exist.
-   **Root causes**:
    1.  **Poor thermal design**: Through holes connect directly to large ground planes, wicking heat too quickly and starving solder temperature.
    2.  **Solder mask opening too small**: Restricts solder flow and wetting.
-   **Fix**: Manual touch-up, but appearance and consistency are poor.
-   **Prevention**:
    -   Require Thermal Relief Pad design for THT holes connected to large copper areas at the Fab Drawing stage.
    -   Ensure mask openings are larger than the THT pad, providing enough room for solder flow.

<div class="cta-container">
    <p>Is your Fab Drawing complete enough? HILPCB offers free DFM/DFA analysis. Our engineers review your design files from fabrication, assembly, and test perspectives to identify and eliminate risks before release. <strong>Upload your Gerber now to get a professional assessment report!</strong></p>
</div>

---

## Part 3: Testing FAQ

Testing issues are often the final manifestation of manufacturing and assembly problems—but some can be avoided directly by improving Fab Drawing.

### 12. Issue: poor ICT probe contact and high false-fail rate?

-   **Symptoms**: ICT reports many false opens; manual retest shows they are actually good, hurting throughput.
-   **Metrics**: ICT false-fail rate > 5%.
-   **Root causes**:
    1.  **Non-standard test point design**: Fab Drawing does not define minimum Test Pad size/spacing/shape; pads are too small, too close to components, or too close to the edge.
    2.  **Test point surface finish**: With OSP, repeated probing can pierce the film, causing later contact issues.
-   **Fix**: Clean probes, adjust fixture, slow test speed.
-   **Prevention**:
    -   Create a dedicated test-point layer in Fab Drawing and note: “All ICT test points: min dia ≥ 0.8 mm, pitch ≥ 1.27 mm; surface must be flat and free of solder mask.”
    -   For dense test designs, specify gold or tin plating on test pads for durability.

### 13. Issue: FCT scripts cannot cover all functions?

-   **Symptoms**: Product passes FCT, but functional failures still appear at the customer; certain modules were never effectively tested.
-   **Metrics**: Test coverage < 95%.
-   **Root causes**: Fab Drawing lacks necessary test-assist information (e.g., jumpers/interfaces to enable test modes).
-   **Fix**: Update scripts and fixtures; recall or field-upgrade shipped units.
-   **Prevention**:
    -   In the Assembly Drawing, clearly label all debug/test interfaces, jumpers, and switch functions.
    -   Attach a “test instruction” describing how to enter different test modes.

### 14. Issue: unclear criteria for reliability tests (e.g., thermal shock)?

-   **Symptoms**: After 500 thermal cycles (-40°C to 125°C), teams disagree on pass/fail for micro-cracks or resistance drift.
-   **Metrics**: No clear Accept/Reject Criteria.
-   **Root causes**: Fab Drawing does not reference reliability standards or define pass/fail thresholds.
-   **Fix**: Quality/design/customer negotiate temporary criteria.
-   **Prevention**:
    -   In notes, define test conditions and acceptance criteria, e.g.: “Must pass 1000 cycles -40°C to 125°C; after test, via resistance change < 10%.”
    -   Reference industry standards directly, e.g., “All reliability requirements shall meet IPC-TM-650.”

### 15. Issue: false trips or breakdown in Hipot testing?

-   **Symptoms**: During dielectric withstand testing, equipment alarms for leakage current, but the circuit is not actually broken down.
-   **Metrics**: Leakage > 10 mA (typical), or arcing occurs below the specified voltage.
-   **Root causes**:
    1.  **Insufficient creepage/clearance**: Clearance and Creepage between HV and LV nets are not emphasized in Fab Drawing and rely only on default Gerber geometry.
    2.  **Material selection**: CTI grade is not selected based on operating voltage.
-   **Fix**: Analyze alarm points to determine true breakdown vs. surface arcing from moisture/contamination.
-   **Prevention**:
    -   Clearly mark HV regions in Fab Drawing and define minimum Clearance/Creepage (e.g., “>3 mm for 500V AC”).
    -   Specify CTI grade in the material list (e.g., CTI ≥ 400V).

---

## Part 4: Quality FAQ

Quality issues reflect systemic gaps. As the starting point of all work, Fab Drawing completeness directly determines the robustness of the quality system.

### 16. Issue: SPC alarms trigger frequently?

-   **Symptoms**: For drilling, line width, impedance and other key steps, SPC charts show frequent points beyond UCL/LCL.
-   **Metrics**: Cpk < 1.33.
-   **Root causes**:
    1.  **Unreasonable tolerances**: Fab Drawing tolerances are too tight relative to natural process capability.
    2.  **CTQ not identified**: The drawing does not identify which features are critical to quality (CTQ), so the factory does not prioritize monitoring.
-   **Fix**: Analyze out-of-control points to determine special vs. common causes, and take actions accordingly.
-   **Prevention**:
    -   Align with the PCB supplier and their **yield improvement roadmap** to set realistic, manufacturable tolerances in Fab Drawing.
    -   Use symbols (e.g., `[CTQ]`) to mark all CTQ dimensions/features such as impedance trace width and BGA pad diameter.

### 17. Issue: after a customer complaint, the 8D report cannot be closed effectively?

-   **Symptoms**: Quality teams cannot locate root cause quickly; the 8D report stalls at D4 (root cause analysis) and corrective actions cannot be defined.
-   **Metrics**: 8D closure cycle > 30 days.
-   **Root causes**: Fab Drawing is incomplete, blocking traceability. Example: material model is not specified; when delamination occurs, it is unclear whether it’s material or process.
-   **Fix**: Perform extensive DPA such as cross-sections and SEM/EDX to reverse-infer causes.
-   **Prevention**:
    -   Fab Drawing must include a complete material list, stack-up, surface finish standards, and all special process requirements.
    -   HILPCB’s automation maps your Fab Drawing parameters to manufacturing data (e.g., lamination temperature profile, plating current). When issues occur, our 8D data system can quickly correlate design requirements and actual process parameters to pinpoint root cause.

<div class="custom-block-type-5">
    <h4>HILPCB value: data-driven quality assurance</h4>
    <p>We are more than a manufacturer. HILPCB digitizes your Fab Drawing and deeply integrates it with our MES system. From incoming materials to final shipment, every key parameter is recorded and monitored. When you need traceability, we provide a complete 8D data package spanning design specs and real production data—making root cause analysis far more efficient.</p>
</div>

### 18. Issue: quality problems occur, but the traceability chain has gaps?

-   **Symptoms**: A defective batch is found, but it’s impossible to precisely identify all affected boards or trace back to specific shifts or raw material lots.
-   **Metrics**: Unable to provide a full bidirectional traceability report from finished goods to raw materials within 24 hours.
-   **Root causes**: Fab Drawing does not clearly require traceability markings.
    1.  **No unique serial number**: No requirement to print a unique QR code or serial number on each PCB.
    2.  **Inconsistent marking format**: Date Code, UL mark, and part number position/format are not defined.
-   **Fix**: Expand recall scope, wasting significant cost.
-   **Prevention**:
    -   Specify silkscreen must include: part number, revision, UL mark, lead-free symbol, production week code (WW/YY).
    -   For high-reliability products, require a unique QR code at a defined location and specify encoding rules for scan-based traceability.

### 19. Issue: poor consistency between PCBs from different suppliers?

-   **Symptoms**: The same Gerber and Fab Drawing sent to two suppliers yields boards with clear differences in color, impedance, and mechanical properties.
-   **Metrics**: Key electrical parameters (e.g., TDR impedance) differ by > 10% between lots.
-   **Root causes**: Fab Drawing leaves “room for interpretation”. Example: it says only “FR-4” without specifying S1141 vs IT-180A; it requires “green solder mask” without a specific color code.
-   **Fix**: Add supplementary testing and screening across lots.
-   **Prevention**:
    -   In the material list, specify “manufacturer + model” wherever possible, or provide an Approved Vendor List (AVL).
    -   Provide Pantone Color Code for solder mask and silkscreen inks.
    -   For all performance requirements (impedance, Dk/Df, etc.), provide numeric targets and tolerances—not vague descriptions.

### 20. Issue: final product certification (e.g., UL, CE) fails?

-   **Symptoms**: Certification labs reject the product due to PCB flame rating, creepage/clearance, or materials not meeting requirements.
-   **Metrics**: Certification failure requiring redesign and resubmission.
-   **Root causes**: Fab Drawing does not include all compliance-related requirements.
-   **Fix**: Modify design, rebuild samples, and retest—significantly delaying schedule.
-   **Prevention**:
    -   On the first page of Fab Drawing, clearly call out applicable certifications, e.g., “UL 94V-0”, “RoHS Compliant”.
    -   Ensure specified laminates, solder mask inks, etc. comply with UL yellow card requirements.
    -   Confirm the PCB supplier is qualified for the required certifications and require UL mark and factory code on the board.

---

## Additional content

### Defect countermeasure matrix

The table below summarizes common defects, related process steps, key metrics, and corrective/preventive actions—a practical tool for fast troubleshooting.

| Defect | Related process step | Key metric | Corrective/Preventive action |
| :--- | :--- | :--- | :--- |
| **Warpage** | Stack-up, lamination | Warpage < 0.75% | **Prevention**: enforce symmetric stack-up and copper balance in Fab Drawing. |
| **PTH Void** | Plating | Average hole copper thickness > 25 μm (Class 3) | **Prevention**: specify IPC class clearly and add special process requirements for high Aspect Ratio holes. |
| **Solder mask dam peeling** | Solder mask, exposure | Min dam width > 75 μm | **Prevention**: specify LDI and define mask opening rules precisely. |
| **BGA voids** | SMT, reflow | Void ratio < 25% | **Prevention**: require Via-in-Pad resin fill and plated capping. |
| **ICT contact issues** | Test | Test pad dia > 0.8 mm | **Prevention**: include a dedicated test-point layer and design rules in Fab Drawing. |
| **Traceability break** | Silkscreen, laser marking | Unique serial readability | **Prevention**: require a unique QR code at a defined location and specify format. |
| **Impedance out of spec** | Etching, lamination | Impedance tolerance ±10% | **Prevention**: provide detailed stack-up parameters (Dk, Df, thickness) and impedance model. |
| **Black Pad** | ENIG | Ni phosphorus content 7–9% | **Prevention**: require ENIG per IPC-4552A and request XRF report. |

### Fab Drawing quality audit checklist

Before sending your design package to the manufacturer, use the checklist below to self-audit and ensure all **fab drawing essentials** are covered.

| # | Audit item | Status (Y/N) | Notes |
| :-- | :--- | :--- | :--- |
| 1 | Clear part number and revision included? | | |
| 2 | Board outline dimensions and tolerances defined? | | |
| 3 | Detailed stack-up drawing provided? | | Includes per-layer thickness, material model, copper weight |
| 4 | All laminate manufacturers and models specified? | | Or an AVL is provided |
| 5 | Final board thickness and tolerance defined? | | |
| 6 | Complete Drill Table provided? | | Hole sizes, tolerances, hole types (PTH/NPTH) |
| 7 | Hole copper thickness requirement defined (IPC class)? | | |
| 8 | Special holes (blind/buried/backdrill) clearly documented? | | |
| 9 | Minimum trace/space defined? | | |
| 10 | Solder mask color/type/thickness specified? | | e.g., LPI, green, matte |
| 11 | Solder mask opening rules defined? | | |
| 12 | Silkscreen color and minimum text height specified? | | |
| 13 | Surface finish type and standard defined? | | e.g., ENIG per IPC-4552A |
| 14 | Any impedance control requirement? | | If yes, impedance values/tolerances/test method provided? |
| 15 | All CTQ dimensions/features marked? | | |
| 16 | Warpage requirement defined? | | |
| 17 | All required safety/environment markings included? | | UL, RoHS, CE, etc. |
| 18 | Traceability markings defined (date code, serial)? | | |
| 19 | Via-in-Pad filling and capping requirements defined? | | |
| 20 | Extra requirements for special areas (e.g., gold fingers)? | | e.g., beveling, thicker gold |
| 21 | Electrical test requirements defined (flying probe/fixture)? | | 100% E-Test |
| 22 | ICT test-point design rules provided? | | |
| 23 | Cleanliness/ionic contamination requirements specified? | | |
| 24 | Packaging/shipping/storage requirements specified? | | e.g., MSL level |
| 25 | All notes clear, unambiguous, and not outdated? | | |

---

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

A great Fab Drawing is far more than an add-on to Gerber files. It is the precise expression of design intent, the clear definition of manufacturing constraints, and a strong guarantee of quality. By systematically addressing the 20 common issues above and embedding **fab drawing essentials** best practices into your workflow, you can significantly improve yield and reliability while building an efficient, transparent relationship with your supply chain. This is the foundation of a successful **yield improvement roadmap**.

<div class="cta-container">
    <p>Ready to take your PCB design to the next level? HILPCB’s expert team is ready to help. We don’t just provide top-tier manufacturing—we aim to be your design-stage partner, ensuring your Fab Drawing is robust from day one. <strong>Contact us now and start your high-reliability PCB journey!</strong></p>
</div>

> For manufacturing and assembly support, contact HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) or [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) for DFM/DFT guidance.
