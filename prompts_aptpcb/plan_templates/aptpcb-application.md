# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# ----------------------------------------------------

You are writing an **English Application & Industry Guide** for APTPCB, focused on the primary keyword: `{{keyword}}`.

**Article Style**: Industry-focused, application-driven. This template emphasizes WHERE and WHY to use `{{keyword}}`—real industries, real products, real benefits. Written from an application engineer's perspective helping customers choose the right solution.

**Differentiation**: Unlike Capability Guide (factory specs) or Comparison Guide (A vs B decisions), this guide answers "What industries use {{keyword}}? What are the benefits? How do I specify it for my application?"

### Word Count
- Total: 1800–2200 words

## Output Hard Rules (must follow)
1) Output final **Markdown only**. The first character must be `---` (Front Matter). No preface, no analysis, no "as an AI".
2) Language: English (US). Short sentences; translation-friendly.
3) Include **exactly once**: `<!-- COMPONENT: BlogQuickQuoteInline -->` (right before the conclusion).
4) Brand: first mention `APTPCB (APTPCB PCB Factory)`, then `APTPCB`. Total 3–5 mentions. No hype.
5) No images, no scripts, no canvas.
6) Do not mention search/SEO meta terms in the article.
7) Tone: consultative, educational. Help the reader understand applications and make informed choices.
8) Coherence rules:
   - Every section must show practical value of `{{keyword}}` for real-world applications.
   - Each H2 starts with 1 sentence connecting to the previous section.
   - Use specific industry examples: automotive ADAS, medical implants, 5G infrastructure, industrial automation, aerospace avionics, consumer wearables, etc.
9) Heading rules (H2/H3):
   - **Generate H2/H3 dynamically based on `{{keyword}}`.**
   - H2 should reflect application/benefit intent: "{{keyword}} benefits for [industry]", "why choose {{keyword}}", "{{keyword}} in [application]", "how to specify {{keyword}} for [use case]".
   - Avoid generic headings. Each H2 must add specific value related to `{{keyword}}`.
   - If `{{keyword}}` contains "vs" / "versus", include "how to choose" in at least one H2.
10) Do not output any "template instructions". Only output the final article.

## Internal Link Rules (CRITICAL)
- Select **3–5 links** from the pool below.
- **Distribute links naturally throughout the article**—at least 3 different H2 sections. Never cluster links.
- **Anchor text must be unique and semantic**:
  - ✅ Good: "multi-layer stackup design", "high-speed signal integrity", "thermal via patterns", "impedance-controlled routing"
  - ❌ Bad: "click here", "learn more", repeated anchor text, exact URL as anchor
- Place links mid-paragraph where they provide additional value to the reader.
- Do NOT create a separate "Resources" or "Related Links" section.

## Internal link pool (choose 3–5, distribute throughout)
{{internal_link_pool}}

## Capability Reference
Use these industry-competitive values when discussing specifications:
- Layer count: 1–64 layers
- Board thickness: 0.2mm–6.0mm
- Min trace/space: 3mil/3mil standard, 2mil/2mil advanced
- Min hole: 0.1mm mechanical, 0.075mm laser
- Max board size: 600mm × 1100mm
- Copper weight: 0.5oz–20oz
- Surface finishes: HASL, ENIG, OSP, Immersion Ag/Sn, Hard Gold
- Impedance: ±5% single-ended, ±8% differential
- Materials: FR4, High-Tg, Rogers, Isola, Taconic, Megtron, Aluminum, Polyimide
- Certifications: ISO 9001, IATF 16949, UL, IPC Class 2/3

## SEO placement rules
- `{{keyword}}` must appear in: title, description, first paragraph, at least two H2, and conclusion.
- Use LSI naturally: {{lsi}}

---
title: "{{keyword}}: Industry Applications, Benefits, and Specification Guide"
description: "Discover how {{keyword}} is used across industries—key benefits, application examples, and specification tips for engineers."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## [Dynamic H2: What is {{keyword}} and why it matters]
Write 2–3 paragraphs:
- Define {{keyword}} clearly for engineers searching this term
- Explain the core value proposition—what problem does it solve?
- Set context for the industries and applications covered in this guide
- Include 1 internal link naturally where relevant

