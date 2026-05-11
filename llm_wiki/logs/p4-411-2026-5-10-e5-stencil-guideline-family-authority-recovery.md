# P4-411 E5 Stencil Guideline Family Authority Recovery

Date: 2026-05-10
Lane owner: `E5 narrow authority recovery`
Execution mode: `source_fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/如何避免踩坑钢网.pdf`

Parent surfaces:
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-335-2026-5-9-e5-stencil-and-paste-route-integration.md`
- `sources/registry/standards/ipc-7525c-toc.md`
- `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`
- `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `wiki/processes/mixed-technology-solder-route-selection.md`

## Purpose

Advance one `E5` stencil lane beyond `single_pdf_usage_route_only` by adding one standards-owner public source anchor and one dedicated narrow fact boundary for stencil-guideline family scope and upstream solder-paste print-control framing.

This pass stays narrow.
It does not attempt to promote aperture geometry rules, fiducial defaults, fabrication-method rankings, or intrusive-soldering process-window limits.

## Official Source Support Added

Created one new public standards-owner source record:

1. `ipc-7525c-toc`
   - anchors `IPC-7525C Stencil Design Guidelines` as a real official document family
   - provides public scope wording around stencil data, aperture-design surfaces, solder-paste layer, mixed-technology intrusive-soldering context, step stencil, fiducials, fabrication technologies, inspection, and cleaning
   - explicitly stays metadata-only and does not unlock licensed clause content

## What Was Created

Created:

- `sources/registry/standards/ipc-7525c-toc.md`
- `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`

## What Was Promoted

Promoted into reusable `official_fact-backed` article-side coverage:

- stencil guidance can now be anchored to an official IPC stencil-guideline family rather than only to article vocabulary or internal service-page wording
- stencil work can be framed as an upstream solder-paste print-control surface
- `stencil data`, `solder-paste layer`, `aperture list`, `step stencil`, `fiducials`, and mixed-technology intrusive-soldering context can now be mentioned as official topic-family surfaces at metadata scope

## What This Pass Does Not Promote

This pass still does not authorize:

- aperture reduction defaults, area-ratio or aspect-ratio rules, or paste-volume formulas
- notch or home-plate / bow-tie aperture recommendations as public reusable defaults
- mark-point or fiducial geometry, size, location, or equipment-fit rules
- stencil thickness defaults, step-up / step-down selection rules, or intrusive-soldering process-window limits
- etch / laser / electroform precision, durability, release-performance, or cost-superiority claims
- defect-prevention certainty, yield, cost, delivery, or supplier-capability claims

## E5 Lane Effect

`如何避免踩坑钢网.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `stencil guideline family and upstream print-control boundary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Reused And Strengthened

- `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`
- `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `wiki/processes/mixed-technology-solder-route-selection.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the new IPC stencil source record resolves cleanly as a public metadata-only standards anchor
- the new stencil fact resolves cleanly with its source IDs and keeps claims inside scope framing
- the stencil article entry in `p4-325` no longer understates the lane as route-only
- `p4-309` now records one additional official-fact raise inside `E5`
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
