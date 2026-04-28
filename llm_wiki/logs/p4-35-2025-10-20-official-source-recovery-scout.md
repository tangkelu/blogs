# P4-35 2025-10-20 Official-Source Recovery Scout

Date: 2026-04-28
Model: `gpt-5.4`
Input inventory: `/code/blogs/tmps/2025.10.20/en`
Lane: official-source recovery scout for `aluminum / IMS / MCPCB` and `flex / FPC / polyimide / dynamic-flex`
Output ownership: only this file

## Purpose

This scout treats the `tmps/2025.10.20/en` drafts as claim inventory only, not as authority.

The goal is to identify official sources that can support later upgrades, record exact scope limits, and leave unsupported commercial, capability, and performance claims blocked.

It does not promote facts into registries, facts, wiki pages, or trackers.

## Draft Families Inspected

- Aluminum / IMS / MCPCB:
  `aluminum-substrate.md`, `metal-core-pcb.md`, `aluminum board.md`, `aluminum-base-pcb.md`, `aluminum-circuit-board.md`, `aluminum-core-pcb.md`, `high-thermal-aluminum-pcb.md`, plus related manufacturing / factory / prototype / supplier / turnkey drafts.
- Flex / FPC / polyimide / dynamic-flex:
  `flex-pcb.md`, `flexible-pcb.md`, `flexible-circuit-board.md`, `fpc-board.md`, `polyimide-pcb.md`, `dynamic-flex-pcb.md`, `single-layer-flex-pcb.md`, `double-layer-flex-pcb.md`, `multilayer-flex-pcb.md`, `bendable-pcb.md`, `rollable-pcb.md`, `foldable-pcb.md`, and related manufacturing / assembly / manufacturer drafts.

## Official Sources Found

### 1. Ventec IMS family overview

- URL: `https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/`
- Source owner: Ventec International Group
- Source type: official manufacturer product-family page
- Supported claims:
  official identity for Ventec `tec-thermal` IMS / metal-base laminate family;
  manufacturer-controlled family naming and thermal-management positioning;
  product-family context for MCPCB / IMS writing.
- Exact limits / non-claims:
  not a license for numeric thermal conductivity, dielectric thickness, thermal impedance, copper weight, metal plate, stock, or shop capability claims;
  pair with exact-product datasheets for numbers;
  do not freeze lineup order or availability.
- Candidate fact IDs if upgraded later:
  `methods-mcpcb-ims-family-context`
  `materials-ventec-ims-family-overview`

### 2. Ventec VT-4B7 IMS datasheet

- URL: `https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b7/datasheet/`
- Source owner: Ventec International Group
- Source type: official manufacturer datasheet page
- Supported claims:
  official `VT-4B7` product identity;
  exact-product IMS / metal-base laminate context;
  product-level dielectric / thermal / flammability / construction context;
  thermal-conductivity and dielectric-thickness discussion only when kept product-bound and treated as typical-data context.
- Exact limits / non-claims:
  do not convert typical data into guaranteed design limits;
  not proof of board-level thermal resistance, junction-temperature reduction, LED-life improvement, or HIL capability;
  not proof of supplier stock, lead time, or available build options at any fab.
- Candidate fact IDs if upgraded later:
  `materials-ventec-vt-4b7`
  `methods-mcpcb-ims-material-value-scope`

### 3. Ventec VT-4BC IMS datasheet

- URL: `https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4bc/datasheet/`
- Source owner: Ventec International Group
- Source type: official manufacturer datasheet page
- Supported claims:
  official `VT-4BC` product identity;
  exact-product IMS material example for lighting, motor drive, controller, rectifier, power-supply, and power-conversion context;
  source-scoped thermal and dielectric values when method / thickness / typical-data scope is preserved.
- Exact limits / non-claims:
  not a board-level performance guarantee;
  not permission to infer generic MCPCB defaults such as `all aluminum boards use 3-5 W/mK dielectric`;
  not proof of HIL/APT copper-weight, panel-size, or production options.
- Candidate fact IDs if upgraded later:
  `materials-ventec-vt-4bc`
  `methods-ims-product-example-scope`