## [Dynamic H2: Key benefits of {{keyword}}]
Write 6–8 benefit bullets, each with:
- **Benefit name**: 1–2 sentence explanation of the value
- Focus on performance, reliability, cost-efficiency, design flexibility
- Connect benefits to real engineering outcomes (signal integrity, thermal performance, weight reduction, etc.)

## [Dynamic H2: {{keyword}} applications by industry]
Create a detailed Markdown table:
| Industry | Typical Products | Key Requirements | Why {{keyword}} Fits |
At least 6 rows covering:
- Automotive (ADAS, EV, infotainment)
- Medical (implants, diagnostics, imaging)
- Telecommunications (5G, base stations, networking)
- Industrial (automation, power, sensors)
- Aerospace/Defense (avionics, radar, satellites)
- Consumer Electronics (wearables, smartphones, IoT)

After the table, write 2–3 paragraphs with specific application examples.
Include 1 internal link naturally.

## [Dynamic H2: How to specify {{keyword}} for your project]
Write 10–12 specification bullets covering:
- Base material selection (FR4, high-Tg, RF materials, flex)
- Layer count and stackup considerations
- Trace/space and copper weight requirements
- Via types (through-hole, blind, buried, micro-via)
- Surface finish selection based on application
- Impedance control requirements
- Testing and inspection levels (IPC Class 2 vs 3)
- Environmental requirements (temperature, humidity, vibration)
- Compliance needs (UL, RoHS, automotive standards)
- Documentation deliverables

Include specific values from Capability Reference.
Include 1 internal link naturally.

## [Dynamic H2: {{keyword}} selection criteria by use case]
Write 6–8 decision rules as:
- **For [application/requirement]**: recommend [approach] because [reason]

Examples of contexts to cover:
- High-speed digital designs
- RF/microwave applications
- High-power applications
- Space-constrained designs
- Cost-sensitive production
- Harsh environment deployment

## [Dynamic H2: {{keyword}} manufacturing considerations]
Write 3–4 paragraphs covering:
- Key manufacturing process steps relevant to {{keyword}}
- Quality checkpoints and inspection methods
- How design choices affect manufacturability and cost
- DFM tips specific to {{keyword}}

Include 1 internal link naturally.

## [Dynamic H2: {{keyword}} FAQ]
Write 8–10 questions with detailed answers (2–4 bullets each).

**Required long-tail questions (at least 5):**
- What is the typical cost of {{keyword}}?
- What is the lead time for {{keyword}}?
- What materials are best for {{keyword}}?
- What testing is required for {{keyword}}?
- How do I prepare files for {{keyword}} quote?
- What is the MOQ for {{keyword}}?
- Can {{keyword}} meet [specific industry] requirements?
- What certifications are available for {{keyword}}?

Include 1 internal link in a relevant answer.

<!-- COMPONENT: BlogQuickQuoteInline -->

## [Dynamic H2: Getting started with {{keyword}}—complete checklist]
Write a comprehensive conclusion section with:

**Summary paragraph (3–4 sentences):**
- Restate the core value of {{keyword}}
- Highlight the key industries and applications covered
- Emphasize the importance of proper specification

**Ready-to-quote checklist (8–10 items):**
Provide a complete list of what engineers should prepare:
- Design files: Gerber (RS-274X), drill files (Excellon), IPC-2581 or ODB++ if available
- Stackup: layer count, material requirements, impedance targets
- Specifications: trace/space, hole sizes, copper weights, surface finish
- Special requirements: controlled impedance, blind/buried vias, special materials
- Testing requirements: electrical test, impedance verification, cross-section
- Compliance needs: UL, IPC class, industry-specific standards
- Quantity and schedule: prototype vs production quantities, delivery timeline
- Packaging: panel requirements, shipping method, ESD protection

**Next steps (2–3 sentences):**
- Encourage the reader to gather their specifications
- Mention that APTPCB provides DFM review with quotes
- Keep the tone helpful, not pushy
