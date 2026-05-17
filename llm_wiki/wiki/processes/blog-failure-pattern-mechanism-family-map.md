---
topic_id: "processes-blog-failure-pattern-mechanism-family-map"
title: "Blog Failure Pattern Mechanism Family Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-14"
fact_ids:
  - "methods-pcba-ict-fixture-strain-and-mlcc-latent-damage-boundary"
source_ids:
  - "murata-mlcc-test-probe-board-flex-precaution-faq"
  - "murata-small-mlcc-board-bending-caution-pdf"
  - "tdk-mlcc-flex-crack-cause-and-consequence-faq"
tags: ["prompt-consumption", "failure-pattern", "mechanism-family", "taxonomy", "writing-routing", "engineering-depth"]
---

# Definition

> This page is the writing-facing routing map for failure patterns. Its job is to stop PCB / PCBA blogs from using one generic `risk exists` paragraph across every topic family. Before drafting a failure pattern, first classify the article into a primary mechanism family, then retrieve facts and examples that match that family.

## Why This Page Exists

- Many weak drafts already had `a failure pattern`, but the pattern was too generic because it was not tied to the topic's actual failure mechanism.
- The most common failure was not factual wrongness; it was mechanism collapse:
  `test`, `stackup`, `thermal`, `assembly`, and `quote-package` topics were all being flattened into review posture and generic warnings.
- This page gives prompt work one shared routing surface so the agent first asks `what truly fails here?` before it asks `how do I structure the H2s?`

## Primary Mechanism Families

| Mechanism family | Best-fit topic families | What the failure pattern must show | Default retrieval keywords |
| --- | --- | --- | --- |
| `mechanical load / strain` | `ICT`, fixture, probing, support tooling, depanel support, connector insertion, press-fit, edge handling | Where force enters the board, what structure takes local strain, and why the damage can be latent rather than immediate | `probe load`, `board flex`, `mechanical strain`, `support`, `micro-crack`, `latent damage`, `open solder joint`, `MLCC`, `fixture` |
| `electrical field / return path collapse` | `SI`, `PI`, impedance, DDR, RF, EMC, ESD, connector launch | Which reference, coupling, or protection path becomes discontinuous and what electrical symptom appears | `return path`, `plane split`, `stitching via`, `crosstalk`, `eye closure`, `overshoot`, `ESD path`, `stub`, `field coupling` |
| `thermal mismatch / heat path` | thermal, power, LED, heavy copper, MCPCB, heat-spreading, rework heat | Where heat accumulates or cannot escape, where expansion mismatch appears, and what reliability or assembly consequence follows | `thermal path`, `hot spot`, `CTE mismatch`, `heat spreading`, `thermal fatigue`, `voiding`, `delamination`, `thermal cycle` |
| `process window interaction` | stencil, reflow, via-in-pad, warpage, coplanarity, solderability, assembly DFM | Why a design that looks buildable still compresses the process window and turns into variation, rework, or unstable yield | `process window`, `warpage`, `coplanarity`, `bridging`, `insufficient wetting`, `tombstone`, `paste release`, `rework` |
| `chemical / surface condition` | coating, cleaning, residue, contamination, corrosion, surface finish, interface adhesion | Which residue, surface state, or chemical interface is uncontrolled and how it becomes leakage, corrosion, adhesion, or wetting failure | `residue`, `ionic contamination`, `electrochemical migration`, `corrosion`, `surface condition`, `adhesion`, `wetting`, `oxidation` |
| `data-package incompleteness / governance failure` | quote package, Gerber, ODB++, IPC-2581, BOM completeness, fabrication drawing, stackup note, release docs | Which input is missing or ambiguous, who must stop, and why that gap becomes EQ, wrong assumptions, rework, or release delay | `missing input`, `ambiguity`, `package completeness`, `EQ hold`, `netlist`, `coordinate data`, `stackup note`, `fabrication drawing`, `release package` |

## How To Use This Page

1. Classify the article into one primary mechanism family before drafting the failure pattern.
2. Pull the matching local facts, wiki pages, or source records first.
3. If the local corpus only supports posture language but not the mechanism family itself, do not mark the article `ready`; recover sources first.
4. If two families both matter, choose one as the primary chain and keep the second as a supporting risk, not a replacement.

## Routing Rules By Family

### Mechanical Load / Strain

- Default for `ICT / fixture / probe / support tooling` topics.
- The pattern should usually look like:
  `force entry -> local board flex / strain -> fragile package or joint damage -> latent field or release consequence`
- Use [ict-fixture-introduction-and-method-selection.md](/code/blogs/llm_wiki/wiki/processes/ict-fixture-introduction-and-method-selection.md) and `methods-pcba-ict-fixture-strain-and-mlcc-latent-damage-boundary` first.

### Electrical Field / Return Path Collapse

- Default for `stackup / SI / PI / RF / EMC / ESD` topics.
- The pattern should usually look like:
  `uncontrolled path / split / discontinuity -> field or current-return distortion -> measurable signal, EMC, or protection failure`
- Do not accept a draft that only says `review burden increased`; it must name the broken path.

### Thermal Mismatch / Heat Path

- Default for `thermal / MCPCB / LED / power` topics.
- The pattern should usually look like:
  `incomplete heat path or CTE mismatch -> local hot spot / repeated stress -> solder, interface, or material-life consequence`

### Process Window Interaction

- Default for `assembly / stencil / reflow / solderability / warpage` topics.
- The pattern should usually look like:
  `marginal geometry or sequencing -> narrower assembly window -> visible process variation, rework, or release pause`

### Chemical / Surface Condition

- Default for `coating / cleaning / contamination / surface-finish behavior` topics.
- The pattern should usually look like:
  `uncontrolled residue or surface state -> interface or electrochemical problem -> leakage, corrosion, poor wetting, or adhesion loss`

### Data-Package Incompleteness / Governance Failure

- Default for `quote package / BOM completeness / data exchange / release docs` topics.
- The pattern does not need physical breakage, but it still must be causal:
  `missing definition -> wrong assumption or EQ stop -> rework, delay, or incorrect release path`

## Common Failure Of Failure Patterns

- Writing one generic warning paragraph that could fit five adjacent topics.
- Using `review burden` as the whole mechanism instead of naming what physically or procedurally failed.
- Borrowing a mechanical example for an SI article, or a thermal example for a quote-package article, just because it feels vivid.
- Adding a dramatic case study without enough local or source-backed mechanism support.

## Decision Standard

- If replacing the article keyword with a neighboring keyword leaves the failure pattern almost unchanged, the mechanism family is still too generic.
- If the draft cannot name the `force path`, `field path`, `heat path`, `process window`, `surface state`, or `missing package field`, the mechanism is not specific enough yet.
- If the corpus has no local support for the needed mechanism family, the article is not `ready`; it is a source-recovery task.

## Current Strongest Local Example

- The strongest currently landed explicit mechanism-family example is the dense ICT lane:
  `probe load -> board flex -> small-MLCC crack or open solder joint -> latent open/short risk`
- That lane is now the reference example for how future articles should move from generic posture to real mechanism.
