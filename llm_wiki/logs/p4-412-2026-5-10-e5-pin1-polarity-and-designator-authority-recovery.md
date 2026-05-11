# P4-412 E5 Pin-1 Polarity And Designator Authority Recovery

Date: 2026-05-10
Lane owner: `E5 narrow authority recovery`
Execution mode: `fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCBA丝印位号与极性符号的组装性设计.pdf`

Parent surfaces:
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-332-2026-5-9-e5-polarity-reference-designator-route-integration.md`
- `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md`
- `facts/methods/iec-smd-component-marking-boundary.md`
- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- `wiki/testing/pcba-visual-inspection-taxonomy.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## Purpose

Advance one `E5` lane beyond `single_pdf_usage_route_only` by creating one dedicated fact boundary for `pin-1`, polarity, and reference-designator documentation governance using already-landed public IEC boundaries plus existing internal assembly-document and inspection sources.

This pass stays narrow.
It does not attempt to promote universal silkscreen rules, text-size rules, component-prefix grammar, or package-family-specific marking geometry.

## Official Source Support Reused

This pass does not need new source records, but it does add one dedicated fact boundary.
The repo already had public and internal authority strong enough for this lane:

1. `iec-61760-1-smd-specification-page` and `iec-61760-1-component-marking-preview-page`
   - keep `pin-1` and polarity discussion inside controlled component-marking scope

2. `iec-61188-7-zero-orientation-cad-library-page`
   - keeps orientation intent tied to controlled CAD-library construction

3. `frontendapt-blog-assembly-drawing-essentials-en` and `frontendapt-blog-smt-component-polarity-en`
   - keep assembly-drawing completeness, pin-1 visibility, polarity annotation, and zero-orientation discipline inside documentation-governance framing

4. `frontendapt-pcba-aoi-inspection-page-en` and `frontendapt-pcba-quality-system-page-en`
   - keep visible polarity and orientation checks inside broader PCBA inspection and release workflow

## What Was Created

Created:

- `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md`

## What Was Promoted

Promoted into reusable `official_fact-backed` article-side coverage:

- `pin-1` and polarity intent should be explicit in controlled component specification, CAD-library, and assembly-document layers
- reference designators belong to assembly communication and documentation completeness rather than operator memory
- orientation, polarity, and visible marking checks belong to the broader inspection workflow

## What This Pass Does Not Promote

This pass still does not authorize:

- universal `R/C/L/U/Q` prefix grammar as standards truth
- silkscreen text size, stroke width, spacing, keepout, or placement-distance rules
- universal pin-1 symbol, polarity symbol, or package-family marking default
- board-level installation-mark geometry
- guaranteed failure-prevention, yield, cost, or delivery claims

## E5 Lane Effect

`PCBA丝印位号与极性符号的组装性设计.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `pin-1 polarity and reference-designator documentation boundary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Reused And Strengthened

- `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md`
- `facts/methods/iec-smd-component-marking-boundary.md`
- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- `wiki/testing/pcba-visual-inspection-taxonomy.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the new polarity / pin-1 / designator fact resolves cleanly with existing source IDs
- the article entry in `p4-325` no longer understates the lane as route-only
- `p4-309` now records one additional official-fact raise inside `E5`
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
