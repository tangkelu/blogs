---
task_id: "P4-275 public-capability-parameter-consumption-map"
status: "completed"
owner: "Codex"
write_scope:
  - "/code/blogs/llm_wiki/wiki/processes/public-capability-parameter-consumption-map.md"
  - "/code/blogs/llm_wiki/logs/p4-275-public-capability-parameter-consumption-map.md"
---

# Scope

- Promoted `wiki/processes/public-capability-parameter-consumption-map.md` from `draft` to `active`.
- Used only the already-landed local parameter-scope fact cards and `ASSESSMENT.md` protocol guidance.
- Made no shared tracker edits and added no URL-only refresh work.

# Blocked Claims

- Public-site page claims remain blocked from upgrade into factory guarantees, lot capability, qualification proof, and compliance thresholds.
- Cross-family synthetic capability tables remain blocked unless the prompt preserves separate page scope.
- Acceptance-threshold, release-criteria, and current-availability claims remain blocked.
- JSON inventory coverage remains blocked from being treated as extracted-fact completeness or verified capability proof.

# Landed Changes

- Reframed the page as an active routing and consumption-governance surface.
- Added routing guidance, stable facts, explicit blocked claims, common misreadings, must-refresh boundaries, and related-facts/source-scope sections.
- Kept the original decision rules and claim ceiling, but tied them more explicitly to the landed parameter fact cards and the internal JSON coverage boundary.

# Verification

- Edited files only with `apply_patch`.
- Confirmed the scoped diff contains only:
  - `/code/blogs/llm_wiki/wiki/processes/public-capability-parameter-consumption-map.md`
  - `/code/blogs/llm_wiki/logs/p4-275-public-capability-parameter-consumption-map.md`
- Checked repository status after edits and did not modify any out-of-scope files.
