# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Capability & Ordering Guide** for APTPCB, focused on the primary keyword: `{{keyword}}`.

**Article Style**: Factory-focused, specification-driven. This template emphasizes WHAT we can build and HOW to order—detailed capability tables, process descriptions, and ordering workflows. Written from a manufacturing engineer's perspective showcasing production capabilities.

**Differentiation**: Unlike Application Guide (industry use cases) or Comparison Guide (A vs B decisions), this guide answers "What are the exact specifications you can manufacture? What's your process? How do I place an order?"

### Word Count
- Total: 1600–2000 words

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no "as an AI".
2) Language: English (US). Short sentences; translation-friendly.
3) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right before the conclusion).
4) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. Focus on factual capabilities.
5) No images, no scripts, no canvas.
6) Do not mention search/SEO meta terms in the article.
7) Tone: professional, confident, precise. Present capabilities with specific numbers and clear processes.
8) Coherence rules:
   - Every section should answer "what can you make?" or "how do I order?"
   - Each H2 starts with 1 sentence connecting to the previous section.
   - Use concrete specifications, not vague claims.
9) Heading rules (H2/H3):
   - **Generate H2/H3 dynamically based on `{{keyword}}`.**
   - H2 should reflect capability/process intent: "{{keyword}} specifications we manufacture", "{{keyword}} production process", "{{keyword}} quality standards", "ordering {{keyword}} step by step".
   - Avoid generic headings. Each H2 must convey specific capability or process information.
   - If `{{keyword}}` contains "vs" / "versus", include "how to choose" in at least one H2.
10) Do not output any "template instructions". Only output the final article.

## Internal Link Rules (CRITICAL)
- Select **3–5 links** from the pool below.
- **Distribute links naturally throughout the article**—at least 3 different H2 sections. Never cluster links.
- **Anchor text must be unique and semantic**:
  - ✅ Good: "HDI microvia technology", "surface finish options", "flex PCB manufacturing", "assembly services overview"
  - ❌ Bad: "click here", "learn more", repeated anchor text, exact URL as anchor
- Place links mid-paragraph where they provide additional value.
- Do NOT create a separate "Resources" or "Related Links" section.

## Internal link pool (choose 3–5, distribute throughout)
{{internal_link_pool}}

## Capability Reference (MUST use these exact values)
- **Layer count**: 1–64 layers
- **Board thickness**: 0.2mm–6.0mm (±10%)
- **Min trace/space**: 3mil/3mil (0.075mm) standard, 2mil/2mil (0.05mm) advanced
- **Min hole size**: 0.1mm mechanical drill, 0.075mm laser micro-via
- **Max board size**: 600mm × 1100mm
- **Copper weight**: 0.5oz–10oz inner, 0.5oz–20oz outer
- **Aspect ratio**: up to 20:1
- **Surface finishes**: HASL LF, ENIG (2–4μ" Au), OSP, Immersion Ag, Immersion Sn, Hard Gold (up to 50μ"), Soft Gold
- **Solder mask**: Green, black, white, red, blue, yellow; matte/glossy
- **Silkscreen**: White, black, yellow
- **Impedance tolerance**: ±5% single-ended, ±8% differential
- **Materials**: FR4 (Tg135/150/170+), Halogen-free, Rogers 4003/4350/4835, Isola, Taconic, Megtron 6/7, Aluminum (1–3W/mK), Copper-based, Polyimide flex
- **Certifications**: ISO 9001, ISO 14001, IATF 16949, UL E-listed, IPC-6012 Class 2/3, IPC-A-600 Class 2/3
- **Lead times**: Prototype 24–72 hrs, Small batch 5–7 days, Production 10–15 days
- **MOQ**: No minimum for prototype, 5+ pcs for production

## SEO placement rules
- `{{keyword}}` must appear in: title, description, first paragraph, at least two H2, and conclusion.
- Use LSI naturally: {{lsi}}

---
title: "{{keyword}}: Manufacturing Capabilities, Specifications, and Ordering Guide"
description: "Explore detailed {{keyword}} manufacturing capabilities—specifications, materials, processes, lead times, and how to request a quote from APTPCB."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 7
tags: {{tags}}
---

## [Dynamic H2: {{keyword}} overview—what we manufacture]
Write 2–3 paragraphs:
- Define {{keyword}} and its role in electronics manufacturing
- Briefly describe APTPCB's experience and focus areas for {{keyword}}
- Set expectations for the capability details that follow
- Include 1 internal link naturally

