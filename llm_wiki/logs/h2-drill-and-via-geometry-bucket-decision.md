# H2 Drill And Via Geometry Bucket Decision

Date: 2026-04-25

## Purpose

This file defines the current governance decision for the `drill_and_via_geometry` H2 bucket.

It is a bucket-level policy and readiness note.

It is not:

- a fact card
- a numeric recovery sheet
- approval to publish drill or via geometry values from current prose sources

## Why `drill_and_via_geometry` Is A Top H2 Bucket

- It appears across multiple high-risk layer-count blogs, especially `8-layer`, `10-layer`, `12-layer`, `14-layer`, `18-layer`, and `20-layer`.
- It sits at the intersection of rigid multilayer capability, HDI build-up vocabulary, and high-density routing claims, so weak handling here creates overclaiming fast.
- H0 already shows that many blog sections collapse `minimum drill`, `laser via`, `blind/buried via`, `stacked-via`, `hole-family-count`, and architecture examples into one unsupported capability cluster.
- H2 inventory already marked this bucket as high priority and explicitly warned against mixing ordinary rigid-board capability with HDI-specific process windows.

## In-Scope Claims

These claim shapes belong inside this bucket when they are presented as current fabrication capability numerics:

- minimum mechanical drill
- minimum laser via
- blind-via or buried-via geometry windows
- stacked-via or skip-via geometry windows
- hole-size-count limits when framed as manufacturability capability
- via-family geometry bundled into HDI service claims
- via-related capability numbers embedded in DFM checklists, capability banners, or quote-style summaries

## Excluded Claims

These do not belong in `drill_and_via_geometry` recovery, even when they mention holes or vias:

- HDI vocabulary without a numeric capability claim
  - examples: `1+N+1`, `any-layer`, `VIPPO`, `SBU`, `ELIC`
- reliability or qualification thresholds
  - examples: stacked-microvia robustness claims, `IST` cycle claims, reflow-cycle claims
- standards or design-reference geometry tables
  - examples: IPC-derived capture-pad tables, legacy guide values, class-threshold restatements
- board-level SI or package-context numbers
  - examples: BGA pitch or channel-performance numerics used as capability proof
- stackup recipe counts or lamination defaults
  - those belong to separate H2/H3 handling
- dynamic commercial or lead-time claims

## Current Corpus Support

Current corpus support is useful for posture, claim-splitting, and downgrade boundaries, but not for reusable geometry numerics.

What is currently strong enough:

- internal HDI pages consistently frame microvia, any-layer build-up, and VIPPO as part of HDI process posture
- public IPC / NASA / supplier-side materials and any-layer records support cautionary context around microvia reliability and legacy-vs-current HDI reference status
- internal advanced-manufacturing and drilling pages identify which process families belong together: mechanical drilling, laser drilling, backdrill, VIPPO, HDI build-up, and substrate-style fine-line work

What is not currently strong enough:

- a transferable minimum mechanical-drill number
- a transferable minimum laser-via number
- a reusable blind / buried / stacked-via geometry table
- a universal any-layer geometry default
- a shop-wide via-family capability card

## Non-Claim Boundaries

Current corpus already gives several important non-claim boundaries:

- `methods-hdi-microvia-and-vippo-process-posture`
  - does not prove every HDI topology is available on every line
  - does not claim any specific microvia, fill, or lamination window is universal
- `methods-microvia-reliability-public-context`
  - does not provide universal cycle counts, geometry limits, copper-thickness rules, or pass/fail thresholds
  - does not turn public method names or papers into general manufacturing requirements
- `methods-any-layer-hdi-public-boundary-for-20-layer`
  - does not support generic any-layer geometry tables or stacked-microvia limits
  - does not turn supplier-side architecture wording into factory capability
- `standards-hdi-design-reference-status-metadata`
  - does not provide microvia diameter tables, capture-pad rules, aspect-ratio limits, or stacked-height limits
- `processes-advanced-pcb-fabrication-and-stackup-planning`
  - treats exact microvia or other internal capability numbers as refresh-sensitive and not fit for direct publication

## Blocker Statement

The blocking issue is unchanged:

- there is no Tier 1 dated capability record in the current corpus for `drill_and_via_geometry`
- current internal pages are Tier 3 framing sources, not reusable capability evidence
- current public IPC/NASA/supplier sources help define vocabulary and caution boundaries, but they do not authorize this repo to publish shop-level geometry numerics

Until a Tier 1 dated capability record exists, no `drill_and_via_geometry` fact card should be created.

## Claim-Splitting Rule

Every incoming claim in this bucket must be split before disposition.

### split A: mechanical drill

- use when the claim is about ordinary drilled-hole capability in rigid multilayer production
- do not mix with laser-via or HDI build-up claims

### split B: laser via

- use when the claim is specifically about laser-drilled microvia capability
- keep separate from through-hole mechanical drilling

### split C: HDI vocabulary

- use when the claim is really architecture or process language, not a numeric limit
- examples:
  - `any-layer`
  - `1+N+1`
  - `VIPPO`
  - `SBU`
- default handling:
  - `downgrade` into vocabulary or posture wording if the numeric layer is unsupported

### split D: reliability context

