Date: 2026-05-01
Lane: `P4-102 controller integration`
Input: `logs/p4-98-2026-5-1-dna-biological-split-lane-controller-integration.md`, `logs/p4-99-2026-5-1-dna-computing-owner-platform-scout.md`, `logs/p4-100-2026-5-1-biological-computing-owner-material-scout.md`, `logs/p4-101-2026-5-1-hilpcb-life-science-capability-decision.md`
Output: `logs/p4-102-2026-5-1-owner-material-capability-controller-integration.md`
Scope status: `controller_integrated`
Evidence status: `default_strip_path_opened`

# Purpose

Controller-integrate the owner-platform, material, and HILPCB capability decision lanes for the two remaining held `2026.4.29` drafts, and decide whether the next best move is more authority recovery or a generic strip-first eligibility test.

# Integrated Results

## `dna-computing`

- `P4-99` shows that a generic rewrite can strip all named platform, compute-stack, regulator, and HILPCB readiness nouns while preserving broad subsystem context plus documentation-boundary manufacturing-control language
- owner-platform recovery is now optional rather than mandatory; it should open only if publication scope insists on exact platform nouns

## `biological-computing`

- `P4-100` shows that a generic rewrite would need to strip owner nouns, material nouns, wet-zone framing, and most biointerface-specific proof language
- after that strip, remaining value may be thin enough that hold is still preferable unless a very narrow packaging-pressure or manufacturing-control article is still worthwhile

## HILPCB Capability

- `P4-101` sets the default controller decision to `strip`
- no current local evidence supports HILPCB-specific life-science, diagnostics, medical-device, neural-interface, or bioelectronic manufacturing-readiness language in public rewrite scope
- dated internal capability records would be required before any of that wording is retained

# Controller Disposition

The active path is no longer broader authority recovery by default.

New preferred order:

1. test whether `dna-computing` can survive a strip-first generic rewrite at subsystem and documentation-control level only
2. test whether `biological-computing` still has enough value after owner, material, wet-zone, and HILPCB capability stripping; if not, keep it on hold
3. only reopen owner-platform, material, or internal capability recovery if publication explicitly requires exact nouns that the strip-first path cannot preserve

Current hold state remains unchanged until that strip-first eligibility test is done:

- `dna-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`
- `biological-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`

# Next Micro-Lanes

1. `dna-computing` generic-strip rewrite eligibility test
2. `biological-computing` generic-strip value test
3. reopen owner-platform, material, or dated internal capability recovery only if exact nouns remain a publication requirement

# Status

- active continuation state: `strip_first_eligibility_testing`
- tracker state: `ready_for_p4_102_update`
