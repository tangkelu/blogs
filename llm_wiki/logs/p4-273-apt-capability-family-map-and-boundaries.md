---
task_id: "P4-273 apt-capability-family-map-and-boundaries"
status: "completed"
owner: "Codex"
write_scope:
  - "/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md"
  - "/code/blogs/llm_wiki/logs/p4-273-apt-capability-family-map-and-boundaries.md"
---

# Scope

- Promoted `wiki/processes/apt-capability-family-map-and-boundaries.md` from `draft` to `active`.
- Used only already-landed local fact cards covering the six-family capability map, HDI posture, rigid-flex posture, and MCPCB/IMS boundary handling.
- Made no shared tracker edits and added no URL-only refresh work.

# Blocked Claims

- Exact fabrication windows, impedance limits, and layer-count claims remain blocked without refreshed engineering data.
- Bend-radius, bend-life, and rigid-flex mechanical durability claims remain blocked without refreshed process support.
- Ceramic numeric property claims remain blocked without product-level source refresh.
- MCPCB or IMS process claims remain blocked when they imply universal reflow profiles or universal thermal windows.
- Lead-time, certification, quality-system, and sector-approval claims remain blocked without separate refresh.

# Landed Changes

- Changed the wiki page status to `active` and set `last_reviewed_at` to `2026-05-04`.
- Added explicit routing-use guidance so the page functions as an active scope-control surface.
- Kept blocked claims explicit instead of letting the capability pages read like manufacturing guarantees.
- Extended refresh boundaries to include IMS and solder-paste-specific reflow claims.

# Verification

- Edited files only with `apply_patch`.
- Limited changes to the declared write scope:
  - `/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md`
  - `/code/blogs/llm_wiki/logs/p4-273-apt-capability-family-map-and-boundaries.md`
