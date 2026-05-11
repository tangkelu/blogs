# P4-492 0.75 mm Owner And Standards Candidate Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-481-2026-5-11-intel-fourth-owner-0p75mm-ubga-csp-guidelines-table-landing.md`
- `logs/p4-482-2026-5-11-completion-audit-successor-after-intel-fourth-owner-0p75mm-raise.md`
- `logs/p4-491-2026-5-11-completion-audit-successor-after-package-and-doctrine-candidate-tightening.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout across both sides of the still-open `0.75 mm` residual lane after `P4-491`.

This pass is not a reopen.
It checks whether any newly surfaced current-public owner or standards-side candidate now clears the current repo ceiling.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a new materially stronger current-public owner exact row or package page with stronger same-surface geometry evidence
2. a legitimately public official geometry surface above the current metadata-level standards ceiling

## Candidate Classes Rechecked

### Owner-side classes

1. Infineon current-public `PG-TFBGA` package-page class
2. NXP processor-package datasheet sections with true `0.75 mm` identity
3. ST legacy BGA design-rule page with printed geometry values

### Standards-side and quasi-standards-side classes

1. IEC `61188-5-8:2007`
2. IEC `61188-6-2:2021`
3. IEC `60191-6-2:2001`
4. IPC `7351B` product page and public TOC PDF
5. JEDEC official primary lane as recoverable in the current environment

## Findings

### 1. No new owner-side surface exceeds the current `Microchip + Renesas + NXP + Intel` stack

- Infineon is the strongest new owner-side near-hit from this pass because current-public `PG-TFBGA` package pages do expose:
  - true `0.75 mm` pitch identity
  - named package-family identity
  - a visible package page with `Footprint Drawing` in the same owner-controlled surface
- but the current surfaced Infineon public pages still do not expose one same-surface printed PCB land-pattern geometry row strong enough to exceed the current stack
- NXP processor-package datasheet sections do show true `0.75 mm` package identity and ball-matrix context
- but they do not add one stronger printed PCB land-pattern geometry page above the current owner stack
- ST does expose printed geometry numbers in one public BGA design-rule class
- but the concrete surfaced package in that document is actually `0.8 mm`, not a true `0.75 mm` package hit

### 2. No new standards-side or quasi-standards-side surface exceeds the current public ceiling

- current official IEC pages remain strong for family framing only:
  - `IEC 61188-5-8` for area-array land-pattern family scope
  - `IEC 61188-6-2` for later maintained SMD land-pattern-design scope
  - `IEC 60191-6-2` for visible coarse-pitch package-design framing, but not `0.75 mm`
- IPC `7351B` public surfaces remain the strongest quasi-standards near-hit from this pass
- but even the public TOC still exposes only section-level framing and table names, not one visible `0.75 mm` geometry row or table
- JEDEC did not produce one recoverable current-public official primary surface strong enough to raise the ceiling in this environment

### 3. The safest result remains `no reopen`

- no new owner-controlled public surface exceeded the current `Microchip + Renesas + NXP + Intel` owner stack
- no new standards-side or quasi-standards-side public surface exceeded the current metadata-level family framing for generic `0.75 mm`
- the repo-supported `0.75 mm` ceiling therefore still remains:
  - three Microchip current-public exact rows
  - one Renesas second-owner exact-data page
  - one NXP third-owner exact-data page
  - one Intel-hosted fourth-owner exact table

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat current-public Infineon `PG-TFBGA` package pages as if true `0.75 mm` identity plus `Footprint Drawing` alone already exceeds the current stack
- future AI should not treat NXP processor-package identity pages as if ball-map and package identity alone already create a stronger `0.75 mm` land-pattern authority
- future AI should not treat the surfaced ST `0.80/0.75 mm` design-rule table as a true `0.75 mm` package hit when the actual package in context is `0.8 mm`
- future AI should not treat IPC `7351B` TOC visibility as if it already exposes one citable public `0.75 mm` geometry table

## Continuation Rule

Keep `0.75 mm` as a watch-only residual below `1.50 mm`.

Do not reopen it again unless a future pass recovers either:

1. one same-surface public owner document with true `0.75 mm` package identity plus printed PCB land-pattern geometry strong enough to exceed the current owner stack
2. one legitimately public official geometry surface above the current IEC and IPC metadata-level ceiling
