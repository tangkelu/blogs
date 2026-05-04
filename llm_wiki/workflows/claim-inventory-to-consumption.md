# Claim Inventory to Consumption Workflow

**Workflow ID**: `wf-claim-inventory-to-consumption`
**Version**: 1.0
**Date**: 2026-05-02
**Status**: Active

---

## Purpose

Define the standardized workflow for processing new blog content requests through the `llm_wiki` source-backed knowledge system.

This workflow ensures:
- Claims are inventoried before writing
- Source gaps are identified explicitly
- Recovery is attempted for gaps
- Facts are created only from verified sources
- Wiki aggregation happens after fact layer
- Consumption (evidence packs) is the final step

---

## Workflow Stages

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1. Claim       │───→│  2. Source Gap  │───→│  3. Recovery    │
│   Inventory     │    │    Analysis     │    │   Attempt       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
        ┌───────────────────────────────────────────────┘
        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  4. Fact        │───→│  5. Wiki        │───→│  6. Consumption │
│   Creation      │    │  Aggregation    │    │   (Evidence Pack)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
        ┌───────────────────────────────────────────────┘
        ▼
┌─────────────────┐
│  7. Prompt      │
│   Execution     │
└─────────────────┘
```

---

## Stage 1: Claim Inventory

### Input
- New blog topic or rewrite request
- Existing blog drafts (if rewrite)
- Target keywords and search intent

### Actions

1. **Extract all claims** from request or existing draft
   - Capability claims (e.g., "we achieve ±8% tolerance")
   - Performance claims (e.g., "supports PCIe Gen6")
   - Material claims (e.g., "uses MEGTRON 6")
   - Process claims (e.g., "48-hour turnaround")
   - Certification claims (e.g., "IPC Class 3 certified")

2. **Classify each claim** using Claim Class Matrix:

| Class | Description | Example | Usability |
|-------|-------------|---------|-----------|
| **A** | Official material datasheet | "MEGTRON 6 Dk 3.4 @ 10GHz" | ✅ Safe |
| **B** | Fabrication capability | "±8% impedance tolerance" | ❌ Blocked |
| **C** | Standards/qualification | "IPC Class 3 certified" | ❌ Blocked |
| **D** | Board-level SI/EMC | "10dB emissions reduction" | ❌ Blocked |
| **E** | HDI/reliability | "0.1mm blind via capability" | ❌ Blocked |
| **F** | Dynamic commercial | "48-hour turnaround" | ❌ Blocked |
| **G** | Supplier-status | "HILPCB certified supplier" | ❌ Blocked |

3. **Create claim inventory document**

```yaml
# Template: workflows/inventory/{topic}-claim-inventory.md
claim_inventory:
  topic: "6-layer PCB manufacturing"
  date: "2026-05-02"
  
  claims:
    - id: C001
      text: "6-layer PCBs achieve ±8% impedance tolerance"
      class: B
      status: blocked
      reason: "No fabrication capability layer"
      
    - id: C002
      text: "MEGTRON 6 has Dk 3.4 at 10GHz"
      class: A
      status: needs_source
      target_source: "Panasonic MEGTRON 6 datasheet"
      
    - id: C003
      text: "48-hour quick-turn service"
      class: F
      status: must_refresh
      refresh_path: "HIL current service status"
```

### Output
- `workflows/inventory/{topic}-claim-inventory.md`
- List of A-class claims needing source recovery
- List of blocked claims (B-G) for exclusion
- List of claims requiring refresh

---

## Stage 2: Source Gap Analysis

### Input
- Claim inventory (A-class claims needing sources)
- Existing `sources/registry/` coverage

### Actions

1. **Check existing sources** for each A-class claim
   ```
   Search sources/registry/ for:
   - Material datasheets
   - Product pages
   - Official specifications
   ```

2. **Identify source gaps**

| Claim | Required Source | Exists? | Gap Type |
|-------|-----------------|-----------|----------|
| MEGTRON 6 values | Panasonic datasheet | ✅ Yes | None |
| Taconic RF-35 | Taconic product page | ❌ No | Missing source |
| IT-180A Tg | ITEQ product page | ⚠️ Partial | Needs verification |

3. **Categorize gaps**

- **Recoverable**: Official source exists but not yet registered
- **Hold**: No current official source available (e.g., Taconic RF)
- **Refresh needed**: Source exists but may be stale

### Output
- `workflows/gaps/{topic}-source-gaps.md`
- List of sources to recover
- List of holds (cannot proceed)
- Refresh priorities

---

## Stage 3: Source Recovery

### Input
- Source gap analysis
- Official manufacturer websites

### Actions

1. **Attempt recovery for each gap**

```
For each missing source:
  1. Search official manufacturer website
  2. Locate product page or datasheet
  3. Verify URL is current (not 404/redirected)
  4. Extract metadata (date, version, scope)
  5. Register in sources/registry/
