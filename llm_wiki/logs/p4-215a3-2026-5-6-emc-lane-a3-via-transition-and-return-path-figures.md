# P4-215A3 EMC Lane A3: Via Transition And Return-Path Figures

Date: 2026-05-06
Lane: `A3`
Model requested: `gpt-5.4`

## Purpose

Capture the `via-transition / return-path continuity / split-plane caution / backplane connector-zone` handbook slice inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`

This lane is primarily a `structural_context` lane. Most of the reviewed pages reinforce already stronger source-backed boundaries recorded in:

- `logs/p4-212-2026-5-6-via-transition-authority-recovery-integration.md`

Accordingly, this lane preserves figure and page traceability, notes narrow vocabulary alignment, and keeps handbook formulas, thresholds, and cookbook routing rules blocked.

## Page Slice Covered

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- extracted text pages:
  - `page-0057.txt`
  - `page-0058.txt`
  - `page-0059.txt`
  - `page-0060.txt`
  - `page-0061.txt`
  - `page-0062.txt`
  - `page-0066.txt`
  - `page-0067.txt`
  - `page-0068.txt`
  - `page-0069.txt`
- source page numbers:
  - `57`
  - `58`
  - `59`
  - `60`
  - `61`
  - `62`
  - `66`
  - `67`
  - `68`
  - `69`
- reviewed image assets:
  - `images/bc479982eb8d9758.png`
  - `images/6cc6f9127125ec41.png`
  - `images/57f5e8a7316eb23e.png`
  - `images/bfc8a1e13a93b359.png`
  - `images/ab37fbcc87f27b21.png`
  - `images/08e387b65ae01f57.png`
  - `images/0396b2b73498a810.png`
  - `images/c937cdef5bf9a582.png`
- manifest traceability verified from:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/manifest.json`

## `exact_data_candidate` Items

No new lane-local `exact_data_candidate` items are strong enough to stand on their own from this secondary-PDF slice.

Reason:

- the reviewed images are primarily topology and return-path diagrams
- the handbook numerics and formulas in this slice remain blocked
- the strongest reusable content here mostly reinforces already stronger boundaries from TI / ADI / NXP style primary sources already summarized in `P4-212`

Narrow alignment note:

- the slice reinforces already-recovered vocabulary such as:
  - `via-transition`
  - `return-path continuity`
  - `impedance discontinuity`
  - `nearby ground-return handling`
  - `avoid splits / slots under critical routes`

## `structural_context_candidate` Items

### `dense via field can create slot discontinuity in reference plane`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `57`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/bc479982eb8d9758.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure shows a dense connector/via field with isolation rings merging into a slot-like opening in the ground or power plane; preserve as slot-formation context, not as a numeric rule.

### `low-speed return current follows broad resistive path`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `58`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/6cc6f9127125ec41.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure depicts a broad return-current distribution over the reference plane for a lower-speed case; this aligns with existing return-path boundary language and is useful as structural context only.

### `high-speed return current concentrates beneath signal path`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `59`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/57f5e8a7316eb23e.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure shows a narrow, bundled high-speed return-current path under the signal route; this strongly reinforces already-recovered return-path continuity vocabulary.

### `slot crossing forces return-path detour and crosstalk risk`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `60`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/bfc8a1e13a93b359.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure shows signals crossing a slot in the reference plane and labels that the A-B and C-D return currents cannot flow along the slot; preserve as slot-crossing caution context.

### `bridge across split to restore return-path continuity`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `61`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/ab37fbcc87f27b21.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure compares return-current routing with and without an explicit bridge across a split, showing the preferred bridged path when split crossing cannot be avoided; preserve as structural context only because bridge-style recipes are not source-backed enough for direct promotion.

### `connector should not be placed on ground-plane seam`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `61`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/08e387b65ae01f57.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure contrasts an incorrect connector placement across a ground-plane seam with a corrected placement that avoids A/B potential difference across the external cable path.

### `high-density connector escape should preserve plane continuity`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `62`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/0396b2b73498a810.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure contrasts an over-isolated connector region that forms a slot with a more moderate separation that preserves reference-plane continuity and allows direct return-current passage.

### `backplane branching topology better-versus-bad example`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `67`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/c937cdef5bf9a582.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the figure contrasts a `BAD` branching structure with a `BETTER` topology for a driver feeding multiple receivers; preserve as backplane connector-zone and interconnect-topology context only.

## `blocked_secondary_pdf_claim` Items

### `via-count minimization and sub-1GHz inner-layer routing rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `57`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook recommends minimizing via count, preferring plane-continuous layer changes, and preferring inner-layer routing for signals below `1GHz`; these cookbook rules and threshold claims remain blocked.