### 4. Ventec VT-4BD IMS datasheet

- URL: `https://www.ventec-group.com/cht/products/tec-thermal-thermal-management-ims/vt-4bd/datasheet/`
- Source owner: Ventec International Group
- Source type: official manufacturer datasheet page
- Supported claims:
  official `VT-4BD` product identity;
  exact-product higher-conductivity IMS example;
  source-scoped thermal / dielectric / electrical / flammability / construction context.
- Exact limits / non-claims:
  localized manufacturer-controlled path should be refreshed before public reuse;
  not proof of generic aluminum-board superiority, board-level heat-spreading outcome, or finished-product reliability;
  not proof of supplier availability or fab options.
- Candidate fact IDs if upgraded later:
  `materials-ventec-vt-4bd`
  `methods-ims-high-thermal-example-scope`

### 5. DuPont Kapton HN product page

- URL: `https://www.dupont.com/electronics-industrial/product-family/kapton-hn.html`
- Source owner: DuPont
- Source type: official manufacturer product page
- Supported claims:
  official `Kapton HN` product identity;
  exact-product all-polyimide film positioning;
  manufacturer-controlled temperature-use context and application vocabulary for the film itself.
- Exact limits / non-claims:
  dynamic live page; refresh before public numeric use;
  does not make `Kapton HN` interchangeable with all `Kapton`, all polyimide films, or finished flex PCB constructions;
  not proof of bend life, bend radius, IPC compliance, or production use by any board shop.
- Candidate fact IDs if upgraded later:
  `materials-dupont-kapton-hn`
  `materials-polyimide-film-product-identity-scope`

### 6. DuPont Kapton HN datasheet

- URL: `https://www.dupont.com/content/dam/dupont/amer/us/en/ei-transformation/public/documents/en/EI-10206-Kapton-HN-Data-Sheet.pdf`
- Source owner: DuPont
- Source type: official manufacturer datasheet PDF
- Supported claims:
  exact-product `Kapton HN` film identity;
  datasheet-backed material values when thickness, temperature, and test method remain attached;
  product-specification context for film-level discussion.
- Exact limits / non-claims:
  film data is not finished-board bend-cycle proof, rigid-flex reliability proof, or flex-manufacturing capability proof;
  do not generalize `Kapton HN` values into generic polyimide values.
- Candidate fact IDs if upgraded later:
  `materials-dupont-kapton-hn`
  `materials-kapton-hn-datasheet-scope`

### 7. UBE UPILEX grade-details page

- URL: `https://www.ube.com/ube/en/contents/chemical/polyimide/upilex/upilex_grade.html`
- Source owner: UBE Corporation
- Source type: official manufacturer product page
- Supported claims:
  official `UPILEX-S` grade identity;
  exact-product thickness / width lineup;
  grade-specific mechanical, electrical, thermal, environmental, and chemical-resistance tables when grade / condition / method stay attached;
  official FPC / TAB substrate application context.
- Exact limits / non-claims:
  dynamic page; refresh before public numeric reuse;
  does not make `UPILEX-S` interchangeable with all `UPILEX` grades or generic polyimide;
  not proof of bend-life, bend-radius, stackup defaults, or HIL/APT usage.
- Candidate fact IDs if upgraded later:
  `materials-ube-upilex-s`
  `materials-upilex-grade-scoped-values`

### 8. UBE UPILEX family advantages page

- URL: `https://www.ube.com/ube/en/contents/chemical/polyimide/upilex/upilex.html`
- Source owner: UBE Corporation
- Source type: official manufacturer product-family page
- Supported claims:
  official UPILEX family positioning;
  grade-lineup context;
  family-level application vocabulary including circuit-board materials, base film, cover film, reinforcing plate, and laminated two-layer CCL.
- Exact limits / non-claims:
  family page is not a substitute for grade-specific data;
  not proof of finished-board reliability, fab capability, or IPC compliance.
- Candidate fact IDs if upgraded later:
  `materials-ube-upilex-family-context`
  `materials-upilex-application-vocabulary`

