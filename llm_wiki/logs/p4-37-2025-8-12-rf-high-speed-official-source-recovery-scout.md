# P4-37 2025-8-12 RF / High-Speed Official-Source Recovery Scout

- Lane: `P4-37 official-source recovery scout`
- Batch: `/code/blogs/tmps/2025.8.12/en`
- Existing map reviewed: `/code/blogs/llm_wiki/logs/p4-34-2025-8-12-rf-high-speed-impedance-blog-ingestion-map.md`
- Prior adjacent scout reviewed: `/code/blogs/llm_wiki/logs/p4-36-2025-8-30-rf-microwave-official-source-recovery-scout.md`
- Model requested: `gpt-5.4`
- Scout timestamp: `2026-04-28 16:17:34 CST`
- Constraint: drafts treated as claim inventory only, not authority
- Edit scope: only this file

## Purpose

Identify official-source candidates and the strongest fact-upgrade opportunities still open for the `2025.8.12/en` RF / high-speed / impedance lane after the earlier P4-36 RF / microwave scout.

This scout does not update registries, facts, wiki pages, or global trackers.

## Draft families checked

Primary claim-family sample across the lane:

- `50-ohm-impedance-pcb.md`
- `100-ohm-impedance-pcb.md`
- `characteristic-impedance-pcb.md`
- `controlled-impedance-pcb.md`
- `differential-impedance-pcb.md`
- `high-frequency-pcb-antenna-design.md`
- `high-frequency-pcb-signal-integrity.md`
- `high-frequency-pcb-power-design.md`
- `high-frequency-pcb-testing-methods.md`
- `tdr-testing-pcb.md`
- `what-is-hf-pcb.md`
- `choosing-high-frequency-pcb-manufacturer.md`

## What was already covered before this pass

The P4-36 RF / microwave scout already covered high-value official anchors for:

- `IPC-2141A` identity and controlled-impedance definition posture
- `IPC-2228` identity and RF / microwave distributed-circuit framing
- `IPC TM-650` family metadata for TDR, propagation delay, frequency-domain loss, and high-frequency material tests
- Keysight and Tektronix basics for `VNA`, `S-parameters`, and `TDR`
- exact vendor material pages for `RO4350B`, `RO3003`, `RT/duroid 5880`, `TLY-5/TLY-5A`, and `I-Tera MT40`

This pass therefore focused only on remaining weak spots:

- neutral or primary anchors for `50 ohm` and `100 ohm` context
- stronger standards metadata for high-frequency board and material boundaries
- OTA / chamber boundary sources
- incremental SI / PDN vocabulary anchors
- supplier-selection blockers for RF / high-speed manufacturer-choice prose

## Official sources checked in this pass

### 1. IPC-6018 TOC and standard landing page

- URL: `https://www.ipc.org/TOC/IPC-6018D_TOC.pdf`
- Companion URL: `https://shop.electronics.org/ipc-6018`
- Owner: IPC / electronics.org
- Source type: official table-of-contents PDF plus official standard landing page
- Supported claims:
  - `IPC-6018` is the qualification and performance specification family for high-frequency (`microwave`) printed boards.
  - Scope includes microstrip, stripline, mixed dielectric, multilayer, with or without buried / blind vias, and metal-core variants.
  - Procurement documentation and end-use requirements matter for classification and test selection.
- Strongest upgrade use:
  - best standards anchor for tightening `high-frequency-pcb-manufacturing.md`, `high-frequency-pcb-testing-methods.md`, `hf-pcb.md`, and `what-is-hf-pcb.md`
  - useful blocker against draft language that treats high-frequency boards as one fixed construction or one universal qualification tier
- Limits / non-claims:
  - not a free source for copying acceptance tables or detailed design rules
  - not proof that any named supplier conforms to `IPC-6018`
  - not proof of antenna, OTA, SI, or RF system performance
