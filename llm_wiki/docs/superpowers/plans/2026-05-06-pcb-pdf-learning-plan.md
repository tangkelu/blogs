# PCB PDF Exact-Data Learning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Learn formulas, data tables, figures, and parameter data from `/code/blogs/tmps/PCB资料` into reusable `llm_wiki` knowledge modules that later blog-writing agents can directly consume, combine, and cite.

**Architecture:** Use a four-layer learning pipeline. Layer 1 preserves raw evidence through extracted page text, local images, and manifests. Layer 2 turns each PDF slice into English canonical data families with linked Chinese provenance. Layer 3 recovers exact data through page-level image/table understanding plus primary-source validation, classifying each item as `part-scoped`, `method-scoped`, `standard-scoped`, or `dated-capability`. Layer 4 promotes only validated exact data into English `sources/`, `facts/`, and `wiki/`, while keeping reusable image assets local with explicit source-page links.

**Tech Stack:** `PyMuPDF` extraction outputs in `/code/blogs/tmps/pcb_pdf_extracted_full`, local Markdown knowledge-base files under `llm_wiki/`, `gpt-5.4` subagents for page/table/figure lanes, local image assets, manifest references, and controller integration logs.

---

## Scope Definition

### In Scope

- Learning exact formulas, parameters, figures, and data tables from `/code/blogs/tmps/PCB资料`
- Preserving real image/table assets locally
- Removing or excluding vendor logos, QR codes, CTA banners, and branded page shells
- Writing English canonical `sources/`, `facts/`, and later `wiki/` pages for reusable blog consumption
- Running bounded subagent lanes in parallel for PDF slices, table reading, figure interpretation, and source mapping

### Out of Scope

- Directly treating raw PDF prose as already-learned fact layer
- Preserving branded full-page marketing posters as reusable image assets
- Bulk OCR of every image-bearing page regardless of value
- Publishing paid-standard threshold tables without appropriate authority
- Rewriting blogs in this plan

## File Structure And Responsibilities

### Existing source material and control files

- `tmps/PCB资料/`
  - raw PDFs
- `tmps/pcb_pdf_extracted_full/`
  - extracted page text, local image assets, manifest references
- `scripts/extract_pcb_pdf_assets.py`
  - extraction pipeline
- `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
  - batch intake and image-governance controller
- `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
  - handbook intake map
- `llm_wiki/logs/p4-209*`, `p4-210*`, `p4-211*`, `p4-212*`
  - EMC sub-lane intake and partial promotion history
- `llm_wiki/policies/language-normalization-and-indexing.md`
  - canonical English indexing rule

### New outputs that must exist after this plan

- One exact-data family map for the whole PDF batch
- One asset-learning map that links figures/tables to English canonical concepts
- One exact-data promotion policy that defines how formulas/tables/parameters are admitted
- Three first-wave exact-data workstream controller logs
- New `sources/registry` records for exact authoritative anchors
- New `facts/` for exact reusable formulas, table semantics, and parameter boundaries
- One or more `wiki/` aggregation pages only after multiple exact-data facts land in the same family

---

### Task 1: Create The Batch-Wide Exact-Data Learning Map

**Files:**
- Create: `llm_wiki/logs/p4-213-2026-5-6-pcb-pdf-exact-data-learning-map.md`
- Input:
  - `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
  - `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
  - `tmps/pcb_pdf_extracted_full/*/manifest.json`
- Test: manual review only

- [ ] **Step 1: Create the batch map skeleton**

Create `llm_wiki/logs/p4-213-2026-5-6-pcb-pdf-exact-data-learning-map.md` with:

```md
# P4-213 PCB PDF Exact-Data Learning Map

## Purpose
## Batch Summary
## Family Ranking
## Family Definitions
## Promotion Targets
## Blocked Families
## Final Status
```

- [ ] **Step 2: Define the exact-data families**

Populate exactly these top-level families:

```md
- EMC component and suppression data
- Transmission-line / via-transition / return-path data
- Safety spacing and insulation-distance data
- PCBA inspection and defect-taxonomy data
- Package / footprint / library-governance data
```

For each family, include:

- exact data types expected
- PDF origins
- likely table/figure-heavy page ranges
- promotion target (`sources`, `facts`, `wiki`)

