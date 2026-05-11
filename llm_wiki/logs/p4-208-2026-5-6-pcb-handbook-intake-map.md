# P4-208 `PCB资料` Handbook Intake Map

Date: 2026-05-06

## Purpose

This log starts the first formal learning pass for the `4` handbook PDFs under `/code/blogs/tmps/PCB资料`.

Scope of this pass:

- text-first handbook intake
- topic-family inventory
- existing `llm_wiki` support check
- blocked-claim classification
- routing for later image/table vision passes

This pass does **not** promote handbook-originated numeric thresholds or acceptance criteria directly into `facts/` or `wiki/`.

## Input Files

- `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`

Derived text/image assets:

- `/code/blogs/tmps/pcb_pdf_extracted_full`

## Batch Summary

- handbook count: `4`
- total pages: `478`
- pages with extracted images: `422`
- extraction posture: `text_first`

## Existing `llm_wiki` Support Found

Current corpus already has meaningful partial support for:

- PCBA inspection and test-stack vocabulary
- DFM / DFA / DFT framing
- PCB/PCBA process governance
- file-package and CAM handoff boundaries
- high-speed / impedance / board-review conservative routing
- EMC-aware board-review context

Strongest likely reuse areas:

- `wiki/testing/pcba-quality-gates-and-test-strategy.md`
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
- `wiki/processes/pcb-and-assembled-board-stage-boundaries.md`
- `wiki/processes/public-capability-parameter-consumption-map.md`
- existing `facts/methods/*inspection*`, `*dfm*`, `*impedance*`, and `*validation*` lanes

## Per-Handbook Intake

### 1. `【PCB必备】42种-常见PCB封装设计指导规范.pdf`

Observed posture:

- heavily branded handbook with repeated vendor banner / CTA
- text is extractable
- all `41` pages contain image assets

Primary topic families:

- package / footprint naming taxonomy
- pad classes and pad-shape vocabulary
- silk / origin / pin ordering / keepout framing
- hole-size and package-library governance

Safe reuse classes in this pass:

- package-family taxonomy
- footprint-library governance topics
- pad / origin / pin-order / keepout claim inventory

Blocked claim classes:

- handbook-specific exact hole tables
- exact keepout values
- direct promotion of vendor DFM-rule tables
- any claim that a specific naming or pad rule is universal industry law

Recommended next route:

- create a package / footprint intake log or wiki routing page
- later use selective vision pass for figure-heavy package examples

Current status:

- `completed_at_claim_family_level`

### 2. `【PCB必备】85页-PCB设计EMC设计指导书.pdf`

Observed posture:

- relatively clean technical handbook
- text extraction quality is high
- `46` pages contain images

Primary topic families:

- EMC terminology and design-stage posture
- filtering / decoupling / bypass behavior
- grounding and return-path design
- split planes and slot crossing
- microstrip / stripline and routing effects

Safe reuse classes in this pass:

- EMC-aware board-review vocabulary
- filtering / decoupling topic routing
- ground-split / slot-crossing / signal-quality claim inventory

Blocked claim classes:

- old supplier-specific cost references
- exact impedance / delay / current / stackup numbers
- universal EMC performance promises

Recommended next route:

- strong candidate for future `wiki/processes` or `wiki/methods` aggregation
- selective vision pass should target diagram and table pages only

Current status:

- `completed_at_claim_family_level`

### 3. `【PCB必备】158页-PCBA检验规范汇总.pdf`

Observed posture:

- inspection and acceptability style handbook
- text extraction quality is high
- `141` pages contain images

Primary topic families:

- EOS / ESD handling
- component placement and orientation
- soldering conditions and defects
- cleanliness / board defects / warpage / jumper wire
- SMT/THT workmanship vocabulary

Safe reuse classes in this pass:

- defect-taxonomy intake
- process-stage vocabulary
- inspection-governance routing

Blocked claim classes:

- accept / fail image judgments
- workmanship thresholds
- standards-equivalent acceptance criteria
- direct substitution for paid IPC acceptance documents

Recommended next route:

- create a dedicated inspection-handbook intake log
- later promote only taxonomy / boundary content after standards metadata alignment

Current status:

- `completed_at_claim_family_level`

### 4. `【PCB必备】194页-PCB设计规范经验之书.pdf`

Observed posture:

- RK3588-specific design guide / board-reference handbook
- text extraction quality is high
- all `194` pages contain image assets
- contains both real layout-review knowledge and owner-/platform-specific numerics

Primary topic families:

- PCB design flow and rule setup
- stackup / impedance / via / length-matching / serpentine routing
- PMIC / power PCB design
- high-speed and interface-specific routing
- memory / Type-C / camera / display / RJ45 / RGMII / audio interface layout

Safe reuse classes in this pass:

- board-review checklist families
- interface routing topic discovery
- power-layout and high-speed review claim inventory

Blocked claim classes:

- RK3588-owner-specific numerics
- exact stackup / impedance / current tables
- direct reuse of promotional or owner-specific screenshot material
- any claim that SoC-platform advice is universal for all boards

Recommended next route:

- split future learning by topic family rather than by full handbook
- create narrower lanes for power layout, interface routing, and high-speed review boundaries
- selective vision pass should exclude repeated promo slices and focus on real diagrams/tables

Current status:

- `completed_at_claim_family_level`

## Priority Ranking For Next Learning Pass

1. `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
   - cleanest technical route
   - strongest overlap with existing EMC / routing / grounding wiki potential
2. `【PCB必备】158页-PCBA检验规范汇总.pdf`
   - highest inspection-taxonomy value
   - needs careful acceptance-criteria blocking
3. `【PCB必备】42种-常见PCB封装设计指导规范.pdf`
   - useful for package / footprint governance
   - branding heavier, but still structurally valuable
4. `【PCB必备】194页-PCB设计规范经验之书.pdf`
   - very large and valuable
   - must be split into narrow topic lanes because of owner-specific numeric content

## Vision-Pass Guidance

Only use `gpt-5.4` visual passes for:

- diagram-heavy pages without good text alternatives
- image tables whose structure matters
- package/footprint illustrations
- defect-example plates

Do not spend vision passes on:

- plain text pages
- pages whose only images are repeated banners, QR codes, or promo slices
- pages already sufficiently represented by extracted text

## Current Batch Status

- handbook intake status: `completed_at_claim_family_level`
- reusable fact-layer promotion: `not_started`
- selective image/table analysis: `not_started`
- recommended next lane: `85页 PCB设计EMC设计指导书`
