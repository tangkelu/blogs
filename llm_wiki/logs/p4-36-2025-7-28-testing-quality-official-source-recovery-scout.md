# P4-36 Official-Source Recovery Scout

- Lane: `P4-36 official-source recovery scout`
- Scope: `/code/blogs/tmps/2025.7.28/en` testing / quality / reliability drafts
- Output-only lane: no registry, fact, wiki, or tracker edits performed
- Model requested by user: `gpt-5.4`
- Date: `2026-04-28`

## Boundary

The `tmps/` drafts were treated as claim inventory only, not authority.

The required bootstrap command from `AGENTS.md` was not available at:

- `/root/.codex/superpowers/.codex/superpowers-codex`

So this scout proceeded with direct inventory plus official-source recovery.

## Drafts Covered

- `burn-in-testing.md`
- `thermal-shock-testing.md`
- `impedance-testing.md`
- `pcb-vibration-testing.md`
- `flying-probe-testing.md`
- `pcb-functional-testing.md`
- `pcb-electrical-testing.md`
- `thermal-cycling-testing.md`
- `ict-testing.md`
- `pcb-solderability-testing.md`

## High-Value Claim Families Needing Real Data

- Burn-in: what it is, what standards govern it, whether PCB/PCBA-level burn-in claims are actually semiconductor/package-level claims, and whether duration/temperature defaults are standard or vendor-specific.
- Flying probe: what it can legitimately detect, how it differs from ICT, and what test-access / throughput / coverage claims are standard vs vendor marketing.
- ICT: structural/component-level defect coverage, boundary-scan relationship, fixture-based constraints, and whether cited precision figures are supportable.
- Impedance test: TDR as the primary method, what IPC officially covers, and whether claims about ±1% or sub-50 ps are standard-neutral or instrument-specific.
- Electrical test: bare-board electrical test requirements, continuity/isolation framing, and where assembly-level electrical test claims stop.
- Functional test: hard split between system-behavior validation and structural/component tests; standards coverage is weak compared with vendor-source coverage.
- Solderability: dip-and-look, wetting-balance, spread/steam-aging support, and whether surface-finish shelf-life / contact-angle / coverage thresholds are standard-backed.
- Thermal cycling / thermal shock: rate definitions, cycle/severity framing, and board-level vs component-level standard boundaries.
- Vibration / shock: IEC generic environmental test metadata vs IPC rigid-board-specific test methods; avoid laundering sector-specific G-levels without primary source.
- Reliability / quality gates: traceability, lot acceptance, qualification, and screening are often real but application-specific; many draft numbers are not primary-backed.

## Recovered Official-Source Candidates

### 1. Bare-board electrical testing requirements

- URL: `https://www.ipc.org/TOC/IPC-9252B.pdf`
- Owner: `IPC`
- Source type: `official standard PDF`
- Supported claims:
  - IPC has a dedicated standard for electrical testing of unpopulated printed boards.
  - The document is `IPC-9252B`.
  - Scope is bare/unpopulated boards, not assembled PCBA functional behavior.
- Limits / non-claims:
  - Does not support assembly-level functional, ICT, or burn-in claims.
  - Does not justify draft ROI claims like “85-95% field-failure reduction.”
- Candidate source_id: `src_ipc_9252b_electrical_test_unpopulated_boards`
- Candidate fact_id: `fact_ipc_9252b_exists_for_unpopulated_board_electrical_test`

### 2. IPC test-method index for approved board/environment/electrical methods

- URL: `https://www.ipc.org/test-methods`
- Owner: `IPC`
- Source type: `official methods index`
- Supported claims:
  - IPC publishes current approved TM-650 methods relevant to testing/reliability.
  - Confirms the existence of methods such as `2.5.5.7A`, `2.5.5.14`, `2.6.7.2C`, `2.6.8E`, `2.6.9B`, `2.6.5D`, `2.6.23`.
