# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Query Page v3** (problem-solving landing page) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: match real search intent (what/how/specs/troubleshooting/cost/lead time) and help an engineer take action, while naturally guiding to a quote/DFM request.

## v3 layout boosters (must follow)
1) Start with a short narrative hook: a real engineering/buyer scenario in 1–2 sentences, then define `{{keyword}}` in plain English.
2) Add a compact **Tech / Decision Lever → Practical Impact** matrix near the top (styled HTML table block, 6–8 rows).
   - Use it to connect technical choices to outcomes (yield, reliability, lead time, cost, test coverage).
   - Keep the table factual; do not invent certifications/equipment. Prefer “confirm during DFM/quote”.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) After front matter, output exactly one H1 (`# ...`) and it must match the front-matter `title` exactly.
4) Include at least once: `<!-- COMPONENT: BlogQuickQuoteInline -->` (place it in the “Request a quote” section right before the conclusion).
5) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
6) Images are allowed but must be controlled (see “Image rules” below). No scripts, no canvas.
7) Do not mention search/SEO meta terms in the article (e.g., “SERP”, “People Also Ask”, “internal links required”).
8) Coherence rules:
   - Every section must directly solve `{{keyword}}`; remove anything that doesn’t.
   - Prefer direct answers. Add a **single short bridge sentence** at the start of an H2 only when it improves flow (avoid filler).
   - Use concrete rules, ranges, decision criteria, and acceptance checks whenever possible.
9) Heading rules:
   - Headings must read like user intent (definition/specs/steps/troubleshooting/cost/lead time).
   - Avoid self-referential headings and generic filler.
10) “Don’t hallucinate” rule:
   - Do not invent factory certifications, equipment brands, or capability numbers. If you need capabilities, only use the “Capability reference” below; otherwise phrase as “confirm during DFM/quote”.
11) Section order (do not skip; keep this order):
   - Front matter → H1 → opening paragraph → `## Quick Answer` → Highlights → v3 matrix block → (optional Contents) → definition → rules table → steps → troubleshooting → how to choose → (optional manufacturing) → FAQ → related resources → glossary → quote → conclusion.
   - Do not jump directly into a table before the opening + Quick Answer.

## Internal link pool (choose 6–10, do not output this list)
{{internal_link_pool}}

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

Write a 2–3 sentence answer-first opening (start with a scenario hook, then definition, then why it matters).

## Quick Answer (30 seconds)
Write 5–7 bullets that include: one rule/range, one pitfall, one verification method, one boundary case, one DFM/RFQ item.

Then add **Highlights** (5–7 bullets). Do not use an H2 for this list.

Now add the v3 matrix block (no H2). Use this format:
Replace all `...` placeholders with real content (no ellipsis in final output).

<div style="background-color:#F5F7FA;padding:18px;border-radius:10px;margin:20px 0;">
<h3 style="margin:0 0 12px 0;color:#000000;">Tech / Decision Lever → Practical Impact</h3>
<table style="width:100%;border-collapse:collapse;text-align:left;color:#000000;">
<thead style="background-color:#F0F0F0;">
<tr>
<th style="padding:10px;border:1px solid #ddd;">Decision lever</th>
<th style="padding:10px;border:1px solid #ddd;">Practical impact (what changes)</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:10px;border:1px solid #ddd;">...</td><td style="padding:10px;border:1px solid #ddd;">...</td></tr>
</tbody>
</table>
</div>

### Contents
Optional: add 6–10 anchor links to the H2 sections below.

## {{keyword}}: definition and scope (what it is, what it isn’t)

## {{keyword}} rules and specifications (key parameters and limits)
Create a Markdown table: `Rule | Recommended value/range | Why it matters | How to verify | If ignored` (>= 8 rows).

## {{keyword}} implementation steps (process checkpoints)

## {{keyword}} troubleshooting (failure modes and fixes)

## How to choose {{keyword}} (design decisions and trade-offs)

## {{keyword}} FAQ (cost, lead time, materials, testing, acceptance criteria)

## Related pages & tools (internal resources)

## {{keyword}} glossary (key terms)

## Request a quote for {{keyword}} (DFM review + pricing)
<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion (next steps)
