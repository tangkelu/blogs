---
topic_id: "materials-taconic-material-family-source-governance"
title: "Taconic Material Family Source Governance"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-taconic-official-source-coverage-gap"
  - "materials-taconic-detailed-material-specs-recovery"
  - "taconic_ptfe_laminate_family_parameters"
  - "materials-taconic-tly-series-rf-laminate"
  - "materials-taconic-tlx-moderate-loss-ptfe"
  - "materials-taconic-tlc-economy-ptfe"
  - "materials-taconic-rf35-ceramic-ptfe"
  - "materials-taconic-cer-series-high-dk"
  - "materials-taconic-bonding-materials"
source_ids:
  - "frontendapt-taconic-pcb-json"
  - "taconic-usa-industrial-materials-homepage"
  - "taconic-divisions-page"
  - "taconic-add-rohs-weee-compliance-2022"
tags: ["materials", "taconic", "ptfe", "rf-laminate", "source-governance", "tly", "tlx", "tlc", "rf-35", "cer-10", "fastrise", "taclam"]
---

# Definition

> Taconic material-family governance means treating Taconic as a confirmed RF laminate manufacturer whose **current official public product pages are not recoverable** at this time, but whose material portfolio has been **internally recovered** via the APTPCB internal JSON source (Tier-2). All exact numeric material values must be treated as internally sourced only and must not be published externally without explicit source-gap pairing. Three source tiers apply: (1) official Taconic-controlled public anchors for division identity and compliance only; (2) internally recovered APTPCB JSON values for constrained internal use; (3) blocked claims for all official product-level and external publication contexts.

## Why This Topic Matters

- Taconic is named in APT's public material coverage and is a real RF laminate manufacturer with a documented Advanced Dielectric Division.
- The knowledge base now has two internal recovery tiers: official-controlled anchors (division + compliance only) and internally recovered material parameters (APTPCB JSON, P4-143).
- Prompt and blog workflows need a stable frame to distinguish what Taconic knowledge can be cited externally vs. what must stay internal-only.
- Without this governance page, later AI agents risk treating APTPCB internal JSON values as if they were official Taconic datasheet authority—this page prevents that misuse.

---

## Source Tier Map

| Tier | Scope | Evidence Basis | External Use |
|------|-------|---------------|-------------|
| **Tier 1 — Official (Division + Compliance)** | Division existence, Advanced Dielectric Division framing, RoHS/WEEE compliance context | Official pages at `4taconic.com` (divisions page + RoHS PDF) | ✅ Division-level framing only |
| **Tier 2 — Internal Recovery (APTPCB JSON)** | TLY, TLX, TLC, RF-35, CER-10, fastRise 27, TacLam, TF-260/290 Dk/Df/CTE/thermal values | APTPCB internal JSON `frontendapt-taconic-pcb-json` (P4-143) | ⚠️ Internal stackup planning only; no external publication |
| **Tier 3 — Blocked** | Official Taconic product pages, product-level datasheets, exact product availability, lead times, supplier capability | Not found in 2026-05-02 pass | ❌ Blocked; no external publication |

---

## Official Source Posture (Tier 1)

The following Taconic-controlled official sources are registered and usable for division-level framing only:

| Source Record | URL | Scope |
|--------------|-----|-------|
| `taconic-usa-industrial-materials-homepage` | `4taconic.com/` | Current public site posture — industrial PTFE coated fabrics, tapes, belts; **not** RF laminate |
| `taconic-divisions-page` | `4taconic.com/page/divisions-27.html` | Division-level anchor: confirms Advanced Dielectric Division exists and describes PTFE laminates/prepregs for low-loss PCBs |
| `taconic-add-rohs-weee-compliance-2022` | `4taconic.com/.../RoHS WEEE Compliance ADD 2022.pdf` | ADD compliance statement; suitable for RoHS/WEEE source anchoring only |

**Key constraint**: None of these three Tier-1 sources expose RF laminate product-level pages, datasheets, Dk/Df values, or product family parameters. They confirm that Taconic's Advanced Dielectric Division exists and that ADD materials have a current RoHS/WEEE statement, nothing more.

**Blocker note**: As of 2026-05-02, direct requests to `4taconic.com` division/search URLs resolve to the industrial-materials site posture rather than a recoverable RF laminate product-page tree. No current Taconic-controlled product-level datasheet or RF laminate product page was recovered.

---

## Internal Recovery Posture (Tier 2)

The following material series have been internally recovered via the APTPCB JSON source (`frontendapt-taconic-pcb-json`, P4-143). Values are available for **internal stackup planning only**. They must not be published externally without explicit source-gap pairing referencing `taconic-official-source-coverage-gap`.

### Family Summary

