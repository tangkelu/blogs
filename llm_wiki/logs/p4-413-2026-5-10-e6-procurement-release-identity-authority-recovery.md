# P4-413 E6 Procurement-Release Identity Authority Recovery

Date: 2026-05-10
Lane owner: `E6 narrow authority recovery`
Execution mode: `fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/如何避免采购电子元器件入坑.pdf`

Parent surfaces:
- `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`
- `logs/p4-338-2026-5-9-e6-procurement-risk-route-integration.md`
- `logs/p4-336-2026-5-9-e6-bom-sourcing-and-alternate-control-route-integration.md`
- `facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md`
- `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
- `facts/methods/avl-and-alternate-control-posture.md`
- `facts/standards/high-reliability-traceability-and-counterfeit-control-metadata.md`

## Purpose

Advance one `E6` procurement-risk lane beyond `single_pdf_usage_route_only` by landing a narrow official-fact boundary for procurement-ready BOM identity completeness and controlled-source governance.

This pass is intentionally narrow.
It does not try to close market-state claims, seller-quality claims, package numerics, or procurement-outcome promises.

## Official And Existing Source Support Used

This pass reuses already-landed official and internal source support:

1. `altium-activebom-managing-solutions-manufacturer-supplier-identity`
   - supports the boundary that manufacturer-side identity and supplier-facing sourcing identity are separate review objects

2. `altium-activebom-manufacturer-link-fields-dialog`
   - supports explicit mapped fields for `Manufacturer Name` and `Manufacturer Part Number`

3. `altium-365-bom-portal-identity-and-sourcing-columns`
   - supports the boundary that structured identity and sourcing review can stay visible together without being collapsed into one ambiguous text field

4. `ipc-1782b-traceability-standard-page`
   - supports traceability vocabulary as a supply-chain governance layer

5. `as6171a-counterfeit-test-methods-page`
   - supports the boundary that testing alone does not prove authenticity without chain of custody

6. `dfars-252-246-7008-sources-of-electronic-parts-page`
   - supports preferred-source hierarchy and traceability-aware procurement governance as responsibility layers

7. `frontendapt-pcba-component-sourcing-page-en` and `frontendapt-pcba-components-bom-page-en`
   - support BOM review, sourcing review, alternates posture, and traceability as part of one governed release flow

## What Was Promoted

Promoted into reusable `facts/` coverage:

- procurement-ready review should keep manufacturer identity explicit
- `Manufacturer Part Number` should remain distinct from supplier-facing sourcing or order-link fields
- alternates should be resolved through controlled review rather than casual substitution
- traceability and authenticity checks are governance layers, not proof of supply success
- sample-stage or inquiry-stage visibility should not be treated as production-release readiness

## What This Pass Does Not Promote

This pass still does not authorize:

- stock, `现货`, shortage, lead-time, MOQ, replenishment, or market-state claims
- supplier quality, inventory-control strength, channel superiority, or delivery reliability claims
- authorized-source, authenticity, or counterfeit-avoidance outcome claims for any named marketplace or seller
- software or workflow guarantee claims for BOM checking, package matching, or procurement correctness
- package-width, body-size, suffix-taxonomy, or dimensional examples from the PDF itself
- sample-stage continuity claims into mass-production release

## E6 Lane Effect

`如何避免采购电子元器件入坑.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `procurement-release identity completeness and controlled-source governance` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `facts/methods/procurement-release-identity-completeness-and-controlled-source-boundary.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- source IDs resolve cleanly inside the new fact card
- the per-PDF `E6` entry for `如何避免采购电子元器件入坑.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
