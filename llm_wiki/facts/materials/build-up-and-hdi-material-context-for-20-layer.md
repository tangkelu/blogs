---
fact_id: "materials-build-up-and-hdi-material-context-for-20-layer"
title: "Public build-up and HDI material sources can now support cautious 20-layer material framing without turning laminate pages into geometry rules"
topic: "build-up and HDI material context for 20-layer"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "ipc-jpca-4104-toc"
  - "ipc-board-design-standards-page"
  - "panasonic-felios-frcc-page"
  - "panasonic-megtron-6-family-page"
  - "panasonic-megtron-6-halogen-free-page"
  - "panasonic-megtron-6-r5775n"
  - "agc-fastrise-family-page"
  - "agc-bond-plies-prepregs-page"
  - "agc-n7000-3f-datasheet"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "ventec-vt-47lt-datasheet-page"
  - "ventec-pro-bond-4c-vt-464lt-rcc-datasheet-page"
  - "resonac-mcl-hs200-build-up-page"
  - "resonac-mcl-e700g-build-up-page"
  - "resonac-mcl-e705g-build-up-page"
  - "iteq-product-catalog-page"
  - "iteq-high-tg-very-low-loss-page"
  - "iteq-it-150da-page"
  - "iteq-it-968-page"
  - "iteq-it-602g-datasheet"
  - "isola-370hr-datasheet"
  - "isola-370hr-dk-df-tables"
  - "doosan-dsf-900sq-page"
  - "isola-sequential-lamination-in-pcbs-note"
  - "shengyi-s7439-processing-guide"
  - "mitsui-rcc-engineered-materials-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
tags: ["20-layer", "build-up", "hdi", "megtron-6", "iteq", "isola-370hr", "abf", "bt", "materials"]
---

# Canonical Summary

> `llm_wiki` now has enough public material-source coverage to support cautious `20-layer` material framing: `MEGTRON 6` as a public high-speed / HDI-friendly multilayer family anchor, `370HR` as a high-Tg baseline anchor, ITEQ low-loss and very-low-loss families as official supplier examples for server / backplane / `HDI` contexts, and `ABF / BT` as build-up-material class anchors. This still does not justify publishing microvia geometry tables, `RCC` thickness windows, or generic stacked-microvia capability numbers.

## Stable Facts

- Panasonic publicly positions `MEGTRON 6` as an ultra-low-loss circuit-board-material family for networking and high-speed designs and explicitly associates it with `HDI` and thermal-performance context.
- Panasonic also publicly positions the halogen-free `MEGTRON 6` family as suitable for `HDI` constructions and high-layer-count printed circuit boards in ICT and networking contexts.
- Official Panasonic model-level material records already give `MEGTRON 6` this corpus a datasheet-backed anchor for exact values when needed.
- Official AGC `Bond Plies / Prepregs` framing now gives this corpus a guarded class-level anchor for low-loss bonding-layer, prepreg, and low-fiberglass / non-reinforced material-form vocabulary in multilayer `PWB` constructions.
- Legacy `IPC/JPCA-4104` gives this corpus a historical standards-side taxonomy anchor for treating `HDI` / `microvia` materials as a distinct materials topic, but only at a historical vocabulary layer.
- Official AGC `fastRise` framing now gives this corpus a guarded supplier-side anchor for `nonreinforced prepreg`, `bonding layer`, `sequential lamination`, and `stacked or staggered microvias` vocabulary without forcing those terms into default rigid-board recipes.
- Official AGC `N7000-3F` now gives this corpus a product-grade polyimide laminate/prepreg anchor for guarded multilayer construction context and exact condition-bound values where needed.
- Ventec's official ultrathin build-up page now gives this corpus a guarded manufacturer anchor for `ALIVH`, build-up material, and sequential-lamination vocabulary.
- Ventec's official `VT-47LT` page now gives this corpus a guarded supplier-side anchor showing that `Any-layer HDI Designs`, `Sequential Laminations`, and `High Reliability for HDI Designs` can appear together on one official material page without transferring those claims to rigid `20-layer` board architecture, qualification, or manufacturability.
- Ventec's official `VT-464LT RCC` page now gives this corpus a guarded product-grade `RCC` / `bondply` anchor for `resin-coated copper` and `unreinforced adhesive` wording without turning those terms into rigid-board-default architecture.
- Resonac's official `MCL-HS200 / MCL-HS20N` page now gives this corpus a guarded laminate-family anchor that explicitly ties high-speed material positioning to build-up-construction suitability.
- Resonac's official `MCL-E-700G` and `MCL-E-705G` pages now give this corpus additional guarded laminate-family anchors that explicitly tie `HDI`/`PWB` usage to build-up-construction suitability.
- `370HR` remains a stable official high-Tg FR-4-family baseline when a `20-layer` draft needs a conservative core-material reference instead of jumping straight to low-loss marketing language.
- Official ITEQ pages now give this corpus product-existence and application anchors across high-Tg low-loss, very-low-loss, and `HDI`-adjacent laminate families including `IT-150DA`, `IT-968`, and `IT-602G`.
- Official `IT-602G` datasheet now upgrades that branch from family-level mention to product-grade `HDI` / `multiple lamination` coverage with exact condition-bound values.
- Official Doosan `DSF-900SQ` positioning now gives this corpus a guarded build-up-material anchor that explicitly combines `multiple lamination`, `HDI process`, and high-thermal-reliability application vocabulary.
- Isola's official sequential-lamination note now gives this corpus a separate supplier-side anchor for treating sequential lamination as a distinct fabrication context with explicit stress-factor and failure-mode vocabulary.
- Shengyi's official `S7439 / S7439B` processing guide now gives this corpus another mainstream supplier-side anchor that low-loss multilayer material families can carry explicit handling, lay-up, drilling, and desmear-sensitivity context beyond property tables alone.
- Panasonic's official `FRCC` page now gives this corpus a guarded public anchor for resin-coated-copper / build-up-process vocabulary without forcing that material form into ordinary rigid-board defaults.
- Mitsui's official engineered-materials page now gives this corpus a direct official `RCC` anchor by defining resin-coated copper foil as a semi-hardened resin applied on copper foil and linking that material form to slim-substrate and via-creation context.
- Isola's official `370HR` construction table now gives this corpus a safer way to discuss `370HR` property variation without collapsing it into one generic `Dk / Df`.
- Official Ajinomoto and MGC sources continue to support `ABF` and `BT` only as build-up-material class anchors, not as product-grade parameter tables.