### 9. Minco Flex Circuits Design Guide

- URL: `https://www.minco.com/wp-content/uploads/Minco-Flex-Circuits-Design-Guide-2019.pdf`
- Source owner: Minco
- Source type: manufacturer design guide
- Supported claims:
  flex-circuit design-guidance context;
  bend-radius guidance as manufacturer design recommendation;
  explanation that bend posture depends on thickness, construction, and static vs dynamic use;
  guidance vocabulary around adhesiveless materials, conductor plating in bend areas, and unbonding strategies.
- Exact limits / non-claims:
  use as design-guidance context only;
  do not convert example bend ratios into universal IPC thresholds or released-lot acceptance criteria;
  not proof of dynamic-flex cycle life, HIL/APT factory capability, or warranty.
- Candidate fact IDs if upgraded later:
  `methods-flex-bend-guidance-minco`
  `methods-static-vs-dynamic-bend-posture`

### 10. IPC-6013E public TOC

- URL: `https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf`
- Source owner: IPC
- Source type: standards metadata / public TOC
- Supported claims:
  official identity for `IPC-6013E`;
  high-level scope that IPC maintains a qualification / performance specification for flexible printed boards and related flex / rigid-flex topics.
- Exact limits / non-claims:
  public TOC does not expose reusable thresholds;
  do not infer class-specific requirements, bend limits, plating criteria, workmanship limits, or acceptance tables from this public record alone.
- Candidate fact IDs if upgraded later:
  `standards-ipc-6013e-identity`
  `methods-flex-performance-spec-family-context`

### 11. IPC-2223E official standard page

- URL: `https://shop.electronics.org/ipc-2223/ipc-2223-standard-only/Revision-e/english`
- Source owner: IPC / electronics.org
- Source type: standards product page
- Supported claims:
  official identity for `IPC-2223E`;
  high-level scope that IPC maintains a sectional design standard for flexible / rigid-flexible printed boards.
- Exact limits / non-claims:
  does not supply bend-radius tables, adhesive rules, conductor geometry thresholds, dynamic-flex cycle limits, or construction defaults;
  pair with licensed standards or vendor guides before any design-threshold use.
- Candidate fact IDs if upgraded later:
  `standards-ipc-2223e-identity`
  `methods-flex-design-standard-family-context`

## Official Sources Not Recovered In This Lane

No new official source was recovered here for:

- generic aluminum alloy `5052 / 6061 / 1100` property rows from a clearly authoritative alloy owner or standards body, with enough precision to safely upgrade draft CTE / conductivity tables;
- official dynamic-flex cycle-life guarantees;
- official rollable / foldable flex reliability thresholds;
- official supplier-neutral connector-flex capability rules;
- official HIL/APT factory certifications, lead times, MOQ, yields, scale, or quality rates.

Those remain blocked.

## Candidate Facts

These are candidate fact targets only. They were not created in this lane.

- `materials-ventec-vt-4b7`
- `materials-ventec-vt-4bc`
- `materials-ventec-vt-4bd`
- `materials-ventec-ims-family-overview`
- `materials-dupont-kapton-hn`
- `materials-kapton-hn-datasheet-scope`
- `materials-ube-upilex-s`
- `materials-ube-upilex-family-context`
- `methods-mcpcb-ims-family-context`
- `methods-mcpcb-ims-material-value-scope`
- `methods-flex-bend-guidance-minco`
- `methods-static-vs-dynamic-bend-posture`
- `standards-ipc-6013e-identity`
- `standards-ipc-2223e-identity`
- `methods-flex-performance-spec-family-context`
- `methods-flex-design-standard-family-context`

## Supported Claim Recovery Summary

### Aluminum / IMS / MCPCB

Recovered support is good for:

- official manufacturer identity for IMS / metal-base laminate family and exact-product examples;
- source-scoped material-property discussion at the exact-product level;
- explanation that IMS / MCPCB articles should distinguish family context from datasheet-backed values;
- method names already attached by official datasheets, including `ISO 22007-2` and `ASTM D5470`, when preserved exactly as source context.

