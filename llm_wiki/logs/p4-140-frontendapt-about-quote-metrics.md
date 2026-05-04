---
task_id: "p4-140-frontendapt-about-quote-metrics"
status: "completed"
owner: "cascade-agent"
lane: "frontendAPT About + Quote 核心业务指标索引"
input_paths:
  - /code/hileap/frontendAPT/public/static/about/en/index.json
  - /code/hileap/frontendAPT/public/static/quote/en/index.json
output_paths:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-about-index-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-quote-index-en.md
  - /code/blogs/llm_wiki/facts/internal/frontendapt-business-metrics-boundary.md
  - /code/blogs/llm_wiki/logs/p4-140-frontendapt-about-quote-metrics.md
write_scope:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-about-index-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-quote-index-en.md
  - /code/blogs/llm_wiki/facts/internal/frontendapt-business-metrics-boundary.md
blocked_claims:
  - current real-time capacity utilization
  - current headcount accuracy
  - ISO certification current validity (unverified)
  - 24h/72h service level guarantees under all conditions
  - future performance predictions from historical return rate
  - pricing or MOQ specifics
completed_at: "2026-05-03"
---

# P4-140 frontendAPT About + Quote Metrics

## Scope

Index APTPCB core business profile and service commitment JSON files, extracting reusable company metrics, facility specifications, and service level context.

## Changes Made

### Source Records Created

**`frontendapt-about-index-en.md`** (NEW)
- Company overview with trust metrics table (Founded 2002, 20,000㎡ PCB, 4,500㎡ PCBA, 100,000㎡/mo capacity, 80 engineers, 5 SMT lines)
- History timeline (2002-2023 milestones)
- Factory specifications (PCB Factory Shenzhen, PCBA Factory with detailed metrics)
- Equipment highlights (LDI, Plating, Laser Drilling, SPI, SMT, X-ray)
- Quality control stages (DFM → NPI → Sourcing → IQC → Fab → SMT → Final)
- Business scope taxonomy (Design & NPI, Fabrication, Sourcing & Assembly, Inspection & Test)

**`frontendapt-quote-index-en.md`** (NEW)
- Service highlights (24h DFM, in-house stack-up/impedance/sourcing, Cloudflare R2 security)
- Response metrics table (24h quote, <0.1% return rate, 72h fastest delivery)
- SEO/service context for quote page

### Fact Card Created (Knowledge Increment)

**`frontendapt-business-metrics-boundary.md`** (NEW)
- Comprehensive company profile aggregation
- Facility scale matrix (Area, Capacity, Equipment)
- Certification inventory (ISO 9001, ISO 13485, IATF 16949, UL, CCC, CE, RoHS)
- History milestones table
- Service commitments table
- Technology capabilities (PCB + PCBA)
- Quality control 7-stage pipeline
- ERP/MES/Traceability systems context

## Knowledge Value Added

1. **Company Profile Boundary**: Reusable facts for About Us, RFP responses, investor materials
2. **Facility Scale Context**: 20,000㎡ + 4,500㎡ footprint with capacity figures
3. **Certification Inventory**: Structured list of claimed quality/regulatory certifications
4. **Service Commitment Baseline**: 24h DFM, 72h turnkey as stated service levels
5. **Quality Process Map**: 7-stage control pipeline from DFM to final delivery
6. **Historical Milestones**: 2002-2023 timeline for experience depth claims

## Critical Data Points Extracted

| Category | Key Data | Refresh Priority |
|----------|----------|------------------|
| **Facility** | 20,000㎡ PCB, 4,500㎡ PCBA | High |
| **Capacity** | 100,000㎡/mo PCB | High |
| **Headcount** | 800-1,000 workers, 80 engineers | Medium |
| **Certifications** | ISO 9001, ISO 13485, IATF 16949, UL | High |
| **Response Times** | 24h DFM, 72h turnkey | High |
| **Quality Metric** | <0.1% return rate | Medium |
| **SMT Lines** | 5 lines (Panasonic) | Medium |

## Residual Gaps

| Gap | Reason | Status |
|-----|--------|--------|
| Certification validity | ISO/IATF status not verified | `needs_review` |
| Current capacity utilization | Point-in-time from JSON | `blocked` |
| Real-time headcount | May have changed since source | `blocked` |
| Service level guarantees | Workload-dependent commitments | `blocked` |
| Equipment currency | SMT line models may have updated | `needs_review` |

## Currency Warnings

- **All metrics are point-in-time from JSON source (2026-05-03 check)**
- Facility sizes, capacity, headcount require verification before external use
- ISO certifications need current validity confirmation
- Service commitments (24h/72h) are workload-dependent
- Historical return rate (<0.1%) does not predict future performance

## Blocked Claims

- Current real-time capacity utilization or availability
- Current headcount accuracy (vs. source figures)
- ISO certification current validity (without verification)
- 24h/72h service level guarantees under all workloads
- Future performance predictions from historical data
- Pricing, MOQ, or specific customer terms
