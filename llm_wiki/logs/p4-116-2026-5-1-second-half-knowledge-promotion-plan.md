# P4-116 2026-05-01 Second-Half Knowledge Promotion Plan

Date: 2026-05-01

Status: `execution_integrated`

## Purpose

Turn the remaining half of the `llm_wiki` goal into a durable multi-agent execution map that prioritizes source-backed knowledge promotion over rewrite-layer completion.

## Current Position

- `llm_wiki` already has large standing asset coverage in `sources/`, `facts/`, and `wiki/`.
- All current dated English `tmps/*/en` batches are deletion-safe at claim-family or routing level.
- This is not the same as full source-backed learning.
- Most of the roughly `715` English drafts still need official-source recovery, fact extraction, wiki aggregation, or narrower authority promotion before they are knowledge-complete.

## Work Buckets

### 1. High-Value Source-Gap Lanes

- `grounding-and-return-path-execution-boundary`
- `optical-module-handling-contamination-control`
- `Taconic product-grade official datasheet anchors`
- `Arlon product-grade official datasheet anchors`
- `compute exact interface / cooling / deployment boundary strengthening`

These lanes have the best value-to-effort ratio because each can promote reusable knowledge without reopening broad draft-layer work.

Current audit note:

- `grounding-and-return-path-execution-boundary` ended `source_backed_fact_layer_partial`
- `optical-module-handling-contamination-control` ended `source_backed_fact_layer_partial`
- `Taconic product-grade official datasheet anchors` ended `remains_hold_due_to_missing_current_authority`
- `Arlon product-grade official datasheet anchors` ended `fact_partial` through the new `86HP` exact-product branch
- the compute lane remains the only Batch B lane that can support a narrow wiki aggregation without new fact claims

### 2. Partial Fact-Layer Lanes Needing Promotion

- `rf-cable-beyond-coax-identity`
- `encoder-beyond-digital-priority-identity`
- `ohms-law-and-watts-to-amps chain`
- `bom-hdi-cost-governance residual`
- `2026.4.27 exact-claim promotion`
- `2026.4.29 exact-claim promotion`

These lanes already have narrow partial support, but they are still below the threshold for broader reusable fact-layer confidence.

### 3. Large Corpus Lanes Still Only Deletion-Safe

- full `/tmps` English corpus
- `2026.4.27/en`
- `2026.4.29/en`
- `HILPCB Blog1-13 input-device drafts`
- `APTPCB260401 2-layer drafts`
- `2025.7 mixed service drafts`

These remain the largest long-run gap between routing-level learning and source-backed knowledge completion.

### 4. Explicit Holds

Keep these closed unless new evidence changes the ceiling:

- `biological-computing`
- `20-layer`
- `22-layer`
- `tmps/materias_pdf`
- `grounding-and-return-path-execution-boundary` until new source appears
- `optical-module-handling-contamination-control` until new source appears

## Do-Not-Reopen Reuse Areas

Future work should consume these layers rather than reopen generic rewrite / normalization loops:

- embedded imaging serial-interface boundaries
- thermal-imaging output / video / machine-vision interface boundaries
- EO/IR detector owner-identity review boundaries
- RF validation and staged validation coverage
- PCB design data-exchange / tool boundaries

## First Batch After P4-116

### Batch A: Narrow Source Recovery

Priority order:

1. `grounding-and-return-path-execution-boundary`
2. `optical-module-handling-contamination-control`
3. `Taconic product-grade official datasheet anchors`
4. `Arlon product-grade official datasheet anchors`

Expected artifact types:

- `sources/registry/*`
- `facts/*`
- only add `wiki/*` if the new fact set creates reusable aggregation value

### Batch B: Promotion From Routing To Reusable Facts

Priority order:

1. `compute exact interface / cooling / deployment boundary strengthening`
2. `ohms-law-and-watts-to-amps chain`
3. `current-carrying / high-current layout strengthening`

Expected artifact types:

- narrow `facts/*`
- reuse existing `wiki/*` where possible
- avoid broad topic rewrites

Current audit note:

- compute remains a narrow boundary aggregation until exact cooling or deployment evidence appears
- `ohms-law` and `watts-to-amps` remain limited to stitching the existing formula-identity, current-carrying, and conservative-generation-gate pages together; no new capability facts should be added

### Batch C: Corpus-Level Backlog Sweep

Target families:

- `2026.4.27/en` residual exact claims
- `2026.4.29/en` residual exact claims
- `HILPCB Blog1-13`
- `APTPCB260401 2-layer`
- `2025.7 mixed service drafts`

This batch should stay at inventory-plus-promotion planning unless one sublane has clear official-source recovery value.

## Multi-Agent Pattern

- subagent lane 1: source-gap narrowing
- subagent lane 2: existing fact/wiki reuse and conflict check
- subagent lane 3: residual batch inventory / claim-family narrowing
- main agent: artifact promotion, tracker updates, hold enforcement, verification

## Stop Rules

Stop a lane and return it to hold if:

- only draft-layer cleanup remains
- only `logs/` support exists
- the next claim needs numbers, compliance proof, supplier proof, or capability proof without new authority

## Exit Condition

This “second half” plan is complete only when the next execution batches are driven by source-backed lane promotion rather than by rewrite-layer continuation.
