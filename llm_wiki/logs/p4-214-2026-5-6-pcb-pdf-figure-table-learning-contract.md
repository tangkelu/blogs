# P4-214 PCB PDF Figure / Table Learning Contract

Date: 2026-05-06

## Purpose

This controller log defines the bounded learning contract for figure, table, formula, and technical image intake from:

- `/code/blogs/tmps/PCB资料`
- `/code/blogs/tmps/pcb_pdf_extracted_full`

The purpose of this contract is to make later `llm_wiki` and blog composition work directly reusable for:

- figures
- tables
- formulas
- parameter visuals
- defect examples
- process illustrations

while preserving only technically useful local assets and removing or blocking vendor branding when possible.

This contract aligns with:

- `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
- `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
- `llm_wiki/policies/language-normalization-and-indexing.md`

## Scope

This contract applies to image-like learning units derived from PCB PDFs, including:

- full-page technical figures
- cropped diagrams
- formula panels
- tables
- defect photographs
- footprint and package drawings
- process illustrations

This contract does not authorize direct promotion of raw PDF images into `facts/`, `wiki/`, or public-facing blog output without class-based review and branding governance.

## Core Contract

### 1. Source-first rule

All figures, tables, and images from these PDFs are intake material first.

They may support:

- claim inventory
- vocabulary discovery
- structural learning
- local technical asset preservation
- later source-backed composition planning

They do not automatically support:

- authority-level fact promotion
- universal numeric rule reuse
- acceptance-criteria reuse
- supplier capability claims
- standards equivalence claims

### 2. Branding-removal rule

Every candidate asset must be checked for:

- vendor logos
- QR codes
- CTA banners
- download prompts
- contact or group-join prompts
- product UI promo slices
- repeated branded headers and footers

Required behavior:

- if branding is separable, crop or mask it away
- if branding is inseparable from the technical content, block reuse of the branded image
- if only a technical sub-region is reusable, preserve only that local sub-region
- if the page is mainly a branded poster, block image reuse and keep only claim inventory or text-derived topic routing

### 3. Provenance-link rule

Every learned asset must preserve exact traceability from source PDF to learned output.

Required fields for every learned asset:

- source PDF path
- page number
- local asset path
- English canonical concept name
- learning type: `exact_data` or `structural_context`

### 4. Canonical-language rule

Per `language-normalization-and-indexing` policy:

- Chinese filenames and page references may remain as provenance
- reusable concept naming must normalize to English
- each learned asset must have one English canonical concept name
- do not create parallel Chinese and English concept identities for the same reusable asset meaning

## Asset Classes And Required Learning Action

### `formula_figure`

Definition:

- equation panels
- derived formula diagrams
- formula plus labeled geometry figures
- transmission-line, stackup, or electrical-parameter formula visuals

Learning action:

- `extract exact values`
- `extract structural meaning`
- `preserve as local asset`

Reuse posture:

- preserve the visual locally if branding is removable
- extract variable names, symbol roles, and concept structure
- do not promote handbook- or vendor-origin formulas as authority without stronger source backing
- if values or equations are old, partial, image-blurred, or unsupported, keep them as claim inventory only

### `parameter_table`

Definition:

- impedance tables
- spacing tables
- process setting tables
- acceptance-like parameter matrices
- package dimension tables
- material property tables

Learning action:

- `extract exact values`
- `preserve as local asset`

Reuse posture:

- exact rows and columns may be extracted into intake notes or later structured records
- preserve table image locally if readable after crop/mask
- block direct fact promotion when the table appears vendor-specific, standards-sensitive, capability-specific, or not independently sourced
- use the table as a bridge to later authoritative source recovery where needed

### `defect_photo`

Definition:

- solder defect examples
- board damage photos
- void, bridging, tombstone, contamination, crack, delamination, or similar inspection photos

Learning action:

- `extract structural meaning`
- `preserve as local asset`

Reuse posture:

- prioritize defect identity, visual taxonomy, and inspection vocabulary
- do not infer acceptance or rejectability from image alone unless the source class is later matched to authoritative criteria
- keep the image locally when branding is removable and the defect remains visually clear

### `process_diagram`

Definition:

- flowcharts
- manufacturing flow diagrams
- DFM / DFA / DFT process illustrations
- return-path or stackup concept diagrams
- grounding, shielding, or routing concept figures

Learning action:

- `extract structural meaning`
- `preserve as local asset`

Reuse posture:

- preserve neutral diagrams locally
- extract concept flow, stage boundaries, and relationship structure
- block vendor workflow claims or “best practice” claims that appear supplier-specific or unsupported
- prefer neutral re-expression of the process logic

### `package_footprint_drawing`

Definition:

- footprint diagrams
- pad layout drawings
- package geometry sketches
- land-pattern examples
- pin-1, origin, keepout, courtyard, or orientation illustrations

Learning action:

- `extract exact values`
- `extract structural meaning`
- `preserve as local asset`

Reuse posture:

- exact dimensions may be captured at intake level when clearly legible
- preserve locally for future package-library or footprint-governance work
- do not treat single-PDF dimension drawings as universal unless source class is authoritative
- keep English canonical concept names for package family and drawing type

