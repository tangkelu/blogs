---
source_id: "murata-mlcc-test-probe-board-flex-precaution-faq"
title: "What should I pay attention to when mounting chip capacitors for inspection?"
organization: "Murata Manufacturing"
owner: "Murata Manufacturing"
source_type: "manufacturer_technical_faq"
url: "https://www.murata.com/support/faqs/capacitor/ceramiccapacitor/mnt/0016"
jurisdiction: "global"
checked_at: "2026-05-14"
retrieved_at: "2026-05-14"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_mounting_precaution_faq"
scope_type: "vendor_scoped_board_flex_and_test_probe_precaution"
source_origin_path: "official Murata HTML FAQ"
source_page_range: "HTML FAQ body"
confidence: "high"
topic_tags: ["murata", "mlcc", "inspection", "test-probe", "board-flex", "open-solder-joint", "mounting"]
status: "active"
notes: "Official Murata mounting FAQ. Safe for guarded statements that test-probe thrusting force can flex the PCB and cause cracked chips or open solder joints, and that backside support pins should be placed close to the probe point. Do not rewrite this as a universal fixture-force limit or geometry rule."
---

# Source Summary

## What It Covers

- Murata warns that the thrusting force of a test probe can flex the PCB during inspection.
- Murata states that this flexing can result in cracked chips or open solder joints.
- Murata recommends support pins on the back side of the PCB to prevent warping or flexing.
- Murata recommends placing those support pins as close to the test probe as possible.

## Why It Matters

- Gives the local corpus one official manufacturer source for the exact `test probe -> PCB flex -> cracked chips / open solder joints` failure chain.
- Supports dense-PCBA ICT writing that must explain why test-point planning is a mechanical-support problem, not only an electrical-access problem.

## Extraction Notes

- Safe for narrow statements about probe-force-induced board flex and the need for nearby support during inspection.
- Safe for guarded wording that cracked chips and open solder joints can be introduced during probing if support is poor.
- Do not use this page for exact fixture force, support-pin count, support-pin spacing, or universal keepout rules.

## Refresh Notes

- Refresh before reuse because the page is dynamic.
- Keep the claims tied to Murata's published mounting precaution scope.
