---
title: "P4-42 Kingboard material blog official-source recovery scout"
lane: "P4-42 official-source recovery scout"
status: "source_backed_fact_layer_partial"
reviewed_at: "2026-04-28"
input_dir: "/code/blogs/tmps/2026.2.25/en"
output_path: "/code/blogs/llm_wiki/logs/p4-42-2026-2-25-kingboard-material-blog-official-source-recovery-scout.md"
---

# Purpose

Create a deletion-safe scout log for `/code/blogs/tmps/2026.2.25/en` focused on Kingboard laminate/material blog drafts. Drafts were treated as claim inventory only, not as authority.

# Input File Inventory

- `hf-140-hf-170-pcb.md`
- `kb-3200g-pcb.md`
- `kb-6150-pcb.md`
- `kb-6160-pcb.md`
- `kb-6160a-pcb.md`
- `kb-6160f-kb-6160lc-pcb.md`
- `kb-6164-pcb.md`
- `kb-6165-pcb.md`
- `kb-6165c-kb-6165le-pcb.md`
- `kb-6165f-pcb.md`
- `kb-6167f-pcb.md`
- `kb-6167gld-pcb.md`
- `kb-6167gmd-pcb.md`
- `kb-6168le-pcb.md`
- `kb-6169gt-pcb.md`
- `kingboard-pcb-laminate.md`
- `pi-515g-pi-520g-pcb.md`

# Topic / Heading Inventory

- Exact-product FR-4 baseline drafts: `KB-6150`, `KB-6160`, `KB-6160A`
- Exact-product modified / low-CTE FR-4 drafts: `KB-6160F`, `KB-6160LC`, `KB-6164`, `KB-6165`, `KB-6165F`, `KB-6165C`, `KB-6165LE`, `KB-6168LE`
- High-Tg / halogen-free / low-loss exact-product drafts: `KB-6167F`, `HF-140`, `HF-170`, `KB-6167GMD`, `KB-6167GLD`, `KB-6169GT`, `KB-3200G`, `PI-515G`, `PI-520G`
- Portfolio selector draft: `kingboard-pcb-laminate.md`

# Existing llm_wiki Support Checked

## Kingboard topic aggregation

- `wiki-materials-kingboard-laminate-selection-and-boundaries`
  - Path: `/code/blogs/llm_wiki/wiki/materials/kingboard-laminate-selection-and-boundaries.md`
  - Status: `source_backed_fact_layer_partial`
  - Scope: exact-product coverage plus selector and boundary guidance

## Boundary fact support

- `materials-kingboard-material-selection-boundaries`
  - Path: `/code/blogs/llm_wiki/facts/materials/kingboard-material-selection-boundaries.md`
  - Status: `source_backed_fact_layer_partial`
  - Scope: safe grouping language and blocked-claim hygiene
- `materials-kingboard-prepreg-construction-data-boundaries`
  - Path: `/code/blogs/llm_wiki/facts/materials/kingboard-prepreg-construction-data-boundaries.md`
  - Status: `source_backed_fact_layer_partial`
  - Scope: exact prepreg/construction-row use limits

## Exact-product fact cards present

- `materials-kingboard-kb-6150`
- `materials-kingboard-kb-6160`
- `materials-kingboard-kb-6160a`
- `materials-kingboard-kb-6160f`
- `materials-kingboard-kb-6160lc`
- `materials-kingboard-kb-6160lc-c`
- `materials-kingboard-kb-6164`
- `materials-kingboard-kb-6165`
- `materials-kingboard-kb-6165f`
- `materials-kingboard-kb-6165c`
- `materials-kingboard-kb-6165le`
- `materials-kingboard-kb-6167f`
- `materials-kingboard-kb-6167gmd`
- `materials-kingboard-kb-6167gld`
- `materials-kingboard-kb-6168le`
- `materials-kingboard-kb-6169gt`
- `materials-kingboard-hf-140`
- `materials-kingboard-hf-170`
- `materials-kingboard-kb-3200g`
- `materials-kingboard-pi-515g`
- `materials-kingboard-pi-520g`

## Exact-product source records present

