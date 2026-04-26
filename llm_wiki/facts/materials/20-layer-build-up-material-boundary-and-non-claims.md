---
fact_id: "materials-20-layer-build-up-material-boundary-and-non-claims"
title: "Current public build-up material sources for 20-layer support material-form vocabulary and family framing, not transferable process windows or factory capability"
topic: "20-layer build-up material-form boundary and non-claims"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "ipc-jpca-4104-toc"
  - "panasonic-felios-frcc-page"
  - "panasonic-megtron-6-family-page"
  - "panasonic-megtron-6-halogen-free-page"
  - "agc-fastrise-family-page"
  - "agc-bond-plies-prepregs-page"
  - "agc-meteorwave-1000nf-page"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "ventec-vt-47lt-datasheet-page"
  - "ventec-pro-bond-4c-vt-464lt-rcc-datasheet-page"
  - "resonac-mcl-hs200-build-up-page"
  - "resonac-mcl-e700g-build-up-page"
  - "resonac-mcl-e705g-build-up-page"
  - "mitsui-rcc-engineered-materials-page"
  - "rogers-2929-bondply-datasheet"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-37n-product-page"
  - "arlon-47n-product-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
  - "isola-370hr-datasheet"
  - "ipc-validation-services-qpl-ipc-4101-page"
  - "ipc-validation-services-qpl-ipc-4103-page"
tags: ["20-layer", "build-up", "materials", "material-form", "boundary", "gap-control", "non-claims", "hdi"]
---

# Canonical Summary

> The current public material layer for `20-layer` writing is now broad enough to support guarded material-form vocabulary such as `FRCC`, `RCC`, `bond ply`, `controlled-flow prepreg`, `no-flow prepreg`, `ABF`, `BT`, `ALIVH`, `sequential lamination`, and build-up-oriented laminate families. It is still not broad enough to let evidence packs inherit process windows, stack recipes, via geometry, lamination counts, substrate-style assumptions, or factory-capability claims from those material pages.

## Stable Facts

- Panasonic `FRCC` is usable as a guarded build-up-material-form anchor, not as a default rigid-board recipe.
- `FRCC` and `RCC` are both usable as resin-coated-copper vocabulary, but the current source layer supports them as material-form language rather than as interchangeable default stack prescriptions.
- Legacy `IPC/JPCA-4104` is usable only as a historical taxonomy anchor showing that `HDI` / `microvia` materials were treated as a distinct materials-standard topic; it is not a current rule source.
- Panasonic `MEGTRON 6` family pages are usable as guarded high-speed / `HDI` / high-layer-count family-positioning anchors.
- AGC `Bond Plies / Prepregs` and `fastRise` are usable as guarded `bond ply` / `prepreg` / `nonreinforced` / `sequential lamination` material-form anchors.
- AGC `Meteorwave 1000NF` is usable as a guarded product-grade `no-flow prepreg` anchor for high-layer-count PCB context, not as a lamination or via-structure recommendation.
- Rogers `2929 Bondply` is usable as a guarded product-grade `unreinforced bondply` anchor for bonding-layer vocabulary, not as a default rigid high-layer stack prescription.
- Arlon `Controlled Flow Prepreg` is usable as application-context wording for `controlled-flow prepreg`, while official `37N` and `47N` pages add guarded product-identity anchors for low-flow prepreg families without supplying datasheet-grade process or parameter facts.
- Ventec Ultrathin is usable as a guarded manufacturer anchor for `ALIVH`, build-up-material, and sequential-lamination vocabulary.
- Ventec `VT-47LT` is usable as a guarded supplier-side anchor showing that `Any-layer HDI Designs`, `Sequential Laminations`, and `High Reliability for HDI Designs` can appear together on one material page; it does not show that those claims transfer to rigid `20-layer` board architecture, qualification, or manufacturability.
- Ventec `pro-bond 4C (VT-464LT RCC)` is usable as a guarded product-grade `RCC` / `bondply` anchor that sharpens `resin-coated copper` and `unreinforced adhesive` material-form wording without creating rigid-board stack rules.
- Mitsui `RCC` is usable as a guarded resin-coated-copper material-form anchor, not as a default rigid multilayer recipe.
- Resonac `HS200`, `E-700G`, and `E-705G` are usable as guarded laminate-family anchors for build-up-construction and `HDI`/`PWB` application language.
- Ajinomoto `ABF` and MGC `BT` remain class-level build-up anchors rather than direct evidence for ordinary rigid multilayer defaults.
- `370HR` remains a conservative rigid multilayer baseline when a `20-layer` draft needs to contrast mainstream high-Tg FR-4-family materials against more build-up-oriented families.
- IPC's public `QPL IPC-4101` page adds a guarded boundary that public qualification-listing vocabulary can attach to certified base materials and listed products/sites without qualifying a finished `20-layer` board.
- IPC's public `QPL IPC-4103` page adds a more specific guarded boundary that qualification-listing vocabulary can also attach to high-speed/high-frequency base materials and bonding-layer products/sites without qualifying a finished `20-layer` board or its signal-performance outcome.

## Conditions And Methods

