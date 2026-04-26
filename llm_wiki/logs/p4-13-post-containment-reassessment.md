# P4-13 Post-Containment Reassessment Of Blocked Drafts

Date: 2026-04-26

## Purpose

This control note records the reassessment after the current blocker-reduction stack has landed for both still-blocked high-layer drafts:

- `20-layer` interconnect / process-window / geometry containment
- `22-layer` hi-rel governance / threshold containment

The goal is not to reopen broad source hunting.

The goal is:

- verify whether the blocked drafts are now limited by narrower claim classes
- identify the highest-leverage remaining blocker class on each branch
- decide whether another blocker-reduction pass is still required before any `P4-06` bridge work

## Current Verdict

The readiness verdict remains unchanged:

- `20-layer`: `needs_sources`
- `22-layer`: `needs_sources`
- `P4-06`: blocked

What changed is the blocker shape.

The current blocker surface is no longer mainly `retrieval ambiguity`.

The current blocker surface is now concentrated inside the remaining draft-level claim clusters that still exceed the narrowed boundary stack.

## 20-Layer Reassessment

### Draft-Level Result

`20-layer` remains blocked because the current draft still depends on unsupported:

- shop capability and promotional claims
- geometry and feature-size tables
- stack recipe and lamination-count claims
- process-control and chemistry numerics
- `IST` threshold and qualification claims
- yield, lead-time, and production-scale assertions

### Representative Remaining Claim Clusters

- title / positioning:
  - `Any-Layer HDI & Stacked Microvias`
  - `ELIC construction`
  - `IST reliability qualification`
- HIL capability quote:
  - `stacked microvias spanning up to 6 layers`
  - `trace/space down to 2.5/2.5mil`
  - `IST-verified microvia reliability exceeding 200 thermal cycles`
  - `from NPI prototypes through production volumes`
- architecture / recipe claims:
  - `10 or more sequential lamination`
  - `full 20 layer ELIC (18 lamination cycles)`
  - `5+10+5`
- geometry / registration / feature-size claims:
  - `40-80μm`
  - `60-100μm`
  - `40-60μm`
  - `±15-25μm`
  - `≤5μm`
  - `2.5/2.5mil`
  - `200μm / 250μm / 275μm capture pad`
  - `±75-125μm cumulative misregistration`
- process-control claims:
  - `100% void-free`
  - `CVS analysis every 8 hours`
  - `Accelerator concentration is maintained within ±5%`
  - `±18μm registration accuracy`
  - `Tg degradation exceeding 5°C triggers investigation`
- commercial / production claims:
  - `Yield (typical) | 60-75% | 75-85% | 85-95%`
  - `20-30 business days`
  - `15-20 days`
  - `NPI prototypes from 10 business days`
- qualification / standards claims:
  - `IPC requirements: stacked microvias must survive 200 IST cycles per IPC-2315`
  - `300+ cycles`
  - `IPC-6012 Class 3 and IPC-2226 Type III compliance`

### Assessment

The existing boundary stack already blocks most of these claim families in principle.

What still remains under-contained is the draft's direct use of:

- HIL-specific capability assertions
- HIL-specific process-control numerics
- HIL-specific production-readiness and timeline claims

This means the narrowest next blocker class is no longer generic `any-layer vocabulary leakage`.

It is now:

`shop-asserted capability and process-control numerics for 20-layer any-layer / stacked-microvia marketing claims`

### Decision

Another blocker-reduction pass is still needed before any `P4-06` bridge work.

That pass should target:

- HIL-specific capability claims
- HIL-specific process-control / chemistry-control numerics
- HIL-specific volume / lead-time / sustainment language

## 22-Layer Reassessment

### Draft-Level Result

`22-layer` remains blocked because the current draft still depends on unsupported:

- `Class 2 / Class 3 / Class 3A` threshold tables
- addendum-triggered acceptance claims
- supplier-status and compliance assertions
- coupon / qualification / acceptance-plan numerics
- hi-rel process and manufacturability numerics
- HIL-specific qualification and program-language claims

### Representative Remaining Claim Clusters

- HIL capability quote:
  - `fabricate 22 layer PCBs to IPC-6012 Class 3/3A standards`
  - `full material traceability`
  - `coupon-based qualification testing`
  - `controlled production environments meeting aerospace, defense, and medical quality requirements`
- `Class 3 vs. Class 2` table:
  - `25μm / 50μm`
  - `0% voids permitted`
  - `10s at 288°C, 6 cycles`
  - `≤0.75%`
- `Class 3A` acceptance claims:
  - `100-500 thermal cycles`
  - `>5%`
  - `TML ≤1.0%`
  - `CVCM ≤0.10%`
  - `1.5μg/cm²`
  - `45° angles`
- hi-rel manufacturability claims:
  - `±2mil`
  - `±3mil`
  - `2.8-3.5mm`
  - `0.3mm`
  - `8:1 to 12:1`
  - `50-100% longer`
  - `14-16 layers`
  - `3-4 buildup layers per side`
  - `±8mil`
  - `1.5mm`
  - `3Gbps`
- coupon / acceptance / lifetime tables:
  - `4-6 per panel`
  - `2-4 per panel`
  - `8-12 per panel`
  - `≥25μm average`
  - `≤20%`
  - `≥50μm`
  - `≤1.56μg/cm²`
  - `1000-2000 thermal cycles`
- supplier-status / compliance marketing:
  - `pass qualification testing on the first submission`
  - `Compliance with MIL-PRF-31032 and MIL-PRF-55110 processing requirements`
  - `Certifications: ISO 9001, ISO 14001, UL`

### Assessment

The existing `22-layer` boundary stack already blocks threshold leakage, approval/listing leakage, and lot-acceptance leakage in principle.

What still remains under-contained is the draft's direct use of:

- HIL-specific compliance assertions
- HIL-specific qualification / acceptance assertions
- HIL-specific supplier-status and hi-rel-program marketing language

This means the narrowest next blocker class is no longer generic `Class 3 / addendum threshold leakage`.

It is now:

`supplier-status, compliance, and acceptance-assertion leakage through 22-layer high-reliability marketing language`

### Decision

Another blocker-reduction pass is still needed before any `P4-06` bridge work.

That pass should target:

- HIL-specific `Class 3 / 3A` compliance assertions
- HIL-specific qualification / acceptance / traceability claims
- HIL-specific hi-rel supplier-status and program-language claims

## Cross-Branch Priority Order

After this reassessment, the next long-task order should be:

1. `22-layer supplier-status / compliance / acceptance-assertion containment`
2. `20-layer shop-capability / process-control numeric containment`
3. reassess both blocked drafts again before any `P4-06` bridge work

## Stop Conditions

Do not treat either branch as unlocked if the remaining unsupported claim classes still dominate the current draft.

`P4-06` must stay blocked if any of the following remain true:

- `20-layer` or `22-layer` still show `needs_sources` in `layer-count-blog-readiness.md`
- HIL-specific capability, compliance, or qualification claims still exceed the current source-governance layer
- public standards metadata can still be rewritten into technical thresholds or acceptance proof
- build-up / any-layer / hi-rel wording can still be rewritten into shop capability, supplier status, or release-authority claims

## Current Decision

The next long-task execution step under `P4-13` should be:

- `22-layer supplier-status / compliance / acceptance-assertion containment`

The following step should be:

- `20-layer shop-capability / process-control numeric containment`

Until those land and are reassessed again:

- `20-layer` remains `needs_sources`
- `22-layer` remains `needs_sources`
- `P4-06` remains blocked
