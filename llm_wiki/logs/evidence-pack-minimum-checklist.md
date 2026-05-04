# Evidence Pack Minimum Checklist

Use this checklist when a prompt consumes `llm_wiki` as the source layer.

## Required Inputs

- Topic or question being written.
- Target output type: query, pillar, comparison, capability, or other.
- Required scope limits: geography, product line, process, standard, or timeframe.
- Freshness requirement: whether the answer may use cached facts or must re-check now.
- Allowed source classes for the task, if narrower than default governance.

## Source Hierarchy

1. Standard / regulatory source.
2. Original manufacturer / datasheet / processing guide.
3. Official filing, annual report, or official product page.
4. Official dataset or public database.
5. Internal engineering review record.
6. Internal blog or note only as secondary support.
7. External blog, SEO article, reseller copy, or forum post only for background, never as primary fact support.

Lower-priority sources must not override higher-priority sources.

## Must Refresh Handling

- Treat price, lead time, capacity, certification status, market numbers, exemption status, and current regulatory cutoffs as dynamic.
- Mark any dynamic item `must_refresh: true`.
- Require `published_at` and `checked_at` for any dynamic item that is used in the pack.
- Before publishing, re-check official sources for any dynamic item or any value that depends on a live revision, status, or cutoff.
- If refresh cannot be completed, downgrade the claim, label it as unverified, or reject it.

## Evidence Pack Shape

- One topic, one evidence pack.
- Include:
  - `topic`
  - `scope`
  - `fact_ids`
  - `source_ids`
  - `must_refresh`
  - `conflicts`
  - `notes`
- Keep facts atomic. One fact card should support one claim.
- Keep judgments separate from facts. Do not merge interpretation into the fact list.
- Keep conflicts visible. Do not flatten contradictory sources into one statement.

## Citation and Fact IDs

- Every claim used by the prompt must map to at least one `fact_id`.
- Every `fact_id` must map back to one or more `source_id`s.
- If factual support is claimed, the pack must carry traceable `fact_id` + `source_id` pairs.
- Use stable IDs only. Do not invent temporary labels in the prompt output.
- If a claim has no valid `fact_id`, it is not eligible for publication.
- If a source is used, cite the source ID alongside the fact ID in the evidence pack.

## Reject Conditions

Reject the evidence pack if any of the following are true:

- No primary source is present for a high-risk or technical claim.
- A dynamic claim is present without `must_refresh: true`.
- The pack contains a number, limit, or certification status without date or conditions.
- A lower-priority source is used to override a higher-priority source.
- The pack hides a known conflict instead of marking it.
- A claim cannot be traced to a `fact_id` and `source_id`.
- The prompt asks for a live status, but the pack is stale or unverified.

## Minimum Acceptance Rule

The pack is not prompt-consumable unless every claim, judgment, and capability unit has a canonical status label.

If the pack does not support a unit with traceable facts, governed sources, and current refresh status, do not use it to write the blog.
