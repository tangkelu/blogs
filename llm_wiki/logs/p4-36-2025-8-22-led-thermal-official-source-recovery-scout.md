# P4-36 Official-Source Recovery Scout

- Lane: `P4-36 official-source recovery scout`
- Batch: `/code/blogs/tmps/2025.8.22/en`
- Focus: LED thermal management, MCPCB/IMS materials, optical/photometric testing, LED assembly process, automotive/medical LED boundaries, reliability testing
- Model requested: `gpt-5.4`
- Scout timestamp: `2026-04-28 15:49:45 CST`
- Constraint: drafts treated as claim inventory only, not authority
- Edit scope: only this file

## Files inventoried

- `/code/blogs/tmps/2025.8.22/en/led-pcb-assembly-techniques.md`
- `/code/blogs/tmps/2025.8.22/en/led-pcb-testing-methods.md`
- `/code/blogs/tmps/2025.8.22/en/mcpcb-reliability-testing.md`
- `/code/blogs/tmps/2025.8.22/en/mcpcb-thermal-simulation.md`
- `/code/blogs/tmps/2025.8.22/en/led-pcb-automotive-lighting.md`
- `/code/blogs/tmps/2025.8.22/en/automotive-mcpcb-standards.md`
- `/code/blogs/tmps/2025.8.22/en/led-pcb-medical-devices.md`
- `/code/blogs/tmps/2025.8.22/en/mcpcb-assembly.md`

## Claim-family inventory from drafts

### 1. LED thermal management

High-value claims needing real data:

- LED junction temperature strongly affects light output, color stability, and lifetime.
- MCPCB, ceramic, and other high-thermal substrates reduce junction temperature.
- Thermal validation uses thermocouples, IR thermography, thermal resistance measurement, and cycling/power-cycling methods.
- Thermal simulation should model metal base, dielectric, copper, interfaces, and boundary conditions.

### 2. MCPCB / IMS materials

High-value claims needing real data:

- IMS / MCPCB is a layered construction with circuit copper, dielectric, and metal base.
- Aluminum and copper bases have materially different thermal conductivities and assembly behavior.
- Dielectric thermal conductivity and thickness dominate insulation-versus-heat-transfer tradeoffs.
- Vendor-specific IMS materials support certain thermal ranges, isolation properties, and application classes.

### 3. Optical / photometric testing

High-value claims needing real data:

- Integrating spheres and goniophotometers are used for total flux and angular distribution measurements.
- LED optical validation should separate product-level photometric measurement from lumen-maintenance testing of LED packages/modules.
- Photobiological safety is a separate standards boundary from basic photometric performance.

### 4. LED assembly process

High-value claims needing real data:

- LED assembly is sensitive to solder profile, thermal pad voiding, moisture/handling limits, and package-specific assembly precautions.
- SMT, COB, wire bonding, and through-hole claims need package-vendor or standard-backed support.
- Generic process windows in drafts should not be promoted unless tied to standard guidance or a vendor application note.

### 5. Automotive LED / MCPCB boundaries

High-value claims needing real data:

- AEC-Q100 and AEC-Q200 apply to components, not bare PCBs as a direct qualification badge.
- IATF 16949 is a quality-management-system standard, not a product-performance certification.
- Automotive environment/test claims need proper linkage to AEC, ISO 16750, CISPR 25, and lamp/regulatory standards where relevant.

### 6. Medical LED boundaries

High-value claims needing real data:

- ISO 13485 is a QMS standard.
- ISO 14971 is risk-management process guidance.
- IEC 60601-1 and related collateral standards define medical electrical equipment safety / EMC boundaries.
- IEC 62471 governs photobiological safety of lamps and lamp systems.
- Implantable / patient-contact / FDA submission / biocompatibility claims require tighter scope and should not be generalized from LED board manufacturing text.

### 7. Reliability testing

High-value claims needing real data:

- Thermal cycling, THB, HAST, salt spray, vibration, shock, hipot, and insulation-resistance tests each have separate standard homes.
- Draft claims that convert test hours directly into “equivalent field years” are weak unless a named source gives that model and its limits.

## Official-source candidate set

Note: `candidate_source_id` and `candidate_fact_id` are proposed only. Nothing here updates registries.

### Candidate 1