### `branded_poster`

Definition:

- marketing posters
- pages dominated by vendor identity
- CTA-heavy layouts
- promotional UI screenshots
- figures whose main value is branded persuasion rather than neutral technical content

Learning action:

- `block from reuse`

Reuse posture:

- do not preserve as a reusable learned image
- only keep claim inventory, page reference, and block reason
- if a small technical sub-region is clearly separable, reclassify that sub-region into another asset class and preserve only the neutral crop

## Learning-Type Rules

Use exactly one learning-type label per stored learned asset:

- `exact_data`
  - the asset is primarily valuable because specific values, dimensions, symbols, rows, columns, or numeric labels matter
- `structural_context`
  - the asset is primarily valuable because the concept layout, failure mode, topology, sequence, or geometry relationship matters more than exact numbers

Guidance:

- `formula_figure` may produce both exact extraction notes and a local preserved asset, but the stored asset still needs one declared primary learning type
- `parameter_table` is usually `exact_data`
- `defect_photo` is usually `structural_context`
- `process_diagram` is usually `structural_context`
- `package_footprint_drawing` may be either, depending on whether dimension values or layout structure is the primary learning target

## Required Asset Metadata

Every learned asset must keep all of the following:

- `source_pdf_path`
- `page_number`
- `local_asset_path`
- `english_canonical_concept_name`
- `learning_type`
- `asset_class`
- `branding_removed`
- `crop_or_mask_strategy`
- `reuse_status`

Recommended allowed values:

- `learning_type`
  - `exact_data`
  - `structural_context`
- `branding_removed`
  - `yes`
  - `partial`
  - `no`
- `crop_or_mask_strategy`
  - `top_crop`
  - `bottom_crop`
  - `side_crop`
  - `multi_crop`
  - `mask`
  - `crop_and_mask`
  - `blocked`
- `reuse_status`
  - `safe_local_preserve`
  - `needs_source_recovery`
  - `blocked`

## Branding And Image-Governance Rules

### Allowed preservation

Preserve locally only when the technical core survives after de-branding.

Examples:

- a routing diagram after top-banner removal
- a package drawing after footer CTA crop
- a table after masking a corner logo
- a defect photo after removing repeated branded frame strips

### Required blocking

Block image reuse when:

- the logo is embedded inside the only useful technical region
- the QR code overlaps the technical content materially
- the figure is mostly a vendor poster or product promotion
- the image’s value depends on branded UI rather than a neutral engineering concept
- removing branding would destroy readability or meaning

### Required posture for inseparable branding

If branding is inseparable:

- do not keep the branded image as a reusable technical asset
- keep only provenance plus block reason
- optionally retain text-derived claim inventory or concept routing separately

## Learning Output Expectations By Class

### Exact-value extraction priority

Classes that may justify exact-value extraction:

- `formula_figure`
- `parameter_table`
- `package_footprint_drawing`

But exact extraction does not equal authority. It means:

- exact symbols or values may be captured
- the asset remains traceable to the PDF page
- later promotion still depends on source class and claim sensitivity

### Structural-learning priority

Classes that should emphasize structural meaning first:

- `defect_photo`
- `process_diagram`

This includes:

- defect identity
- flow sequence
- topology relationship
- routing or return-path concept
- package orientation or spatial relationship

### Default block class

- `branded_poster`

This class is blocked unless a neutral technical sub-region can be isolated and reclassified.

## PDF / Page / Image Reference Contract

Later composition work must be able to trace a learned visual back to:

1. source PDF
2. page number
3. derived local asset path
4. English canonical concept name
5. whether the learning came from exact data or structural context

This is required so future `llm_wiki` writing and blog composition can directly reuse:

- figures
- tables
- formulas
- parameter visuals

without losing provenance or mixing structural illustrations with unsupported numeric claims.

## Operational Guidance For Later Vision Passes

Selective vision work is justified for:

- formula-heavy pages where OCR / text extraction loses symbols
- table pages where column structure matters
- defect plates where image identity matters
- package drawings where geometry or labels matter
- process diagrams where arrows, zones, or topology encode meaning

Selective vision work is not justified for:

- plain text pages
- repeated branded headers / footers alone
- pages whose only visual value is vendor promotion
- low-signal screenshots that do not encode a reusable engineering concept

## Relationship To Existing Intake Logs

This contract extends the governance direction already established in:

- `p4-207`
  - by formalizing class-based image learning actions and branding removal rules
- `p4-208`
  - by turning handbook and vendor-PDF image review into a reusable controller-level learning contract

It also enforces the canonical English concept naming required by the language normalization policy while preserving Chinese PDF provenance locally.

## Current Status

- controller contract status: `drafted_for_execution`
- image/table learning status: `not_started_under_contract`
- reusable local-asset policy: `defined`
- branding-removal policy: `defined`
- provenance-link policy: `defined`

## Next Step

Start a bounded execution pass that classifies extracted page assets into the six asset classes, records required metadata, preserves only de-branded local technical assets, and blocks inseparable branded visuals before any fact-layer or wiki-layer promotion.
