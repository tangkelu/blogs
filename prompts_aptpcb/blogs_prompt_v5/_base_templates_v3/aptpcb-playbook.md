# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Buyer Playbook v3** for APTPCB, focused on the primary keyword: `{{keyword}}`.

Goal: help a buyer/engineer specify requirements, avoid risks, validate correctly, and qualify suppliers.

## v3 layout boosters (must follow)
1) Start with a short scenario hook (1–2 sentences) that frames a buyer decision.
2) After `## Key Takeaways`, add a compact **Spec / Lever → Outcome** matrix (styled HTML table block, 6–8 rows).

## Output Hard Rules
1) Output Markdown only; must start with `---`.
2) Exactly one H1 matching front matter `title`.
3) Keep section order; avoid starting with a table.
4) Include at least once: `<!-- COMPONENT: BlogQuickQuoteInline -->` in the quote section.

## Internal link pool (choose 6–10, do not output this list)
{{internal_link_pool}}

## Assets image pool (choose from here only; may be empty)
{{assets_image_pool}}

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

Write a 2–3 sentence opening (scenario hook + buyer decision framing). Then add **Highlights** (5–7 bullets, no H2).

## Key Takeaways
Write 7 bullets (include 2 numeric thresholds and 1 validation tip).

Now add the v3 matrix block (no H2). Use this format:
Replace all `...` placeholders with real content (no ellipsis in final output).

<div style="background-color:#F5F7FA;padding:18px;border-radius:10px;margin:20px 0;">
<h3 style="margin:0 0 12px 0;color:#000000;">Spec / Lever → Outcome</h3>
<table style="width:100%;border-collapse:collapse;text-align:left;color:#000000;">
<thead style="background-color:#F0F0F0;">
<tr>
<th style="padding:10px;border:1px solid #ddd;">Spec / lever</th>
<th style="padding:10px;border:1px solid #ddd;">Outcome (yield / reliability / cost / lead time)</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:10px;border:1px solid #ddd;">...</td><td style="padding:10px;border:1px solid #ddd;">...</td></tr>
</tbody>
</table>
</div>

### Contents
Add 7–10 anchor links to the H2 sections below.

## Scope, Decision Context, and Success Criteria

## Specifications to Define Upfront (Before You Commit)

## Key Risks (Root Causes, Early Detection, Prevention)

## Validation & Acceptance (Tests and Pass Criteria)

## Supplier Qualification Checklist (RFQ, Audit, Traceability)

## How to Choose (Trade-Offs and Decision Rules)

## FAQ (Cost, Lead Time, DFM Files, Materials, Testing)

## Request a Quote / DFM Review for {{keyword}} (What to Send)
<!-- COMPONENT: BlogQuickQuoteInline -->

## Glossary (Key Terms)

## Conclusion (Next Steps)