- Limits / non-claims:
  - Index page alone does not validate method details beyond existence/current listing.
- Candidate source_id: `src_ipc_tm650_index_test_methods`
- Candidate fact_id: `fact_ipc_tm650_index_lists_relevant_test_methods`

### 3. IPC TDR method for characteristic impedance

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2-5-5-7a.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.5.5.7A` covers characteristic impedance of lines on printed boards by TDR.
  - TDR is an IPC-supported method for measuring and calculating characteristic impedance of PCB transmission lines.
  - Method notes measurement limitations and uncertainty sources.
- Limits / non-claims:
  - Does not support the draft’s instrument-performance numbers like sub-50 ps rise time, ±1% accuracy, or 40 GHz VNA claims.
  - Does not support generic “production systems always achieve X repeatability” statements.
- Candidate source_id: `src_ipc_tm650_2_5_5_7a_tdr_impedance`
- Candidate fact_id: `fact_ipc_tm650_2_5_5_7a_supports_tdr_impedance_measurement`

### 4. IPC frequency-domain high-frequency loss/propagation method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/TM%202.5.5.14.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.5.5.14` covers frequency-domain measurement of signal loss and propagation on printed boards.
  - VNA-based characterization and de-embedding are official IPC method territory for high-speed boards.
- Limits / non-claims:
  - Does not validate brand-specific fixture, GHz-range, or accuracy marketing from the drafts.
- Candidate source_id: `src_ipc_tm650_2_5_5_14_freq_domain_loss`
- Candidate fact_id: `fact_ipc_tm650_2_5_5_14_supports_freq_domain_signal_loss_methods`

### 5. IPC TDR propagation-delay method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2-5_2-5-5-11.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.5.5.11` covers propagation delay of lines on printed boards by TDR.
  - Useful for controlled-impedance / signal-integrity topic recovery.
- Limits / non-claims:
  - Not a direct source for assembled-board functional validation claims.
- Candidate source_id: `src_ipc_tm650_2_5_5_11_tdr_propagation_delay`
- Candidate fact_id: `fact_ipc_tm650_2_5_5_11_supports_tdr_delay_measurement`

### 6. IPC thermal shock / thermal cycle / continuity for unpopulated boards

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.6.7.2c.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.6.7.2C` exists for unpopulated-board thermal shock, thermal cycle, and continuity.
  - It distinguishes thermal shock from thermal cycle by rate.
  - Method is intended to evaluate interconnect quality and can be used for qualification, conformance, or lot acceptance.
- Limits / non-claims:
  - Scope is unpopulated test specimens, not finished assembled products in general.
  - Does not support draft cycle-count defaults for specific industries.
  - Does not support large application-market claims without additional sources.
- Candidate source_id: `src_ipc_tm650_2_6_7_2c_thermal_shock_cycle_continuity`
- Candidate fact_id: `fact_ipc_tm650_2_6_7_2c_defines_board_thermal_shock_vs_cycle`

### 7. IEC change-of-temperature standard

- URL: `https://webstore.iec.ch/en/publication/71503`
- Owner: `IEC`
- Source type: `official standards metadata`
- Supported claims:
  - `IEC 60068-2-14:2023` exists.
  - It covers change-of-temperature tests.
  - It is current IEC metadata for this family.
- Limits / non-claims:
  - Metadata alone does not expose detailed severities or exact pass/fail values.
  - Supports standard existence/scope, not the draft’s specific chamber-rate or cycle-number claims.
- Candidate source_id: `src_iec_60068_2_14_2023_change_of_temperature`
- Candidate fact_id: `fact_iec_60068_2_14_is_change_of_temperature_standard`

### 8. IEC sinusoidal vibration standard

- URL: `https://webstore.iec.ch/en/publication/544`
- Owner: `IEC`
- Source type: `official standards metadata`
- Supported claims:
  - `IEC 60068-2-6:2007` exists.
  - It covers sinusoidal vibration testing.
  - Purpose includes determining mechanical weakness and/or degradation in specified performance.
