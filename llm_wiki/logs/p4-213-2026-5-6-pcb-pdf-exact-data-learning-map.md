# P4-213 `PCB资料` PCB PDF Exact-Data Learning Map

Date: 2026-05-06

## Purpose

This controller log defines a batch-wide `exact-data learning map` for the handbook-led PDF batch under:

- `/code/blogs/tmps/PCB资料`

User intent is explicit: future blog writers should eventually be able to directly reuse `formulas`, `parameter data`, `tables`, and `figures` discovered in these PDFs.

That reuse is allowed only after controlled learning into the canonical `llm_wiki` storage surface. This document is a planning and routing artifact. It is not a claim that the batch is already learned, normalized, or safe for direct numeric reuse.

## Alignment Context

This map aligns with:

- `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
- `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
- `llm_wiki/logs/p4-209-2026-5-6-emc-handbook-controller-note.md`
- `llm_wiki/logs/p4-211-2026-5-6-emc-source-first-authority-recovery-integration.md`
- `llm_wiki/logs/p4-212-2026-5-6-via-transition-authority-recovery-integration.md`
- `llm_wiki/policies/language-normalization-and-indexing.md`

Key governing consequences from those references:

- PDF content begins as `claim inventory`, not authority
- figure/table-heavy pages may justify selective visual analysis
- reusable knowledge storage must be English-only under:
  - `sources/registry/`
  - `facts/`
  - `wiki/`
- direct handbook or secondary-PDF numerics must not bypass source qualification

## Scope

This map covers the batch-wide exact-data learning problem across these reusable families:

1. `EMC component and suppression data`
2. `transmission-line / via-transition / return-path data`
3. `safety spacing and insulation-distance data`
4. `PCBA inspection and defect-taxonomy data`
5. `package / footprint / library-governance data`

This map does not complete those lanes. It defines how they should be learned, split, promoted, and blocked.

## Core Exact-Data Rule

Exact data from PDFs may become reusable only through a controlled promotion path:

1. identify the exact data family and source page cluster
2. classify whether the PDF is primary enough, secondary-but-usable, or blocked pending authority recovery
3. normalize the reusable concept into English
4. land the qualified evidence in `sources/registry/`
5. land bounded reusable statements in `facts/`
6. aggregate cross-source operating guidance in `wiki/` only after enough fact support exists

Until that happens, the PDF remains:

- useful for demand discovery
- useful for topic routing
- useful for figure/table candidate selection
- not yet safe for direct prompt consumption as exact authority

## Exact Data Versus Blocked Secondary Claims

### Promotable exact-data classes after controlled learning

These are the classes this map intends to recover and preserve:

- formulas with stable engineering meaning and identifiable source scope
- parameter definitions and bounded parameter relationships
- neutral tables of technical categories, defect classes, package classes, or standards-mapped fields
- figure structures that encode reusable engineering relationships
- inspection or taxonomy plates whose value is categorical, not purely promotional
- standards-linked spacing, insulation, or workmanship metadata when tied to real authority
- vendor-backed component selection boundaries when clearly scoped as vendor guidance, not universal law

### Blocked secondary-PDF claim classes

These remain blocked unless upgraded by stronger authority:

- universal numeric rules copied from handbook prose
- compliance or pass/fail claims inferred from design examples
- capability promises, yield claims, or acceptance guarantees
- cookbook selection rules presented without scope or test conditions
- supplier- or platform-specific tables reused as if they were general industry defaults
- old heuristic thresholds presented as modern universal boundaries
- exact figures with embedded branding that cannot be cleanly neutralized
- standards-equivalent acceptance criteria copied from secondary summaries instead of governed sources

## Likely PDF Origins By Exact-Data Family

### 1. EMC component and suppression data

Likely main origin:

- `【PCB必备】85页-PCB设计EMC设计指导书.pdf`

Likely subfamilies:

- capacitor role / parasitic / resonance framing
- ferrite bead versus common-mode choke boundary
- low-pass topology identity
- grounding and suppression vocabulary
- figure/table candidates for filter structures and component behavior

Current batch posture from prior logs:

- claim-family intake completed
- first source-first recovery already started for narrow EMC sublanes
- exact-data promotion still partial and deliberately bounded

### 2. Transmission-line / via-transition / return-path data

Likely main origins:

