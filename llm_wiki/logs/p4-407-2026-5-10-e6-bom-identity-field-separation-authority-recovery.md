# P4-407 E6 BOM Identity-Field Separation Authority Recovery

Date: 2026-05-10
Lane owner: `E6 narrow authority recovery`
Execution mode: `source_fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/BOM查错助力元器件采购.pdf`

Parent surfaces:
- `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`
- `logs/p4-336-2026-5-9-e6-bom-sourcing-and-alternate-control-route-integration.md`
- `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
- `facts/methods/avl-and-alternate-control-posture.md`
- `facts/methods/bom-and-hdi-complexity-boundary.md`

## Purpose

Advance one `E6` lane beyond `single_pdf_usage_route_only` by landing a current-public official boundary for BOM identity-field separation.

This pass is intentionally narrow.
It does not try to close procurement outcomes, market-state claims, or software sufficiency.

## New Official Source Support

This pass adds three Altium official documentation surfaces:

1. `altium-activebom-managing-solutions-manufacturer-supplier-identity`
   - supports the boundary that `Manufacturer Part` and linked `Supplier Part` identities are separate review objects

2. `altium-activebom-manufacturer-link-fields-dialog`
   - supports explicit mapped fields for `Manufacturer Name` and `Manufacturer Part Number`

3. `altium-365-bom-portal-identity-and-sourcing-columns`
   - supports the boundary that structured identity and sourcing review can remain visible together without collapsing into one ambiguous field

## What Was Promoted

Promoted into reusable `facts/` coverage:

- BOM identity should keep manufacturer identity explicit
- `Manufacturer Part Number` is a distinct controlled identity field
- supplier-facing sourcing identity is a separate downstream review surface
- sourcing review and alternate-control depend on structured identity fields, but are not the same thing as identity fields

## What This Pass Does Not Promote

This pass still does not authorize:

- automatic BOM matching sufficiency
- quote readiness guarantees
- stock, MOQ, lead time, or price claims
- supplier approval or counterfeit-control guarantees
- shipping or delivery claims
- universal ERP / PLM schema doctrine

## E6 Lane Effect

`BOM查错助力元器件采购.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `BOM identity-field separation` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `sources/registry/methods/altium-activebom-managing-solutions-manufacturer-supplier-identity.md`
- `sources/registry/methods/altium-activebom-manufacturer-link-fields-dialog.md`
- `sources/registry/methods/altium-365-bom-portal-identity-and-sourcing-columns.md`
- `facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- source IDs resolve cleanly inside the new fact card
- the per-PDF `E6` entry for `BOM查错助力元器件采购.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
