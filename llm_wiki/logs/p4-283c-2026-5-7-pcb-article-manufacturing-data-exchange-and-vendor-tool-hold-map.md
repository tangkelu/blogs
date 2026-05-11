# P4-283C PCB Article Manufacturing Data Exchange And Vendor Tool Hold Map

Date: 2026-05-07
Parent: `P4-283`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Execution mode: `claim_family_boundary_mapping_only`

## Purpose

Map the `E7` manufacturing data exchange / file prep / vendor-tool workflow cluster into English canonical claim families only.

This log does not promote vendor workflow promises, file-preparation claims, branded rule tables, or tool screenshots into `facts/`.

## E7 Subclusters

- manufacturing-data exchange format identity
- CAD-to-CAM handoff packaging
- assembly-analysis input dependency by file family
- layer-to-layer and coordinate-to-graphic alignment workflow
- vendor-tool feature and workflow promotion

## Safe Claim Families Learned

- PCB manufacturing handoff uses distinct data families for artwork, drilling, and native design exchange
- Gerber and Excellon function as manufacturing-transfer outputs rather than the original authoring database
- native PCB design files, neutral exchange packages, and manufacturing-output files carry different levels of embedded design context
- assembly-oriented review depends on whether coordinate and BOM data are already embedded in the chosen input family
- Gerber-based assembly review usually requires separate coordinate and BOM companions
- alignment problems can occur when imported graphic layers do not share a common reference frame
- alignment correction is a local workflow based on shared reference points rather than a reusable manufacturing rule
- vendor-tool pages in this cluster are usable as provenance for workflow intent, not as authority for universal DFM/DFA outcomes

## Blocked Classes

- all promises that a specific vendor tool will reduce cycle time, cost, defect rate, communication burden, or iteration count
- all file-prep promises framed as guaranteed readiness, automatic matching, or direct production unlock
- all branded rule-count tables, capability matrices, feature checklists, and software screenshots used as authority
- all BOM auto-matching, visualization, share-link, pricing, or procurement-service claims
- all exact software-operation sequences that only apply inside one branded tool shell
- all secondary-PDF numerics about rule counts, percentages, cost, yield, throughput, or market adoption

## Per-PDF Evidence Map

- `PCB制造文件传输数据的主要格式.pdf`
  - supports file-format identity and handoff taxonomy across native PCB files, ODB++, Gerber, and Excellon
  - supports the boundary that manufacturing outputs and design-authoring files are not the same data layer
  - vendor support-format list remains provenance only, not reusable authority
- `华秋DFM组装分析前需准备的数据文件.pdf`
  - supports the conditional distinction between inputs that already include coordinate/BOM context and inputs that need external coordinate/BOM companions
  - supports the claim family that assembly-analysis readiness depends on the chosen file family
  - all “prepare these files before analysis” promises remain blocked as branded workflow framing
- `简单好用！再也不用担心PCB图形对齐问题.pdf`
  - supports local alignment workflow as a claim family for layer graphics, coordinate overlays, and component-library alignment
  - useful only as a narrow alignment-correction provenance source
  - all shortcuts, UI-specific button paths, and convenience claims remain blocked
- `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf`
  - confirms a vendor-tool workflow around BOM-linked PCB visualization and assembly-side review
  - the neutral reusable layer is limited to the existence of a BOM/coordinate/graphics cross-reference workflow
  - all welding-assistance, inventory-checking, sharing, export, and progress-marking promises remain blocked
- `华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf`
  - confirms the cluster’s DFA / pre-production workflow-promotion posture
  - contains only inventory-level evidence for feature categories such as BOM checking, impedance utility, file comparison, and panelization tooling
  - all outcome claims, percentages, and rule-count summaries remain blocked
- `华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf`
  - inspected as E7-adjacent support only because it overlaps branded DFM workflow framing and software-check examples
  - not used to extend E7 beyond provenance-level workflow context

## Image / Table Candidates Worth Preserving Locally

- `PCB制造文件传输数据的主要格式.pdf` p2-p4: file-extension lists and Gerber / Excellon identity panels
- `华秋DFM组装分析前需准备的数据文件.pdf` p2-p4: input-family comparison panels for PCB / ODB vs Gerber + coordinate + BOM
- `简单好用！再也不用担心PCB图形对齐问题.pdf` p2-p6: alignment examples for layer graphics, coordinate overlays, and component-library adjustment
- `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf` p3-p4: input-path comparison panels for PCB / ODB vs Gerber + coordinate + BOM

Branding-removal notes:

- crop out `华秋DFM` top banners, QR prompts, and download / share CTAs
- preserve only the technical comparison core where the branded shell can be removed cleanly
- treat full-page UI screenshots as contaminated unless the technical panel can be isolated without the promo frame

## Contamination Patterns To Exclude

- repeated download prompts and join-group QR surfaces
- “simple to use,” “blessing,” “heavy launch,” or similar product-pitch language
- claims that one vendor workflow guarantees manufacturability, assemblability, or purchasing correctness
- share-link, export, pricing, and online-collaboration features presented as engineering authority
- rule-count and feature-count tables presented without independent authoritative grounding

## Status

`E7` is complete at claim-family level only. A narrow neutral layer around manufacturing-data family identity and conditional assembly-input dependency is preserved, while vendor-tool workflow, file-prep promises, and branded rule surfaces remain on hold.
