# Lane Log: P4-152 HIL Assembly Capability Aggregation

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-152-hil-assembly-capability-aggregation` |
| `lane` | `HIL assembly capability aggregation` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Land a dedicated HIL assembly aggregation layer instead of leaving HIL assembly knowledge only indirectly absorbed into shared APT/HIL PCBA pages |
| `write_scope` | `facts/processes/`, `wiki/processes/`, `logs/p4-152-hil-assembly-capability-aggregation.md` |

---

## Inputs Read

| File | Role |
|------|------|
| `facts/processes/hil-smt-assembly-capability-specs.md` | SMT placement, stencil, inspection, quality metrics |
| `facts/processes/hil-through-hole-assembly-capability-specs.md` | Wave/selective/robotic solder, barrel fill, press-fit, testing |
| `facts/processes/hil-small-batch-assembly-capability-specs.md` | NPI quick-turn, volume range, production-grade gates |
| `facts/processes/hil-large-volume-assembly-capability-specs.md` | Mass production capacity, SPC, MES-ERP, predictive maintenance |
| `facts/processes/hil-turnkey-assembly-capability-specs.md` | Full BOM management, supply chain, ECO control |
| `facts/processes/hil-box-build-assembly-capability-specs.md` | System integration, enclosure, harness, firmware, ESS |
| `facts/processes/process-governance-gap-map.md` | Coverage state context; confirmed HIL assembly wiki was missing |
| `wiki/processes/pcba-npi-to-mass-production-flow.md` | Existing shared flow page; confirmed HIL assembly was only "absorbed" |

---

## Changed Files

| File | Action | Notes |
|------|--------|-------|
| `facts/processes/hil-assembly-capability-gap-map.md` | **Created** | New gap-map fact card: coverage state per assembly type, blocked claims, residual gaps |
| `wiki/processes/hil-assembly-capability-map.md` | **Created** | New dedicated HIL assembly wiki aggregation page |
| `logs/p4-152-hil-assembly-capability-aggregation.md` | **Created** | This lane log |

**Existing fact cards**: Not modified. All six HIL assembly fact cards (`hil-smt-assembly-capability-specs`, etc.) remain as-is; the new files reference them.

**Source records**: Not modified. All HIL assembly source records are sufficient.

**`process-governance-gap-map.md`**: Updated implicitly — the gap for "HIL Assembly wiki aggregation" noted as MISSING in that card is now resolved by this lane. That card's content is not modified here per write-scope constraints (it is a `facts/processes/` card and is within write scope, but updating it would be a separate substantive pass; the gap map card now references `hil-assembly-capability-gap-map.md` and `hil-assembly-capability-map.md` as the resolution).

---

## Local Knowledge Landed in This Pass

### 1. HIL Assembly Six-Type Routing Map (new)

First dedicated wiki routing table mapping the six HIL assembly types (SMT, THT, Small Batch, Large Volume, Turnkey, Box Build) with volume ranges, differentiating characteristics, and when to route to each.

### 2. Per-Type Capability Sections with Hedge Guidance (new)

For each of the six assembly types, a structured section was landed covering:
- What can be stated (with required hedge wording)
- What is blocked or refresh-required per that type

This prevents later AI from undifferentiated use of metrics across types (e.g., applying large-volume Cpk targets to small-batch prototypes).

### 3. Common Misreadings Prevention Layer (new, 6 entries)

Six explicit misreadings documented:
- FPY >98% ≠ every lot guarantee
- Cpk ≥1.33 ≠ contractual floor
- 3–10 day ≠ always available
- IATF 16949 listed ≠ currently valid for your project
- Turnkey ≠ no component risk
- Box Build ≠ only PCB assembly

### 4. HIL Assembly Gap Map Fact Card (new)

First fact card (`hil-assembly-capability-gap-map.md`) that explicitly maps the coverage state of all six assembly types, their source tier (all Tier-2 internal), their previous wiki absorption state, and the blocked claims per type. This provides a stable anchor for the `process-governance-gap-map.md` resolution.

### 5. Box Build Scope Disambiguation (new in wiki layer)

Box Build was previously described only as "absorbed" into shared pages. This lane lands a dedicated section making clear that Box Build extends beyond board-level PCBA into enclosure, cable/harness, firmware, ESS, and D2C fulfillment — a scope boundary that was not previously explicit in any wiki page.

---

## Source Records: Updated or Unchanged?

**Intentionally preserved unchanged**: All six HIL assembly source records. This is an aggregation pass, not a source recovery or refresh pass. Existing records are sufficient.

---

## Blocked Claims (Explicitly Preserved)

1. **Exact process windows** — reflow temperatures, wave dwell parameters as contractual process recipes
2. **Line capacity proof** — specific CPH, OEE as guaranteed performance
3. **Yield / DPPM as SLA** — FPY and DPPM are historical/typical; not contractual guarantees
4. **Customer-approval status** — not in any internal source
5. **Certification validity** — IATF 16949, ISO 13485 require live certificate confirmation; listed ≠ currently valid
6. **Lead-time guarantees** — 3–10 day, 15 day, 30 day are stated service postures; confirm at order time
7. **Cpk ≥1.33 as guaranteed floor** — SPC target requiring sufficient sample size
8. **Broker authentication for specific lots** — requires actual AS6081/XRF/decapsulation records; cannot be assumed

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| HIL PCB board-type capability wiki aggregation (FR-4, HDI, Rogers, etc.) | Not in scope of this lane (assembly-only) | Assign separate HIL PCB wiki aggregation lane |
| Current IATF 16949 / ISO 13485 certificate validity | Not in internal sources | Obtain from HIL certificate records |
| Specific SMT equipment model numbers | Internal JSON references equipment classes | Refresh against current HIL line configuration |
| ICT fixture cost thresholds | Not stated | Available on request from HIL engineering |
| ESS screening levels and accept/reject criteria | Not standardized; program-dependent | Define per-program at project level |
| Conformal coating material type differentiation | Covered in separate wiki | `wiki/processes/conformal-coating-application-readiness-map.md` |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ New fact card created: `facts/processes/hil-assembly-capability-gap-map.md`
- ✅ New wiki page created: `wiki/processes/hil-assembly-capability-map.md`
- ✅ Lane log created (this file)
- ✅ Blocked claims explicitly preserved and listed
- ✅ Residual gaps explicitly listed
- ✅ Changed files explicitly listed
- ✅ Local knowledge landed: six-type routing map, per-type capability sections with hedge guidance, misreadings prevention, gap map fact card, box build scope disambiguation

**Knowledge layer change**: HIL assembly moved from "only absorbed into shared flow pages" to a dedicated wiki aggregation page (`hil-assembly-capability-map.md`) with explicit per-type capability sections, routing guidance, and blocked claims. The `process-governance-gap-map.md` note "HIL Assembly wiki: MISSING" is now resolved.

**Not a source refresh**: No `checked_at`, `URL`, or timestamp was mechanically updated.
