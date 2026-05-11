# P4-247 Post-A1 Next Exact-Data Lane Selection: B1 Over C2

Date: 2026-05-07

## Purpose

Choose the next highest-yield exact-data recovery lane for `/code/blogs/tmps/PCB资料` after the current `A1 capacitor` continuation reached a useful but partially stalled state.

This log exists so a later AI does not reopen broad scouting across `B1/B2/B3/C2/C3` and can instead continue from one bounded next lane with one explicit fallback lane.

## Inputs Reviewed

- `logs/p4-215b-2026-5-6-pcba-inspection-exact-data-workstream.md`
- `logs/p4-215b1-2026-5-6-pcba-lane-b1-eos-esd-handling-pages.md`
- `logs/p4-215b2-2026-5-6-pcba-lane-b2-solder-defect-and-workmanship-pages.md`
- `logs/p4-215b3-2026-5-6-pcba-lane-b3-cleanliness-warpage-jumper-orientation-pages.md`
- `logs/p4-215c2-2026-5-6-package-lane-c2-pad-origin-pin1-keepout-drawings.md`
- `logs/p4-215c3-2026-5-6-package-lane-c3-library-governance-and-hole-pad-examples.md`
- `logs/p4-219b-2026-5-7-pcba-taxonomy-first-promotion-review.md`
- `logs/p4-219c-2026-5-7-package-footprint-governance-promotion-review.md`
- `policies/exact-data-admission-policy.md`
- subagent audit memos for `B1` and `C2/C3`

## Decision

Current default continuation is:

- `B1-R1: ESD workstation grounding exact-data recovery`

Current fallback continuation is:

- `C2-R1: BGA pitch-to-pad-diameter official-source recovery`

## Why `B1-R1` Wins

### Strongest bounded recoverable target

`B1` contains one narrow candidate that already looks like an official-source replacement lane rather than a handbook-only cookbook rule:

- `ESD-safe workbench grounding layout`
- `1 MOhm` resistor-path / grounding-method context
- named workstation elements such as wrist strap, tabletop mat, floor mat, and common ground point

This has a plausible path to either:

- `standard_scoped_exact_data`
- or `method_scoped_exact_data`

depending on whether the stronger replacement source is a public standards-body page or an owner-backed ESD-control technical guide.

### Better yield than `B2/B3`

`B2` and `B3` are still useful, but their highest-value content is now already captured at:

- taxonomy
- visual-language boundary
- structural-context asset level

Their remaining handbook numbers are mostly:

- accept / reject thresholds
- geometry thresholds
- warpage percentages
- jumper-wire prescriptions
- workmanship judgments

Those are low-confidence promotion targets under the current admission policy.

### Better near-term yield than `C2/C3`

`C2` still has one meaningful follow-on lane in:

- `BGA pitch-to-pad-diameter table`

But much of `C2/C3` remains entangled with:

- handbook geometry defaults
- package-family compensation formulas
- branded or workflow-shaped rule surfaces
- threshold bands such as `optimal / general / risk / danger`

That makes `C2/C3` a valid secondary queue, but not the best immediate lane.

## Explicit Lane Ranking

1. `B1-R1: ESD workstation grounding exact-data recovery`
2. `C2-R1: BGA pitch-to-pad-diameter official-source recovery`
3. `C2-R2: through-hole / SMD pad-relationship formula replacement`
4. `B1-R2: ESD warning / protection symbol identity recovery`
5. everything else in current `B2/B3/C3` residual numerics remains `blocked_or_low_yield_for_now`

## Scope For `B1-R1`

### In scope

- page `11` grounding-layout method content first
- page `10` only as claim inventory comparison, not as direct fact source
- exact official wording for:
  - workstation elements
  - resistor-path role
  - grounding relationship
- any public exact parameter that is explicitly stated by the stronger source and can be preserved with scope

### Out of scope

- handbook `page 8` generic device-family sensitivity ranges
- handbook `page 7` magnification table unless a strong official public replacement is found
- handbook `0.5V`, `0.3V`, and similar threshold fragments
- reconstructing paywalled or implied standards content from the secondary PDF
- treating local symbols or workstation drawings as authority by themselves

## Expected Artifact Shape

If `B1-R1` succeeds, the next AI should aim for:

- `1` source record in `sources/registry/`
- `1` narrow fact card in `facts/methods/` or `facts/standards/`
- `1` controller log recording:
  - what was admitted
  - what remained blocked from `B1`
  - what exact scope restrictions apply

Safe target posture:

- `method_scoped_exact_data` or `standard_scoped_exact_data`
- workstation-grounding method only
- no universal compliance rewrite

## Non-Winning Candidate Retention

`C2-R1` should stay active in backlog because it is still the best non-PCBA next lane.

It should be reopened only if:

- `B1-R1` fails on authority access or public-source availability
- or a later prompt explicitly needs package / footprint exact numeric recovery next

## Resulting Program Direction

Program state after this decision:

- `A1 capacitor` remains valuable and partially open, but no longer monopolizes active continuation
- `B1-R1` is now the default next exact-data recovery lane outside `A1`
- `C2-R1` is the preferred fallback lane
- `B2/B3/C3` remain primarily taxonomy / governance / supporting-asset territory unless stronger narrow authority appears
