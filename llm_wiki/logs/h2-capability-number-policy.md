# H2 Capability Number Policy

Date: 2026-04-25

## Purpose

This document defines the governance rules for `H2 Workstream 2: Fabrication Capability Numeric Layer`.

Its job is to decide when a fabrication capability number is:

- kept in governed numeric form inside `llm_wiki`
- downgraded to internal framing or non-numeric wording
- blocked from fact-card promotion
- blocked from future evidence packs

This is not a source-hunting file.

This is not a capability fact card.

This document exists so `llm_wiki` does not leak shop-style numbers from marketing pages, mixed-context blog prose, or unsupported standards language into reusable evidence packs.

## Scope

This policy governs capability-style fabrication numbers used in the 10 layer-count blogs under:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en`

It applies to numeric claims such as:

- `trace/space`
- minimum mechanical drill
- minimum laser via
- aspect ratio
- annular ring
- board thickness window
- copper-weight production window when used as a shop capability claim
- impedance tolerance
- registration tolerance
- backdrill depth or residual-stub window
- test-coverage numbers when framed as production capability
- sequential-lamination counts when framed as transferable fabrication capacity

It also applies when the same number is embedded inside:

- comparison tables
- DFM checklists
- stackup recipe blocks
- QA / test banners
- service or capability landing-page claims
- future prompt evidence packs

## Non-Goals

This policy does not:

- define material datasheet numerics; that belongs to `H1`
- define standards thresholds or acceptance criteria; that belongs to `H3`
- define board-level SI, channel-budget, or RF performance numerics; that belongs to the later high-speed workstream
- define dynamic commercial numerics such as lead time, yield, MOQ, or cost uplift
- approve any specific capability number by itself
- invent default capability values for any factory, line, or region

## Definition: Fabrication Capability Numerics

For this repo, a fabrication capability numeric is a number that claims, implies, or strongly suggests what a fabricator can currently manufacture, control, verify, or deliver as an operational capability.

This includes numbers that describe:

- minimum producible geometry
- process-window limits
- tolerance promises
- verification depth
- manufacturing-route limits
- capability-conditioned stackup windows

This class is broader than pure geometry.

A number is still a fabrication capability numeric if it is written as:

- a recommended default
- a common production range
- a standard shop target
- a quote-stage promise
- a test-coverage promise
- a manufacturability shortcut

even when it appears inside educational prose rather than a formal capability table.

## Canonical Numeric Families In Scope

- feature geometry: `trace/space`, drill size, laser-via size, annular ring, aspect ratio
- tolerance and control: impedance tolerance, registration tolerance, thickness tolerance, backdrill depth tolerance
- process windows: lamination cycle count, board-thickness range, copper-weight processing window, drill-program counts, press parameters when reused as shop capability
- QA and validation coverage: `100% electrical test`, TDR coupon counts, VNA frequency coverage, test-structure counts
- HDI / build-up capability numbers: blind-via pitch windows, stacked-microvia limits, any-layer geometry defaults

## Source Tiers

### Tier 1: Internal Dated Capability Record

This is the preferred source class for reusable fabrication capability numbers.

Required characteristics:

- internally controlled
- explicitly date-stamped
- clearly scoped to a capability family, line family, plant family, region, or release context
- maintained as a capability record rather than prose marketing copy
- suitable for refresh and expiry handling

Examples of acceptable use:

- a dated internal capability table for rigid multilayer production
- a dated internal capability record for HDI / laser-via windows
- a dated internal verification record for impedance / TDR / backdrill control ranges

### Tier 2: Official External Source

This is allowed only when the number is truly external and does not pretend to be this repo's shop capability.

Allowed examples:

- an official manufacturer engineering guide that states a product- or process-specific fabrication condition with clear scope
- an official maintained source describing a supplier's own capability window
- an official method/governance page naming a process metric without turning it into a threshold for this repo's capability layer

Tier 2 may support:

- external industry-context framing
- supplier-specific examples
- guarded manufacturability context

Tier 2 may not be silently rewritten as:

- this repo's current factory capability
- a generic industry default
- a universal threshold

### Tier 3: Internal Process Page For Framing Only

This includes internal APT/HIL capability, service, drilling, HDI, backplane, FAQ, and process pages that are useful for vocabulary, routing, and capability-family framing.

These pages are valid for:

- identifying which capability family is in scope
- explaining why a control matters
- supporting guarded workflow language
- routing future source recovery

These pages are not sufficient on their own for reusable capability numerics unless the number is also anchored in a Tier 1 dated capability record.

### Forbidden Source Classes

The following are forbidden as primary support for H2 capability numbers:

- undated internal marketing copy
- blog prose
- quote-page snippets
- generic service pages used as frozen capability tables
- vendor laminate datasheets used to infer shop capability
- third-party datasheet mirrors
- distributor pages
- forum posts
- scraped tables
- unsupported paid-standard paraphrases
- speculative engineer lore
- stale copied numbers with no date, scope, or owner

## Explicit Exclusion Rules

### 1. Marketing-Page Leakage

A number is excluded if it appears only on a capability, service, product, or promotional page without a dated capability record behind it.

Examples:

- `±8% impedance`
- `2.5/2.5mil`
- `100% electrical testing`
- `7-day prototype`

If the number is only marketing-visible, it is not reusable capability evidence.

### 2. Stale Undated Shop Numbers

Any internal number without a usable date and scope is excluded from `llm_wiki` capability facts and evidence packs.

This includes numbers copied forward from:

- old site pages
- old proposals
- legacy deck content
- prior blog drafts

### 3. Unsupported Standards Thresholds Disguised As Capability

Numbers that are really standards thresholds, acceptance criteria, or qualification thresholds are excluded from H2 unless a later standards workstream explicitly authorizes them.

Examples:

- `IPC Class 2 / 3` annular-ring thresholds
- plating minimums
- bow/twist limits
- `IST` pass/fail counts
- thermal-cycle acceptance thresholds

H2 does not absorb standards thresholds just because they are written inside a capability section.

### 4. Industry-Context Numbers Disguised As Shop Capability

Numbers that describe ecosystems, interfaces, packages, or application demand are excluded as capability proof.

Examples:

- `DDR5 6400 MT/s`
- `56G / 112G`
- `0.5mm pitch BGA`
- `100G / 400G switch`

These may support design context elsewhere, but they do not prove current fabrication capability by themselves.

### 5. SI / Performance Numbers Disguised As Manufacturability

Numbers that really describe channel, loss, timing, resonance, EMC, or board-level electrical outcome are excluded from H2 capability promotion.

Examples:

- insertion-loss budgets
- Nyquist mappings
- stub resonance thresholds
- weave-skew impact tables
- eye-opening or return-loss promises

These belong to the high-speed / interconnect governance layer, not to H2.

### 6. Recipe Tables Disguised As Generic Capability

Illustrative stackups, process examples, and architecture patterns may be useful as examples, but they are excluded as reusable capability numbers unless they are explicitly governed as dated capability records.

Examples:

- default `1+N+1` / `2+N+2` claims
- “common” board-thickness windows
- “typical” lamination counts
- rigid-flex bend and stack recipes

## Disposition Labels For Capability Numerics

H2 uses the same repository-wide disposition discipline, but with capability-specific meaning.

### `keep`

The number may enter a capability fact card and future evidence packs.

Requirements:

- supported by Tier 1, or exceptionally by tightly scoped Tier 2
- has complete provenance fields
- has a refresh rule
- is written with exact scope

### `downgrade`

The numeric idea may remain only as internal context or non-reusable drafting support after conversion into guarded, non-numeric wording.

Typical triggers:

- internal capability pages with useful posture but no dated numeric authority
- official external process pages that show why a control matters but do not authorize a generic number

Typical outputs:

- `tight impedance control`
- `registration-sensitive`
- `requires tighter process control`
- `more fabrication-sensitive than standard multilayer work`

### `needs_source`

The number is conceptually relevant, but cannot enter `llm_wiki` or evidence packs until a valid source tier is registered.

This is the default label for most current capability numbers found in the blogs.

### `delete`

The number must be removed from future evidence packs.

Typical triggers:

- dynamic commercial numerics
- unsupported standards thresholds
- SI/channel numbers disguised as capability
- copied shop promises with no governed provenance

## Required Provenance Fields At Capability-Card Level

No capability numeric card should be created without all of the following fields being defined.

- `capability_family`
  - examples: `rigid_multilayer`, `hdi_microvia`, `backdrill`, `impedance_control`, `rigid_flex`, `metal_core`
- `number_type`
  - examples: `minimum_feature`, `maximum_aspect_ratio`, `tolerance`, `process_window`, `test_coverage`
- `value`
- `unit`
- `scope`
  - what exact product family, board family, process family, line family, or region the number applies to
- `source_tier`
  - `internal_dated_capability_record`, `official_external_source`, or `internal_process_framing_page`
- `source_id`
- `captured_at`
- `effective_date`
- `review_by`
- `owner`
  - person, team, or system responsible for refresh
- `refresh_interval`
- `confidence`
- `customer_facing_allowed`
  - `yes`, `internal_only`, or `no`
- `notes_on_limits`
  - what the number does not prove

If any of these fields is missing, the number is not evidence-pack ready.

## Reuse Rules For Blogs And Evidence Packs

Capability numbers may be reused in blogs or future evidence packs only when all of the following are true:

1. the number is labeled `keep`
2. the source tier is valid under this policy
3. provenance fields are complete
4. the number is still inside its refresh window
5. the destination draft keeps the original scope
6. the draft does not silently convert the number into:
   - a universal industry rule
   - a standards threshold
   - a qualification claim
   - a board-performance promise

Additional reuse restrictions:

- A shop capability number cannot be blended with supplier material numerics into one synthetic table row.
- A supplier-specific external capability example cannot be rewritten as this repo's own capability.
- A capability number allowed for one board family cannot be silently reused for another family.
- Evidence packs must prefer omission over unsupported numeric carryover.

## Refresh And Expiry Posture

Capability numbers are refresh-sensitive by default.

Default posture:

- no capability number is evergreen
- every allowed capability number must have a `review_by`
- expired numbers must be treated as `not reusable` until revalidated

Default expiry behavior:

- missing `review_by` means `not reusable`
- missing owner means `not reusable`
- missing scope means `not reusable`
- dated but expired numbers fall back to `downgrade` or `delete`, not silent reuse

This repo should prefer a shorter reuse window over a broader unsupported claim.

## Stop / Go Rules For H2

### Stop

Stop promotion immediately when any of the following is true:

- the number comes only from blog prose or marketing copy
- the number has no date
- the number has no defined scope
- the number is actually a standards threshold
- the number is actually an SI or performance claim
- the number is actually dynamic commercial data
- the number depends on suffix inference, family averaging, or recipe generalization
- the number would force `20-layer` or `22-layer` writing to overclaim unsupported capability

### Go

H2 may promote a capability number only when:

- the number is truly a fabrication capability numeric
- the source tier is valid
- provenance is complete
- scope is narrow enough to prevent overgeneralization
- refresh handling is defined
- non-claims are explicit
- the number improves evidence-pack discipline rather than weakening it

## Practical Repo-Level Rules

- Treat current internal capability and method cards as posture support, not as frozen parameter sheets.
- Treat official supplier process guides as manufacturability context unless a number is explicitly scoped and reusable under this policy.
- Keep `20-layer` and `22-layer` capability numerics under stricter review because those blogs currently carry the highest unsupported capability density.
- Prefer deleting a reused capability number over carrying an unsupported promise into `P4-06`.

## Exit Condition For H2 Policy Adoption

This policy is active for H2 only when:

- future capability cards follow the provenance schema above
- `H0` capability claims are re-labeled against this policy
- no evidence pack includes capability numerics sourced only from vague marketing wording

If those conditions are not met, H2 is not complete.
