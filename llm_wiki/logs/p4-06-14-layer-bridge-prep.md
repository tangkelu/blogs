# P4-06 14-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note prepares the current `14-layer` layer-count blog for second-wave `P4-06` evidence-pack use.

It does not:

- rewrite the blog
- unlock standards-threshold or rigid-flex reliability numerics
- approve fabrication-capability tables

Its purpose is to define the strictest governed bridge posture for future prompt execution against:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/14-layer-pcb-manufacturing.md`

## Template Choice

Default template choice:

- `prompts_template/shared/query.md`

Required supporting templates:

- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/hilpcb/query-overlay.md`

Reason:

- `14-layer` remains the riskiest branch in the second safe bridge wave
- the page mixes `C` standards-threshold leakage, `B` fabrication-capability tables, and `E` rigid-flex reliability numerics more densely than `12-layer` or `16-layer`
- it is still closer to a decision page than a pillar page, but it needs the strictest section-level pruning of the three

## Scope

In scope for this prep note:

- the current blog at `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/14-layer-pcb-manufacturing.md`
- second-wave conservative bridge preparation only
- section-level keep / downgrade / delete / needs-source rules for future evidence-pack assembly
- safe fact / source candidates already present in `llm_wiki`

Out of scope:

- standards-threshold recovery
- rigid-flex reliability numeric recovery
- fabrication-capability numeric recovery
- lead-time refresh work
- readiness upgrade beyond conservative prompt bridging

## Conservative Readiness Verdict

`14-layer` is suitable for `second-wave conservative bridge-prep` only under the heaviest pruning of the second-wave set.

It is not suitable for high-numeric-density evidence-pack use.

Current posture:

- bridge-prep verdict: `allowed with very heavy pruning`
- readiness verdict: remains `mostly_ready` for conservative rewriting only
- main blocker classes: `C` standards-threshold leakage, `B` fabrication-capability numerics, and `E` rigid-flex reliability numerics

## Allowed Claim Classes

Allowed in the usable evidence pack:

- `A` official material datasheet numerics when tied to exact flex / rigid-flex / digital-material product or class sources
- non-numeric rigid-flex construction posture
- non-numeric high-layer and transition-zone planning posture
- non-numeric manufacturability framing around structure choice, stack symmetry, and process review

Allowed only as downgraded wording, not as retained numerics:

- representative rigid-flex architectures such as `14R-4F` as examples only
- flex-material selection as class framing rather than numeric cookbook guidance
- process complexity wording around drilling, coverlay, and transition zones without numeric thresholds

## Excluded Claim Classes

Do not allow these into the usable pack:

- `B` fabrication capability numerics such as fine-line rules, transition-zone tolerances, via geometry, aspect ratio, adhesion values, drilling speeds, or capability banners
- `C` standards / qualification / acceptance numerics such as `Class 2 / Class 3`, registration / annular-ring threshold tables, or compliance-style banners
- `D` board-level outcome numerics and performance multipliers
- `E` rigid-flex reliability numerics such as bend radius, flex-life cycle tables, and rigid-flex recipe defaults
- `F` dynamic commercial numerics such as `7 business days`
- `G` unsupported contextual numerics that function as hidden assurance proof

Specific exclusions from the current blog:

- `IPC-6013 Type 3/4`
- `±4mil`, `±2mil`
- `Class 2 = 1mil`, `Class 3 = 2mil`
- `0.3mm` to `0.5mm`
- `6` cores, `5` prepreg layers, `2.0-2.5mm`, `90-120 minutes`
- `10-12` inner layers, `1-2` buildup layers per side
- `12.5-75μm`, `12.5-50μm`, `25-75μm`
- `20-30%` slower feed, `100,000+ RPM`
- `2-3 lb/in`, `6-8 lb/in`, `8+ lb/in`
- `3-5mm`
- `6×`, `12×`, `20-25×`
- `1-100 cycles`, `>100,000 cycles`
- `10mil`, `30mil`, `30-40%`
- `2.0-2.4mm`, `10:1`, `0.20-0.24mm`
- `3/3mil`, `2.5/2.5mil`
- `288°C, 6 cycles`
- `7 business days`

## Must-Refresh Handling

