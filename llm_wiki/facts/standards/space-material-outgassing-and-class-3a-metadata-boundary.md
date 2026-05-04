---
fact_id: "standards-space-material-outgassing-and-class-3a-metadata-boundary"
title: "Space-material outgassing and Class 3A language can be anchored as metadata and hierarchy context, not qualification proof"
topic: "space material outgassing and Class 3A metadata boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "astm-e595-15r21-page"
  - "nasa-vacuum-outgassing-database-page"
  - "nasa-outgassing-user-guide-page"
  - "ipc-6012fs-space-military-addendum-page"
  - "ipc-6012fs-toc"
  - "ipc-cc-830c-toc"
tags: ["space-materials", "outgassing", "astm-e595", "nasa", "ipc-6012fs", "class-3", "class-3a", "metadata-boundary"]
---

# Canonical Summary

> Public ASTM, NASA, and IPC metadata is strong enough to support narrow `llm_wiki` wording that keeps `ASTM E595` at test-method identity level, NASA outgassing pages at screening/database context level, and `IPC-6012FS` at procurement-triggered `Class 3` exception-layer context. These sources are not strong enough to prove `Class 3A` thresholds, coating subtype performance, qualification-listing status, or mission-readiness outcomes.

## Stable Facts

- `ASTM E595-15(2021)` is a public test-method anchor for vacuum outgassing measurements including `TML`, `CVCM`, and `WVR`, not a standalone mission-acceptance rule.
- NASA Goddard's public outgassing database is a screening and reference context for spaceflight-material evaluation and publicly ties its test basis to `ASTM E595`.
- NASA's public outgassing user guide keeps familiar low-outgassing values in database-screening context rather than as automatic acceptance criteria for every board, material, or coating.
- `IPC-6012FS` is the current public IPC space and military avionics addendum anchor in this corpus and is publicly framed as providing exceptions to `IPC-6012F` `Class 3` requirements.
- The public `IPC-6012FS` TOC shows that the addendum is not standalone, applies with procurement-document invocation, and touches clause families rather than exposing reusable public thresholds.
- The public `IPC-CC-830C` TOC is only a document-identity and scope anchor for conformal-coating standard metadata in this corpus; it does not unlock subtype-specific coating claims.
- Together, these sources support guarded wording such as `outgassing method`, `screening context`, `space-material evaluation`, `procurement-triggered addendum`, and `Class 3 exception layer`.

## Conditions And Methods

- Use this card when a space-oriented PCB or materials draft needs to mention `ASTM E595`, NASA outgassing screening, `IPC-6012FS`, or `Class 3 / Class 3A` without turning those references into acceptance tables.
- Prefer wording such as `may be screened`, `is publicly identified as`, `can sit inside program-specific interpretation`, `is invoked by procurement documentation`, and `does not prove acceptance by itself`.
- Keep `Class 3A` wording at hierarchy or context level unless a stronger exact public authority is added for the specific claim.
- Use `IPC-CC-830C` only for generic conformal-coating standard identity in this card's scope, not for `Type AR` or other subtype assertions.

## Limits And Non-Claims

- This card does not provide `Class 3A` thresholds, sample plans, frequencies, or clause-level acceptance criteria.
- It does not turn NASA database screening context or `ASTM E595` method identity into approval for a laminate, solder mask, adhesive, conformal coating, finished board, or mission.
- It does not support `GSFC-STD-7000`, `ECSS-E-ST-10-03`, radiation, thermal-cycle, vibration, shock, or other environmental-test numerics.
- It does not support `Parylene C`, `Parylene HT`, or `IPC-CC-830 Type AR` performance or subtype claims.
- It does not prove supplier qualification, `QML` or `QPL` status, release authority, heritage, `space-grade` status, or mission readiness.

## Open Questions

- Add a narrower follow-on only if future work brings exact public authority for `Class 3A` terminology or coating subtype identity that can be separated from performance claims.

## Source Links

- https://store.astm.org/e0595-15r21.html
- https://etd.gsfc.nasa.gov/capabilities/capabilities-listing/vacuum-outgassing-database/
- https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf
- https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf
