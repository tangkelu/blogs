# H3 14-Layer Threshold And Rigid-Flex Intake

Date: 2026-04-26

## Purpose

This file is the `H3` queue-intake note for `14-layer`.

It exists to convert the remaining `14-layer` standards-threshold and rigid-flex-adjacent risk into a queue-controlled intake surface.

This file is not:

- a new `P4-06` bridge plan
- a numeric recovery note
- permission to reuse `Class 2 / Class 3`, bend-life, bend-radius, or generic flex-material numerics

## Current Baseline

Current `14-layer` reality:

- `14-layer` already has a conservative bridge path under `P4-06`
- `NQ-3` already split its highest-risk branch into narrower boundary cards
- that earlier closeout was containment-only, not numeric unlock

So this `H3` intake is not reopening the bridge.

It is hardening the standards-threshold and rigid-flex-adjacent control layer so the conservative bridge does not silently drift back into threshold, reliability, or supplier-proof overclaim.

## Current Queue Posture

Current working assumption:

- `public_threshold_available`: `none`
- `metadata_only`: standards family identity, applicability branch, non-numeric rigid-vs-rigid-flex posture
- `controlled_exclusion`: threshold numerics, rigid-flex reliability numerics, supplier/compliance assertions, and genericized flex-material numerics

## Surviving Risk Clusters

### 1. Standards-Threshold Leakage

Current risk:

- `IPC-6012 / IPC-6013 / Class 2 / Class 3` language can still collapse into engineering thresholds
- standards family names can still be overread as annular-ring, registration, plating, or acceptance authority

Default disposition:

- `downgrade_to_boundary_only`

### 2. Rigid-Flex Reliability Numeric Leakage

Current risk:

- rigid-flex branch discussion can still collapse into bend-radius, flex-life, transition-tolerance, or dynamic-flex guarantees
- architecture discussion can still drift toward cookbook-style default constructions

Default disposition:

- `controlled_exclusion`

### 3. Supplier / Compliance Assertion Leakage

Current risk:

- standards family names and rigid-flex complexity wording can still be rewritten as direct HIL capability or compliance proof
- frontmatter and trust-banner style language are especially vulnerable here

Default disposition:

- `hold_for_supplier_evidence`

### 4. Exact-Product To Generic Flex-Material Overreach

Current risk:

- narrow exact-product anchors can still be expanded into generic polyimide / LCP / FRCC numeric ladders
- material examples can still be overread as default reliability or stackup authority

Default disposition:

- `controlled_exclusion`

## Safe Residual Wording Classes

The following residual shapes remain safe for `14-layer`:

### 1. Standards Hierarchy And Applicability Context

Allowed:

- rigid-board and rigid-flex/flex standards families are distinct
- a `14-layer` design can sit on either branch depending on construction
- public metadata identifies document families, not reusable thresholds

### 2. Branch Posture

Allowed:

- `14-layer` can remain a rigid board
- `14-layer` can also move into a rigid-flex route
- rigid-flex is a separate construction branch requiring separate stackup and review discipline

### 3. Non-Numeric Manufacturability Posture

Allowed:

- thicker multilayer builds are more registration-sensitive
- rigid-flex transition zones need dedicated review
- coverlay, stiffener, and flex-zone handling belong to a specialized manufacturing path

### 4. Class-Level Material Framing

Allowed:

- polyimide, LCP, and adjacent flex-material families may be relevant by branch
- narrow exact-product examples may remain narrow
- material names do not by themselves authorize reliability or geometry defaults

## Blocked Numeric And Assertion Classes

The following remain blocked for `14-layer`:

- `Class 2 / Class 3` threshold tables
- annular-ring, registration, plating, and acceptance numerics inferred from standards families
- bend-radius tables
- flex-life tables
- transition-tolerance numbers
- default `14R-4F` or similar cookbook constructions
- genericized flex-material numeric ladders derived from narrow exact-product anchors
- HIL-specific `IPC-6012` or `IPC-6013` compliance claims
- HIL-specific capability, reliability, or turnaround proof built on standards language

## Draft-Area Mapping

| Draft area | Current risk shape | Source policy | Default disposition | Notes |
| :--- | :--- | :--- | :--- | :--- |
| frontmatter and opening trust language | supplier/compliance proof bundled into standards and rigid-flex language | `controlled_exclusion` | `hold_for_supplier_evidence` | Do not soften unsupported supplier proof into weaker claims. |
| standards / annular-ring / registration discussion | standards hierarchy can collapse into threshold authority | `metadata_only` + `controlled_exclusion` | `downgrade_to_boundary_only` | Keep only family identity and applicability context. |
| rigid-flex architecture discussion | branch posture can collapse into default construction recipes | `metadata_only` | `keep_non_numeric_context` | Keep branch distinction, not cookbook architecture. |
| transition zone / bend-radius / dynamic-flex discussion | reliability numerics and guarantees | `controlled_exclusion` | `delete` or `downgrade_to_boundary_only` | Keep only specialized-review posture. |
| polyimide / flex-material examples | exact-product anchors can be generalized into branch defaults | `controlled_exclusion` | `downgrade_to_boundary_only` | Keep examples narrow and conditional. |
| DFM / via / fabrication tables | capability numerics mixed with threshold/reliability logic | `controlled_exclusion` | `delete` | Outside this intake's safe residual layer. |

## Queue Completion Criteria

This queue intake is complete when:

1. the surviving `14-layer` risk clusters are explicit
2. safe residual wording classes are explicit
3. blocked numeric/assertion classes are explicit
4. the file preserves the existing conservative bridge posture without recasting it as numeric unlock
5. `public_threshold_available` remains explicitly `none`

## Minimal Control Posture

For `14-layer`, `H3` should preserve standards family identity, construction-branch posture, and non-numeric manufacturability context only. Thresholds, rigid-flex reliability numerics, supplier-proof claims, and generalized flex-material numerics remain blocked by default.