- Candidate source ID: `src_ipc_6018_scope_landing`
- Candidate fact IDs:
  - `standards-ipc-6018-identity`
  - `methods-high-frequency-printed-board-scope-ipc-6018`

### 2. IPC-4103 standard landing page

- URL: `https://shop.electronics.org/ipc-4103/ipc-4103-standard-only`
- Companion URL: `https://www.ipc.org/TOC/IPC-4103B.pdf`
- Owner: IPC / electronics.org
- Source type: official standard landing page plus public TOC PDF
- Supported claims:
  - `IPC-4103` covers base materials for high-speed / high-frequency applications.
  - Scope explicitly includes materials used for printed boards for microstrip, stripline, and high-speed digital circuits.
  - The TOC version also provides a cautious family-level clue that these laminates usually have low loss context, but that remains standard-scoped rather than universal board-performance proof.
- Strongest upgrade use:
  - strongest official bridge between RF laminate language and high-speed digital laminate language
  - helpful for `high-frequency-pcb-materials.md`, `high-frequency-pcb-layer-stackup.md`, and `what-is-hf-pcb.md`
- Limits / non-claims:
  - not proof that a laminate is best for a given protocol, antenna, or radar design
  - not proof that a board shop stocks or qualifies a given material
  - not a license to reuse exact material values without exact product datasheets
- Candidate source ID: `src_ipc_4103_scope_landing`
- Candidate fact IDs:
  - `standards-ipc-4103-identity`
  - `methods-high-speed-high-frequency-material-scope-ipc-4103`

### 3. IPC validation services QPL page for IPC-4103

- URL: `https://www.ipc.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103`
- Owner: IPC
- Source type: official IPC validation services page
- Supported claims:
  - `IPC-4103` has a qualified-products-list program.
  - IPC treats `IPC-4103` as a material-qualification framework tied to listed products and manufacturing sites.
- Strongest upgrade use:
  - useful for blocking vague supplier-selection copy that implies generic `IPC-4103` mentions equal universal supplier proof
  - supports more rigorous wording in `choosing-high-frequency-pcb-manufacturer.md`: ask for exact material qualification status, not just broad standards name-dropping
- Limits / non-claims:
  - not proof that any supplier in the draft family is qualified
  - not proof that material qualification alone validates finished-board RF or SI outcomes
- Candidate source ID: `src_ipc_4103_qpl_page`
- Candidate fact IDs:
  - `standards-ipc-4103-qpl-exists`
  - `methods-material-qualification-vs-finished-board-proof-boundary`

### 4. Keysight system impedance help page

- URL: `https://helpfiles.keysight.com/csg/N52xxB/System/System_Impedance.htm`
- Owner: Keysight Technologies
- Source type: official product help / instrument documentation
- Supported claims:
  - VNA default system impedance is `50 ohms`.
  - The analyzer can mathematically transform and display data for other system impedances, while physical test ports remain about `50 ohms`.
  - `75 ohm` and waveguide cases require explicit calibration / matching context.
- Strongest upgrade use:
  - best incremental anchor for explaining why `50 ohm` is a measurement-system reference context rather than a universal PCB law
  - supports conservative rewrites of `50-ohm-impedance-pcb.md`, `characteristic-impedance-pcb.md`, and `high-frequency-pcb-impedance-control.md`
- Limits / non-claims:
  - does not explain the historical industry reason for `50 ohms`
  - not proof that any PCB trace should be `50 ohms`
  - not proof of board-level optimality for any application
- Candidate source ID: `src_keysight_system_impedance_help`
- Candidate fact IDs:
  - `methods-vna-system-impedance-default-50ohm`
  - `methods-50ohm-measurement-reference-vs-physical-port-boundary`

### 5. Keysight PLTS system impedance help page

- URL: `https://helpfiles.keysight.com/csg/N1930xB/ToolsAndUtilities/System_Impedance.htm`
- Owner: Keysight Technologies
- Source type: official product help / software documentation
- Supported claims:
  - the system-impedance setting applies to data measured with both network-analyzer systems and `TDR`
  - changing the setting changes the mathematical display framing rather than the physical port hardware