```

2. **Recovery outcomes**

| Outcome | Action | Example |
|---------|--------|---------|
| ✅ Found | Register source | `sources/registry/materials/panasonic-megtron-6-datasheet.md` |
| ❌ Not found | Mark hold | `facts/materials/taconic-official-source-coverage-gap.md` |
| ⚠️ Partial | Note limitations | Source exists but missing key parameters |

3. **Create source records** (for successful recovery)

```yaml
# Template: sources/registry/{category}/{source-id}.md
---
source_id: "panasonic-megtron-6-datasheet"
source_type: "datasheet"
manufacturer: "Panasonic"
product_family: "MEGTRON"
product_grade: "MEGTRON 6 R-5775(N)"
url: "https://..."
date_accessed: "2026-05-02"
url_status: "live"
content_scope: "Electrical properties, thermal properties, laminate specs"
---
```

### Output
- New source records in `sources/registry/`
- Hold notes for unrecoverable sources
- Recovery attempt log

---

## Stage 4: Fact Creation

### Input
- Recovered source records
- A-class claims from inventory

### Actions

1. **Create atomic fact cards** from verified sources

```yaml
# Template: facts/{category}/{fact-id}.md
---
fact_id: "materials-panasonic-megtron-6"
title: "Panasonic MEGTRON 6 official properties"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
source_ids:
  - "panasonic-megtron-6-datasheet"
---

# Canonical Summary

> Panasonic MEGTRON 6 (R-5775N) public datasheet gives Tg 185°C, 
> Td 410°C, Dk ~3.4-3.7, Df <0.004 depending on frequency and grade variant.

## Stable Facts

- Tg: 185°C (DSC)
- Td: 410°C (TGA 5% weight loss)
- Dk @ 10GHz: ~3.4 (process-dependent)
- Df @ 10GHz: <0.004
```

2. **Fact creation rules**

| Rule | Implementation |
|------|----------------|
| One claim per fact | Atomic fact cards |
| Source attached | Every fact has `source_ids` |
| Conditions included | Frequency, grade, temperature context |
| Limits explicit | What the fact does NOT claim |

3. **Handle blocked claims**

- B-G class claims → No fact created
- Document in gap notes
- Do not attempt workaround

### Output
- `facts/{category}/{fact-id}.md` files
- Each fact linked to source(s)
- Gap notes for blocked claims

---

## Stage 5: Wiki Aggregation

### Input
- Fact cards (from Stage 4)
- Topic boundary requirements

### Actions

1. **Create or update wiki aggregation pages**

```yaml
# Template: wiki/{category}/{topic-aggregation}.md
---
wiki_id: "wiki/processes/6-layer-pcb-manufacturing"
title: "6-Layer PCB Manufacturing Guide"
category: "processes"
fact_ids:
  - "materials-panasonic-megtron-6"
  - "materials-iteq-it-180a"
  - "methods-controlled-impedance-tdr-verification-posture"
---

## Overview

Guidance for 6-layer PCB manufacturing decisions based on 
source-backed material and method facts.

## Material Selection

