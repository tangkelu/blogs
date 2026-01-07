## APTPCB Base Templates v3

These templates are a **v3 layout/structure variant** built on top of `_base_templates_v2`.

### What’s new vs v2 (inspired by `iphone-consumer-electronics.md`)
- Stronger narrative opening: a short “why the reader cares” hook before the technical breakdown.
- Adds a compact **Tech/Decision Lever → Practical Impact** matrix (styled HTML table block) near the top to improve scanability.
- Keeps the same core sections (Query / Pillar / Playbook) and stays compatible with the existing generator pipeline.

### Optional: Story-style template
- `aptpcb-story.md` provides a separate narrative structure that embeds the styled tables **inside relevant sections**
  (avoids “bullet list → sudden styled table”).
- For an isolated A/B test, use `batch_blog_generation_aptpcb_story_v3.py` (outputs to `blogs_aptpcb_story_v3`).

### How to test
Use the v3 entrypoint:

`python batch_blog_generation_aptpcb_v3.py --limit 5 --max-generation-attempts 1`
