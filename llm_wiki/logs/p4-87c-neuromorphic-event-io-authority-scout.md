Date: 2026-05-01
Lane: `P4-87c neuromorphic event-io authority scout`
Input: `/code/blogs/tmps/2026.4.29/en/neuromorphic-computing-pcb.md`
Output: `/code/blogs/llm_wiki/logs/p4-87c-neuromorphic-event-io-authority-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `source_backed_fact_layer_partial`

# Purpose

This scout log treats `neuromorphic-computing-pcb.md` as claim inventory only, checks what `llm_wiki` can already support safely, and records the exact-noun authority gaps that still block a source-backed neuromorphic identity lane.

This lane does not create facts, source records, wiki pages, or tracker updates. It is deletion-safe reconnaissance only.

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-87c-neuromorphic-event-io-authority-scout.md`

# Lane Status

- Draft inspected: `neuromorphic-computing-pcb.md`
- Current disposition: `topic_inventory_only` with `partial_reuse_available`
- Best next narrow lane: `neuromorphic event-io and platform identity`
- Recommended output shape for a later integration pass:
  `facts/interfaces/neuromorphic-event-io-and-platform-identity-boundary.md`

# Draft Surface Observed

Primary exact nouns and claim families appearing in the draft:

- neuromorphic concepts: `neuromorphic`, `spiking neural network`, `SNN`, `sub-threshold`, `event-driven`, `STDP`
- product / vendor nouns: `Intel Loihi 2`, `IBM NorthPole`, `BrainChip Akida`, `SynSense Speck`, `SynSense Xylo`
- sensor / event nouns: `DVS`, `Dynamic Vision Sensor`, `silicon cochlea`, `AER`
- interface / platform nouns: `PMBus`, `I2C`, `USB 3.2`, `GbE`, `PCIe Gen 4`, `LVDS`, `sub-LVDS`, `COM Express`, `Jetson-compatible`
- manufacturing / capability claims: research boards, production modules, ICT, conformal coating, HDI, chip-on-board, custom interposers

High-risk claim clusters in the draft:

- power, noise, skew, jitter, temperature, and thermal-cycle numerics
- exact product-performance claims for `Loihi 2`, `NorthPole`, `Akida`, and event sensors
- shipping / production / deployment claims across robotics, satellite, hearing-aid, medical, defense, and industrial sectors
- supplier capability claims for board count, turnaround, volume, validated noise floor, and production-module readiness

# Existing `llm_wiki` Support Checked

## Primary batch boundary

- `p4-83-2026-4-29-expert-batch-controller-summary`
  Path: `/code/blogs/llm_wiki/logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
  Use: places `neuromorphic-computing-pcb.md` in the `Compute Carrier, Consumer Audio, And Interactive Hardware Lane` and explicitly blocks exact neuromorphic-chip claims without owner sources.

## Safe reuse classes already available

- `methods-high-speed-interface-system-context`
  Path: `/code/blogs/llm_wiki/facts/methods/high-speed-interface-system-context.md`
  Use: guarded system-context support for `PCIe` generation vocabulary and broader high-speed board-pressure framing.

- `standards-embedded-imaging-serial-interface-boundary`
  Path: `/code/blogs/llm_wiki/facts/standards/embedded-imaging-serial-interface-boundary.md`
  Use: guarded `LVDS` vocabulary only at interface-family level.

- `standards-interface-wireless-positioning-product-level-boundary`
  Path: `/code/blogs/llm_wiki/facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
  Use: guarded `Ethernet` family vocabulary only at standards-owner context level.

- `processes-usb-connector-and-capability-taxonomy-boundaries`
  Path: `/code/blogs/llm_wiki/wiki/processes/usb-connector-and-capability-taxonomy-boundaries.md`
  Use: guarded `USB 3.2` family naming as capability taxonomy, not board-proof.

- `methods-maker-platform-official-identity-boundary`
  Path: `/code/blogs/llm_wiki/facts/methods/maker-platform-official-identity-boundary.md`
  Use: adjacent precedent that named compute platforms need owner-backed product identity before they can be reused safely.

- `wiki/testing/pcba-quality-gates-and-test-strategy`
  Path: `/code/blogs/llm_wiki/wiki/testing/pcba-quality-gates-and-test-strategy.md`
  Use: guarded `ICT`, inspection, and functional-test workflow vocabulary for assembled boards.

- `methods-hidden-joint-xray-inspection-boundary`
  Path: `/code/blogs/llm_wiki/facts/methods/hidden-joint-xray-inspection-boundary.md`
  Use: guarded dense-package inspection context if future rewrites discuss hidden-joint assemblies.

## Exact local absences confirmed

No neuromorphic-specific owner or standards layer was found locally for:

- `Loihi` / `Loihi 2`
- `Akida`
- `NorthPole`
- `SynSense`
- `Speck`
- `Xylo`
- `DVS`
- `Dynamic Vision Sensor`
- `AER`
- `silicon cochlea`
- `STDP`
- `PMBus`
- `COM Express`
- `Jetson-compatible`
- `sub-LVDS`

# Safe Reuse Classes

These classes are safe to reuse now, but only conservatively:

- Generic high-speed compute board context around mixed-signal pressure, dense-package review, validation staging, and system-level interface planning.
- Guarded `PCIe` generation vocabulary from the existing high-speed interface context layer.
- Guarded `USB 3.2` naming as a capability family, not as proof of board throughput or implementation quality.
- Guarded `Ethernet` family vocabulary through the IEEE-backed interface boundary, which can cover `GbE` only as broad interface context.
- Guarded `LVDS` vocabulary via the existing MIPI/TI serial-interface boundary.
- Generic PCBA inspection and test-stack wording around `ICT`, `X-ray`, and functional test as process layers.
- Generic multilayer / HDI / chip-on-board / interposer manufacturing vocabulary only when kept at process-family level and not turned into neuromorphic readiness proof.

