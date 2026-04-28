# p4-35-2025-10-25 official-source recovery scout

Date: 2026-04-28
Model: gpt-5.4
Scope lane: official-source recovery scout for `HTCC`, `thin-film ceramic PCB`, `blind/buried via`, and `IC-substrate boundary` claims inventoried from `/code/blogs/tmps/2025.10.25/en`
Edit boundary honored: only this file created

## Scope and method

Tmp drafts were treated as claim inventory only, not authority. I searched for official sources that can support reusable definitional or technology-boundary claims from:

- standards bodies
- official manufacturer product / technology pages
- official government / space-agency standards where useful

I did not promote unsupported supplier capability, pricing, lead-time, MOQ, certification, yield, quality-rate, RF/thermal superiority, or production-parameter claims from drafts unless an official source directly supported them.

## Changed files

- `/code/blogs/llm_wiki/logs/p4-35-2025-10-25-official-source-recovery-scout.md`

## Official sources found

### 1) ECSS PCB design standard: blind via / buried via / HDI / microvia definitions

URL: https://ecss.nl/wp-content/uploads/2025/05/ECSS-Q-ST-70-12C-Rev.1%2830April2025%29.pdf
Source owner: ECSS / European Space Agency standards system

Supports:

- `blind via` = via exposed only on one side of the PCB
- `buried via` = via connecting internal layers without exposure on either surface
- `HDI` = PCB technology allowing smaller surface-footprint pitch and higher internal routing density than conventional PCBs
- `microvia` = blind via with diameter smaller than `250 µm`
- HDI/core-via design constraints exist in an official space PCB design standard

Exact limits / non-claims:

- Supports definitions and selected ECSS design-rule context, not generic commercial capability claims
- Does not support draft claims about universal aspect-ratio limits, yield, lead time, pricing, or any specific supplier capability
- Does not support the draft’s broad application marketing claims by itself
- Its numerical limits are ECSS design-standard values, not universal market-wide maxima/minima

Candidate fact IDs:

- `cand_fact_blind_via_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_buried_via_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_hdi_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_microvia_lt_250um_ecss_q_st_70_12c_rev1`
- `cand_fact_hdi_core_via_constraints_exist_ecss_q_st_70_12c_rev1`

### 2) MARUWA HTCC page

URL: https://www.maruwa-g.com/e/products/ceramic/000317.html
Source owner: MARUWA Co., Ltd.

Supports:

- official product category: `Alumina Multilayered Ceramic Substrates & Packages (HTCC)`
- multilayer ceramic structure with flexible routing and cavity structures
- official metallization stack examples for this product family:
  - metallized via: `W`
  - inner layer: `W`
  - surface layer: `W / Cu`
  - plating examples: `NiB`, `NiP-Au`, `NiP-Pd-Au`, `Ni-Au`
- official application examples: sensor packages, surface-mount packages, MEMS packages, optical communication packages, LED packages
- official property table for this specific alumina HTCC family, including CTE, thermal conductivity, dielectric constant, volume resistivity, breakdown strength

Exact limits / non-claims:

- Supports MARUWA’s specific HTCC product family, not all HTCC products industry-wide
- Does not support the draft’s claims about `>1600°C` firing temperature, inherent hermeticity, `500°C` continuous operation, `30+ layers`, or helium leak performance
- Does not support HILPCB-specific capability, certification, yield, or in-house process claims

Candidate fact IDs:

- `cand_fact_htcc_maruwa_alumina_multilayer_definition`
- `cand_fact_htcc_maruwa_w_via_and_inner_layers`
- `cand_fact_htcc_maruwa_surface_w_or_cu_and_plating_options`
- `cand_fact_htcc_maruwa_application_examples`
- `cand_fact_htcc_maruwa_property_table_alumina_92`

### 3) MARUWA AlN multilayer ceramic page

URL: https://www.maruwa-g.com/products/ceramic/000101.html
Source owner: MARUWA Co., Ltd.

Supports:

- official AlN multilayer ceramic substrate/package family
- AlN multilayer package positioned for high heat dissipation
- official stack examples similar to the HTCC family:
  - metallized via: `W`
  - inner layer: `W`
  - surface layer: `W / Cu`
- official property table including `CTE 4.6 ppm/°C`, `thermal conductivity 170 W/(m·K)`, dielectric constant, resistivity, breakdown strength

Exact limits / non-claims:

- Supports MARUWA’s own AlN multilayer family only
- Does not prove that all HTCC uses AlN, nor that all thin-film ceramic circuits use AlN
- Does not support the draft’s generalized thermal claims across all ceramic PCB constructions

Candidate fact IDs:

- `cand_fact_aln_multilayer_maruwa_high_heat_dissipation`
- `cand_fact_aln_multilayer_maruwa_w_metallization_stack`
- `cand_fact_aln_multilayer_maruwa_property_table`

### 4) AdTech Ceramics HTCC page

URL: https://www.adtechceramics.com/products/htcc
Source owner: AdTech Ceramics

Supports:

- HTCC is used for hermetic packaging
- HTCC page states desirable electrical properties, high mechanical strength, and good thermal conductivity
- official process-stage outline:
  - material preparation
  - green processing
  - sintering / co-firing in controlled atmosphere
  - post-fire processing
- green-process examples: cavity punch, via punch, via fill, screen print, lamination
- post-fire note that almost all packages are plated with `Ni` and `Au` for solder / wirebond applications
- official application sectors: military, aerospace, medical device, high-temperature applications

Exact limits / non-claims:

- Supports AdTech’s own HTCC process framing, not universal industry process limits
- Does not support the draft’s numeric claims for operating temperature, line/space, via diameter, layer count, leak rate, or thermal-cycle endurance
- Does not support HILPCB capability or certification claims

Candidate fact IDs:

- `cand_fact_htcc_adtech_process_stages`
- `cand_fact_htcc_adtech_hermetic_packaging_use`
- `cand_fact_htcc_adtech_ni_au_post_fire_plating`
- `cand_fact_htcc_adtech_application_sectors`

### 5) Kyocera thin-film circuit boards overview

URL: https://global.kyocera.com/prdct/semicon/about_ceramic_package/detail/thin_film.html
Source owner: KYOCERA

Supports:

- thin-film circuit boards are manufactured using vacuum deposition technology
- conductive and insulating layers are formed on a substrate surface
- listed substrate possibilities include ceramic, glass, metal, resin, and others
- thin-film circuit boards are generally used where high-precision circuitry is required
- Kyocera states ceramic thin-film boards often use solid single-layer ceramic substrates, and it also offers multilayer ceramic thin-film substrates
- process examples include vacuum deposition and sputtering

Exact limits / non-claims:

- Supports general thin-film technology description and Kyocera product framing
- Does not support draft numeric claims such as `1-10 µm` conductor thickness, sub-micron accuracy, or universal mmWave / radiation / medical suitability
- Does not support HILPCB-specific fabrication capability or quality claims

Candidate fact IDs:

- `cand_fact_thin_film_vacuum_deposition_kyocera`
- `cand_fact_thin_film_high_precision_use_kyocera`
- `cand_fact_thin_film_single_and_multilayer_ceramic_options_kyocera`
- `cand_fact_thin_film_process_examples_vacuum_deposition_and_sputtering_kyocera`

### 6) Kyocera thin-film technology page

URL: https://global.kyocera.com/prdct/semicon/technology_strengths/detail/thinfilm_technology.html
Source owner: KYOCERA

Supports:

- applying thin-film processing to ceramics can provide finer, higher-precision patterns than screen-printed thick-film technology in multilayer ceramic structures
- ceramic materials suitable for thin-film processing include `Al2O3`, `AlN`, and `Si3N4`
- official example film stacks include `Ti-Pt-Au`, `Ti-Pd-Au`, `Ti-Al`, `Ti-TiW-Cu-Ni-Au`, `Ti-TiW-Cu-Ni-Pd-Au`

Exact limits / non-claims:

- Supports relative precision comparison to thick-film, not exact minimum line/space values
- Does not support the draft’s exact performance figures, medical/aerospace qualification claims, or custom supplier capability claims

Candidate fact IDs:

- `cand_fact_thin_film_finer_than_thick_film_kyocera`
- `cand_fact_thin_film_ceramic_material_options_kyocera`
- `cand_fact_thin_film_example_metal_stacks_kyocera`

### 7) CoorsTek thin-film electronic substrates page

URL: https://www.coorstek.com/english/industries/electronics/microelectronics/thin-film-electronic-substrates/
Source owner: CoorsTek

Supports:

- official thin-film ceramic substrate product family
- four thin-film substrate material options with smooth surface finish, flexural strength, and consistent electrical properties
- alumina described as optimal for most thin-film ceramic substrate applications
- CoorsTek controls surface finish, grain size, and surface imperfections to improve fine-line resolution, spacing, and yields in thin-film processing
- official availability in as-fired, lapped, and polished configurations
- official alumina substrate thickness range on this page

Exact limits / non-claims:

- Supports substrate-side claims, not full assembled-circuit performance claims
- Does not support draft claims around mmWave insertion loss, radiation resistance, medical implant suitability, or exact conductor thicknesses
- Does not support generic all-industry yield or precision guarantees

Candidate fact IDs:

- `cand_fact_thin_film_substrate_family_coorstek`
- `cand_fact_alumina_optimal_for_many_thin_film_substrates_coorstek`
- `cand_fact_surface_finish_and_grain_control_affect_fine_line_results_coorstek`
- `cand_fact_thin_film_substrate_finish_options_coorstek`

### 8) Kyocera build-up FC-BGA package substrate page

URL: https://global.kyocera.com/prdct/organic/prdct/package/fcbga/std/
Source owner: KYOCERA

Supports:

- FC-BGA substrates are semiconductor packages, not ordinary board-level PCB marketing pages
- official package-substrate framing: fine design rule, high reliability, next-generation flip-chip LSI
- official specs on this page include:
  - more than `3,000 I/Os`
  - build-up line/space `9 µm / 12 µm`
  - via land diameter `85 µm`
  - core line width `30 µm`
  - core space `45 µm`
  - flip-chip pitch `100 µm`
- official mention of laser via technology and thermosetting epoxy

Exact limits / non-claims:

- Supports one Kyocera package-substrate family, not a universal threshold between all PCBs and all IC substrates
- Does not support the tmp draft’s blanket rule that feature size below `50 µm` always means IC substrate
- Does not support broad claims about 2.5D, fan-out, or all AI package architectures unless separately sourced

Candidate fact IDs:

- `cand_fact_package_substrate_semiconductor_package_kyocera_fcbga`
- `cand_fact_package_substrate_9_12um_linespace_kyocera_fcbga`
- `cand_fact_package_substrate_gt_3000_ios_kyocera_fcbga`
- `cand_fact_package_substrate_laser_vias_kyocera_fcbga`

### 9) Ajinomoto ABF page

URL: https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
Source owner: Ajinomoto Group

Supports:

- Ajinomoto Build-up Film (`ABF`) is an interlayer insulation material used in complex circuit substrates for high-performance CPUs
- ABF is used by semiconductor package substrate manufacturers
- page explicitly frames build-up substrates as the structure connecting nanoscale CPU circuits to millimeter-scale terminals on printed substrates
- ABF supports laser processing and direct copper plating for micrometer-scale circuits

Exact limits / non-claims:

- Supports package-substrate material context, not a formal standards definition of `IC substrate`
- Does not support the tmp draft’s universal line-width threshold, package-layer count, or all package-substrate market claims

Candidate fact IDs:

- `cand_fact_abf_interlayer_insulation_for_cpu_package_substrates_ajinomoto`
- `cand_fact_build_up_substrate_bridge_nanoscale_cpu_to_printed_substrate_terminals_ajinomoto`
- `cand_fact_abf_supports_laser_processing_and_direct_copper_plating_ajinomoto`

### 10) SHINKO package substrate pages

URLs:

- https://www.shinko.co.jp/english/product/ic-package/buildup/dll3.php
- https://www.shinko.co.jp/english/product/package/substrate/pbga.php
- https://www.shinko.co.jp/english/product/under-development/i-thop/

Source owner: SHINKO ELECTRIC INDUSTRIES CO., LTD.

Supports:

- package substrates are framed as semiconductor package products
- build-up package substrates use semi-additive process and stacked via structures
- high density is enabled by semi-additive processing and laser vias
- advanced package-substrate roadmap includes ultra-high-density organic substrate integrating interposer and build-up substrate, with thin-film technology in the interposer section

Exact limits / non-claims:

- Supports package-substrate technology direction and official product framing
- Does not support a clean universal PCB / IC-substrate cutoff threshold
- Does not support tmp-draft feature-size numbers unless those numbers appear on the specific source page

Candidate fact IDs:

- `cand_fact_shinko_build_up_package_substrate_sap_and_stacked_vias`
- `cand_fact_shinko_high_density_package_substrates_use_laser_vias`
- `cand_fact_shinko_ultra_high_density_package_substrate_integrates_interposer_and_build_up`

## Candidate fact set worth upgrading later

High-confidence upgrade candidates from this scout:

- `cand_fact_blind_via_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_buried_via_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_hdi_definition_ecss_q_st_70_12c_rev1`
- `cand_fact_microvia_lt_250um_ecss_q_st_70_12c_rev1`
- `cand_fact_htcc_maruwa_w_via_and_inner_layers`
- `cand_fact_htcc_maruwa_surface_w_or_cu_and_plating_options`
- `cand_fact_htcc_adtech_process_stages`
- `cand_fact_thin_film_vacuum_deposition_kyocera`
- `cand_fact_thin_film_finer_than_thick_film_kyocera`
- `cand_fact_thin_film_ceramic_material_options_kyocera`
- `cand_fact_package_substrate_semiconductor_package_kyocera_fcbga`
- `cand_fact_package_substrate_9_12um_linespace_kyocera_fcbga`
- `cand_fact_abf_interlayer_insulation_for_cpu_package_substrates_ajinomoto`

## Blocked claims from the tmp drafts

### HTCC blocked claims

Blocked pending better official evidence:

- firing temperature claims such as `over 1,600°C`
- continuous operating temperature claims such as `up to 500°C`
- inherent hermeticity claims stated as universal fact across all HTCC constructions
- helium leak numbers
- dielectric-strength numbers not tied to a specific official HTCC product table
- `30+ layer` claims
- HILPCB-specific line/space, via, thickness, alignment, yield, SPC, in-house process, and certification claims
- HILPCB application proof in aerospace / medical / automotive

### Thin-film ceramic PCB blocked claims

Blocked pending better official evidence:

- universal conductor-thickness claims such as `1 to 10 µm`
- sub-micron or `≤10 µm` routing claims unless tied to a specific official capability page
- broad claims about mmWave insertion-loss superiority, radiation resistance, vacuum compatibility, optical precision, implant suitability
- HILPCB-specific line/space, via, alignment, and certification claims
- performance tables for alumina / AlN / quartz / sapphire unless backed by official material datasheets from the exact source owner

### Blind / buried via blocked claims

Blocked pending better official evidence:

- broad manufacturing capability claims such as `10-30 layers`, `20-60 layers`, or specific aspect-ratio ceilings from the draft
- laser depth-control tolerances, plating-wall thickness, cycling counts, IPC class claims, and automotive-grade validation claims tied to HILPCB
- assertions that buried vias inherently improve EMI, thermal performance, or reliability without design-specific context
- any HILPCB timeline, prototype lead-time, annual output, or mass-production claims

### IC-substrate boundary blocked claims

Blocked pending better official evidence:

- universal boundary statements like `below 50 µm means IC substrate`
- broad claims that IC substrate technology always means `10+ buildup layers per side`
- unsupported claims about `2.5D and fan-out packaging services` by the draft supplier
- any claim that modified polyimide / epoxy systems or ABF-based substrates are equivalent to ordinary HDI PCBs

## Residual gaps

Still missing if later upgrade work is required:

- a standards-body or official glossary source that defines `IC substrate` directly, not just package-substrate product pages
- official HTCC source with explicit firing-temperature statement, if that claim is needed
- official thin-film source with explicit line/space capability numbers, if numeric precision claims are needed
- official, source-owner-specific qualification or reliability data for ceramic thin-film or HTCC, if application claims must be hardened
- supplier-official evidence for any HILPCB-specific capability or certification claims; none was promoted here

## Bottom line

Recovered official-source support is strongest for:

- definitions of blind via / buried via / HDI / microvia
- HTCC structural / metallization basics
- thin-film ceramic process framing and materials
- package-substrate versus PCB boundary directionally, through official semiconductor package-substrate pages

Recovered official-source support is weak or absent for:

- the drafts' commercial supplier claims
- most numeric capability claims
- universal performance claims
- universal PCB-to-IC-substrate cutoff thresholds
