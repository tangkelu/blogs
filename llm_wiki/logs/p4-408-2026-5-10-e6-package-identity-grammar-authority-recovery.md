# P4-408 E6 Package Identity Grammar Authority Recovery

Date: 2026-05-10
Lane owner: `E6 narrow authority recovery`
Execution mode: `source_fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/电子元器件封装(Package).pdf`

Parent surfaces:
- `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`
- `logs/p4-333-2026-5-9-e6-package-family-and-footprint-route-integration.md`
- `facts/methods/package-family-and-footprint-governance-vocabulary-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## Purpose

Advance one `E6` lane beyond `single_pdf_usage_route_only` by landing a current-public official boundary for package identity grammar.

This pass is narrow by design.
It does not attempt to promote package geometry, size-code conversion tables, or universal naming doctrine.

## New Official Source Support

This pass adds two current-public official source classes:

1. `infineon-package-family-and-package-detail-identity-grammar`
   - supports owner-scoped package identifier fields such as `Package Material`, `Package Family`, `Terminals`, and `Variant`
   - supports documented family qualifiers and legacy aliases in owner context

2. `kicad-library-conventions-package-family-and-footprint-naming`
   - supports package-family-first naming such as `QFN-48` and `DIP-20`
   - supports explicit pin-count fields in footprint identity
   - remains useful as CAD-library convention reinforcement

## What Was Promoted

Strengthened existing `facts/` coverage:

- package-family labels can be reused as owner-scoped and CAD-library identity grammar
- pin count and variant can be treated as distinct identifier fields rather than implied free-text suffixes
- common industry / JEDEC naming can be referenced as a convention surface when kept inside CAD-library identity framing
- owner-documented legacy aliases can be reused conservatively as package-identity context

## What This Pass Does Not Promote

This pass still does not authorize:

- package-size conversion tables
- exact package geometry or land-pattern rules
- handbook naming strings as universal standards truth
- one universal naming schema across every CAD, ERP, vendor, or package family

## E6 Lane Effect

`电子元器件封装(Package).pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `package identity grammar` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `sources/registry/methods/kicad-library-conventions-package-family-and-footprint-naming.md`
- `sources/registry/methods/infineon-package-family-and-package-detail-identity-grammar.md`

## Deliverables Strengthened

- `facts/methods/package-family-and-footprint-governance-vocabulary-boundary.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the strengthened fact card now cites the new Infineon owner naming source and the KiCad naming source
- the per-PDF `E6` entry for `电子元器件封装(Package).pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
