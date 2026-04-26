---
fact_id: "compliance-rohs-reach-svhc"
title: "RoHS and SVHC data require live-date handling"
topic: "RoHS REACH SVHC"
category: "compliance"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids: ["ec-rohs-directive", "ec-rohs-implementation", "echa-candidate-list", "echa-candidate-list-news-2026-02-04"]
tags: ["rohs", "reach", "svhc", "compliance", "regulation"]
---

# Canonical Summary

> In PCB/PCBA content, RoHS logic can be summarized statically, but exemption status and SVHC list counts are live compliance data and should always be checked against current official pages before publication.

## Stable Facts

- The European Commission describes RoHS as EU rules restricting hazardous substances in electrical and electronic equipment.
- The current RoHS directive overview page states the latest RoHS directive entered into force on `21 July 2011`.
- The Commission implementation page states RoHS exemptions are limited in time and reassessed regularly.
- The same implementation page states an exemption decision currently takes about `18 to 24 months` from the application date.
- ECHA states that the Candidate List published on its website is the authentic version for legal-obligation purposes.
- ECHA's `2026-02-04` news release states that the Candidate List reached `253` entries on that date.

## Conditions And Methods

- Use regulator pages to explain what RoHS is and how exemption review works.
- Use ECHA's live Candidate List page for current SVHC checks.
- Keep any Candidate List count tied to an explicit date.

## Limits And Non-Claims

- Do not present an old Candidate List count as evergreen.
- Do not assume an exemption remains valid without checking the current implementation status.
- Do not collapse REACH article obligations and RoHS substance restrictions into the same rule set.

## Open Questions

- Add a separate card for SCIP notification logic if your content will discuss article disclosure workflows

## Source Links

- https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive_en
- https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive/implementation-rohs-directive_en
- https://www.echa.europa.eu/candidate-list-table
- https://www.echa.europa.eu/-/echa-adds-two-hazardous-chemicals-to-the-candidate-list-1
