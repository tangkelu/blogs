# T9/T10 Assessment: 20-Layer and 22-Layer PCB Capability Evaluation

**Date**: 2026-05-02
**Assessment ID**: T9-T10-EVAL-20260502
**Status**: COMPLETE - Both layers remain `still_hold`

---

## Executive Summary

| Layer | General Capability | Specific Evidence | Status | Verdict |
|-------|-------------------|-------------------|--------|---------|
| **20-layer** | ✅ Confirmed (64-layer capable) | ❌ Insufficient | `still_hold` | Data gaps in process windows, supplier evidence |
| **22-layer** | ✅ Confirmed (64-layer capable) | ❌ Insufficient | `still_hold` | Data gaps in qualification, acceptance authority |

**Conclusion**: While APTPCB has confirmed **64-layer manufacturing capability** which technically includes 20/22 layers, the specific evidence required for high-density numeric reuse remains missing. Both layers **cannot be upgraded to `go_now`** at this time.

---

## T9: 20-Layer Assessment

### ✅ Available Evidence (Sufficient for General Capability)

| Source | Evidence | Status |
|--------|----------|--------|
| `apt-rigid-pcb-capability-page.md` | Up to 64 layers rigid PCB | ✅ Confirmed |
| `high-layer-count-pcb.json` | 12-64 layer fabrication services | ✅ Confirmed |
| `multilayer-pcb.json` | 4-32 layers, HDI builds to 40 | ✅ Confirmed |
| `rigid-pcb.json` | Max 64 layers, HDI 1-3 SBU | ✅ Confirmed |
| `apt-pcb-process-technologies-summary.md` | Sequential lamination, backdrill, registration | ✅ Confirmed |

### ❌ Missing Evidence (Blocking `go_now` upgrade)

| Gap Category | Specific Missing Data | Impact |
|--------------|----------------------|--------|
| **Geometry Tables** | 20-layer specific trace/space, via diameter, pad size | Cannot claim exact manufacturability |
| **Process Windows** | Lamination recipes for 20-layer stacks | Cannot claim process stability |
| **IST/Coupon Plans** | 20-layer thermal cycle thresholds, cross-section plans | Cannot claim reliability proof |
| **HIL-Specific Claims** | HIL capability for 20-layer builds | Marketing claims blocked |
| **Supplier Evidence** | Dated supplier records for 20-layer production | No external verification |
| **Aspect Ratio Data** | 20-layer specific aspect ratio limits | Deep hole plating unverified |

### Controller Decision (per P4-113)

```
20-layer remains blocked because the missing ceiling is concentrated in:
- geometry / process-window / method-to-qualification / HIL-specific proof

Permanent exclusion under current corpus:
- geometry and feature-size tables
- via diameter, pad, aspect-ratio, registration numerics
- lamination-count defaults and stack-recipe claims
- IST, thermal-cycle, coupon numerics
- HIL-specific capability, process-control, production claims
```

---

## T10: 22-Layer Assessment

### ✅ Available Evidence (Sufficient for General Capability)

Same as 20-layer - all general 64-layer capability evidence applies.

### ❌ Missing Evidence (Blocking `go_now` upgrade)

| Gap Category | Specific Missing Data | Impact |
|--------------|----------------------|--------|
| **Class 2/3/3A Thresholds** | IPC-6012 acceptance criteria for 22-layer | Cannot claim compliance |
| **Qualification Authority** | Supplier listing, QML status | Cannot claim qualified source |
| **Lot Conformance** | PLT sample plans, acceptance rules | Cannot claim lot-level proof |
| **HIL Compliance Claims** | HIL-specific qualification packages | Marketing claims blocked |
| **Outgassing Data** | 22-layer screening acceptance numerics | Space/military claims blocked |
| **Addendum Tables** | IPC-6012 addendum technical requirements | Cannot claim automotive/medical |

### Controller Decision (per P4-113)

