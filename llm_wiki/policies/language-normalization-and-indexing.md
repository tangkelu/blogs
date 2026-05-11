# Language Normalization And Indexing Policy

Last updated: 2026-05-06

## Purpose

This policy prevents `llm_wiki` from drifting into parallel Chinese and English indexing trees for the same concept.

The knowledge base may ingest Chinese PDFs, Chinese headings, and Chinese source artifacts, but the reusable knowledge layer must normalize into a single English storage and retrieval surface.

## Core Rule

Use English as the canonical language for all reusable knowledge-layer storage and retrieval:

- `sources/registry/`
- `facts/`
- `wiki/`

Chinese may appear as source evidence or operator context, but it must not become a second canonical indexing path.

## Canonical Storage Rules

### 1. File naming

Use English slugs only for reusable knowledge files:

- source record filenames
- fact card filenames
- wiki page filenames

Do not create parallel Chinese and English files for the same concept.

### 2. Frontmatter identity

Use English canonical identifiers only:

- `source_id`
- `fact_id`
- `topic`
- `tags`

These fields define retrieval and deduplication boundaries, so they must stay in one language.

### 3. Body language

Use English for the main body of:

- source summaries
- fact cards
- wiki pages

This keeps retrieval, embedding, linking, and downstream prompt consumption on one language spine.

## Where Chinese Is Allowed

Chinese is allowed only in non-canonical or provenance-bearing contexts:

- raw source filenames and input paths such as PDF names
- quoted original headings when needed for provenance
- operator-facing maintenance logs under `logs/`
- temporary intake notes during claim inventory

Chinese should not be used as the primary title, topic, tag, or canonical summary language in reusable knowledge files.

## Translation And Alias Rules

When the source is Chinese:

1. extract the original Chinese faithfully into intake logs if needed
2. normalize the reusable concept into English before writing `sources/`, `facts/`, or `wiki/`
3. keep the original Chinese title only as provenance context, not as the retrieval key

Allowed pattern:

- English canonical title
- optional note mentioning the original Chinese source title or PDF filename

Disallowed pattern:

- one English fact card and one Chinese fact card for the same concept
- Chinese tags alongside English tags that create duplicate retrieval paths
- Chinese topic names in reusable frontmatter when an English canonical term exists

## Retrieval Rules

During maintenance or search:

- search Chinese source text when exploring raw intake
- write back only English-normalized reusable knowledge
- map synonymous Chinese source terms onto existing English canonical concepts instead of opening new parallel entries

Example:

- Chinese source term: `去耦电容`
- Canonical storage term: `decoupling capacitor`

The Chinese term can remain in logs or provenance notes, but the fact card, topic, tags, and wiki references must stay English.

## Special Case: Logs

`logs/` are operational documents, not the canonical knowledge layer.

Chinese is acceptable in logs for:

- operator notes
- user intent capture
- workflow explanations
- deletion-safe intake summaries

But even in logs, when naming reusable source/fact/wiki targets, prefer the English canonical file or identifier.

## Enforcement Guidance

Before creating a new reusable knowledge file:

1. check whether an English canonical concept already exists
2. merge Chinese-source evidence into that English concept if it does
3. create a new file only if the concept is genuinely new
4. keep Chinese only as provenance, not as the main retrieval surface

## Related Documents

- `policies/prompt-consumption-specification.md`
- `policies/ai-execution-contract.md`
- `README.md`
