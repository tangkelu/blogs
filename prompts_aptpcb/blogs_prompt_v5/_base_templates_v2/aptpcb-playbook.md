# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Buyer Playbook** for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: help an engineer/procurement lead make a safe decision (specs → risks → validation → supplier checklist) with practical, actionable steps, while naturally guiding to a quote/DFM request.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) After front matter, output exactly one H1 (`# ...`) and it must match the front-matter `title` exactly.
4) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right before the conclusion, after the RFQ/quote section).
5) Include **3–6** internal links from the pool below (Markdown links, diverse anchor text).
6) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
7) Images are allowed but must be controlled (see “Image rules” below). No scripts, no canvas.
8) Do not mention search/SEO meta terms in the article.
9) Coherence rules:
   - Every section must support solving `{{keyword}}` as a buyer/decision-maker.
   - Prefer direct answers. Add a **single short bridge sentence** at the start of an H2 only when it improves flow (avoid filler).
   - Prefer checklists, acceptance criteria, and risk controls over generic advice.
10) “Don’t hallucinate” rule:
   - Do not invent factory certifications, equipment brands, or capability numbers. Use the “Capability reference” below only when relevant; otherwise say “confirm during DFM/quote”.
11) Section order (do not skip; keep this order):
   - Front matter → H1 → opening paragraph → Highlights → (optional Contents) → scope/success criteria → specs upfront → risks → validation → supplier checklist → decision rules → FAQ → quote section → conclusion.
   - Do not jump directly into a table before the opening + Highlights.

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
- Word count target: **1700–2500 words** (keep it complete; avoid truncated outputs).
- H2 target: **7–9 H2** (H3 allowed).
- Include at least **1 table** (recommended in validation/specs).
- Include **20–50** list items total (checklists/steps/risk bullets).

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

## Image rules (use 0–4 total; skip if pool is empty)
- Only use image paths from the **Assets image pool** below. Do not invent paths. Do not hotlink external images.
- If you include images:
  - Pick **1 hero image** and set it in front matter `image: "/assets/img/..."`.
  - Insert the same hero image once in the body, immediately after the H1:
    `![<same as title>](/assets/img/...)`
  - Add **0–2** additional in-body images, placed near the most relevant sections (specs/validation/risks).
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
- Lead times: Prototype 24–72 hrs, Small batch 5–7 days, Production 10–15 days

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid stuffing): {{lsi}}

---
title: "{{keyword}}: Buyer-Friendly Playbook (Specs, Risks, Checklist)"
description: "A practical playbook for {{keyword}}: requirements to define upfront, key risks, validation plan, and a supplier qualification checklist."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 10
tags: {{tags}}
---

# {{keyword}}: Buyer-Friendly Playbook (Specs, Risks, Checklist)

If `image` is set in front matter, insert the hero image right below this H1 using Markdown image syntax.

Write a 2–3 sentence definition-first opening framed as a buyer decision. Then add **Highlights** (5–7 bullets). Do not use an H2 for Highlights. Use `- ` bullets.

### Contents
Optional (recommended for long pages): add 7–10 anchor links to the H2 sections below.
If you skip a TOC, keep H2 titles extremely clear and “question-like”.

## {{keyword}}: scope, decision context, and success criteria
Define:
- what “success” looks like (3–5 bullets)
- what decisions must be made (3–5 bullets)

## Specifications to define upfront (before you commit)
Provide 10–14 bullets grouped by:
- electrical/performance
- mechanical/environment
- manufacturing/quality
- documentation/deliverables

If relevant, include a small table: `Spec | Recommended range | Why it matters | How to validate`.

## Key risks (root causes, early detection, prevention)
Provide 8–12 items. Each item must include:
- Risk
- Root cause
- Early detection
- Prevention/control

## Validation & acceptance (tests and pass criteria)
Provide 8–12 validation steps. Each step includes:
- Objective
- Method
- Acceptance criteria (what “pass” means)

## Supplier qualification checklist (RFQ, audit, traceability)
Provide a buyer-ready checklist grouped into:
- RFQ inputs (8–12 bullets)
- Capability proof (6–10 bullets)
- Quality system & traceability (6–10 bullets)
- Change control & delivery (6–10 bullets)

## How to choose {{keyword}} (trade-offs and decision rules)
Write 6–10 decision rules:
**If you prioritize X, choose Y; otherwise choose Z.**
If the keyword is not a choice, interpret as “how to choose the right options/parameters for {{keyword}}”.

## Optional: side-by-side comparison (only if the keyword is “X vs Y”)
If `{{keyword}}` contains `vs` / `versus`:
- Add a short comparison H2 section titled: `## {{keyword}} (key differences in practice)`
- Include a table: `Factor | Option A | Option B | Best when | Trade-off`
- Follow with 5–8 “If…, choose…” decision rules (do not claim one option is always better).

## FAQ (cost, lead time, DFM files, materials, testing)
Write 6–8 questions; each answer: 1–2 sentence direct answer + 2–4 bullets.
At least 5 questions must be long-tail modifiers using `{{keyword}}` + (cost/lead time/materials/testing/DFM files/acceptance criteria).

## References & standards (optional)
If the buyer decision depends on standards/compliance, add 3–8 bullets:
- Standard / spec name (IPC/IEC/UL, etc.) → what to request from the supplier → what evidence proves compliance
Do not add external URLs unless they are official standards pages and you are confident they are correct.

## Request a quote / DFM review for {{keyword}} (what to send)
Write 1 short paragraph to set expectations (DFM + pricing).
Then list what to send (8–12 bullets), such as:
- Gerbers / ODB++ / IPC-2581
- Stackup + impedance targets
- Fab drawing + tolerances + special notes
- Quantity (proto + production) + target lead time
- Test plan + acceptance criteria
- Assembly inputs (BOM, centroid) if relevant

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion (next steps)
Restate `{{keyword}}` in 2–4 sentences and summarize next steps. No aggressive CTA.
