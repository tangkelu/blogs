# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Pillar Page** (end-to-end guide) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: cover Definition → Metrics → Selection → Implementation → Validation → Mistakes, and become the hub page that future Query posts can link to.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no “as an AI”.
2) Language: English (US). Short sentences; translation-friendly.
3) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right after Key takeaways).
4) Include **at least 3** internal links from the pool below (Markdown links, diverse anchor text).
5) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions.
6) No images, no scripts, no canvas.
7) Do not mention search/SEO meta terms in the article (e.g., “SERP”, “People Also Ask”, “internal links required”).
8) Coherence rules:
   - Keep the page as a single narrative: Definition → Metrics → Selection → Implementation → Mistakes → FAQ → Conclusion.
   - Each H2 must start with 1 sentence that links back to the previous section.
   - If a detail is not relevant to `{{keyword}}`, drop it instead of forcing it in.
9) Heading rules (H2/H3):
   - Headings must stay “definition/metric/selection/implementation/validation” oriented (avoid generic filler headings).
   - Avoid self-referential headings (e.g., “what this guide covers”) and purely promotional headings.
   - If `{{keyword}}` contains “vs” / “versus”, include “how to choose” wording in at least one H2/H3.
10) Do not output any “template instructions” (e.g., “Use a table”, “Pick 3–6 links from the pool”, “At least 12 rows”). Only output the final article.
11) Do not paste the internal link pool list into the article. Only include the links you actually use.
12) Section requirements (must match structure below):
   - “Key Takeaways”: 5–7 bullets (definition/3 metrics/misconception/tip/validation).
   - “Metrics that matter”: a Markdown table (Metric | Why it matters | Typical range or influencing factors | How to measure).
   - “Selection guidance by scenario”: at least 6 scenarios with clear trade-offs.
   - “From design to manufacturing”: 8–12 checkpoints; each has recommendation + risk + acceptance method.
   - “Common mistakes”: 6–10 items.
   - “FAQ”: 8–12 questions; at least 5 questions must be long-tail queries that include `{{keyword}}` + one modifier (cost/lead time/materials/testing/acceptance criteria).
   - “Glossary (key terms)”: a Markdown table with at least 12 rows.

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally (avoid keyword-stuffing): {{lsi}}

## Internal link pool (choose 3–6, do not output this list)
{{internal_link_pool}}

---
title: "{{keyword}}: A Practical End-to-End Guide (from basics to production)"
description: "One-sentence summary of what readers will learn about {{keyword}}: definitions, key metrics, selection trade-offs, and validation."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## Key takeaways for {{keyword}}

## What {{keyword}} really means (scope & boundaries)

## {{keyword}} metrics that matter (how to evaluate quality)

## How to choose {{keyword}}: selection guidance by scenario (trade-offs)

## {{keyword}} implementation checkpoints (design to manufacturing)

## {{keyword}} common mistakes (and the correct approach)

## {{keyword}} FAQ (cost, lead time, materials, testing, acceptance criteria)

## Resources for {{keyword}} (related pages and tools)

## {{keyword}} glossary (key terms)

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion: {{keyword}} next steps
- Restate {{keyword}} and list what information to provide for a DFM review / quote (Gerbers, stackup, specs, test requirements, etc.).
