# P4-116 2026-05-02 Taconic Product-Grade Source Recovery

Date: 2026-05-02
Status: `remains_hold_due_to_missing_current_authority`

## Purpose

Attempt official source recovery for Taconic product-grade RF laminate anchors named by the Batch A lane, with priority on exact-grade rows such as `RF-35` and nearby Taconic product-grade families.

## Inputs Inspected

- `/code/blogs/llm_wiki/policies/ai-execution-contract.md`
- `/code/blogs/llm_wiki/logs/p4-116-2026-5-2-execution-controller-note.md`
- `/code/blogs/llm_wiki/logs/site-material-baseline-coverage.md`
- `/code/blogs/llm_wiki/logs/p4-116-2026-5-1-second-half-knowledge-promotion-plan.md`
- `/code/blogs/llm_wiki/sources/registry/materials/taconic-divisions-page.md`
- `/code/blogs/llm_wiki/sources/registry/materials/taconic-add-rohs-weee-compliance-2022.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-taconic-pcb-page-en.md`

## Official Source Recovery Result

- Taconic-controlled official coverage confirmed at division/compliance level only.
- The official divisions page anchors Taconic's Advanced Dielectric Division and PTFE laminate / prepreg positioning for low-loss multilayer PCB use.
- The official RoHS / WEEE statement confirms Taconic ADD product-family names in compliance context, including `RF-35`, `RF-35A2`, `RF-35P`, `RF-35TC`, `RF-41`, `RF-43`, `RF-45`, `RF-60`, `RF-60TC`, `CER-10`, `TLC`, `TLE`, `TLX`, `TLY`, and `TSM Family`.
- No Taconic-controlled public product-page or datasheet URL for exact product-grade recovery was verified in this pass.

## Blocker

- Exact Taconic product-grade datasheet authority remains missing.
- Third-party mirrors were not accepted as authority.
- No product-level Dk / Df / Tg / thickness / copper / processing record was promoted.

## Artifacts

- No new `sources/registry/materials/*` record added.
- No new `facts/materials/*` card added.

## Completion Status

- lane end state: `hold`
- residual blocker: `no verified Taconic-controlled product-grade datasheet anchor for RF-35 or nearby TLY/TLX/TLC/TLE product rows`
