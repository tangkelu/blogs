---
title: "LED MCPCB Thermal Assembly Evidence Pack"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-13"
tags: ["led", "mcpcb", "ims", "thermal-platform", "reflow", "inspection"]
---

# LED MCPCB Thermal Assembly Evidence Pack

**Pack ID**: `consumption-led-mcpcb-thermal-assembly`  
**Date**: 2026-05-13  
**Template**: `query`  
**Gate status**: `ready` for scoped board-level LED MCPCB / IMS thermal-platform, reflow, inspection, and validation-handoff writing only.

## Scope

This pack supports a conservative HILPCB query article about LED MCPCB thermal assembly. It may be used for LED engines, LED modules, signage boards, gallery or creative LED boards, solar LED modules, and automotive-adjacent lighting boards only when the article stays at board / assembly review level.

It does not support finished-luminaire optical performance, LED lifetime, photometric pass/fail, hazardous-location approval, transportation lighting compliance, aviation readiness, automotive qualification, medical efficacy, field reliability, cost, lead time, or yield.

## Local Consumption Map

| Article need | Local fact or wiki path | Allowed use | Not allowed |
| --- | --- | --- | --- |
| Separate board-level thermal work from optical and regulated product tests | `wiki/testing/led-pcb-optical-thermal-and-regulated-test-boundaries.md`; `standards-led-optical-lifetime-and-safety-boundary`; `standards-medical-and-automotive-led-pcb-boundary` | Explain LM-79, LM-80, TM-21, IEC 62471, medical, and automotive standards as context boundaries | Claim lumen output, L70, color stability, photobiological pass/fail, medical approval, automotive grade, PPAP, or finished-light compliance |
| Select thermal board route | `methods-thermal-pcb-platform-selection-posture`; `wiki/materials/ceramic-aln-ims-thermal-platforms.md` | Compare MCPCB / IMS, high-thermal PCB, heavy copper, ceramic, and FR-4 as platform choices driven by heat path and validation plan | Claim one platform is universally best or publish thermal-resistance / junction-temperature outcomes |
| Frame MCPCB reflow | `methods-mcpcb-ims-and-reflow-source-coverage` | Tie reflow planning to solder paste, assembly thermal mass, component package, profiling, and first-build evidence | Publish universal reflow profiles, paste windows, void targets, or thermal-mass limits |
| Treat panelization and edge risk | `methods-mcpcb-depanelization-method-selection-boundary` | Discuss singulation route selection by geometry, edge cleanliness, nearby components, and mechanical-load risk | Publish web thickness, burr-height, blade-gap, or cutting-speed rules |
| Connect to HILPCB product paths | `methods-thermal-pcb-platform-selection-posture`; HIL high-thermal, metal-core, heavy-copper, SMT pages | Link to product / service pages as project routing choices | Convert service-page language into industry-wide proof or guaranteed design outcome |

## Required Public Article Behavior

- Add a table with columns equivalent to `Review area | What to decide | Why it matters | How to verify | If ignored`.
- Keep the first substantive H2 focused on heat path, board platform, reflow, inspection, and validation handoff.
- Include a TOC when the article has three or more H2 sections.
- Include `<!-- COMPONENT: BlogQuickQuoteInline -->` after a useful engineering table or checklist, not as a banner.
- Use public references for standards and official vendor/process pages.
- Use only public-safe author and review wording.

## Data Gaps And Holds

- `explosion-proof-led-lighting`, `ground-lighting-transportation`, and `runway-lighting-transportation` remain `llm_wiki_gap`.
- Any exact LED lifetime, L70, lumen-maintenance, CRI, photometric, junction-temperature, thermal-resistance, solder-void, profile-window, regulated-market, lead-time, cost, yield, or field-reliability claim must be refreshed from official or dated project evidence before publication.

