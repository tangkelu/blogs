# H3 Threshold Inventory And Blacklist

Date: 2026-04-26

## Purpose

This file converts `Class C` threshold and acceptance risk into an explicit `H3` inventory and evidence-pack blacklist.

It exists so the repo can distinguish:

- public standards metadata
- truly public threshold authority
- controlled exclusion classes that must stay out of future high-density packs

## Policy Classes

### `metadata_only`

Allowed use:

- document identity
- revision status
- hierarchy and addendum framing
- clause-family visibility
- procurement and governance ecosystem context

Not allowed:

- technical thresholds
- reconstructed sample plans
- acceptance tables
- supplier approval or accepted-status claims

### `public_threshold_available`

Allowed use only if:

- a public primary source exposes the threshold directly
- scope, condition, and interpretation are visible
- the number is legally and contextually reusable

Current default posture:

- assume `not available` unless proven otherwise

### `controlled_exclusion`

Must stay out of evidence packs under current discipline.

Typical reasons:

- threshold depends on licensed standard text
- claim depends on contract invocation
- claim depends on supplier or lot-specific evidence
- public page shows hierarchy only, not technical criteria
- threshold would need reconstruction from metadata or indirect summaries

## Threshold And Acceptance Claim Families

### 1. `class_linked_workmanship_thresholds`

Examples:

- `Class 2 / Class 3 / Class 3A` thresholds
- class-linked annular-ring or workmanship values
- class-linked visual acceptability restated as general engineering rules

Current posture:

- `controlled_exclusion`

### 2. `ipc_6012_6013_acceptance_thresholds`

Examples:

- bow / twist thresholds
- plating minima when cited as standard criteria
- addendum-linked acceptance values
- technical tables inferred from public TOCs

Current posture:

- `controlled_exclusion`

### 3. `ist_or_reliability_acceptance_thresholds`

Examples:

- `IST` cycle counts used as pass/fail proof
- thermal-cycle counts used as qualification proof
- microvia reliability counts reused as transferable acceptance authority

Current posture:

- `controlled_exclusion`

### 4. `lot_acceptance_and_plt_numerics`

Examples:

- `PLT` sample plans
- lot-conformance counts
- accepted-lot or release numerics

Current posture:

- `controlled_exclusion`

### 5. `outgassing_and_screening_acceptance_numerics`

Examples:

- outgassing acceptance percentages or limits
- screening thresholds rewritten as general PCB release rules

Current posture:

- `controlled_exclusion`

### 6. `supplier_status_compliance_qualification_assertions`

Examples:

- approved / qualified / listed supplier status implied by numeric or threshold language
- compliance proof implied through standards references
- accepted-status or release-authority claims

Current posture:

- `controlled_exclusion`

### 7. `metadata_and_hierarchy_only_items`

Examples:

- document revision
- active / legacy / addendum lineage
- public hierarchy between base documents and addenda
- public method identity without pass/fail criteria

Current posture:

- `metadata_only`

## Evidence-Pack Blacklist Rules

The following claim types must be blacklisted from future high-density evidence packs unless a later `H3` note explicitly unlocks a narrower family.

### Blacklist A: Threshold Tables

Do not include:

- `Class 2 / 3 / 3A` threshold tables
- `IPC-6012 / 6013` technical threshold tables
- addendum technical tables
- public-summary reconstructions of licensed standard values

### Blacklist B: Acceptance And Qualification Numerics

Do not include:

- `IST` pass/fail numerics
- thermal-cycle qualification counts used as release proof
- coupon or qualification-plan counts
- accepted-lot or lot-release numerics

### Blacklist C: Supplier Or Compliance Proof Claims

Do not include:

- approved / listed / qualified supplier claims
- compliance proof claims
- accepted-status or release-authority claims
- public-framework-to-supplier-proof rewrites

### Blacklist D: Contract And Program Invocation Leakage

Do not include:

- contract-flowdown wording rewritten as technical acceptance proof
- procurement clauses rewritten as current product compliance proof
- governance-program metadata rewritten as universal manufacturing criteria

## Blog And Risk Cluster Queue

### First Priority: `22-layer`

Main risk families:

- `class_linked_workmanship_thresholds`
- `ipc_6012_6013_acceptance_thresholds`
- `lot_acceptance_and_plt_numerics`
- `outgassing_and_screening_acceptance_numerics`
- `supplier_status_compliance_qualification_assertions`

Reason:

- highest concentration of hi-rel governance vocabulary that can be overread as current acceptance proof

### Second Priority: `14-layer`

Main risk families:

- `class_linked_workmanship_thresholds`
- rigid-flex-adjacent threshold leakage
- standards-threshold reuse inside manufacturability language

Reason:

- already narrowed by boundary cards, but still structurally close to threshold leakage

### Third Priority: `20-layer`

Main risk families:

- `ist_or_reliability_acceptance_thresholds`
- method-vs-qualification confusion
- reliability and qualification wording that can be overread as acceptance proof

Reason:

- standards risk is narrower than `22-layer`, but still blocks high-density reuse

### Fourth Priority: Cross-Blog Safe-Wave Cleanup

Blogs:

- `6-layer`
- `8-layer`
- `10-layer`
- `12-layer`
- `16-layer`
- `18-layer`
- `24-layer`

Main risk families:

- class-style quality wording
- `100%` test or quality banners drifting into acceptance proof
- standards references being used as quasi-threshold engineering support

## Current Working Rule

Until a later `H3` branch proves otherwise:

- public metadata is allowed only for hierarchy and identity
- threshold numerics are presumed blocked
- acceptance numerics are presumed blocked
- supplier/compliance/accepted-status claims are presumed blocked

This is the safe default for future high-density evidence-pack assembly.