# Blocked Claims

The current corpus still blocks these claim families for this draft:

- Any numeric claim for current swing, response time, noise floor, PSRR, voltage range, telemetry bandwidth, skew, jitter, timestamp accuracy, thermal rise, converter efficiency, thermal cycles, layer count, board size, turnaround, or production volume.
- Any claim that `Loihi 2`, `NorthPole`, `Akida`, `Speck`, or `Xylo` is shipping in production, production-ready, or deployed in named end markets without exact owner-backed sources.
- Any claim that `SNN`, `STDP`, `DVS`, `AER`, or `silicon cochlea` implies a stable board-interface standard, interoperability guarantee, or reusable electrical target.
- Any use of `PMBus` as proof of fast adaptive voltage scaling, rail telemetry quality, or production power-management capability without standards-owner or device-owner support.
- Any use of `PCIe Gen 4`, `USB 3.2`, `GbE`, `LVDS`, or `sub-LVDS` as proof of timing, bandwidth, signal integrity, or interoperability.
- Any use of `COM Express` or `Jetson-compatible` as proof of module compatibility, ecosystem support, or production-platform readiness.
- Any supplier claim for HILPCB capability, evaluation-board volume, production-module scale, validated noise floor, medical / defense / aerospace suitability, or quality performance.

# Source Gap Inventory

## Highest-value authority gaps

These are the cleanest next exact-noun recovery candidates inferred from the draft and current local gaps:

- `Intel Loihi 2`
  Need: owner-backed product or program identity page from Intel's neuromorphic program.
  Why: the draft foregrounds `Loihi 2` in title-adjacent and opening positioning.

- `BrainChip Akida`
  Need: owner-backed BrainChip product page or official documentation anchor.
  Why: `Akida` is the strongest product-level noun in the draft's sensor and platform sections.

- `SynSense Speck` and `SynSense Xylo`
  Need: owner-backed SynSense product pages or official documentation anchors.
  Why: these are exact platform nouns in the event-interface section and are currently unsupported locally.

- `PMBus`
  Need: standards-owner or consortium anchor for PMBus identity and scope.
  Why: the draft uses `PMBus/I2C voltage programming` as part of a control-plane architecture claim.

## Medium-value gaps

- `DVS` / `Dynamic Vision Sensor`
  Need: owner-backed event-camera identity pages, likely from named sensor vendors if the rewrite must preserve exact vendor nouns.
  Why: current local support covers `LVDS` and generic imaging serial links, but not neuromorphic event-camera identity.

- `AER`
  Need: primary-source recovery lane, likely literature or vendor technical documentation rather than an obvious public standards-owner page.
  Why: the draft treats `AER` like a stable interface noun, but no local authority layer exists.

- `COM Express`
  Need: standards-owner or consortium source for module-form-factor identity if the rewrite keeps that noun.
  Why: current local platform support covers Raspberry Pi precedent only, not COM Express.

- `Jetson-compatible`
  Need: owner-backed NVIDIA platform identity or module-program documentation if the rewrite keeps this compatibility noun.
  Why: no local NVIDIA / Jetson authority layer exists.

## Lower-confidence or research-heavy gaps

- `SNN`, `STDP`, and `silicon cochlea`
  Likely need a separate literature-driven lane instead of an owner-product lane.
  They are concept or architecture nouns, not clean public standards-owner nouns in the current corpus.

- `IBM NorthPole`
  Likely needs a separate owner or primary-research recovery pass.
  It is present in the opener but does not appear to be the best first noun to recover for a narrow event-io lane.

- `sub-LVDS`
  Needs a narrower public source if future rewrites must retain it exactly.
  Current `LVDS` support does not automatically normalize into `sub-LVDS`.

# Recommended Next Integration Shape

If this lane is selected for mainline integration, keep it narrow:

- Fact target:
  `facts/interfaces/neuromorphic-event-io-and-platform-identity-boundary.md`
- Minimal noun scope:
  `Loihi 2`, `Akida`, `Speck`, `Xylo`, `PMBus`, `DVS`, `AER`, plus guarded reuse of already-supported `PCIe`, `USB 3.2`, `Ethernet`, and `LVDS`
- Explicit exclusions:
  all draft numerics, power-integrity targets, signal-integrity thresholds, thermal targets, production scale, medical / aerospace / defense deployment claims, and supplier capability claims

# Practical Recovery Order

1. Recover owner-backed product identity for `Akida`, `Loihi 2`, `Speck`, and `Xylo`.
2. Recover a standards-owner or consortium anchor for `PMBus`.
3. Decide whether `DVS` should be handled as a vendor-identity lane or deferred.
4. Defer `AER`, `STDP`, and `silicon cochlea` unless the rewrite truly requires those exact nouns.
5. Add separate platform-owner coverage later only if `COM Express` or `Jetson-compatible` must remain in the article.

# Summary Judgment

`neuromorphic-computing-pcb.md` is still blocked as a source-backed rewrite target. The current corpus can safely support only generic high-speed-compute, mixed-signal, inspection, and interface-family context. The missing value is not another broad process card; it is a narrow owner-and-interface identity lane around exact neuromorphic product and event-io nouns.
