# APTPCB Top-Rank Blog “Deep Read” Extraction Plan (from full page content)

Goal: deeply analyze the **body content** of top-ranking competitor blog pages we downloaded under `/data/top_keywords_blog`, and turn the findings into **reusable template assets** so APTPCB can consistently write “winner-shaped” posts.

Scope:
- Input corpus: `/data/top_keywords_blog/**/*.md` (ranking-referenced set)
- Ranking metadata: `/data/top_keywords_blog/seo_features.csv`
- Output templates target: `prompts_aptpcb/blogs_prompt_v5/_base_templates_v2/` (query/pillar/playbook) + optional “angle modules” (application/comparison/capability) used as plug-ins.

Non-goals:
- Do not copy competitor text verbatim into our prompts or blog outputs.
- Do not claim templates guarantee ranking; focus on intent-fit + winner-shaped structure + measurable quality.

---

## Phase 1 — Build the deep-read dataset (content-level, not just counts)

### 1.1 Define the “ranking-referenced” corpus (ground truth)
- Use `seo_features.csv` → the `MdPath` column as the canonical list of pages referenced by rankings.
- Validate:
  - every `MdPath` exists on disk
  - dedupe by `URL_norm` and by `MdPath`
- Output:
  - `/data/top_keywords_blog/deep_read/index_pages.csv` (MdPath, Site, URL_norm, position_summary, word_count, h2, tables, has_faq, etc.)

### 1.2 Page-level intent labeling (primary + secondary intent)
Goal: decide which base skeleton applies (query/pillar/playbook) and which “angle modules” should be enabled.
- Infer primary intent from:
  - URL path patterns (`what/meaning/define`, `how-to`, `vs`, `cost/price`, `lead-time`, `troubleshoot/defects`)
  - H1 and early H2 cues (e.g., “FAQ”, “Key takeaways”, “Glossary”, “Troubleshooting”)
- Output:
  - `/data/top_keywords_blog/deep_read/page_intents.csv` (MdPath → intent_primary, intent_secondary[])

---

## Phase 2 — Deep parse each page into reusable structure units

### 2.1 Extract structural tree + “answer-first opening”
Per page, parse:
- frontmatter `title`, body `H1`
- first 2–3 sentences under H1 (definition/why/what-you-get)
- presence of:
  - Highlights / Key takeaways near top
  - Contents / TOC (anchor list)
  - FAQ / Glossary / Conclusion / Related resources blocks
- headings tree: H2/H3 list, in order
- tables: count + table schemas (column headers)
- troubleshooting patterns (Symptom/Cause/Fix)
- decision-rule patterns (“If X, choose Y”)

Output:
- `/data/top_keywords_blog/deep_read/page_features.jsonl` (one JSON per page)

### 2.2 Canonical section labeling (semantic normalization)
Goal: map messy real headings into a stable “section vocabulary”.
Example labels:
- Definition & scope
- Quick answer / highlights
- Metrics / parameters
- Rules & specs table
- Steps / process
- Comparison / trade-offs
- Troubleshooting (symptom→cause→check→fix)
- Common mistakes
- Validation & acceptance (tests + pass criteria)
- FAQ (modifier buckets: cost/lead time/materials/testing/DFM/acceptance)
- Glossary
- Related resources
- Conclusion / next steps

Output:
- `/data/top_keywords_blog/deep_read/section_sequences.csv` (intent → canonical section sequences + frequencies)

---

## Phase 3 — Derive “winner writing assets” (blueprints + phrase banks + table schemas)

### 3.1 Blueprint library (intent → best structure)
For each primary intent, compute:
- most common canonical section order(s)
- recommended APTPCB section order (cleaned + consistent)
- target ranges (word_count, H2 count, tables, list density) from Top3/Top10

Output:
- `/data/top_keywords_blog/deep_read/SECTION_BLUEPRINTS.md`

### 3.2 Phrase banks (rewrite-safe, non-copying)
Generate reusable *patterns*, not competitor sentences:
- H2/H3 title patterns per canonical section
- answer-first opening templates:
  - definition sentence forms
  - boundary/exception sentence forms
  - “what you will get” sentence forms
- bridging sentence patterns (“Now that…, next…”)
- decision rule patterns (“If…, choose… because…”)
- troubleshooting micro-templates

Output:
- `/data/top_keywords_blog/deep_read/PHRASE_BANKS.md`

### 3.3 Table schema library
From real pages, infer stable table models:
- Rules/specs table
- Comparison table
- Validation & acceptance table
- Glossary table
- Cost/lead-time driver table

Output:
- `/data/top_keywords_blog/deep_read/TABLE_SCHEMAS.md`

---

## Phase 4 — Apply assets back to our templates (v2 templates become “winner-shaped”)

### 4.1 Base skeletons (query/pillar/playbook)
Update:
- `prompts_aptpcb/blogs_prompt_v5/_base_templates_v2/aptpcb-query.md`
- `prompts_aptpcb/blogs_prompt_v5/_base_templates_v2/aptpcb-pillar.md`
- `prompts_aptpcb/blogs_prompt_v5/_base_templates_v2/aptpcb-playbook.md`

Rules to enforce:
- Answer-first opening + Highlights + (long pages) TOC
- Minimum table requirements aligned with intent
- Stronger acceptance criteria and boundary conditions
- Stronger FAQ modifiers and troubleshooting patterns
- Avoid template leakage (“[Dynamic H2: …]” placeholders)

### 4.2 Angle modules (application/comparison/capability)
Turn existing plan_templates into **opt-in modules**:
- comparison module → comparison tables + decision matrix + trade-offs wording
- capability module → capability specs + lead time/MOQ + “what to send for quote”
- application module → industry/use-case table + scenario-based decision rules

Output:
- `prompts_aptpcb/blogs_prompt_v5/_modules_v1/*.md` (optional new folder)
- and update base templates to reference the module behavior in rules (without requiring new runtime variables).

---

## Phase 5 — Quality gates (prove we implemented the plan)

### 5.1 Template lint (static)
Write a checker that validates generated outputs:
- frontmatter present
- H1 equals title
- has Highlights + has TOC (when word count > threshold)
- required tables exist with required columns
- FAQ count + long-tail modifier coverage
- no banned meta terms (SERP/PAA/“internal links required”)
- acronym expansion rules respected (first mention expands)

Output:
- `scripts/lint_generated_blog_md.py` (run on new outputs)

### 5.2 Pilot generation + review loop
- Generate 5–10 posts with v2 templates (across intents).
- Run lint + spot-check for: answer quality, specificity, non-hallucination, non-copying.
- Iterate: adjust phrase banks and templates.

---

## Implementation status (this repo)

Next actions (starting now):
1) Implement deep parser + intent labeler + sequence mining scripts.
2) Generate `/data/top_keywords_blog/deep_read/*` assets.
3) Feed the derived assets back into `_base_templates_v2` with minimal prompt bloat.

