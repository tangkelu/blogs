## APTPCB Story Template (v3)

This directory contains a **single narrative/story-style template** inspired by:
`/code/hileap/frontendHIL/public/static/blogs/2025/10/en/iphone-consumer-electronics.md`

Key idea: keep a **narrative H2 flow** and embed the “visual” tables *inside the relevant sections*
instead of placing a styled table right after a bullet list.

## Note
Story v3 is also included in the unified v3 template set:
- `prompts_aptpcb/blogs_prompt_v5/_base_templates_v3/aptpcb-story.md`

The recommended entrypoint is:
- `python batch_blog_generation_aptpcb_story_v3.py ...` (it selects `--template-kind story` automatically)
