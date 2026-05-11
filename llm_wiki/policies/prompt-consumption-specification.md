# Prompt Consumption Specification

Last updated: 2026-05-08

## Purpose

This document defines the rules for consuming `llm_wiki` content in downstream blog prompt execution. It establishes:

- Topic-level reuse conventions
- Downstream guardrails (safe vs blocked claims)
- Dynamic claim refresh handling
- Exclusion rules for `still_hold` topics

## Scope

Applies to all prompt execution against `llm_wiki` sources for blog content generation.

Canonical knowledge-layer language is English. Prompt retrieval should use English `fact_id`, `source_id`, wiki paths, and English canonical topic names even when the upstream source artifact was Chinese. See `policies/language-normalization-and-indexing.md`.

Exact-data prompt use is additionally governed by `policies/exact-data-admission-policy.md`.

---

## 1. Topic-Level Reuse Conventions

### 1.1 Source Hierarchy for Prompt Consumption

When building prompts, use sources in this priority order:

```
1. official_fact cards in facts/ admitted under exact-data-admission-policy.md
2. local_pdf_fact cards in facts/local_pdf/
3. other facts/
4. wiki/processes/ → Topic aggregation pages (for framing and context)
5. wiki/methods/   → Methodology and workflow guidance
6. wiki/materials/ → Material selection guidance
7. sources/registry/ → Raw source records (for citation only, not claims)
```

Do not consume raw `pdf_evidence/` or any `blocked_evidence` item as blog-body support unless it has been explicitly promoted into `facts/local_pdf/` or a stronger fact layer.

### 1.2 Citation Format in Prompts

| Source Type | Citation Format | Example |
|-------------|-----------------|---------|
| `official_fact` | `fact_id: {fact_id}` + preserve stated scope | `fact_id: methods-capacitor-parasitic-self-resonance-and-antiresonance-boundary` |
| `local_pdf_fact` | `fact_id: {fact_id}` + keep local-PDF scope wording | `fact_id: local-pdf-footprint-review-dimensions-visual-boundary` |
| Fact card | `fact_id: {fact_id}` | `fact_id: materials-panasonic-megtron-6` |
| Wiki page | `wiki/{category}/{slug}` | `wiki/processes/advanced-pcb-fabrication-and-stackup-planning` |
| Source record | `source_id: {source_id}` | `source_id: panasonic-megtron-6-datasheet` |

Never cite `blocked_evidence` or raw `pdf_evidence` as direct blog-body proof.

### 1.3 Topic-to-Prompt Mapping Rules

| Topic State | Prompt Treatment | Evidence Pack Status |
|-------------|------------------|---------------------|
| `go_now` | Full consumption allowed | Ready for prompt execution |
| `go_now_conservative` | Conservative consumption only | Must filter blocked claim classes |
| `mostly_ready` | Partial consumption | Requires section-by-section review |
| `still_hold` | Exclude from evidence packs | Do not use in prompt execution |
| `needs_refresh` | Refresh before use | Check `must_refresh` flags |

### 1.4 Exact-Data Consumption Rules

- Prefer `official_fact` cards first when the prompt needs formulas, tables, figures, or parameter data.
- `local_pdf_fact` may also be used in blog body when the card explicitly allows it and the prompt preserves the narrow scope wording.
- Preserve the scope stated on the fact card. Do not widen part-scoped, method-scoped, or local-PDF-scoped data into universal rules.
- Ignore all unresolved `secondary_pdf_claim_inventory_only` items and all `blocked_evidence` in downstream prompts.
- Do not cite local extracted image / table assets unless they are attached to an admitted `official_fact` or `local_pdf_fact` record.

---

## 2. Downstream Guardrails

### 2.1 Claim Class Safety Matrix

