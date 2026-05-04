---
topic_id: "materials-arlon-material-family-source-governance"
title: "Arlon Material Family Source Governance"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-arlon-official-source-coverage"
  - "materials-arlon-product-page-recovery-n-series"
  - "materials-arlon-hi-rel-branch-normalization"
  - "materials-arlon-86hp-exact-product"
  - "materials-arlon-85n-exact-product"
  - "materials-arlon-85nt-exact-product"
  - "materials-arlon-55nt"
  - "materials-arlon-detailed-material-specs-recovery"
  - "materials-arlon-rf-ptfe-current-site-gap"
  - "materials-arlon-clte-xt-microwave"
  - "materials-arlon-tc350-thermal-rf"
  - "materials-arlon-ad-series-antenna"
source_ids:
  - "frontendapt-materials-arlon-pcb-page-en"
  - "arlon-products-directory"
  - "arlon-current-product-sitemap"
  - "arlon-laminate-guide"
  - "arlon-33n-product-page"
  - "arlon-35n-product-page"
  - "arlon-37n-product-page"
  - "arlon-45n-product-page"
  - "arlon-47n-product-page"
  - "arlon-84n-product-page"
  - "arlon-85n-product-page"
  - "arlon-85n-datasheet"
  - "arlon-55nt-product-page"
  - "arlon-55nt-datasheet"
  - "arlon-85nt-product-page"
  - "arlon-85nt-datasheet"
  - "arlon-86hp-product-page"
  - "arlon-86hp-datasheet"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-heavy-copper-layers-application-page"
tags: ["materials", "arlon", "agc", "polyimide", "epoxy", "ptfe", "rf", "prepreg", "source-governance", "86hp", "clte-xt", "tc350", "ad-series"]
---

# Definition

> Arlon material-family governance means treating Arlon as a real site-mentioned laminate family with a three-tier source posture: (1) official product-page + datasheet backed for N-series and 86HP; (2) internally recovered but officially unanchored for the RF/PTFE group (CLTE-XT, TC350, AD, CuClad); (3) still-blocked for external publication without source-gap pairing for all internal-only families. The current official Arlon sitemap (2026-05-02) does not expose the RF/PTFE families as live product pages.

## Why This Topic Matters

- Arlon is named in APT's public material coverage across polyimide, epoxy, Thermount, and RF/PTFE families.
- The knowledge base now has three distinct recovery tiers for Arlon: official-backed N-series, internally recovered RF/PTFE (via P4-143 APTPCB JSON), and still-blocked official datasheets for RF/PTFE.
- Prompt and blog workflows need a stable frame to distinguish which Arlon grades can be cited externally vs. which must stay internal-only.

## Routing Rules

- Route `33N`, `35N`, `45N`, `47N`, `84N`, `85N`, `55NT`, `85NT`, and `86HP` to external-use prompts only when the downstream claim is supported by the exact official product page or datasheet-backed fact card.
- Route `CLTE-XT`, `TC350`, `AD250/300/1000`, `CuClad`, `DiClad`, and `IsoClad` to internal planning only unless the prompt also carries explicit source-gap disclosure and stays inside internal evaluation posture.
- Route family-discovery prompts to the Arlon products directory and laminate guide only for naming and coverage context, not for frozen parameter extraction.
- Route any RF/PTFE exact-product publishing request back to the blocked state unless a current official Arlon/AGC-controlled product page or datasheet is already landed locally.
- Keep this page as the governance router for what can be said externally, what stays internal, and what remains blocked.

## Source Tier Map

| Tier | Families | Evidence Basis | External Use |
|------|----------|---------------|-------------|
| **Tier 1 — Official** | 33N, 35N, 45N, 47N, 84N, 85N, 55NT, 85NT, 86HP | Official product pages + datasheets at `arlonemd.com` | ✅ With datasheet citation |
| **Tier 2 — Internal** | CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad, Thermount specs | APTPCB internal JSON (P4-143) | ⚠️ Internal stackup planning only |
| **Tier 3 — Blocked** | CLTE-XT, TC350, AD, CuClad official datasheets | Not found in 2026-05-02 sitemap pass | ❌ No external publication |

## Stable Facts

- APT's Arlon page covers polyimide, epoxy, Thermount, and microwave/PTFE family language.
- Arlon's official products directory (`arlonemd.com/arlon-products/`) is a live manufacturer-controlled discovery anchor.
- The current official Arlon sitemap (2026-05-02) exposes: 33N, 35N, 37N, 45N, 45NK, 47N, 55NT, 84N, 85N, 85NT, 86HP, and non-RF ancillary families.
- **86HP** is newly recovered (P4-116): official product page (2022-11-10) and official datasheet (`86HP-v-1.6.pdf`, 2024/02 path). It is a high-performance polyimide / hi-rel branch, distinct from the older hi-rel 85N posture.
- **55NT / 85NT** have official product pages and datasheets; Thermount is aramid-reinforced, low in-plane CTE, non-glass-weave.
- **CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad** were **not** found in the current official sitemap. Their material specifications (Dk, Df, CTE, thermal) have been internally recovered via APTPCB JSON (P4-143) and are available in `arlon-detailed-material-specs-recovery` for constrained internal use.
- Arlon controlled-flow prepreg and heavy-copper application pages remain registered as official application-context anchors.
- The Arlon laminate guide supports family discovery and naming context, not as a substitute for current product datasheets.

## Engineering Boundaries

