---
lane: "P4-64A connector-rating split"
title: "Deletion-safe split log for remaining connector-rating and component-current-rating claims after P4-63"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-64a-2025-11-10-connector-rating-split.md"
input_root: "/code/blogs/tmps/2025.11.10/en"
---

# Purpose

- Assigned lane: `P4-64A connector-rating split`
- Goal: isolate the remaining connector-rating and component-current-rating claim family after `P4-63` split off the named simulation-tool lane.
- Drafts were treated as claim inventory only, not as authority.
- Output-only boundary honored: no tracker edits, no fact/wiki/source-registry edits, and no edits outside this log.

# Inputs Reviewed

## Draft inventory

- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Local prior context

- `/code/blogs/llm_wiki/logs/p4-61a-2025-11-10-watts-to-amps-pcb-consequence-split.md`
- `/code/blogs/llm_wiki/logs/p4-62a-2025-11-10-watts-to-amps-validation-split.md`
- `/code/blogs/llm_wiki/logs/p4-63-source-backed-integration.md`
- `/code/blogs/llm_wiki/wiki/processes/current-carrying-and-high-current-layout-boundaries.md`
- `/code/blogs/llm_wiki/wiki/processes/electrical-formula-identity-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/tht-pressfit-terminal-route-boundary.md`

# Claim-Family Split

## 1) Potentially recoverable connector or component rating identity / selection-boundary claims

These are the narrowest claims that could still be promoted later if a source-backed connector/component lane appears:

- current can be used as a selection input for choosing a connector family or power component family
- component identity language such as `regulator`, `connector`, or generic `power component` when used only as a selection boundary, not a rating claim
- safe qualitative wording that a part must be chosen to handle the known current with an explicit review step
- generic board-interface selection language where the discussion stays at the level of `component selection`, `connector selection`, or `current-path planning`
- board-level routing language that keeps current-aware choice separate from any numeric rating statement

## 2) Claims that clearly require specific part-owner datasheets

These claims need the exact connector owner, regulator owner, or component owner datasheet before they can be promoted:

- any explicit current rating for a named connector, terminal, regulator, or component
- `10 A`-style example language when it is used as a product claim rather than as a teaching example
- continuous-current, peak-current, or per-pin current limits for a specific part
- contact resistance, temperature-rise, derating, or thermal-limit numbers for a specific connector or component
- insertion, retention, mating-cycle, or service-life values for a specific connector family
- package-specific or footprint-specific current capability for a named component
- owner-datasheet-backed statements about whether a specific part is suitable for the target current

## 3) Blocked manufacturability, reliability, or safety-margin claims

These remain blocked because the draft does not have the needed part-owner evidence:

- claims that current selection by itself improves reliability or manufacturability
- claims that a safety margin is already justified for a named part family
- claims that a component or connector is `safe` for production without a part-specific datasheet
- claims that current sizing alone reduces revisions, delays, or assembly cost
- claims that the board is ready for real-world application because current was calculated
- claims that component or connector selection already ensures thermal safety, field safety, or production readiness
- claims that assembly or field failure is avoided by current math alone

# File-Level Claim Disposition

## `watts‑to‐amps.md`

- The file still carries a residual connector-rating / component-current-rating family after the formula-identity lane and the named-simulation-tool lane are separated.
- The recoverable portion is only a selection-boundary story at this stage.
- The rating numbers and part-suitability claims remain blocked until specific owner datasheets are attached.
- The manufacturability, reliability, and safety-margin language remains blocked and should not be promoted from this inventory.

# Split Guidance

## Keep in the narrow connector/component lane if promoted later

- current-aware connector selection
- current-aware component selection
- generic selection-boundary language for regulators, connectors, and other board-interface parts
- board-interface planning that stays qualitative and does not state numeric ratings

## Keep out of the narrow connector/component lane even if it lands

- exact current ratings
- contact-resistance, temperature-rise, derating, insertion-force, retention-force, or life numbers
- named-part suitability claims without the part-owner datasheet
- manufacturability, reliability, safety, or production-readiness conclusions from current math alone
- part performance claims that imply a default safe margin without source-backed evidence

# Blocked Claim Classes

- formula identity taught as authority
- unit-identity teaching for `volt`, `ampere`, `ohm`, and `watt`
- connector-rating or component-current-rating numbers without owner datasheets
- current-limit or derating tables presented as reusable fact
- generic safety-margin language that pretends to be part-specific evidence
- manufacturability, reliability, thermal-safety, or field-safety claims inferred from current alone
- production-readiness, assembly-success, or cost-reduction claims tied to current math without evidence

# Narrowest Recommended Promotion Target

- Recommended target, if a source pack lands: `connector_and_component_rating_selection_boundary`.
- If the lane stays narrower than that, keep the promotion target at `connector_selection_boundary` and do not absorb part-rating numerics.
- Do not promote manufacturability, reliability, or safety-margin claims from this split until specific part-owner datasheets are separately recovered.

# Verification Notes

- `watts‑to‐amps.md` remains the only reviewed draft in this split.
- `P4-63` already separated the named simulation-tool lane, so this pass focuses only on the remaining connector/component rating family.
- This log is deletion-safe: it preserves reviewed-file scope, split shape, blocked classes, and the narrowest future promotion target without promoting draft claims to fact status.
