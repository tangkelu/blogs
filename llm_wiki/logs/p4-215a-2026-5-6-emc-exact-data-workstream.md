# P4-215A EMC Exact Data Workstream

Date: 2026-05-06

## Purpose

This workstream opens the first batch-wide exact-data execution lane for EMC-related content inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`

This workstream builds on the existing controller and source-first lanes already established by:

- `logs/p4-209-2026-5-6-emc-handbook-controller-note.md`
- `logs/p4-210a-2026-5-6-emc-source-lane-capacitor-parasitic-resonance.md`
- `logs/p4-210b-2026-5-6-emc-source-lane-common-mode-choke-vs-ferrite-bead.md`
- `logs/p4-212-2026-5-6-via-transition-authority-recovery-integration.md`

Its role is not to reopen broad claim-family learning. Its role is to turn the already-identified EMC formulas, figures, parameter tables, and return-path diagrams into bounded exact-data candidates with image / page traceability and source-mapping recommendations.

## Exact Data Targets

Priority exact-data targets:

- capacitor impedance / ESR / SRF / antiresonance examples
- ferrite bead impedance / current examples
- common-mode choke current / DCR / intended-line-family examples
- via-transition parasitic and return-path vocabulary backed by primary sources

Secondary structural targets:

- filter-topology figures
- return-path continuity diagrams
- split-plane / slot-crossing caution figures
- grounding / suppression relationship diagrams

Blocked targets by default:

- handbook-only capacitor value recipes
- universal placement distances
- handbook formula values without stronger source class
- EMC effectiveness promises

## Page Slices

Primary page clusters from the extracted handbook:

- pages `19-22`
  - capacitor role, filter structures, common-mode choke, ferrite bead
- pages `25-28`
  - parallel capacitor resonance, ESR / ESL effects, storage-capacitor examples
- pages `48-52`
  - transmission-line / impedance / coupled-line figures
- pages `57-62`
  - via, return-path, slot-crossing, and discontinuity figures
- pages `66-69`
  - backplane-adjacent impedance and return-path continuity figures

## Subagent Lanes

### Lane A1: capacitor figures and parameter tables

- page range: `19-20`, `25-28`
- focus:
  - filter capacitor role figures
  - SRF / antiresonance diagrams
  - ESR / ESL discussion tables or figure labels
  - storage-capacitor example values and scope
- expected outputs:
  - candidate `formula_figure` and `parameter_table` inventory
  - exact values or curve labels preserved with page traceability
  - English canonical concept names
  - source-mapping candidates to Murata / TDK / ADI or stronger primary sources
- image understanding required: `yes`

### Lane A2: ferrite bead versus common-mode choke figures and tables

- page range: `21-22`
- focus:
  - common-mode choke frequency-behavior figures
  - ferrite bead versus choke distinction
  - current / DCR / line-family or noise-mode examples
  - filter topology structure on the same pages
- expected outputs:
  - candidate exact-data rows for vendor-scoped examples
  - structural diagrams for later local asset preservation
  - source-mapping candidates to component-vendor primary sources
  - blocked items list for handbook-only or uncited examples
- image understanding required: `yes`

### Lane A3: via-transition diagrams and return-path figures

- page range: `57-62`, `66-69`
- focus:
  - return-path continuity diagrams
  - via-transition parasitic vocabulary
  - discontinuity and split-plane caution figures
  - backplane connector-zone return-path examples
- expected outputs:
  - candidate `structural_context` assets
  - candidate exact-data phrases tied to primary-source-backed boundaries
  - source-mapping recommendations to TI / ADI / NXP style sources
  - unresolved slot-bridging and quiet-ground items kept blocked
- image understanding required: `yes`

## Promotion Targets

This workstream may produce bounded candidates for:

- `sources/registry/methods/*`
- `facts/methods/*`

Potential later aggregation targets:

- `wiki/methods/*`
- `wiki/processes/*`

Each lane must explicitly separate:

- `candidate exact-data rows`
- `candidate structural assets`
- `blocked secondary-PDF-only claims`
- `required stronger authority`

## Output Contract

This workstream must produce:

- local figure / table asset references
- candidate exact-data rows
- candidate source mappings
- candidate fact-card boundaries
- English canonical concept names
- blocked / unresolved claim inventory

## Completion Criteria

This workstream counts as executed only when:

- all three lanes return page-bounded outputs
- every candidate figure / table has source-page and asset-path traceability
- every exact-data candidate is classified under `exact-data-admission-policy.md`
- blocked handbook-only claims remain blocked
- source-mapping recommendations are explicit enough for the next promotion pass

## Current Status

- workstream definition: `defined`
- subagent execution: `round_3_completed`
- lane A1 result log: `logs/p4-215a1-2026-5-6-emc-lane-a1-capacitor-figures-and-parameter-tables.md`
- lane A2 result log: `logs/p4-215a2-2026-5-6-emc-lane-a2-ferrite-bead-vs-common-mode-choke.md`
- lane A3 result log: `logs/p4-215a3-2026-5-6-emc-lane-a3-via-transition-and-return-path-figures.md`
- fact-layer promotion from this workstream: `not_started`

## Next Step

Use `logs/p4-216c-2026-5-6-pcb-pdf-round-3-a3-b3-c3-controller-integration.md` and `logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md` to start EMC promotion review for the strongest curve-recovery and return-path vocabulary candidates.