| Family | Chemistry | Dk @ 10 GHz | Df @ 10 GHz | Primary Use Case | Fact Card |
|--------|-----------|-------------|-------------|-----------------|-----------|
| **TLY / TLY-5A** | PTFE / woven E-glass | 2.17 ± 0.02 | 0.0009 | Ultra-low-loss: Ka-band, satellite LNA, EW receivers | `materials-taconic-tly-series-rf-laminate` |
| **TLX** | PTFE / woven E-glass | 2.55 ± 0.04 | 0.0019 | Moderate-loss: base-station duplexers, GPS/GNSS arrays | `materials-taconic-tlx-moderate-loss-ptfe` |
| **TLC** | PTFE / woven E-glass | 2.95 – 3.20 | 0.0020 | Economy PTFE: Wi-Fi 6/7, Bluetooth, automotive V2X | `materials-taconic-tlc-economy-ptfe` |
| **RF-30 / RF-35** | Ceramic-filled PTFE (ORCER) | 3.50 ± 0.05 | 0.0018 | Sub-6 GHz 5G, PA pallets, WLAN enterprise | `materials-taconic-rf35-ceramic-ptfe` |
| **CER-10 / 20 / 30** | High-Dk PTFE/ceramic | 10.0 ± 0.25 (CER-10) | 0.0035 | Miniaturized antennas, DRA, compact cavity filters | `materials-taconic-cer-series-high-dk` |
| **fastRise 27 / 27HF** | Low-loss thermoset prepreg | 2.72 ± 0.04 | 0.0014 | Bonding prepreg for hybrid PTFE/FR-4 multilayers | `materials-taconic-bonding-materials` |
| **TacLam** | Pure PTFE bonding film | 2.10 – 2.35 | 0.0008 | All-PTFE multilayer: satellite transponders, defense radar | `materials-taconic-bonding-materials` |
| **TF-260 / TF-290** | Thermally enhanced PTFE | 2.60 / 2.90 | 0.0015 – 0.0020 | GaN/GaAs PA boards, high-power RF transmitters | `taconic_ptfe_laminate_family_parameters` |

**Full parameter table** (with CTE, thermal conductivity, moisture absorption, processing requirements): see `taconic_ptfe_laminate_family_parameters`.

**Detailed Dk/Df, thermal, mechanical matrix** (with test methods): see `materials-taconic-detailed-material-specs-recovery`.

### Processing Requirement Shared Across All PTFE Families

All PTFE-based Taconic materials (TLY, TLX, TLC, RF-35, CER, TF series) require **plasma desmear** for reliable via metallization. This is not unique to Taconic — it is the industry standard for PTFE/ceramic-PTFE PCB processing. Standard FR-4 chemistry does not apply.

### APTPCB Internal Stock Posture (Tier-2, refresh-required)

The following series were noted as internally stocked in the APTPCB JSON at the time of P4-143 recovery. These are **refresh-required** before any external or time-sensitive use:

| Series | Noted Thickness Range | Noted Copper |
|--------|----------------------|--------------|
| RF-35 | 10 – 60 mil | 1/2 oz, 1 oz ED |
| TLY-5A | 5 – 31 mil | 1/2 oz, 1 oz ED |
| CER-10 | 20 – 40 mil | 1/2 oz, 1 oz ED |
| fastRise 27 | Bonding prepreg | — |

---

## Blocked / Hold Posture (Tier 3)

The following claim families are explicitly blocked. They must not be promoted into external content or treated as established facts.

| Blocked Claim Class | Reason |
|--------------------|--------|
| Official Taconic product-page authority | No current product-level pages recovered from `4taconic.com` in 2026-05-02 pass |
| Official Taconic datasheet values | No current Taconic-controlled product-level datasheets recovered |
| External publication of Dk/Df/thermal/CTE values | All recovered values are APTPCB internal JSON only — not official Taconic datasheet truth |
| Current product availability | Cannot be determined without current official Taconic product catalog |
| Lead times or delivery estimates | Internal stocking notes are refresh-required; no current official data |
| Supplier capability proof | No dated, independently verifiable capability record for Taconic RF laminate production |
| Any claim that Taconic RF laminate products are discontinued | Not established; absence of current public product page ≠ discontinuation |
| Comparison tables citing these values as "Taconic official" | All values are APTPCB internal recovery — must be labeled accordingly |

---

## Family Grouping and Usage Boundaries

### Loss-Performance Grouping

| Group | Families | Df Range | Suitable Frequency |
|-------|----------|---------|-------------------|
| Ultra-low loss | TLY, TLX, TacLam | 0.0008 – 0.0019 | 10 GHz+ (Ka-band, mmWave fringe) |
| Low-moderate loss | fastRise 27, TF-260/290, RF-35 | 0.0014 – 0.0020 | 3 – 30 GHz |
| Economy entry | TLC | 0.0020 | Sub-6 GHz |
| High-Dk specialty | CER-10/20/30 | 0.0035 | Sub-30 GHz miniaturized |

### Hybrid Stackup Role

- **fastRise 27**: bonding prepreg for **hybrid PTFE/FR-4** multilayers (compatible with both Taconic and Rogers RF cores)
- **TacLam**: ultra-low-loss bonding film for **all-PTFE** multilayer constructions only

