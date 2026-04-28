---
fact_id: "methods-telecom-node-board-context-vs-radio-coverage-claims"
title: "Telecom node board context does not authorize radio-coverage or capacity claims"
topic: "telecom node board context versus radio coverage claims"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "3gpp-38-series"
  - "3gpp-ts-38104-archive"
  - "frontendapt-industry-communication-equipment-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-large-volume-assembly-product-page-en"
tags: ["base-station", "pico-cell", "small-cell", "telecom-node", "rf-pcb", "coverage", "boundary"]
---

# Canonical Summary

> Current 3GPP and internal telecom/manufacturing sources are strong enough to frame `base station` and `pico cell` as compact or distributed telecom-node hardware contexts. They are not evidence for radio coverage, capacity, throughput, link budget, or supplier-qualified deployment outcomes. The safe rewrite lane is board partitioning, assembly control, inspection, and validation handoff.

## Stable Facts

- The 3GPP 38-series and TS 38.104 archive support identity-level 5G NR and base-station standards framing, with revision sensitivity explicitly preserved.
- The internal communication-equipment page supports application context for base stations, RRUs, AAUs, microwave links, and related telecom infrastructure hardware.
- The internal antenna, high-frequency, and microwave pages support board-level language around RF sections, connectors, transitions, shielding, and material review.
- The internal NPI, PCBA quality, turnkey, and volume-assembly pages support execution language around revision control, sourcing, assembly flow, inspection, traceability, and staged release.
- Together, these sources support conservative language that telecom-node hardware often mixes RF, digital, power, thermal, and manufacturability constraints on one program.

## Conditions And Methods

- Use this card for `5g-base-station-5g-telecom` and `5g-pico-cell-5g-telecom`.
- Treat `base station` and `pico cell` as hardware-deployment context only, then translate immediately into board partitioning, connector and enclosure awareness, shielding, fine-pitch assembly review, and program-specific validation access.
- Pair this card with `facts/methods/5g-rf-system-context-vs-pcb-execution-boundary.md`, `facts/standards/5g-nr-standards-identity-and-revision-boundary.md`, and `facts/methods/rf-validation-capability.md`.
- Prefer wording such as `compact telecom node`, `mixed-signal telecom hardware`, `requires project-specific board review`, and `needs staged manufacturing validation`.

## Limits And Non-Claims

- This card does not authorize cell radius, coverage, throughput, capacity, latency, handoff, or deployment-density claims.
- It does not authorize radio budget, antenna count, band support, FR1/FR2 values, or protocol-compliance claims.
- It does not authorize operator qualification, supplier approval, field uptime, availability, or deployment-success claims.
- It does not authorize thermal, power, or enclosure numerics unless a separate current primary source exists for the exact statement.
- It does not prove any named base-station or small-cell product architecture beyond general telecom-node context.

## Open Questions

- Add a smaller-cell taxonomy source layer only if future drafts need public small-cell vocabulary beyond `compact telecom node hardware`.
- Add dated public architecture sources only if later rewrites need to distinguish AAU, RRU, DU, or other system roles.

## Source Links

- https://www.3gpp.org/dynareport?code=38-series
- https://www.3gpp.org/ftp/specs/archive/38_series/38.104/
- /code/hileap/frontendAPT/public/static/industries/en/communication-equipment-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/npi-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/large-volume-assembly.json