- Use Tier-1 (official-backed) product pages and datasheets for any external Dk, Df, Tg, CTE, moisture, peel-strength, or thickness claim.
- Use Tier-2 (internal-only) data from `arlon-detailed-material-specs-recovery` for internal stackup evaluation; do not publish without explicit source-gap pairing.
- Keep Tier-3 (RF/PTFE official datasheets) blocked until an Arlon/AGC-controlled URL is recovered.
- Do not treat the Arlon laminate guide as a substitute for current product datasheets.
- Treat any stocking, lead-time, manufacturing-readiness, or recommended-substitution claim as refresh-required.
- Separate `family coverage` from `manufacturing proof`: site presence plus internal JSON does not prove current production support for every grade.

## External, Internal, And Blocked Use

- External use:
  Limit to Tier-1 families with the exact official-backed fact cards and keep every numeric statement tied to that grade's current manufacturer source.
- Internal use:
  Tier-2 RF/PTFE recovery can support stackup exploration, comparison framing, and draft triage inside `llm_wiki`, but it is not public-datasheet authority.
- Blocked use:
  Tier-3 RF/PTFE official exact-product publication remains blocked until a current official Arlon/AGC-controlled page or datasheet is already landed locally.

## Blocked Claims

- supplier-capability claims
- current exact-product completeness claims
- performance guarantees
- cost, lead-time, and yield claims

## Common Misreadings

- A recovered product page is not the same as a captured datasheet; 86HP has both, but CLTE-XT has neither.
- Arlon N-series recovery does not close the RF/PTFE gap; those families require separate official datasheet authority.
- Internal APTPCB JSON values for CLTE-XT/TC350/AD/CuClad are not official Arlon/AGC datasheet values.
- The laminate guide is a discovery aid, not a source of freezable parameters.
- 86HP is a hi-rel polyimide; it is not interchangeable with the PTFE/ceramic RF families (CLTE-XT, TC350, AD).
- Thermount (55NT/85NT) is aramid-reinforced, not PTFE; do not conflate it with the RF/PTFE group.

## Must Refresh Before Publishing

- Any numeric Arlon property value (Dk, Df, CTE, Tg, thermal conductivity) for external use — verify against current official datasheet
- Any grade-to-grade comparison table that includes CLTE-XT, TC350, or AD series
- Any claim about current product availability, stocking, or lead time
- Any content relying on internal APTPCB JSON for RF/PTFE families — must pair with source-gap disclosure
- Any certification, qualification, or sector-approval statement linked to Arlon grades

## Prompt-Consumption Guidance

- Use this page first when a prompt says "Arlon" without naming whether it needs public citation, internal planning, or blocked RF/PTFE families.
- Send numeric external prompts to the exact-product cards for `85N`, `55NT`, `85NT`, `86HP`, or other official-backed N-series members.
- Send RF/PTFE prompts through `materials-arlon-rf-ptfe-current-site-gap` and `materials-arlon-laminate-family-parameters` only as governance context, not as public proof.
- If a prompt asks for "complete current Arlon family coverage," answer conservatively: the current corpus has partial official exact-product coverage plus internal-only RF/PTFE recovery, not current exact-product completeness.

## Related Facts And Source Scope

- `materials-arlon-official-source-coverage` is the master family coverage map and should anchor any statement about which Arlon branches are official-backed versus internal-only.
- `materials-arlon-rf-ptfe-current-site-gap` is blocker evidence showing the current official sitemap gap for RF/PTFE families.
- `materials-arlon-laminate-family-parameters` is internal-parameter context only and must not be elevated to public-datasheet authority.
- `materials-arlon-clte-xt-microwave`, `materials-arlon-tc350-thermal-rf`, and `materials-arlon-ad-series-antenna` remain boundary cards, not proof of current official exact-product completeness.

## Related Fact Cards

- `materials-arlon-official-source-coverage` — full coverage state map by family
- `materials-arlon-product-page-recovery-n-series` — N-series official page recovery record
- `materials-arlon-hi-rel-branch-normalization` — normalization of hi-rel branches
- `materials-arlon-86hp-exact-product` — 86HP exact-product card (official backed)
- `materials-arlon-85n-exact-product` — 85N exact-product card
- `materials-arlon-85nt-exact-product` — 85NT exact-product card
- `materials-arlon-detailed-material-specs-recovery` — CLTE-XT/TC350/AD/CuClad internal recovery
- `materials-arlon-rf-ptfe-current-site-gap` — current official blocker evidence (2026-05-02)
- `materials-arlon-clte-xt-microwave` — CLTE-XT microwave boundary card
- `materials-arlon-tc350-thermal-rf` — TC350 thermal-RF boundary card
- `materials-arlon-ad-series-antenna` — AD-series antenna boundary card

## Primary Sources

- /code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
- https://www.arlonemd.com/arlon-products/
- https://www.arlonemd.com/wp-sitemap-posts-arlon_product-1.xml
- https://www.arlonemd.com/wp-content/uploads/2020/05/Laminate-Guide.pdf
- https://www.arlonemd.com/arlon_product/33n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/35n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/37n-low-flow-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/45n-multifunctional-epoxy/
- https://www.arlonemd.com/arlon_product/47n-modified-efoxy-low-flow-prepreg/
- https://www.arlonemd.com/arlon_product/84n-filled-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/85n-high-temperature-polyimide/
- https://www.arlonemd.com/applications/controlled-flow-prepreg/
- https://www.arlonemd.com/applications/heavy-copper-layers/
