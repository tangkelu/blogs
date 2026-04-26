# H2 Aspect Ratio Source Map

Date: 2026-04-25

## Purpose

This file maps the current corpus for the `aspect_ratio` bucket into support classes before any numeric recovery attempt.

It is a source-governance map, not a fact card and not a source record.

## Current Classification

### Downgrade / Framing Support

Use these for guarded non-numeric wording only:

- `facts/methods/high-layer-count-backdrill-and-registration-posture.md`
  - supports coupled-process framing around registration, sequential lamination, and drilling sensitivity
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - supports HDI architecture and microvia-process vocabulary
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - supports separation of HDI, high-layer, impedance, and process-route planning

These can justify wording such as:

- `more drilling-sensitive`
- `requires tighter manufacturability planning`
- `high-layer and HDI structures should not be treated as commodity defaults`

They do not justify numeric aspect-ratio reuse.

### Posture Support

Use these to identify the relevant capability family and where future numeric recovery would have to come from:

- `sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
- `sources/registry/internal/frontendapt-pcb-high-layer-count-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
- `facts/methods/high-layer-rigid-board-manufacturability-context.md`

These support:

- drilling posture
- high-layer manufacturability posture
- HDI-vs-rigid distinction
- process sensitivity and handling context

They do not authorize a reusable aspect-ratio number.

### Non-Claim Boundaries

Use these to block overreach:

- `sources/registry/standards/ipc-2226a-hdi-standard-page.md`
  - current HDI standard identity and scope framing only
- `sources/registry/standards/ipc-2315-legacy-hdi-guide-page.md`
  - legacy guide identity only
- `sources/registry/standards/mil-prf-31032-1e-rigid-multilayer-thermosetting-spec-sheet-page.md`
  - rigid-multilayer military sheet identity and scope only
- `sources/registry/materials/ats-hdi-anylayer-page.md`
  - any-layer architecture vocabulary only
- `sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - named-construction process-discipline context only

These sources help say what the bucket is not:

- not a standards-threshold bucket
- not a microvia-reliability bucket
- not a material-processing recipe bucket
- not an any-layer architecture bucket

### Candidate Upstream Inputs

Current candidate upstream inputs are narrow and still non-authorizing until converted into a dated capability record:

- `frontendapt-pcb-drilling-page-en`
  - best current internal pointer for drilling posture and aspect-ratio-related vocabulary
- `frontendapt-pcb-high-layer-count-pcb-page-en`
  - best current internal pointer for high-layer routing and drilling-sensitive execution posture
- `frontendapt-pcb-multilayer-pcb-page-en`
  - candidate context for rigid multilayer scope

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- not normalized by site, line, or explicit measurement basis

## Refresh-Sensitive Or Non-Authorizing Sources

Treat the following as refresh-sensitive and non-authorizing for numeric reuse:

- all internal product/process JSON registry records
- internal method cards derived from those records
- official standards metadata pages
- official supplier processing guides
- official any-layer or HDI architecture pages

Reasons:

- wording may change
- scope is usually broad or architectural
- numeric context is often incomplete or absent
- they do not function as a dated internal capability record

## Missing Items

Missing items before `aspect_ratio` can move beyond intake:

- a dated internal capability record for plated-through-hole aspect-ratio capability
- explicit measurement basis for any future ratio claim
- explicit rigid-multilayer vs HDI separation
- explicit site, line, or process-family scope where needed
- explicit refresh rule and supersession chain
- one intake note confirming that no standards or microvia-reliability table was imported through this bucket

## Recommended Ingestion Order

1. internal drilling posture inputs
   - start with `frontendapt-pcb-drilling-page-en`
2. rigid multilayer scope inputs
   - then `frontendapt-pcb-multilayer-pcb-page-en` and `frontendapt-pcb-high-layer-count-pcb-page-en`
3. HDI boundary inputs
   - then `frontendapt-pcb-hdi-pcb-page-en` and `facts/methods/hdi-microvia-and-vippo-process-posture.md`
4. standards and external boundary inputs
   - then `ipc-2226a-hdi-standard-page`, `ipc-2315-legacy-hdi-guide-page`, `mil-prf-31032-1e-rigid-multilayer-thermosetting-spec-sheet-page`
5. only after that, decide whether a real dated capability record can be created

If step 5 fails, the bucket remains:

- `needs_source` for reusable numerics
- `downgrade` for non-numeric manufacturability wording

## Current Source-Map Conclusion

The current corpus is strong enough to map `aspect_ratio` boundaries and to prevent collapse between plated-through-hole capability, HDI architecture, and standards/reliability content.

It is not strong enough to recover a reusable aspect-ratio number today.