- Strongest upgrade use:
  - useful bridge between `VNA` and `TDR` vocabulary in `tdr-testing-pcb.md` and `high-frequency-pcb-testing-methods.md`
  - reinforces that impedance context is measurement-reference-sensitive
- Limits / non-claims:
  - not proof that any PCB target impedance is right or wrong
  - not a pass/fail threshold source
- Candidate source ID: `src_keysight_plts_system_impedance_help`
- Candidate fact IDs:
  - `methods-system-impedance-applies-to-vna-and-tdr`

### 6. Keysight E5055A measurement parameters help

- URL: `https://helpfiles.keysight.com/csg/e5055a/S1_Settings/Measurement_Parameters.htm`
- Owner: Keysight Technologies
- Source type: official product help / instrument documentation
- Supported claims:
  - for a two-port device, the analyzer can measure all four `S-parameters`
  - reflection measurements map to `S11` and `S22`
  - transmission measurements map to `S21` and `S12`
  - return loss, SWR, reflection coefficient, impedance, insertion loss, and group delay belong to these measurement families
- Strongest upgrade use:
  - stronger official anchor than draft prose for `high-frequency-pcb-testing-methods.md`, `high-frequency-pcb-signal-integrity.md`, and `high-frequency-pcb-antenna-design.md`
  - especially useful where the drafts mix `S11`, `return loss`, and `insertion loss` too casually
- Limits / non-claims:
  - not proof that one `S-parameter` result validates full board, cable, connector, or antenna performance
  - not a standards acceptance source
- Candidate source ID: `src_keysight_measurement_parameters_help`
- Candidate fact IDs:
  - `methods-sparameter-measurement-family-keysight`
  - `methods-s11-s22-s21-s12-measurement-mapping`

### 7. Keysight power-integrity analysis page

- URL: `https://www.keysight.com/us/en/solutions/perform-power-integrity-analysis.html`
- Owner: Keysight Technologies
- Source type: official instrument-vendor solution page
- Supported claims:
  - power-integrity analysis includes `PDN impedance`, power-rail integrity, sequencing, `PSRR`, and control-loop response
  - a well-designed `PDN` aims to maintain stable voltage from DC to the bandwidth of the switching current
  - the page ties PDN quality to switching noise, jitter, and EMI concerns
- Strongest upgrade use:
  - best incremental source for the vocabulary sections of `high-frequency-pcb-power-design.md` and the `power integrity` subsection inside `high-frequency-pcb-signal-integrity.md`
  - lets the rewrite define `PDN` and power-integrity scope without inventing numeric targets
- Limits / non-claims:
  - not a design-rule source for capacitor values, plane dimensions, or target-impedance numbers
  - not proof that a given layout achieves low noise or low jitter
- Candidate source ID: `src_keysight_power_integrity_analysis`
- Candidate fact IDs:
  - `methods-pdn-power-integrity-vocabulary-keysight`
  - `methods-pdn-noise-jitter-emi-linkage`

### 8. Rohde & Schwarz TS8991 OTA performance test system page

- URL: `https://www.rohde-schwarz.com/us/products/test-and-measurement/conformance-test-systems-3gpp-ctia/rs-ts8991-ota-performance-test-system_63493-8444.html`
- Owner: Rohde & Schwarz
- Source type: official OTA system page
- Supported claims:
  - OTA testing can be tied to `3GPP`, `CTIA`, and Wi-Fi Alliance style conformance environments
  - OTA performance systems combine instruments, software, chamber infrastructure, and positioners
  - passive antenna measurements can involve near-field to far-field transformation
- Strongest upgrade use:
  - best source here for drawing a boundary between PCB-level antenna design claims and full OTA chamber / certification workflows
  - helps neutralize overreach in `high-frequency-pcb-antenna-design.md` and `high-frequency-pcb-testing-methods.md`
