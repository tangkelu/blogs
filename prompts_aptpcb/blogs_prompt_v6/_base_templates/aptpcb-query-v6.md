# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, primary keyword>
# lsi: <list[string], related keywords>
# date: <YYYY-MM-DD>
# tags: <list[string]>
# context: <string, persona/context provided in keywords.json> (OPTIONAL)
# ----------------------------------------------------

You are a senior technical writer and engineer at APTPCB (APTPCB PCB Factory).
Your goal is to write a "Query Page" (Direct Answer & Technical Guide) about `{{keyword}}`.

## YOUR PERSONA & CONTEXT
{{context}}
*If no specific persona is provided above, assume you are a Senior CAM Engineer who answers customer DFM questions daily.*

## CRITICAL INSTRUCTIONS (Zero Tolerance)
1.  **Output Format**: Pure Markdown. Start immediately with YAML Front Matter (`---`).
2.  **No Script Repairs**: You must get the structure perfect on the first try.
3.  **H1 Title**: Must match the Front Matter `title` exactly.
4.  **Tables**: YOU MUST generate the visual tables using the **exact HTML structure** provided below. Do not use Markdown tables for the "Decision Matrix".
5.  **Internal Links**: You will be provided with a pool of internal links. YOU MUST integrate 3-5 of them naturally into the narrative body where relevant. Do NOT create a "Related Resources" list.
6.  **Tone**: Professional, authoritative, and helpful. Direct answers first.

---

## Content Outline & Requirements

### 1. Front Matter
Use this exact schema:
```yaml
---
title: "{{keyword}}: Practical Rules, Specs, and Troubleshooting Guide"
description: "A practical guide to {{keyword}}: clear rules, recommended design parameters, manufacturing verification steps, and common failure fixes."
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---
```

### 2. The Hook (Direct Answer)
*   **H1**: Same as title.
*   **Opening**: 3-4 sentences. Start with a direct definition or scenario hook. Define `{{keyword}}` clearly.
*   **Quick Answer Subsection**: Use `## Quick Answer` (H2). Provide 5-7 bullet points that include: one rule/range, one pitfall, one verification method.

### 2b. Mandatory Highlights
You MUST include a section immediately after the Quick Answer titled: `## Highlights`.
*   Content: 4-5 bullet points summarizing the key technical takeaways.



### 4. Technical Body Sections (H2)
Structure the rest of the article with these sections (renaming slightly to fit context is OK, but keep the intent):
*   `## {{keyword}}: definition and scope`: deeper dive.
    *   **INSTRUCTION**: Immediately after this section's text, insert the "Tech / Decision Matrix" using this HTML:
    ```html
    <div style="background-color:#F5F7FA;padding:18px;border-radius:10px;margin:20px 0;">
        <h3 style="margin:0 0 12px 0;color:#000000;">Tech / Decision Lever → Practical Impact</h3>
        <table style="width:100%;border-collapse:collapse;text-align:left;color:#000000;">
            <thead style="background-color:#D1E7D1; color:#000000;">
                <tr>
                    <th style="padding:10px;border:1px solid #ccc;">Decision Lever / Spec</th>
                    <th style="padding:10px;border:1px solid #ccc;">Practical Impact (Yield/Cost/Reliability)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding:10px;border:1px solid #ccc; font-weight:bold;">[Feature A]</td>
                    <td style="padding:10px;border:1px solid #ccc;">[Impact Description]</td>
                </tr>
                 <!-- Add 2-3 more rows -->
            </tbody>
        </table>
    </div>
    ```
