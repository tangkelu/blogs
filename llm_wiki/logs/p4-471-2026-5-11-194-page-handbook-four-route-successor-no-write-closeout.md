# P4-471 194-Page Handbook Four-Route Successor No-Write Closeout

Date: 2026-05-11
Parent surfaces:

- `logs/p4-386-2026-5-10-pcb-ziliao-residual-route-audit-and-no-write-closeout.md`
- `logs/p4-402-2026-5-10-d5-connector-adjacent-esd-entry-path-boundary-route.md`
- `logs/p4-403-2026-5-10-d5-esd-entry-path-boundary-owner-source-strengthening.md`
- `logs/p4-404-2026-5-10-d5-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`
- `logs/p4-468-2026-5-11-d3-remote-feedback-and-quiet-sense-point-boundary.md`
- `logs/p4-469-2026-5-11-d5-clock-source-termination-and-crystal-routing-emc-boundary.md`
- `logs/p4-470-2026-5-11-d5-clock-routing-boundary-successor-sitime-ti-strengthening.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

Execution mode: `subagent_aided_handbook_residual_successor_closeout`

## Purpose

Replace the stale `P4-386` residual wording for `【PCB必备】194页-PCB设计规范经验之书.pdf` with the current truth after `P4-402`, `P4-404`, `P4-468`, `P4-469`, and `P4-470`.

This pass is a no-write closeout for the current authority ceiling.
It is not a full handbook closeout, not a full `D3` closeout, and not a full `D5` closeout.

## Audit Scope

1. recheck whether the handbook should still be treated as `below narrow-route admission`
2. enumerate the currently landed non-overlapping narrow routes
3. define which residual surfaces remain reopenable and which ones should stop being reopened on the current source layer

## Findings

### 1. `P4-386` is no longer the right residual wording for this handbook

- `P4-386` correctly recorded the earlier state on `2026-05-10`, when no handbook-specific narrow route had yet been admitted for this PDF.
- That wording is now stale because the repo has since landed four non-overlapping official-source-backed handbook routes:
  - one `D3` route
  - three `D5` routes
- The current handbook state is therefore no longer `pure claim-family residual waiting for first narrow-route admission`.

### 2. The current handbook ceiling is now four landed narrow routes

Current landed route set:

1. `D3 remote feedback / quiet sense-point`
   - landed through `P4-468`
   - safe reuse ceiling:
     - quiet sense-point selection
     - short and direct feedback or sense routing
     - quiet layer or quiet analog-ground handling
     - switch-node or noisy-power avoidance
   - still blocked:
     - line-width or spacing numerics
     - divider or compensation values
     - rail-specific recipes
     - regulation or EMI outcome claims

2. `D5 connector-adjacent ESD entry-path interception`
   - landed through `P4-402`, then strengthened by `P4-403`
   - safe reuse ceiling:
     - connector-adjacent protection placement
     - `ESD source -> protection -> protected IC` routing order
     - avoid stub or branch-first routing
     - low-impedance local return or reference handling
   - still blocked:
     - exact path lengths or distances
     - via-count or package-layout rules
     - IEC pass levels
     - full `D5` closure

3. `D5 surface-ground continuity / exposed-zone isolation`
   - landed through `P4-404`
   - safe reuse ceiling:
     - connector-near or board-edge surface-ground continuity
     - exposed-zone routing separation from clean sensitive traces
   - still blocked:
     - exact board-edge distances
     - copper setback values
     - stitch-via count or spacing rules
     - EMC or ESD pass claims

4. `D5 clock source-end termination / crystal-routing EMC`
   - landed through `P4-469`, then strengthened by `P4-470`
   - safe reuse ceiling:
     - series termination close to source
     - stable or solid reference under clock traces
     - clock or crystal source close to the related device
     - no unrelated routing near or under the source region
     - avoid bend or branch-first routing
     - avoid board-edge and noisy high-current regions
   - still blocked:
     - exact resistor values
     - exact length, spacing, or impedance numbers
     - shielding-via recipes
     - timing, jitter, SI, or EMC outcome claims

### 3. The handbook should not be reopened on the same already-landed surfaces

The current repo should not reopen this handbook just to:

- restate the same `remote feedback` route with synonym-level wording changes
- restate the same `D5 clock` route from the current `SiTime + TI` ceiling
- repackage generic return-path continuity or generic high-speed guidance as if it were a new handbook-specific route
- leak `RK3588`-specific numerics, recipes, tables, exact values, or exact distances into reusable authority

### 4. The handbook is still not fully closed

This closeout does not say that all remaining handbook value is exhausted forever.
It says only that reopening now must clear a higher bar: materially stronger and non-overlapping authority.

The best still-open handbook-side residual candidates are now limited to:

- `D5 switch-mode power EMC placement`, if a strong non-duplicative owner or standards-adjacent primary source appears
- another genuinely independent `D5` EMC sub-surface that is not already absorbed by:
  - `entry-path ESD`
  - `surface-ground continuity / exposed-zone isolation`
  - `clock-specific EMC`
- a `D3` power-layout sub-surface beyond `remote feedback`, but only if a new primary source closes a distinct boundary rather than restating broad PMIC doctrine

## Audit Result

- no new `facts/`, `wiki/`, or `sources/registry/` files were admitted
- the handbook remains below full `D3` and full `D5` closure
- the handbook does not return to `pure claim-family residual` status
- the current safe description is now:
  - `claim_family_level_only_with_four_strengthened_official_routes`

## What This Closeout Fixes

- future AI should no longer treat `P4-386` as the current residual truth for the `194页 handbook`
- future AI should not reopen `remote feedback` or current `D5 clock` on the same source set expecting one missed obvious narrow route
- future AI should default away from broad reread of this handbook and reopen only source-first on a still-unlanded independent residual surface

## Recommended Next Action

If `/goal` continues from here:

1. keep this handbook closed at the current four-route ceiling unless materially stronger non-overlapping authority appears
2. prefer reranking other corpus residuals over another broad `194页 handbook` pass
3. if this handbook is reopened later, prioritize only a truly independent residual such as `D5 switch-mode power EMC placement`
