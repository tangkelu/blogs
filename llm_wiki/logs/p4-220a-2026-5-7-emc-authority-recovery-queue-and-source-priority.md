# P4-220A EMC Authority-Recovery Queue And Source Priority

Date: 2026-05-07
Lane: `EMC exact authority-recovery queue after P4-219a`
Model requested: `gpt-5.4`

## Purpose

Build the tight next-step EMC recovery queue after `P4-219A` using only already captured local knowledge.

This log does not promote new facts. It converts the current EMC lane state into:

- a prioritized source-class queue
- the exact claim families worth recovering next
- the blocked claim families that remain out of scope
- the already-covered areas that should not be reopened now

## Inputs Used

- `llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`
- `llm_wiki/logs/p4-219a-2026-5-7-emc-promotion-review-existing-coverage-and-gap-map.md`
- `llm_wiki/logs/p4-215a2-2026-5-6-emc-lane-a2-ferrite-bead-vs-common-mode-choke.md`
- `llm_wiki/logs/p4-215a3-2026-5-6-emc-lane-a3-via-transition-and-return-path-figures.md`
- `llm_wiki/facts/methods/ferrite-bead-vendor-guidance-boundary.md`
- `llm_wiki/facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`
- `llm_wiki/facts/methods/via-transition-return-path-continuity-boundary.md`
- `llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`

## Current EMC Lane Status

Current state after `P4-219A`:

- `A2`:
  - `existing_fact_layer_reused_only`
- `A3`:
  - `existing_fact_layer_reused_only`
- newly approved EMC promotion from handbook-derived local evidence:
  - `none`
- strongest safe reusable EMC coverage already available:
  - ferrite-bead impedance-curve notation boundary
  - ferrite-bead versus common-mode-choke family distinction boundary
  - via-transition and return-path continuity boundary
  - continuous-reference-plane and split-avoidance boundary

Operational conclusion:

- the next EMC step should be a narrow authority-recovery step
- it should not be another broad handbook review
- it should prioritize exact curve recovery over general routing or cookbook-rule recovery

## Source-Priority Queue

### Priority `P1`: component-owner exact-part or exact-family datasheets

Use first for:

- named ferrite-bead impedance curve recovery
- named common-mode-choke frequency-behavior recovery

Why this is first:

- `P4-215A2` already identified a named ferrite-bead candidate: `BLA3216A102SG4`
- exact curve promotion is blocked mainly by missing original part-level provenance
- datasheets are the most direct route to exact `Z / R / X` curve recovery, part family identity, ratings, and conditions

Expected recovery value:

- `part_scoped_exact_data`
- exact curve ownership
- narrower electrical context such as current, DCR, package, and frequency framing when present

### Priority `P2`: component-owner application notes or official technical overviews

Use second for:

- common-mode versus differential-mode choke behavior for a named family
- vendor-scoped explanation boundaries that are stronger than handbook summaries

Why this is second:

- the current local fact layer already supports family distinction and intended-use vocabulary
- what remains missing is a stronger owner-backed explanation tied to a named choke family or published mode-behavior plot
- this source class is the best candidate when a datasheet alone does not show both `common mode` and `differential mode` traces clearly

Expected recovery value:

- tighter source-backed interpretation for common-mode-choke mode behavior
- better boundary control than generic handbook wording

### Priority `P3`: cross-vendor semiconductor or component-owner method notes

Use third for:

- low-pass topology selection context only if later demand requires it
- cross-vendor reinforcement when a single vendor source is too narrow for article use

Why this is lower:

- current EMC next-step demand is exact-curve recovery, not topology-cookbook recovery
- `P4-215A2` marked topology-selection recipes as blocked, and nothing in `P4-219A` raised them to immediate recovery priority

Expected recovery value:

- method-scoped context
- stronger wording control for future boundary cards
- not the first recovery target for this lane

### Priority `P4`: narrower official layout guidance for slot-crossing or quiet-ground execution

Use only if later prompts require more than the current return-path boundaries.

Why this is deferred:

- `P4-219A` explicitly says these are residual authority-recovery gaps, not current promotion-ready needs
- `A3` already has strong enough boundary language for via transition, return-path continuity, and split avoidance
- the current lane does not need broader routing-rule expansion before exact curve recovery is handled

Expected recovery value:

- only narrow execution-boundary supplementation
- not a prerequisite for the immediate EMC recovery step

## Exact Claim Families Worth Recovering Next

### Queue item `Q1`: named ferrite-bead impedance curve recovery

Recover next:

- the original primary source for `BLA3216A102SG4`, or an exact family-equivalent owner source if the original exact identifier cannot be recovered locally later

Reason:

- this is the strongest exact-data candidate in `A2`
- it has a named part signal already captured in local inventory
- current local facts already define the safe boundary for `Z`, `R`, and `X`; what is missing is owner-backed exact-curve provenance

Recovery target shape:

- named part or exact family
- impedance-versus-frequency curve
- `Z`, `R`, `X` interpretation under owner provenance
- any directly published DCR, rated current, package, and test framing

Promotion posture:

