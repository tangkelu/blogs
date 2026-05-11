# P4-321 Connector-Owner Amphenol Public Access Blocker Note

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_public_source_access_recheck`

## Purpose

Recheck whether one additional connector-owner drawing candidate can safely strengthen the current `connector-origin / installation mark` lane beyond the existing `KiCad + Molex` boundary.

This pass does not create new `sources/registry/` or `facts/` records unless the candidate drawing is publicly retrievable and text-verifiable as a real owner document.

## Inputs

- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`

## Candidate Rechecked

- Amphenol candidate noted in `P4-315`:
  - `https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/10178546.pdf`

## What This Pass Confirmed

- the Amphenol candidate remains structurally promising at scout level because `P4-315` associated it with:
  - `ARROW MARK`
  - `CONNECTOR FRONT SIDE`
  - `PIN-1`
- the currently reachable public URL did not return a real PDF during this pass
- direct fetch returned `403` plus Cloudflare challenge HTML rather than a retrievable owner drawing

## Negative Finding Worth Preserving

- this candidate should remain in `scout` status only
- it is not safe to promote the Amphenol candidate into `sources/registry/` while the currently reachable public endpoint is challenge-blocked and cannot be reverified as a real owner document in this environment
- the current reusable ceiling for this lane therefore remains:
  - `KiCad KLC` as CAD-owner convention
  - `Molex 105133` as connector-owner named-series drawing

## What Did Not Land

- no new official source record
- no new boundary fact card
- no new wiki route change

## Final Status

- lane result:
  - `candidate_rechecked_but_public_access_blocked`
- continuation state:
  - `connector_owner_amphenol_candidate_should_not_be_promoted_until_publicly_retrievable`
  - `p4_317_remains_the_current_lane_ceiling`
