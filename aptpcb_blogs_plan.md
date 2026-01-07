# APTPCB Blog SEO Optimization Plan (EN, 2025 corpus)

Scope: `/code/hileap/frontendAPT/public/static/blogs/2025/**/en/*.md` (434 posts)

Reference datasets:
- Audit summary: `/data/hileap_blogs_2025_en_audit.md`
- Audit rows: `/data/hileap_blogs_2025_en_audit.csv`
- Competitor crawl insights (top keywords): `/data/top_keywords_blog/SEO_INSIGHTS.md`
- Competitor feature table: `/data/top_keywords_blog/seo_features.csv`

---

## 1) What “high ranking” is really telling us

From the competitor corpus (top10 positions) and your own EN corpus, the winning pattern is less about “URL contains keyword” and more about:
- **Intent match**: “what is / how to / vs / cost / checklist” pages map cleanly to queries.
- **Topic authority**: lots of closely related pages + internal links → Google sees a topical cluster.
- **Scannability**: clear H2/H3 structure, short answers early, tables/checklists, and visual aids.
- **Trust & proof**: references, specs, process controls, validations, examples, and clear identity.
- **CTR**: titles/descriptions that read naturally and don’t get truncated.

---

## 2) Baseline (your site vs competitor winners)

### Your EN 2025 posts (434)
Source: `/data/hileap_blogs_2025_en_audit.md`
- **Title length**: median 78 chars (p90 92); **82% > 70 chars**
- **Titles templated**: 97% contain `:`; 60% contain parentheses; repeated suffixes are common
- **H2/H3**: H2 median 10; H3 present in 42.6% (median H3 = 0)
- **Tables**: 65.7% of posts contain tables
- **Images in body**: median 0
- **Links**: internal links median 6; external links ~0

### Competitor “winner pages” (top10; 3451 unique pages)
Computed from `/data/top_keywords_blog/seo_features.csv` (dedup by MdPath)
- **Title length**: median ~56 chars (p90 ~81); only ~22% > 70 chars
- **H2**: median ~6
- **Images**: median ~4
- **Links**: median ~22 (note: includes some navigation in main container, but still signals stronger cross-linking)
- **Tables**: ~25% (your content is more table-heavy; that’s fine if tables serve intent)

Implication: your content depth is competitive, but **titles are too long/templated**, **visuals are sparse**, and **internal linking can be much stronger**.

---

## 3) North-star goals & KPIs (90 days)

Primary goals:
1. Increase organic clicks for priority topics (clusters) by improving **CTR + topical coverage**.
2. Improve average position for cluster keywords via **internal linking + content refresh**.

KPIs (track in GSC/GA4 weekly):
- **CTR uplift** on updated pages: +0.5–1.5pp on average for pages where titles were shortened
- **Impressions growth** on cluster keywords: +20–50% (depends on baseline)
- **Top3/Top10 keyword count** for targeted clusters: +10–30% for chosen topics
- **Internal link graph**: median internal links per post from ~6 → **12–20**
- **Media usage**: median in-body explanatory images from 0 → **2+**

---

## 4) Workstreams (what to change, exactly)

### A) Titles & descriptions (highest ROI)

Problem:
- 82% of titles are >70 chars and heavily templated (`:` + repeated suffix).
- In SERP this often truncates, reduces uniqueness, and hurts CTR.

Rules to adopt:
- **Target title length**: 50–65 chars (hard stop ~70).
- **One delimiter max**: prefer **one** `:` or `–`; avoid “double-colon” styles.
- Move templated suffixes (“A Practical End-to-End Guide…”, “Buyer-Friendly Playbook…”) into the **description** or into the first paragraph.
- Keep the head term early: put the primary keyword in the first 3–6 words.

Recommended title patterns (pick one per intent):
- **Definition**: `What Is {Term}? Definition, Use Cases, and Key Specs`
- **How-to**: `How to {Task}: Steps, Tools, and Common Mistakes`
- **Comparison**: `{A} vs {B}: Differences, Pros/Cons, and When to Use Each`
- **Testing**: `{Test} vs {Test}: Coverage, Cost, and Lead Time`
- **Buyer/DFM**: `{Topic}: Specs, DFM Checklist, and Validation Steps`
- **Manufacturing service**: `{Service}: Capabilities, Tolerances, and Lead Times`

Description rules:
- 150–170 chars, state “who it’s for + what it solves + proof angle”.
- Add 1–2 “supporting phrases” (SI/PI/EMI, DFM, IPC class, reliability test) as appropriate.

