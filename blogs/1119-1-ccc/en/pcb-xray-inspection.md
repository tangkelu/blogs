---
title: "What PCB X-Ray Inspection Should Really Look At: It Is Not Just About Capturing Void Images"
description: "A practical guide to the scope, defect interpretation, sampling logic, process feedback, and traceability chain that should be defined first for PCB X-Ray inspection."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# What PCB X-Ray Inspection Should Really Look At: It Is Not Just About Capturing Void Images

- **The first problem X-Ray inspection should solve is not whether a hidden defect image was captured, but whether hidden-joint quality can actually be closed back to the assembly process, sampling rules, and traceability chain.** The public titles of IPC-7095E and IPC-7093 both place design and assembly process guidance at the center, which already shows that X-Ray should not be treated as image judgment after the fact.
- **X-Ray should not be reduced to the single word "void."** On BGA, BTC, QFN, LGA, and large bottom-pad packages, wetting, bridging, offset, head-in-pillow, joint consistency, and void distribution are different risk dimensions.
- **The most useful X-Ray result is not finding one bad board. It is being able to trace the image back to stencil design, solder paste, pad geometry, reflow profile, and moisture exposure.** If the image does not feed back into process, quality improvement stays slow.
- **Sampling strategy has to be tied to package risk, lot change, and failure cost.** New packages, new stencils, new solder paste, or a new reflow window should not inherit the old sampling density by default.
- **X-Ray images without lot number, equipment, program, and judgment records attached are weak evidence for later root-cause work and customer complaints.**

> **Quick Answer**  
> The core of PCB X-Ray inspection is not producing a clear image. It is defining in advance which packages must be checked, which hidden-joint risks matter for each package, how image findings map back to process, and how the result enters the traceability chain. On BGA-, BTC-, and reliability-critical PCBA, X-Ray is a process-control tool, not only an acceptance step.

## Table of Contents