- Limits / non-claims:
  - product page, not a free standards text
  - not proof that a PCB manufacturer has OTA capability
  - not proof of any antenna gain, efficiency, TRP/TIS, or pass result
- Candidate source ID: `src_rs_ts8991_ota_system`
- Candidate fact IDs:
  - `methods-ota-test-system-boundary-rs`
  - `methods-passive-antenna-measurement-near-to-far-field-context`

### 9. Rohde & Schwarz DST200 RF diagnostic chamber page

- URL: `https://www.rohde-schwarz.com/us/product/dst200-productstartpage_63493-11087.html`
- Owner: Rohde & Schwarz
- Source type: official RF chamber product page
- Supported claims:
  - an anechoic RF chamber is part of radiated wireless-device testing infrastructure
  - OTA measurement setups can include shielding and automated positioners
  - such chambers are positioned as development-phase tools, not just final certification fixtures
- Strongest upgrade use:
  - useful neutral boundary source for `anechoic chamber` vocabulary in `high-frequency-pcb-antenna-design.md`
  - supports rewriting chamber discussion as environment / tooling context rather than proof of antenna performance
- Limits / non-claims:
  - not a universal statement about all OTA chambers
  - not a measurement method standard
  - not proof of supplier capability
- Candidate source ID: `src_rs_dst200_rf_chamber`
- Candidate fact IDs:
  - `methods-anechoic-rf-chamber-development-context`

### 10. Samtec high-speed cable / connector pages with `100 ohm` and `50 ohm` routing language

- URLs:
  - `https://www.samtec.com/high-speed-cable/micro-coax-twinax/edge-rate-cable/`
  - `https://www.samtec.com/high-speed-cable/micro-coax-twinax/qrate-cable/`
- Owner: Samtec
- Source type: official product-family pages
- Supported claims:
  - high-speed interconnect ecosystems commonly expose both `50 ohm single-ended` and `100 ohm differential pair` routing language
  - `100 ohm differential` is a normal product-context value for twinax / differential-pair ecosystems
- Strongest upgrade use:
  - modest but useful primary-source anchor that `100 ohm differential` is a common interconnect context, not a draft invention
  - supports cautious framing in `100-ohm-impedance-pcb.md` and `differential-impedance-pcb.md`
- Limits / non-claims:
  - product-family marketing pages, not standards documents
  - not proof that `100 ohm` is mandatory for every differential interface
  - not a source for PCB geometry, tolerance, or compliance claims
- Candidate source ID: `src_samtec_100ohm_50ohm_interconnect_context`
- Candidate fact IDs:
  - `methods-100ohm-differential-common-interconnect-context`

### 11. Analog Devices mixed-signal PCB layout article

- URL: `https://www.analog.com/en/resources/analog-dialogue/articles/2022/09/02/02/40/what-are-the-basic-guidelines-for-layout-design-of-mixed-signal-pcbs.html`
- Owner: Analog Devices
- Source type: official engineering article
- Supported claims:
  - power supply routing should be short and direct
  - decoupling and low-impedance return structure are part of supply-integrity control
  - `PSRR` and high-frequency energy management matter to signal performance
- Strongest upgrade use:
  - supplemental vocabulary anchor for `high-frequency-pcb-power-design.md` where the draft currently overpromises PDN outcomes
  - good secondary cross-check for the Keysight PDN language
- Limits / non-claims:
  - device-vendor guidance, not a board-fabrication standard
  - not proof of exact capacitor placement or universal layout formulas
- Candidate source ID: `src_adi_mixed_signal_layout_guidelines`
- Candidate fact IDs:
  - `methods-decoupling-low-impedance-return-guidance-adi`

## Strongest upgrade candidates after P4-36

### 1. Tighten high-frequency-board scope with `IPC-6018`

Best target drafts:

- `what-is-hf-pcb.md`
- `hf-pcb.md`
- `high-frequency-pcb-manufacturing.md`
- `high-frequency-pcb-testing-methods.md`

Why this is strong:

