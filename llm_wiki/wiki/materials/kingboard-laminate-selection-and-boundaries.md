---
wiki_id: "wiki-materials-kingboard-laminate-selection-and-boundaries"
title: "Kingboard laminate selection and boundaries"
topic: "Kingboard laminate selection"
category: "materials"
status: "active"
reviewed_at: "2026-04-27"
fact_ids:
  - "materials-kingboard-kb-6150"
  - "materials-kingboard-kb-6160"
  - "materials-kingboard-kb-6160a"
  - "materials-kingboard-kb-6160f"
  - "materials-kingboard-kb-6160lc"
  - "materials-kingboard-kb-6160lc-c"
  - "materials-kingboard-kb-6164"
  - "materials-kingboard-kb-6165"
  - "materials-kingboard-kb-6165f"
  - "materials-kingboard-kb-6165c"
  - "materials-kingboard-kb-6165le"
  - "materials-kingboard-kb-6167f"
  - "materials-kingboard-kb-6167gmd"
  - "materials-kingboard-kb-6167gld"
  - "materials-kingboard-kb-6168le"
  - "materials-kingboard-kb-6169gt"
  - "materials-kingboard-hf-140"
  - "materials-kingboard-hf-170"
  - "materials-kingboard-kb-3200g"
  - "materials-kingboard-pi-515g"
  - "materials-kingboard-pi-520g"
  - "materials-kingboard-material-selection-boundaries"
  - "materials-kingboard-prepreg-construction-data-boundaries"
source_ids:
  - "kblaminates-kb-6150-technical-information"
  - "kblaminates-kb-6160-kb-6060-technical-information"
  - "kblaminates-kb-6160a-kb-6060a-technical-information"
  - "kblaminates-kb-6160f-kb-6060f-technical-information"
  - "kblaminates-kb-6160lc-technical-information"
  - "kblaminates-kb-6160lc-c-technical-information"
  - "kblaminates-kb-6164-kb-6064-technical-information"
  - "kblaminates-kb-6165-kb-6065-technical-information"
  - "kblaminates-kb-6165f-kb-6065f-technical-information"
  - "kblaminates-kb-6165c-kb-6065c-technical-information"
  - "kblaminates-kb-6165le-kb-6065le-technical-information"
  - "kblaminates-kb-6167f-kb-6067f-technical-information"
  - "kblaminates-kb-6167gmd-kb-6067gmd-technical-information"
  - "kblaminates-kb-6167gld-kb-6067gld-technical-information"
  - "kblaminates-kb-6168le-kb-6068le-technical-information"
  - "kblaminates-kb-6169gt-kb-6069gt-technical-information"
  - "kblaminates-hf-140-pp-hf140-technical-information"
  - "kblaminates-hf-170-pp-hf170-technical-information"
  - "kblaminates-kb-3200g-pp-kb3200g-technical-information"
  - "kblaminates-pi-515g-pp-pi515g-technical-information"
  - "kblaminates-pi-520g-pp-pi520g-technical-information"
---

# Use This Page For

- Writing or rewriting Kingboard laminate articles from `/code/blogs/tmps/en`.
- Selecting safe exact-product material facts for Kingboard FR-4, low-CTE, high-Tg, halogen-free, low-loss, and PI-series topics.
- Preventing draft-only cost, lead-time, speed, qualification, and capability claims from entering public copy.

# Covered Exact Products

- `KB-6150`
- `KB-6160`
- `KB-6160A`
- `KB-6160F`
- `KB-6160LC`
- `KB-6160LC(C)`
- `KB-6164`
- `KB-6165`
- `KB-6165F`
- `KB-6165C`
- `KB-6165LE`
- `KB-6167F`
- `KB-6167GMD`
- `KB-6167GLD`
- `KB-6168LE`
- `KB-6169GT`
- `HF-140`
- `HF-170`
- `KB-3200G`
- `PI-515G`
- `PI-520G`

# Safe Selection Language

- Use exact product names and suffixes.
- Say a product has official KBLaminates material-property coverage when its fact card exists.
- Describe broad material positioning as conventional FR-4, low-CTE FR-4, high-Tg FR-4, halogen-free laminate, low-loss digital laminate, or PI-series high-Tg laminate only when the exact product card supports it.
- Use product values only with frequency, method, condition, and specimen context where relevant.

# Unsafe Selection Language

- Do not rank the Kingboard portfolio by cost or performance unless a source explicitly supports that ranking.
- Do not map `Dk / Df` values directly to PCIe, USB, DDR, Ethernet, PAM4, or trace-length support.
- Do not claim application qualification such as automotive, aerospace, defense, medical, AEC, PPAP, or mission-critical suitability from material datasheets alone.
- Do not claim HIL/APT stocking, sourcing, lead time, quote speed, yield, or capability from KBLaminates source records.

# Prepreg And Construction Data

- Prepreg rows must keep exact prepreg family, glass style, resin content, pressed thickness, frequency, and official source attached.
- Do not average construction rows into one Kingboard or FR-4 dielectric number.
- Do not convert construction rows into stackup recipes or impedance guarantees.

# Remaining Blocked Products

No product in the original P4-25 residual list remains blocked for lack of official KBLaminates source after P4-28.

Remaining blocked claim families:

- cost ladder
- lead time
- inventory or stocking
- supplier relationship
- yield
- finished-board compliance
- application qualification
- SI/channel compliance
- insertion-loss budgets
- trace-length limits
- HIL/APT fabrication capability
- process recipes

# Blog Rewrite Implications

- `kingboard-pcb-laminate.md` can now be rewritten as a selector article, but not as a portfolio ranking or cost guide.
- Product-specific drafts can use exact values from the matching product fact card.
- Draft estimates should be deleted or replaced with source-scoped exact-product facts.
- High-speed products can discuss Dk / Df values, but channel support claims must be reframed as design-review considerations or removed.
