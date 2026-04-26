---
fact_id: "methods-pcba-npi-to-mass-production-gates"
title: "Internal PCBA pages frame NPI, pilot, small-batch, and mass production as gated stages"
topic: "PCBA NPI to mass-production gates"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendapt-pcba-small-batch-page-en"
  - "frontendapt-pcba-mass-production-page-en"
  - "frontendapt-pcba-support-services-page-en"
  - "frontendhil-small-batch-assembly-product-page-en"
  - "frontendhil-large-volume-assembly-product-page-en"
tags: ["internal", "pcba", "npi", "pilot", "small-batch", "mass-production", "methods"]
---

# Canonical Summary

> The internal PCBA pages present development ramp, pilot execution, small-batch production, and mass production as different operating stages with gate checks in between, rather than as one generic build mode.

## Stable Facts

- The first-article page frames FAI as an early-run confirmation point before broader release.
- The NPI assembly page frames prototype and pilot builds as part of launch stabilization.
- The small-batch page frames low-volume work as a distinct production posture.
- The mass-production page frames higher-volume work as a later, more repeatable execution mode.
- The support-services page reinforces the idea that engineering and manufacturing support span more than one volume stage.
- The HIL small-batch assembly page reinforces prototype and NPI framing as a controlled pre-volume posture.
- The HIL large-volume assembly page reinforces volume production as a more automated and statistically managed execution mode.

## Conditions And Methods

- Use this card when explaining why launch programs need explicit gates between prototype, pilot, and production.
- Keep the framing program-specific rather than assuming every board follows the same ramp path.
- Refresh any volume, timing, or yield claims before publication.

## Limits And Non-Claims

- This card does not claim all programs require the same number of gates.
- It does not claim a specific capacity threshold defines NPI, small batch, or mass production.
- It does not replace a project ramp plan or approval workflow.

## Open Questions

- Add a later topic page for `pcba-ramp-from-npi-to-volume`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/npi-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/small-batch.json
- /code/hileap/frontendAPT/public/static/pcba/en/mass-production.json
- /code/hileap/frontendAPT/public/static/pcba/en/support-services.json
- /code/hileap/frontendHIL/public/static/products/en/small-batch-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/large-volume-assembly.json