| Class | Description | Prompt Treatment | Example |
|-------|-------------|------------------|---------|
| **A** | Official material datasheet numerics | ✅ Safe to use with conditions | `MEGTRON 6 Dk 3.4 @ 10GHz` |
| **B** | Fabrication capability numerics | ⚠️ Allowed only if landed as scoped `official_fact` or `local_pdf_fact`; otherwise blocked | `±8% impedance tolerance` |
| **C** | Standards/qualification numerics | ❌ Blocked | `IPC Class 3 acceptance` |
| **D** | Board-level SI/EMC numerics | ⚠️ Allowed only if landed as scoped `official_fact` or `local_pdf_fact`; otherwise blocked | `10dB emissions reduction` |
| **E** | HDI/reliability/geometry numerics | ⚠️ Allowed only if landed as scoped `official_fact` or `local_pdf_fact`; otherwise blocked | `0.1mm blind via capability` |
| **F** | Dynamic commercial numerics | ❌ Blocked | `48-hour turnaround` |
| **G** | Supplier-status assertions | ❌ Blocked | `HILPCB certified supplier` |

### 2.2 Safe Claim Patterns

```
✅ SAFE:
- "According to Panasonic's published MEGTRON 6 data..."
- "According to the admitted exact-data card for the named part or method..."
- "In this accepted local PCB资料 figure, the diagram illustrates..."
- "This handbook example is usable here only as a scoped local visual explanation..."
- "Stackup planning should consider..."
- "Validation typically includes TDR or coupon measurement..."
- "Material selection depends on loss budget and thermal constraints..."

❌ BLOCKED:
- "A handbook table shows..."
- "This PDF rule proves..."
- "The official standard requires..." when the source is only `local_pdf_fact`
- "The manufacturer datasheet proves..." when the source is only `local_pdf_fact`
- "This local handbook figure proves the supplier is certified or currently capable..."
- "Our 6-layer PCBs achieve ±8% impedance tolerance..."
- "We guarantee 100% electrical testing coverage..."
- "Standard lead time is 48 hours..."
- "We are IPC Class 3 certified..."
```

### 2.3 Section-Level Treatment Rules

| Blog Section | Safe Treatment | Blocked Treatment |
|--------------|--------------|-------------------|
| Capability banner | Exclude entirely | Retain unsupported numerics |
| Material selection | Exact product anchors only | Generic family ladders |
| Stackup discussion | Architecture framing only | Recipe tables with hard numbers |
| Impedance control | Verification posture only | Width tables, tolerance claims |
| Via strategies | Vocabulary only | Size/cost/escape tables |
| DFM rules | Qualitative prompts only | Feature-size thresholds |
| Cost/lead-time | Exclude entirely | Dynamic commercial claims |
| Supplier CTA | Neutral next-step only | Capability/service promises |

---

## 3. Dynamic Claim Refresh Checklist

### 3.1 Must-Refresh Indicators

A claim MUST be refreshed if:

- [ ] `must_refresh: true` in source metadata
- [ ] HIL capability or service promise
- [ ] Lead time, cost, or turnaround claim
- [ ] Current certification or approval status
- [ ] Material availability or stock claim
- [ ] Internal tolerance or validation scope

### 3.2 Refresh Process

```
1. Identify refresh-sensitive claim
2. Check if governed refresh path exists
3. If yes: refresh from current primary source
4. If no: exclude from evidence pack
```

### 3.3 Date-Sensitive Claims

| Claim Type | Max Age | Action if Stale |
|------------|---------|-----------------|
| Material datasheet values | 2 years | Re-verify from official source |
| Supplier capability numbers | 6 months | Exclude pending refresh |
| Certification status | 3 months | Exclude pending refresh |
| Commercial terms | 1 month | Exclude pending refresh |

---

## 4. Still_Hold Topic Exclusion Rules

### 4.1 Exclusion List (Current)

