---
topic_id: "processes-named-simulation-tool-boundaries"
title: "Named Simulation Tool Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "methods-named-simulation-tool-entry-identity-boundary"
  - "methods-pre-fabrication-validation-workflow-boundary"
source_ids:
  - "hilpcb-circuit-simulator-tool-page"
tags: ["simulation-tool", "tool-identity", "feature-identity", "validation-workflow", "circuit-simulator", "hilpcb", "routing-boundary"]
---

# Governance Summary

> A named simulator page and a generic validation workflow are different knowledge lanes. The safe active posture in this corpus is: a named tool can be described only at tool-entry and visible feature-identity level, while pre-fabrication validation remains a separate workflow layer involving prototype routing, DFM/DFT review, first-article confirmation, and staged inspection or test handoff. This page is a tool identity boundary, not a proof-of-capability or proof-of-outcome page.

## Boundary Split

| Lane | Safe question | What the corpus supports |
|---|---|---|
| Named simulator identity | "Does an official named tool page exist, and what visible feature labels appear on it?" | Tool-entry identity and guarded feature labels only |
| Generic validation workflow | "How does a design move through review, prototype, FAI, inspection, and handoff before release?" | Workflow and gate-level process framing |
| Not supported here | "What does the tool prove about the design?" | Not supported by this page |

## What This Page Controls

- Use this page when a draft names a specific simulator rather than speaking only about generic validation steps.
- Keep named tool wording at `official tool exists` and `page-visible feature identity` level only.
- Route prototype, NPI, DFM/DFT, FAI, inspection, and functional-test language to the broader validation workflow lane.
- Stop any wording that turns a tool page into proof of electrical correctness, manufacturability, or production readiness.

## Stable Facts

- HILPCB has an official page for a named `Circuit Simulator` tool.
- The named tool page supports treating the simulator as a distinct tool entry rather than as a fabrication, assembly, or workflow page.
- The named tool page supports guarded feature-identity wording when those labels are visible on the page.
- The broader pre-fabrication validation lane is supported separately by prototype, NPI, DFM/DFT, FAI, inspection, and functional-test workflow records.
- The named tool lane remains separate from the broader validation workflow lane and must not be collapsed into it.

## Tool Identity Rules

### Safe Named Tool Language

- `HILPCB has an official Circuit Simulator page`
- `the simulator appears as a named online tool entry`
- `the tool page shows specific feature labels when they are visible on that page`

### Safe Feature-Identity Language

- mention only page-visible feature labels
- keep those labels at identity level, not at outcome level
- treat feature mentions as `what the page says is present`, not `what the tool has proven in this design`

### Stop Line

- do not turn feature labels into validated current-draw, power-consumption, signal-integrity, manufacturability, or production conclusions

## Validation Workflow Separation

- Pre-fabrication validation belongs to a different lane.
- That lane can safely discuss prototype routing, DFM/DFT review, first-article confirmation, inspection gates, and functional-test handoff.
- It cannot be backfilled by saying a named simulator already solved the validation problem.
- If a draft needs to explain how a board moves toward release, it should route to workflow and gate language rather than named tool language.

## Common Overclaims To Block

- `the simulator validates current draw or power consumption`
- `the simulator ensures the design is electrically sound`
- `the simulator proves manufacturability or reliability`
- `the simulator makes the design production-ready`
- `the simulator reduces revisions, delays, or cost`
- `the page proves exact analysis support without checking current tool documentation`

## Explicit Blocked Claims

- `tool-outcome guarantees`: do not claim that the named simulator guarantees electrical correctness, current validation, performance, manufacturability, or reliability.
- `production-readiness claims`: do not treat the tool page as proof that the design is ready for fabrication, NPI, or release.
- `exact feature-support claims without refresh`: do not state exact supported analyses, formats, workflows, or solver behavior unless refreshed from the current official tool page in publication workflow.
- `cost/lead-time/yield claims`: do not claim commercial, schedule, or yield benefits from the named tool page.

## Must Refresh Before Publishing

- any claim about exact supported file formats, component models, or analysis types
- any claim that uses present-tense feature wording such as `now supports`
- any claim that turns tool labels into verified engineering outcomes
- any claim that treats named-tool access as a substitute for review, prototype, inspection, or test gates

## Related Fact Cards

- `methods-named-simulation-tool-entry-identity-boundary`
- `methods-pre-fabrication-validation-workflow-boundary`

## Primary Sources

- https://hilpcb.com/en/tools/circuit-simulator