- Limits / non-claims:
  - Does not justify the draft’s specific acceleration/frequency profiles for every sector.
- Candidate source_id: `src_iec_60068_2_6_2007_sinusoidal_vibration`
- Candidate fact_id: `fact_iec_60068_2_6_covers_sinusoidal_vibration`

### 9. IEC broadband random vibration standard

- URL: `https://webstore.iec.ch/en/publication/547`
- Owner: `IEC`
- Source type: `official standards metadata`
- Supported claims:
  - `IEC 60068-2-64:2008` exists.
  - It covers broadband random vibration.
  - It is applicable to transportation/operational environments and functional/structural integrity assessment.
- Limits / non-claims:
  - Metadata does not validate draft PSD values or application-specific duty cycles.
- Candidate source_id: `src_iec_60068_2_64_2008_random_vibration`
- Candidate fact_id: `fact_iec_60068_2_64_covers_random_vibration`

### 10. IEC shock standard

- URL: `https://webstore.iec.ch/publication/514`
- Owner: `IEC`
- Source type: `official standards metadata`
- Supported claims:
  - `IEC 60068-2-27:2008` exists.
  - It covers non-repetitive or repetitive shock.
  - Purpose includes revealing mechanical weakness / degradation from shocks.
- Limits / non-claims:
  - Not a source for handheld-component drop-test specifics; those belong elsewhere.
- Candidate source_id: `src_iec_60068_2_27_2008_shock`
- Candidate fact_id: `fact_iec_60068_2_27_covers_shock_testing`

### 11. IPC rigid printed wiring vibration method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.6.9b.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.6.9B` covers vibration testing for rigid printed wiring.
  - It includes example parameters and requires before/after interconnection resistance checks.
  - It explicitly says specific test conditions must be agreed by customer and vendor.
- Limits / non-claims:
  - Draft claims that imply universal vibration severities by industry should not be promoted without application-specific standards.
- Candidate source_id: `src_ipc_tm650_2_6_9b_vibration_rigid_printed_wiring`
- Candidate fact_id: `fact_ipc_tm650_2_6_9b_exists_for_rigid_board_vibration`

### 12. IPC physical shock method

- URL: `https://www.ipc.org/test-methods`
- Owner: `IPC`
- Source type: `official methods index`
- Supported claims:
  - IPC lists TM-650 `2.6.5D` for physical shock, multilayer printed wiring.
- Limits / non-claims:
  - In this pass, only index-level confirmation was recovered, not the full method PDF.
- Candidate source_id: `src_ipc_tm650_index_physical_shock_multilayer`
- Candidate fact_id: `fact_ipc_tm650_2_6_5d_exists_for_multilayer_physical_shock`

### 13. IPC plated-through-hole thermal stress method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.6.8e.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.6.8E` exists for plated-through-hole thermal stress.
  - It supports PTH/via reliability discussion for board quality gates.
- Limits / non-claims:
  - Not a general source for complete assembled-PCBA thermal-cycling narratives.
- Candidate source_id: `src_ipc_tm650_2_6_8e_pth_thermal_stress`
- Candidate fact_id: `fact_ipc_tm650_2_6_8e_exists_for_pth_thermal_stress`

### 14. IPC solderability of metallic surfaces

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.4.14.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.4.14` exists for solderability of metallic surfaces.
  - It is a direct primary source for dip-style solderability evaluation of PCB metallic surfaces.
- Limits / non-claims:
  - Old method; do not overstate modern lead-free acceptability details from this alone.
  - Does not support draft shelf-life claims by finish.
- Candidate source_id: `src_ipc_tm650_2_4_14_solderability_metallic_surfaces`
- Candidate fact_id: `fact_ipc_tm650_2_4_14_exists_for_surface_solderability`

### 15. IPC wetting-balance method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.4.14.2a.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.4.14.2A` covers wetting-balance method.
  - Wetting-balance testing is a legitimate primary-source-backed method family.