- use when geometry claims are tied to stacked-microvia life, thermal stress, `IST`, or field-failure caution
- default handling:
  - keep as guarded reliability context only if numerics are removed
  - otherwise block from H2

### split E: standards geometry tables

- use when the claim depends on IPC or legacy design-guide geometry tables, capture-pad tables, or current-vs-legacy design-rule framing
- default handling:
  - `delete` or hold for later standards workstream

## Disposition Guidance For Common Claim Shapes

### exact minimum mechanical-drill number from internal page only

- disposition:
  - `needs_source`
- reason:
  - internal support page without Tier 1 dated capability record

### exact minimum laser-via number from internal HDI page only

- disposition:
  - `needs_source`
- reason:
  - same blocker; current page is framing only

### `1+N+1`, `2+N+2`, `any-layer`, `VIPPO`, `ELIC` with implied geometry promise

- disposition:
  - `downgrade`
- reason:
  - safe as architecture vocabulary, unsafe as transferable geometry default

### stacked-microvia or sequential-build-up number justified by reliability papers or public warning material

- disposition:
  - `delete` for capability reuse
- reason:
  - reliability context does not prove current shop geometry capability

### IPC or legacy HDI design-reference geometry values presented as general rules

- disposition:
  - `delete`
- reason:
  - standards/design-reference geometry tables are excluded from H2 capability promotion

### public supplier-side any-layer or build-up-material wording without shop-specific geometry scope

- disposition:
  - `downgrade`
- reason:
  - useful for guarded vocabulary only

### mixed cluster combining drill size, via geometry, lamination count, and cost

- disposition:
  - split claim first
  - geometry portions: `needs_source`
  - architecture vocabulary portions: `downgrade`
  - commercial portions: `delete`

## Per-Blog Impact Summary

### `6-layer`

- effect:
  - via-rule and tolerance sections remain blocked wherever hole geometry is implied as current capability
- practical result:
  - keep generic multilayer drilling posture only; no geometry numerics

### `8-layer`

- effect:
  - HDI / via / aspect-ratio / pitch clusters remain source-blocked
- practical result:
  - architecture and process wording can survive after downgrade, but geometry numbers stay out

### `10-layer`

- effect:
  - blind-via geometry and `1+8+1` / `2+6+2` capability bundles must be split
- practical result:
  - topology labels may remain as vocabulary; exact geometry stays `needs_source`

### `12-layer`

- effect:
  - drill-program and hole-family sections remain blocked where they imply reusable via capability
- practical result:
  - keep workflow framing only; no via-geometry table restoration

### `14-layer`

- effect:
  - via-geometry and dense DFM rule clusters remain one of the heaviest blocked areas
- practical result:
  - this blog stays high risk until the bucket gets real Tier 1 support

### `16-layer`

- effect:
  - via geometry is less central than process-window claims, but any embedded hole-rule numerics remain blocked
- practical result:
  - no geometry promotion from power or heavy-copper sections

### `18-layer`

- effect:
  - any high-layer via-strategy claim stays posture-only unless scoped to a future capability record
- practical result:
  - conservative rewrites remain possible, not geometry-number recovery

### `20-layer`

- effect:
  - this bucket is a major blocker because the article still leans on unsupported any-layer, stacked-microvia, and geometry-table language
- practical result:
  - H2 cannot unlock `20-layer` geometry numerics without Tier 1 capability evidence plus separate reliability and standards controls

### `22-layer`

- effect:
  - bucket impact is secondary but still relevant where via geometry overlaps qualification or standards language
- practical result:
  - default to exclusion when geometry claims are wrapped in class/compliance framing

### `24-layer`

- effect:
  - not the primary blocker, but any high-density via claim still requires the same split-and-hold discipline
- practical result:
  - no drift from high-speed or high-layer posture into geometry promises

## Exact Next-Step Requirements Before Any Fact Card Could Exist

All of the following must be true before a `drill_and_via_geometry` fact card exists:

1. a Tier 1 dated internal capability record exists
   - it must be explicitly date-stamped and scoped to line family, plant family, region, or release context
2. mechanical drill and laser via are separated
   - no blended “minimum drill” record spanning ordinary multilayer and HDI microvia
3. architecture vocabulary is separated from numeric capability
   - `any-layer`, `VIPPO`, `SBU`, `1+N+1`, and related terms must not carry implied numeric defaults
4. reliability context is separated from capability numerics
   - public microvia-reliability or `IST` context cannot be used as numeric evidence
5. standards geometry references are filtered out
   - no legacy or current IPC design-reference tables are reused as capability proof
6. provenance and refresh fields are defined
   - source owner, scope, refresh rule, and expiry discipline must be explicit
7. blog claim shapes are remapped by split bucket
   - each affected blog claim must be labeled as `keep`, `downgrade`, `delete`, or `needs_source` after splitting

## Current Bucket Decision

`drill_and_via_geometry` remains a high-priority but blocked H2 bucket.

Current corpus is sufficient for:

- posture support
- downgrade-safe vocabulary
- non-claim boundaries
- future capability-record routing

Current corpus is not sufficient for:

- any reusable drill or via geometry fact card
- any transferable minimum drill or laser-via number
- any generic HDI / any-layer geometry table
