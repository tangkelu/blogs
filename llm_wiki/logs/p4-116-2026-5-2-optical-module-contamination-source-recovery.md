# P4-116 2026-05-02 Optical Module Contamination Source Recovery

Date: 2026-05-02

Status: `source_backed_fact_layer_partial`

## Purpose

Determine whether current official authority exists for optical-module handling / contamination-control wording that is more reusable than the existing keepout-only boundary, without overstating optical performance, non-outgassing, or release readiness.

## Prior State

- Existing reusable boundary: `facts/methods/conformal-coating-optical-interface-keepout-boundary.md`
- Prior blocker from `P4-114`: current corpus did not support optical cleanliness, contamination-control, non-outgassing, or qualification proof.
- Lane assignment from `P4-116` required a source-first check before any new fact promotion.

## Official Source Recovery

Current official authority was found on IEC standards-owner pages:

- `sources/registry/standards/iec-61300-3-35-2022-page.md`
- `sources/registry/standards/iec-tr-62627-01-2023-page.md`
- `sources/registry/standards/iec-tr-62572-4-2020-page.md`

### What These Sources Safely Unlock

- visual inspection wording for fibre optic connector and fibre-stub transceiver end faces
- cleaning-method wording for fibre optic connectors, adaptors, receptacles excluding optical transceivers, and dust caps
- handling-and-cleaning wording for receptacle style optical transceiver connector end faces
- explicit boundary that visual inspection does not replace optical performance measurement

### What These Sources Still Do Not Unlock

- broad optical-module contamination-control claims
- non-outgassing claims
- optical qualification, BER, attenuation-result, return-loss-result, or interoperability claims
- release-readiness or manufacturing-readiness claims
- universal contamination thresholds, cleanliness windows, or pass/fail rules

## Lane Output

Added narrow reusable fact:

- `facts/methods/optical-connector-endface-inspection-and-cleaning-boundary.md`

This fact is intentionally narrower than `optical-module contamination control` as a whole. It promotes only the part supported by current official authority: connector-endface inspection and cleaning workflow language, including receptacle-style optical transceivers.

## Exact Blocker Status

`blocker_status: partially cleared only for connector-endface inspection-and-cleaning wording backed by IEC 61300-3-35:2022, IEC TR 62627-01:2023, and IEC TR 62572-4:2020; still blocked for broad optical-module contamination-control, non-outgassing, optical-performance, and release-readiness claims`

## Decision

- lane result: `fact_partial`
- controller interpretation: `source_backed_fact_layer_partial`
- broad wiki expansion: `not justified`

## Verification

- checked source IDs referenced by the new fact card
- ran `git diff --check` on changed files
- ran targeted `sed` review on all changed lane-local files