Recovered support is not enough for:

- generic `aluminum substrate` numeric tables in the drafts;
- alloy-default claims such as `5052 is standard for LED`, `6061 for power electronics`, or `1100` as a routine base-metal option;
- board-level thermal-performance multipliers versus FR4;
- junction-temperature reduction, component-life extension, EMI-shielding outcome, or finished-product application readiness.

### Flex / FPC / polyimide / dynamic-flex

Recovered support is good for:

- exact-product polyimide-film examples from DuPont and UBE;
- family-level UPILEX vocabulary;
- design-guide explanation that bend posture depends on thickness, construction, and static vs dynamic use;
- official IPC document identity for flex performance-spec and design-standard families.

Recovered support is not enough for:

- generic polyimide numeric ladders across all films;
- universal bend-radius tables;
- dynamic-flex cycle counts such as `100,000 to 1,000,000+`;
- claims that RA copper is universally mandatory or that ED copper universally fails;
- adhesiveless cost/thickness deltas treated as universal rules;
- component / via / stiffener prohibitions presented as IPC or universally authoritative thresholds without narrower source framing.

## Blocked Claims

### Numeric and performance claims still blocked

- `50-200 um` dielectric layer and `1.0-3.0 mm` metal-base ranges as generic MCPCB defaults unless tied to a named product.
- Generic dielectric thermal-conductivity ladders such as `1-5 W/mK`, `1.5-2.0 W/mK`, or `3-5 W/mK` unless tied to an exact source/product/method.
- Generic aluminum thermal conductivity claims such as `170-180 W/mK` or `200 W/mK` when used as authoritative board-material defaults without a recovered alloy source.
- Draft CTE tables for `5052`, `6061`, polyimide dielectric, and FR4 z-axis as promotable facts from this lane.
- Board-vs-FR4 outcome claims such as `8-10 times faster`, `30-50 C lower junction temperature`, `2-5x longer lifespan`, or similar.
- Dynamic-flex endurance claims such as `100,000 to 1,000,000+ cycles` or `millions of cycles`.
- Universal bend-radius, roll-diameter, trace-width/spacing, via-diameter, or coverlay-thickness defaults taken from drafts.

### Capability / certification / commercial claims still blocked

- HIL/APT `ISO 9001`, `UL`, `IPC-6012`, `IATF 16949`, PPAP, automotive, medical, aerospace, or biocompatibility claims.
- Lead time, price, MOQ, throughput, yield, quick-turn, prototype timing, production-scale, or supplier-superiority claims.
- Factory-line, tooling, AOI, e-test, thermal-simulation, fixturing, inspection-depth, or turnkey-completeness claims as proven facts.

### Application-readiness and qualification claims still blocked

- LED-life extension, RF stability, automotive readiness, medical sterilization readiness, implant suitability, dynamic robotics durability, foldable-display readiness, or harsh-environment qualification claims.

## Residual Gaps

### Highest-value next recovery lanes

1. Recover authoritative alloy-property sources for aluminum `5052 / 6061 / 1100` if alloy tables will be kept.
2. Recover additional official IMS supplier sources if drafts need supplier-neutral comparisons instead of Ventec-only examples.
3. Recover official flex-material construction sources beyond film-only pages, preferably manufacturer-controlled flex laminate / adhesiveless construction sources.
4. Recover official dynamic-flex design or reliability sources if any dynamic-flex cycle or RA-vs-ED claim is to survive.
5. Recover dated internal capability evidence before any HIL/APT factory, certification, lead-time, MOQ, or quality-rate claim is reintroduced.

### Current posture

- Aluminum / IMS / MCPCB:
  `partially_recovered_at_official_source_level`
- Flex / FPC / polyimide:
  `partially_recovered_at_official_source_level`
- Dynamic-flex / rollable / foldable:
  `still_blocked_pending_better_official_sources`
- Commercial / supplier / capability claims:
  `still_blocked_pending_dated_capability_records`

## Changed Files

- `/code/blogs/llm_wiki/logs/p4-35-2025-10-20-official-source-recovery-scout.md`