See fact cards for exact-product material properties:
- `materials-panasonic-megtron-6`
- `materials-iteq-it-180a`
```

2. **Aggregation rules**

| Rule | Implementation |
|------|----------------|
| Reference facts | Wiki references `fact_ids`, does not duplicate |
| Add context | Design guidance, tradeoffs, planning |
| No new numerics | Wiki does not introduce un-sourced numbers |
| Link to sources | Citation paths maintained |

### Output
- `wiki/{category}/{topic-aggregation}.md`
- Aggregation of facts with context
- No unsupported claims

---

## Stage 6: Consumption (Evidence Pack)

### Input
- Fact cards (atomic)
- Wiki aggregations (context)
- Source records (traceability)

### Actions

1. **Create evidence pack** for prompt consumption

```yaml
# Template: wiki/consumption/{topic}-evidence-pack.md
---
pack_id: "consumption-6-layer-pcb"
topic: "6-layer PCB manufacturing"
status: "go_now_conservative"
template: "prompts_template/shared/query.md"

fact_ids:
  - "materials-panasonic-megtron-6"
  - "materials-iteq-it-180a"
  # ... (all usable facts)
  
source_ids:
  - "panasonic-megtron-6-datasheet"
  - "iteq-it-180a-page"
  # ... (all primary sources)

must_refresh:
  - claim: "Lead time promises"
    value: true
  - claim: "Cost estimates"
    value: true

excluded_classes:
  - "B: Fabrication capability numerics"
  - "C: Standards thresholds"
  - "F: Commercial claims"
---

## Traceability Core
## Topic Summary
## Usable Technical Facts
## Claim Extraction & Disposition
## Handoff to Template
```

2. **Evidence pack quality gates**

| Gate | Check |
|------|-------|
| All facts verified | Every `fact_id` exists in `facts/` |
| All sources live | Every `source_id` has current URL |
| No B-G numerics | Blocked claims excluded |
| Must-refresh flagged | Dynamic claims identified |
| Wiki framing only | Wiki pages as secondary support |

### Output
- `wiki/consumption/{topic}-evidence-pack.md`
- Ready for prompt template consumption
- All claims traceable to sources

---

## Stage 7: Prompt Execution

### Input
- Evidence pack
- Prompt template

### Actions

1. **Load evidence pack** into prompt context
2. **Execute template** with evidence constraints
3. **Generate content** using only evidenced claims
4. **Log execution** in `logs/update-log.md`

### Output
- Generated blog content
- Source-backed citations in content
- Execution log entry

---

## Workflow Integration

### Entry Points

| Trigger | Action | Creates |
|---------|--------|---------|
| New blog request | Start Stage 1 | Claim inventory |
| Rewrite request | Start Stage 1 + analyze existing | Gap analysis |
| Source discovered | Start Stage 3 | Source record + Fact |
| Fact verified | Start Stage 5 | Wiki update |
| Wiki complete | Start Stage 6 | Evidence pack |

### Exit Conditions

| Condition | Next Step |
|-----------|-----------|
| Source gap unrecoverable | Hold topic, update gap notes |
| Evidence pack ready | Proceed to Stage 7 |
| Must-refresh items stale | Return to Stage 3 |

---

## File Structure

```
llm_wiki/
├── workflows/
│   └── claim-inventory-to-consumption.md    (this file)
│   └── inventory/
│       └── {topic}-claim-inventory.md       (Stage 1 output)
│   └── gaps/
│       └── {topic}-source-gaps.md           (Stage 2 output)
├── sources/
│   └── registry/
│       └── {category}/
│           └── {source-id}.md               (Stage 3 output)
├── facts/
│   └── {category}/
│       └── {fact-id}.md                     (Stage 4 output)
├── wiki/
│   └── {category}/
│       └── {topic-aggregation}.md           (Stage 5 output)
│   └── consumption/
│       └── {topic}-evidence-pack.md         (Stage 6 output)
└── logs/
    └── update-log.md                        (Stage 7 tracking)
```

---

## Related Documents

| Document | Purpose |
|----------|---------|
| `policies/prompt-consumption-specification.md` | Consumption layer rules |
| `policies/ai-execution-contract.md` | Primary operating contract |
| `logs/phase-status.md` | Topic readiness tracking |
| `logs/en-layer-count-blog-generation-gate.md` | Layer-count specific gates |

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2026-05-02 | 1.0 | Initial workflow definition (T21) |

---

*This workflow enforces source-backed promotion over rewrite expansion.*