- `kblaminates-kb-6150-technical-information`
- `kblaminates-kb-6160-kb-6060-technical-information`
- `kblaminates-kb-6160a-kb-6060a-technical-information`
- `kblaminates-kb-6160f-kb-6060f-technical-information`
- `kblaminates-kb-6160lc-technical-information`
- `kblaminates-kb-6160lc-c-technical-information`
- `kblaminates-kb-6164-kb-6064-technical-information`
- `kblaminates-kb-6165-kb-6065-technical-information`
- `kblaminates-kb-6165f-kb-6065f-technical-information`
- `kblaminates-kb-6165c-kb-6065c-technical-information`
- `kblaminates-kb-6165le-kb-6065le-technical-information`
- `kblaminates-kb-6167f-kb-6067f-technical-information`
- `kblaminates-kb-6167gmd-kb-6067gmd-technical-information`
- `kblaminates-kb-6167gld-kb-6067gld-technical-information`
- `kblaminates-kb-6168le-kb-6068le-technical-information`
- `kblaminates-kb-6169gt-kb-6069gt-technical-information`
- `kblaminates-hf-140-pp-hf140-technical-information`
- `kblaminates-hf-170-pp-hf170-technical-information`
- `kblaminates-kb-3200g-pp-kb3200g-technical-information`
- `kblaminates-pi-515g-pp-pi515g-technical-information`
- `kblaminates-pi-520g-pp-pi520g-technical-information`

# Coverage Assessment

- Exact-product official-source recovery for the named Kingboard materials is already present in `llm_wiki`.
- This lane does not need new source records or fact cards to preserve the current batch at claim-family level.
- The batch is not a fully open rewrite lane because many drafts contain unsafely promoted ranking, pricing, interface-speed, qualification, capability, or application claims that exceed current source support.

# Per-Draft / Claim-Family Disposition

## `completed_at_claim_family_level`

- `kb-6150-pcb.md`
  - Reusable lane: exact-product identity and source-backed material facts can be rebuilt from `materials-kingboard-kb-6150`
  - Blocked lane: draft cost-position language, BOM optimization claims, layer-count/process-limit guidance
- `kb-6160-pcb.md`
  - Reusable lane: exact-product material facts and paired prepreg existence
  - Blocked lane: “global standard” framing, production-capability language, generalized multilayer/process claims
- `kb-6160a-pcb.md`
  - Reusable lane: exact-product identity and source-backed material facts
  - Blocked lane: yield/volume positioning and unsupported manufacturing optimization claims
- `kb-6160f-kb-6160lc-pcb.md`
  - Reusable lane: exact-product comparison only if suffixes stay exact and product cards stay separate
  - Blocked lane: overgeneralized “same family means same performance” or merged construction behavior
- `kb-6164-pcb.md`
  - Reusable lane: exact-product material facts and low-CTE/high-reliability positioning within source scope
  - Blocked lane: reliability outcome guarantees, specific application qualification, supplier capability promises
- `kb-6165-pcb.md`
  - Reusable lane: exact-product material facts and mid-Tg positioning
  - Blocked lane: “performance center” ranking, design-rule or process-window claims
- `kb-6165f-pcb.md`
  - Reusable lane: exact-product material facts
  - Blocked lane: unsupported fabrication reliability promises or process recipes
- `kb-6165c-kb-6165le-pcb.md`
  - Reusable lane: exact-product identity separation and source-backed product-level comparison
  - Blocked lane: portfolio ranking, via-reliability guarantee, halogen-free/compliance inheritance beyond source scope
- `kb-6167f-pcb.md`
  - Reusable lane: exact-product material facts and high-Tg/low-CTE positioning
  - Blocked lane: automotive/aerospace/mission-critical qualification or finished-board compliance claims
- `kb-6167gmd-pcb.md`
  - Reusable lane: exact-product low-loss material facts
  - Blocked lane: interface-speed support, server-board suitability, SI/channel margin conclusions
- `kb-6167gld-pcb.md`
  - Reusable lane: exact-product low-loss material facts
  - Blocked lane: 25G/56G design promises, ranking against outside brands, quote/capacity claims
- `kb-6168le-pcb.md`
  - Reusable lane: exact-product high-Tg/low-CTE facts
  - Blocked lane: “maximum via reliability” as an outcome guarantee and unsupported layer-count ceilings
- `hf-140-hf-170-pcb.md`
  - Reusable lane: exact-product halogen-free fact support exists for both products
  - Blocked lane: draft environmental/legal interpretation, OEM adoption assertions, application qualification and comparative performance claims
- `kb-3200g-pcb.md`
  - Reusable lane: exact-product low-loss halogen-free material facts
  - Blocked lane: “world’s largest manufacturer” marketing carryover, cost-security claims, 10G/25G/HPC suitability conclusions, Megtron-tier mapping
