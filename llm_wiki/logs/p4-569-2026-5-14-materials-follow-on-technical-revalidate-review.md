# P4-569 Materials / Surface Finish / Thermal Follow-On Technical Revalidate Review

Date: 2026-05-14
Owner lane: `Materials / Surface Finish / Thermal`
Scope:
- `mri-compatible-pcb-materials-testing`
- `low-thermal-conductivity-stackup`
- `electrowetting-pcb`
- `mri-compatible-pcb-materials-routing`

## What This Pass Did

- Reviewed the four remaining `technical_revalidate` slugs against the current local `llm_wiki` layer.
- Added one reusable MRI boundary fact card:
  `facts/methods/mri-board-material-and-routing-mr-conditional-boundary.md`
- Added one lane-facing rewrite readiness map:
  `wiki/processes/materials-surface-finish-thermal-follow-on-revalidate-map.md`
- Recorded which slugs still need official-source recovery instead of generation-first rewriting.

## Main Findings

### 1. MRI Has A Reusable Boundary, But Not A Full Playbook

- Current support is strong enough to say:
  MRI is a device-level hazard and labeling problem,
  board materials/routing can only be discussed as conservative risk-reduction posture,
  and MR claims must stop at device-level validation boundary.
- Current support is not strong enough to publish:
  exact MRI material lists,
  exact screening thresholds,
  exact routing rules,
  or a public test-acceptance checklist.

### 2. Low-Thermal-Conductivity Stackup Is Still A Source Gap

- Current `llm_wiki` supports thermal platform selection and thermal-path language.
- It does not support cryogenic feedthrough, thermal-isolation geometry, vacuum stackup, or low-heat-leak validation as a reusable article layer.

### 3. Electrowetting Is Still A Hard Gap

- Current local sources do not provide electrowetting-specific support for dielectric stack, hydrophobic surface, contact-angle change, leakage, or droplet-failure vocabulary.
- The current blog is therefore far beyond the local authority layer.

## Outcome By Slug

- `mri-compatible-pcb-materials-testing`: `hold_for_official_source_recovery`
- `mri-compatible-pcb-materials-routing`: `safe_but_generic`
- `low-thermal-conductivity-stackup`: `hold_for_official_source_recovery`
- `electrowetting-pcb`: `hold_for_official_source_recovery`

## Why This Matters For Future Rewrites

- The useful abstraction is not "add more concrete wording."
- The useful abstraction is:
  choose the primary mechanism family first,
  then only allow the failure chain and validation boundary that the local evidence can actually support.
- In this lane, MRI is mainly a `MR labeling + induced-loop risk` boundary,
  low-thermal stackup is a `thermal-path isolation` gap,
  and electrowetting is a `surface chemistry + dielectric integrity` gap.
