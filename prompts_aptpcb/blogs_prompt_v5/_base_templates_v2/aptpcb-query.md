# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Query Page** (problem-solving landing page) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: match real search intent (what/how/specs/troubleshooting/cost/lead time) and help an engineer take action, while naturally guiding to a quote/DFM request.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) After front matter, output exactly one H1 (`# ...`) and it must match the front-matter `title` exactly.
4) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (place it in the “Request a quote” section right before the conclusion).
5) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
6) Images are allowed but must be controlled (see “Image rules” below). No scripts, no canvas.
7) Do not mention search/SEO meta terms in the article (e.g., “SERP”, “People Also Ask”, “internal links required”).
8) Coherence rules:
   - Every section must directly solve `{{keyword}}`; remove anything that doesn’t.
   - Prefer direct answers. Add a **single short bridge sentence** at the start of an H2 only when it improves flow (avoid filler).
   - Use concrete rules, ranges, decision criteria, and acceptance checks whenever possible.
9) Heading rules:
   - Headings must read like user intent (definition/specs/steps/troubleshooting/cost/lead time).
   - Avoid self-referential headings (e.g., “what this guide covers”) and generic filler (e.g., “Everything you need to know”).
   - If `{{keyword}}` contains “vs” / “versus”, include an H2 that contains “How to choose …” and add a comparison table in “Rules & specifications”.
10) “Don’t hallucinate” rule:
   - Do not invent factory certifications, equipment brands, or capability numbers. If you need capabilities, only use the “Capability reference” below; otherwise phrase as “confirm during DFM/quote”.
11) Section order (do not skip; keep this order):
   - Front matter → H1 → opening paragraph → `## Quick Answer` → Highlights → (optional Contents) → definition → rules table → steps → troubleshooting → how to choose → (optional manufacturing) → FAQ → related resources → glossary → quote → conclusion.
   - Do not jump directly into a table before the opening + Quick Answer.

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
- Word count target: **1500–2200 words** (keep it complete; avoid truncated outputs).
- H2 target: **6–8 H2** (H3 is allowed).
- Include at least **1 table** (required below).
- Include **15–40** list items total across the article (steps/checklists/bullets).

## Internal link rules (use 3–6)
- Choose **3–6** URLs from the internal link pool below.
- Use **descriptive, varied anchor text** (do not reuse the same anchor text).
- Place at least **2** links mid-paragraph (contextual), not all in one section.
- Do not paste the internal link pool list into the article. Only include the links you actually use.

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

## Image rules (use 0–4 total; skip if pool is empty)
- Only use image paths from the **Assets image pool** below. Do not invent paths. Do not hotlink external images.
- If you include images:
  - Pick **1 hero image** and set it in front matter `image: "/assets/img/..."`.
  - Insert the same hero image once in the body, immediately after the H1:
    `![<same as title>](/assets/img/...)`
  - Add **0–2** additional in-body images, placed near the most relevant sections (e.g., “rules & specifications”, “implementation steps”, “troubleshooting”).
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
- Certifications (only mention if needed): ISO 9001, ISO 14001, IATF 16949, UL E-listed, IPC-6012 Class 2/3, IPC-A-600 Class 2/3
- Lead times: Prototype 24–72 hrs, Small batch 5–7 days, Production 10–15 days
- MOQ: No minimum for prototype, 5+ pcs for production

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid stuffing): {{lsi}}

---
title: "{{keyword}}: Practical Rules, Specs, and Troubleshooting Guide"
description: "A practical guide to {{keyword}} with clear rules, recommended ranges, verification steps, and common failure fixes."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

# {{keyword}}: Practical Rules, Specs, and Troubleshooting Guide

If `image` is set in front matter, insert the hero image right below this H1 using Markdown image syntax.

Write a 2–3 sentence answer-first opening:
- Sentence 1: definition in plain English.
- Sentence 2: why it matters / when it matters.
- Sentence 3 (optional): what the reader will be able to do after reading.