### `via delay and edge-slowing numeric claims`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `57`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook mentions via-induced effects such as `tens of ps` edge slowing and `hundreds of ps` delay; these exact numeric statements remain blocked as handbook-only claims.

### `no signal should cross a split as universal rule text`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `59`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/57f5e8a7316eb23e.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook states that neither high-speed nor low-speed signals should cross a split and lists several consequences; the structural risk is useful, but the universalized rule text remains blocked pending stronger source handling.

### `slot-bridging execution recipe`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `60`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/bfc8a1e13a93b359.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook says effective bridging should be added when split crossing is unavoidable; because `P4-212` explicitly kept bridge-style routing rules unrecovered, this remains blocked as secondary-PDF execution guidance.

### `quiet-ground crossing treatment as direct reusable rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `62`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook states that differential pairs crossing `quiet ground` need no treatment while ordinary signals must be given a return path; this remains blocked as handbook-only execution guidance.

### `connector-zone coupling inductance formula`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `68`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook gives `L=5dln(d/w)` for coupling inductance through a dense via area; the formula remains blocked as a handbook formula even though the page is useful for topic routing.

### `backplane topology and level-selection numeric recipes`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `67`
  - `68`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/c937cdef5bf9a582.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook gives topology and interface-level advice including `2000 mil`, `<100M`, `hundreds of MHz`, and `>1GHz` signal-family selections; these are blocked as handbook-only or owner-specific design recipes.

### `backplane spacing and shielding distance rules`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `69`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - handbook rules such as `10mm`, `15mm`, `20H`, and `3W` in the backplane grounding/shielding section remain blocked as secondary-PDF thresholds and spacing rules.

## Source-Mapping Recommendations

### `reuse existing primary-source-backed via-transition boundary before opening new exact-data promotion`

- target source families:
  - `NXP`
  - `ADI`
  - `TI`
- short recommendation:
  - for prompts needing `via-transition`, `stub`, `return-path continuity`, or `nearby ground-via` vocabulary, reuse the already stronger boundary established in `P4-212` rather than promoting these handbook figures directly.

### `recover stronger slot-crossing or bridge-style sources only if a future prompt truly needs them`

- target source families:
  - `TI`
  - `ADI`
  - `NXP`
  - signal-integrity application notes with explicit split-plane return-path treatment
- short recommendation:
  - the handbook figures are useful for structural inventory, but bridge-style and slot-crossing execution claims should remain blocked unless a stronger primary source is recovered.

### `recover connector-zone and dense-via-field return-path guidance from primary backplane sources`

- target source families:
  - `connector-vendor application notes`
  - `TI`
  - `ADI`
  - `NXP`
- short recommendation:
  - if future work needs more than general return-path continuity posture, recover primary backplane or connector-zone guidance that explicitly covers dense via fields, return-current detours, and reference-plane discontinuity around connectors.

### `treat backplane topology figure as structural support, not exact rule support`

- target source families:
  - `signal-integrity method notes`
  - `backplane design application notes`
- short recommendation:
  - the `BAD` versus `BETTER` branching figure on page `67` is useful for structural review language, but numeric matching, branching limits, and topology-selection rules need stronger method-scoped sources.

## Unresolved Items

### `no extracted image assets for pages 66, 68, and 69`

- short note:
  - the reviewed slice includes text on pages `66`, `68`, and `69`, but the manifest provides no image assets for those pages; only text-derived claim inventory is available there.

### `quiet-ground example figure appears absent from the provided asset set`

- short note:
  - page `62` text references `quiet ground` handling and an `RS-232` example, but no corresponding quiet-ground figure asset appears in the reviewed manifest slice.

### `bridge-style routing remains below admission threshold`

- short note:
  - `P4-212` explicitly kept `slot-crossing / quiet-ground` at `existing_fact_layer_reused_only`, so the handbook bridge figures should remain structural evidence only.

### `this slice mostly reinforces already-recovered boundaries`

- short note:
  - the strongest content here is not new exact data but repeated structural reinforcement of:
    - `return-path continuity`
    - `reference-plane discontinuity risk`
    - `split / slot avoidance`
    - `connector-zone continuity posture`

## Lane Status

- lane output status:
  - `completed_at_candidate_inventory_level`
- exact-data admission status:
  - `secondary_pdf_claim_inventory_only`
- strongest reusable outcome:
  - `structural_context reinforcement for already stronger via-transition and return-path boundaries`
- main policy result:
  - handbook formulas, routing thresholds, bridge recipes, and backplane spacing rules remain blocked pending stronger primary-source recovery
