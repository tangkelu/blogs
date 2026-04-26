# H2 Drill And Via Geometry Source Map

Date: 2026-04-25

## Purpose

This file maps the current corpus into support classes for the `drill_and_via_geometry` H2 bucket.

It is a governance and source-mapping document.

It is not:

- a source registry record
- a fact card
- a numeric geometry recovery sheet

## Source Classes

### 1. Downgrade / Framing Support

These sources are useful for guarded vocabulary, workflow framing, and claim-splitting.

They do not authorize reusable drill or via geometry numerics.

#### `facts/methods/hdi-microvia-and-vippo-process-posture.md`

- role:
  - downgrade / framing support
- why it is useful:
  - normalizes internal HDI posture around microvia, any-layer build-up, and VIPPO
- why it is limited:
  - explicitly says microvia size, impedance tolerance, and turn-time figures are refresh-sensitive internal claims
  - explicitly says exact drill geometry or stack-up limits must refresh against current engineering data first

#### `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

- role:
  - downgrade / framing support
- why it is useful:
  - keeps HDI build-up, high-layer work, drilling, backdrill, substrate-style fine-line build-up, and stackup planning in one controlled frame
- why it is limited:
  - explicitly marks exact microvia and other capability numbers as refresh-sensitive

#### `sources/registry/internal/frontendapt-pcb-drilling-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - strongest current internal pointer for drilling, controlled-depth backdrill, mechanical and laser drilling, microvia, and PTFE drilling posture
- why it is limited:
  - extraction notes explicitly say exact numeric claims are internal capability framing, not machine-acceptance commitments

#### `sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - clear internal HDI source for any-layer, microvia, VIPPO, and TDR-verified build framing
- why it is limited:
  - all numeric capability claims are refresh-required before external publication

#### `sources/registry/internal/frontendhil-hdi-pcb-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - corroborates HIL-side HDI and microvia posture
- why it is limited:
  - numeric microvia details are refresh-sensitive internal claims

#### `sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - broad internal aggregation point for any-layer HDI, sequential lamination, rigid-flex, VIPPO, and backdrill language
- why it is limited:
  - numeric figures and production scope are internal capability framing only

#### `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - useful for claims where via geometry is blended into multilayer stackup and registration framing
- why it is limited:
  - thickness and feature-size figures are internal claims requiring re-check

#### `sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - HIL-side multilayer route for via-strategy and stackup-complexity language
- why it is limited:
  - process-capability numbers are internal support only

#### `sources/registry/internal/frontendhil-ic-substrate-pcb-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - helps separate substrate-style fine-line build-up and stacked-microvia language from ordinary PCB capability claims
- why it is limited:
  - line/space and microvia values are refresh-sensitive internal claims and should not be generalized back into standard PCB capability

#### `sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - useful internal capability-family pointer for HDI microvia, SBU, any-layer, and fine-line posture
- why it is limited:
  - layer-count, microvia, and line/space details are refresh-sensitive internal claims

### 2. Posture Support

These sources are the strongest current support for how the bucket should be described, bounded, and split.

They support process posture and governance, not reusable numerics.

#### `facts/methods/hdi-microvia-and-vippo-process-posture.md`

- role:
  - posture support
- what it supports safely:
  - HDI can be described as a standard build-up discipline rather than a niche exception
  - microvia, any-layer build-up, and VIPPO belong together in posture language
- what it does not support:
  - any universal microvia, fill, or lamination window

#### `facts/methods/microvia-reliability-public-context.md`

- role:
  - posture support
- what it supports safely:
  - public IPC and NASA material justify caution around stacked microvia, weak interfaces, registration sensitivity, and thermal-stress exposure
  - reliability discussion deserves its own layer
- what it does not support:
  - geometry limits, cycle thresholds, or general manufacturing rules

#### `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`

- role:
  - posture support
- what it supports safely:
  - guarded public vocabulary for `HDI`, `any-layer`, `FRCC`, `RCC`, `ABF`, `BT`, and supplier-side any-layer architecture
  - caution against unsupported inheritance of old `ELIC` blog numbers
- what it does not support:
  - generic geometry tables, lamination-count allowances, or stacked-microvia limits

#### `facts/standards/hdi-design-reference-status-metadata.md`

- role:
  - posture support
- what it supports safely:
  - current-vs-legacy IPC HDI reference hierarchy
  - why old HDI guide values should not be reused as current universal rules
- what it does not support:
  - publishable microvia diameter tables, capture-pad rules, or stacked-height limits

### 3. Non-Claim Boundaries

These sources are valuable because they explicitly say what this repo still cannot claim.

#### `facts/methods/hdi-microvia-and-vippo-process-posture.md`

- boundary value:
  - does not prove every HDI topology is available on every line
  - does not claim any specific microvia, fill, or lamination window is universal

#### `facts/methods/microvia-reliability-public-context.md`

- boundary value:
  - does not provide universal cycle counts, geometry limits, copper-thickness rules, or pass/fail thresholds
  - does not turn paper-specific study setups into general manufacturing requirements

#### `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`