## Conditions And Methods

- Use this card when a `20-layer` article needs to discuss material-family choices for dense, high-speed, or build-up-oriented multilayer work without pretending all `HDI` builds use one laminate recipe.
- Use the `FRCC` source only as a guarded build-up-material-form anchor; do not silently shift a standard rigid multilayer article into flex / flex-rigid assumptions.
- Use the AGC sources only as guarded `bond ply` / `prepreg` / `nonreinforced` / `sequential lamination` vocabulary anchors; do not let them silently become thickness-window, lamination-count, or generic rigid-board-default evidence.
- Use `IPC/JPCA-4104` only as a historical taxonomy anchor; do not let it silently become current maintained IPC material guidance.
- Use the `VT-47LT` source only as a guarded prepreg/material-positioning anchor for `any-layer HDI`, `sequential lamination`, and `high reliability for HDI designs`; do not let those phrases silently become default rigid-board architecture, qualification, or process-window evidence.
- Use the `VT-464LT RCC` source only as a guarded `RCC` / `bondply` material-form anchor; do not let `RCC` identity silently become dielectric-thickness, lamination-sequence, or laser-via guidance.
- Use the Mitsui page only as a guarded `RCC` material-form anchor; do not let `RCC` identity silently become dielectric-thickness, lamination-sequence, or via-geometry guidance.
- Ultrathin, `FRCC`, `RCC`, `bond ply`, `no-flow prepreg`, and `ABF` / `BT` references should be treated as boundary-setting material-form vocabulary unless a future source batch adds board-level evidence for the exact stack class being discussed.
- Use the Ventec and Resonac pages as vocabulary anchors for build-up / sequential-lamination-friendly material families, not as universal any-layer design-rule sources.
- Use the Doosan `DSF-900SQ` page only as a guarded build-up / `multiple lamination` vocabulary anchor, not as proof that a specific rigid `20-layer` stack should use non-glass build-up materials.
- Use the Isola sequential-lamination note only as a guarded process-context anchor for stress-factor and failure-mode vocabulary; do not let it silently become a stack recipe, lamination-count rule, or reliability guarantee.
- Use the Shengyi `S7439 / S7439B` processing guide only as a guarded multilayer process-sensitivity anchor for storage, lay-up orientation, drilling caution, and desmear sensitivity; do not let it silently become a bake schedule, press cycle, drill table, or default `20-layer` process window.
- Use the Resonac `E-700G / E-705G` pages as guarded examples of build-up-oriented laminate families that sit near the package-substrate / thinner-module boundary without turning that boundary into a default rigid-board assumption.
- Pair this card with the current `IPC-2226A` / microvia-reliability guardrails before discussing any-layer or stacked-microvia structures.
- Keep exact material numbers tied to the specific registered datasheet or product page, and keep geometry / reliability numbers under separate source control.
- Keep `N7000-3F` and `IT-602G` values tied to their exact datasheets rather than flattening them into generic high-layer material averages.