| Topic | Status | Reason |
|-------|--------|--------|
| `20-layer-pcb-manufacturing` | `still_hold` | Missing HIL-specific geometry/process-window numerics |
| `22-layer-pcb-manufacturing` | `still_hold` | Missing Class 3/3A threshold, supplier qualification |
| `dna-computing-pcb` | `still_hold` | Missing owner platform, material, capability authority |
| `biological-computing-pcb` | `still_hold` | Missing biointerface, material-suitability authority |
| `taconic-rf-ptfe` (exact product) | `hold_first` | Missing current Taconic product-grade datasheets |
| `arlon-rf-ptfe` (exact product) | `blocked` | Missing current Arlon RF product pages |

### 4.2 Hold Reopening Conditions

A `still_hold` topic may reopen only if:

1. Exact new authority recovered (official datasheet, dated supplier record)
2. Narrow dated supplier evidence obtained
3. Controller explicitly approves via `logs/phase-status.md` update

### 4.3 Hold Maintenance

- Do NOT attempt source recovery for hold topics by default
- Do NOT create bridge-prep notes for hold topics
- Monitor monthly for new official source availability
- Log hold decisions in `logs/phase-status.md`

---

## 5. Evidence Pack Assembly Rules

### 5.1 Required Evidence Pack Sections

Every evidence pack must include:

1. **Traceability Core**: topic, scope, template, fact_ids, source_ids, authority layer
2. **Topic Summary**: keywords, page type, target reader
3. **Source Facts**: Usable hard anchors from `llm_wiki`
4. **Claim Extraction**: Table mapping current draft claims to disposition
5. **Classification**: `official_fact` / `local_pdf_fact` / Site references / `blocked_evidence` / Unsupported
6. **Handoff To Template**: Recommended prompt structure

### 5.2 Evidence Pack Location

- Store completed evidence packs in: `wiki/consumption/`
- Naming convention: `{layer}-layer-evidence-pack.md` or `{topic}-evidence-pack.md`
- Link from bridge-prep notes in `logs/`

### 5.3 Pack Quality Gates

Before marking an evidence pack complete:

- [ ] All `fact_id` references verified existing in `facts/`
- [ ] All `source_id` references verified existing in `sources/registry/`
- [ ] Any exact formula/table/parameter claim is backed by an admitted `official_fact` or explicitly allowed `local_pdf_fact`
- [ ] No unsupported B/C/D/E/F/G numerics in usable section
- [ ] `blocked_evidence` and unresolved secondary-PDF-only formulas/tables/figures are excluded from usable sections
- [ ] `must_refresh` flags identified and documented
- [ ] Section-by-section bridge guidance complete
- [ ] Conflicts and open gaps documented

---

## 6. Prompt Execution Checklist

Before executing a prompt with evidence pack:

- [ ] Verify topic status is `go_now` or `go_now_conservative`
- [ ] Confirm evidence pack passes quality gates
- [ ] Prefer `official_fact` first when the prompt asks for exact parameters, formulas, or table values
- [ ] If using `local_pdf_fact`, preserve the card's narrow local-source wording and non-claims
- [ ] Check `must_refresh` items are current
- [ ] Exclude any `blocked_evidence` or unresolved secondary-PDF-only data that was not admitted under `exact-data-admission-policy.md`
- [ ] Review blocked claim classes are excluded
- [ ] Ensure wiki pages used only as secondary framing
- [ ] Validate all in-body citations have traceable sources

---

## 7. Related Documents

| Document | Purpose |
|----------|---------|
| `logs/phase-status.md` | Current topic readiness states |
| `logs/en-layer-count-blog-generation-gate.md` | Layer-count specific gates |
| `policies/ai-execution-contract.md` | Primary operating contract |
| `policies/exact-data-admission-policy.md` | Admission and downstream use rules for exact-data extracted from secondary PDFs |
| `logs/p4-06-*-evidence-pack.md` | First-wave evidence pack examples |

---

## 8. Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-05-02 | Initial specification for Phase 5 | AI Assistant |
| 2026-05-08 | Added `official_fact` + `local_pdf_fact` + `blocked_evidence` downstream contract for `PCB资料` first slice | AI Assistant |

---

*This document is a living policy. Updates require explicit controller approval logged in `logs/phase-status.md`.*
