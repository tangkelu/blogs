# P4-127 2026-05-02 Taconic And Arlon RF PTFE Current-Site Recheck

Date: 2026-05-02
Lane: `Taconic / Arlon RF-PTFE recovery`
Status: `fact_partial`

## Scope

Recheck current official Taconic- and Arlon-controlled sites for missing or undercovered RF / PTFE product-page or datasheet anchors, then land only justified source/fact updates inside the Taconic / Arlon material lane.

## Read Baseline

- `facts/materials/taconic-official-source-coverage-gap.md`
- `facts/materials/arlon-product-page-recovery-n-series.md`
- `logs/p4-116-2026-5-2-arlon-product-grade-source-recovery.md`
- existing Taconic and Arlon material source records under `sources/registry/materials/`

## Official Checks Performed

### Taconic

- checked current `4taconic.com` public pages directly
- rechecked previously cited `divisions` and search-style URL patterns on the current public site
- kept the official Taconic compliance PDF in scope as a domain-validity anchor only

### Arlon

- checked the current `arlon-products` directory page
- checked the official `wp-sitemap-posts-arlon_product-1.xml` product sitemap
- rechecked current official site search / product-endpoint visibility for the still-missing RF / PTFE families

## Recovery Decision

No new exact-product Taconic or Arlon RF / PTFE source records were justified in this pass.

### Taconic Outcome

- On `2026-05-02`, the current public `4taconic.com` site resolved to the industrial PTFE coated-fabrics / tapes / belts posture.
- The current public site pass did not expose recoverable official RF laminate product pages or datasheets for `RF`, `TLY`, `TLX`, `TLC`, or related ADD laminate families.
- Taconic therefore remains blocked for exact-product RF / PTFE promotion.

### Arlon Outcome

- The current official Arlon product directory remained live.
- The current official `arlon_product` sitemap exposed live public pages for the already covered `N-series`, `45NK`, `55NT`, `85NT`, and `86HP` branches.
- The same current official inventory did not expose `CLTE-XT`, `TC350`, `AD250`, `AD255`, `AD300`, `CuClad`, or `DiClad` as live public product pages.
- Those RF / PTFE families therefore remain blocked for exact-product promotion in the current public-site posture.

## Landed Artifacts

- `sources/registry/materials/arlon-current-product-sitemap.md`
- `sources/registry/materials/taconic-usa-industrial-materials-homepage.md`
- `facts/materials/arlon-rf-ptfe-current-site-gap.md`
- updated `facts/materials/taconic-official-source-coverage-gap.md`

## Outcome

Lane ended `fact_partial`.

This pass improved current official blocker evidence for Taconic and Arlon RF / PTFE recovery, but it did not justify any new exact-product Taconic or Arlon RF / PTFE material card because current official product-page or datasheet authority was still missing for the targeted families.

## Verification

- checked new source IDs and fact ID naming consistency
- kept all edits inside `sources/registry/materials/`, `facts/materials/`, and `logs/`
