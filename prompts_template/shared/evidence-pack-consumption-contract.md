# Evidence Pack Consumption Contract

This contract defines how `prompts_template` may consume `llm_wiki` evidence packs without inventing blocked PCB/PCBA numeric claims.

It applies to both `query.md` and `pillar.md`.

## 1. What an Evidence Pack May Contribute

An evidence pack may contribute only these input classes:

| Input class | Allowed use in prompt consumption |
| --- | --- |
| Usable facts | Facts marked `verified`. These may become outline decisions, body claims, tables, FAQ answers, and quick-answer material. |
| Safe wording | Scoped qualitative wording marked `framing_only`. These may support non-numeric framing, cautions, workflow language, and decision context. |
| Citation handles | Inline citation handles tied to `verified` facts. These may be attached to supported claims. |
| AI-SEO primitives | Definitions, quick answers, FAQ phrasing seeds, and section primitives, but only if they stay inside `verified` facts or `framing_only` wording. |
| Blocked claims | These may only be consumed as refusal signals, omission rules, or `DATA_GAP` markers. They must not be converted into article claims. |

Interpretation rules:

- `verified` facts are the only source for hard factual or numeric article claims.
- `framing_only` content may shape wording, but it may not be upgraded into thresholds, guarantees, or numerics.
- Citation handles do not upgrade unsupported content. A handle is usable only when the underlying claim is usable.

## 2. Hard Refusal Classes

The following classes are hard-blocked for shared prompt generation and must not be inferred, reconstructed, rounded, estimated, or generalized:

1. Shared `B` capability numerics:
   `trace/space`, minimum mechanical drill, minimum laser via, aspect ratio, annular ring, impedance tolerance, registration tolerance, and similar capability-table numerics.
2. Standards thresholds:
   `IPC Class 2 / 3 / 3A`, `IPC-6012 / 6013`, `IST`, `PLT`, coupon plans, plating minima, bow/twist limits, acceptance thresholds, and similar pass/fail criteria.
3. Supplier proof:
   supplier approval, qualification, compliance, release authority, accepted-lot status, transferable factory capability, or similar proof-style claims.
4. Process windows and recipes:
   lamination-count allowances, stack recipes, bake or press cycles, build-up defaults, manufacturability windows, and similar recipe claims.
5. High-speed or RF budget numerics:
   channel-loss budgets, insertion-loss tables, Nyquist-budget claims, RF geometry rules, and similar performance-budget numerics.
6. Dynamic commercial numerics:
   lead time, quick-turn windows, yield, cost uplift, MOQ, regional pricing, and similar time/cost/commercial numerics.

If a sentence needs one of these classes to sound convincing, the sentence must be downgraded or removed.

## 3. Status Handling

Each consumed fact or wording unit should be treated as one of these statuses:

| Status | Template behavior |
| --- | --- |
| `verified` | May be used as a factual claim. Numeric use is allowed only if the fact itself is `verified` and is not in a hard refusal class. |
| `framing_only` | May be used only for qualitative framing, workflow language, risk context, or scoped engineering judgment. No numerics, no thresholds, no proof claims. |
| `blocked` | Do not use in article content. Remove it or surface `DATA_GAP` internally. |
| `must_refresh` | Treat as unavailable until refreshed. Do not use in claims, tables, or FAQ answers. |
| `supplier_scoped_dated_only` | Not shared reusable authority. Exclude from normal `query` / `pillar` body generation. Only usable in a supplier-scoped dated note that preserves supplier, date, and scope exactly, without promotion to shared capability or proof. |

## 4. Required Reaction to Missing Verified Facts

When a prompt needs support that is not available as `verified`, templates must react in this order:

1. Downgrade to `framing_only` if a qualitative, scoped version is already supported.
2. Omit the sentence, table row, FAQ answer, or module if no safe downgrade exists.
3. Mark `DATA_GAP` in the working prompt or handoff note when the missing fact changes structure, comparison logic, or answer completeness.

Never:

- guess a number
- derive a threshold from adjacent wording
- convert supplier-scoped dated evidence into shared authority
- turn workflow naming, standards metadata, or overview copy into numeric proof

## 5. Minimal Preflight for `query` / `pillar`

Before a template consumes an evidence pack, confirm all of the following:

1. Every intended hard claim maps to a status label.
2. Every intended numeric claim maps to `verified` support and is outside the hard refusal classes.
3. Quick-answer, FAQ, and table content contain no blocked thresholds, capability numerics, supplier proof, or commercial numerics.
4. Site-specific capability statements are separated from shared factual framing.
5. Any unsupported but structurally important claim is downgraded, omitted, or marked `DATA_GAP` before generation starts.

If this checklist fails, the template should reduce scope instead of filling gaps.

## 6. Operating Rule

Evidence packs are permission boundaries, not inspiration pools.

If the pack does not clearly permit a factual claim, `prompts_template` must not invent it.
