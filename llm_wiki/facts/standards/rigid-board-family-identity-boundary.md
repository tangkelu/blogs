---
fact_id: "standards-rigid-board-family-identity-boundary"
title: "Public rigid-board standards metadata plus internal baseline and multilayer pages support family identity for double-sided and 4-layer rigid boards"
topic: "Rigid-board family identity boundary"
category: "standards"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "ipc-6012f-toc"
  - "mil-prf-55110-general-spec-page"
  - "frontendhil-single-double-layer-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
tags: ["rigid-board", "double-sided", "single-sided", "multilayer", "4-layer", "board-family", "standards-boundary", "baseline-vs-multilayer"]
---

# Canonical Summary

> The current source layer is strong enough to support a conservative rigid-board family boundary: double-sided boards belong to the baseline rigid-board branch, while 4-layer boards belong to the multilayer rigid-board branch. Public IPC and DLA metadata support the broader rigid-board standards family, and internal HIL / APT pages support the baseline-versus-multilayer manufacturing split. These sources do not authorize manufacturer-ranking language, capability tables, lead-time promises, or default stackup recipes.

## Stable Facts

- Public `IPC-6012F` metadata supports document identity and broad scope for qualification and performance of rigid printed boards.
- Public `MIL-PRF-55110` metadata supports a rigid-board family scope that explicitly includes rigid single-sided, double-sided, and multilayer printed wiring boards, while also showing the document as inactive legacy military-spec context.
- The internal HIL single/double-layer page supports a baseline low-layer rigid-board branch associated with simpler routing and faster manufacturing posture.
- The internal HIL multilayer page supports a separate multilayer rigid-board branch where stackup architecture, registration control, via strategy, and impedance review become more prominent.
- The internal APT multilayer page supports multilayer build framing around sequential lamination, registration, backdrill, and impedance language as complexity increases.
- Together, these sources support a guarded family identity layer:
  `single-sided / double-sided baseline rigid boards` versus `multilayer rigid boards such as 4-layer`.

## Conditions And Methods

- Use this card for `4-layer-pcb-manufacturing.md` and `double-sided-pcb-manufacturer.md` only when the goal is to explain board-family position and complexity boundary.
- Safe `double-sided` posture:
  place it in the baseline rigid-board family with plated-through-hole interconnection and lower complexity than multilayer work.
- Safe `4-layer` posture:
  place it in the multilayer rigid-board family rather than in the single/double-sided baseline branch.
- Keep standards-family identity separate from supplier-selection and quote-advice language.
- Pair this card with `methods-pcb-prototype-quickturn-and-volume-routing`, `methods-pcb-stackup-special-process-and-baseline-families`, and `processes-prototype-vs-quick-turn-pcb-routing` when the prompt needs routing-mode or stackup-planning context.

## Limits And Non-Claims

- This card does not authorize default 4-layer stackups, plane assignments, impedance geometry, EMI outcomes, or thermal outcomes.
- It does not authorize manufacturer-selection advice, `best manufacturer` language, supplier-proof framing, or commercial recommendations.
- It does not authorize current capability tables, lead times, MOQ, yield, quality-rate, certification, or delivery promises.
- It does not prove that every double-sided board is simpler in every application or that every 4-layer board needs advanced features such as HDI, backdrill, or special materials.
- It does not extract class-specific requirements, pass/fail limits, or design-rule details from public IPC or DLA metadata pages.

## Open Questions

- Add narrower public IPC design-standard metadata if a future pass needs a conservative board-hierarchy bridge from baseline rigid boards into multilayer design context.
- Add stronger official or dated internal evidence before publishing any stackup, manufacturability-limit, or supplier-comparison claims for this draft family.

## Source Links

- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=29227
- /code/hileap/frontendHIL/public/static/products/en/single-double-layer-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/multilayer-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/multilayer-pcb.json
