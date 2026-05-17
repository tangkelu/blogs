# P4-568 Blog Failure Pattern Mechanism Family Taxonomy

## Purpose

Turn `failure pattern` from a generic writing requirement into a reusable mechanism-family routing system for future PCB / PCBA blogs.

## New Wiki Surface

- `wiki/processes/blog-failure-pattern-mechanism-family-map.md`

## Prompt-System Updates

- `prompts_template/shared/technical-blog-standard.md`
- `prompts_template/shared/query.md`
- `prompts_template/shared/blog-rewrite-data-gap-contract.md`
- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/shared/pillar.md`
- `prompts_template/README.md`

## What This Pass Now Allows

- Future agents can classify a draft into one primary mechanism family before writing:
  - `mechanical load / strain`
  - `electrical field / return path collapse`
  - `thermal mismatch / heat path`
  - `process window interaction`
  - `chemical / surface condition`
  - `data-package incompleteness / governance failure`
- Query and Pillar prompts can now require topic-specific failure chains instead of one generic warning paragraph.
- Evidence packs now have a clearer requirement: pick the mechanism family first, then fill the failure-pattern inventory.

## What This Pass Fixes

- It reduces the chance that future articles stay at `safe but generic` even when they technically include a failure-pattern paragraph.
- It prevents a narrow fix like the ICT fixture-strain example from being mistaken as the universal pattern for all topics.

## Residual Gaps

- The taxonomy page is a routing layer, not a complete fact layer for every mechanism family.
- Some families, especially `thermal mismatch`, `chemical / surface condition`, and `data-package incompleteness`, still need more narrow source-backed example cards as future topics demand them.