## Limits And Non-Claims

- This card does not prove that `20-layer` any-layer `HDI` should default to `MEGTRON 6`, `370HR`, or any ITEQ family.
- It does not prove that `N7000-3F` or `IT-602G` is the default or preferred `20-layer` material system.
- It does not provide `RCC` thickness windows, laser-via diameters, capture-pad sizes, lamination-cycle counts, or `IST` thresholds.
- It does not turn historical `IPC/JPCA-4104` taxonomy into current maintained IPC requirements for build-up materials.
- It does not turn Mitsui's `RCC` material-form wording into proof that ordinary rigid `20-layer` boards should use resin-coated copper foil or substrate-style build-up materials.
- It does not turn AGC `fastRise` or class-level bond-ply wording into proof that ordinary rigid `20-layer` boards should use non-reinforced prepreg, sequential build-up dielectric layers, or stacked/staggered microvia architectures.
- It does not turn Ventec `VT-47LT` wording into proof that `any-layer HDI`, sequential lamination, or `high reliability` is the default or validated path for a rigid `20-layer` board.
- It does not turn Ventec `VT-464LT RCC` wording into proof that `RCC` / `bondply` is the default or validated path for a rigid `20-layer` board.
- It does not prove that introducing `bond ply`, `no-flow prepreg`, ultrathin build-up dielectric, or `RCC` wording makes a rigid `20-layer` stack more manufacturable, more reliable, or more production-ready.
- It does not turn Isola's sequential-lamination note into approved cycle counts, stress budgets, or transferable process windows for `20-layer` rigid boards.
- It does not turn Shengyi's `S7439 / S7439B` processing guide into universal bake schedules, lay-up rules, drill parameters, desmear chemistry, or capability claims for `20-layer` boards.
- It does not prove that `multiple lamination` wording on a product page transfers into generic `20-layer` build architecture or reliability guarantees.
- It does not prove `ALIVH`, build-up construction, or sequential lamination is the default or recommended route for every `20-layer` design.
- It does not convert `ABF`, `BT`, or `HDI` application language into a guaranteed fabricator capability statement.

## Open Questions

- Add dedicated official `RCC` or build-up dielectric source records if a future batch needs stronger non-substrate-board evidence for any-layer `HDI` material stacks.
- Decide whether `IT-602G` or another `HDI`-oriented ITEQ grade deserves its own registered source record beyond the current family-level page.

## Source Links

- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/megtron-series/series/127603
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/megtron-series/series/127605
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/megtron-series/series/127603/model/131590
- https://www.agc-multimaterial.com/fastrise/
- https://www.agc-multimaterial.com/bond-plies-prepregs/
- https://www.agc-multimaterial.com/agc-downloads/AGC_N7000-3F_TDS.pdf
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://www.ventec-group.com/cht/products/bondply/pro-bond-4c-vt-464lt-rcc/datasheet/
- https://eu.resonac.com/project/hs200/
- https://eu.resonac.com/project/e700gr/
- https://eu.resonac.com/project/e705g/
- https://www.iteqcorp.com/product/product/?lang=en
- https://www.iteqcorp.com/product/product/high-tg-very-low-loss/?lang=en
- https://www.iteqcorp.com/product/product/high-tg-low-loss/?lang=en
- https://www.iteqcorp.com/product/product/high-tg-very-low-loss/?lang=en
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/03/W-CTE-1002-78B_Data-sheet-IT-602G.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
- https://www.doosanelectronics.com/en/product/Copper_Clad_Laminate/DSF-900SQ
- https://www.isola-group.com/wp-content/uploads/Sequential-Lamination-in-PCBs.pdf
- https://www.syst.com.cn/uploadfiles/2018/10/20181027173559031.pdf
- https://www.mitsui-kinzoku.com/en/seihin/engineered_materials/
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
