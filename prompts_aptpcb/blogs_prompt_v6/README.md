# APTPCB Blogs Prompt v6 (Prompt-First Architecture)

This version shifts the generation logic from **Python Script** to **Markdown Prompt (LLM)**.

## Key Changes from v5
1.  **Smart Templates**: The `.md` templates in `_base_templates` are no longer passive skeletons. They contain:
    *   Strict HTML Table statutes (preventing script injection needs).
    *   Self-validation instructions.
    *   Dynamic Header logic (no fixed H2s).

2.  **Persona Injection**:
    *   `keywords.json` now supports a `context` field.
    *   This is injected into the prompt via `{{context}}`, allowing per-keyword personas (e.g., "EV Engineer", "Safety Auditor").

3.  **Strict Mode**:
    *   The goal is for the LLM output to pass the `batch_blog_generation_aptpcb.py` checks *without* triggering any `repair_...` functions.

## Usage
Run with the standard script, pointing to this directory:

```bash
python batch_blog_generation_aptpcb.py \
  --prompts-dir prompts_aptpcb/blogs_prompt_v6 \
  --base-templates-dir prompts_aptpcb/blogs_prompt_v6/_base_templates \
  --strict-template
```