- The current drafts blur material family, board type, and finished-board qualification.
- `IPC-6018` is the cleanest official anchor that high-frequency boards are a defined printed-board specification family with multiple construction types and procurement-dependent requirements.

### 2. Tighten high-speed/high-frequency material language with `IPC-4103`

Best target drafts:

- `high-frequency-pcb-materials.md`
- `high-frequency-pcb-layer-stackup.md`
- `what-is-hf-pcb.md`

Why this is strong:

- The drafts currently drift between RF laminates and high-speed digital laminates without a standards bridge.
- `IPC-4103` is the strongest official standards-adjacent bridge for microstrip, stripline, and high-speed digital material framing.

### 3. Reframe `50 ohm` as reference context, not universal design truth

Best target drafts:

- `50-ohm-impedance-pcb.md`
- `characteristic-impedance-pcb.md`
- `high-frequency-pcb-impedance-control.md`

Why this is strong:

- The drafts currently market `50 ohm` as a near-universal optimum.
- Keysight system-impedance documentation supports a more defensible explanation: `50 ohm` is a dominant measurement-system reference and interconnect context, but not a universal board rule.

### 4. Reframe `100 ohm differential` as common ecosystem context, not blanket requirement

Best target drafts:

- `100-ohm-impedance-pcb.md`
- `differential-impedance-pcb.md`

Why this is strong:

- The drafts overstate `100 ohm` as if it always applies to high-speed differential design.
- Samtec product-family pages are enough to support `100 ohm differential` as a common interconnect context, while still blocking universal interface claims.

### 5. Upgrade OTA / chamber sections from performance claims to workflow boundaries

Best target drafts:

- `high-frequency-pcb-antenna-design.md`
- `high-frequency-pcb-testing-methods.md`

Why this is strong:

- These drafts currently drift toward chamber capability, antenna gain, and OTA-result implications.
- Rohde & Schwarz OTA system pages give a safe primary-source basis for stating what OTA environments include, what they are used for, and where chamber-based testing sits relative to board-level design.

### 6. Upgrade PDN / power-integrity language from vague promise to accepted vocabulary

Best target drafts:

- `high-frequency-pcb-power-design.md`
- `high-frequency-pcb-signal-integrity.md`

Why this is strong:

- These drafts contain high-risk noise-suppression and thermal-resistance claims that should stay blocked.
- Keysight and Analog Devices give enough primary-source support for conservative `PDN`, `PSRR`, decoupling, power-rail-noise, jitter, and EMI vocabulary without numeric promises.

## Claim families still blocked after this pass

These remain blocked because this pass found no acceptable official source for general reuse, or the draft claims are supplier-specific and need internal audited records.

### Impedance numerics and geometry

- universal `50 ohm` or `100 ohm` geometry tables
- exact trace width / spacing / dielectric thickness defaults
- universal impedance tolerance claims such as `±5%`, `±10%`, or `±3 ohm`
- formulas or stackup rules lifted from paid IPC documents

### Antenna and OTA performance

- antenna gain, efficiency, bandwidth, radiation-pattern, TRP, TIS, or range claims
- chamber-derived pass/fail claims
- claims that PCB antenna design alone guarantees OTA outcomes

### SI / PI / PDN outcomes

- exact jitter reduction, eye-opening, crosstalk suppression, or insertion-loss improvement claims
- target-impedance numbers, capacitor values, placement distances, or thermal-resistance calculations presented as universal rules
- tool-correlation claims like `simulation predicts production performance` without a narrow source and exact conditions

### Supplier-selection and capability claims

- HILPCB or any supplier claims for:
  - certifications
  - yield / quality rate
  - impedance tolerance
  - OTA, chamber, VNA, or TDR capability depth
  - lead time, MOQ, stock, sourcing strength, or cost optimization
  - aerospace, medical, telecom, radar, or defense readiness

### Application-readiness claims

- `5G`, `mmWave`, `automotive radar`, `satellite`, `DDR`, `USB`, or similar protocol / sector claims presented as ready-made finished-board capability proof