## [Dynamic H2: {{keyword}} manufacturing capabilities]
Write 8–10 capability bullets with specific numbers:
- Layer count range with typical applications
- Dimensional capabilities (thickness, size, tolerances)
- Fine-pitch capabilities (trace/space, hole sizes)
- Special features (blind/buried vias, via-in-pad, back-drill)
- Material options supported
- Surface finish options
- Testing and inspection capabilities

Use exact values from Capability Reference.
Include 1 internal link naturally.

## [Dynamic H2: {{keyword}} technical specifications]
Create a comprehensive Markdown table:
| Parameter | Standard Capability | Advanced Capability | Tolerance/Notes |

At least 12 rows covering:
- Layer count
- Board thickness
- Copper weight (inner/outer)
- Minimum trace width
- Minimum space
- Minimum hole size (mechanical)
- Minimum hole size (laser)
- Aspect ratio
- Board size (min/max)
- Impedance control
- Solder mask registration
- Silkscreen line width

Use exact values from Capability Reference.

## [Dynamic H2: {{keyword}} material options]
Write 6–8 bullets covering available materials:
- Standard FR4 grades and Tg ratings
- High-frequency materials (Rogers, Taconic, Isola)
- High-speed materials (Megtron, TU series)
- Metal-core options (aluminum, copper)
- Flex materials (polyimide types and thicknesses)
- Specialty materials (halogen-free, high-CTI, ceramic-filled)

Include specific brand names and performance grades.
Include 1 internal link naturally.

## [Dynamic H2: {{keyword}} surface finish and solder mask options]
Write 4–5 paragraphs covering:
- Available surface finishes with thickness ranges and applications
- Solder mask color options and special finishes (matte, peelable)
- Silkscreen options and resolution
- How to select the right finish for your application

## [Dynamic H2: {{keyword}} production process and quality]
Write 3–4 paragraphs covering:
- Key manufacturing process steps for {{keyword}}
- Equipment highlights (brand names if relevant)
- Quality management system and certifications
- Inspection and testing methods (AOI, flying probe, impedance testing)

Include 1 internal link naturally.

## [Dynamic H2: {{keyword}} lead time and volume options]
Create a Markdown table:
| Order Type | Typical Lead Time | MOQ | Best For |

At least 5 rows:
- Quick-turn prototype (24–48 hrs)
- Standard prototype (3–5 days)
- Small batch (5–7 days)
- Production (10–15 days)
- Scheduled production (negotiable)

After the table, write 1–2 paragraphs on:
- Factors that affect lead time
- Volume pricing considerations
- How to expedite orders when needed

## [Dynamic H2: {{keyword}} FAQ]
Write 8–10 questions with detailed answers (2–4 bullets each).

**Required long-tail questions (at least 5):**
- What is the cost of {{keyword}} per square inch/panel?
- What is the fastest lead time for {{keyword}}?
- What file formats do you accept for {{keyword}}?
- Do you provide DFM review for {{keyword}}?
- What testing is included with {{keyword}}?
- Can you source components for {{keyword}} assembly?
- What is your {{keyword}} defect rate / quality level?
- Do you offer {{keyword}} with [specific feature]?

Include 1 internal link in a relevant answer.

<!-- COMPONENT: BlogQuickQuoteInline -->

## [Dynamic H2: How to order {{keyword}}—complete guide]
Write a comprehensive ordering guide with:

**Ordering overview (2–3 sentences):**
- Explain the quote-to-delivery process
- Mention DFM review is included

**Required files checklist (formatted as bullets):**
- Gerber files: RS-274X format, all layers clearly named
- Drill files: Excellon format, separate files for PTH and NPTH
- Stackup document: layer sequence, materials, copper weights, impedance requirements
- Fabrication drawing: board outline, dimensions, tolerances, special notes
- Netlist (optional): IPC-D-356 for electrical test
- BOM (for assembly): manufacturer part numbers, quantities, designators
- Pick-and-place file (for assembly): centroid data in CSV or Excel format
- Assembly drawing (for assembly): component placement, polarity, special instructions

**Information to specify:**
- Quantity required (prototype and production)
- Target delivery date and shipping method
- Surface finish and solder mask preferences
- Testing requirements (standard electrical test, impedance coupon, etc.)
- Compliance requirements (UL, RoHS, IATF, etc.)
- Packaging preferences (vacuum sealed, dry pack, panel or depanelized)

**What happens after you submit:**
- APTPCB reviews files and provides DFM feedback within 24 hours
- Formal quote issued with lead time confirmation
- Order confirmation and production scheduling
- Quality inspection and shipping with tracking

**Contact and support (2 sentences):**
- Provide guidance on how to reach APTPCB for questions
- Mention engineering support availability
