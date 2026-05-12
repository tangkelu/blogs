---
fact_id: "methods-ddr-memory-interface-routing-governance-boundary"
title: "Intel EMIF guidance supports a narrow DDR memory-interface routing-governance boundary without numeric DDR recipes"
topic: "DDR memory-interface routing governance, reference-plane continuity, return vias, skew matching, and serpentine compensation"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "intel-emif-ddr4-general-layout-routing-guidelines"
  - "ti-high-speed-layout-guidelines"
  - "analog-devices-mixed-signal-pcb-layout-guidelines"
  - "nxp-an11397-ptn3363-pcb-layout-guidelines"
tags: ["ddr", "memory-interface", "reference-plane", "return-path", "ground-stitching-vias", "length-match", "skew-match", "serpentine", "methods"]
---

# Canonical Summary

> Current public owner guidance is strong enough to support one narrow memory-interface routing boundary: DDR/EMIF routing should preserve a solid reference-plane and local return path, manage layer transitions with nearby ground stitching vias, avoid unnecessary signal-layer changes, and treat time-domain length / skew matching and serpentine routing as controlled timing-compensation governance. This does not authorize handbook-derived numeric DDR recipes, universal timing budgets, or any proof that a specific board supports DDR4 or DDR5.

## Stable Facts

- Intel's Agilex 7 EMIF user guide gives a current-public memory-interface layout source for routing from FPGA to memory.
- Intel explicitly frames memory-interface routing around solid ground reference planes and uninterrupted return-current paths.
- Intel ties memory-interface layer transitions to nearby ground stitching vias and warns against unnecessary signal-layer transitions because they can add crosstalk, loss, and skew risk.
- Intel names time-domain length and skew matching as routing goals for the memory interface.
- Intel recommends keeping signals from the same byte or group together on the same layer to avoid layer-transition mismatch effects.
- Existing repo return-path facts already support the generic layer-change boundary: reference-plane continuity and local return vias matter when signals change layers.

## Conditions And Methods

- Use this card when a prompt needs guarded memory-interface routing language for DDR/EMIF topics without numeric layout rules.
- Keep routing language at governance level: reference continuity, local return path, ground stitching vias, controlled layer transitions, time-domain matching, and compensation routing.
- Pair with DDR system-context cards only when a prompt needs to explain why DDR4/DDR5 creates design pressure, not when it needs proof of capability or timing closure.
- Pair with via-transition and ground/return-path cards when the prompt discusses layer changes or plane-split risk outside memory-interface-specific context.

## Limits And Non-Claims

- This card does not authorize exact impedance, trace width, spacing, via-count, via-distance, serpentine-spacing, length-mismatch, timing, or skew numbers.
- It does not authorize universal DDR4, DDR5, LPDDR, eMMC, or memory-bus routing recipes.
- It does not prove SI margin, eye opening, calibration success, compliance, validation pass, bandwidth, or board-level performance.
- It does not prove that HIL, APT, or any supplier can build or validate DDR4/DDR5 boards by default.
- It does not promote any numeric table or figure from `【PCB必备】194页-PCB设计规范经验之书.pdf`.

## Open Questions

- A later lane could add a separate memory-interface card for eMMC matching only if a current-public owner source supports that specific route without importing handbook pull-up / matching numerics.
- A later lane could add topology-specific DDR routing only if it remains tied to a named owner guide and avoids universalizing exact values.

## Source Links

- https://www.intel.com/content/www/us/en/docs/programmable/683216/23-2-2-7-1/general-layout-routing-guidelines-21541.html
- https://www.ti.com/lit/an/scaa082a/scaa082a.pdf
