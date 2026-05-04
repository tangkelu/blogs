# P4-116 2026-05-02 Arlon Product-Grade Source Recovery

Date: 2026-05-02
Lane: `Arlon product-grade official datasheet anchors`
Worker: `D`
Status: `fact_partial`

## Scope

Determine whether meaningful Arlon product-grade official recovery remained beyond the already covered `N-series`, `55NT`, `85N`, and `85NT` posture, then land only the minimum justified Arlon artifacts.

## Read Baseline

- `wiki/materials/arlon-material-family-source-governance.md`
- `facts/materials/arlon-product-page-recovery-n-series.md`
- `facts/materials/arlon-hi-rel-branch-normalization.md`
- existing source records for `55NT`, `85N`, and `85NT`

## What Was Already Covered

- `33N`, `35N`, `37N`, `45N`, `47N`, `84N`, and `85N` already had official product-page identity anchors.
- `55NT`, `85N`, and `85NT` already had product-grade exact-product posture through current source records and fact cards.
- The remaining open boundary from prior governance was mostly unresolved RF/PTFE families plus any newly discoverable current Arlon exact-product branch outside the prior normalization set.

## Recovery Decision

Meaningful recovery still existed.

On `2026-05-02`, current official Arlon pages confirmed a distinct `86HP` high-performance polyimide branch with:

- an official product page published `2022-11-10`
- a current official datasheet at `86HP-v-1.6.pdf` under the `2024/02` Arlon PDF path

That branch was not already registered in the Arlon lane files, so it justified a minimal promotion.

## Landed Artifacts

- `sources/registry/materials/arlon-86hp-product-page.md`
- `sources/registry/materials/arlon-86hp-datasheet.md`
- `facts/materials/arlon-86hp-exact-product.md`

## Why `86HP` Was Chosen

- It is outside the already covered `55NT` / `85N` / `85NT` exact-product posture.
- It has a current official product page and current official datasheet support, which clears the lane requirement against unsupported parameter claims.
- It allows one narrow exact-product card without reopening broad Arlon wiki work.

## Exact Blocker Status

The Arlon lane is not fully closed.

Still blocked for product-grade promotion in this lane:

- `CLTE-XT`
- `TC350`
- `AD250`
- `AD255`
- `AD300`
- `CuClad`
- `DiClad`

Blocker reason:

- current registered product-grade official pages or datasheets were not landed for those RF/PTFE families in this pass
- prior governance still treats those families as unresolved and not parameter-ready
- no broad wiki expansion is justified until current official product-grade authority is recovered

Additional non-blocking note:

- `45NK` appears as a live official Arlon controlled-CTE / SMT branch with a datasheet, but this pass stayed minimal and did not open a second exact-product branch once `86HP` was sufficient to prove meaningful remaining recovery.

## Outcome

Lane ended `fact_partial`.

The Arlon lane did not remain purely source-only because one new justified exact-product branch was recoverable and was landed with current official datasheet support. The unresolved RF/PTFE families remain explicit holds for future source recovery rather than implicit completion.

## Verification

- verified new source IDs and fact ID naming consistency
- ran `git diff --check` on the changed Arlon lane files
