Date: 2026-05-05
Lane: `P4-186 PCIe Gen6 source-first repair`
Input:
- `/code/blogs/blogs/1206-p0-rewrite/en/pcie-gen6-si-checklist-mass-production.md`
- `/code/hileap/frontendAPT/public/static/blogs/2025/10/en/pcie-gen6-si-checklist-mass-production.md`
Outputs:
- `/code/blogs/llm_wiki/facts/methods/pcie-gen6-board-review-boundary.md`
- `/code/blogs/llm_wiki/wiki/processes/pcie-gen6-si-review-and-release-boundary.md`
- `/code/blogs/blogs/1206-p0-rewrite/en/pcie-gen6-si-checklist-mass-production.md`
- prompt contract updates under `/code/blogs/prompts_template/shared/`

Scope status: `landed`
Evidence status: `source-first board-review boundary plus rewrite`

# Purpose

Repair the PCIe Gen6 rewrite lane so it explicitly follows the `llm_wiki -> official/public source check -> write-back -> rewrite` workflow instead of skipping from partial local context to a thin conservative article.

# What Changed

- Added a dedicated `PCIe Gen6` board-review boundary card anchored to:
  - `PCI-SIG PCIe 6.0 FAQ`
  - local APT high-speed context
  - Panasonic `MEGTRON 7` family positioning
  - Isola `Tachyon 100G` datasheet positioning
  - TE `112G` interconnect ecosystem context
- Added a reusable process aggregation page so future `PCIe Gen6 / 112G / backplane / release-review` drafts do not fall back to generic high-speed wording.
- Rewrote the blog to restore engineering density through:
  - board-ownership framing
  - stackup/material direction logic
  - local launch/via review burden
  - typical release-blocker and EQ-style scenarios
  - layered validation boundaries
- Updated prompt contracts so future execution must explicitly list consumed `fact_id` / `wiki` paths and external-source gaps before drafting.

# Root-Cause Note

- The earlier rewrite did inspect some local cards, but they were not treated as the primary consumption layer.
- High-risk SI claims were stripped without adding back enough source-backed failure modes, review burdens, or scenario logic.
- That combination produced a `safe but generic` skeleton instead of a publishable engineering article.