```
22-layer remains blocked because the missing ceiling is concentrated in:
- threshold reconstruction / workflow-to-acceptance collapse / lot-release implication / HIL-specific compliance-proof

Permanent exclusion under current corpus:
- Class 2/3/3A threshold tables
- IPC-6012/6013 acceptance thresholds
- IST, thermal-cycle, screening numerics as qualification proof
- PLT sample-plan numerics, accepted-lot rules
- HIL-specific compliance, qualification-package claims
```

---

## Layer-Count Readiness Comparison

| Layer | Status | Conservative Rewrite | High-Density Numeric |
|-------|--------|---------------------|---------------------|
| 6-layer | `go_now` | ✅ Supported | ✅ Available |
| 8-layer | `go_now` | ✅ Supported | ✅ Available |
| 10-layer | `go_now` | ✅ Supported | ✅ Available |
| 12-layer | `go_now` | ✅ Supported | ✅ Available |
| 14-layer | `go_now` | ✅ Supported | ⚠️ Partial |
| 16-layer | `go_now` | ✅ Supported | ⚠️ Partial |
| 18-layer | `mostly_ready` | ✅ Supported | ❌ Blocked |
| **20-layer** | **still_hold** | ⚠️ Reduced only | ❌ **Blocked** |
| **22-layer** | **still_hold** | ⚠️ Reduced only | ❌ **Blocked** |
| 24-layer | `mostly_ready` | ✅ Supported | ❌ Blocked |

---

## Specific Data Gaps Summary

### For 20-Layer Unlock (Future T9 Re-evaluation)

Required evidence categories:
1. **Exact 20-layer geometry tables** (trace/space, drill, pad, aspect ratio)
2. **20-layer stack recipes** (lamination cycles, material specs)
3. **IST qualification data** (thermal cycles, coupon pass/fail)
4. **HIL 20-layer production records** (dated capability evidence)
5. **Process window documentation** (registration, impedance on thin dielectric)

### For 22-Layer Unlock (Future T10 Re-evaluation)

Required evidence categories:
1. **IPC Class 3/3A threshold tables** specific to 22-layer
2. **Supplier qualification listing** (QML, QPL status)
3. **Lot acceptance criteria** (PLT plans, sample sizes)
4. **HIL 22-layer qualification package**
5. **Outgassing/screening acceptance numerics**

---

## Recommendations

### Immediate Actions
1. **Keep 20/22 layer on `still_hold`** - Do not upgrade to `go_now`
2. **Do not create 20/22 specific fact cards** - Insufficient specific authority
3. **Continue using general 64-layer capability** for conservative drafting only

### Future Unlock Paths

| Path | Evidence Required | Likelihood |
|------|------------------|------------|
| HIL capability records | Dated internal records for 20/22 layer builds | Medium |
| Supplier evidence | Narrow dated supplier records | Low-Medium |
| Standards authority | IPC-6012 addendum technical tables | Low (requires purchase) |
| Primary authority | Official test results, qualification reports | Low |

### Alternative: Conservative Rewrite Only

For `20-layer` and `22-layer` topics, use:
- General high-layer-count framing (12-64 layers)
- HDI/build-up workflow language
- Material-family discussion
- Non-numeric manufacturability context

Avoid:
- Exact 20/22 layer process claims
- Geometry tables
- Qualification assertions
- HIL-specific marketing

---

## Source Files Referenced

### Capability Sources
- `/code/blogs/llm_wiki/sources/registry/capabilities/apt-rigid-pcb-capability-page.md`
- `/code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json`
- `/code/hileap/frontendAPT/public/static/pcb/en/high-layer-count-pcb.json`
- `/code/hileap/frontendAPT/public/static/pcb/en/multilayer-pcb.json`

### Controller Decision Sources
- `/code/blogs/llm_wiki/logs/p4-113-2026-5-1-20-22-layer-blocker-closure-sheets-and-permanent-exclusion-path.md`
- `/code/blogs/llm_wiki/logs/layer-count-blog-readiness.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`

---

**Assessment Completed**: 2026-05-02
**Next Re-evaluation Trigger**: Exact new authority or narrow dated supplier evidence for 20/22 layer specific claims
