---
source_id: "ti-managing-emi-in-class-d-audio-applications"
title: "AN-1737 Managing EMI in Class D Audio Applications"
organization: "Texas Instruments"
source_type: "application_note"
url: "https://www.ti.com/lit/pdf/SNAA050"
jurisdiction: "global"
published_at: "2013-05"
checked_at: "2026-05-02"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
topic_tags: ["texas-instruments", "audio", "class-d", "emi", "pcb-layout", "floor-planning", "speaker-routing", "connectors"]
status: "active"
notes: "Official TI application note. Use for class-D audio EMI posture, PCB floor planning, connector filtering, loop-antenna avoidance, and short speaker-path language only; do not use it as proof of audio performance, EMI compliance, or exact filter design."
---

# Source Summary

## What It Covers

- PCB floor planning as part of EMI control for class-D audio applications
- Long traces, vias, component leads, and unpopulated connectors as unintended antennas
- General PCB guidelines around decoupling, plane-edge treatment, avoiding cuts in planes, connector filtering, and loop-antenna avoidance
- Audio-specific guidance to keep amplifier-to-speaker traces short in filterless class-D systems

## Why It Matters

- Supports a narrow audio-amplifier board-review lane centered on sensitive-versus-noisy partitioning, connector and speaker-path review, and EMI-aware floor planning.

## Extraction Notes

- Safe for statements that class-D audio board review should include floor planning, connector filtering, avoidance of unintended antenna structures, and caution around speaker-output trace length.
- Safe to describe EMI as a system-level concern that spans circuit, layout, and manufacturing review.
- Do not use this source for exact EMI limits, compliance pass claims, ferrite-bead selection recipes, or audio-quality proof.

## Refresh Notes

- Refresh before publication if TI updates the note revision or exact wording matters.
