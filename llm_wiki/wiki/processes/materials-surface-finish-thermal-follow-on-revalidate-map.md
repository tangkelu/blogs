---
topic_id: "processes-materials-surface-finish-thermal-follow-on-revalidate-map"
title: "Materials Surface Finish Thermal Follow-On Revalidate Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-14"
fact_ids:
  - "methods-mri-board-material-and-routing-mr-conditional-boundary"
  - "methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity"
  - "methods-thermal-pcb-platform-selection-posture"
  - "applications-medical-application-coverage-gap-map"
source_ids:
  - "fda-mri-benefits-and-risks-page"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
tags: ["materials", "surface-finish", "thermal", "rewrite-readiness", "mri", "electrowetting", "stackup", "processes"]
---

# Definition

> This map classifies the remaining `technical_revalidate` slugs in the `Materials / Surface Finish / Thermal` lane by primary mechanism family, expected failure chain, and rewrite readiness. Its job is to stop old drafts from sounding specific while actually outrunning the local evidence layer.

## Why This Topic Matters

- These four slugs are not blocked for the same reason.
- MRI drafts currently overclaim from incomplete device-validation evidence.
- `low-thermal-conductivity-stackup` overclaims from missing cryogenic / thermal-isolation source support.
- `electrowetting-pcb` overclaims from missing electrowetting-specific dielectric, hydrophobic-surface, and actuation-validation sources.
- Without one readiness map, future rewrites will keep falling back to generic materials prose or unsupported engineering numerics.

## Stable Local Support

- The local corpus can support `MRI` only at medical-imaging application context plus MR-labeling and loop-risk boundary level.
- The local corpus can support `routing continuity`, `return-path discipline`, and `loop-area minimization` as general board-review language.
- The local corpus can support `thermal platform selection` among MCPCB, heavy copper, and ceramic as a heat-path decision family.
- The local corpus does not yet support a reusable public source layer for cryogenic thermal-isolation stackups or for electrowetting-specific surface / dielectric behavior.

## Slug Classification

### `mri-compatible-pcb-materials-testing`

- Supported status:
  `hold_for_official_source_recovery`
- Primary mechanism family:
  `data-package incompleteness / governance failure`
- Secondary mechanism family:
  `electrical field / return path collapse`
- Expected failure chain:
  board or material screening is mistaken for device-level MR qualification -> artifact / heating / force risk is still unclosed in scanner conditions -> public copy overclaims `MRI-compatible` or test completeness.
- Strongest local support:
  `methods-mri-board-material-and-routing-mr-conditional-boundary`,
  `applications-medical-application-coverage-gap-map`
- Keep blocked:
  exact ASTM test flows,
  susceptibility limits,
  accepted material lists,
  finish prohibitions,
  field-strength compatibility,
  artifact thresholds,
  SAR or heating limits,
  and supplier qualification claims.
- Rewrite note:
  safe only as a boundary article about why board screening does not equal MR labeling; not yet safe as a concrete testing playbook.

### `mri-compatible-pcb-materials-routing`

- Supported status:
  `safe_but_generic`
- Primary mechanism family:
  `electrical field / return path collapse`
- Secondary mechanism family:
  `data-package incompleteness / governance failure`
- Expected failure chain:
  enlarged conductive loops or broken return-path continuity in MRI-adjacent hardware -> induced current, artifact, or local heating risk -> device-level MR-conditional validation still required.
- Strongest local support:
  `methods-mri-board-material-and-routing-mr-conditional-boundary`,
  `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity`
- Keep blocked:
  exact loop-area rules,
  differential-pair recipes,
  finish chemistry claims,
  scanner-frequency tuning claims,
  component-material rules,
  and MR pass/fail language.
- Rewrite note:
  can be rewritten only as conservative routing-review posture unless new MRI-specific owner or standards sources are recovered.

### `low-thermal-conductivity-stackup`

- Supported status:
  `hold_for_official_source_recovery`
- Primary mechanism family:
  `thermal mismatch / heat path`
- Expected failure chain:
  unintended copper, connector, or plated-through thermal bridge defeats the isolation intent -> thermal budget collapses across the hot/cold boundary -> drift, cooldown loss, or mechanical stress appears elsewhere in the system.
- Strongest local support:
  `methods-thermal-pcb-platform-selection-posture`
- What is still missing:
  cryogenic feedthrough context,
  low-thermal-conductivity material or geometry authority,
  outgassing plus vacuum handling context specific to this stackup family,
  and validation-boundary support for thermal-isolation articles.
- Keep blocked:
  meander geometry rules,
  thin-copper defaults,
  slots and hatch percentages,
  cryo test methods,
  bake rules,
  and cost / lead-time / yield claims.
- Gap note:
  the current corpus supports `heat-path platform selection`, not `thermal-isolation stackup design`.

### `electrowetting-pcb`

- Supported status:
  `hold_for_official_source_recovery`
- Primary mechanism family:
  `chemical / surface condition`
- Secondary mechanism family:
  `electrical field / return path collapse`
- Expected failure chain:
  rough, contaminated, or chemically unstable active surface plus weak dielectric isolation -> contact-angle hysteresis, droplet pinning, leakage, electrolysis, or dielectric breakdown -> actuation fails even if the electrode netlist is electrically correct.
- Strongest local support:
  none beyond very generic coating / materials vocabulary
- What is still missing:
  electrowetting-specific official sources for dielectric layers,
  hydrophobic coatings,
  contact-angle behavior,
  breakdown and leakage framing,
  and PCB-surface flatness relevance to droplet transport.
- Keep blocked:
  ENIG / ENEPIG recommendations,
  dielectric thickness ranges,
  surface roughness limits,
  actuation voltages,
  gap rules,
  and application claims for lab-on-chip, lenses, or displays.
- Gap note:
  this topic currently has no credible local electrowetting evidence pack and should not be rewritten from generic PCB knowledge alone.

## Engineering Boundaries

- Do not let MRI copy drift from `board-review posture` into `MR Safe`, `MR Conditional`, implant, or medical-device approval proof.
- Do not let low-thermal-isolation copy inherit heat-spreader or MCPCB language as if reducing heat flow were the same problem as improving heat dissipation.
- Do not let electrowetting copy borrow ordinary surface-finish or conformal-coating language as if that proved electrowetting behavior.
- When the evidence layer is thin, prefer a rewrite hold or narrow boundary article over a specific-looking but unsupported design guide.

## Official-Source Recovery Priorities

1. MRI board and component screening / validation sources that are specific enough to distinguish board-level review from device-level MR labeling without inventing test criteria.
2. Cryogenic or thermal-isolation stackup sources that discuss heat-leak paths, feedthrough structure, or validation vocabulary.
3. Electrowetting owner or academic-primary sources that expose dielectric, hydrophobic-surface, contact-angle, leakage, and breakdown boundaries in a reusable way.

## Recommended Consumption Order

1. Pick the slug from this map.
2. Lock its primary mechanism family before drafting.
3. Read only the listed supporting fact cards.
4. If the slug status is `hold_for_official_source_recovery`, do not draft a full technical playbook.
5. Recover official sources first, then promote new fact/wiki support back into `llm_wiki`.
