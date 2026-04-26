# High Numeric Density Program Plan

Date: 2026-04-25

## Goal

Build a source-backed `llm_wiki` layer that can support the 10 layer-count blogs under `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en` in a genuinely high-numeric-density form, rather than only in conservative rewritten form.

## Why This Program Exists

Current `P4-12` work proved that narrow source supplementation can improve guarded wording, but it does not by itself create a stable path to high numeric density.

The blocking issue is structural:

- the blogs do not fail because of missing prose
- they fail because multiple numeric claim classes are still unsupported
- those claim classes come from different source ecosystems and require different handling rules

So the work must move from `ad hoc source hunting` to a program with fixed readiness gates.

## Target Outcome

The target is not merely `more numbers`.

The target is:

1. every numeric claim class in the 10 blogs is classified
2. every allowed numeric claim class has an approved source policy
3. every kept number can be traced to a registered primary source
4. unsupported numbers are either replaced, downgraded, or explicitly excluded
5. `P4-06` starts only after blog-level numeric readiness passes

## Current Baseline

- `conservative rewrite support` exists for `6 / 8 / 10 / 12 / 14 / 16 / 18 / 24-layer`
- `20-layer` and `22-layer` remain blocked even for conservative prompt bridging
- `high numeric density support` is not ready for any of the 10 blogs

## Hard Definition Of High Numeric Density Ready

A blog is `high_numeric_density_ready` only if all of the following are true:

1. its numeric claims are fully inventoried by paragraph or table
2. at least `90%` of kept numeric claims map to registered primary sources
3. the remaining `<=10%` are either:
   - date-stamped dynamic values with a refresh rule, or
   - intentionally deleted from the future article
4. no unsupported claim remains in these categories:
   - fabrication capability table
   - standards threshold table
   - hi-rel qualification or acceptance number
   - channel-budget or board-loss promise
   - supplier-status or approval claim disguised as a number
5. the blog has a dedicated readiness note saying `safe for high numeric density evidence-pack use`

If any one of the above fails, the blog is not ready.

## Numeric Claim Classes

### Class A: Material Datasheet Numerics

Examples:

- `Dk / Df`
- `Tg / Td / T288`
- `CTE`
- moisture absorption
- peel strength
- thermal conductivity

Target:

- official product page or official datasheet only

Current posture:

- strongest existing layer
- still incomplete for broader FR-4 and exact families used in blog tables

### Class B: Fabrication Capability Numerics

Examples:

- `trace/space`
- minimum mechanical drill
- minimum laser via
- aspect ratio
- annular ring
- board thickness window
- backdrill residual stub
- impedance tolerance
- registration tolerance

Target:

- current authoritative fabricator capability source with refresh discipline, or a separate internal dated capability layer

Current posture:

- weakest reusable numeric layer
- cannot be inferred safely from internal marketing pages or vendor laminate guides

### Class C: Standards / Qualification / Acceptance Numerics

Examples:

- `IPC Class 2 / 3 / 3A` thresholds
- plating minimums
- bow/twist limits
- solder-float counts
- thermal-cycle thresholds
- `IST` cycle references used as acceptance claims
- `lot acceptance` thresholds

Target:

- public primary threshold source if available, otherwise controlled exclusion

Current posture:

- metadata layer exists
- threshold layer does not

### Class D: High-Speed / Channel / Interconnect Numerics

Examples:

- `PCIe / DDR / 56G / 112G / PAM4` board-level budgets
- insertion loss
- Nyquist frequency mapping
- weave-skew impact tables
- stub resonance numbers

Target:

- official system-standard context plus a separate board-level interpretation source policy

Current posture:

- ecosystem vocabulary improved
- article-grade board-budget numerics remain unsupported

### Class E: Reliability / Build-Up / HDI Numerics

Examples:

- lamination counts
- stacked-microvia height limits
- `ELIC / any-layer` geometry defaults
- `IST` cycle counts
- via reliability thresholds
- reflow-cycle limits

Target:

- official maintained method, qualification, or manufacturer-specific engineering source with strict scope handling

Current posture:

- vocabulary improved a lot
- transferable numbers still weak

### Class F: Dynamic Commercial Numerics

Examples:

- lead time
- quick-turn windows
- cost uplift
- MOQ
- yield

Target:

- dedicated dynamic fact policy with refresh timestamp

Current posture:

- not suitable for static fact cards under the current discipline

