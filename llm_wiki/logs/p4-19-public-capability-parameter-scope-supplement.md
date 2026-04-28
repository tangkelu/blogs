# P4-19 Public Capability Parameter Scope Supplement

Date: 2026-04-27

## Purpose

Extract real parameter claims from local English APT and HIL public JSON pages for prompt use without inventing factory capability.

This is not a blog-writing round.

This is not a capability unlock round.

This is a scope-and-governance round for public-site parameter consumption.

## Source Scope Used

English local JSON only:

- `/code/hileap/frontendHIL/public/static/products/en`
- `/code/hileap/frontendAPT/public/static/pcb/en`
- `/code/hileap/frontendAPT/public/static/pcba/en`
- `/code/hileap/frontendAPT/public/static/capabilities/en`

Non-goals for this round:

- no translated-page extraction
- no edits to source JSON
- no edits to protected log files
- no conversion of page claims into supplier-proof capability

## What Landed

New fact cards:

- `facts/methods/parameter-scope-public-capability-drilling-and-via-geometry.md`
- `facts/methods/parameter-scope-public-capability-impedance-and-validation.md`
- `facts/methods/parameter-scope-public-capability-construction-windows.md`
- `facts/methods/parameter-scope-public-capability-coating-and-fine-pitch-assembly.md`

New process map:

- `wiki/processes/public-capability-parameter-consumption-map.md`

## Parameter Families Captured

### Drilling And Via Geometry

- mechanical drill minimum
- laser microvia minimum
- backdrill depth accuracy
- residual stub claim
- aspect ratio claim
- HDI trace/space claim
- microvia aspect-ratio claim

### Impedance And Validation

- impedance tolerance claim
- TDR coverage claim
- coupon-based TDR claim
- sample-based VNA claim
- RF/PTFE validation-frequency claim

### Construction Windows

- layer-count claim
- board-thickness claim
- copper-weight claim
- flex-core thickness claim
- sequential-lamination claim
- bend-radius claim

### Coating And Fine-Pitch Assembly

- coating family vocabulary
- coating thickness claim
- coating application-method claim
- cure-family claim
- fine-pitch BGA/QFN pitch claim
- component-size claim
- placement-accuracy claim
- void-target claim
- rework-cycle claim
- inline-inspection / AXI / cleanliness claim

## Governance Outcome

The new cards explicitly fix the scope at:

- `public website claim`
- `page context`
- `language=en`
- checked on `2026-04-27`

The cards also explicitly block these upgrades:

- supplier-independent proof
- lot capability
- qualification proof
- acceptance threshold
- universal master capability table

## Why This Round Was Needed

The repo already had strong boundary cards for capability families, drilling posture, impedance posture, HDI posture, coating posture, and fine-pitch process flow.

What it did not yet have was a clean place to store:

- exact parameter claims that the English public pages do make
- the exact `source_id` that owns each claim
- the rule that these claims remain page-scoped prompt support rather than factory-proof evidence

This round closes that gap.

## Key Extracted Claims Added

- `0.15 mm` mechanical drill, `0.075 mm` UV laser microvia, `±50 μm` backdrill depth accuracy, `under 200 μm` residual stub
- `±5Ω / ±7%` and `100% TDR` on APT impedance page
- `±3–5% with TDR`, `sample-based VNA`, `up to 40 GHz` on HIL PTFE page
- `50–75 μm` HDI microvia, `75/75 μm` standard and `50/50 μm` advanced trace/space on HIL HDI page
- HDI, rigid-flex, and PTFE layer/thickness/copper windows from APT and HIL family pages
- `1–5 mil (25–127 μm)` coating thickness and manual / automated / robotic selective coating methods
- `0.3 mm` BGA/QFN pitch, `±25 μm` placement, `BTC void <10%`, `rework ≤3 cycles`
- SMT placement `±25 μm @ 3σ` standard and `±8 μm @ 3σ` advanced, `0.2–0.25 mm` advanced fine pitch, `≤1.56 μg/cm²` ionic cleanliness claim

## Remaining Gaps

- No Tier 1 dated internal capability record was created or discovered in this round.
- These cards still do not authorize reusable factory capability tables.
- Several page claims mix marketing, capability, and standards-adjacent wording; those values remain refresh-sensitive.
- Some extracted numbers are stronger than current governance would allow for universal evidence-pack reuse and therefore stay page-scoped only.
- Acceptance-threshold, compliance, and qualification meanings still need separate source layers if later prompts require them.

## Verification Target

This round is complete when:

1. the new fact cards resolve their `source_id` references
2. the new process map resolves its `fact_id` and `source_id` references
3. `git diff --check` passes for the newly added files
