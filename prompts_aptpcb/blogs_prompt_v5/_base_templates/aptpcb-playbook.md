# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Playbook / Buyer-Friendly Guide** for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: help an engineer/procurement lead make a safe decision (specs → risks → validation → supplier checklist) with practical, actionable steps, while naturally guiding to a quote/DFM request.

### 字数要求
- 总字数：2000-2500词

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right before the conclusion, after the quote/DFM request section).
4) Include **3–6** internal links from the pool below (Markdown links, diverse anchor text).
5) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
6) No images, no scripts, no canvas.
7) Do not mention search/SEO meta terms in the article (e.g., “SERP”, “People Also Ask”, “internal links required”).
8) Coherence rules:
   - Every section must support solving `{{keyword}}`; drop anything that doesn’t.
   - Each H2 starts with 1 sentence that links to the previous section (no topic jumps).
   - Prefer fewer, consistent examples over many unrelated examples.
9) Heading rules (H2/H3):
   - Avoid self-referential headings like “what this playbook covers”.
   - Use intent-first phrasing (definition/scope → when to use → key specs → risks → validation → supplier qualification).
   - No boilerplate “before quoting” phrasing; use “specifications to define upfront” instead.
   - If `{{keyword}}` contains “vs” / “versus”, include “how to choose” wording in at least one H2.
   - Ensure FAQ headings and questions include long-tail modifiers (cost/lead time/DFM files/materials/testing/acceptance criteria).
10) Do not output any “template instructions”. Only output the final article.
11) Do not paste the internal link pool list into the article. Only include the links you actually use.

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid keyword-stuffing): {{lsi}}

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

---
title: "{{keyword}}: A Buyer-Friendly Playbook (Specs, Risks, Checklist)"
description: "A practical playbook for {{keyword}}: requirements, risk points, validation plan, and a supplier checklist to scale safely."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## {{keyword}}: definition, scope, and who this guide is for
- Write 2–4 short paragraphs that define the scope, what the reader will get, and the decision context.

## When to use {{keyword}} (and when a standard approach is better)

## {{keyword}} specifications (materials, stackup, tolerances)
- List 8–12 bullets with concrete ranges/targets (materials, stackup, tolerances, reliability, environment, testing, documentation).

## {{keyword}} manufacturing risks (root causes and prevention)
- 8–12 items, each: risk → why it happens → how to detect early → prevention.

## {{keyword}} validation and acceptance (tests and pass criteria)
- Provide 8–12 validation steps, each: objective → method → acceptance criteria.

## {{keyword}} supplier qualification checklist (RFQ, audit, traceability)
- Provide a buyer-ready checklist grouped into 4 groups:
  - RFQ inputs (8–12 bullets)
  - Capability proof (6–10 bullets)
  - Quality system & traceability (6–10 bullets)
  - Change control & delivery (6–10 bullets)

## How to choose {{keyword}} (trade-offs and decision rules)
- 5–8 trade-offs with “If you prioritize X, choose Y; otherwise choose Z”.

## {{keyword}} FAQ (cost, lead time, DFM files, materials, testing)
- 8–10 questions; each with 1–2 sentence answer + 2–4 bullets; at least 5 questions must be long-tail queries that include `{{keyword}}` + one modifier (cost/lead time/materials/testing/DFM/acceptance criteria).

## Resources for {{keyword}} (related pages and tools)
- Add 3–6 internal links selected from the pool, with 1-sentence “why this helps”.

## Request a quote for {{keyword}} (DFM review + pricing; place this right before the conclusion)
<!-- COMPONENT: BlogQuickQuoteInline -->

- Add 1 internal link to Quote or Contact, with 1 sentence that sets expectations (DFM review + pricing).
- List what files/info to send for DFM review/quote (Gerbers, stackup, drawings, test, volume, packaging).

## Conclusion: {{keyword}} next steps
- Restate {{keyword}} in 2–4 sentences. No CTA here.