## Program Structure

## Workstream 0: Claim Inventory And Rulebook

Objective:

- convert the 10 blogs into a numeric-claim inventory instead of treating them as prose pages

Deliverables:

- one master spreadsheet or markdown matrix of all numeric claims by blog
- one numeric claim taxonomy
- one allowed-source rulebook by claim class
- one `keep / downgrade / delete / needs_source` label per claim

Exit gate:

- no later workstream starts blind

## Workstream 1: Material Numeric Coverage Completion

Objective:

- make material comparison tables sourceable at product-grade level

Priority tasks:

- expand official FR-4 family coverage across the exact families used in current blog comparisons
- continue official low-loss and very-low-loss material recovery only where stable product sources exist
- keep Taconic and unresolved Arlon under gap-control until official stable pages or datasheets are verified

Deliverables:

- manufacturer-by-family source matrix
- product-grade fact cards with approved numeric fields
- comparison-table-ready material ladders

Exit gate:

- blog material tables no longer rely on generic FR-4 placeholders or third-party mirrors
- status on 2026-04-25: complete; see `logs/h1-material-numeric-coverage-closeout-summary.md`

## Workstream 2: Fabrication Capability Numeric Layer

Objective:

- create a separate, governed capability-number layer instead of leaking numbers from prose pages

Priority tasks:

- inventory which fabrication numbers in the 10 blogs are truly required
- separate `shop capability numbers` from `industry context numbers`
- define whether each number can come from:
  - internal dated capability record
  - official external source
  - or must be removed

Deliverables:

- capability-number policy
- dated capability-source schema
- capability fact cards with refresh rules

Exit gate:

- no fabrication capability table in any blog depends on vague marketing wording

## Workstream 3: Standards Threshold And Acceptance Layer

Objective:

- decide which standards-heavy numbers can be supported and which must remain excluded

Priority tasks:

- build a threshold inventory for `IPC-6012 / 6013 / Class 3 / 3A / IST / lot acceptance`
- separate `public metadata only` vs `public threshold available`
- explicitly blacklist unsupported threshold classes from evidence packs

Deliverables:

- threshold-availability matrix
- standards-threshold guardrail cards
- per-blog list of deletable standards tables

Exit gate:

- every standards-heavy number is either sourceable or forbidden

## Workstream 4: High-Speed Numeric Interpretation Layer

Objective:

- close the gap between system-context standards pages and board-level numeric claims

Priority tasks:

- inventory all high-speed numeric claims used in `12 / 16 / 18 / 20 / 24-layer`
- distinguish:
  - interface-release numbers
  - connector/I-O ecosystem numbers
  - board-loss and channel-budget numbers
- define which board-level interpretations can enter `llm_wiki`

Deliverables:

- high-speed claim taxonomy
- approved interpretation boundaries
- channel-budget exclusion list where evidence is insufficient

Exit gate:

- no high-speed table mixes official interface numbers with unsupported board promises

## Workstream 5: 20-Layer Build-Up / Reliability Numeric Recovery

Objective:

- attack the hardest `20-layer` blockers directly

Blocking claim classes:

- `ELIC` defaults
- build-up geometry
- microvia and stacked-via rules
- `IST` thresholds
- lamination-count and reliability numbers

Deliverables:

- `20-layer` numeric blocker sheet
- updated build-up / reliability fact cards
- final `20-layer` readiness decision for high-density writing

Exit gate:

- either `20-layer` becomes high-density ready, or a permanent exclusion list is documented

## Workstream 6: 22-Layer Hi-Rel Acceptance Numeric Recovery

Objective:

- attack the hardest `22-layer` blockers directly

Blocking claim classes:

- `Class 3 / 3A` threshold tables
- qualification-flow reconstruction
- acceptance numbers
- `PLT` or lot-acceptance reinterpretation
- supplier-status implications hidden in numeric language

Deliverables:

- `22-layer` hi-rel numeric blocker sheet
- updated hi-rel guardrails
- final `22-layer` readiness decision for high-density writing

Exit gate:

- either `22-layer` becomes high-density ready, or a permanent exclusion list is documented

## Workstream 7: Dynamic Commercial Number Policy

Objective:

- prevent unstable business numbers from polluting the static corpus

Deliverables:

- separate dynamic-number policy
- timestamp and refresh rule
- explicit rule for when commercial numbers may appear in final blog drafts