- Limits / non-claims:
  - This specific method is for liquid flux activity, not a blanket proof of every PCB finish claim in the draft.
  - Does not support the draft’s exact mN-resolution claim as a universal requirement.
- Candidate source_id: `src_ipc_tm650_2_4_14_2a_wetting_balance`
- Candidate fact_id: `fact_ipc_tm650_2_4_14_2a_supports_wetting_balance_method`

### 16. IPC spread test

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.4.46a.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.4.46A` exists for spread testing.
  - Spread area measurement is an official IPC-supported method family.
- Limits / non-claims:
  - Not enough by itself to support broad claims about contact-angle thresholds or shelf life.
- Candidate source_id: `src_ipc_tm650_2_4_46a_spread_test`
- Candidate fact_id: `fact_ipc_tm650_2_4_46a_exists_for_spread_testing`

### 17. IPC steam ager repeatability method

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2.6.23.pdf`
- Owner: `IPC`
- Source type: `official test method PDF`
- Supported claims:
  - IPC TM-650 `2.6.23` exists for steam ager temperature repeatability.
  - Steam aging is in IPC’s official method stack for solderability-related setup control.
- Limits / non-claims:
  - This does not directly prove the draft’s default “93 ± 3°C for 8 hours” aging recipe unless backed by a more direct solderability standard.
- Candidate source_id: `src_ipc_tm650_2_6_23_steam_ager_repeatability`
- Candidate fact_id: `fact_ipc_tm650_2_6_23_exists_for_steam_ager_repeatability`

### 18. IEEE boundary-scan architecture

- URL: `https://standards.ieee.org/ieee/1149.1/4484/`
- Owner: `IEEE`
- Source type: `official standards metadata`
- Supported claims:
  - `IEEE 1149.1-2013` exists.
  - It defines test access port and boundary-scan architecture.
  - It supports claims about standardized interconnect/component test access on assembled PCBs.
- Limits / non-claims:
  - Does not support broad flying-probe or ICT coverage claims by itself.
- Candidate source_id: `src_ieee_1149_1_2013_boundary_scan`
- Candidate fact_id: `fact_ieee_1149_1_defines_boundary_scan_architecture`

### 19. Official flying-probe vendor page

- URL: `https://www.spea.com/en/products/4080-flying-probe-tester/`
- Owner: `SPEA`
- Source type: `official vendor product page`
- Supported claims:
  - Flying-probe systems exist as multi-probe automated electrical test platforms.
  - Official vendor positioning supports use on assembled boards, bare PCBs, flexible circuits, and large/complex boards.
  - Vendor claims include fine-feature probing and multi-domain test integration.
- Limits / non-claims:
  - Vendor marketing is not a neutral standard.
  - Do not promote “zero-failure escape,” “fastest in the world,” or micron-level performance as generic facts.
- Candidate source_id: `src_spea_4080_flying_probe_vendor`
- Candidate fact_id: `fact_spea_officially_positions_flying_probe_for_board_test`

### 20. Official board-test vendor page for ICT / repair / flying probe

- URL: `https://www.spea.com/en/electronic-board-test/`
- Owner: `SPEA`
- Source type: `official vendor solution page`
- Supported claims:
  - Vendors distinguish flying probe, repair test, and in-circuit test as separate board-test modalities.
  - ICT is positioned for component/process-defect detection.
- Limits / non-claims:
  - Still vendor framing, not standard-neutral test taxonomy.
- Candidate source_id: `src_spea_electronic_board_test_modalities`
- Candidate fact_id: `fact_spea_distinguishes_flying_probe_and_ict_modalities`

### 21. Official ICT vendor page

