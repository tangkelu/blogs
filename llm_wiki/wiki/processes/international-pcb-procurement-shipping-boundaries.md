---
topic_id: "processes-international-pcb-procurement-shipping-boundaries"
title: "International PCB Procurement Shipping Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-28"
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

> International PCB procurement content must separate four clocks: factory quote/manufacturing time, export/import document readiness, customs clearance, and carrier transit. Official shipping sources can support document and risk allocation boundaries, not PCB factory delivery promises.

## Stable Facts

- Incoterms allocate delivery-related tasks, costs, and risks between seller and buyer.
- Customs documents need specific goods descriptions and commercial data; vague descriptions can block or delay clearance.
- Duties and taxes are jurisdictional and classification-dependent.
- Carrier transit-time estimates depend on shipment data and assume no clearance delays unless otherwise stated.

## Writing Boundaries

- Say `shipping estimate` only for carrier movement, not total order lead time.
- Say `landed-cost risk` when duties, taxes, freight, insurance, and classification can change the buyer's actual cost.
- Say `document-ready` only when invoice, AWB, origin, tariff-code, value, quantity, and weight data are prepared.
- Do not promise customs clearance, delivery dates, or tariff outcomes from a PCB blog draft.

## Common Overclaims

- `Fast-turn PCB` implying international delivery is guaranteed.
- `DDP` or any Incoterms term implying customs clearance cannot delay the shipment.
- `Free shipping` implying duties, taxes, or broker charges do not exist.
- `Samples` or `parts` as sufficient customs descriptions for PCB / PCBA shipments.

## Must Refresh Before Publishing

- Country-specific import duties, taxes, de minimis thresholds, customs-document rules, restricted-goods rules, and broker-responsibility statements.
- Any current service promise, quote speed, lead time, MOQ, stock, carrier SLA, or route-specific delivery date.

## Related Fact Cards

- `methods-international-pcb-shipping-customs-document-boundary`

## Primary Sources

- https://iccwbo.org/business-solutions/incoterms-rules/
- https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-clearance-documents.html
- https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-duties-and-taxes.html
- https://www.fedex.com/en-us/please_notes/wgrt/us/us/pn_expintlresults.html
