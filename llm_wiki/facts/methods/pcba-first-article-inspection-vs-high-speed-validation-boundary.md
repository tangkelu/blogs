---
fact_id: "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
title: "First-article inspection is a launch and documentation gate, not a substitute for high-speed validation"
topic: "PCBA first article inspection versus high-speed validation boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-15"
source_ids:
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "as9102c-first-article-inspection-page"
  - "iaqg-9102-page"
  - "as9145-page"
tags: ["fai", "first-article-inspection", "npi", "high-speed", "si", "methods", "boundary"]
---

# Canonical Summary

> The current evidence base supports a narrow but useful distinction: `FAI` is an early-run verification and documentation gate that confirms build readiness and process alignment, while high-speed performance claims still depend on separate signal-path design and validation work.

## Stable Facts

- The internal first-article inspection page frames FAI as early-run verification, setup confirmation, and NPI release support.
- The PCBA quality-system page places front-end review, inspection, electrical or functional validation, and traceability into one broader quality flow rather than collapsing them into a single first-build event.
- The high-speed PCB page ties high-speed success to stackup, impedance, and validation posture instead of treating it as a byproduct of generic launch inspection.
- The SAE `AS9102C` page provides the official identity and scope framing for performing and documenting first article inspection.
- The IAQG `9102` page frames first article inspection as a standardized process and documentation approach across the aerospace, space, and defense supply chain.
- The SAE `AS9145` page reinforces that product and process validation language extends beyond the identity of FAI alone.
- The local APT quality and first-article surfaces also support a writing-safe `launch control` framing: FAI belongs to first-build package confirmation, traceable review, and process alignment before the route is treated as ready to scale.

## Conditions And Methods

- Use this card when a rewrite needs safe wording such as `FAI helps confirm that the first build matches the released package and planned process`.
- Keep `FAI` attached to launch control, documentation discipline, and early-run verification.
- If a draft also discusses `high-speed SI`, pair this card with impedance, stackup, and validation cards rather than letting FAI absorb those claims.
- Refresh the standards-page metadata before publication if a draft names `AS9102C`, `9102`, or `AS9145` directly.

## Failure Pattern Translation

- For `FAI / BOM / release-package / NPI` topics, the most useful local failure chain is not `FAI is important`, but `small package ambiguity gets multiplied by automation before downstream test catches it`.
- Safe local wording can describe a typical factory-floor setup such as:
  - a mixed BOM contains an unapproved substitute or unclear AVL status
  - polarity, `Pin 1`, or placement rotation in the tape-and-reel flow does not match the released drawing or coordinate assumptions
  - the line program is released without a strong documented `FAI halt-and-verify` stop gate
  - SMT placement then repeats the same wrong assumption across the lot
  - electrical test, power-on, or debug finds the issue only after batch-level rework or scrap risk already exists
- This card therefore supports a stronger public explanation of why `FAI` is a brake point before scale, not merely a paperwork step after the first board appears.

## CTA Consumption Hints

- If the article ends with an engineering CTA, keep it tied to release-package readiness rather than generic quoting language.
- Safe intake-package wording can ask for:
  - BOM with `AVL` and approved-substitute status
  - assembly drawing and revision-controlled notes
  - `Gerber` plus placement or coordinate data
  - expected `FAI`, inspection, and downstream test ownership
- Safe promise wording should stay at `review`, `readiness check`, `ambiguity exposure`, or `launch-gate alignment` level unless a site-specific SLA is publicly exposed.

## Limits And Non-Claims

- This card does not prove a supplier completed an `AS9102`-compliant package for any specific program.
- It does not authorize eye-diagram, jitter, insertion-loss, skew, or channel-pass claims.
- It does not state that FAI alone can release a high-speed product to production.
- It does not authorize universal batch size, yield, scrap, or turnaround numerics for FAI scenarios.

## Open Questions

- Add a later card if the corpus needs a narrower `npi-launch-gates-for-high-speed-pcba` treatment.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-speed-pcb.json
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
- https://iaqg.org/standard/9102-first-article-inspection-requirement/
- https://saemobilus.sae.org/standards/as9145-aerospace-series-requirements-advanced-product-quality-planning-production-part-approval-process
