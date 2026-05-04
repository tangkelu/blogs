---
task_id: "p4-203-high-speed-material-family-selection"
status: "completed"
owner: "codex"
write_scope:
  - "/code/blogs/llm_wiki/wiki/materials/high-speed-material-family-selection.md"
  - "/code/blogs/llm_wiki/logs/p4-203-high-speed-material-family-selection.md"
---

# Lane Summary

> Started `2026-05-03 20:50:01 CST` to promote the high-speed material selector from `draft` to a reusable routing page using only existing local fact coverage.

## Scope

- Read `ASSESSMENT.md`, the target wiki draft, and supporting `facts/materials/*` plus `facts/standards/*` already landed in `llm_wiki`.
- Stay inside declared write scope.
- Do not refresh URLs or edit shared trackers.

## Blocked Claims

- process windows
- supplier-capability claims
- channel-performance guarantees
- cost, lead-time, and yield claims

## Planned Output

- normalize `wiki/materials/high-speed-material-family-selection.md` into an `active` routing page
- preserve conservative material-family boundaries, source scope, and refresh rules

## Landed Changes

- promoted the target wiki from `draft` to `active`
- added explicit routing guidance for `MEGTRON 6/7/8`, `Tachyon 100G`, `VT-464G`, `Astra MT77`, and `VT-870` contrast handling
- added explicit blocked-claim section matching the lane contract
- expanded `must_refresh` discipline to prevent stock, supplier, process-window, and channel-performance overclaims
- linked the page more directly to landed fact cards for parameter scope, family coverage, and standards boundary control

## Residual Risks

- The page still depends on family-level and grade-level source anchors rather than stackup-specific validation evidence.
- Any future attempt to add process windows, supplier capability, or channel-performance outcome claims still requires new local fact coverage first.
