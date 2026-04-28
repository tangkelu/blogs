# P4-37 2025.7.23 Specialty Materials Official-Source Recovery Scout

Date: 2026-04-28
Model: `gpt-5.4`
Input root: `/code/blogs/tmps/2025.7.23/en`
Prior map checked: `/code/blogs/llm_wiki/logs/p4-34-2025-7-23-specialty-materials-and-structures-blog-ingestion-map.md`
Output-only boundary honored: this file only

## Scope and method

This lane treated the `tmps/` drafts as claim inventory only, not authority.

Focus was limited to official-source candidates and strongest fact-upgrade opportunities not already covered for:

- IPC finish standards / official TOCs for `ENIG`, `ENEPIG`, `immersion silver`, `OSP`, `HASL`
- official anchors for copper foil `RA` / `ED` distinctions and roughness framing
- peelable mask
- insulation testing
- waterproof / coating / potting boundaries
- LTCC official class sources
- ceramic / alumina / `AlN` support gaps

The bootstrap path required by `AGENTS.md` was not present in this workspace:

- `/root/.codex/superpowers/.codex/superpowers-codex`

So this scout proceeded with direct inventory plus official-source recovery.

## Changed files

- `/code/blogs/llm_wiki/logs/p4-37-2025-7-23-specialty-materials-official-source-recovery-scout.md`

## Lane status

- Lane status: `official_source_candidates_recovered_partial`
- Best upgrade shape: `strong for standards metadata and class-definition anchors`
- Still weak: `product-specific numerics`, `supplier capability claims`, `waterproof finished-assembly claims`, `peelable-mask process-rule claims`

## Official sources checked

### 1) IPC-4552B TOC for ENIG

- URL: `https://www.ipc.org/TOC/IPC-4552B-toc.pdf`
- Source owner: `IPC`
- Supports:
  - official ENIG standard identity: `IPC-4552B`
  - ENIG is a defined IPC surface-finish family, not just marketing vocabulary
  - TOC confirms sections for `performance functions`, `limitations of ENIG`, `finish thickness`, `nickel corrosion`, `porosity`, `solderability`, `wire bonding`
- Best use:
  - upgrade generic ENIG definitional framing
  - anchor claims that ENIG has official IPC thickness / corrosion / solderability requirements
- Non-claims:
  - do not promote draft bath chemistry, shelf life, black-pad prevention guarantees, universal RF superiority, or supplier capability from this TOC alone

### 2) IPC-4556 TOC for ENEPIG

- URL: `https://www.ipc.org/TOC/IPC-4556.pdf`
- Source owner: `IPC`
- Supports:
  - official ENEPIG standard identity: `IPC-4556`
  - TOC explicitly includes `wire bonding`, `contact surface`, `connectors`, `press-fit applications`, `limitations of ENEPIG`, `high frequency signal loss`, and separate `nickel`, `palladium`, `gold` thickness sections
- Strongest upgrade candidate:
  - replace draft misuse of `IPC-4552` for ENEPIG with the correct official anchor `IPC-4556`
  - safely support that ENEPIG is a tri-metal IPC finish family intended for more than plain solderability alone
- Non-claims:
  - do not promote draft numeric thickness targets or fine-pitch suitability numbers without the full standard or another primary source

### 3) IPC revision table for finish-family coverage

- URL: `https://www.ipc.org/ipc-document-revision-table`
- Source owner: `IPC`
- Supports:
  - `IPC-4552` = ENIG
  - `IPC-4553` = immersion silver
  - `IPC-4555` = high-temperature OSP
  - `IPC-4556` = ENEPIG
  - `IPC-4553` is marked `No Longer Maintained`
  - no dedicated `IPC-4554` for HASL in this family because `IPC-4554` is immersion tin, not HASL
- Strongest upgrade candidate:
  - correct draft-standard mapping errors
  - explain that HASL should be anchored through `IPC-6012` surface-finish coverage rather than a mistaken `IPC-4554` reference

### 4) IPC-4553A immersion silver official TOC / translated TOC

- URL: `https://www.ipc.org/TOC/IPC-4553A-Chinese.pdf`
- Source owner: `IPC`
- Supports:
  - official immersion silver standard identity: `IPC-4553A`
  - TOC sections include `immersion silver thickness`, `solderability`, `cleanliness`, `electrochemical corrosion`, `packaging and storage`, `high frequency signal loss`
- Best use:
  - support that immersion silver has an official IPC finish specification and that corrosion / storage / signal-loss topics are legitimate claim families
- Non-claims:
  - do not promote exact shelf-life windows, tarnish resistance guarantees, or low-loss ranking without fuller primary support

### 5) IPC-4555 TOC for high-temperature OSP

- URL: `https://www.ipc.org/TOC/IPC-4555_TOC.pdf`
- Source owner: `IPC`
- Supports:
  - official OSP standard identity: `IPC-4555`
  - TOC includes `OSP chemical descriptions`, `process control requirements`, `shelf life`, `storage and handling`, `limitations of OSP`, `connectors`, `solderability`, `reworking OSP coated PBs`
- Strongest upgrade candidate:
  - safely harden OSP as a formal IPC finish family with explicit lifecycle and handling topics
- Non-claims:
  - do not promote draft shelf-life numbers, reflow-count defaults, or universal cost-benefit rankings from TOC metadata alone

### 6) IPC-6012F TOC for HASL and Pb-free solder coating

- URL: `https://www.ipc.org/TOC/IPC-6012F-TOC.pdf`
- Source owner: `IPC`
- Supports:
  - official bare-board performance spec includes `Hot Air Solder Leveling (HASL)/Solder`
  - TOC separates `Eutectic Tin-Lead Solder Coating` and `Pb-Free Solder Coating`
- Strongest upgrade candidate:
  - anchor `HASL` and `lead-free HASL` under a real IPC performance specification instead of unsupported marketing prose
- Non-claims:
  - does not support draft planarity, low-cost, reliability, or application-ranking claims by itself

### 7) IPC-4562B TOC for copper foil

- URL: `https://www.ipc.org/TOC/IPC-4562B-TOC.pdf`
- Source owner: `IPC`
- Supports:
  - official copper-foil standard identity: `IPC-4562B`
  - TOC explicitly includes `foil type`, `foil grade`, `bond enhancement treatment`, `foil profile`, `thickness`, `electrodeposited foil`, `wrought foil`, `peel strength`, `treatment integrity`
- Strongest upgrade candidate:
  - upgrade generic copper-foil articles from vague `foil types` language to standards-backed categories:
    - `electrodeposited foil`
    - `wrought foil`
    - `foil profile`
    - `bond enhancement treatment`
- Non-claims:
  - TOC alone does not justify any draft roughness numbers, RF-loss values, or heavy-copper performance claims

### 8) JX Advanced Metals official ED foil pages

- URL: `https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/`
- URL: `https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/rigid/`
- Source owner: `JX Advanced Metals`
- Supports:
  - official manufacturer taxonomy for `electro-deposited copper foil`
  - specific rigid-board products explicitly tagged with IPC foil grades
  - low-profile / smooth ED foil framing and published `Rz` roughness examples on product pages
- Strongest upgrade candidate:
  - official vendor anchor for ED foil as a real product class and for low-profile / smooth ED foil distinctions
- Non-claims:
  - only supports JX product families, not universal all-vendor defaults

### 9) JX Advanced Metals official rolled copper foil pages

- URL: `https://www.jx-nmm.com/english/products/copper_foil/rolled_copper_foil/`
- URL: `https://www.jx-nmm.com/english/products/copper_foil/rolled_copper_foil/index.html`
- Source owner: `JX Advanced Metals`
- Supports:
  - official manufacturer taxonomy for `rolled copper foil`
  - rolled foil described as lower roughness than electrodeposited copper foil
  - flex / vibration / pliability framing for rolled foil product families
- Strongest upgrade candidate:
  - use as a clean official anchor for `RA` vs `ED` class distinction in prose, without importing unsupported numeric performance claims
- Non-claims:
  - not enough to generalize all RF or flex superiority claims across every rolled-foil family

### 10) Tex Technology official manufacturing pages for RA and ED copper foil

- URL: `https://www.textech.co.jp/en/products/foil-stretched/`
- URL: `https://www.textech.co.jp/en/products/foil-electrolytic`
- Source owner: `Tex Technology Inc.`
- Supports:
  - rolled annealed copper foil is manufactured by repeated rolling and annealing
  - rolled foil is framed as having better flexibility than electrodeposited foil
  - separate official manufacturing pages exist for rolled and electrodeposited foil
- Best use:
  - supplementary process-language anchor for RA/ED distinctions
- Non-claims:
  - not enough for PCB-level roughness targets, insertion-loss claims, or bend-life numerics

### 11) IPC TM-650 2.6.3.7 Surface Insulation Resistance

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2-6-3-7.pdf`
- Source owner: `IPC`
- Supports:
  - official SIR method exists
  - method quantifies deleterious effects of fabrication / process / handling residues on `Surface Insulation Resistance`
  - testing is performed in moisture with electrical bias and is intended to assess leakage current and electrochemical degradation
- Strongest upgrade candidate:
  - harden `pcb-insulation.md` around real test-method vocabulary instead of unsupported dielectric-strength marketing
- Non-claims:
  - does not support draft universal pass values, high-voltage safety qualification, creepage / clearance rules, or generic substrate property tables

### 12) IPC TM-650 test-method index

- URL: `https://www.ipc.org/test-methods`
- Source owner: `IPC`
- Supports:
  - official method existence for:
    - `2.5.6B` dielectric breakdown of rigid printed wiring material
    - `2.5.7D` dielectric withstanding voltage, PWB
    - `2.5.17E` volume resistivity and surface resistance of printed wiring materials
    - `2.6.3F` moisture and insulation resistance, printed boards
    - `2.6.3.4A` moisture and insulation resistance, conformal coating
    - `2.5.7.1` dielectric withstanding voltage, polymeric conformal coating
- Strongest upgrade candidate:
  - upgrade insulation and coating articles with standards-existence claims only, not fabricated thresholds

### 13) IPC-CC-830C TOC for conformal coating qualification

- URL: `https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf`
- Source owner: `IPC`
- Supports:
  - official conformal-coating qualification standard identity: `IPC-CC-830C`
  - full title frames conformal coating as an `electrical insulating compound for printed wiring assemblies`
- Strongest upgrade candidate:
  - tighten boundary language in `waterproof-pcb.md`: coating belongs to printed wiring assemblies / PCBA protection, not bare-board waterproof proof
- Non-claims:
  - does not support IP ratings, lifetime, or immersion claims for finished products by itself

### 14) IPC-HDBK-830 handbook snippet for conformal-coating purpose

- URL: `https://www.ipc.org/TOC/IPC-HDBK-830.pdf`
- Source owner: `IPC`
- Supports:
  - conformal coatings are used with `printed circuit assemblies (PCAs)`
  - handbook purpose is design / selection / application guidance for conformal coatings
- Best use:
  - reinforce PCBA-level boundary for protection language

### 15) Dow official conformal-coating / gel / encapsulant category page

- URL: `https://www.dow.com/en-us/product-technology/pt-gels-encapsulants.html`
- Source owner: `Dow`
- Supports:
  - official separation of `Conformal Coatings`, `Gels`, and `Encapsulants`
  - conformal coatings are described as a protective barrier against moisture, dust, and chemicals
  - gels / encapsulants are separately listed for potting PCB system assemblies
- Strongest upgrade candidate:
  - sharpen waterproof article boundaries:
    - conformal coating = thin protective barrier
    - gel / encapsulant / potting = separate protection family
- Non-claims:
  - does not support specific IP ratings or service-life outcomes for finished products

### 16) Electrolube / MacDermid Alpha peelable coating mask

- URL: `https://www.macdermidalpha.com/products/circuit-board-assembly/circuit-board-protection/conformal-coatings/electrolube-pcm-peelable-coating-mask`
- Source owner: `MacDermid Alpha / Electrolube`
- Supports:
  - official product framing for a `peelable coating mask`
  - used for masking components / connectors / areas during conformal coating
  - peel-off by hand after drying without breaking or residue according to the product page
  - spot-mask use for wave soldering is explicitly mentioned
- Best use:
  - official vendor anchor that peelable-mask materials are temporary masking materials, not permanent solder mask substitutes
- Limits:
  - this is a coating-mask product page, not a PCB-fabrication-wide standards document for peelable solder mask geometry, thickness, or hole-size rules

### 17) Sun Chemical PCB materials page

- URL: `https://www.sunchemical.com/product/finetac-for-electronics/`
- Source owner: `Sun Chemical`
- Supports:
  - official PCB materials portfolio includes `peelable solder mask`
- Best use:
  - low-granularity official confirmation that peelable solder mask is a real PCB materials category from a major source owner
- Limits:
  - page is too broad to support process rules, removal behavior, or application-specific constraints

### 18) KYOCERA LTCC class page

- URL: `https://global.kyocera.com/prdct/semicon/search_material/detail/ltcc.html`
- Source owner: `KYOCERA`
- Supports:
  - official definition: `LTCC` stands for `Low Temperature Co-Fired Ceramics`
  - LTCC are also described as `glass ceramics`
  - lower co-firing temperature allows use of low-electrical-resistance metals such as copper
  - page frames LTCC for semiconductor packaging and high-frequency devices
- Strongest upgrade candidate:
  - harden LTCC definitional and class-framing content immediately
- Non-claims:
  - do not promote draft layer counts, shrinkage values, cavity tolerances, hermeticity, or application superiority from this one page

### 19) CeramTec official advanced ceramic substrates page

- URL: `https://www.ceramtec-group.com/en/ceramtec-us/substrates`
- Source owner: `CeramTec`
- Supports:
  - official comparative substrate table including `Al2O3` and `AlN`
  - page gives published example values for thermal conductivity, CTE, dielectric strength, and strength for CeramTec substrate families
  - alumina and AlN are both explicit electronic-substrate families with different positioning
- Strongest upgrade candidate:
  - this is the best recovered official bridge for `alumina-pcb.md`, `aluminum-nitride-pcb.md`, and `thermally-conductive-pcb.md`
  - can support carefully attributed product-owner-specific property examples for ceramic substrate comparison
- Limits:
  - values are source-owner-specific and should not be silently generalized to all ceramic PCBs or all AlN/alumina vendors

## Strongest fact-upgrade candidates

### Surface finishes

- `cand_fact_finish_enig_ipc_4552b_exists`
  - ENIG has an official IPC standard `IPC-4552B`.
- `cand_fact_finish_enepig_ipc_4556_exists`
  - ENEPIG has a separate official IPC standard `IPC-4556`.
- `cand_fact_finish_enepig_wire_bonding_contact_surface_in_scope`
  - IPC TOC confirms ENEPIG scope includes wire bonding and contact-surface use cases.
- `cand_fact_finish_immersion_silver_ipc_4553a_exists`
  - immersion silver has official IPC finish-spec coverage, though the revision-table entry shows it is no longer maintained.
- `cand_fact_finish_osp_ipc_4555_exists`
  - OSP has official IPC standard coverage with shelf-life / storage / handling / solderability sections.
- `cand_fact_finish_hasl_ipc_6012f_surface_finish_anchor`
  - HASL / Pb-free solder coating can be anchored through `IPC-6012F`.
- `cand_fact_finish_standard_mapping_corrected`
  - correct finish mapping:
    - `IPC-4552` = ENIG
    - `IPC-4553` = immersion silver
    - `IPC-4555` = OSP
    - `IPC-4556` = ENEPIG
    - `IPC-4554` is immersion tin, not HASL

### Copper foil

- `cand_fact_copper_foil_ipc_4562b_categories`
  - official standard covers foil type, grade, profile, bond-enhancement treatment, electrodeposited foil, and wrought foil.
- `cand_fact_copper_foil_ra_vs_ed_vendor_anchor`
  - rolled foil and ED foil are distinct official vendor product classes.
- `cand_fact_copper_foil_rolled_lower_roughness_than_ed_jx`
  - JX explicitly states rolled foil has lower roughness than electro-deposited foil.
- `cand_fact_copper_foil_ed_low_profile_smooth_variants_jx`
  - JX provides official low-profile and smooth ED foil variants with roughness examples.

### Insulation / protection

- `cand_fact_insulation_sir_ipc_tm650_2_6_3_7`
  - SIR is an official IPC method family for moisture-biased insulation degradation assessment.
- `cand_fact_insulation_method_family_exists`
  - IPC officially lists dielectric breakdown, dielectric withstand, volume/surface resistivity, and moisture/insulation resistance methods.
- `cand_fact_conformal_coating_ipc_cc_830c_pcba_scope`
  - conformal coating is officially treated as an insulating compound for printed wiring assemblies.
- `cand_fact_conformal_vs_potting_family_split_dow`
  - conformal coatings, gels, and encapsulants are separate official protection families.

### Peelable mask

- `cand_fact_peelable_mask_temporary_masking_material`
  - official vendor pages support peelable mask as a temporary masking material for selective protection during downstream processing.
- `cand_fact_peelable_mask_not_permanent_soldermask_substitute`
  - strongest safe inference from the recovered vendor pages

### LTCC / ceramic / AlN

- `cand_fact_ltcc_definition_kyocera`
  - LTCC = Low Temperature Co-Fired Ceramics.
- `cand_fact_ltcc_glass_ceramic_kyocera`
  - KYOCERA explicitly describes LTCC as glass ceramics.
- `cand_fact_ltcc_lower_firing_enables_cu_conductors_kyocera`
  - lower co-firing temperature enables use of copper conductors.
- `cand_fact_ceramic_substrate_owner_specific_alumina_aln_comparison_ceramtec`
  - CeramTec offers a source-owner-specific comparative property table for alumina and AlN substrate families.

## Blocked claims after this recovery pass

### Surface finishes still blocked

- exact ENIG / ENEPIG / OSP / immersion-silver shelf life numbers
- universal finish-thickness recommendations copied from drafts
- exact black-pad prevention recipes, Pd barrier performance guarantees, or universal wire-bond suitability
- comparative claims such as `best`, `ideal`, `more reliable`, `more durable`, `lower loss`, `more cost-effective`
- factory capability or QA claims like XRF cadence, CpK, yield, or supplier process windows

### Copper foil still blocked

- universal `RA` / `ED` roughness values
- unsupported `Ra` / `Rz` numeric defaults generalized across suppliers
- RF insertion-loss or skin-effect outcome claims not tied to the exact foil / laminate / treatment context
- heavy-copper current or heat claims copied from drafts

### Peelable mask still blocked

- design-rule numbers such as minimum hole size, thickness, keepout, or peel tab dimensions
- compatibility across all finishes / all soldering processes
- zero-residue or perfect-removal claims generalized beyond exact product pages

### Insulation still blocked

- generic FR-4 / PTFE / ceramic dielectric-strength tables copied from drafts
- CTI thresholds, creepage / clearance rules, or safety-certification claims without the exact governing standard context
- high-voltage application-readiness or automotive qualification claims

### Waterproof / protection still blocked

- IP54 / IP67 / IP68 claims for PCB or PCBA alone
- lifetime, immersion duration, pressure-cooker endurance, salt-fog duration, or field-failure reduction claims from drafts
- broad `waterproof PCB` phrasing unless clearly reframed to enclosure/system-level or coated-assembly protection context

### LTCC / ceramic / thermal still blocked

- shrinkage values, firing temperatures, conductor widths, via diameters, layer counts, hermeticity, or 3D-integration capability claims from drafts
- universal alumina vs AlN numeric comparisons unless tied to the exact source owner and product family
- direct substitution claims that all ceramic PCBs are LTCC, or that all LTCC outperforms all alumina constructions

## Residual gaps

- full English-accessible primary TOC or text for `IPC-4553A` if later fact work needs tighter immersion-silver extraction than the recovered IPC material here
- a stronger official primary anchor for `peelable solder mask` in PCB fabrication specifically, not just coating-mask or broad vendor portfolio confirmation
- official enclosure/system-level source if `waterproof-pcb.md` must discuss IP ratings without overclaiming PCB-only protection
- more source-owner-specific alumina / AlN datasheets if the batch later needs exact numeric property tables beyond the CeramTec comparison page
- additional vendor or standard anchors if the copper-foil article later needs exact roughness classes by IPC grade rather than only RA/ED and low-profile class framing

## Practical next-use summary

Use these recovered anchors first:

1. `IPC-4552B`, `IPC-4556`, `IPC-4555`, `IPC-6012F`, and the IPC revision table to clean up finish taxonomy and incorrect standard references.
2. `IPC-4562B` plus JX / Tex official pages to harden copper-foil class language around `ED`, `wrought/rolled`, profile, and treatment.
3. `IPC TM-650` insulation methods plus `IPC-CC-830C` to move insulation / coating articles toward real test-method and scope language.
4. `KYOCERA LTCC` and `CeramTec` to upgrade LTCC, alumina, and AlN from topic-inventory level into conservative source-backed class framing.

Do not use this pass to promote:

- draft numbers
- supplier superiority
- readiness / certification / yield / shelf-life promises
- PCB-only `waterproof` claims that actually depend on coating selection, assembly details, and enclosure design
