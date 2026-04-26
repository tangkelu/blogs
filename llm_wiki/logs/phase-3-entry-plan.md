# Phase 3 Entry Plan

Last updated: 2026-04-24

## Purpose

Phase 3 expands the official-source layer for high-speed / RF materials and for finish-standard metadata. The goal is to widen coverage without weakening source governance: official sources first, conservative facts second, and no blog-facing claims unless they can be traced to a public anchor.

This plan is for execution only. It does not create source records, fact cards, or wiki pages by itself.

## Operating Constraints

- Do not use reseller, forum, or blog material as a primary source.
- Prefer official public datasheets, processing guides, technical notes, standards pages, and regulatory pages.
- Keep dynamic items separate from stable facts.
- Preserve source/fact boundaries:
  - source work confirms the official anchor and revision context
  - fact work extracts only what the source actually supports
- If a revision anchor is ambiguous or missing, mark it as a dependency instead of forcing a fact.

## Batch Shape

Use one coordinated Phase 3 batch with three sub-agents, but execute it in staged order so later work can reuse earlier anchors and naming.

- Batch size target:
  - 2 to 5 source records
  - 2 to 6 fact cards
  - 0 to 1 topic wiki follow-on per sub-theme only if the source layer is complete

## Execution Order

1. P3-02 Finish Standard Metadata
2. P3-01 Taconic Official Coverage
3. P3-03 More High-Speed / RF Material Families

Reason:

- P3-02 gives the revision-anchoring pattern needed for later source registration.
- P3-01 is source-discovery heavy and benefits from a settled metadata convention.
- P3-03 should reuse the same source/fact template so the family expansion stays consistent.

## Sub-Agent Split

### P3-02 Finish Standard Metadata

Ownership:

- Sub-agent A: source registry and revision anchor confirmation
- Sub-agent B: conservative fact extraction from confirmed anchors

Write scope:

- Public revision anchors for:
  - IPC-4552
  - IPC-4553
  - IPC-4554
  - IPC-4556
- Metadata fields to stabilize:
  - standard identifier
  - public revision or edition
  - publication date if available
  - checked_at
  - notes for missing public revision detail

Source dependencies:

- Standard organization pages or official public standard listings
- If only partial public metadata exists, record the gap rather than inferring the edition

Fact dependencies:

- Do not write process or performance facts from standards text unless the public anchor is clear
- Any metadata fact must be tied to the exact public revision anchor

Output expectation:

- A stable revision-anchoring pattern that can be reused for later standards refresh work
- Conservative metadata facts only, no paid-text reproduction

### P3-01 Taconic Official Coverage

Ownership:

- Sub-agent C: Taconic source discovery and source confirmation only
- Sub-agent D: Taconic fact extraction only after source confirmation

Write scope:

- Taconic official product pages, datasheets, processing guides, and technical notes
- Focus on RF / high-frequency laminate families with public official coverage
- Capture family-level attributes only when they are clearly stated by the official source

Source dependencies:

- Taconic official domain material only
- If the public family page is sparse, check for linked datasheets or technical notes before widening scope
- Do not backfill from distributor copies or third-party summaries

Fact dependencies:

- Facts must stay within the exact family and revision confirmed by the source
- Keep numeric claims conditioned by the source context when applicable
- If the official material is incomplete, leave the family as partially covered rather than guessing at adjacent product lines

Output expectation:

- A small but trustworthy Taconic source set
- Enough facts to let later material-selection pages compare Taconic against the already covered families

### P3-03 More High-Speed / RF Material Families

Ownership:

- Sub-agent E: Isola family expansion
- Sub-agent F: Panasonic family expansion
- Sub-agent G: Ventec family expansion

Write scope:

- Additional Isola low-loss families
- Additional Panasonic build-up / ultra-low-loss families
- Additional Ventec RF / low-loss families where official coverage is strong

Source dependencies:

- Official manufacturer product pages, datasheets, and processing guides
- Prefer families that already have obvious public anchors and compare well with the current coverage set
- Skip any family that requires speculative interpretation to identify

Fact dependencies:

- Extract only stable family attributes that are directly supported by the official source
- Keep test-condition details attached to the fact whenever the source provides them
- Avoid collapsing different product variants into one family fact unless the source explicitly groups them

Output expectation:

- Broader comparison coverage across manufacturer families
- Better material-selection granularity for later wiki work

## Handoff Rules

- Sub-agents must report:
  - changed files
  - source gaps
  - unresolved revision questions
  - whether the family is ready for facts or still source-only
- The coordinating agent must verify:
  - source priority compliance
  - no dynamic claim was frozen as static
  - no family was expanded beyond the confirmed anchor
  - the batch remains small enough to review cleanly

## Residual Risks To Watch

- Taconic public material may be sparse, which can limit the size of the source set.
- Some standard metadata may have weak public revision visibility, especially if only high-level listings are available.
- Manufacturer family naming can overlap across variants, so source identity needs to stay exact.
- Any numeric claim pulled into facts must retain its test context and should be treated as revision-sensitive if the source changes.