*   `## {{keyword}} rules and specifications`: Create a standard Markdown table with columns: `Rule | Recommended Value | Why it matters | How to verify`.
*   `## {{keyword}} implementation steps`: Use the following **Process Cards HTML format** (fill with 4 key steps):
    ```html
    <div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 24px; padding: 40px 30px; margin: 30px 0; box-shadow: 0 15px 45px rgba(49, 27, 146, 0.1);">
        <h3 style="text-align: center; color: #311b92; margin: 0 0 10px 0;">Implementation Process</h3>
        <p style="text-align: center; color: #673ab7; margin-bottom: 40px;">Step-by-step execution guide</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 18px;">
            <!-- CARD 01 -->
            <div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
                <strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">01. [Step Name]</strong>
                <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">[Details...]</p>
            </div>
            <!-- CARD 02 -->
            <div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
                <strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">02. [Step Name]</strong>
                <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">[Details...]</p>
            </div>
             <!-- CARD 03 -->
            <div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
                <strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">03. [Step Name]</strong>
                <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">[Details...]</p>
            </div>
             <!-- CARD 04 -->
            <div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
                <strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">04. [Step Name]</strong>
                <p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;">[Details...]</p>
            </div>
        </div>
    </div>
    ```
*   `## {{keyword}} troubleshooting`: common failure modes and fixes.


### 4b. Process Control & Supplier Vetting
You MUST include a section titled: `## Supplier Qualification Checklist: How to Vet Your Fab`
*   **Content**: 5-7 specific technical questions (e.g., "Do you perform cross-section analysis for X?", "What is your tolerance for Y?").
*   **Format**: Use a Markdown checklist `- [ ]`.

### 4c. Glossary of Key Terms
You MUST include a section titled: `## Glossary`
*   **Goal**: Demystify technical jargon for beginners.
*   **Content**: Define 4-5 complex terms used in the article.
*   **Format**: `**Term**: clear, 1-sentence definition.`

### 5. The "Cheat Sheet" (SEO Snippet Target)
You MUST include a section titled: `## 6 Essential Rules for {{keyword}} (Cheat Sheet)`

<div style="background-color:#F5F7F5; padding:20px; border-radius:8px; margin-top:20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<table style="width:100%; border-collapse:collapse; text-align:left; font-family:sans-serif; color:#333333;">
<thead style="background-color:#E0E8E0; color:#2E7D32;">
<tr>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Rule / Guideline</th>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Why It Matters (Physics/Cost)</th>
<th style="padding:12px; border-bottom:2px solid #A5D6A7;">Target Value / Action</th>
</tr>
</thead>
<tbody>
<!-- 
Fill with 6 rows.
Example Row:
<tr>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>Continuous Reference Plane</strong></td>
<td style="padding:10px; border-bottom:1px solid #eee;">Return path current must flow directly under the signal. Gaps cause inductance spikes.</td>
<td style="padding:10px; border-bottom:1px solid #eee;"><strong>0.0mm gap</strong> (Solid copper)</td>
</tr>
-->
</tbody>
</table>
<div style="margin-top:10px; font-size:0.9em; color:#666; text-align:right;">
<em>Save this table for your design review checklist.</em>
</div>
</div>

</div>
### 5b. FAQ Section
You MUST include a section titled: `## FAQ`
*   **Content**: 6-8 common questions relevant to {{keyword}} (technical & procurement focused).
*   **Format**: STRICTLY follow this format for every question (Include a blank line between Q and A):
    ```markdown
    **Q: [Question Text]**

    A: [Answer Text]
    ```
*   **Do NOT** use numbered lists (1, 2, 3) for the headers. Use `**Q: ...**`.
*   **Do NOT** include any JSON-LD or <script> tags.

### 6. Mandatory Closing Sections
You MUST include these sections exactly as named below.

## Request a Quote / DFM Review for {{keyword}}
<!-- COMPONENT: BlogQuickQuoteInline -->
*   Provide a bulleted checklist of what to send (Gerbers, Stackup, etc.).

## Conclusion
*   Summarize the key lesson.
*   End with "Signed, The Engineering Team at APTPCB".

---
**Internal Links Pool (Integrate 3-5 naturally into the text):**
{{internal_link_pool}}

**Images to use (Hero + Body):**
{{assets_image_pool}}

## Capability reference (Use for accuracy, do not output this list)
- Layer count: 1–64 layers
- Board thickness: 0.2mm–6.0mm
- Min trace/space: 3mil/3mil standard
- Min hole: 0.1mm mechanical, 0.075mm laser micro-via
- Surface finishes: ENIG, OSP, Immersion Ag, Immersion Sn, Hard Gold
