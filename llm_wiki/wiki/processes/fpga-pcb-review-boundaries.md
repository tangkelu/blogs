---
topic_id: "processes-fpga-pcb-review-boundaries"
title: "FPGA PCB Review Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "interfaces-fpga-platform-and-high-speed-io-identity-boundary"
  - "methods-high-speed-interface-system-context"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "methods-boundary-scan-does-not-prove-high-speed-channel-quality"
source_ids:
  - "amd-versal-adaptive-soc-page"
  - "amd-kintex-ultrascale-page"
  - "intel-agilex-fpga-page"
  - "pcisig-pcie-5-faq"
  - "pcisig-pcie-6-faq"
  - "micron-ddr5-sdram-page"
  - "ti-lvds-overview-page"
tags: ["fpga", "versal", "kintex-ultrascale", "agilex", "pcie", "ddr5", "lvds", "bga", "high-speed", "review-boundary"]
---

# Definition

> FPGA PCB writing is safe only when it stays inside a board-review boundary: owner-backed FPGA platform identity, dense-BGA escape pressure, stackup and impedance discipline, guarded interface-family context, and explicit separation between first-build confirmation, boundary-scan access, and separate channel validation. The current corpus does not support turning FPGA-family nouns into finished-board capability proof or production-readiness claims.

## Why This Topic Matters

- FPGA board drafts often jump from device-family names straight into workload, interface, or deployment claims.
- The landed facts already support a narrower but reusable review posture: dense digital package pressure, IO-family context, controlled-impedance planning, and staged validation separation.
- This page gives future AI workers one active boundary surface for FPGA PCB content without drifting into unsupported speed, readiness, or supplier claims.

## FPGA Review Model

### Layer 1: Platform Identity

| Layer | Safe posture | What it does not prove |
|---|---|---|
| **FPGA family nouns** | Use `Versal`, `Kintex UltraScale`, and `Agilex` as owner-backed platform names | Workload suitability, board capability, or supplier readiness |
| **Board context** | Describe the PCB as a dense digital or high-speed review surface around the platform | That the board is already validated or deployable |

### Layer 2: Interface Pressure

| Interface family | Safe posture | What it does not prove |
|---|---|---|
| **PCIe** | System-context pressure that raises routing and validation demands | Protocol pass, interoperability, or lane-rate success |
| **DDR5** | Memory-interface pressure that tightens stackup, escape, and timing review | Stable bandwidth, timing closure, or SI success |
| **LVDS** | IO-family context for signaling and routing review | Final signal integrity, noise margin, or field behavior |

### Layer 3: Board Review And Validation Separation

| Review layer | Safe posture |
|---|---|
| **BGA escape and stackup** | Treat FPGA boards as BGA-dense layouts that need stackup and escape discipline |
| **Controlled impedance** | Keep impedance planning and TDR posture in the high-speed review lane |
| **FAI** | First-build confirmation and setup-release discipline |
| **Boundary-scan / JTAG** | Test-access and digital-interconnect layer only |
| **Separate SI / protocol validation** | Still required beyond FAI or JTAG access |

## Stable Facts

- AMD owner pages support `Versal` and `Kintex UltraScale` as real FPGA / adaptive-SoC family nouns.
- Intel owner pages support `Agilex` as a real FPGA portfolio noun.
- Existing public interface-context sources support `PCIe`, `DDR5`, and `LVDS` only as ecosystem or interface-family context.
- Existing high-speed and validation cards support BGA escape pressure, stackup sensitivity, controlled-impedance posture, and first-article-versus-separate-high-speed-validation separation.
- The landed boundary-scan card supports a strict separation between JTAG / test-access language and high-speed channel proof.
- Together these facts support one reusable FPGA review posture:
  `platform identity -> interface pressure -> stackup / escape discipline -> staged validation separation`,
  while keeping finished-board claims outside the stable authority layer.

## Active Review Guidance

### Use This Page For

- FPGA board-review language
- owner-backed platform naming
- BGA escape and stackup-pressure framing
- separating interface context from validation proof

### Safe Vocabulary

- `dense digital board review`
- `BGA escape pressure`
- `stackup discipline`
- `controlled-impedance posture`
- `interface-family context`
- `first-build confirmation`
- `boundary-scan access`
- `separate channel validation`

### Recommended Routing Flow

- Start with the FPGA platform as an owner-backed device family.
- Add interface families only as design-pressure context.
- Move to BGA escape, stackup, impedance, and validation planning.
- Keep FAI, JTAG, and high-speed validation in separate review lanes.

## Engineering Boundaries

- Do not let FPGA family nouns become board-capability proof.
- Do not write as if `PCIe`, `DDR5`, or `LVDS` context proves the board is validated for those interfaces.
- Do not let boundary-scan or JTAG language absorb channel-quality, eye, timing, or protocol-compliance claims.
- Keep first-build confirmation separate from separate high-speed validation.
- Keep stackup, escape, impedance, and debug-access language tied to review pressure rather than deployment proof.

## Common Misreadings

- `Versal` or `Agilex` naming proves a finished board supports a given workload.
- `PCIe`, `DDR5`, or `LVDS` naming proves validated interface behavior.
- `FAI` replaces separate signal-path validation.
- `JTAG` or boundary-scan proves channel quality.
- FPGA family names prove shop capability, sector readiness, or production success.

## Must Refresh Before Publishing

- any exact data-rate, lane-count, bandwidth, jitter, skew, or eye-result statement
- any exact power, thermal, BGA-pitch, via, or stackup numeric
- any statement about supplier readiness, program deployment, or customer qualification
- any claim that JTAG, FAI, or boundary-scan is sufficient for high-speed validation

## Related Fact Cards

- `interfaces-fpga-platform-and-high-speed-io-identity-boundary`
- `methods-high-speed-interface-system-context`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `methods-boundary-scan-does-not-prove-high-speed-channel-quality`

## Primary Sources

- https://www.amd.com/en/products/adaptive-socs-and-fpgas/versal.html
- https://www.amd.com/en/products/adaptive-socs-and-fpgas/fpga/kintex-ultrascale.html
- https://www.intel.com/content/www/us/en/products/details/fpga/agilex.html
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_5.0
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_6.0
- https://www.micron.com/products/memory/dram-components/ddr5-sdram
- https://www.ti.com/product-category/interface/lvds/overview.html
