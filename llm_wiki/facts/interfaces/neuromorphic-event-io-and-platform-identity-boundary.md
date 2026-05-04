---
fact_id: "interfaces-neuromorphic-event-io-and-platform-identity-boundary"
title: "Loihi 2, Akida, Speck, Xylo, DVS, and PMBus are identity-only nouns, not PCB capability proof"
topic: "neuromorphic identity-only noun boundary"
category: "interfaces"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "intel-neuromorphic-computing-page"
  - "intel-loihi-2-technology-brief-page"
  - "brainchip-akida-page"
  - "synsense-speck-page"
  - "synsense-xylo-page"
  - "synsense-dvs-page"
  - "pmbus-about-page"
  - "pmbus-current-specifications-page"
tags: ["loihi-2", "akida", "speck", "xylo", "dvs", "pmbus", "neuromorphic", "identity-boundary", "interface-boundary"]
---

# Canonical Summary

> Intel, BrainChip, SynSense, and PMBus owner pages support a narrow identity-only lane for neuromorphic writing: `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus` may be named as source-backed platform or protocol nouns. This card does not authorize interface behavior, board capability, system readiness, or supplier readiness.

## Stable Facts

- Intel's neuromorphic computing pages and Loihi 2 brief support `Loihi 2` as an Intel neuromorphic platform noun.
- BrainChip's Akida page supports `Akida` as a BrainChip neuromorphic platform noun.
- SynSense's product pages support `Speck`, `Xylo`, and `DVS` as SynSense neuromorphic product or series nouns.
- PMBus's about and current-specifications pages support `PMBus` as the Power Management Bus name and specification family.

## Conditions And Methods

- Use this card only for `neuromorphic-computing-pcb.md` when the draft needs identity-only nouns and no capability claim.
- Keep `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus` at name level.
- Pair this card with existing board-review and interface-boundary pages before any broader rewrite.

## Limits And Non-Claims

- This card does not authorize `AER`, `STDP`, or `silicon cochlea`.
- It does not authorize `PCIe`, `USB 3.2`, `Ethernet`, or `LVDS`.
- It does not authorize production, deployment, readiness, power, noise, skew, jitter, thermal, layer-count, or turnaround numerics.
- It does not authorize supplier capability claims.
- It does not authorize interface behavior, performance, interoperability, or board-compliance claims for `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, or `PMBus`.

## Open Questions

- Add narrower owner or product pages only if future drafts must name other neuromorphic families.
- Add a separate interface card only if a later rewrite needs independently sourced interface nouns or exact electrical / protocol behavior.

## Source Links

- https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html
- https://www.intel.com/content/www/us/en/research/neuromorphic-computing-loihi-2-technology-brief.html
- https://brainchip.com/product/
- https://www.synsense.ai/products/speck-2/
- https://www.synsense.ai/products/xylo
- https://www.synsense.ai/products/dvs/
- https://pmbus.org/about-pmbus/
- https://pmbus.org/current-specifications/
