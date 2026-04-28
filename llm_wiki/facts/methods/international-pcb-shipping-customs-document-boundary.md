---
fact_id: "methods-international-pcb-shipping-customs-document-boundary"
title: "International PCB shipping content can use customs-document and trade-term governance, but not delivery guarantees"
topic: "International PCB shipping customs document boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "icc-incoterms-rules"
  - "dhl-customs-clearance-documents"
  - "dhl-customs-duties-and-taxes"
  - "fedex-international-transit-notes"
tags: ["shipping", "customs", "commercial-invoice", "incoterms", "transit-time", "pcb-procurement"]
---

# Canonical Summary

> International PCB and PCBA shipping articles may explain Incoterms, customs documents, duties/taxes, HS-code dependency, and carrier transit caveats. They must not turn those sources into PCB-specific tariff rates, customs-clearance guarantees, or manufacturing lead-time promises.

## Stable Facts

- ICC defines Incoterms rules as eleven three-letter trade terms for business-to-business contracts for the sale and purchase of goods.
- ICC states that Incoterms rules clarify delivery-related tasks, costs, and risks between seller and buyer; the current `Incoterms 2020` edition entered into force on `1 January 2020`.
- DHL identifies the commercial invoice as the primary customs document and lists required customs data such as seller, buyer, goods description, value, currency, origin, tariff code, quantity, and weight.
- DHL explicitly rejects vague goods descriptions such as `parts` or `samples`; PCB shipments should use specific plain-language descriptions and classification data.
- DHL states that most international shipments are subject to customs duties and taxes, and that duties are tied to HS-code classification and customs value logic.
- FedEx transit-time notes state that certain commodities and high-value shipments can require additional clearance time, and that displayed service options assume no clearance delays.

## Conditions And Methods

- Use this fact for PCB procurement, delivery, logistics, landed-cost, and international shipping articles.
- Keep trade-term allocation, customs-document completeness, carrier transit estimates, and factory manufacturing lead time as separate concepts.
- Refresh jurisdiction-specific official sources before publishing current de minimis, tariff, tax, restricted-goods, or broker-responsibility claims.

## Limits And Non-Claims

- This card does not provide PCB HS codes, tariff rates, tax rates, export-control status, or customs broker advice.
- It does not prove any HILPCB / APTPCB / Highleap delivery time, quote speed, customs-clearance speed, landed cost, or carrier SLA.
- It does not replace importer, broker, legal, or tax review.

## Open Questions

- Refresh CBP pages or other official customs pages before adding importer-of-record responsibility facts.
- Add country-specific customs records if future blogs target the EU, UK, Canada, Japan, or other destination markets.

## Source Links

- https://iccwbo.org/business-solutions/incoterms-rules/
- https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-clearance-documents.html
- https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-duties-and-taxes.html
- https://www.fedex.com/en-us/please_notes/wgrt/us/us/pn_expintlresults.html