- `kb-6169gt-pcb.md`
  - Reusable lane: exact-product identity and source-backed material card exist
  - Blocked lane: the draft explicitly self-flags unsourced estimated values; PAM4/channel/insertion-loss/copper-foil mandates remain blocked pending stricter official support
- `pi-515g-pi-520g-pcb.md`
  - Reusable lane: exact-product fact support exists for both products; draft pairing can be rebuilt without letting `PI-520G` stand in for `PI-515G`
  - Blocked lane: “extreme reliability” outcome claims, application qualification, traditional-polyimide equivalence, and cost-delta language
- `kingboard-pcb-laminate.md`
  - Reusable lane: selector framing via the Kingboard wiki and boundary cards
  - Blocked lane: tier tables that map data rate directly to laminate choice, cost ladder, portfolio ranking, speed-to-material prescriptions, and unsupported mentions such as unrecovered `KB-6165G`

# Safe Reuse Classes

- Exact product identity, suffix, and family naming
- Source-backed exact-product laminate facts from existing Kingboard fact cards
- Source-backed existence of paired prepreg systems when exact source/product pairing is preserved
- Portfolio grouping language already normalized in `materials-kingboard-material-selection-boundaries`
- Selector/containment language from `wiki-materials-kingboard-laminate-selection-and-boundaries`
- Construction-table existence statements when exact prepreg family, glass style, resin content, pressed thickness, frequency, and source remain attached

# Blocked Claim Classes

- Cost ladders, lowest-cost claims, pricing, MOQ, quote-speed, sourcing advantage
- Lead time, stock, inventory, capacity assurance, supplier relationship, “world’s largest means availability”
- Yield, quality rate, reliability outcome guarantees, or defect-rate language
- HIL/APT fabrication capability, stocking, process recipes, lamination cycles, impedance guarantees, or manufacturing-window promises
- Direct signal-speed/interface compliance mapping such as `PCIe`, `USB`, `DDR`, `Ethernet`, `25G NRZ`, `56G PAM4`, `112G PAM4`
- Insertion-loss budgets, trace-length budgets, copper-foil mandates unless separately source-backed
- Automotive, aerospace, defense, medical, AEC, PPAP, finished-board compliance, or legal/IP conclusions
- Environmental/legal conclusion language extrapolated from halogen-free or standards references
- Cross-product inheritance where one Kingboard grade is used to validate another

# Official-Source Gaps

## `blocked_pending_official_source`

- Public official support for any draft claim that maps material numbers directly to interface-speed ceilings, channel compliance, insertion-loss budgets, or trace-length limits
- Public official support for comparative rankings across Kingboard products or versus external brands
- Public official support for environmental/regulatory conclusion language that goes beyond product-side halogen-free or slash-sheet identification

## `blocked_pending_dated_capability_record`

- APT/HIL stocking, sourcing, MOQ, capacity, lead-time, fabrication-capability, quick-turn, and process-control claims
- Any supplier-specific ordering or fulfillment promises in “How to order” sections
- Any manufacturing capability claims tied to advanced stackups, via reliability outcomes, or production scaling

# Remaining Gaps / Recovery Notes

- `kingboard-pcb-laminate.md` still needs selector-table cleanup because the draft mixes supported exact-product identities with unsupported speed, cost, and missing-product claims.
- `kb-6169gt-pcb.md` is the highest-risk exact-product draft because it contains explicit estimated numeric language and aggressive high-speed application framing despite an existing official source record.
- The batch already has strong exact-product official-source coverage; the main remaining work is rewrite governance, not source discovery.

# Recommended Next Recovery Lanes

- Rewrite lane for `kingboard-pcb-laminate.md` using only the Kingboard wiki plus boundary fact cards
- High-risk rewrite lane for `kb-6169gt-pcb.md` to remove estimated and channel-budget claims
- High-speed-claims containment lane across `kb-6167gmd`, `kb-6167gld`, `kb-3200g`, and `kb-6169gt`
- Supplier-capability evidence lane only if dated APT/HIL records are explicitly authorized for recovery

# Lane Status

- Batch status: `source_backed_fact_layer_partial`
- Official-source recovery status for exact named Kingboard materials: `completed_at_claim_family_level`
- Residual blocker status for pricing/capability/speed/qualification claims: `blocked_pending_official_source` and `blocked_pending_dated_capability_record`

# Notes

- No tracker files were updated in this lane.
- No reusable fact cards or source records were created in this lane.
- The superpowers bootstrap command referenced by `AGENTS.md` was unavailable at `/root/.codex/superpowers/.codex/superpowers-codex`; lane execution proceeded with the available local `llm-wiki-workflow` instructions.
