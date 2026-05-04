# 5G Telecom PCB Evidence Pack

**Pack ID**: `consumption-5g-telecom`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "5G Telecom PCB/PCBA (base station, antenna, mmWave front-end, pico cell, turnkey build)"
scope: |
  Conservative evidence pack for 5G telecom PCB/PCBA content.

  Supports board-class and execution-context vocabulary for 5G base station,
  antenna system, mmWave front-end, pico cell, NSA hardware, turnkey build,
  and NPI/EVT/DVT/PVT ramp board families.

  No RF-system performance, OTA results, standards compliance, operator
  qualification, or deployment proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-5g-telecom-coverage-gap-map"

  # 5G-specific method cards
  - "methods-5g-telecom-empty-image-rewrite-boundary"
  - "methods-5g-rf-system-context-vs-pcb-execution-boundary"
  - "methods-beamforming-mmwave-conservative-generation-gate"

  # Standards identity
  - "standards-5g-nr-identity-and-revision-boundary"

  # RF method cards
  - "methods-rf-isolator-component-class-vs-pcb-execution-boundary"
  - "methods-rf-validation-capability"
  - "methods-hybrid-rf-stackup-capability"

  # Fabrication method cards
  - "methods-backdrill-control-capability"
  - "methods-cavity-machining-capability"

  # NPI / ramp gate
  - "methods-pcba-evt-dvt-pvt-gated-ramp-boundary"

source_ids:
  - "3gpp-38-series"
  - "3gpp-ts-38104-archive"
  - "frontendapt-industry-communication-equipment-page-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"

wiki_framing_support:
  - "wiki/applications/5g-telecom-pcb-execution-boundary-map"

must_refresh:
  - claim: "5G NR release version or revision-specific features"
    value: true
  - claim: "RF interface speed, frequency band, or OTA measurement statements"
    value: true
  - claim: "mmWave substrate material loss specifications"
    value: true
  - claim: "3GPP compliance or operator rollout claims"
    value: true

excluded_claim_classes:
  - "mmWave performance proof (insertion loss, phase error, beamforming, OTA)"
  - "3GPP standards compliance, certification, or protocol-behavior proof"
  - "Operator rollout, deployment coverage, or field-proven claims"
  - "Exact RF metrics (gain, EIRP, S-parameters) as production output"
  - "PCIe/DDR5/112G/400G/800G interface speed or throughput proof"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `5G PCB`, `5G base station PCB`, `mmWave PCB`, `antenna PCB`, `RF PCB 5G`, `5G PCBA` |
| **Page Type** | `query` |
| **Search Intent** | 5G telecom hardware, RF/antenna board design, base station component manufacturing |
| **Target Reader** | RF/hardware engineers, telecom equipment designers, system integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class and execution-context discussion is supported; RF-system performance and OTA claims are blocked.

---

## 3. Board Families (Evidence Scope)

### 3.1 5G Base Station

| Aspect | Evidence Support |
|--------|-----------------|
| PCB partitioning (RF/digital/power/control zones) | Supported at review/routing vocabulary level |
| Hybrid stackup discussion | Supported at planning posture level |
| Connector and backplane transitions | Supported at vocabulary level |
| Validation-structure planning | Supported at gate-positioning level |
| RF-system performance claims | ❌ Blocked — OTA, field deployment proof |

### 3.2 5G NSA Hardware

| Aspect | Evidence Support |
|--------|-----------------|
| Interface density review | Supported at system-context pressure level |
| Reference-plane continuity | Supported at design-consideration vocabulary |
| Revision-control framing | Supported at NPI process vocabulary |
| NSA compliance or deployment speed claims | ❌ Blocked |

### 3.3 5G Pico Cell

| Aspect | Evidence Support |
|--------|-----------------|
| Small-form-factor stackup tradeoffs | Supported at planning vocabulary level |
| RF/digital coexistence in compact layout | Supported at design-consideration level |
| Shielded-structure planning | Supported at vocabulary level |
| Fine-pitch assembly review | Supported at DFM vocabulary level |
| Power efficiency or coverage range claims | ❌ Blocked |

### 3.4 Antenna System Board

| Aspect | Evidence Support |
|--------|-----------------|
| Feed-network routing posture | Supported at layout-consideration vocabulary |
| Return-path discipline | Supported at design-consideration level |
| Drilled-transition control | Supported at fab-discipline vocabulary |
| Connector footprint review | Supported at DFM vocabulary level |
| Coupon-based validation framing | Supported at validation-gate vocabulary |
| Antenna gain, EIRP, or efficiency claims | ❌ Blocked |

### 3.5 mmWave Front-End

| Aspect | Evidence Support |
|--------|-----------------|
| Laminate selection review (loss budget framing) | Supported at material-selection vocabulary |
| Drilled-transition discipline | Supported at fab-note vocabulary |
| Shield / cavity / ground-continuity coordination | Supported at layout vocabulary |
| Fab-note and tolerance discipline | Supported at process vocabulary |
| Sample-based validation access framing | Supported at gate vocabulary |
| Exact insertion loss, phase error, OTA, or mmWave performance claims | ❌ Blocked |

### 3.6 Turnkey Telecom Build

