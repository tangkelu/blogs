# P4-124 FPGA Platform And High-Speed IO Identity Source-Backed Integration

Date: 2026-05-02

## Purpose

Recover the next narrow non-held source-backed lane after `P4-123` by upgrading `fpga-pcb.md` from generic compute-boundary reuse to an owner-backed FPGA platform and IO-identity lane.

This pass does not promote interface-validation proof, throughput proof, signal-integrity proof, exact BGA escape tables, programming guarantees, supplier readiness, or production readiness.

## Inputs Reviewed

- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `logs/p4-92-2026-4-29-conservative-rewrite-consumption-batch-3.md`
- `logs/p4-116-2026-5-2-2026-4-29-claim-inventory.md`
- `tmps/2026.4.29/en/fpga-pcb.md`
- existing local support:
  - `wiki/processes/compute-infrastructure-pcb-review-boundaries.md`
  - `facts/methods/high-speed-interface-system-context.md`
  - `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
- official sources checked on 2026-05-02:
  - AMD `Versal` owner page
  - AMD `Kintex UltraScale` owner page
  - Intel `Agilex` owner page

## Integrated Source-Backed Lane

### FPGA Platform And High-Speed IO Identity Boundary

Added source records:

- `interfaces/amd-versal-adaptive-soc-page`
- `interfaces/amd-kintex-ultrascale-page`
- `interfaces/intel-agilex-fpga-page`

Added fact card:

- `interfaces-fpga-platform-and-high-speed-io-identity-boundary`

Added topic wiki:

- `processes-fpga-pcb-review-boundaries`

Supported draft family:

- FPGA platform / guarded IO noun subset of `/code/blogs/tmps/2026.4.29/en/fpga-pcb.md`

## What Is Now Source-Backed

- exact `Versal` may now be used as an AMD-owned adaptive-SoC platform noun
- exact `Kintex UltraScale` may now be used as an AMD-owned FPGA family noun
- exact `Agilex` may now be used as an Intel-owned FPGA portfolio noun
- guarded `PCIe`, `DDR5`, and `LVDS` wording may now be paired with FPGA drafts only as IO-family or memory-interface context, not as board-capability proof

## Boundary Added

The new lane is intentionally identity-only and board-review-only:

- keep FPGA-family nouns at owner-backed identity level
- keep IO nouns as design-pressure context only
- route `fpga-pcb.md` through `processes-fpga-pcb-review-boundaries`
- continue pairing FPGA wording with impedance, stackup, and validation-separation cards rather than widening into performance claims

## Blocked Claim Classes

Still blocked after `P4-124`:

- exact lane-rate, throughput, bandwidth, jitter, skew, BER, eye, or channel-pass claims
- exact BGA pitch, breakout geometry, via recipe, stackup recipe, power, or thermal numerics
- any claim that `Versal`, `Kintex UltraScale`, or `Agilex` proves board readiness, interoperability, or deployment readiness
- any claim that `PCIe`, `DDR5`, or `LVDS` is validated on a finished board
- any supplier capability, shop qualification, customer-program, or production-readiness claim
- any generic claim that JTAG, programming, or debug support is guaranteed for every FPGA board

## Residual Disposition After P4-124

- `fpga-pcb.md` now has narrow source-backed support for:
  - owner-backed FPGA platform nouns
  - guarded high-speed IO and memory-interface-family context
  - existing board-review posture around BGA escape pressure, stackup discipline, impedance, and staged validation
- `fpga-pcb.md` still does not have source-backed support for:
  - interface behavior or pass/fail proof
  - exact transceiver, memory, or SI numerics
  - programming, bring-up, or production-readiness claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `fpga-pcb.md` at platform-identity and guarded IO-context level only
- mainline unchanged:
  - `P4-121` remains the active first-wave prompt-handoff controller
