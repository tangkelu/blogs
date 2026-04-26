---
source_id: "frontendapt-pcba-remaining-index-en"
title: "APTPCB Remaining English PCBA JSON Index"
organization: "APTPCB"
source_type: "internal_json_group"
url: "/code/hileap/frontendAPT/public/static/pcba/en"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-04-24"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "aptpcb", "pcba", "box-build", "index", "x-ray"]
status: "active"
notes: "Directory-level registry record for remaining APT English PCBA JSON files not individually registered or intentionally treated as duplicates."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendAPT/public/static/pcba/en/box-build-assembly.json`
- `/code/hileap/frontendAPT/public/static/pcba/en/index.json`
- `/code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json`

## Why It Matters

- Captures the remaining PCBA index/box-build framing and the duplicate x-ray spelling variant after the main PCBA extraction batch.

## Extraction Notes

- Use the existing `frontendapt-pcba-xray-inspection-page-en` record for X-ray inspection facts.
- Use this source only as grouped support unless a page later needs a dedicated fact card.

## Refresh Notes

- Re-check if `x-ray-inspection.json` diverges from `xray-inspection.json` or the PCBA index gains unique content.
