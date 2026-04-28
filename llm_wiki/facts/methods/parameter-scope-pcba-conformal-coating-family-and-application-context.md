---
fact_id: "methods-parameter-scope-pcba-conformal-coating-family-and-application-context"
title: "Conformal-coating parameter cards may use family and application-method context, with numbers only in named source context"
topic: "PCBA parameter scope for conformal coating family and application context"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "humiseal-conformal-coating-brochure"
  - "electrolube-conformal-coatings-archive"
  - "ipc-cc-830c-toc"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
tags: ["parameter-scope", "pcba", "conformal-coating", "humiseal", "electrolube", "ipc-cc-830", "application-method"]
---

# Canonical Summary

> For conformal coating, the stable parameter layer is family vocabulary plus application-method context. Real numbers are admissible only when tied to the exact source context that states them, such as the local APT coating page's own thickness description. That does not convert them into general HIL defaults or standards requirements.

## Source-Backed Parameters

- HumiSeal supports chemistry-family vocabulary such as acrylic, silicone, urethane, and parylene, plus general application-method framing.
- Electrolube supports manufacturer-controlled coating-family context and application-oriented knowledge categories, but the archive is dynamic and not a stable numeric source.
- The APT PCBA coating page exposes one explicit local context value: `1-5 mils` and `25-127 microns` as the page's stated thickness range for its conformal-coating description.
- The same APT page supports application-method vocabulary `manual spraying`, `automated spraying`, and `selective coating`.
- IPC-CC-830C is usable only as metadata and scope identity for the standard family; it does not authorize qualification limits, performance requirements, or pass/fail criteria.

## Scope And Applicability Limits

- Use this card for `conformal-coating-5g-6g-communication`, `conformal-coating-5g-6g-communication-2`, `conformal-coating-data-center-optical-module`, `conformal-coating-medical-imaging-wearable`, and `conformal-coating-automotive-adas-ev-power`.
- Safe broad reuse: family names, protection targets such as moisture / dust / chemicals / temperature exposure, and application-method categories.
- Safe numeric reuse is narrower: the `1-5 mils` / `25-127 microns` range may be cited only as `APTPCB page-stated conformal-coating thickness context`, not as a universal process window or supplier default.
- If a later draft needs cure timing, chemistry-specific thickness, dielectric behavior, adhesion testing, or environmental qualification, refresh from a product datasheet or licensed standard and keep the named product attached.

## Explicit Blocked Uses

- Do not turn the APT page's `1-5 mils` / `25-127 microns` range into generic coating thickness defaults for HIL, customer programs, or IPC.
- Do not infer cure defaults, cure schedules, cleanliness limits, masking dimensions, keep-out rules, or inspection thresholds from this card.
- Do not convert coating-family language into HIL capability claims, supplier superiority claims, yield claims, cost claims, or lead-time claims.
- Do not use IPC-CC-830C metadata as a substitute for qualification requirements or compliance proof.
- Do not claim one chemistry is universally best for telecom, optical, medical, automotive, charger, or inverter builds.

## Blog Usage

- empty-image slugs: `conformal-coating-5g-6g-communication`, `conformal-coating-5g-6g-communication-2`, `conformal-coating-data-center-optical-module`, `conformal-coating-medical-imaging-wearable`, `conformal-coating-automotive-adas-ev-power`
- families supported:
  - `conformal-coating`
  - `environmental-protection-workflow`
  - `masking-and-keep-access`

## Open Questions

- Product-level HumiSeal or Electrolube datasheets are still missing if a later draft needs chemistry-specific numeric properties.
- A future pass could add a dedicated card for named cure-method families only if those numbers are backed by stable product datasheets rather than by marketing or dynamic archive pages.

## Source Links

- https://info.humiseal.com/hubfs/Product%20Brochure-v4%5B93%5D.pdf
- https://electrolube.com/knowledge-product-type/conformal-coatings/
- https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