Batch execution:
- Use `/data/hileap_blogs_2025_en_audit.csv` to prioritize pages with `title_len>90`.
- Update titles first; wait 14 days; measure CTR change (GSC).

### B) H2/H3 structure (scannability + intent match)

Problem:
- H2 median 10; many posts have no H3 → long walls of text under many H2s.
- H2 text is long (median ~59 chars).

Targets:
- H2 count: **6–9** (keep 10+ only if it’s truly a long-form reference guide).
- Use H3 consistently: each major H2 should have **2–4** H3 subsections.
- H2 length: aim **35–55 chars** where possible; avoid overly long “keyword stuffed” headings.

Recommended “winning” outline (works for most PCB topics):
1. **Fast definition / when it matters** (2–4 sentences + 3 bullet “Key takeaways”)
2. **Specs that matter** (table)
3. **Design rules / DFM rules** (checklist)
4. **Common failures & root causes** (symptom → cause → fix)
5. **Validation / test methods** (how to verify)
6. **Manufacturing capabilities & tolerances** (what to specify)
7. **FAQ** (6–10 Q&As)
8. **Conclusion** (short recap + CTA)

Also: ensure “Menu Navigation” links are local anchors (`#...`), not external URLs.

### C) Internal linking (topical authority)

Problem:
- Internal links median ~6 per post; many posts likely link only to a couple of capability pages.

