# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Pillar Page** (end-to-end hub guide) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: cover Definition → Metrics → Selection → Implementation → Mistakes → FAQ → Glossary, and become the hub page that future Query pages can link to.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) After front matter, output exactly one H1 (`# ...`) and it must match the front-matter `title` exactly.
4) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (place it right after “Key Takeaways”).
5) Include **3–6** internal links from the pool below (Markdown links, diverse anchor text).
6) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
7) Images are allowed but must be controlled (see “Image rules” below). No scripts, no canvas.
8) Do not mention search/SEO meta terms in the article.
9) Coherence rules:
   - Keep the page as a single narrative: Definition → Metrics → Selection → Implementation → Mistakes → FAQ → Glossary → Conclusion.
   - Prefer direct answers. Add a **single short bridge sentence** at the start of an H2 only when it improves flow (avoid filler).
   - Prefer specific ranges, decision criteria, and verification methods over generic advice.
10) “Don’t hallucinate” rule:
   - Do not invent factory certifications, equipment brands, or capability numbers. Use the “Capability reference” below only when relevant; otherwise say “confirm during DFM/quote”.
11) Section order (do not skip; keep this order):
   - Front matter → H1 → opening paragraph → `## Key Takeaways` → (optional Contents) → scope → metrics → selection → implementation → mistakes → FAQ → glossary → conclusion.
   - Do not jump directly into a table before the opening + Key Takeaways.

## Markdown layout rules (make it look clean)
- Use `- ` for all bullet lists (avoid `*` bullets).
- Use `1. ` for ordered lists (do not restart numbering mid-list).
- Use exactly one blank line between paragraphs/blocks; avoid double-blank “gaps”.
- Keep paragraphs short: 2–4 sentences max; prefer lists/tables for dense info.
- Do not indent list items with extra spaces (avoid `*   item` formatting).
- Tables: keep headers concise; use consistent column names and alignment.

## Acronyms & naming rules (translation-friendly)
- On first mention, expand the acronym: **Full term (ACRONYM)**. After that, use the acronym consistently.
- Use canonical casing: `PCB`, `PCBA`, `SMT`, `THT`, `DFM`, `DFA`, `SI/PI`, `EMI`, `EMC`, `AOI`, `SPI`, `ICT`, `FCT`, `BOM`, `BGA`, `QFN`, `ENIG`, `OSP`, `HASL`, `UL`, `RoHS`, `IPC`, `CTE`, `Tg`, `ESD`.
- If the keyword itself is an acronym (e.g., “SMT”), include the full expansion in the opening paragraph.

Common expansions you may use (only when relevant; do not force):
- Printed circuit board (**PCB**)
- Printed circuit board assembly (**PCBA**)
- Surface mount technology (**SMT**)
- Through-hole technology (**THT**)
- Automated optical inspection (**AOI**)
- Solder paste inspection (**SPI**)
- In-circuit test (**ICT**)
- Functional circuit test (**FCT**)
- Design for manufacturability (**DFM**)
- Design for assembly (**DFA**)
- Signal integrity / power integrity (**SI/PI**)
- Electromagnetic interference / electromagnetic compatibility (**EMI/EMC**)
- Electroless nickel immersion gold (**ENIG**)
- Organic solderability preservative (**OSP**)
- Hot air solder leveling (**HASL**)
- Bill of materials (**BOM**)

## Quantitative targets (match top-ranking page shape)
- Word count target: **1800–2600 words** (keep it complete; avoid truncated outputs).
- H2 target: **7–9 H2** (H3 allowed).
- Include **2 tables minimum** (required below).
- Include **20–50** list items total across the article.

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

## Image rules (use 0–4 total; skip if pool is empty)
- Only use image paths from the **Assets image pool** below. Do not invent paths. Do not hotlink external images.
- If you include images:
  - Pick **1 hero image** and set it in front matter `image: "/assets/img/..."`.
  - Insert the same hero image once in the body, immediately after the H1:
    `![<same as title>](/assets/img/...)`
  - Add **0–2** additional in-body images, placed near the most relevant sections (metrics/implementation/mistakes).
- Alt text rules:
  - Be descriptive and specific (what the image shows), not keyword stuffing.
  - Keep it under ~120 characters.
