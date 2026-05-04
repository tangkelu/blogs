---
fact_id: "interfaces-fpga-platform-and-high-speed-io-identity-boundary"
title: "Versal, Kintex UltraScale, and Agilex are owner-backed FPGA platform nouns, not PCB capability proof"
topic: "fpga platform and high-speed io identity boundary"
category: "interfaces"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "amd-versal-adaptive-soc-page"
  - "amd-kintex-ultrascale-page"
  - "intel-agilex-fpga-page"
  - "pcisig-pcie-5-faq"
  - "pcisig-pcie-6-faq"
  - "micron-ddr5-sdram-page"
  - "ti-lvds-overview-page"
tags: ["fpga", "versal", "kintex-ultrascale", "agilex", "pcie", "ddr5", "lvds", "identity-boundary", "high-speed-io"]
---

# Canonical Summary

> AMD and Intel owner pages support one narrow FPGA identity lane only: `Versal`, `Kintex UltraScale`, and `Agilex` may be used as owner-backed FPGA platform nouns, and guarded `PCIe`, `DDR5`, and `LVDS` wording may be used only as adjacent IO or memory-interface family context. The current evidence layer does not support turning those nouns into finished-PCB capability proof, interface-validation proof, or supplier-readiness proof.

## Stable Facts

- AMD publicly presents `Versal` as an adaptive-SoC family with programmable logic, programmable I/O, high-speed serial transceivers, and broad hard-IP context.
- AMD publicly presents `Kintex UltraScale` as an FPGA family and exposes guarded `PCI Express`, `DDR4`, and transceiver-family vocabulary on the owner page.
- Intel publicly presents `Agilex` as an FPGA and SoC FPGA portfolio with multiple family tiers.
- Existing public interface-context sources already support `PCIe`, `DDR5`, and `LVDS` as ecosystem or interface-family nouns that create board-review pressure without proving a finished board.
- Across these sources, it is safe to describe an FPGA board as a platform-and-IO review surface rather than as a proof of validated high-speed behavior.

## Conditions And Methods

- Use this card only for `fpga-pcb.md` and adjacent FPGA board-review drafts when exact owner-backed platform nouns are necessary.
- Safe posture: keep `Versal`, `Kintex UltraScale`, and `Agilex` at owner-backed platform-identity level.
- Safe companion posture: keep `PCIe`, `DDR5`, and `LVDS` as design-pressure, transceiver-adjacent, or memory-interface-family context only.
- Pair this card with:
  - `methods-high-speed-interface-system-context`
  - `methods-controlled-impedance-tdr-verification-posture`
  - `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- Keep FPGA platform nouns separate from supplier capability, compliance, or release-readiness language.

## Limits And Non-Claims

- This card does not authorize exact lane rates, jitter, skew, eye results, BER, insertion loss, reach, or timing-budget claims.
- It does not authorize claims that a PCB shop supports `Versal`, `Kintex UltraScale`, or `Agilex` by default.
- It does not authorize claims that `PCIe`, `DDR5`, or `LVDS` are validated on a finished board.
- It does not authorize exact BGA escape geometry, stackup recipe, power, thermal, deployment, or production-readiness claims.
- It does not authorize JTAG, programming, bring-up, or debug guarantees for every FPGA family or device.

## Open Questions

- Add narrower owner-backed pages later if a future rewrite must retain other FPGA family nouns or exact per-series hard-IP nouns.
- Add a separate FPGA bring-up or configuration lane only if future drafts truly need device-programming or debug-boundary claims with official support.

## Source Links

- https://www.amd.com/en/products/adaptive-socs-and-fpgas/versal.html
- https://www.amd.com/en/products/adaptive-socs-and-fpgas/fpga/kintex-ultrascale.html
- https://www.intel.com/content/www/us/en/products/details/fpga/agilex.html
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_5.0
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_6.0
- https://www.micron.com/products/memory/dram-components/ddr5-sdram
- https://www.ti.com/product-category/interface/lvds/overview.html
