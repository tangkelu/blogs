---
fact_id: "standards-22-layer-compliance-assertion-boundary"
title: "22-layer compliance assertions must stay separate from public standards, audit, and qualification-framework metadata"
topic: "22-layer compliance assertion boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-a-600k-toc"
  - "ipc-6011a-toc"
  - "ipc-6012f-toc"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fa-toc"
  - "as9100d-qms-requirements-page"
  - "as9101g-audit-requirements-page"
  - "mil-prf-55110-general-spec-page"
  - "mil-prf-31032-general-spec-page"
  - "mil-prf-31032-1e-rigid-multilayer-thermosetting-spec-sheet-page"
  - "dfars-252-246-7008-sources-of-electronic-parts-page"
  - "far-52-246-11-higher-level-contract-quality-requirement-page"
tags: ["22-layer", "compliance", "assertion-boundary", "class-3", "mil-prf-31032", "as9100", "dfars", "far", "boundary"]
---

# Canonical Summary

> Public IPC, SAE, military-spec, FAR, and DFARS records are strong enough to support guarded `22-layer` wording around standards hierarchy, contract-quality frameworks, and governance vocabulary. They are not strong enough to prove that any supplier or `22-layer` board complies with `IPC Class 3/3A`, `MIL-PRF-31032`, `MIL-PRF-55110`, or contract-specific higher-level quality requirements.

## Stable Facts

- A conservative `22-layer` rewrite may describe compliance-related language as framework context rather than verified conformance.
- Public `IPC-6011A`, `IPC-6012F`, and `IPC-A-600K` metadata support printed-board framework, rigid-board hierarchy, and acceptability vocabulary, not reusable compliance proof.
- Public `IPC-6012FA` metadata supports addendum-branch visibility, not technical compliance evidence.
- Public `AS9100D` metadata supports baseline `QMS` vocabulary under customer and regulatory precedence, not product compliance proof.
- Public `AS9101G` metadata supports audit-process identity, not audit success or conformity results.
- Public `MIL-PRF-55110`, `MIL-PRF-31032`, and `MIL-PRF-31032/1E` metadata support hierarchy and qualification-ecosystem vocabulary, not current conformance proof for a supplier or board.
- Public `DFARS 252.246-7008` and `FAR 52.246-11` metadata support source-hierarchy, traceability, and contract-quality-flowdown vocabulary, not proof that a given compliance obligation was invoked or met.
- These sources together support guarded wording such as `may be governed by`, `can sit inside`, `contract may invoke`, and `requires procurement confirmation`, not `complies with`.

## Conditions And Methods

- Use this card when a `22-layer` draft risks turning public framework metadata into direct claims such as `complies with`, `manufactured to`, or `meets standards`.
- Pair this card with `facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`, `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`, and `facts/standards/22-layer-supplier-status-marketing-boundary.md`.
- Prefer wording such as `publicly identifies a framework`, `may be contract-driven`, `belongs to program context`, and `does not prove conformance by itself`.
- Keep standards names, audit identities, and contract clauses attached to governance scope rather than conformance conclusions.

## Limits And Non-Claims

- This card does not prove `IPC Class 3/3A` compliance, `MIL-PRF-31032` qualification, `MIL-PRF-55110` standing, or contract-quality compliance for any `22-layer` supplier or board.
- It does not prove that any higher-level quality standard was invoked or flowed down in a specific procurement.
- It does not turn public standards hierarchy or military-spec identity into supplier conformance, release authority, or accepted-lot proof.
- It does not provide certificate evidence, clause-level conformity evidence, or customer-approval evidence.

## Open Questions

- Add a narrower supplier-evidence discipline only if future work needs actual conformance claims.
- Reassess `22-layer` readiness only after compliance-assertion leakage is fully separated from framework metadata.

## Source Links

- https://www.electronics.org/TOC/IPC-A-600K-EN_TOC.pdf
- https://www.electronics.org/TOC/IPC-6011A_TOC.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english-0
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://saemobilus.sae.org/standards/as9100d-quality-management-systems-requirements-aviation-space-defense-organizations
- https://saemobilus.sae.org/standards/as9101g-requirements-conducting-audits-aviation-space-defense-quality-management-systems
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=119627
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=29227
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=119628
- https://www.acquisition.gov/dfars/252.246-7008-sources-electronic-parts.
- https://www.acquisition.gov/far/52.246-11