- URL: `https://store.ies.org/product/lm-79-19-approved-method-optical-and-electrical-measurements-of-solid-state-lighting-products-1409.cfm`
- Owner: Illuminating Engineering Society
- Source type: standards storefront / standard landing page
- Supported claims:
  - LM-79 is the product-level IES method for optical and electrical measurements of solid-state lighting products.
  - Appropriate for total luminous flux / electrical measurement framing at finished-product level.
- Limits / non-claims:
  - Not a lumen-maintenance method.
  - Landing page alone will not support detailed test setup or derived numeric claims.
- Candidate source_id: `src_ies_lm79_2019_store`
- Candidate fact_id: `fact_led_photometric_product_measurement_lm79`

### Candidate 2

- URL: `https://store.ies.org/product/lm-80-21-approved-method-measuring-lumen-and-color-maintenance-of-led-packages-arrays-and-modules-1335.cfm`
- Owner: Illuminating Engineering Society
- Source type: standards storefront / standard landing page
- Supported claims:
  - LM-80 concerns lumen and color maintenance of LED packages, arrays, and modules.
  - Useful boundary against draft language that blurs product photometry and package maintenance testing.
- Limits / non-claims:
  - Does not itself justify projected lifetime claims unless paired with TM-21 and the applicable data set.
- Candidate source_id: `src_ies_lm80_2021_store`
- Candidate fact_id: `fact_led_lumen_color_maintenance_lm80_scope`

### Candidate 3

- URL: `https://store.ies.org/product/tm-21-19-projecting-long-term-luminous-flux-maintenance-of-led-packages-arrays-and-modules-1225.cfm`
- Owner: Illuminating Engineering Society
- Source type: technical memorandum storefront / standard landing page
- Supported claims:
  - TM-21 is the IES method used with LM-80 data for long-term luminous-flux-maintenance projection.
- Limits / non-claims:
  - Not direct proof of a specific product lifetime by itself.
  - Does not validate blanket `L70 >= 50,000 h` claims without the actual underlying data and projection conditions.
- Candidate source_id: `src_ies_tm21_2019_store`
- Candidate fact_id: `fact_led_lifetime_projection_tm21_scope`

### Candidate 4

- URL: `https://webstore.iec.ch/en/publication/2600`
- Owner: IEC
- Source type: standards storefront / standard landing page
- Supported claims:
  - IEC 62471 is the photobiological safety standard for lamps and lamp systems.
- Limits / non-claims:
  - Does not support general optical performance claims.
  - Does not support medical efficacy claims.
- Candidate source_id: `src_iec_62471_store`
- Candidate fact_id: `fact_led_photobiological_safety_iec62471`

### Candidate 5

- URL: `https://www.iso.org/standard/59752.html`
- Owner: ISO
- Source type: official standards landing page
- Supported claims:
  - ISO 13485:2016 is titled `Medical devices — Quality management systems — Requirements for regulatory purposes`.
  - Supports QMS framing for medical-device manufacturing organizations.
- Limits / non-claims:
  - Does not by itself certify a specific LED board as medically safe or clinically effective.
  - Does not support implantable-device suitability claims.
- Candidate source_id: `src_iso_13485_2016_landing`
- Candidate fact_id: `fact_medical_qms_iso13485_scope`

### Candidate 6

- URL: `https://www.iso.org/standard/72704.html`
- Owner: ISO
- Source type: official standards landing page
- Supported claims:
  - ISO 14971:2019 is titled `Medical devices — Application of risk management to medical devices`.
  - Supports risk-management process framing.
- Limits / non-claims:
  - Not evidence that a given LED assembly is safe or compliant.
- Candidate source_id: `src_iso_14971_2019_landing`
- Candidate fact_id: `fact_medical_risk_management_iso14971_scope`

### Candidate 7

- URL: `https://webstore.iec.ch/en/publication/2612`
- Owner: IEC
- Source type: standards storefront / standard landing page
- Supported claims:
  - IEC 60601-1 is the core basic safety and essential performance standard family anchor for medical electrical equipment.
- Limits / non-claims:
  - Does not support blanket FDA-marketability claims.
  - Needs related collateral/particular standards for EMC and product-specific interpretations.
- Candidate source_id: `src_iec_60601_1_store`
- Candidate fact_id: `fact_medical_electrical_safety_iec60601_1_scope`

### Candidate 8

- URL: `https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/quality-system-qs-regulationmedical-device-good-manufacturing-practices`
- Owner: U.S. FDA
- Source type: regulator guidance / overview page
- Supported claims:
  - FDA treats device manufacturing under quality-system requirements / good manufacturing practices.
  - Useful as regulator anchor for U.S. medical-device process boundaries.
