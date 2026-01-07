# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Pillar Page v3** (end-to-end hub guide) for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: cover Definition → Metrics → Selection → Implementation → Mistakes → FAQ → Glossary, and be the hub page that future Query pages can link to.

## v3 layout boosters (must follow)
1) Start with a short narrative hook (1–2 sentences), then define `{{keyword}}` in plain English.
2) After `## Key Takeaways`, add a compact **Tech Feature → Buyer Impact** matrix (styled HTML table block, 5–7 rows).
   - Convert engineering details into outcomes: yield, reliability, lead time, cost, testability.
   - Keep claims conservative; if uncertain, say “confirm during DFM/quote”.

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis.
2) Language: English (US). Short sentences; translation-friendly.
3) After front matter, output exactly one H1 (`# ...`) and it must match the front-matter `title` exactly.
4) Include at least once: `<!-- COMPONENT: BlogQuickQuoteInline -->` (place it right after “Key Takeaways”).
5) Include 6–10 internal links from the pool below (diverse anchor text; distribute across the article).
6) Images are allowed but must be controlled (use only `/assets/img/...` from pool if provided).
7) Do not mention SEO meta terms in the article.
8) Section order (do not skip): front matter → H1 → opening → Key Takeaways → v3 matrix block → Contents → scope → metrics → selection → implementation → mistakes → FAQ → glossary → conclusion.

## Internal link pool (choose 6–10, do not output this list)
{{internal_link_pool}}

## Assets image pool (choose from here only; may be empty)
{{assets_image_pool}}

## SEO placement rules
- Primary keyword `{{keyword}}` must appear in: title, description, first paragraph, at least one H2, and conclusion.
- Use LSI keywords naturally: {{lsi}}

---
title: "{{keyword}}: A Practical End-to-End Guide (from Basics to Production)"
description: "Learn {{keyword}} from definition to production: key metrics, selection trade-offs, implementation checkpoints, and acceptance criteria."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 10
tags: {{tags}}
---

# {{keyword}}: A Practical End-to-End Guide (from Basics to Production)

Write a 2–3 sentence opening (scenario hook + definition + why it matters).

## Key Takeaways
Write 5–7 bullets (definition, metrics, misconception, validation tip, decision rule).

Now add the v3 matrix block (no H2). Use this format:
Replace all `...` placeholders with real content (no ellipsis in final output).

<div style="background-color:#E8F5E8;padding:18px;border-radius:10px;margin:20px 0;">
<h3 style="margin:0 0 12px 0;color:#000000;">Tech Feature → Buyer Impact</h3>
<table style="width:100%;border-collapse:collapse;text-align:left;color:#000000;">
<thead style="background-color:#DFF3DF;">
<tr>
<th style="padding:10px;border:1px solid #ddd;">Technical feature / decision</th>
<th style="padding:10px;border:1px solid #ddd;">Direct impact (what the buyer gets)</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:10px;border:1px solid #ddd;">...</td><td style="padding:10px;border:1px solid #ddd;">...</td></tr>
</tbody>
</table>
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

### Contents
Add 7–10 anchor links to the H2 sections below.

## What It Really Means (Scope & Boundaries)

## Metrics That Matter (How to Evaluate It)
Include at least 1 Markdown table.

## How to Choose (Selection Guidance by Scenario)

## Implementation Checkpoints (Design to Manufacturing)

## Common Mistakes (and the Correct Approach)

## FAQ (Cost, Lead Time, Materials, Testing, Acceptance Criteria)

## Glossary (Key Terms)

## Conclusion (Next Steps)
