---
fact_id: "methods-internal-application-scenario-coverage-map"
title: "APT industry pages provide reusable application-scenario coverage across ten electronics markets"
topic: "Internal application scenario coverage"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-automotive-electronics-page-en"
  - "frontendapt-industry-communication-equipment-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-industry-robotics-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-industry-server-data-center-page-en"
tags: ["internal", "applications", "industries", "scenario-coverage", "pcb", "pcba"]
---

# Canonical Summary

> The APT industry pages form a reusable internal application-scenario layer across ten electronics markets. They are suitable for market and use-case framing, but they do not by themselves prove certifications, customer approvals, or regulated-program qualification.

## Stable Facts

- The current internal corpus includes dedicated application pages for aerospace and defense, automotive and EV, telecom and 5G, drone and UAV, industrial control, medical, power and new energy, robotics, security equipment, and server/data-center hardware.
- Across those pages, APT consistently frames PCB and PCBA work around application clusters rather than around one generic industry list.
- The pages repeatedly connect market framing to concrete hardware categories such as avionics, BMS, inverters, base stations, UAV flight controllers, PLCs, medical imaging, solar inverters, robot controllers, surveillance devices, and server/backplane hardware.
- This gives `llm_wiki` a stable internal scenario layer for evidence-pack discovery and topic routing.

## Conditions And Methods

- Use this card to decide whether a blog or prompt has an internal application-scenario anchor in the site corpus.
- Treat the industry pages as scenario framing and service-language support, not as proof of sector-specific certification or customer deployment history.
- Refresh any qualification, compliance, or approval statement before publication.

## Limits And Non-Claims

- This card does not prove current certifications for any regulated market.
- It does not prove a shipped customer history in every scenario named by the pages.
- It does not replace standards, regulatory, or customer-program sources.

## Open Questions

- Add scenario-specific topic pages if future prompts need deeper split by regulated, high-reliability, or infrastructure-heavy markets.
- Decide whether APT `capabilities` and `industry` pages should later be merged into a broader internal solution-map wiki.

## Source Links

- /code/hileap/frontendAPT/public/static/industries/en/aerospace-defense-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/automotive-electronics-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/communication-equipment-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/power-energy-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/robotics-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/security-equipment-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/server-data-center-pcb.json