- Use this card when selecting which build-up-material sources are safe to expose to prompt-side drafting for `20-layer` articles.
- Use it as a negative-control layer together with `methods-any-layer-hdi-public-boundary-for-20-layer` so that material-family pages do not silently become geometry tables.
- Use each term only at its supported level: `FRCC`, `RCC`, `bond ply`, `controlled-flow prepreg`, `no-flow prepreg`, and `ultrathin build-up material` should not be flattened into one generic prepreg bucket.
- Prefer wording like `may be framed as`, `is publicly positioned as`, `is a guarded example of`, and `belongs to a build-up-oriented family` rather than wording like `requires`, `typically uses`, or `supports up to`.
- Keep `FRCC` and `RCC` attached to material-form identity, not to dielectric-thickness, build-sequence, or via-geometry guidance.
- Keep historical `IPC/JPCA-4104` wording attached to legacy material taxonomy only, not to current active IPC requirements or current `20-layer` build-up practice.
- Keep `bond ply`, `unreinforced bondply`, and `no-flow prepreg` attached to bonding-layer vocabulary, especially where the source explicitly says `non-reinforced`, `unreinforced`, or `minimal and consistent resin flow`.
- Treat `controlled-flow prepreg` as application-context wording unless a product-grade datasheet is separately registered.
- Treat Arlon `37N` and `47N` only as low-flow prepreg product-identity anchors; do not use those product pages as substitutes for resin-flow, press-cycle, dielectric, or thickness data.
- Treat `no-flow prepreg` as stronger than `controlled-flow` here because `Meteorwave 1000NF` is a named product page with explicit `high layer count printed circuit board designs` positioning.
- Keep AGC `stacked or staggered microvias` wording attached to supplier-side material-family positioning, not to transferable `20-layer` structure or reliability claims.
- Keep Ventec `Any-layer HDI Designs`, `Sequential Laminations`, and `High Reliability for HDI Designs` wording attached to supplier-side material positioning, not to transferable `20-layer` qualification, stack architecture, or capability claims.
- Keep `VT-464LT RCC` attached to `RCC` / `bondply` / `unreinforced adhesive` identity, not to dielectric windows, lamination-count rules, or laser-via prescriptions.
- Ultrathin, `FRCC`, `RCC`, `bond ply`, `no-flow prepreg`, and `ABF` / `BT` references should be treated as boundary-setting material-form vocabulary unless a future source batch adds board-level evidence for the exact stack class being discussed.
- Keep `QPL IPC-4101` wording attached to base-material / product / site listing scope, not to finished-board qualification, interconnect qualification, or supplier approval wording.
- Keep `QPL IPC-4103` wording attached to high-speed/high-frequency base-material / bonding-layer / product / site listing scope, not to finished-board qualification, interconnect qualification, or channel-performance qualification wording.

## Limits And Non-Claims

- These sources do not prove default `RCC` thickness ranges, dielectric-thickness windows, laser-via diameters, capture-pad sizes, stacked-via heights, or lamination-cycle counts for `20-layer` builds.
- They do not prove that legacy `IPC/JPCA-4104` taxonomy still reflects current maintained IPC material guidance for present-day `20-layer` work.
- These sources do not prove that `FRCC`, `RCC`, `bond ply`, `controlled-flow prepreg`, `no-flow prepreg`, and ultrathin build-up materials are interchangeable.
- They do not prove that AGC `fastRise` or generic bond-ply / prepreg category language makes stacked or staggered microvias a default, reliable, or production-approved `20-layer` choice.
- They do not prove that AGC bond-ply language, Rogers bondply language, or Arlon controlled-flow application language creates lamination recipes, selective-fill rules, or reliability evidence for `20-layer`.
- They do not prove that Arlon `37N` or `47N` product identity creates datasheet-grade controlled-flow rules, rigid-board defaults, or process recommendations for `20-layer`.
- They do not prove that Ventec `VT-47LT` makes `any-layer HDI`, sequential lamination, or `high reliability for HDI designs` a default, validated, or production-approved rigid `20-layer` choice.
- They do not prove that Ventec `VT-464LT RCC` makes `RCC` / `bondply` a default, validated, or production-approved rigid `20-layer` choice.
- They do not prove that `RCC`-style materials, slim-substrate vocabulary, or via-creation wording from Mitsui should be treated as ordinary rigid-board defaults for `20-layer` articles.
- They do not prove that introducing `bond ply`, `no-flow prepreg`, ultrathin build-up dielectric, or `RCC` wording makes a rigid `20-layer` stack more manufacturable, more reliable, or more production-ready.
- They do not prove that package-substrate or thinner-module materials should be treated as ordinary rigid-board defaults.
- They do not prove that any supplier can manufacture `ALIVH`, any-layer `HDI`, or stacked-microvia structures at production yield.
- They do not prove that a listed `IPC-4101` base material, `Laminate Supplier Audit` entry, or `QPL` product record qualifies a finished `20-layer` board, its interconnect structure, or a supplier for customer acceptance.
- They do not prove that a listed `IPC-4103` high-speed/high-frequency base material or bonding-layer product qualifies a finished `20-layer` board, its interconnect structure, or its insertion-loss / signal-integrity performance.
- They do not let `Any-layer HDI` or related wording on a material page become a factory-capability, yield, or default-architecture claim for `20-layer` articles.
- They do not convert material-family positioning into impedance, insertion-loss, thermal-cycle, or reliability guarantees.

## Open Questions

- Decide whether `20-layer` prompt packs should explicitly exclude all manufacturer live tables unless a matching product-grade datasheet is already registered.
- Decide whether this boundary card should later be referenced directly from `P4-06` evidence-pack selection rules once that phase is unblocked.

## Source Links

- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/megtron-series/series/127603
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/megtron-series/series/127605
- https://www.agc-multimaterial.com/fastrise/
- https://www.agc-multimaterial.com/bond-plies-prepregs/
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://www.ventec-group.com/cht/products/bondply/pro-bond-4c-vt-464lt-rcc/datasheet/
- https://eu.resonac.com/project/hs200/
- https://eu.resonac.com/project/e700gr/
- https://eu.resonac.com/project/e705g/
- https://www.mitsui-kinzoku.com/en/seihin/engineered_materials/
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
