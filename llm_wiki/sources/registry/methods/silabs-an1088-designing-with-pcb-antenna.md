---
source_id: "silabs-an1088-designing-with-pcb-antenna"
title: "AN1088 Designing with an Inverted-F 2.4 GHz PCB Antenna"
organization: "Silicon Labs"
source_type: "application_note"
url: "https://www.silabs.com/documents/public/application-notes/an1088-designing-with-pcb-antenna.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-05"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["antenna", "pcb-antenna", "2.4ghz", "keep-out", "layout", "wireless", "smart-home"]
status: "active"
notes: "Official Silicon Labs antenna-layout note. Use for antenna-region discipline, keep-out, and nearby-metal sensitivity wording; avoid turning it into universal geometry rules."
---

# Source Summary

## What It Covers

- PCB antenna implementation for compact wireless boards
- Sensitivity of antenna performance to nearby ground, copper, and mechanical placement
- Need to preserve antenna region discipline rather than treating it as ordinary layout space

## Why It Matters

- Provides an official source for careful antenna-placement language in smart-lock and compact IoT board articles without inventing universal keep-out numbers.

## Extraction Notes

- Safe for guarded wording that antenna regions should follow the module or antenna vendor's keep-out and placement guidance.
- Safe for statements that nearby metal, copper, and enclosure changes can detune or weaken antenna behavior.
- Do not use this note as authority for universal clearance values, range guarantees, or certification outcomes.

## Refresh Notes

- Refresh before publication because antenna notes and linked hardware guidance may be revised.