### What These Values Cannot Justify

Even internally, the recovered values do **not** justify:
- Specific antenna performance predictions
- Validated RF simulation outcomes
- Manufacturing readiness statements beyond "APTPCB internal JSON notes stock"
- Guaranteed impedance at any trace width or stackup

---

## Engineering Boundaries

- Use Tier-1 (official division/compliance) for confirming Taconic's corporate identity and ADD division framing only.
- Use Tier-2 (APTPCB internal JSON) for internal material selection, stackup planning, and engineering tradeoff analysis only.
- Keep Tier-3 (official product-level datasheets and product pages) blocked until a current Taconic-controlled URL is registered.
- Treat stocking, lead-time, and manufacturing-readiness notes as refresh-required at all times.
- Do not treat the APTPCB internal JSON as a substitute for official Taconic datasheets when writing for external audiences.
- When any Taconic material value appears in an external-facing document, pair it explicitly with `taconic-official-source-coverage-gap` to disclose the source tier.

---

## Common Misreadings to Avoid

- **"APTPCB internal JSON = Taconic official datasheet"** — False. The internal JSON represents APTPCB's framing of Taconic materials; it is not Taconic-published.
- **"Absence of official product page = Taconic discontinued RF laminates"** — Not established. Absence of current public URL does not prove discontinuation.
- **"Taconic division page = product-level authority"** — False. The divisions page confirms the ADD exists; it does not publish product parameters.
- **"RF-35 Df 0.0018 vs RO4350B Df 0.0037 comparison is officially verified"** — False. The RF-35 value is from APTPCB internal JSON, not a current official Taconic datasheet; treat as internally recovered comparison only.
- **"CER-10 Dk 10.0 is a safe external claim"** — False. All recovered CER values are Tier-2 internal only.
- **"Processing requirements (plasma desmear) are Taconic-certified procedures"** — False. Plasma desmear for PTFE is industry standard practice cited in the internal JSON, not a Taconic-certified procedure statement.

---

## Must Refresh Before Publishing

- Any Dk, Df, CTE, thermal conductivity, or mechanical property for external use — require current official Taconic datasheet
- Any stocking, inventory, lead-time, or availability claim
- Any material comparison table citing Taconic values alongside official-backed competitor values
- Any claim that Taconic materials are approved for a regulated industry or qualify under a customer specification
- The official source posture check: confirm whether current `4taconic.com` still lacks accessible RF laminate product pages

---

## Relationship to Arlon Governance

Taconic and Arlon are governed under parallel structures:

| Dimension | Arlon | Taconic |
|-----------|-------|---------|
| Official Tier-1 coverage | N-series (33N–86HP) with product pages + datasheets | Division page + RoHS/WEEE PDF only |
| Internal Tier-2 recovery | CLTE-XT, TC350, AD, CuClad via APTPCB JSON | TLY, TLX, TLC, RF-35, CER, fastRise, TacLam via APTPCB JSON |
| Official RF/PTFE status | Blocked (not found in 2026-05-02 sitemap) | Blocked (no product pages in 2026-05-02 pass) |
| Governance page | `arlon-material-family-source-governance.md` | This page |

Taconic's official recovery state is **weaker** than Arlon's: Arlon has official product pages and datasheets for N-series and 86HP, while Taconic currently has no product-level official anchors at all. Both share the same RF/PTFE official block.

---

## Related Fact Cards

- `materials-taconic-official-source-coverage-gap` — official source blocker and recovery status map
- `materials-taconic-detailed-material-specs-recovery` — full Dk/Df/CTE/thermal recovery table (Tier-2 internal)
- `taconic_ptfe_laminate_family_parameters` — full parameter matrix including TF series and comparison table
- `materials-taconic-tly-series-rf-laminate` — TLY/TLY-5A individual fact card
- `materials-taconic-tlx-moderate-loss-ptfe` — TLX individual fact card
- `materials-taconic-tlc-economy-ptfe` — TLC individual fact card
- `materials-taconic-rf35-ceramic-ptfe` — RF-30/RF-35 individual fact card
- `materials-taconic-cer-series-high-dk` — CER-10/20/30 individual fact card
- `materials-taconic-bonding-materials` — fastRise 27 and TacLam bonding materials fact card

## Related Wiki Pages

- `arlon-material-family-source-governance.md` — parallel governance structure for Arlon
- `internal-material-family-coverage-and-refresh-rules.md` — broader internal material coverage governance
- `rf-material-selector-by-application-band.md` — RF material selection by frequency band

## Primary Sources

- `/code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json` (Tier-2 internal)
- `https://www.4taconic.com/` (Tier-1 official — industrial site posture only)
- `https://www.4taconic.com/page/divisions-27.html` (Tier-1 official — division anchor)
- `https://www.4taconic.com/uploads/Corporate%20Documents/1646170073_RoHS%20WEEE%20Compliance%20ADD%202022.pdf` (Tier-1 official — ADD compliance)