Targets:
- **12–20 internal links** per long-form post (contextual, not footer spam).
- Add links to:
  - relevant **/pcb/** capability pages
  - relevant **/materials/** and **/resources/** pages
  - 3–8 closely related blog posts (same cluster)

Implementation pattern:
- Add a consistent section near the end:
  - `## Related resources` (3–6 links)
  - `## Related guides` (3–6 links)
- Within-body links: every major H2 should include 1 contextual internal link if relevant.

Anchor text rules:
- Mix exact/partial/semantic anchors; don’t repeat the same anchor 10 times.
- Prefer “concept anchors” over “click here”.

### D) Visuals & diagrams (reduce bounce, increase understanding)

Problem:
- In-body images median 0; competitor winners often have ~4.

Targets:
- 2–6 meaningful visuals for long guides:
  - stack-up diagram
  - via structure / cross-section
  - process flow (AOI/ICT/FCT)
  - failure examples (voiding, delamination, warpage)
  - decision tree / checklist graphic

Rules:
- Every visual must answer “why is this here?” (don’t add stock photos to inflate image count).
- Use descriptive alt text (“BGA voiding X-ray examples”).

### E) Trust / E‑E‑A‑T signals

Add/standardize:
- “Updated date” or “Last reviewed” (if supported by the frontend)
- references section for standards:
  - IPC-6012 / IPC-A-600, IPC-2221, IPC-7351, JEDEC, etc. (topic-dependent)
- explicit “what we can manufacture / verify” statements with tolerances

### F) Technical SEO hygiene (guardrails)

Checks (site/platform-level):
- canonical tags and correct language alternates (en + translations)
- sitemap includes updated posts
- no accidental blocking (403/202 patterns observed on competitors; ensure APTPCB is crawl-friendly)

Content-level:
- avoid changing slugs unless necessary; if you must, do 301 + update internal links.

---

## 5) Rollout plan (what to do next week / next month)

### Week 1: pick focus clusters + prepare
- Choose **2–3 clusters** (e.g., “flex PCB”, “high-speed PCB”, “PCB testing/inspection”).
- For each cluster: define pillar page + supporting pages + product pages to link to.
- Create a “link map” spreadsheet: page → must-link-to list.

### Week 2–3: quick wins on existing posts
- Title shortening (batch 30–60 posts) + description refresh
- Fix TOC links that are not local anchors
- Add “Related resources/guides” blocks

### Week 4–6: deepen clusters
- Add 5–10 supporting posts per cluster (or refresh older posts to become supporting nodes)
- Add diagrams/images to top-performing pages first (highest impressions in GSC)

### Week 7–12: iterate with data
- Review GSC by page:
  - CTR low but impressions high → rewrite title/description again
  - positions 4–10 → improve internal links + snippet sections + add diagram/table
- Refresh top 20 “nearly there” pages monthly

---

## 6) Priority fix list (top candidates from the audit)

These are high-impact targets based on a simple score:
long titles + no images + low internal links + no H3.
Full list is in `/data/hileap_blogs_2025_en_audit.csv`.

Suggested title rewrites below follow the rules: shorter, less templated, intent-first.

1) `delamination-and-blistering-root-causes-and-prevention`
- Current: `delamination and pcb blistering: root causes and prevention: A Practical End-to-End Guide (from basics to production)`
- Suggested: `PCB Delamination & Blistering: Causes, Prevention, and Checklist`

2) `design-review-questions-pcb`
- Current: `design review questions pcb: The Ultimate Checklist for DFM, Signal Integrity, and Manufacturing Success`
- Suggested: `PCB Design Review Checklist: DFM Questions and Common Risks`

3) `ict-test-vs-flying-probe-cost-coverage-and-lead-time`
- Current: `ict test vs flying probe: cost, coverage, and lead time: A Buyer-Friendly Playbook (Specs, Risks, Checklist)`
- Suggested: `ICT vs Flying Probe: Coverage, Cost, and Lead Time`

4) `coverlay-opening-design-rules-tolerance-and-clearance`
- Current: `coverlay opening design rules (tolerance and clearance): A Practical End-to-End Guide (from basics to production)`
- Suggested: `Coverlay Opening Rules: Clearance, Tolerance, and Common Errors`

5) `flex-pcb-teardrop-and-pad-anchoring-best-practices`
- Current: `flex pcb teardrop and pad anchoring best practices: A Buyer-Friendly Playbook (Specs, Risks, Checklist)`
- Suggested: `Flex PCB Teardrops: Pad Anchoring Rules and When to Use Them`

6) `traceability-and-lot-control-in-pcb-manufacturing`
- Current: `traceability and lot control in pcb manufacturing: A Buyer-Friendly Playbook (Specs, Risks, Checklist)`
- Suggested: `PCB Traceability & Lot Control: Data, Labels, and Audit Checklist`

7) `common-pcb-manufacturing-defects-and-how-to-avoid`
- Current: `common pcb manufacturing defects and how to avoid: A Buyer-Friendly Playbook (Specs, Risks, Checklist)`
- Suggested: `Common PCB Defects: Root Causes, Detection, and Prevention`

8) `rigid-flex-impedance-control-and-stackup-planning`
- Current: `rigid flex impedance control and stackup planning: A Buyer-Friendly Playbook (Specs, Risks, Checklist)`
- Suggested: `Rigid-Flex Impedance Control: Stackup Planning and Tolerances`

9) `coverlay-vs-solder-mask-on-fpc`
- Current: `coverlay vs solder mask on FPC: A Practical End-to-End Guide (from basics to production)`
- Suggested: `Coverlay vs Solder Mask on Flex: Differences and Use Cases`

10) `fpc-panelization-and-carriers`
- Current: `FPC panelization and carriers: A Practical End-to-End Guide (from basics to production)`
- Suggested: `FPC Panelization: Carrier Types, Rules, and Yield Tips`

Execution note:
- Keep slugs unless there’s a hard reason to change; titles can change freely.

---

## 7) QA checklist (apply to every updated post)

Title & meta:
- [ ] Title 50–65 chars, 1 delimiter max, unique (no repeated suffix)
- [ ] Description 150–170 chars, intent + proof

Structure:
- [ ] “Key takeaways” near top (3–7 bullets)
- [ ] 6–9 H2s; each major H2 has 2–4 H3s
- [ ] At least 1 table if the query implies comparison/specs
- [ ] FAQ section (6–10 Q&As) where relevant

Linking:
- [ ] 12–20 internal links total; 3–8 to related posts
- [ ] Add `Related resources` / `Related guides`

Media:
- [ ] 2+ explanatory visuals; alt text; no empty decorative images

Trust:
- [ ] Add standards/references when applicable
- [ ] Clear capability/tolerance statements aligned with your factory reality

---

## 8) Deliverables to produce (so this is operational)

1) **Cluster map** (sheet): keyword → intent → pillar/supporting → target URL
2) **Title rewrite batch**: first 50 pages (rank by priority score)
3) **Internal linking rules**: per cluster “must-link” list
4) **Diagram library**: 10–20 reusable engineering figures/templates

---

## 9) Next action (pick your focus)

Reply with:
- the 2–3 clusters you want to push first (e.g., `flex pcb`, `pcb testing`, `high-speed pcb`)
- and whether you want “pure informational” traffic or “RFQ / manufacturing intent” traffic as the KPI

Then we can generate:
- a prioritized “top 50 pages to edit” list (with exact file paths) from `/data/hileap_blogs_2025_en_audit.csv`
- per-page title rewrite + H2/H3 restructure suggestions.

