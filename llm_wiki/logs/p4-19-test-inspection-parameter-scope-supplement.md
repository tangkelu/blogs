# P4-19 Test And Inspection Parameter-Scope Supplement

Date: 2026-04-27

## Purpose

Add source-backed parameter / scope cards for inspection and test methods that can support empty-image blog work without inventing coverage, yield, or pass/fail performance.

This pass stays inside `llm_wiki/facts/methods/` plus one new log file and does not write blogs.

## Files Added

- `llm_wiki/facts/methods/parameter-scope-test-inspection-optical-method-dimensions.md`
- `llm_wiki/facts/methods/parameter-scope-test-inspection-electrical-access-method-dimensions.md`
- `llm_wiki/facts/methods/parameter-scope-test-inspection-high-speed-si-measurement-dimensions.md`
- `llm_wiki/facts/methods/parameter-scope-test-inspection-launch-functional-vocabulary.md`
- `llm_wiki/logs/p4-19-test-inspection-parameter-scope-supplement.md`

## Source Layer Used

Primary method and internal-page records used in this pass:

- `koh-young-spi-technology`
- `koh-young-aoi-technology`
- `frontendapt-pcba-spi-inspection-page-en`
- `frontendapt-pcba-aoi-inspection-page-en`
- `frontendapt-pcba-xray-inspection-page-en`
- `frontendapt-pcba-ict-test-page-en`
- `frontendapt-pcba-flying-probe-testing-page-en`
- `keysight-ict-systems`
- `xjtag-jtag-chains`
- `xjtag-bsdl-file`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendhil-high-speed-product-page-en`
- `frontendhil-high-frequency-product-page-en`
- `frontendapt-pcba-first-article-inspection-page-en`
- `frontendapt-pcba-quality-system-page-en`
- `usb-if-type-c-functional-test-spec-2024-03-03`
- `usb-if-type-c-cable-connector-spec-r2-0`
- `usb-if-type-c-compliance-updates-page`
- `usb-if-pd-compliance-updates-page`
- `usb-if-qbs-information-page`
- `usb-if-connector-qbs-guidelines-page`
- `ipc-a-610h-toc`
- `ipc-j-std-001j-toc`
- `ipc-9252b-toc`
- `ipc-tm650-test-methods-index`

## Key Parameters And Method Dimensions Added

### Optical inspection

- SPI measurement vocabulary:
  `paste volume`, `paste area`, `paste height`, `alignment / offset`, `bridging`, `missing paste`, `trend monitoring`
- AOI scope vocabulary:
  `2D AOI`, `3D AOI`, `bare-board AOI`, `SMT AOI`, `component placement`, `solder-joint formation`, `polarity`, `shadowing`, `hidden geometry`
- X-ray scope vocabulary:
  `2D`, `2.5D`, `3D CT`, `voids`, `bridges`, `cold joints`, `BGA`, `QFN`, `CSP`

### Electrical-access test

- ICT vocabulary:
  `bed-of-nails`, `fixture-based`, `node-level verification`, `continuity`, `shorts`, `component values`
- Flying-probe vocabulary:
  `fixture-free`, `bare PCB`, `assembled PCBA`, `continuity`, `opens`, `shorts`, `value`, `polarity`
- JTAG / BSDL vocabulary:
  `TDI`, `TDO`, `TCK`, `TMS`, optional `nTRST`, `multiple chains`, `TAP pins`, `instruction register`, `boundary register`, `package mapping`, `compliance pins`

### High-speed SI measurement

- APT impedance page vocabulary:
  `single-ended`, `differential`, `coplanar`, `50 / 75 / 90 / 100 ohm`, `±5 ohm / ±7%`, `100% TDR`
- APT / HIL high-speed and high-frequency page vocabulary:
  `TDR / VNA`, `S-parameters`, `85 / 90 / 100 ohm ±5%`, `DC–40 GHz`, `40–67 GHz`, `35 ps`, `10–112 Gbps`

### Launch / functional-test vocabulary

- FAI vocabulary:
  `first-run verification`, `setup confirmation`, `NPI release`, `process / materials / documentation readiness`
- USB-IF functional-test vocabulary:
  `Product Under Test`, `VIF`, `functional test`, `state machine`, `VCONN`, `USB PD implementation context`
- USB Type-C scope and program vocabulary:
  `receptacle`, `plug`, `cable assembly`, `detection`, `USB Type-C compliance updates`, `USB PD compliance updates`, `Qualification by Similarity`

## Boundary Rules Enforced In This Pass

- No invented inspection coverage percentages
- No invented test coverage percentages
- No invented defect-detection rates
- No invented cycle-time or yield claims
- No invented acceptance thresholds
- No conversion of IPC public metadata into clause-level workmanship or soldering criteria
- No conversion of internal TDR / VNA values into universal compliance-pass or lot-release rules
- No conversion of USB-IF functional-test vocabulary into certification, output-power, or protocol-table claims

## Blog-Support Mapping

- `boundary-scan / JTAG`:
  supported by the electrical-access card as topology and BSDL-prerequisite vocabulary only
- `FAI`:
  supported by the launch / functional vocabulary card as first-run gate language only
- `flying-probe / ICT`:
  supported by the electrical-access card as access-mode and node-check vocabulary only
- `low-void BGA`:
  supported by the optical card for SPI upstream measurement and X-ray hidden-joint visibility only
- `high-speed SI`:
  supported by the high-speed SI measurement card for impedance / TDR / VNA measurement vocabulary only
- `type-c charger`:
  supported by the launch / functional vocabulary card for USB-IF functional-test and compliance-program vocabulary, with optical / electrical-access cards available as assembly-test companions

## Gaps That Remain

- No licensed IPC clause content for assembly acceptability, soldering requirements, or class-specific thresholds
- No source-backed universal void thresholds for BGA or BTC packages
- No neutral public source in this pass for ICT / flying-probe coverage percentages or economic selection rules
- No source-backed universal BER, insertion-loss, return-loss, jitter, or eye-mask acceptance thresholds for high-speed blogs
- No USB-IF-backed public extraction in this pass for exact timers, voltage/current limits, PD message tables, or certification outcome rules

## Verification Notes

- The new cards intentionally keep numeric method dimensions fenced as page-scoped vocabulary where the source is internal or dynamic.
- Forbidden files were not edited in this pass.
- Shared-worktree caution remains: other unrelated modifications in `llm_wiki` were left untouched.