- Limits / non-claims:
  - Not a substitute for device-specific clearance/approval evidence.
  - Not proof that a PCB fabricator can claim support for 510(k), PMA, or implantables without broader design-control and regulatory context.
- Candidate source_id: `src_fda_qs_regulation_overview`
- Candidate fact_id: `fact_fda_medical_qs_boundary`

### Candidate 9

- URL: `https://www.aecouncil.com/Documents/AEC_Q100_Rev_H_Base_Document.pdf`
- Owner: Automotive Electronics Council
- Source type: official standard PDF
- Supported claims:
  - AEC-Q100 is the AEC qualification document for integrated circuits.
  - Useful to bound automotive draft claims around qualified semiconductors in LED driver/control chains.
- Limits / non-claims:
  - Not a bare-PCB qualification standard.
  - This scout did not fully verify the live PDF contents because the official endpoint had TLS/handshake failures from the current environment.
- Candidate source_id: `src_aec_q100_rev_h_pdf`
- Candidate fact_id: `fact_aec_q100_ic_scope_not_pcb`

### Candidate 10

- URL: `https://www.aecouncil.com/Documents/AEC_Q200_Rev_E_Base_Document.pdf`
- Owner: Automotive Electronics Council
- Source type: official standard PDF
- Supported claims:
  - AEC-Q200 is the AEC qualification document for passive components.
- Limits / non-claims:
  - Not a bare-PCB qualification standard.
  - This scout did not fully verify the live PDF contents because the official endpoint had TLS/handshake failures from the current environment.
- Candidate source_id: `src_aec_q200_rev_e_pdf`
- Candidate fact_id: `fact_aec_q200_passive_scope_not_pcb`

### Candidate 11

- URL: `https://www.iatfglobaloversight.org/iatf-16949/`
- Owner: IATF Global Oversight
- Source type: official standard overview page
- Supported claims:
  - IATF 16949 is an automotive quality-management-system framework.
- Limits / non-claims:
  - Not a product qualification claim for MCPCB thermal performance.
  - Should not be written as if it directly certifies `automotive-grade LED PCB` performance.
- Candidate source_id: `src_iatf_16949_overview`
- Candidate fact_id: `fact_iatf16949_qms_not_product_cert`

### Candidate 12

- URL: `https://www.iso.org/standard/57399.html`
- Owner: ISO
- Source type: official standards landing page
- Supported claims:
  - ISO 16750 is the road-vehicle environment/testing family for electrical and electronic equipment.
- Limits / non-claims:
  - Family-level anchor only unless the exact part is cited.
  - Not enough alone to justify numeric vibration/shock profiles copied into the drafts.
- Candidate source_id: `src_iso_16750_family_landing`
- Candidate fact_id: `fact_automotive_environmental_testing_iso16750_family`

### Candidate 13

- URL: `https://webstore.iec.ch/en/publication/7407`
- Owner: IEC
- Source type: standards storefront / standard landing page
- Supported claims:
  - CISPR 25 covers radio-disturbance characteristics for protection of receivers used on board vehicles, boats, and internal-combustion-engine devices.
- Limits / non-claims:
  - Emissions scope only; not a general automotive qualification umbrella.
- Candidate source_id: `src_cispr25_store`
- Candidate fact_id: `fact_automotive_emissions_cispr25_scope`

### Candidate 14

- URL: `https://store.astm.org/b0117-19.html`
- Owner: ASTM International
- Source type: standards storefront / standard landing page
- Supported claims:
  - ASTM B117 is `Standard Practice for Operating Salt Spray (Fog) Apparatus`.
  - Good official anchor for salt-spray test naming and scope.
- Limits / non-claims:
  - Does not by itself prove service-life correlation in outdoor LED products.
- Candidate source_id: `src_astm_b117_2019_store`
- Candidate fact_id: `fact_salt_spray_astm_b117_scope`

### Candidate 15

- URL: `https://www.jedec.org/standards-documents/docs/jesd22-a110`
- Owner: JEDEC
- Source type: standard landing page
- Supported claims:
  - JESD22-A110 is the HAST standard family anchor.
- Limits / non-claims:
  - Does not justify field-life equivalence statements without a product-specific acceleration model.
- Candidate source_id: `src_jedec_jesd22_a110_landing`
- Candidate fact_id: `fact_hast_jesd22_a110_scope`

### Candidate 16