- `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `【PCB必备】194页-PCB设计规范经验之书.pdf`

Likely subfamilies:

- microstrip / stripline vocabulary
- characteristic-impedance comparison framing
- via-transition and return-path continuity
- slot-crossing / split-plane / connector-adjacent routing figures
- interface-specific routing tables or geometry examples

Batch posture:

- `85页` already opened the demand map
- narrow via-transition recovery already partially integrated
- exact formulas and geometry tables remain blocked unless tied to stronger authority

### 3. Safety spacing and insulation-distance data

Likely main origins:

- `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `【PCB必备】194页-PCB设计规范经验之书.pdf`
- secondary vendor article cluster under `/code/blogs/tmps/PCB资料/PCB文章` for discovery only

Likely subfamilies:

- creepage / clearance / insulation-distance language
- current-carrying appendix tables
- board-edge, slot, and isolation spacing figure candidates

Batch posture:

- current material is useful for demand discovery
- exact safety spacing cannot be promoted from handbook or article summaries alone
- standards-governed source recovery is required before fact-layer landing

### 4. PCBA inspection and defect-taxonomy data

Likely main origin:

- `【PCB必备】158页-PCBA检验规范汇总.pdf`

Likely subfamilies:

- solder defect taxonomy
- component orientation and placement defect classes
- cleanliness, warpage, jumper-wire, SMT/THT workmanship categories
- defect example images and inspection vocabulary
- process-stage-to-defect-family mappings

Batch posture:

- highest-value taxonomy lane after EMC
- likely strong candidate for exact categorical reuse
- accept/reject thresholds and standards-equivalent judgments remain blocked until authority class is verified

### 5. Package / footprint / library-governance data

Likely main origins:

- `【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- `【PCB必备】194页-PCB设计规范经验之书.pdf`

Likely subfamilies:

- package naming taxonomy
- footprint library governance
- pad, pin-order, origin, keepout, and hole-table structures
- schematic-symbol to footprint governance language
- package-example figures that can be selectively neutralized

Batch posture:

- structurally rich for exact-data extraction
- branding and vendor-rule contamination are more likely
- exact rule tables must be split into neutral taxonomy versus blocked vendor-specific defaults

## First-Wave Exact-Data Ranking

The batch-wide first-wave order is:

1. `EMC component and suppression data`
2. `PCBA inspection and defect-taxonomy data`
3. `package / footprint / library-governance data`
4. `safety spacing and insulation-distance data`
5. `transmission-line / via-transition / return-path data`

## Why This Ranking Holds

### 1. EMC component and suppression data

Reason:

- strongest existing controller groundwork already exists from `P4-209`, `P4-211`, and `P4-212`
- clear user demand for reusable formulas, figures, and parameter language
- several narrow lanes are already separated enough for controlled promotion

### 2. PCBA inspection and defect-taxonomy data

Reason:

- the `158页` handbook likely contains high-density exact categorical data
- defect-taxonomy reuse is highly valuable for future blog writing
- taxonomy can often be promoted more safely than hard acceptance numerics

### 3. Package / footprint / library-governance data

Reason:

- the `42种` handbook likely contains reusable structure and library-governance mappings
- exact package family indexing benefits from English normalization
- more branding contamination exists, but the knowledge value is still high

### 4. Safety spacing and insulation-distance data

Reason:

- high downstream value
- high governance risk
- must be standards-anchored before reuse

### 5. Transmission-line / via-transition / return-path data

Reason:

- technically important, but the hardest family to promote safely from secondary PDFs
- formulas and geometry tables are especially prone to overclaiming when copied out of context
- current corpus already has some narrow support, so urgency is lower than the first three exact-data families

## Promotion Targets Across The Canonical Knowledge Layer

### `sources/registry/`

Use for:

- English-normalized records for handbook-derived exact-data lanes that have been upgraded by acceptable authority
- manufacturer application-note records
- standards metadata records
- clearly scoped vendor guides used as vendor-boundary evidence
- figure/table provenance records where the exact visual structure matters

Expected landing patterns:

- `sources/registry/methods/*`
- `sources/registry/testing/*`
- `sources/registry/components/*`
- `sources/registry/standards/*` where appropriate

### `facts/`

Use for:

- bounded exact-data statements with clear scope
- formula identity cards
- parameter-definition and parameter-relationship cards
- defect-taxonomy cards
- package/footprint governance boundary cards
- exact-data consumption boundaries that tell future writers what can and cannot be reused

Expected landing patterns:

- `facts/methods/*`
- `facts/testing/*`
- `facts/components/*`
- `facts/design-rules/*`

### `wiki/`

Use for:

- aggregated reusable topic pages only after enough fact support exists
- cross-source synthesis that helps blog writers apply exact data correctly
- structured topic maps that link formulas, tables, figures, and blocked boundaries together

Expected landing patterns:

- `wiki/methods/*`
- `wiki/testing/*`
- `wiki/processes/*`
- `wiki/components/*`

## English-Only Canonical Storage Requirement

Per `language-normalization-and-indexing.md`:

- `logs/` may preserve Chinese provenance and operator-facing context
- reusable files under `sources/registry/`, `facts/`, and `wiki/` must use English-only canonical naming and retrieval identifiers
- Chinese PDF titles remain valid as provenance
- reusable concepts must normalize to English before promotion

Examples of what this means operationally:

- Chinese defect labels may appear in intake logs, but the promoted taxonomy file must use English canonical terminology
- Chinese package or EMC terms can be quoted for provenance, but the reusable fact and wiki entry must index under English concepts
- no parallel Chinese and English fact files should be created for the same concept

## Controlled Learning Model For Exact Data

### Phase 1: exact-data inventory

Per handbook or lane, identify:

- formulas present
- table families present
- figure families present
- parameter classes present
- likely contamination or risk class
- likely authority gap

Output class:

- `logs/` only

### Phase 2: authority qualification

For each exact-data candidate, decide:

- `promotable_from_scoped_vendor_authority`
- `promotable_only_from_standard_or_primary_authority`
- `taxonomy_only`
- `blocked_secondary_pdf_only`

Output class:

- `logs/`
- later `sources/registry/`

### Phase 3: exact-data landing

Land only the qualified subset into:

- `sources/registry/`
- `facts/`

Use exact wording that preserves scope, conditions, and source class.

### Phase 4: writer-facing aggregation

Once enough fact support exists, create or update:

- `wiki/` pages
- exact-data consumption boundaries
- figure/table reuse guidance

## Suggested Wave Split

### Wave 1A: EMC component and suppression exact-data lanes

Priority lanes:

- capacitor parasitic / resonance / role exact-data map
- ferrite bead versus common-mode choke exact-data map
- low-pass filter topology exact-data map
- grounding and suppression-figure map

Expected outcome:

- partial `source_backed_fact_layer` with strong blocking around universal rules

### Wave 1B: PCBA inspection and defect-taxonomy exact-data lanes

Priority lanes:

- solder defect families
- orientation / polarity / placement defect families
- cleanliness / contamination / warpage / jumper-wire families
- defect-image taxonomy and selective figure reuse map

Expected outcome:

- strong `taxonomy_first` promotion potential
- blocked acceptance numerics until standards class is confirmed

### Wave 1C: package / footprint / library-governance exact-data lanes

Priority lanes:

- package naming and family normalization
- pad / keepout / origin / pin-order governance
- library-review checklist extraction
- table and footprint-figure candidate map

Expected outcome:

- mix of `taxonomy_first` and `vendor_rule_blocked` output

### Later waves

- safety spacing / insulation-distance authority lane
- transmission-line / via / return-path exact-formula lane
- figure-specific recovery where diagram structure adds value beyond text extraction

## Explicit Non-Completion Boundary

This document does not claim that:

- the `PCB资料` batch is fully learned
- handbook tables are already safe to quote
- formulas are already canonicalized
- figures are already neutralized and reusable
- exact numeric rules are already approved for prompt consumption

It defines the execution map needed to reach that state.

## Current Status

- batch-wide exact-data learning map: `defined_not_executed`
- EMC exact-data recovery: `partially_opened`
- PCBA inspection exact-data recovery: `not_started`
- package / footprint exact-data recovery: `not_started`
- safety spacing exact-data recovery: `not_started`
- transmission-line / via / return-path exact-data recovery: `partially_opened_but_not_formula_ready`

## Next Step

Open the first formal exact-data controller lane for:

1. `EMC component and suppression exact-data`
2. then `PCBA inspection and defect-taxonomy exact-data`
3. then `package / footprint / library-governance exact-data`

That controller should split each family into:

- `promotable exact data`
- `blocked secondary-PDF claims`
- `required authority recovery`
- `figure/table candidates`
- `English canonical landing targets`

## Final Status Labels

- exact-data map status: `defined_not_executed`
- batch claim-family intake status: `already_available_from_P4-207_to_P4-212`
- canonical promotion status: `not_started_at_batch_wide_exact_data_level`
- recommended next action: `open_wave_1_exact_data_controller`