- [ ] **Step 3: Add first-wave ranking**

Add this first-wave ranking:

```md
1. EMC component and suppression data
2. PCBA inspection and defect-taxonomy data
3. Package / footprint / library-governance data
4. Safety spacing and insulation-distance data
5. Transmission-line / via-transition / return-path data
```

- [ ] **Step 4: Add blocked families**

Mark these as blocked or deferred until stronger authority exists:

- pure handbook acceptance thresholds
- generic vendor DFM rule tables
- product-platform-specific routing numbers
- unlabeled current-carrying tables copied from secondary PDF pages

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-213-2026-5-6-pcb-pdf-exact-data-learning-map.md
git commit -m "docs: add pcb pdf exact data learning map"
```

---

### Task 2: Create The Figure/Table Asset Learning Contract

**Files:**
- Create: `llm_wiki/logs/p4-214-2026-5-6-pcb-pdf-figure-table-learning-contract.md`
- Input:
  - `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
  - `tmps/pcb_pdf_extracted_full/*/manifest.json`
- Test: manual review only

- [ ] **Step 1: Create the contract skeleton**

Create:

```md
# P4-214 PCB PDF Figure/Table Learning Contract

## Purpose
## Asset Classes
## Learning Actions
## Branding Rules
## Citation Contract
## English Canonical Mapping
## Final Status
```

- [ ] **Step 2: Define asset classes and learning actions**

Fill in:

```md
- formula_figure
- parameter_table
- defect_photo
- process_diagram
- package_footprint_drawing
- branded_poster
```

For each class, define whether the learning action is:

- extract exact values
- extract structural meaning
- preserve as local asset
- block from reuse

- [ ] **Step 3: Define branding rules**

Explicitly require:

- crop away logos/header/footer CTA where separable
- keep only technical sub-regions
- block assets where branding is inseparable from the technical content
- never store full branded pages as reusable figures

- [ ] **Step 4: Define citation contract**

Require every learned formula/table/figure to keep:

- source PDF path
- source page number
- local asset path if any
- English canonical concept name
- whether the item is exact data or only structural context

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-214-2026-5-6-pcb-pdf-figure-table-learning-contract.md
git commit -m "docs: add pcb pdf figure table learning contract"
```

---

### Task 3: Define The Exact-Data Admission Policy

**Files:**
- Create: `llm_wiki/policies/exact-data-admission-policy.md`
- Modify: `llm_wiki/policies/prompt-consumption-specification.md`
- Test: manual review only

- [ ] **Step 1: Create the policy skeleton**

Create:

```md
# Exact Data Admission Policy

## Purpose
## Data Classes
## Required Metadata
## Admission Gates
## Blocked Promotions
## Output Targets
```

- [ ] **Step 2: Define the data classes**

Populate exactly:

```md
- part_scoped_exact_data
- method_scoped_exact_data
- standard_scoped_exact_data
- dated_capability_exact_data
- secondary_pdf_claim_inventory_only
```

- [ ] **Step 3: Define required metadata**

Require every admitted exact-data item to have:

- English canonical concept name
- exact source page or source document
- conditions
- scope
- whether the item came from figure/table/text
- refresh rule

- [ ] **Step 4: Define blocked promotions**

Explicitly block:

- turning PDF example values into universal defaults
- turning secondary handbook tables into standards truth
- promoting OCR output without source-class validation
- mixing Chinese and English canonical keys for the same concept

- [ ] **Step 5: Add prompt-consumption hook**

Add one note to `llm_wiki/policies/prompt-consumption-specification.md` stating that exact numeric reuse is only allowed when the item has already passed `exact-data-admission-policy.md`.

- [ ] **Step 6: Commit**

```bash
git add llm_wiki/policies/exact-data-admission-policy.md llm_wiki/policies/prompt-consumption-specification.md
git commit -m "docs: define exact data admission policy"
```

---

### Task 4: Create Workstream A For EMC Exact Data

**Files:**
- Create: `llm_wiki/logs/p4-215a-2026-5-6-emc-exact-data-workstream.md`
- Input:
  - `llm_wiki/logs/p4-209-2026-5-6-emc-handbook-controller-note.md`
  - `llm_wiki/logs/p4-210a-2026-5-6-emc-source-lane-capacitor-parasitic-resonance.md`
  - `llm_wiki/logs/p4-210b-2026-5-6-emc-source-lane-common-mode-choke-vs-ferrite-bead.md`
  - `llm_wiki/logs/p4-212-2026-5-6-via-transition-authority-recovery-integration.md`
  - `tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/`
- Test: manual review only

- [ ] **Step 1: Create the workstream skeleton**

Create:

```md
# P4-215A EMC Exact Data Workstream