- URL: `https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing.html`
- Owner: `Keysight`
- Source type: `official vendor solution page`
- Supported claims:
  - ICT is used after assembly for structural/component verification.
  - Official vendor framing supports opens/shorts, wrong/missing/misoriented parts, solder defects, boundary scan integration, and dense-board use.
  - Functional testing is distinct from ICT.
- Limits / non-claims:
  - Vendor page is not a standard; quantitative defect-coverage claims remain unsupported.
- Candidate source_id: `src_keysight_ict_manufacturing_solution`
- Candidate fact_id: `fact_keysight_officially_distinguishes_ict_from_functional_test`

### 22. Official ICT vendor page from another vendor

- URL: `https://www.teradyne.com/teststation-ict-system/`
- Owner: `Teradyne`
- Source type: `official vendor product page`
- Supported claims:
  - ICT platforms are official production systems for complex, highly integrated boards.
  - Supports generic ICT lane recovery where a second official vendor is useful.
- Limits / non-claims:
  - Does not justify universal ICT measurement-precision numbers.
- Candidate source_id: `src_teradyne_teststation_ict`
- Candidate fact_id: `fact_teradyne_positions_teststation_as_ict_for_complex_boards`

### 23. Official burn-in vendor page

- URL: `https://www.aehr.com/solutions`
- Owner: `Aehr Test Systems`
- Source type: `official vendor solutions page`
- Supported claims:
  - Production burn-in and burn-in/test systems exist as a real equipment category.
  - Official page supports wafer-level/package-level burn-in, screening, and qualification contexts.
- Limits / non-claims:
  - This is semiconductor-device burn-in, not automatically PCB/PCBA burn-in.
  - Do not use it to justify board-level burn-in temperature/time defaults.
- Candidate source_id: `src_aehr_solutions_burn_in_test`
- Candidate fact_id: `fact_aehr_officially_positions_burn_in_as_semiconductor_test_category`

### 24. Official burn-in technology page

- URL: `https://www.aehr.com/technology/`
- Owner: `Aehr Test Systems`
- Source type: `official vendor technology page`
- Supported claims:
  - Official vendor states functional test capability can be combined during burn-in in semiconductor contexts.
- Limits / non-claims:
  - Not a source for PCB assembly burn-in guidance.
- Candidate source_id: `src_aehr_technology_burn_in_functional_capability`
- Candidate fact_id: `fact_aehr_vendor_page_claims_functional_test_during_burn_in`

## Top Upgrade Candidates

These are the highest-value source candidates for converting draft claims into reusable facts later.

1. `src_ipc_9252b_electrical_test_unpopulated_boards`
   Use for bare-board electrical-test pages and to tighten the distinction between unpopulated board test and assembled-board test.
2. `src_ipc_tm650_2_5_5_7a_tdr_impedance`
   Best primary source for controlled-impedance/TDR claims.
3. `src_ipc_tm650_2_6_7_2c_thermal_shock_cycle_continuity`
   Best source for board-level thermal-shock vs thermal-cycle distinction.
4. `src_ipc_tm650_2_6_9b_vibration_rigid_printed_wiring`
   Strongest direct IPC source for rigid-board vibration.
5. `src_ipc_tm650_2_4_14_solderability_metallic_surfaces`
   Best direct PCB metallic-surface solderability method source recovered in this pass.
6. `src_ieee_1149_1_2013_boundary_scan`
   Best neutral official source for boundary-scan claims used in ICT/flying-probe articles.
7. `src_keysight_ict_manufacturing_solution`
   Best vendor-primary source for the ICT vs functional-test distinction at PCBA level.
8. `src_iec_60068_2_14_2023_change_of_temperature`
   Best official metadata anchor for broader thermal-cycling / temperature-change claims.

## Blocked Claims

These draft claims should not be promoted without better primary support.

### Burn-in

- Standardized board-level burn-in defaults like `125°C to 150°C`, `24 to 168 hours`, or universal infant-mortality screening rules.
- Arrhenius acceleration-factor ranges like `10x to 1000x` presented as generic burn-in truth.
- Claims that JEDEC burn-in standards directly govern PCB assemblies rather than semiconductor devices.
- Any claim that “burn-in predicts real-world reliability” without a narrower context and better source.