| Aspect | Evidence Support |
|--------|-----------------|
| Build-package completeness framing | Supported at NPI vocabulary level |
| BOM/AVL/lifecycle checks | Supported at supply-chain-review vocabulary |
| SMT/THT integration vocabulary | Supported at assembly-process level |
| Inspection gates | Supported at DFT/inspection vocabulary |
| Traceability framing | Supported at process vocabulary |
| Production-volume or throughput claims | ❌ Blocked |

### 3.7 NPI / EVT / DVT / PVT Ramp

| Aspect | Evidence Support |
|--------|-----------------|
| Gate-separated ramp stages | Supported at EVT/DVT/PVT gate vocabulary |
| Early validation structure reservation | Supported at planning posture level |
| Bring-up discipline framing | Supported at NPI vocabulary |
| Change-control vocabulary | Supported at governance level |
| Ramp timeline, yield rate, or volume claims | ❌ Blocked |

---

## 4. Standards Context (Identity Only)

| Standard / Technology | Safe Use | Blocked Use |
|---|---|---|
| **3GPP 5G NR (38-series)** | Standard-family identity; 5G system-context framing | Latest-version claims, release-specific features, protocol compliance |
| **FR1 (Sub-6 GHz)** | Frequency-range context; RF front-end pressure vocabulary | Exact FR1 frequency values, coverage proof, radio performance |
| **FR2 (mmWave)** | mmWave sensitivity context; execution-risk vocabulary | FR2 band tables, insertion loss, OTA, beamforming accuracy |
| **Beamforming / MIMO** | Architecture-level antenna context only | Beam shape, phase alignment, EIRP, antenna efficiency claims |
| **PCIe Gen 5/6** | System-context pressure naming only | Interface capability proof, throughput, lane-count claims |
| **DDR5** | Memory-interface pressure naming only | Performance guarantee, timing, signal-integrity proof |
| **112G / 400G / 800G Ethernet** | High-speed interconnect pressure context | Link-budget, loss-budget, interface-speed compliance proof |

---

## 5. Allowed vs Blocked

### 5.1 Allowed (Board-Class and Execution Context)

| Claim Pattern | Example |
|---|---|
| Board-class naming | "5G base station boards require partitioned RF/digital/power/control layout review" |
| Material selection context | "mmWave frequencies require low-loss laminate selection review" |
| Execution-risk framing | "Drilled transitions and reference-plane continuity require close coordination in antenna boards" |
| Validation-gate framing | "NPI ramp stages (EVT/DVT/PVT) provide structured gate points before volume production" |
| Standards-identity naming | "3GPP 5G NR (38-series) establishes the system context for base station and antenna board review" |
| Turnkey process vocabulary | "Turnkey telecom builds include stackup review, BOM/AVL checks, inspection gates, and traceability" |

### 5.2 Blocked (RF Performance / Compliance / Deployment)

| Blocked Claim | Reason |
|---|---|
| "Our mmWave PCBs achieve [X dB] insertion loss" | OTA/measurement proof — not supported at wiki level |
| "5G NR compliant PCB" or "3GPP certified board" | Standards compliance is protocol/device level, not PCB level |
| "Proven in operator deployments" | Deployment proof — not available in current source layer |
| "FR2 band frequencies: [range] GHz" | Exact frequency tables require 3GPP clause-level source |
| "PCIe Gen 6 capable board" | Interface capability proof — blocked |
| "48-hour turnkey telecom build" | Commercial/lead-time claim — blocked |

---

## 6. Handoff

**Core Answer**:

> 5G telecom PCBs are addressed through board-class execution-context vocabulary covering base station, antenna system, mmWave front-end, pico cell, NSA hardware, turnkey build, and NPI ramp families. The current evidence supports stackup-review framing, material selection context, RF/digital partitioning vocabulary, validation-gate positioning, and standards-identity naming. It does not support RF-system performance claims, OTA results, 3GPP compliance, deployment proof, or interface-speed guarantees.

**Safe Reusable Shapes**:

- "5G telecom board families create distinct execution-context pressures: base station boards require RF/digital/power/control partitioning; mmWave boards require laminate and drilled-transition discipline; antenna boards require feed-network routing and return-path review."
- "Standards names (3GPP, FR1, FR2, beamforming, MIMO) are safer as system-context pressure labels than as PCB capability descriptors."
- "NPI ramp stages are structural control gates — EVT/DVT/PVT gating is the vocabulary, not yield-rate or throughput proof."

---

## 7. Pre-flight

- [x] 5G telecom wiki boundary page referenced (`wiki/applications/5g-telecom-pcb-execution-boundary-map.md`)
- [x] Application fact card referenced (`facts/applications/5g-telecom-coverage-gap-map.md`)
- [x] All 10 fact_ids from existing landed records — no new records required
- [x] All 7 source_ids from existing landed registry records
- [x] mmWave performance and OTA blocked claims explicitly documented
- [x] Standards identity vocabulary separated from compliance/performance claims
- [x] `must_refresh` items identified for version-sensitive and RF-specific claims

**Verdict**: ✅ `go_now_conservative` — board-class and execution-context discussion. Exclude all RF-performance, OTA, compliance, and deployment claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