- [What should engineers review first in PCB X-Ray inspection?](#overview)
- [Key rules and parameter summary](#rules)
- [Which products and package types should put X-Ray into routine control?](#scope)
- [What defects and signals should X-Ray actually be looking for?](#defects)
- [Why is the biggest value of X-Ray process feedback rather than image capture?](#process)
- [Why must sampling strategy and traceability chain be designed together?](#sampling)
- [Next steps with HILPCB](#next-steps)
- [FAQ](#faq)
- [Public references](#references)
- [Author and review information](#author)

<a id="overview"></a>
## What should engineers review first in PCB X-Ray inspection?

Start with **package type, hidden-joint risk, defect interpretation logic, sampling strategy, and traceability method**.

This is not the same as asking whether the machine can produce an image, and it is not the same as asking whether the void ratio crossed a single threshold. IPC-7095E for BGA and IPC-7093 for Bottom Termination Components both put design and assembly process guidance into their public scope. IPC also stated in its J-STD-001J release note that added illustrations were included for bubbles seen in X-Ray images. Put together, those public facts already show that X-Ray is supposed to serve design, assembly, inspection, and reliability, not only one image-based accept / reject decision.

The items worth freezing before pilot usually include:

- **which packages and which lots must be part of routine X-Ray control**
- **what the key hidden-joint risks are for each package family**
- **whether interpretation is focused on voiding, wetting, bridging, offset, or consistency**
- **how sampling density changes with new packages, new process windows, and risk level**
- **how images, judgments, and process data enter the traceability chain**

For projects with many hidden joints, it usually makes sense to review the process windows of [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) and [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) at the same time, instead of letting inspection strategy and assembly strategy drift apart.

<a id="rules"></a>
## Key rules and parameter summary

| Rule / Parameter | Recommended approach | Why it matters | How to verify it | What happens if ignored |
| --- | --- | --- | --- | --- |
| Inspection scope | Define first which package types and failure-cost cases require X-Ray | High-risk joints should not wait for field failure before being checked | NPI review, package list, quality plan | Critical hidden-joint risk is missed |
| Interpretation focus | Different packages require different defect focus, not just voiding | BGA, BTC, and QFN do not fail in the same way | First-article image review, package classification | Images are captured but conclusions are weak |
| Process feedback | Make every image traceable to stencil, paste, pad, and reflow conditions | The value of inspection is process improvement | Link image records to process parameters | Problems are found but not improved |
| Sampling strategy | Adjust sampling dynamically by risk level, process change, and lot condition | Fixed-template sampling can hide new risk | First-article and production sampling plan | High-risk changes are missed |
| Traceability chain | Archive image, board ID, program, shift, and judgment together | Needed for failure analysis and complaint handling | MES / log review, lot binding | Root cause later becomes guesswork |
| Design coordination | Review pad design, via in pad, and bottom-pad opening early | Many X-Ray findings start with layout and package design | DFM review, package check | Assembly window proves too narrow after placement |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">Define first which packages and lot situations require routine X-Ray. Without scope, inspection becomes reactive.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">Different packages are sensitive to different hidden-joint defects. Voiding, bridging, offset, and head-in-pillow cannot share one interpretation template.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">If the image cannot be traced back to stencil, solder paste, pad design, and reflow, yield improvement stays slow.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">Without board ID, lot, program, and decision records, X-Ray images provide weak support for customer complaints and failure analysis.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Which products and package types should put X-Ray into routine control?

As a rule, **packages with hidden joints, high rework cost, bottom-pad thermal dependence, or high field-failure cost are the best candidates for routine X-Ray**.

IPC-7095E is written around BGA, and IPC-7093 is written around BTC / Bottom Termination Components. That alone already indicates these packages are not good candidates for release based only on AOI or visual inspection. The more practical engineering question is not "do we have an X-Ray machine?" but "if this package is soldered incorrectly, can we afford to find out only at functional test or in the field?"

Typical packages that deserve routine X-Ray include:

- **BGA, CSP, and other hidden-ball packages**
- **QFN, LGA, and large exposed-bottom-pad devices**
- **power devices where thermal path and joint consistency matter**
- **high-layer-count, fine-pitch, or dense PCBA with expensive rework**
- **automotive, medical, industrial-control, and communications boards with higher reliability demand**

If the project is already moving toward batch assembly, it is usually better to put those packages into the pre-control list for [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) or [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) rather than deciding after the first article "which ones should be inspected."

<a id="defects"></a>
## What defects and signals should X-Ray actually be looking for?

Because **the real purpose of X-Ray is not to ask "is there a void?" but to identify the hidden-joint failure modes that matter for that package**.

BTC and BGA do not carry the same risks, which is exactly why IPC treats them through different standards. For BGA, the more relevant checks are wetting, collapse, offset, bridging, and head-in-pillow-type risk. For BTC, QFN, and large bottom-pad devices, the focus is more often on bottom-joint distribution, void location, joint coverage, and consistency.

The most useful inspection observations usually include:

- **whether the joint has formed a reasonable continuous wetting shape**
- **whether hidden joints show bridging or localized abnormal clustering**
- **whether voids are concentrated in critical thermal or stress areas**
- **whether the same device and same lot show clear geometry spread**
- **whether a local anomaly points back to design, printing, or reflow behavior**

If the board also contains large thermal pads, complex power areas, or high heat density, it also helps to review the pad and heat-path structure against [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb) rather than treating X-Ray as a post-assembly-only action.

<a id="process"></a>
## Why is the biggest value of X-Ray process feedback rather than image capture?

Because **the important question is not that one bad board exists. It is why the same abnormality repeats**.

IPC-7093 and IPC-7095 are both design and assembly process guidance documents rather than image atlases. That means the image has to be read together with stencil aperture strategy, solder paste condition, pad design, via in pad treatment, moisture exposure of components, and reflow profile. Without that linkage, X-Ray can only say "there is a problem here" but not "why the same problem keeps coming back."

The process factors most worth tracing back are usually:

- **whether stencil thickness and aperture strategy fit the package**
- **whether solder paste type, lot, storage, and usage condition are stable**
- **whether pad design, solder-mask definition, and via in pad treatment are appropriate**
- **whether the reflow profile matches the device and board conditions**
- **whether package or PCB moisture exposure, warpage, or board-form change has been overlooked**

If the project is still in prototype or pilot, it is usually better to plan those feedback loops together with [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) rather than turning X-Ray into a stand-alone reject report.

<a id="sampling"></a>
## Why must sampling strategy and traceability chain be designed together?

Because **the control value of X-Ray depends on when you inspect, how much you inspect, and whether the result can be traced back into the process**.

The public J-STD-001J update context already shows that X-Ray image interpretation is being formalized more clearly inside assembly acceptance practice. In engineering terms, that means sampling strategy cannot remain a fixed template. It has to change with package risk, process maturity, process changes, and failure cost.

A more robust approach usually includes:

1. **Increase inspection density on first lots with new packages, new stencils, new paste, or new reflow programs.**
2. **Raise the priority level for fine-pitch BGA, large bottom pads, and critical thermal devices.**
3. **Bind sampling results to board ID, shift, program, solder-paste lot, and equipment settings.**
4. **Define escalation rules for higher sampling or 100% inspection when abnormal patterns repeat.**
5. **Archive image judgments together with corrective actions, not separately.**

Without a traceability chain, X-Ray images only support the immediate decision. With a traceability chain, they support complaint handling, failure analysis, and continuous process improvement. For projects close to production, it is usually better to write those expectations directly into [Quote / RFQ](https://hilpcb.com/en/quote/) or early quality instructions.

<a id="next-steps"></a>
## Next steps with HILPCB

If you are introducing BGA, QFN, large bottom-pad devices, or another project with many hidden joints, the next step is usually to turn "inspection" into "process control input":

- When the key issue is hidden-joint assembly quality, put the critical packages and control points into [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) review first.
- When PCB fabrication, sourcing, placement, and testing all need to be closed as one process, use [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) to align the workflow boundaries.
- When the board includes high-heat-density parts or large exposed thermal pads, review pad and heat-path design with [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb).
- When package choice, pad design, and process window need to be proven early, push those checkpoints into [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) first.
- When scope, sampling logic, interpretation method, and traceability expectations are all defined, move the full requirement set into [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Is X-Ray inspection mainly about void percentage?

A: No. Voids are only one risk category. On many products, wetting, bridging, offset, head-in-pillow, joint coverage, and lot-to-lot consistency matter just as much or more.

### Which products should put X-Ray into a routine process?

A: Products with many hidden joints, high rework cost, bottom-pad thermal dependence, or high reliability requirement are the strongest candidates for routine X-Ray control.

### Why is AOI not enough by itself?

A: Because many critical joints are under the package body, where AOI cannot see them, and those same joints often define thermal path and long-term reliability.

### Why do some teams review many X-Ray images but still improve process slowly?

A: The common reason is that the images were never linked back to stencil, solder paste, reflow, pad design, and lot data, so the team could detect anomalies but not close root cause.

### What is most worth freezing before production?

A: Freeze the inspection scope, defect-interpretation logic, sampling strategy, escalation triggers, and traceability chain first. Those decisions shape long-term quality control more than one inspection result does.

<!-- faq:end -->

<a id="references"></a>
## Public references

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   Supports the point that IPC-7095E is framed as design and assembly process guidance for BGA.

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   Supports the point that IPC-7093 is framed around Bottom Termination Components and includes X-Ray usage, repair, and reliability-related sections.

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   Supports the public context that J-STD-001J added illustration material related to bubbles seen in X-Ray images.

<a id="author"></a>
## Author and review information

- Author: HILPCB PCBA quality content team
- Technical review: assembly process, inspection, and reliability engineering team
- Last updated: 2025-11-19