- URL: `https://www.jedec.org/standards-documents/docs/jesd22-a101`
- Owner: JEDEC
- Source type: standard landing page
- Supported claims:
  - JESD22-A101 is the steady-state temperature humidity bias anchor.
- Limits / non-claims:
  - Not interchangeable with HAST.
- Candidate source_id: `src_jedec_jesd22_a101_landing`
- Candidate fact_id: `fact_thb_jesd22_a101_scope`

### Candidate 17

- URL: `https://shop.ipc.org/j-std-001k-english-d`
- Owner: IPC
- Source type: standards storefront / standard landing page
- Supported claims:
  - J-STD-001 is the IPC requirements standard for soldered electrical and electronic assemblies.
- Limits / non-claims:
  - Does not directly provide LED-package-specific reflow settings.
  - Should not be used to justify the draft’s exact profile windows.
- Candidate source_id: `src_ipc_jstd001_store`
- Candidate fact_id: `fact_solder_assembly_jstd001_scope`

### Candidate 18

- URL: `https://shop.ipc.org/ipc-a-610k-english-d`
- Owner: IPC
- Source type: standards storefront / standard landing page
- Supported claims:
  - IPC-A-610 is the acceptance standard for electronic assemblies.
- Limits / non-claims:
  - Acceptance criteria standard, not a thermal-performance or automotive-qualification source.
- Candidate source_id: `src_ipc_a610_store`
- Candidate fact_id: `fact_assembly_acceptability_ipca610_scope`

### Candidate 19

- URL: `https://www.henkel-adhesives.com/us/en/product/thermal-management-materials/bergquist_thermal_clad.html`
- Owner: Henkel
- Source type: official vendor product / design-material page
- Supported claims:
  - THERMAL CLAD is an insulated metal substrate / IMS product family.
  - Useful official vendor source for layered IMS construction and vendor-stated material family positioning.
- Limits / non-claims:
  - Vendor-family page alone may not support numeric dielectric conductivity values for every variant.
- Candidate source_id: `src_henkel_thermal_clad_family`
- Candidate fact_id: `fact_ims_vendor_family_thermal_clad`

### Candidate 20

- URL: `https://www.ventec-group.com/product-range/ims-materials/`
- Owner: Ventec International Group
- Source type: official vendor product family page
- Supported claims:
  - IMS material family availability and official vendor framing of insulated metal substrate offerings.
- Limits / non-claims:
  - Needs a specific data sheet before claiming exact thermal conductivity, dielectric thickness, or breakdown performance.
- Candidate source_id: `src_ventec_ims_family`
- Candidate fact_id: `fact_ims_vendor_family_ventec`

### Candidate 21

- URL: `https://www.rogerscorp.com/advanced-electronics-solutions/curamik-ceramic-substrates`
- Owner: Rogers Corporation
- Source type: official vendor product family page
- Supported claims:
  - Curamik ceramic substrates are official vendor-backed options for high thermal conductivity / high-reliability power applications.
- Limits / non-claims:
  - Not a generic proof that all ceramic PCB options meet any specific medical or automotive requirement.
- Candidate source_id: `src_rogers_curamik_family`
- Candidate fact_id: `fact_ceramic_substrate_vendor_family_curamik`

### Candidate 22

- URL: `https://www.cree-led.com/news/ap-note-thermal-management-of-xlamp-leds/`
- Owner: Cree LED
- Source type: official vendor application note / engineering guidance
- Supported claims:
  - LED thermal path and junction-temperature management can be sourced from a primary LED-package vendor.
- Limits / non-claims:
  - Package-family-specific guidance; should not be generalized without noting source scope.
- Candidate source_id: `src_cree_led_thermal_appnote`
- Candidate fact_id: `fact_led_vendor_thermal_management_primary`

### Candidate 23

- URL: `https://led-ld.nichia.co.jp/en/support/`
- Owner: Nichia
- Source type: official vendor support / precautions portal
- Supported claims:
  - Nichia publishes official handling / soldering / precautions material for LED packages.
- Limits / non-claims:
  - Actual numeric assembly limits must come from the specific package document, not from the portal root.
- Candidate source_id: `src_nichia_led_support_portal`
- Candidate fact_id: `fact_led_vendor_handling_precautions_primary`

## Top upgrade candidates

These are the most leverage-heavy next sources for converting the drafts into reusable real-data coverage:

1. `LM-79 + LM-80 + TM-21`
   - Best correction for the drafts’ optical-testing and LED-lifetime overreach.
   - Establishes clean boundaries among product photometry, package maintenance, and lifetime projection.

2. `AEC-Q100 / AEC-Q200 + IATF 16949 + ISO 16750 + CISPR 25`
   - Best correction for automotive overclaims.
   - Separates component qualification, QMS qualification, environmental testing, and EMC scope.

3. `ISO 13485 + ISO 14971 + IEC 60601-1 + IEC 62471 + FDA QS overview`
   - Best correction for medical-device framing.
   - Prevents unsupported claims around implantables, clinical efficacy, or blanket regulatory readiness.

4. `Henkel THERMAL CLAD + Ventec IMS + Rogers curamik`
   - Best official-source base for MCPCB / IMS / ceramic material construction and property boundaries.
   - Better than generic blog prose for thermal-stack explanations.

5. `Cree LED / Nichia package handling and thermal notes`
   - Best primary sources for LED assembly-process claims that the current drafts express too generically.

## Blocked or weakly supported claims

These claims should remain blocked until exact primary documentation is attached:

- Exact reflow temperature windows, soak durations, cooling rates, and nitrogen thresholds presented as universal MCPCB or LED rules.
- Exact stencil aperture reductions or voiding-performance claims presented without package/material-specific source support.
- Blanket claims that `AEC-Q100` or `AEC-Q200` make a PCB or LED module `automotive-grade`.
- Blanket claims that `IATF 16949` certifies product reliability/performance rather than manufacturing-system process control.
- Product-lifetime statements such as `15+ years`, `L70 >= 50,000 h`, or `264 hours HAST equals 10+ years field exposure` unless tied to a named model and actual test data.
- Broad claims that medical LED boards are suitable for implantable devices, direct patient contact, FDA submission support, or clinical-effectiveness outcomes.
- Exact phototherapy wavelength tolerances, CRI/R9 thresholds, or dosimetry stability windows unless sourced to device-specific or standards-backed primary material.
- Numeric substrate conductivity, dielectric breakdown, or moisture-absorption values when not tied to a specific vendor data sheet revision.
- Simulation ROI claims such as `reducing development cycles 40-60%` without an attributable primary source.
- Factory-capability claims in the drafts such as yields, capacities, response times, and inspection coverage; those are out of scope for official-source recovery unless internal audited records are intentionally provided.

## Residual gaps

- Need exact official URLs confirmed for some paid/storefront standards pages where titles are known but the browser path may vary.
- AEC official PDF endpoints were unstable from the current environment, so contents were not fully verified in-session.
- IES storefront pages were slower / less reliable to fetch directly here; still good candidates, but final fact extraction should verify title/year from the live landing page at extraction time.
- IPC TM-650 method-level pages for thermal cycling / bend are not fully pinned in this scout; IPC storefront or document-specific official pages should be added before method-level numeric claims are recovered.
- Vendor-specific IMS material properties still need exact per-material data sheets, not just family pages.
- LED package assembly claims still need package-family documents from LED manufacturers, not only general support portals.

## Recommended next-step recovery order

1. Recover standards-boundary facts first:
   - `LM-79`
   - `LM-80`
   - `TM-21`
   - `IEC 62471`
   - `ISO 13485`
   - `ISO 14971`
   - `IEC 60601-1`
   - `AEC-Q100`
   - `AEC-Q200`
   - `IATF 16949`
   - `ISO 16750`
   - `CISPR 25`

2. Recover materials facts second:
   - specific Henkel / Ventec / Rogers data sheets for cited IMS or ceramic families

3. Recover assembly-process facts third:
   - LED vendor package handling / soldering / thermal notes from Cree LED, Nichia, Lumileds, or ams OSRAM official sites

4. Defer or block:
   - factory capability claims
   - unsupported lifetime conversions
   - medical efficacy or implantable-device suitability

## Output summary

- Changed file: `/code/blogs/llm_wiki/logs/p4-36-2025-8-22-led-thermal-official-source-recovery-scout.md`
- Top upgrade candidates: IES optical/lifetime standards, automotive standards boundary set, medical standards boundary set, IMS vendor families, LED vendor handling/thermal notes
- Blocked claims: universal process windows, product-lifetime projections without data, automotive-grade misuse of AEC/IATF, medical implantable / FDA-readiness overclaims, unsourced numeric material properties
- Residual gaps: method-level IPC verification, unstable AEC access, per-material vendor data sheets, package-specific LED assembly documentation