Exit gate:

- dynamic numbers stop blocking technical-source progress

## Workstream 8: Blog-Level Evidence-Pack Assembly

Objective:

- assemble the numeric-ready evidence packs only after upstream claim classes pass

Deliverables:

- one readiness sheet per blog
- one evidence-pack manifest per blog
- final labels:
  - `high_numeric_density_ready`
  - `conservative_only`
  - `blocked`

Exit gate:

- only `high_numeric_density_ready` blogs may enter the future high-density writing phase

## Execution Order

The order is fixed:

1. `Workstream 0` claim inventory and rulebook
2. `Workstream 1` material numerics
3. `Workstream 2` fabrication capability numerics
4. `Workstream 3` standards thresholds
5. `Workstream 4` high-speed numeric interpretation
6. `Workstream 5` `20-layer` blocker recovery
7. `Workstream 6` `22-layer` blocker recovery
8. `Workstream 7` dynamic commercial number policy
9. `Workstream 8` blog evidence-pack assembly

This order matters because `20-layer` and `22-layer` should not be treated as isolated blog problems before the shared numeric source classes are settled.

## Multi-Agent Operating Model

Main agent responsibilities:

- define batch scope
- prevent overclaiming
- write final source records and fact cards
- update logs and readiness state

Sub-agent pattern per batch:

- Agent A: manufacturer / material numeric recovery
- Agent B: standards / threshold / acceptance-source scouting
- Agent C: high-speed or reliability-source scouting
- Agent D: blog-side numeric claim inventory and mapping

Rules:

- sub-agents do not edit main logs
- sub-agents return candidate URLs, safe contributions, and non-claims
- main agent remains the only integration point

## Batch Plan

### Batch H0: Numeric Claim Inventory

Outputs:

- 10-blog numeric claim matrix
- claim taxonomy
- `keep / downgrade / delete / needs_source` labels

Success condition:

- we know exactly what must be recovered instead of searching blindly

### Batch H1: Material Table Recovery

Outputs:

- missing product-grade material source matrix
- material fact expansions for comparison-table use

Success condition:

- material tables for `6 / 8 / 10 / 12 / 14 / 16 / 18 / 24-layer` are largely sourceable

### Batch H2: Capability Number Governance

Outputs:

- capability-number policy
- dated capability-source schema
- first governed capability number set

Success condition:

- fabrication tables stop depending on informal copy

### Batch H3: Standards Threshold Decision Batch

Outputs:

- threshold availability matrix
- permanent exclusions where public thresholds cannot be supported

Success condition:

- standards-heavy blogs stop carrying undefined threshold debt

### Batch H4: High-Speed Numeric Interpretation Batch

Outputs:

- approved and forbidden high-speed numeric claim classes
- `18 / 24-layer` channel-budget decision sheet

Success condition:

- board-level high-speed numbers are either governed or removed

### Batch H5: 20-Layer Blocker Batch

Outputs:

- `20-layer` blocker closure sheet
- readiness verdict

### Batch H6: 22-Layer Blocker Batch

Outputs:

- `22-layer` blocker closure sheet
- readiness verdict

### Batch H7: Dynamic Commercial Policy Batch

Outputs:

- dated dynamic-number rules

### Batch H8: Blog Evidence-Pack Readiness Review

Outputs:

- final per-blog readiness labels

## Stop / Go Gates

Do not start high-density writing if any of these remain true:

- a blog still depends on unsupported fabrication capability tables
- a blog still depends on unsupported standards thresholds
- a blog still mixes system-context interface numbers with unsupported board-level promises
- a blog still depends on unresolved `20-layer` or `22-layer` blocker classes
- a kept number cannot be mapped back to a registered source or governed dynamic rule

## Success Metrics

Program success is measured by:

- numeric claims inventoried across all 10 blogs: `100%`
- kept numeric claims with provenance: `>=90%`
- unsupported numeric claims explicitly excluded: `100%`
- blogs labeled `high_numeric_density_ready`: target `10/10`, minimum acceptable first milestone `8/10` without `20/22`
- `20-layer` and `22-layer` final disposition documented with no ambiguity

## Immediate Next Move

Start `Batch H0`, not another free-form source batch.

The next unit of work should be:

- full numeric claim inventory of the 10 layer-count blogs
- claim-class tagging
- sourceability judgment per claim

Without `H0`, all later recovery work remains unfocused.
