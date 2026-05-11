---
fact_id: "methods-dfa-assembly-review-and-package-footprint-mismatch-trigger-boundary"
title: "DFA can be reused as early assembly-review posture, with package-to-footprint mismatch held as an explicit release trigger"
topic: "DFA assembly review and package footprint mismatch trigger boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
source_ids:
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-glossary-terms-resource-page-en"
  - "frontendapt-resources-index-en"
  - "kicad-library-conventions-footprint-orientation-and-marking"
tags: ["dfa", "assembly", "package", "footprint", "pin-count", "review-trigger", "dfm", "methods"]
---

# Canonical Summary

> Current repo-backed internal and CAD-library coverage is strong enough to support one narrow `DFA` boundary: `DFA` may be reused as an early assembly-review posture, and package-name mismatch, pin-count mismatch, or package-to-footprint library-selection mismatch may be treated as explicit review triggers before release. This boundary supports governance and review language only. It does not authorize spacing numerics, pad geometry, fiducial defaults, hole-fit ratios, or workflow-sufficiency claims.

## Stable Facts

- Internal workflow pages already position `DFM`, `DFT`, and `DFA` as front-end review gates before downstream inspection, electrical validation, and release decisions.
- Internal glossary and DFM resource layers already support reusable package, footprint, pad, drill, and assembly-document vocabulary for review-stage discussion.
- The existing package-library governance map already supports the controlled flow from package identity to footprint-library object review, then to stronger geometry authority when exact closure is needed.
- Official KiCad library-convention support already reinforces that footprint-library objects belong to controlled library rules rather than ad hoc local inference.
- The existing package-to-footprint alignment card already supports one narrow review rule:
  package-name mismatch, pin-count mismatch, or library-selection mismatch should trigger review before release.
- From those layers together, the repo can safely preserve one narrow `E5` rule:
  `DFA` can be written as early assembly-review posture, and package / footprint mismatch can be written as an explicit release trigger inside that posture.

## Conditions And Methods

- Use this card when a draft needs conservative `DFA` wording for `E5` article rewrites.
- Treat the safe reusable rule as:
  - `DFA` happens early, before downstream inspection and final release
  - package identity must align with the selected footprint-library object
  - package-name mismatch is a review trigger
  - pin-count mismatch is a review trigger
  - library-selection mismatch is a review trigger
- Pair this card with:
  - [pcba-dfm-dft-dfa-review-gate-positioning.md](/code/blogs/llm_wiki/facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md)
  - [package-to-footprint-and-pin-count-alignment-review-boundary.md](/code/blogs/llm_wiki/facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md)
  - [package-library-governance-and-footprint-review-map.md](/code/blogs/llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md)
- Keep this card at early-review and mismatch-trigger level only; if a prompt needs exact package geometry, spacing thresholds, fiducial rules, or THT fit ratios, require narrower primary sources.

## Safe Blog Usage

- Explain that `DFA` is an upstream assembly-readiness review, not only a post-fabrication check.
- Explain that package identity and footprint-library identity should be reconciled before release.
- Explain that pin-count mismatch and package-name mismatch are stop-and-review signals.
- Explain that early assembly review reduces governance ambiguity, but does not by itself prove build success.

## Limits And Non-Claims

- This card does not authorize component-spacing values, board-edge distances, or rail / depanel clearance numbers.
- It does not authorize chip-pad geometry, toe / heel / width rules, or tombstoning-prevention defaults.
- It does not authorize fiducial count, placement, or geometry rules.
- It does not authorize hole-fit, press-fit, NPTH / THT geometry ratios, or lead / hole dimension rules.
- It does not authorize automatic library-matching sufficiency, workflow-completeness, or tool-superiority claims.
- It does not authorize yield, quality, cost, delivery, or `covers everything` claims.

## Provenance Boundary

- `P4-345` contributes the demand signal that the article groups `DFA`, package mismatch, spacing, marking, and tooling language together.
- Authority comes from the existing internal DFM / quality / turnkey workflow pages plus the already-landed package-library governance and package-to-footprint review boundary.

## Open Questions

- Add a narrower future card only if the repo later needs official-source support for fiducials, THT hole-fit, or assembly-edge transport constraints.
- Add a stronger public assembly-owner lane later if a future batch needs formal DFA terminology beyond internal workflow positioning.

## Source Links

- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
- /code/hileap/frontendAPT/public/static/resources/en/index.json
- https://klc.kicad.org/