- boundary value:
  - does not support generic any-layer geometry tables, stacked-microvia limits, or shop-level capability promises
  - does not turn supplier wording into current maintained IPC rules or factory capability

#### `facts/standards/hdi-design-reference-status-metadata.md`

- boundary value:
  - does not provide microvia diameter tables, capture-pad rules, aspect-ratio limits, stacked-height limits, or `IST` cycle thresholds

#### `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

- boundary value:
  - exact microvia and other capability numbers are refresh-sensitive
  - advanced-process vocabulary should not collapse into one interchangeable capability claim

#### relevant internal registry records

- boundary value:
  - they repeatedly label exact figures as internal support, refresh-sensitive, or not fit for direct external reuse
- implication:
  - current registry sources help route recovery but do not authorize transferable geometry numerics

### 4. Candidate Upstream Inputs

These are the best current upstream inputs if a future Tier 1 dated capability record is created for this bucket.

They are candidates because they identify likely source families, owning pages, and split dimensions.

They are not themselves the future capability record.

#### primary candidate set

- `sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
  - best current internal drilling anchor for separating mechanical drilling, laser drilling, and controlled-depth drilling posture
- `sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
  - strongest current HDI-side internal anchor for microvia and any-layer build framing
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - best current normalized summary of internal HDI posture and refresh boundary

#### secondary candidate set

- `sources/registry/internal/frontendhil-hdi-pcb-product-page-en.md`
  - useful HIL-side cross-check for HDI geometry scope
- `sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`
  - useful capability-family pointer when HDI geometry is embedded in capability-page language
- `sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - useful aggregation point for broader advanced-process context
- `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - useful where via geometry is buried inside multilayer service framing
- `sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
  - useful HIL-side multilayer cross-check

#### boundary-control candidate set

- `facts/methods/microvia-reliability-public-context.md`
  - needed so reliability papers are not misused as capability proof
- `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`
  - needed so supplier-side any-layer wording is not misused as geometry evidence
- `facts/standards/hdi-design-reference-status-metadata.md`
  - needed so legacy/current IPC references are not misread as publishable geometry tables

## Refresh-Sensitive Or Non-Authorizing Sources

### explicitly refresh-sensitive

- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - microvia size, impedance tolerance, and turn-time figures are refresh-sensitive internal claims
- `facts/methods/microvia-reliability-public-context.md`
  - card itself is marked `must_refresh: true`
- `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`
  - card itself is marked `must_refresh: true`
- `facts/standards/hdi-design-reference-status-metadata.md`
  - card itself is marked `must_refresh: true`
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - exact microvia and related capability numbers must refresh before publishing
- all relevant internal registry records in this bucket
  - extraction or refresh notes treat numeric figures as internal, refresh-sensitive, or support-only

### not valid for reusable drill/via geometry numbers on their own

- all current internal registry records in this bucket
  - they are Tier 3 framing sources, not Tier 1 dated capability records
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - methods posture card, not capability record
- `facts/methods/microvia-reliability-public-context.md`
  - reliability context, not geometry authorization
- `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`
  - boundary card, not capability authorization
- `facts/standards/hdi-design-reference-status-metadata.md`
  - standards-reference metadata, not a rules table or capability record
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - broad process frame, not a numeric capability source

## What Remains Missing

- a Tier 1 dated internal capability record for drill and via geometry
- explicit split between mechanical drill and laser via capability scope
- explicit split between ordinary multilayer PCB capability and substrate-style fine-line / stacked-microvia posture
- explicit ownership and refresh discipline for geometry claims
- a governed bridge from internal capability families to blog-side claim shapes after splitting
- a rule for how hole-family-count, blind-via, buried-via, and stacked-via claims are represented without blending in reliability or standards language

## Recommended Ingestion Order

1. `sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
   - start here because it best exposes the mechanical-drill vs laser-drill split
2. `sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
   - then anchor HDI and microvia language to the right capability family
3. `facts/methods/hdi-microvia-and-vippo-process-posture.md`
   - use next to normalize posture and preserve non-claim boundaries
4. `sources/registry/internal/frontendhil-hdi-pcb-product-page-en.md`
   - use as HIL-side corroboration
5. `sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`
   - use to reconcile capability-page wording and split out posture from numbers
6. `sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
   - then absorb broader advanced-manufacturing context without letting it overwrite split logic
7. `facts/methods/microvia-reliability-public-context.md`
   - bring in boundary control so reliability sources are not misused
8. `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`
   - bring in supplier/public any-layer boundaries
9. `facts/standards/hdi-design-reference-status-metadata.md`
   - finally lock current-vs-legacy IPC reference boundaries before any standards leakage occurs

## Current Source-Map Decision

Current corpus support for `drill_and_via_geometry` is good enough for:

- downgrade-safe HDI and via vocabulary
- posture support for drilling, HDI build-up, and advanced manufacturing framing
- non-claim boundaries around reliability, any-layer marketing, and legacy standards reuse
- routing a future Tier 1 capability-record request

Current corpus support is not good enough for:

- a reusable drill/via geometry fact card
- any transferable minimum drill or laser-via number
- any generic blind/buried/stacked-via geometry table
