# H3 14-Layer Bridge Exclusion And Supplier Hold Map

Date: 2026-04-26

## Purpose

This file converts the `14-layer` `H3` intake into execution-grade draft control.

It defines:

- what `14-layer` draft clusters must be excluded from future bridge use
- what residual wording may remain safely
- what HIL-specific supplier or compliance wording must wait for separate supplier evidence

This file is not:

- a numeric-recovery note
- a new `P4-06` bridge plan
- permission to reuse standards, rigid-flex reliability, or supplier-proof numerics

## Queue Baseline

Current `14-layer` posture:

- a conservative `P4-06` bridge already exists
- `H3` intake already fixed the surviving risk clusters
- `public_threshold_available`: `none`

So this execution note exists only to stop bridge-safe `14-layer` wording from drifting back into:

- threshold reconstruction
- rigid-flex reliability numerics
- genericized flex-material ladders
- HIL-specific compliance or capability proof

## Blacklist Clusters

### 1. Standards / Threshold Reconstruction

Blacklist:

- `Class 2 / Class 3` tables
- `IPC-6012 / IPC-6013` threshold restatements
- registration, annular-ring, plating, and acceptance numerics derived from standards families

Default action:

- `delete`

### 2. Rigid-Flex Cookbook Architecture

Blacklist:

- `14R-4F` or similar default constructions presented as reusable templates
- asymmetric-layout advice presented as hard manufacturable default rules
- decision-threshold wording that turns rigid-flex into a fixed recipe

Default action:

- `downgrade_to_boundary_only`

### 3. Polyimide / Transition / Bend-Reliability Numerics

Blacklist:

- bend-radius tables
- flex-life tables
- dynamic-flex guarantees
- transition-zone depth and stiffener numerics
- drilling, adhesion, coverlay, and processing numeric ladders

Default action:

- `delete`

### 4. Genericized Flex-Material Numerics

Blacklist:

- generic `polyimide`, `LCP`, `FRCC`, `Kapton`, `UPILEX`, or adhesiveless-flex numeric ladders
- exact-product examples widened into branch-default reliability or stackup rules

Default action:

- `delete` or `downgrade_to_boundary_only`

### 5. Fabrication Capability And Commercial Tables

Blacklist:

- via diameter, aspect-ratio, fine-line, transition-clearance, copper-balance, and drill-program tables
- turnaround, quality, prototype-window, or similar closing banners

Default action:

- `delete`

## Allowed Residual Wording Classes

The following residual shapes remain safe:

### 1. Standards Hierarchy And Branch Identity

Allowed:

- rigid-board and rigid-flex/flex standards families are distinct
- a `14-layer` build can remain rigid or move into a rigid-flex branch
- public metadata supports family identity, not thresholds

### 2. Rigid Vs Rigid-Flex Branch Posture

Allowed:

- not every `14-layer` board is rigid-flex
- rigid-flex is a separate construction route
- stackup, transition, and assembly review should be handled separately when that branch enters scope

### 3. Non-Numeric Manufacturability Posture

Allowed:

- higher-layer builds are more sensitive to stackup and process coordination
- transition zones, coverlay, stiffeners, and routing direction need dedicated review
- dense routing and via-strategy pressure can still be discussed qualitatively

### 4. Class-Level Material Framing

Allowed:

- polyimide, LCP, and adjacent flex-material families may be relevant by branch
- narrow exact-product examples may remain narrow
- material names do not authorize generic reliability or geometry defaults

## Supplier / Compliance Wording Held For Supplier Evidence

The following must not survive in bridge-safe form without separate supplier evidence:

- `choose HILPCB for 14 layer rigid-flex manufacturing`
- `proven IPC-6013 process control`
- `polyimide material expertise`
- `rapid engineering response`
- `we fabricate 14 layer PCBs`
- `dynamic flex capability`
- `IPC-6013 Type 3/4 compliance`
- `IPC-6012 Class 3 for rigid`
- `meet IPC-6013 requirements consistently`
- `specialized rigid-flex lamination tooling`
- `controlled-depth routing equipment`
- `bend life exceeding 100,000 cycles`
- `Z-routing with ±4mil accuracy`
- `3/3mil`, `2.5/2.5mil`, `288°C, 6 cycles`, `7 business days`

Default action:

- `hold_for_supplier_evidence`

Rule:

- tone softening is not enough for these claims

## Draft-Area Actions

| Draft cluster | Action | Allowed residual shape |
| :--- | :--- | :--- |
| frontmatter and opening trust banner | `hold_for_supplier_evidence` | none in supplier-specific form |
| standards / registration / annular-ring cluster | `delete` or `downgrade_to_boundary_only` | standards family and applicability context only |
| rigid-flex architecture cluster | `downgrade_to_boundary_only` | rigid vs rigid-flex branch posture only |
| polyimide processing numeric cluster | `delete` | class-level material/process posture only |
| transition-zone reliability cluster | `delete` or `downgrade_to_boundary_only` | transition zones require dedicated review |
| bend-radius / flex-life cluster | `delete` | none in numeric form |
| material options / flex section numeric cluster | `downgrade_to_boundary_only` | class-level material framing with narrow examples only |
| via / DFM / fabrication capability cluster | `delete` | dense routing / via-strategy pressure may remain qualitative elsewhere |
| closeout supplier proof cluster | `hold_for_supplier_evidence` | none in supplier-specific form |

## Completion Criteria

This execution-control note is complete when:

1. all standards-family language is compressed back to hierarchy/applicability context only
2. all rigid-flex reliability numerics and default recipe numerics are removed from the bridge-safe layer
3. all generic flex-material numeric ladders are removed or narrowed back to exact-product examples only
4. all HIL-specific capability/compliance/turnaround/reliability proof wording is routed to `hold_for_supplier_evidence`
5. `public_threshold_available` remains explicitly `none` and no wording implies numeric unlock

## Minimal Control Posture

For `14-layer`, safe residual content is limited to standards family identity, rigid-vs-rigid-flex branch posture, non-numeric manufacturability context, and narrow class-level material framing. Thresholds, reliability numerics, fabrication tables, and supplier-proof claims remain blocked by default.