Future prompt execution must mark `must_refresh: true` for any item that depends on:

- live compliance / certification posture
- capability banners
- turnaround claims
- any current qualification assertion

Default bridge rule:

- if a claim would require refresh and lacks a governed `fact_id` plus stable `source_id`, exclude it from the usable pack

## Candidate `fact_id` Set

Primary candidate facts for a conservative pack:

- `materials-flex-polyimide-and-lcp-class-source-coverage`
- `materials-high-speed-digital-material-ladder-normalization`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-high-layer-rigid-board-manufacturability-context`
- `methods-hdi-microvia-and-vippo-process-posture`
- `standards-ipc-rigid-flex-and-microvia-reliability-metadata`
- `standards-hdi-design-reference-status-metadata`

Usable as wiki/topic notes, not atomic facts:

- `materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries`
- `processes-advanced-pcb-fabrication-and-stackup-planning`

## Candidate `source_id` Set

Primary candidate source IDs for the conservative pack:

- `panasonic-felios-series-page`
- `panasonic-felios-lcp-page`
- `panasonic-felios-frcc-page`
- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`
- `frontendapt-rigid-flex-pcb-capability-page-en`
- `frontendapt-pcb-flex-pcb-page-en`
- `frontendhil-flex-pcb-product-page-en`
- `frontendapt-flex-pcb-capability-page-en`
- `frontendapt-pcba-flex-rigid-flex-page-en`
- `ipc-2226a-hdi-standard-page`
- `ipc-2315-legacy-hdi-guide-page`

## Section-By-Section Bridge Guidance

### 1. Intro, title, and capability banner

Allow:

- `14-layer` as a board class where rigid, flex, and dense routing constraints can become tightly coupled
- qualitative framing around architecture complexity

Exclude:

- compliance or capability banners
- `IPC-6013 Type 3/4`
- all tolerance and turnaround numerics

### 2. Core stackup and lamination sections

Allow:

- the qualitative point that higher layer counts drive more stackup planning and process coordination
- rigid versus flex branch separation

Exclude:

- core / prepreg counts
- build-up counts
- thickness windows
- press-time tables

### 3. Standards, registration, and annular-ring sections

Allow:

- only the non-numeric point that standards and acceptance language should not be improvised from draft prose

Exclude:

- all `Class 2 / Class 3` tables
- registration thresholds
- annular-ring thresholds
- any section that attempts to restate standards numerics as factory guidance

### 4. Flex and polyimide material sections

Allow:

- polyimide / LCP / flex-material class framing
- exact material numerics only where a current official source clearly supports them

Exclude:

- unsupported thickness ladders copied from draft prose
- drilling-speed or adhesion numbers
- generalized material-performance multipliers

### 5. Transition-zone, bend-radius, and reliability sections

Allow:

- non-numeric rigid-flex transition planning posture
- the statement that bend reliability and transition design require dedicated review

Exclude:

- bend-radius tables
- flex-life cycle tables
- transition-zone tolerance numerics

### 6. Fine-feature, via-geometry, and closing sections

Allow:

- non-numeric statement that dense rigid-flex routing and via strategy require process review

Exclude:

- fine-line tables
- via-geometry tables
- aspect-ratio numerics
- `288°C, 6 cycles`
- `7 business days`

## Open Gaps That Stay Controlled

- standards-threshold leakage remains the main delete-class risk
- fabrication-capability numerics remain `needs_source`
- rigid-flex reliability numerics remain blocked rather than softened into pseudo-thresholds
- dynamic commercial numerics remain excluded

## Stop Conditions

Do not assemble a future `14-layer` evidence pack if any of the following remain true:

- standards tables are still present in any usable section
- rigid-flex reliability numerics still survive in bend / transition sections
- capability banners or turnaround claims remain in the usable pack
- flex-material prose is still carrying unsupported thickness, drilling, or adhesion numeric ladders

## Current Decision

`14-layer` may enter second-wave `P4-06` evidence-pack assembly only under:

- explicit deletion of `C` standards-threshold content
- explicit hold of `B` fabrication-capability tables at `needs_source`
- explicit downgrade of rigid-flex architecture to non-prescriptive examples