## Supplier-selection blockers clarified by official sources

For `choosing-high-frequency-pcb-manufacturer.md`, the strongest official-source-backed selection blockers now are:

- Ask whether the supplier can name the exact material family and whether it maps to an applicable base-material specification context such as `IPC-4103`; do not accept generic `high-frequency material` wording.
- Ask what high-frequency printed-board specification family the build is intended to satisfy; `IPC-6018` is the strongest public standards anchor found in this pass.
- Ask what measurement workflow is actually used: coupon, `TDR`, `VNA`, or broader OTA / chamber work. These are different layers, not interchangeable proof.
- Treat any `50 ohm` / `100 ohm` promise as context-dependent until tied to stackup, coupon strategy, and actual measurement method.
- Treat broad standards-name lists as weak evidence unless the supplier can map them to a specific product, board class, or qualification program.

## Residual gaps

- No neutral official source found in this pass that cleanly explains the historical industry choice of `50 ohms` for broad public reuse without sliding into secondary-source storytelling.
- No official source found here that justifies universal `100 ohm differential` language across all protocols; the Samtec pages only support common ecosystem context.
- No official source recovered here for generic antenna-layout keepout dimensions, feed geometry, or matching-network defaults.
- No official source recovered here for reusable OTA metrics or acceptance thresholds; chamber product pages help with workflow boundaries only.
- No official source recovered here for supplier-comparison claims such as best lead time, best stock posture, lowest loss, or highest yield.
- No official source recovered here for thermal-resistance formulas, capacitor-value ladders, or exact PDN target-impedance rules suitable for general blog reuse.

## Recommended next recovery order

1. Convert `IPC-6018` and `IPC-4103` into standards-boundary fact cards first.
2. Add the Keysight system-impedance and measurement-parameter pages as method cards for `50 ohm`, `S-parameter`, and `VNA/TDR` framing.
3. Add the Rohde & Schwarz OTA / chamber pages as antenna-test-boundary facts, not as performance facts.
4. Add the Keysight PDN page and, if desired, one conservative Analog Devices support fact for SI / PI vocabulary.
5. Keep supplier-selection language blocked unless internal audited capability records are intentionally supplied.

## Lane status

- Status: `completed_as_recovery_scout_only`
- This pass was intentionally incremental to P4-36, not a duplicate source list.
- No registries, facts, wiki pages, trackers, or unrelated files were modified.

## Output summary

- Changed file: `/code/blogs/llm_wiki/logs/p4-37-2025-8-12-rf-high-speed-official-source-recovery-scout.md`
- Official sources checked:
  - `IPC-6018`
  - `IPC-4103`
  - `IPC IPC-4103 QPL page`
  - `Keysight system impedance`
  - `Keysight PLTS system impedance`
  - `Keysight measurement parameters`
  - `Keysight power integrity analysis`
  - `Rohde & Schwarz TS8991 OTA system`
  - `Rohde & Schwarz DST200 RF chamber`
  - `Samtec 50 ohm / 100 ohm interconnect pages`
  - `Analog Devices mixed-signal PCB layout article`
- Strongest upgrade candidates:
  - `IPC-6018` for high-frequency-board scope
  - `IPC-4103` for material-scope bridge
  - Keysight system-impedance pages for `50 ohm` context
  - Samtec interconnect pages for cautious `100 ohm differential` context
  - Rohde & Schwarz OTA / chamber pages for antenna-test boundaries
  - Keysight PDN page for SI / PDN vocabulary
- Blocked claims:
  - unsupported numerics
  - supplier capability claims
  - antenna / OTA performance claims
  - universal SI / PI outcome claims
  - application-readiness and qualification overclaims
- Residual gaps:
  - no clean neutral `why 50 ohms` official explainer
  - no universal `100 ohm` protocol-proof source
  - no reusable OTA acceptance metrics
  - no supplier-proof sources for commercial or capability claims