## Purpose
## Exact Data Targets
## Page Slices
## Subagent Lanes
## Promotion Targets
## Completion Criteria
```

- [ ] **Step 2: Define exact data targets**

List these exact targets:

- capacitor impedance / ESR / SRF / antiresonance examples
- ferrite bead impedance/current examples
- common-mode choke current/DCR/intended-line-family examples
- via-transition parasitic and return-path vocabulary backed by primary sources

- [ ] **Step 3: Define subagent lanes**

Create these lane definitions inside the file:

```md
- Lane A1: capacitor figures and parameter tables
- Lane A2: ferrite bead versus common-mode choke figures and tables
- Lane A3: via-transition diagrams and return-path figures
```

For each lane, include:

- page range
- expected outputs
- whether image understanding is required

- [ ] **Step 4: Define outputs**

Require the workstream to produce:

- local figure/table asset references
- candidate exact-data rows
- candidate source mappings
- candidate fact-card boundaries

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-215a-2026-5-6-emc-exact-data-workstream.md
git commit -m "docs: add emc exact data workstream"
```

---

### Task 5: Create Workstream B For PCBA Inspection Exact Data

**Files:**
- Create: `llm_wiki/logs/p4-215b-2026-5-6-pcba-inspection-exact-data-workstream.md`
- Input:
  - `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
  - `tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/manifest.json`
  - `tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/pages/`
- Test: manual review only

- [ ] **Step 1: Create the workstream skeleton**

Create:

```md
# P4-215B PCBA Inspection Exact Data Workstream

## Purpose
## Exact Data Targets
## Page Slices
## Subagent Lanes
## Promotion Targets
## Completion Criteria
```

- [ ] **Step 2: Define exact data targets**

List:

- defect taxonomy tables
- workmanship example figures
- EOS / ESD handling rule tables
- cleanliness / warpage / jumper / inspection-class examples

- [ ] **Step 3: Define subagent lanes**

Create these lanes:

```md
- Lane B1: EOS / ESD / handling pages
- Lane B2: solder defect and workmanship pages
- Lane B3: cleanliness / warpage / jumper / inspection-vocabulary pages
```

- [ ] **Step 4: Define promotion caution**

State explicitly:

- defect taxonomy is promotable
- example-image classes may be promotable as local assets
- accept/reject thresholds remain blocked until mapped to stronger standards authority

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-215b-2026-5-6-pcba-inspection-exact-data-workstream.md
git commit -m "docs: add pcba inspection exact data workstream"
```

---

### Task 6: Create Workstream C For Package / Footprint Exact Data

**Files:**
- Create: `llm_wiki/logs/p4-215c-2026-5-6-package-footprint-exact-data-workstream.md`
- Input:
  - `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
  - `tmps/pcb_pdf_extracted_full/PCB必备-42种-常见PCB封装设计指导规范/manifest.json`
  - `tmps/pcb_pdf_extracted_full/PCB必备-42种-常见PCB封装设计指导规范/pages/`
- Test: manual review only

- [ ] **Step 1: Create the workstream skeleton**

Create:

```md
# P4-215C Package And Footprint Exact Data Workstream

## Purpose
## Exact Data Targets
## Page Slices
## Subagent Lanes
## Promotion Targets
## Completion Criteria
```

- [ ] **Step 2: Define exact data targets**

List:

- package naming tables
- pad-shape / origin / pin-1 / keepout drawings
- footprint-library governance examples
- hole and pad relationship examples

- [ ] **Step 3: Define subagent lanes**

Create these lanes:

```md
- Lane C1: package taxonomy and naming pages
- Lane C2: pad / origin / pin-1 / keepout drawing pages
- Lane C3: library-governance and hole/pad example pages
```

- [ ] **Step 4: Define what is promotable**

State:

- package-family taxonomy is promotable
- footprint-governance examples are promotable
- exact dimension tables stay blocked unless sourced from stronger owner/standard references

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-215c-2026-5-6-package-footprint-exact-data-workstream.md
git commit -m "docs: add package footprint exact data workstream"
```

