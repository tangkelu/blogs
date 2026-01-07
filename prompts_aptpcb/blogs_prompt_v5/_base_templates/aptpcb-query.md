# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English problem-solving landing page** (Query Page) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: match real search intent (how to / specs / checklist / troubleshooting / vs / cost / lead time) and help an engineer take action, while naturally guiding to a quote/DFM request.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right before the conclusion, after the quote/DFM request section).
4) Include **at least 3** internal links from the pool below (Markdown links, diverse anchor text).
5) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
6) No images, no scripts, no canvas.
7) Do not mention search/SEO meta terms in the article (e.g., “SERP”, “People Also Ask”, “you might be searching for”, “internal links required”).
8) Coherence rules:
   - Every section must directly support solving `{{keyword}}`; remove anything that doesn’t.
   - Each H2 must start with 1 sentence that connects to the previous section (no “random topic jumps”).
   - Prefer fewer, more consistent examples over many unrelated examples.
9) Heading rules (H2/H3):
   - Headings must read like the user’s question and directly answer it (how-to/specs/troubleshooting/cost/lead time).
   - Avoid self-referential headings (e.g., “what this guide covers”) and generic filler (e.g., “Everything you need to know”).
   - If `{{keyword}}` contains “vs” / “versus”, include “how to choose” wording in at least one H2/H3.
10) Do not output any “template instructions” (e.g., “Use a table”, “Pick 3–6 links from the pool”, “At least 10 rows”). Only output the final article.
11) Do not paste the internal link pool list into the article. Only include the links you actually use.
12) Section requirements (must match structure below):
   - “Quick Answer (30 seconds)”: 3–6 bullets (rule/range/pitfall/validation/boundary).
   - “When {{keyword}} applies (and when it doesn’t)”: 3–5 bullets for each side.
   - “Rules & specifications”: a Markdown table with columns: Rule | Recommended value/range | Why it matters | How to verify | If ignored; at least 10 rows.
   - “Implementation steps”: 6–10 steps; each step includes action + key parameter + acceptance check.
   - “Failure modes & troubleshooting”: 6–10 items; Symptom → causes → checks → fix → prevention.
   - “FAQ”: 10–14 questions; each with a 1–2 sentence answer + 2–4 bullets; at least 6 questions must be long-tail queries that include `{{keyword}}` + one modifier (cost/lead time/materials/testing/DFM/acceptance criteria).
   - “Glossary (key terms)”: a Markdown table with at least 10 rows related to {{keyword}}.

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid keyword-stuffing): {{lsi}}

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

---
title: "{{keyword}}: <Query-style title with one of: Guide / Checklist / Specs / Troubleshooting / Cost / Lead Time>"
description: "One-sentence promise: what rules/specs/checklists/troubleshooting steps readers will get for {{keyword}}."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## {{keyword}} quick answer (30 seconds)

## When {{keyword}} applies (and when it doesn’t)

## {{keyword}} rules and specifications (key parameters and limits)

## {{keyword}} implementation steps (process checkpoints)

## {{keyword}} troubleshooting (failure modes and fixes)

## How to choose {{keyword}} (design decisions and trade-offs)

## {{keyword}} FAQ (cost, lead time, common defects, acceptance criteria, DFM files)
## Resources for {{keyword}} (related pages and tools)

## {{keyword}} glossary (key terms)

## Request a quote for {{keyword}} (DFM review + pricing; place this right before the conclusion)
<!-- COMPONENT: BlogQuickQuoteInline -->

- Add 1 internal link to Quote or Contact, with 1 sentence that sets expectations (DFM review + pricing).
- List what files/info to send for DFM review/quote (Gerbers, stackup, drawings, test, volume, packaging).

## Conclusion: {{keyword}} next steps
- Restate {{keyword}} in 2–4 sentences. No CTA here.
