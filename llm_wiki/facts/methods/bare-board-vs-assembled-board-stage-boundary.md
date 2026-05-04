---
fact_id: "methods-bare-board-vs-assembled-board-stage-boundary"
title: "Current public IPC metadata plus internal PCB and PCBA layers support a bare-board versus assembled-board stage boundary, not universal PCA terminology normalization"
topic: "bare board versus assembled board stage boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "ipc-9252b-toc"
  - "frontendapt-pcb-pcb-fabrication-process-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
tags: ["pcb", "pcba", "bare-board", "assembled-board", "stage-boundary", "terminology", "inspection", "npi"]
---

# Canonical Summary

> The current source layer is strong enough to separate two manufacturing stages: a `PCB` article can safely stay on the bare-board side, while an assembled-board article can safely move into component population, soldering, inspection, electrical-access test, powered functional validation, and release-gate language. The same source layer does not settle whether `PCA` is a standards-grade normalized public term, whether it equals `PCBA`, or which long-form expansion should be preferred in publication.

## Stable Facts

- `IPC-9252B` public metadata supports a separate bare-board electrical-test identity for unpopulated printed boards.
- The internal APT PCB fabrication-process page supports bare-board process framing that includes fabrication flow and final electrical-test language before component population is introduced.
- The internal APT SMT / THT page supports later assembly-stage language spanning stencil and paste engineering, placement, soldering, inspection, and test coverage.
- The internal PCBA quality-system page supports assembly-stage process language such as incoming control, in-process inspection, electrical validation, final inspection, cleaning, and traceability.
- The internal ICT, FCT, and flying-probe pages support a separate assembled-board test layer after bare-board fabrication.
- Together, these sources support a guarded stage boundary:
  `bare board fabrication / bare-board electrical-test scope -> component population and soldering -> assembly inspection -> electrical-access or powered validation -> release`.

## Conditions And Methods

- Use this card for `pca-vs-pcb.md` only when the article needs a minimal stage distinction between an unpopulated board and a later assembled board.
- Safe `PCB` posture:
  keep the article on board fabrication, fabrication outputs, bare-board inspection, and unpopulated-board electrical-test scope.
- Safe assembled-board posture:
  discuss component population, soldering, inspection, ICT / flying-probe style electrical-access checks, powered FCT, and release-gate language only after the board has moved into PCBA scope.
- Treat `PCA` as unresolved publication terminology unless a future public source explicitly defines or normalizes it.
- Pair this card with `methods-pcba-mixed-technology-assembly-flow`, `methods-pcba-layered-inspection-stack`, `methods-pcba-ict-vs-fct-boundary`, `methods-pcba-flying-probe-test-positioning`, and `methods-parameter-scope-test-inspection-electrical-access-method-dimensions` when the prompt needs assembly-flow or test-stack context.

## Limits And Non-Claims

- This card does not prove that `PCA` is the standards-preferred abbreviation.
- It does not prove that `PCA = PCBA` or that either term must expand to `printed circuit assembly`.
- It does not prove universal synonym or hierarchy claims among `PCA`, `PCBA`, `printed board assembly`, and `printed circuit assembly`.
- It does not authorize draft-originated cleaning, contamination, reliability, corrosion, or qualification causality claims.
- It does not authorize universal SMT-versus-THT decision rules, application-domain requirements, prototype-to-volume scaling advice, cost ladders, lead-time claims, or turnkey-partner guidance.
- It does not extract any technical requirements, thresholds, or acceptability criteria from public IPC metadata pages.

## Open Questions

- Add a stronger terminology card only if a future public IPC or equivalent authoritative source exposes exact definitions or preferred term forms for `PCA`, `PCBA`, or adjacent long forms.
- Add independent public sources before publishing any detailed cleaning, reliability, assembly-technology selection, or manufacturing-economics claims from this draft family.

## Source Links

- https://www.ipc.org/TOC/IPC-9252B.pdf
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-fabrication-process.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
