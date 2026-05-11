# P4-215C Package And Footprint Exact Data Workstream

Date: 2026-05-06

## Purpose

This workstream opens the exact-data execution lane for package naming, pad / hole structure, and footprint-governance content inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`

This handbook is image-heavy and branding-heavy. The goal is to preserve the valuable package taxonomy, drawing structure, and library-governance logic while blocking vendor-specific defaults and inseparable branded poster surfaces.

## Exact Data Targets

Priority exact-data targets:

- package naming tables
- pad-shape / origin / pin-1 / keepout drawings
- footprint-library governance examples
- hole and pad relationship examples

Priority structural targets:

- package family visual taxonomy
- footprint drawing patterns
- pin-order and origin-layout diagrams

Blocked targets by default:

- exact dimension tables treated as universal without stronger owner / standard authority
- handbook-only keepout thresholds and hole tables treated as standards truth
- vendor-rule checks tied only to branded DFM workflow

## Page Slices

Primary page clusters from extracted text:

- pages `7-15`
  - package naming rules and examples
- pages `22-24`
  - pad, via, flash, irregular-pad, drill, and hole / pin relationships
- pages `25-28`
  - lead-compensation and SMD package drawing pages
- pages `29-30`
  - basic package-design requirements, origin, pin-order, keepout, standard-hole table
- pages `36-40`
  - footprint checking, pad / lead review, and DFM-adjacent inspection examples

## Subagent Lanes

### Lane C1: package taxonomy and naming pages

- page range: `7-15`
- focus:
  - package-family taxonomy
  - naming examples
  - package-class normalization into English
  - package-example tables or list structures
- expected outputs:
  - candidate package taxonomy rows
  - English canonical concept names
  - blocked vendor-specific naming claims if any
  - local asset candidates for package family illustrations
- image understanding required: `yes`

### Lane C2: pad / origin / pin-1 / keepout drawing pages

- page range: `22-30`
- focus:
  - pad and drill relationship examples
  - origin and pin-order drawings
  - keepout and hole-table structures
  - dimension-bearing footprint figures
- expected outputs:
  - `package_footprint_drawing` inventory
  - exact-data candidates versus blocked dimension tables
  - provenance-linked local asset paths
  - source-mapping recommendations for any authority-sensitive rules
- image understanding required: `yes`

### Lane C3: library-governance and hole / pad example pages

- page range: `36-40`
- focus:
  - footprint review examples
  - lead / pad matching logic
  - library-governance checklist structures
  - branded DFM references that must stay blocked
- expected outputs:
  - candidate governance rows
  - structural-context assets for review examples
  - blocked branded-rule inventory
  - candidate fact-card boundaries for package-library governance
- image understanding required: `yes`

## Promotion Targets

This workstream is expected to support:

- `sources/registry/components/*`
- `facts/components/*`
- `facts/design-rules/*`

Potential later aggregation target:

- `wiki/processes/*` or `wiki/components/*` for package-library governance

Promotable posture:

- package-family taxonomy is promotable
- footprint-governance examples are promotable
- exact dimension tables stay blocked unless sourced from stronger owner / standard references

## Output Contract

This workstream must produce:

- package taxonomy candidates
- local drawing / figure asset references
- candidate exact-data rows
- candidate governance boundaries
- English canonical concept names
- blocked vendor-specific or dimension-sensitive claim inventory

## Completion Criteria

This workstream counts as executed only when:

- all three lanes return page-bounded outputs
- every preserved figure has local asset-path traceability
- package taxonomy is separated from vendor-specific rule tables
- dimension-sensitive claims are explicitly classified under `exact-data-admission-policy.md`
- blocked branding contamination is documented

## Current Status

- workstream definition: `defined`
- subagent execution: `round_3_completed`
- lane C1 result log: `logs/p4-215c1-2026-5-6-package-lane-c1-package-taxonomy-and-naming.md`
- lane C2 result log: `logs/p4-215c2-2026-5-6-package-lane-c2-pad-origin-pin1-keepout-drawings.md`
- lane C3 result log: `logs/p4-215c3-2026-5-6-package-lane-c3-library-governance-and-hole-pad-examples.md`
- promoted package / footprint exact-data facts: `not_started`

## Next Step

Use `logs/p4-216c-2026-5-6-pcb-pdf-round-3-a3-b3-c3-controller-integration.md` and `logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md` to start package-library governance promotion review with branded UI assets still blocked by default.
