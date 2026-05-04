---
task_id: p4-208-prototype-vs-quick-turn-pcb-routing
status: completed
owner: codex
write_scope:
  - /code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md
  - /code/blogs/llm_wiki/logs/p4-208-prototype-vs-quick-turn-pcb-routing.md
---

# Lane Log: P4-208 Prototype Vs Quick Turn PCB Routing

## Task Metadata

| Field | Value |
|---|---|
| `task_id` | `p4-208-prototype-vs-quick-turn-pcb-routing` |
| `status` | `completed` |
| `owner` | `codex` |
| `lane` | `prototype vs quick-turn pcb routing promotion` |
| `started_at` | `2026-05-03` |
| `completed_at` | `2026-05-03` |
| `status_history` | `in_progress -> completed` |

## Write Scope Completed

| File | Type | Description |
|---|---|---|
| `wiki/processes/prototype-vs-quick-turn-pcb-routing.md` | Updated | Promoted from `draft` to `active` with prototype / quick-turn / production boundary routing |
| `logs/p4-208-prototype-vs-quick-turn-pcb-routing.md` | New | Lane log for this task |

## Source Inputs Used

- `ASSESSMENT.md` — active queue and lane rules
- `facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
- `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
- `facts/processes/hil-single-double-layer-capability-specs.md`
- `facts/processes/hil-multilayer-capability-specs.md`
- `facts/processes/hil-fr4-capability-specs.md`
- `facts/processes/inspection-governance-navigation-map.md`

## Extraction Summary

Promoted the page into an `active` process boundary using only landed local facts. The final routing frame explicitly separates:

- `prototype` as validation / iteration posture
- `quick-turn` as schedule-compression posture
- `production` as repeatability / release-governance posture

The page now anchors accelerated routing to low-complexity baseline families first, then explains why multilayer and advanced-material boards require stricter review before inheriting any quick-turn framing.

## Blocked Claims (Maintained)

- turnaround guarantees
- prototype-to-production promises
- yield / reliability claims
- cost, lead-time, and supplier-proof claims

## Residual Risks

- HIL product facts still contain some speed numerics, but this wiki page deliberately keeps those out of final routing guidance except as complexity context.
- The page remains governance-first; it does not settle exact eligibility rules for rush multilayer or specialty-material builds.
- A future main-agent pass may still want to normalize related draft pages such as `pre-fabrication-validation-and-prototype-boundaries.md` and `pcba-npi-to-mass-production-flow.md`.