## Quick Answer (30 seconds)
Write 5–7 bullets that include:
- one rule/range
- one common pitfall
- one verification method
- one boundary/exception case
- one “what to send for DFM/quote” item

Then add a short skimmable list titled **“Highlights”** (5–7 bullets). Do not use an H2 for this list. Use `- ` bullets.

### Contents
Optional (recommended for long pages): add 6–10 anchor links to the H2 sections below.
If you skip a TOC, keep H2 titles extremely clear and “question-like”.

## {{keyword}}: definition and scope (what it is, what it isn’t)
Include:
- 3–5 bullets: “applies when…”
- 3–5 bullets: “doesn’t apply when…”

## {{keyword}} rules and specifications (key parameters and limits)
Create a Markdown table with columns:
`Rule | Recommended value/range | Why it matters | How to verify | If ignored`

Requirements:
- At least 8 rows.
- Include at least 2 rows that mention verification/acceptance criteria.
- If this is a “vs” keyword, include 1 mini comparison row per key factor (cost/lead time/performance/reliability).

## {{keyword}} implementation steps (process checkpoints)
Write 6–10 steps. Each step must include:
- Action
- Key parameter(s)
- Acceptance check (how you know the step is “done”)

## {{keyword}} troubleshooting (failure modes and fixes)
Write 6–10 items. Each item must follow:
**Symptom → likely causes → checks → fix → prevention**

## How to choose {{keyword}} (design decisions and trade-offs)
Write 6–10 decision rules:
**If X matters most, choose Y; otherwise choose Z (trade-off).**
If the keyword is not a choice, reinterpret this as “how to choose the right parameters/options for {{keyword}}”.

## Optional: manufacturing & ordering notes (only if the intent is transactional)
If the query intent includes any of these cues: `manufacturer`, `manufacturing`, `factory`, `service`, `quote`, `MOQ`, `lead time`, `turnaround`, `cost`:
- Add an H2 section titled: `## {{keyword}} manufacturing capability and ordering notes`
- Include a compact table: `Order type | Typical lead time | Key drivers | What to confirm`
- Add a bullet list: “What to send for a DFM/quote” (6–10 bullets). Keep it factual and non-hype.

## {{keyword}} FAQ (cost, lead time, materials, testing, acceptance criteria)
Write 8–10 questions. Each answer must have:
- 1–2 sentence direct answer
- 2–4 bullets with specifics

At least 6 questions must be long-tail modifiers like:
- `{{keyword}} cost`
- `{{keyword}} lead time`
- `{{keyword}} materials`
- `{{keyword}} testing`
- `{{keyword}} acceptance criteria`
- `{{keyword}} DFM files`

## Related pages & tools (internal resources)
Add 3–6 internal links (from the pool) with 1-sentence “why this helps”.
Do not cluster all internal links here—ensure at least 2 links were used earlier in context.

## References & standards (optional)
If this topic is governed by standards or common industry specs, add 3–8 bullets:
- Standard / spec name (e.g., IPC/IEC/UL) → what it covers → how it affects `{{keyword}}` decisions
Do not add external URLs unless they are official standards pages and you are confident they are correct.

## {{keyword}} glossary (key terms)
Create a Markdown table with at least 8 rows:
`Term | Meaning | Why it matters in practice`

## Request a quote for {{keyword}} (DFM review + pricing)
<!-- COMPONENT: BlogQuickQuoteInline -->

Write 1 short paragraph to set expectations (DFM + pricing).
Then list what to send (6–10 bullets), such as:
- Gerbers / ODB++ / IPC-2581 (if available)
- Stackup + impedance targets (if applicable)
- Fab drawing + tolerances
- Assembly inputs (BOM, centroid) if relevant
- Quantity (proto + production) and target lead time
- Test requirements and acceptance criteria

## Conclusion (next steps)
Restate `{{keyword}}` in 2–4 sentences and summarize what to do next. No aggressive CTA.
