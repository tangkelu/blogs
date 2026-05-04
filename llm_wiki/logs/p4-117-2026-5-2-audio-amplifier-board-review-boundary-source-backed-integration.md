# P4-117 Audio Amplifier Board-Review Boundary Source-Backed Integration

Date: 2026-05-02

## Purpose

Recover the next exact non-held source-first lane after `P4-116` closeout by upgrading `audio-amplifier-pcb.md` from conservative-rewrite-only status to a narrow source-backed board-review boundary.

This pass does not promote audio-performance claims, speaker-load recommendations, compliance proof, topology superiority, supplier-readiness claims, or production-readiness claims.

## Inputs Reviewed

- `logs/p4-95-2026-5-1-audio-conservative-rewrite-and-dna-biological-hold-integration.md`
- `logs/p4-116-2026-5-2-2026-4-29-claim-inventory.md`
- `/code/blogs/tmps/2026.4.29/en/audio-amplifier-pcb.md`
- existing local support:
  - `sources/registry/methods/analog-devices-mixed-signal-pcb-layout-guidelines.md`
  - `sources/registry/methods/analog-devices-layout-considerations-for-high-power-circuits.md`
  - `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
  - `facts/methods/current-carrying-trace-width-and-copper-boundary.md`

## Integrated Source-Backed Lane

### Audio-Amplifier PCB Review Boundary

Added source records:

- `ti-managing-emi-in-class-d-audio-applications`
- `ti-tpa3118d2evm-user-guide`

Added fact card:

- `methods-audio-amplifier-pcb-review-boundary`

Added topic wiki:

- `processes-audio-amplifier-pcb-review-boundaries`

Supported draft family:

- board-review subset of `/code/blogs/tmps/2026.4.29/en/audio-amplifier-pcb.md`

What is now source-backed:

- sensitive-versus-noisy region planning for audio-amplifier boards
- power-path and speaker-output-path review as layout and EMI surfaces rather than audio-performance proof
- connector, interface, and access planning as board-review and bring-up surfaces
- documented prototype preparation through schematic / BOM / PCB-layout visibility on an official EVM guide

## Boundary Added

The new lane is intentionally board-review-only:

- keep audio-amplifier wording at mixed-signal partitioning, speaker/output path caution, connector access, and bring-up preparation level
- route future audio-amplifier rewrites through `processes-audio-amplifier-pcb-review-boundaries`
- reuse the existing grounding and current-carrying cards only as companion layers, not as audio-performance proof

## Blocked Claim Classes

Still blocked after `P4-117`:

- exact `THD`, `SNR`, `noise floor`, `frequency response`, `sound quality`, or listening-outcome claims
- exact output-power, efficiency, speaker-load, thermal-rise, or EMI-compliance claims
- exact codec, DSP, wireless, interface-product, or amplifier-topology superiority claims
- any claim that an EVM or reference board proves supplier capability, qualified production, or release readiness

## Residual Disposition After P4-117

- `audio-amplifier-pcb.md` now has narrow source-backed support for:
  - mixed-signal partitioning
  - speaker/output path caution
  - connector and interface access planning
  - prototype bring-up and documented board-preparation language
- `audio-amplifier-pcb.md` still does not have source-backed support for:
  - audio-performance metrics
  - compliance or EMI-test outcomes
  - topology-, codec-, or platform-specific product claims
  - supplier capability or production-readiness claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `audio-amplifier-pcb.md` at board-review boundary level only
- next likely action:
  - keep `2026.4.29/en` on source-backed reuse mode and reopen new lanes only for exact non-held claim families that still lack their own fact layer