### Flying probe / ICT / electrical test

- Precision numbers like `±0.5%`, `±0.1%`, `±25 µm`, `0.2 mm pitch`, or annual break-even unit-volume thresholds as universal facts.
- “100% net accessibility,” “zero-failure escape,” or similar vendor superlatives presented as neutral truth.
- Board-test coverage claims that imply all defects are caught, especially latent reliability defects.
- Generalized industry coverage statements for medical/aerospace/automotive without sector-specific standards.

### Functional test

- Most functional-test sections in the drafts are under-sourced from standards.
- Claims about `24-48 hour` rapid FCT turnaround, exact environmental chamber setups, or exact high-frequency validation stacks are capability/vendor claims, not official neutral facts.
- Broad lists of governing standards for FCT are weakly grounded; likely needs equipment-vendor primary sources plus application-specific standards.

### Solderability

- Specific shelf-life windows by finish (`12 months HASL`, `6 months OSP`, `24 months ENIG`) are not supported by recovered official primary sources here.
- `95% coverage`, `<30° contact angle`, `<1 second wetting time` as blanket accept criteria were not recovered from official pages in this pass.
- Gold-thickness “optimal” numbers and OSP “2-3 reflows / 5-6 reflows” claims are blocked pending stronger primary documentation.

### Thermal cycling / thermal shock / vibration

- Universal consumer/industrial/military cycle counts such as `10-100`, `500-1000+`, or `10,000 cycles`.
- Exact chamber ramp rates, temperature windows, and G-levels presented as standard defaults across all sectors.
- Claims that thermal shock is always `>30°C/min` and thermal cycling `<5°C/min` outside the narrower IPC board-method distinction recovered.

### Reliability / quality gates

- Field-failure reduction percentages.
- Universal ROI / cost-of-failure claims.
- Any claim implying ISO 9001 alone proves specific test capability.

## Residual Gaps

- Official JEDEC metadata for `JESD22-A108` burn-in / operating life was not cleanly recoverable from JEDEC-owned pages in this pass.
- Official JEDEC metadata for `JESD22-A104` thermal cycling was likewise not cleanly recoverable from JEDEC-owned pages, though the standard is clearly referenced in third-party mirrors. Because this lane required official-source recovery, I did not promote mirror content to accepted source status.
- IPC `J-STD-002` and `J-STD-003` official accessible pages were not cleanly recovered in this pass, leaving a gap for modern component/board solderability framing.
- Functional-test standards coverage remains thin relative to vendor-primary content.
- Application-specific standards named in drafts such as `AEC-Q100`, `MIL-STD-810`, `IEC 60601`, and telecom-specific requirements were not expanded here because the lane scope prioritized the listed testing families and only official-source candidates. They remain candidates for a second pass if those article families must retain sector-specific claims.

## Practical Recovery Guidance

- Safe to upgrade now:
  - bare-board electrical test framing
  - TDR/impedance method framing
  - board thermal shock vs thermal cycle distinction
  - rigid-board vibration method existence
  - boundary-scan standard existence
  - solderability method families: dip/solderability, wetting-balance, spread, steam-aging apparatus control

- Needs narrower wording before reuse:
  - ICT vs flying-probe coverage
  - functional-test descriptions
  - burn-in claims for PCB/PCBA articles
  - reliability-prediction and field-correlation claims

- Needs a second official-source pass:
  - JEDEC burn-in / operating-life metadata
  - JEDEC thermal-cycling metadata
  - IPC J-STD solderability pages
  - sector-specific qualification standards if those article lanes must keep automotive / aerospace / medical claims

## Changed File

- `/code/blogs/llm_wiki/logs/p4-36-2025-7-28-testing-quality-official-source-recovery-scout.md`
