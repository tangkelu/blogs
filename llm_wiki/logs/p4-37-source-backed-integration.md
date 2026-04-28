# P4-37 Source-Backed Integration

Date: 2026-04-28

Status: `source_backed_fact_layer_partial`

## Scope

This integration converts the strongest P4-37 official-source scout findings into reusable `llm_wiki` records for:

- `/code/blogs/tmps/2025.8.12/en` RF / high-speed / impedance drafts
- `/code/blogs/tmps/2025.8.1/en` application / inspection / regulated-use drafts
- `/code/blogs/tmps/2025.7.23/en` specialty material / finish / copper foil / insulation / coating / LTCC drafts

The original drafts remain claim inventory only. No draft-originated price, lead time, MOQ, stock, supplier capability, certification status, process window, yield, quality rate, RF result, thermal result, application qualification, or legal conclusion was promoted.

## Source Records Added

### RF / high-speed / OTA

- `ipc-6018d-toc`
- `ipc-4103b-toc`
- `keysight-vna-system-impedance-help`
- `keysight-e5055a-measurement-parameters-help`
- `keysight-power-integrity-analysis-page`
- `rohde-schwarz-ts8991-ota-system-page`
- `rohde-schwarz-dst200-rf-chamber-page`

### Interface / wireless / regulated applications

- `hdmi-2-1b-spec-page`
- `ieee-8023-ethernet-working-group`
- `ieee-p8023dm-task-force`
- `bluetooth-core-specification-page`
- `gps-gov-civil-gps-accuracy-page`
- `iso-26262-road-vehicles-functional-safety-package`
- `aec-documents-page`
- `fda-mri-benefits-and-risks-page`
- `faa-ac-20-152a-page`

### Specialty materials / finishes / protection

- `ipc-4555-toc`
- `ipc-4562b-toc`
- `jx-electrodeposited-copper-foil-page`
- `jx-rolled-copper-foil-page`
- `tex-rolled-copper-foil-page`
- `ipc-tm650-2637-surface-insulation-resistance`
- `dow-gels-encapsulants-conformal-coatings-page`
- `macdermid-electrolube-peelable-coating-mask`
- `kyocera-ltcc-material-page`

## Fact Cards Added

- `standards-high-frequency-printed-board-and-material-boundary`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `standards-interface-wireless-positioning-product-level-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`
- `materials-copper-foil-classes-and-roughness-boundary`
- `standards-ipc-surface-finish-taxonomy-osp-hasl-extension`
- `methods-insulation-coating-potting-peelable-mask-boundaries`
- `materials-ltcc-class-definition-and-nonclaims`

## Topic Wiki Updates

- Updated `wiki/testing/rf-validation-and-test-coverage.md` with Keysight impedance / S-parameter / PDN and R&S OTA / chamber boundaries.
- Updated `wiki/materials/high-speed-material-family-selection.md` with `IPC-6018` vs `IPC-4103` scope separation.
- Updated `wiki/applications/industry-application-scenarios-and-boundaries.md` with interface, wireless, automotive, medical, and aerospace qualification boundaries.
- Updated `wiki/processes/finish-zoning-and-selective-multi-finish.md` with OSP and HASL taxonomy corrections.
- Updated `wiki/processes/conformal-coating-protection-workflow-and-application-boundaries.md` with SIR, potting / encapsulation, and peelable-mask boundaries.
- Updated `wiki/materials/ceramic-aln-ims-thermal-platforms.md` with LTCC class-definition boundaries.
- Added `wiki/materials/copper-foil-class-roughness-and-rf-boundaries.md`.

## Reusable Data Unlocked

- `IPC-6018` can be used as public high-frequency / microwave printed-board specification-scope metadata.
- `IPC-4103` can be used as public high-speed / high-frequency base-material specification-scope metadata.
- `50 ohm` can be framed as measurement-system / instrument-reference context when using Keysight source language, not as a universal PCB trace rule.
- S-parameters can be explained as reflection and transmission measurement families without inventing acceptance thresholds.
- OTA / chamber content can be written as wireless-device test workflow, not PCB supplier capability.
- HDMI / Ethernet / Bluetooth / GPS can be used as interface or receiver-system context, not bare-PCB compliance.
- ISO 26262 / IATF 16949 / AEC-Q / FDA MRI / FAA AC 20-152A can be used as application-layer boundaries, not board qualification proof.
- Copper foil classes can be described using IPC and vendor category language, while roughness, RF loss, and bend life remain exact-source gated.
- Finish taxonomy can now correct `IPC-4554` misuse and add `IPC-4555` OSP plus `IPC-6012F` HASL / solder-coating metadata context.
- SIR, conformal coating, gel, encapsulant, potting, and peelable coating mask can be explained as distinct method / protection families.
- LTCC can be defined using KYOCERA's official page while keeping LTCC separate from all ceramic PCB technologies.

## Remaining Blocked Claim Classes

- Universal impedance geometry, `50 ohm` / `100 ohm` targets, and tolerance values
- Antenna gain, efficiency, TRP, TIS, range, RF performance, eye diagrams, jitter, EMI, or channel-loss results
- Supplier VNA / TDR / OTA / chamber capability and standard-scope test coverage
- HDMI / Ethernet / Wi-Fi / Bluetooth / GPS product compliance, certification, range, throughput, sensitivity, or accuracy
- ISO 26262 / ASIL / PPAP / AEC / IATF / FDA / MR / FAA / AS9100 / ITAR supplier or product qualification
- Copper roughness numbers, RF loss tables, bend-life claims, heavy-copper current / thermal outcomes
- Finish thickness, shelf life, black-pad guarantees, wire-bond guarantees, RF-loss rankings, XRF cadence, or yield
- Waterproof / IP rating / immersion / service-life claims for PCB or PCBA alone
- LTCC process windows, shrinkage, hermeticity, cavity tolerance, line / space, layer count, or supplier capability

## Next Recovery Lanes

- Add official Wi-Fi Alliance public program pages if Wi-Fi draft rehabilitation needs stronger certification wording than the current product-level boundary.
- Add eCFR / DDTC sources only if defense / ITAR drafts are retained for publication.
- Add exact foil product datasheets before any copper roughness or insertion-loss table is written.
- Add exact LTCC / alumina / AlN product datasheets before any ceramic numeric comparison table is written.
- Require dated APT / HIL capability records for supplier-specific equipment, capacity, lead time, price, yield, quality-rate, and certification claims.
