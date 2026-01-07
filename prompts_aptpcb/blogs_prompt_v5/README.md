# blogs_prompt_v5 (APTPCB)

This version is organized around two SEO-friendly page types:
- `aptpcb-query.md`: Query / problem-solving landing page (how-to, checklist, troubleshooting).
- `aptpcb-pillar.md`: Pillar / end-to-end guide (definitions → metrics → selection → implementation).
- `aptpcb-playbook.md`: Playbook / buyer-friendly guide (specs → risks → validation → supplier checklist).

## Optional modules (content angles)
To avoid growing the number of full templates, v5 can inject small **modules** (angles) on top of the 3 skeletons:
- Modules dir: `prompts_aptpcb/blogs_prompt_v5/_modules_v1/`
- Available modules: `comparison` / `application` / `capability`
- Generator support:
  - Auto-infer modules from keyword text, or force via `--modules comparison,capability`
  - Override modules dir via `--modules-dir <path>`

## Internal links
- Internal link pool is synced from `aptpcb_sitemap.xml` into `prompts_aptpcb/internal_link_pool.md`.
- Generation injects this pool into templates via `{{internal_link_pool}}` (see `batch_blog_generation_aptpcb.py` / `batch_blog_generation_openai.py --internal-link-pool`).
- Re-sync when the site routes change:
  - `python scripts/sync_aptpcb_from_sitemap.py`

## Images (optional)
- APTPCB blogs can include a small number of relevant images:
  - 1 hero image (front matter `image:`) + 0–2 in-body images
  - Use only local `/assets/img/...` paths from the catalog: `/code/hileap/frontendAPT/docs/assets-img-filenames.md`
- Generation injects a short candidate list into templates via `{{assets_image_pool}}`:
  - `python batch_blog_generation_openai.py --assets-image-catalog /code/hileap/frontendAPT/docs/assets-img-filenames.md --assets-image-pool-size 18`

## Keywords & taxonomy
- v5 keywords are rebuilt from archived prompt libraries under `prompts_aptpcb/_legacy/` and re-bucketed into a new taxonomy.
- Rebuild/refresh keyword buckets:
  - `python scripts/rebuild_aptpcb_v5_keywords.py`

## Suggested generation commands
Recommended: use the dedicated site entrypoint `batch_blog_generation_aptpcb.py`.

- Dry-run (no API call):
  - `python batch_blog_generation_aptpcb.py --template-kind query --dry-run --limit 1`

- Generate (Query pages):
  - `python batch_blog_generation_aptpcb.py --template-kind query`

- Generate (Pillar pages):
  - `python batch_blog_generation_aptpcb.py --template-kind pillar`

- Generate (Playbook pages):
  - `python batch_blog_generation_aptpcb.py --template-kind playbook`

## Notes
- Default output directory for APTPCB is `blogs_aptpcb/` to avoid collisions with HILPCB output.
- APTPCB v5 supports shared base templates: categories may omit `templates/*.md` and rely on `prompts_aptpcb/blogs_prompt_v5/_base_templates_v2/`.