- promote only if the source is owner-backed and the part/family identity is explicit
- keep all performance generalizations blocked unless the owner source states them clearly enough and the claim remains properly scoped

### Queue item `Q2`: named common-mode-choke common-mode versus differential-mode curve recovery

Recover next:

- a component-owner source that shows both `common-mode` and `differential-mode` frequency behavior for a named choke family

Reason:

- this is the second strongest exact-data candidate in `A2`
- the handbook figure is useful inventory, but `P4-215A2` says it lacks enough part-family and electrical-context provenance
- current local facts already cover family distinction, so the missing piece is exact owner-backed curve evidence

Recovery target shape:

- named family or named part
- both mode traces on one official source path if possible
- family context
- DCR and rated-current context when available

Promotion posture:

- recover only enough to support exact curve interpretation and family-scoped method wording
- do not convert the handbook’s generalized “passes without attenuation” wording into a reusable rule unless the owner source supports a narrower scoped version

### Queue item `Q3`: narrow owner-backed component-family distinction reinforcement

Recover only if `Q1` or `Q2` sources do not already supply it.

Reason:

- the current fact layer is already adequate for conservative family distinction
- this class is only worth reopening if exact-curve recovery still leaves ambiguous wording around single-conductor versus paired-conductor usage

Recovery target shape:

- vendor-scoped family distinction
- intended-use vocabulary
- no universal layout or compliance claims

Promotion posture:

- boundary-only
- lower priority than exact curves

## Claims That Remain Blocked

The following claim families are still blocked and are not the next recovery target:

- handbook ferrite-bead curve by itself as promotable exact data
- handbook common-mode-choke curve by itself as promotable exact data
- ferrite beads as broadly better high-frequency filters than ordinary inductors
- generalized low-`Q` ferrite explanation as reusable rule text
- common-mode choke claims that differential current passes without attenuation as a universal statement
- low-pass topology selection recipes by source/load impedance
- via-delay numerics and edge-slowing numerics
- sub-`1GHz` routing prescriptions
- slot-bridging execution recipes
- quiet-ground execution rules
- connector-zone coupling formula `L=5dln(d/w)`
- backplane or connector-zone spacing thresholds such as `10mm`, `15mm`, `20H`, and `3W`
- any compliance, capability, or cookbook-routing claim inferred from the secondary PDF figures alone

Blocking reason class:

- `secondary_pdf_only`
- `missing primary provenance`
- `too generalized for current source strength`
- `already declared boundary-only in prior EMC logs`

## What Should Not Be Reopened Now

Do not reopen these areas in the immediate next EMC recovery step:

- the safe reuse boundary for ferrite-bead `Z / R / X` notation
- the safe reuse boundary for ferrite-bead versus common-mode-choke family distinction
- the safe reuse boundary for via-transition discontinuity and nearby return-path continuity
- the safe reuse boundary for continuous reference plane and split avoidance
- broad `A3` diagram rereview for return-current basics
- handbook-only slot, connector, backplane, and quiet-ground cookbook guidance
- topology-catalog rereview for `Gamma`, `Pi`, or `T` filters unless a later prompt explicitly needs that lane

Reason not to reopen:

- these are already either safely covered by admitted local facts or explicitly blocked
- reopening them would expand scope without increasing authority where the main gap is still exact component-owner curve recovery

## Immediate Next-Step Queue

Execute the next EMC recovery step in this order:

1. Try exact-part or exact-family ferrite-bead source recovery for `BLA3216A102SG4`.
2. Try named-family common-mode-choke source recovery with both `common-mode` and `differential-mode` curves.
3. Extract only the minimal supporting claim set needed for promotion:
   - curve identity
   - owner provenance
   - family or part identity
   - any directly published DCR/current/package context
4. Recheck whether the recovered sources also cover a tighter family-distinction boundary.
5. Stop before topology-cookbook, slot-bridging, quiet-ground, or connector-zone recovery unless a later prompt explicitly expands the demand.

## Blocked Claims For The Next Worker

Blocked for the next EMC recovery step:

- promoting any handbook figure as authority by itself
- recovering broad routing thresholds
- recovering connector formulas
- recovering backplane spacing rules
- converting vendor-scoped component explanations into universal EMC rules
- treating handbook/PDF lanes as authority instead of claim inventory

## Residual Uncertainties

- whether the exact original owner source for `BLA3216A102SG4` is still locally identified only by name or will require later external recovery
- whether the common-mode-choke figure can be matched to a named family with both mode traces and adequate electrical context
- whether future article demand will actually require low-pass topology-selection recovery after exact-curve recovery is done
- whether any later EMC prompt will require stronger slot-bridging or quiet-ground authority beyond the already admitted return-path boundaries

## Changed Files

- `llm_wiki/logs/p4-220a-2026-5-7-emc-authority-recovery-queue-and-source-priority.md`

## Lane Status

- lane type:
  - `queue_definition_only`
- new fact promotion:
  - `not_attempted`
- new source promotion:
  - `not_attempted`
- next EMC recovery posture:
  - `exact_component_owner_curve_recovery_first`
- handbook-derived EMC claims:
  - `remain_claim_inventory_not_authority`
