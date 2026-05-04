---
topic_id: "processes-international-pcb-procurement-shipping-boundaries"
title: "International PCB Procurement Shipping Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-international-pcb-shipping-customs-document-boundary"
source_ids:
  - "icc-incoterms-rules"
  - "dhl-customs-clearance-documents"
  - "dhl-customs-duties-and-taxes"
  - "fedex-international-transit-notes"
tags: ["pcb-procurement", "shipping", "customs", "incoterms", "commercial-invoice", "lead-time"]
---

# Definition

> International PCB procurement shipping content must keep factory production time, document readiness, customs processing, and carrier transit as separate lanes. The landed source set supports trade-term allocation, customs-document completeness, duty and tax risk, and carrier transit caveats, but it does not support customs-clearance guarantees, delivery-date guarantees, tariff-outcome claims, or factory lead-time claims from shipping sources.

## Routing Guidance

- Use this page for international PCB and PCBA shipping language about Incoterms, document readiness, customs-document completeness, duties and taxes, and carrier transit caveats.
- Route manufacturing turnaround, quick-turn promises, and factory schedule claims elsewhere; shipping sources do not prove fabrication lead time.
- Route importer, broker, legal, and tax advice elsewhere; this page only supports procurement-content boundaries.
- Route country-specific duty, tax, de minimis, and import-control statements to refresh-required review before publication.

## Why This Topic Matters

- International PCB procurement drafts often collapse quote timing, fabrication timing, customs timing, and transit timing into one delivery promise.
- The landed fact record already supports a cleaner split between trade-term responsibility, document completeness, duty and tax variability, and transit estimates.
- This page provides a single routing boundary so shipping language does not drift into unsupported factory, customs, or tariff promises.

## Stable Facts

- Incoterms define delivery-related tasks, costs, and risks between seller and buyer.
- The current source-backed boundary uses `Incoterms 2020` only as trade-term governance, not as proof of transit or clearance outcomes.
- The commercial invoice is a primary customs document and must carry specific shipment data such as seller, buyer, goods description, value, currency, origin, tariff code, quantity, and weight.
- Vague customs descriptions such as `parts` or `samples` are not sufficient for PCB or PCBA shipment content.
- Duties and taxes depend on jurisdiction, classification, and customs value logic.
- Carrier transit-time displays assume shipment data and service conditions that may exclude customs delays.
- Additional clearance time can apply for certain commodities or higher-value shipments.

## Engineering Boundaries

- Keep factory quote time, factory build time, export and import document readiness, customs processing, and carrier transit as separate clocks.
- Use `shipping estimate` only for carrier movement, not for total procurement lead time.
- Use `document-ready` only when commercial-invoice and shipment data fields are complete enough for customs filing context.
- Do not convert shipping-source material into PCB HS-code assignments, tariff rates, tax rates, or broker advice.
- Do not use customs or carrier pages as evidence for factory lead-time, quote-speed, SLA, or landed-cost guarantees.

## Blocked Claims

- customs-clearance guarantees
- delivery-date guarantees
- tariff-outcome claims
- factory lead-time claims from shipping sources

## Common Misreadings

- `DDP` or another Incoterms term does not mean customs delay risk disappears.
- A carrier transit estimate is not the same as total order delivery time.
- A complete airway bill or invoice package is not a customs-clearance guarantee.
- `Free shipping` language does not remove duties, taxes, or broker charges.
- A shipping-source statement about customs paperwork does not prove PCB tariff classification or manufacturing speed.

## Must Refresh Before Publishing

- Any country-specific duty, tax, tariff, de minimis, importer-of-record, broker-responsibility, or restricted-goods claim
- Any route-specific service promise, transit-day estimate, or carrier SLA
- Any PCB-specific HS code, tariff-rate, tax-rate, or customs-treatment claim
- Any current factory lead-time, quick-turn, delivery-window, or landed-cost statement

## Related Facts And Source Scope

- `methods-international-pcb-shipping-customs-document-boundary` is the governing fact card for trade-term allocation, customs-document completeness, duties and taxes variability, and carrier transit caveats.

## Source Scope

- `icc-incoterms-rules`
- `dhl-customs-clearance-documents`
- `dhl-customs-duties-and-taxes`
- `fedex-international-transit-notes`