---

### Task 7: Create The Subagent Coordination Plan

**Files:**
- Create: `llm_wiki/logs/p4-216-2026-5-6-pcb-pdf-subagent-coordination-plan.md`
- Input:
  - `llm_wiki/logs/p4-215a-2026-5-6-emc-exact-data-workstream.md`
  - `llm_wiki/logs/p4-215b-2026-5-6-pcba-inspection-exact-data-workstream.md`
  - `llm_wiki/logs/p4-215c-2026-5-6-package-footprint-exact-data-workstream.md`
- Test: manual review only

- [ ] **Step 1: Create the coordination-plan skeleton**

Create:

```md
# P4-216 PCB PDF Subagent Coordination Plan

## Purpose
## Workstream Ownership
## Subagent Output Contract
## Main-Agent Integration Contract
## Parallel Execution Order
## Completion Criteria
```

- [ ] **Step 2: Define the output contract**

Require every subagent lane to return:

- page slice covered
- candidate formulas/tables/figures found
- exact values or structural meaning extracted
- image/table asset references
- English canonical concept names
- source-mapping recommendation
- blocked/unresolved items

- [ ] **Step 3: Define the main-agent contract**

Require the main agent to:

- decide canonical English names
- deduplicate concepts across lanes
- approve or reject fact promotion
- update trackers
- keep Chinese only as provenance, not as canonical keys

- [ ] **Step 4: Define execution order**

Set order:

```md
Round 1: A1 + B1 + C1
Round 2: A2 + B2 + C2
Round 3: A3 + B3 + C3
Round 4: controller integration and promotion review
```

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-216-2026-5-6-pcb-pdf-subagent-coordination-plan.md
git commit -m "docs: add pcb pdf subagent coordination plan"
```

---

### Task 8: Define Program Completion Criteria

**Files:**
- Create: `llm_wiki/logs/p4-217-2026-5-6-pcb-pdf-program-completion-criteria.md`
- Test: manual review only

- [ ] **Step 1: Create the completion-criteria skeleton**

Create:

```md
# P4-217 PCB PDF Program Completion Criteria

## Purpose
## Minimum Completion
## Strong Completion
## Non-Completion States
## Exit Checklist
```

- [ ] **Step 2: Define minimum completion**

Require:

- exact-data family map exists
- figure/table learning contract exists
- exact-data admission policy exists
- three workstream plans exist
- subagent coordination plan exists

- [ ] **Step 3: Define strong completion**

Require:

- at least three workstreams executed
- at least two exact-data families promoted into `sources/` + `facts/`
- at least one topic-level wiki page assembled from the learned facts
- at least one local technical figure or table asset linked into the knowledge layer

- [ ] **Step 4: Define non-completion**

Explicitly state these are not completion:

- only extraction outputs
- only controller logs
- only source bookmarks
- only authority recovery without exact-data promotion
- only Chinese provenance without English canonical knowledge modules

- [ ] **Step 5: Commit**

```bash
git add llm_wiki/logs/p4-217-2026-5-6-pcb-pdf-program-completion-criteria.md
git commit -m "docs: add pcb pdf program completion criteria"
```

---

## Self-Review

### Spec coverage

This plan now covers the actual requested objective:

- learning formulas
- learning data tables
- learning figures
- learning parameter data
- preserving local assets
- English canonical indexing
- subagent-parallel execution
- promotion into blog-consumable knowledge modules

### Placeholder scan

No `TBD`, `TODO`, or vague “analyze later” placeholders remain. Every task specifies exact files, exact outputs, and exact subagent-facing workstream boundaries.

### Type consistency

The plan uses one consistent vocabulary:

- `exact data`
- `English canonical concept`
- `part-scoped / method-scoped / standard-scoped / dated-capability`
- `asset learning`
- `promotion`

No conflicting naming scheme is introduced.

---

Plan complete and saved to `llm_wiki/docs/superpowers/plans/2026-05-06-pcb-pdf-learning-plan.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
