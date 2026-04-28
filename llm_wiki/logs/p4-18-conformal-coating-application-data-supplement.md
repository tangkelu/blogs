# P4-18 Conformal Coating Application Data Supplement

Date: 2026-04-27

## Purpose

Continue the empty-image data-first program without writing blogs.

This round focuses only on the conformal-coating top-tier candidates from:

- `/code/hileap/frontendHIL/docs/2026-04-23-empty-image-blog-rewrite-priority-list.md`

Target slugs:

- `conformal-coating-medical-imaging-wearable`
- `conformal-coating-automotive-adas-ev-power`
- `conformal-coating-data-center-optical-module`
- `conformal-coating-5g-6g-communication`
- `conformal-coating-5g-6g-communication-2`

The goal is not to make these articles aggressive. The goal is to improve source-backed readiness for conservative rewrites while making overclaim boundaries explicit enough that later prompt execution cannot silently leak into regulated, optical, RF, or high-voltage proof.

## What Landed

New fact cards:

- `facts/methods/conformal-coating-telecom-rf-boundary.md`
- `facts/methods/conformal-coating-optical-interface-keepout-boundary.md`
- `facts/methods/conformal-coating-medical-regulated-boundary.md`
- `facts/methods/conformal-coating-automotive-ev-power-boundary.md`

New topic page:

- `wiki/processes/conformal-coating-application-readiness-map.md`

## Why This Round Was Needed

Existing coating coverage already supported:

- general protection workflow
- application-context framing
- masking and test-access workflow
- one broad lane-B rewrite gate

What it did not yet do well enough for these five slugs was separate the application-specific failure modes:

- telecom wording drifting into RF or mmWave behavior
- optical-module wording drifting into contamination-control or BER claims
- medical wording drifting into biocompatibility, sterilization, or ISO/FDA proof
- automotive and EV power wording drifting into ASIL, ISO 26262, creepage, or high-voltage safety proof

This round closes that gap at the fact-card level without inventing new process windows or performance data.

## Readiness Changes

| slug | previous posture | new posture | note |
| --- | --- | --- | --- |
| `conformal-coating-5g-6g-communication` | broad lane-B only | `boundary_ready_for_conservative_rewrite` | now has a telecom-specific card that forces protection workflow away from RF-performance language |
| `conformal-coating-5g-6g-communication-2` | broad lane-B only | `boundary_ready_for_conservative_rewrite_same_lane` | same safe lane as primary slug; no stronger promise allowed |
| `conformal-coating-data-center-optical-module` | broad lane-B only | `boundary_ready_with_optical_keepout_limits` | now has an optical-interface keepout card, but still no optical cleanliness or BER support |
| `conformal-coating-medical-imaging-wearable` | `needs_refresh_then_go` | unchanged status, stronger containment | now has a dedicated medical-regulated boundary card to block compliance and patient-safety drift |
| `conformal-coating-automotive-adas-ev-power` | broad power/coating boundary only | `boundary_ready_with_functional_safety_block` | now has an automotive/EV-specific card that blocks ASIL, ISO 26262, and high-voltage safety inflation |

## Source Posture

This round intentionally reused existing local registry records only.

Primary source families used:

- IPC-CC-830C public metadata
- Electrolube and HumiSeal public coating-family framing
- local APT industry JSON for telecom, server/data-center, medical, automotive, and power-energy context
- local APT PCB and PCBA JSON for coating, high-speed, backplane, antenna, quality, ICT, flying probe, FCT, first article, and final inspection

No new source registry records were added because the needed application framing was already represented in stable local records.

## Explicitly Blocked Claim Classes

This round does not unlock:

- biocompatibility, sterilization compatibility, patient-contact suitability, FDA applicability, ISO 13485 proof
- ISO 26262, ASIL, creepage, clearance, dielectric-strength, insulation, high-voltage safety, automotive qualification
- optical cleanliness, contamination-control certainty, non-outgassing, optical coupling, BER, module-release proof
- RF, antenna, mmWave, FR1, FR2, protocol-validation, telecom qualification, or deployment-proof claims
- coating thickness, cure schedule, cleanliness limits, masking dimensions, keepout dimensions, pass/fail criteria, yield, cost, lead time, or supplier capability claims

## Remaining Gaps

- `conformal-coating-data-center-optical-module` still lacks a narrower official source layer for optical-interface contamination, non-outgassing, or connector-cage cleanliness language.
- `conformal-coating-medical-imaging-wearable` still lacks formal public sources for medical material compatibility, sterilization compatibility, or regulated-device role boundaries beyond conservative manufacturing-control posture.
- `conformal-coating-automotive-adas-ev-power` still lacks official automotive or EV qualification sources for insulation, creepage, ASIL, lifetime, or safety claims.
- `conformal-coating-5g-6g-communication` and `-2` still lack official RF-validation or telecom-qualification sources that would justify any measured RF or mmWave benefit from coating.

## Verification Target

This round is complete when:

1. all new `fact_id` and `source_id` references resolve in scoped validation
2. `git diff --check` passes
3. later prompt execution can consume explicit status and blocked-claim guidance from the new readiness map
