---
fact_id: "standards-high-reliability-configuration-control-and-problem-reporting-metadata"
title: "Public NASA and DLA records support configuration-control and problem-reporting vocabulary for hi-rel PCB writing, not proof of qualification"
topic: "high reliability configuration control and problem reporting metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "nasa-configuration-management-page"
  - "nasa-std-0005-configuration-management-page"
  - "nasa-gidep-page"
  - "dla-counterfeit-detection-avoidance-program-page"
tags: ["high-reliability", "configuration-management", "baseline-control", "audit", "gidep", "nonconforming-items", "counterfeit", "dla", "nasa", "metadata"]
---

# Canonical Summary

> Public NASA and DLA records are now strong enough to support a guarded configuration-control and problem-reporting layer in `llm_wiki`: NASA configuration-management guidance for baselines, change control, accounting, and verification/audits; `NASA-STD-0005` for the formal configuration-management function vocabulary; NASA `GIDEP`/advisories for nonconforming-item and counterfeit/problem-part reporting; and DLA `CDAP` for traceability-documentation and counterfeit-avoidance workflow language. None of these pages prove supplier qualification, audit passage, or approval for a given PCB lot or manufacturer.

## Stable Facts

- NASA publicly frames configuration management as a lifecycle discipline for identifying configurations, controlling changes, maintaining configuration integrity/traceability, and preserving configuration records.
- NASA's public systems-engineering guidance explicitly uses vocabulary around baselines, configuration identification, configuration control, configuration accounting, configuration verification, and audits.
- `NASA-STD-0005` publicly confirms a formal NASA standard identity for configuration-management functions including traceability and audits, while also showing the standard is inactive for new design.
- NASA's `GIDEP` page publicly frames a cooperative ecosystem for exchanging significant problem and nonconforming item data and explicitly links that ecosystem to avoiding counterfeit, known-problem, or discontinued parts and materials.
- DLA's public `CDAP` page publicly frames counterfeit detection/avoidance as a supply-chain control activity and explicitly connects high-risk electronic-part supply to traceability documentation and test-report workflows.

## Conditions And Methods

- Use this card when a `22-layer` or other hi-rel draft needs vocabulary for configuration baselines, change-control boards, configuration audits, nonconforming-item reporting, or counterfeit-avoidance reporting ecosystems.
- Pair this card with supplier-specific evidence, contractual flowdowns, and program documents before making claims about audit status, approved baselines, or release authority.
- Use this card to avoid flattening configuration-control and advisories language into generic supplier-qualification claims.

## Limits And Non-Claims

- This card does not prove that any supplier participates in `GIDEP`, complies with `CDAP`, or operates under NASA configuration-management requirements.
- It does not provide audit criteria, report templates, change-board composition rules, or contract-specific traceability deliverables.
- It does not establish approval, qualification, or release status for any multilayer PCB design, lot, or supplier.

## Open Questions

- Decide whether future hi-rel evidence packs need a separate organizational-ecosystem card for NASA / DLA / GIDEP / advisory participation claims.
- Decide whether configuration-control vocabulary should remain in a separate card from traceability/counterfeit-control or merge later if prompt retrieval benefits from consolidation.

## Source Links

- https://www.nasa.gov/reference/6-5-configuration-management/
- https://standards.nasa.gov/standard/NASA/NASA-STD-0005
- https://sma.nasa.gov/sma-disciplines/gidep
- https://www.dla.mil/Land-and-Maritime/Business/Selling/Counterfeit-Detection-Avoidance-Program