- If you cannot select a relevant image from the pool, leave `image: ""` and do not add images.

## Assets image pool (choose from here only; may be empty)
{{assets_image_pool}}

## Capability reference (use only when relevant; do not fabricate beyond this)
- Layer count: 1–64 layers
- Board thickness: 0.2mm–6.0mm
- Min trace/space: 3mil/3mil standard, 2mil/2mil advanced
- Min hole: 0.1mm mechanical, 0.075mm laser micro-via
- Max board size: 600mm × 1100mm
- Copper weight: 0.5oz–20oz
- Surface finishes: HASL LF, ENIG, OSP, Immersion Ag, Immersion Sn, Hard Gold
- Impedance tolerance: ±5% single-ended, ±8% differential
- Materials: FR4 (Tg135/150/170+), halogen-free, Rogers, Isola, Taconic, Megtron 6/7, Aluminum, Polyimide flex

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid stuffing): {{lsi}}

---
title: "{{keyword}}: A Practical End-to-End Guide (from basics to production)"
description: "Learn {{keyword}} from definition to production: key metrics, selection trade-offs, implementation checkpoints, and acceptance criteria."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 10
tags: {{tags}}
---

# {{keyword}}: A Practical End-to-End Guide (from basics to production)

If `image` is set in front matter, insert the hero image right below this H1 using Markdown image syntax.

Write a 2–3 sentence definition-first opening (no fluff). Then immediately write the `## Key Takeaways` section before any tables.

## Key Takeaways
Write 5–7 bullets that include:
- definition in one line
- 2–3 metrics that matter
- a common misconception
- one validation/acceptance tip
- one decision rule

<!-- COMPONENT: BlogQuickQuoteInline -->

### Contents
Optional (recommended for long pages): add 7–10 anchor links to the H2 sections below.
If you skip a TOC, keep H2 titles extremely clear and “question-like”.

## What {{keyword}} really means (scope & boundaries)
Define the concept precisely and set boundaries:
- what it covers
- what it does not cover
- typical use cases (3–5 bullets)

## Metrics that matter (how to evaluate {{keyword}})
Create a Markdown table:
`Metric | Why it matters | Typical range or influencing factors | How to measure`

Then explain 3–5 “how to interpret the metric” notes.

## How to choose {{keyword}} (selection guidance by scenario)
Provide at least 6 scenarios. For each scenario:
- Goal / constraint
- Recommended option/approach
- Trade-off

If the keyword is not a “choice”, interpret as “how to choose parameters/options within {{keyword}}”.

## Optional: Applications by industry (only when “used in / applications / industry” intent exists)
If the topic is commonly searched with “applications / used in / industry”, add a short H2 section:
- Title: `## Where {{keyword}} is used (applications and typical constraints)`
- Include a table: `Industry | Typical product | Key constraint | Why {{keyword}} fits`
- Keep examples engineering-focused (constraints + acceptance), not marketing.

## Implementation checkpoints (design to manufacturing)
Write 8–12 checkpoints. Each checkpoint must include:
- Recommendation
- Risk if ignored
- Acceptance method (how to verify)

Include at least 1 small table if it helps.

## Common mistakes (and the correct approach)
Write 6–10 items:
**Mistake → why it happens → correct approach**

## FAQ (cost, lead time, materials, testing, acceptance criteria)
Write 6–8 questions:
- At least 5 must be long-tail modifiers using `{{keyword}}` + (cost/lead time/materials/testing/acceptance criteria/DFM files).
- Each answer: 1–2 sentence direct answer + 2–4 bullets.

## References & standards (optional)
If this topic is governed by standards or common industry specs, add 3–8 bullets:
- Standard / spec name (IPC/IEC/UL, etc.) → what it covers → how it impacts the metrics/acceptance criteria above
Do not add external URLs unless they are official standards pages and you are confident they are correct.

## Glossary (key terms)
Create a Markdown table with at least 10 rows:
`Term | Meaning | Why it matters in practice`

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion (next steps)
Restate `{{keyword}}` and list what to prepare for a DFM review/quote (Gerbers/stackup/specs/test requirements/quantities). No aggressive CTA.
