---
lane: "P4-59B RF cable external-authority scout"
title: "Official-source recovery scout for 2025.11.10 radio-frequency-cable draft"
status: "source_backed_fact_layer_partial"
checked_at: "2026-04-30"
model: "gpt-5.4"
owner_scope: "/code/blogs/llm_wiki/logs/p4-59b-2025-11-10-rf-cable-official-source-recovery-scout.md"
input_files:
  - "/code/blogs/tmps/2025.11.10/en/radio-frequency-cable.md"
  - "/code/blogs/llm_wiki/logs/p4-58a-2025-11-10-rf-cable-authority-scout.md"
  - "/code/blogs/llm_wiki/logs/p4-58-parallel-scout-controller-summary.md"
scope_notes:
  - "draft treated as claim inventory, not authority"
  - "allowed edit honored: output log only"
  - "no tracker, source-registry, fact, wiki, or unrelated log edits"
---

# Purpose

Deletion-safe recovery scout for the narrow RF cable identity lane requested after `P4-58A`.

This pass only asks whether a small official-source-backed promotion is now possible for:

- RF cable identity
- taxonomy boundaries
- impedance-context boundaries

It does not promote draft-originated performance, sourcing, capability, or HILPCB claims.

# Starting Point From Prior Scout

`P4-58A` correctly left the lane at `scout_only` and identified the best next move as:

- measurement-owner support for characteristic-impedance / reflection language
- cable-owner support for coaxial family identity
- connector-owner support for 50 ohm / 75 ohm variant reality

That direction was confirmed by this external pass.

# Official Public Sources Checked

## Measurement-owner sources

1. `NI` RF switch-network guide
   - URL: `https://www.ni.com/en/shop/electronic-test-instrumentation/switches/what-are-switches/guide-to-understanding-and-developing-an-rf-switch-network/chapter-4--effects-of-impedance-matching-and-switch-quality-on-r.html`
   - usable support:
     - coaxial cables are treated as RF transmission-line examples
     - characteristic impedance is a real line property
     - matching source / line / load impedance is used to reduce reflections and improve power transfer
     - TDR is a measurement route for impedance discontinuities

2. `Keysight` network-analysis fundamentals
   - URL: `https://www.keysight.com/us/en/learn/hubs/measurement-fundamentals/network-analysis.html`
   - usable support:
     - cables and connectors should be impedance-matched to the DUT to minimize reflection
     - connector characteristic impedance is part of the RF measurement chain

3. `Keysight` coaxial termination pages
   - URL: `https://www.keysight.com/us/en/product/909E/coaxial-termination-dc-3-ghz-75-ohms.html`
   - URL: `https://www.keysight.com/us/en/product/909A/coaxial-termination-dc-18-ghz.html`
   - usable support:
     - official 75 ohm coaxial systems exist
     - official 50 ohm coaxial systems exist
     - both are discussed explicitly as characteristic-impedance termination cases

## Cable-owner sources

4. `Amphenol RF` coaxial cable guide
   - URL: `https://www.amphenolrf.com/en-us/engineering-center/engineering-resources/coaxial-cable-guide/`
   - usable support:
     - coaxial cable construction can be stated conservatively as center conductor, dielectric, metallic shield, and outer insulating layer
     - coaxial cable is used for RF, video, and data signals
     - the guide explicitly lists coaxial family groupings including flexible, semi-rigid / conformable, micro-coaxial, and corrugated cable
     - the guide includes RG and LMR-family rows, but those rows were not used here for application mapping or performance claims

5. `Times Microwave Systems` semi-rigid family pages
   - URL: `https://timesmicrowave.com/cable-families/semi-rigid-coaxial-cables/`
   - URL: `https://timesmicrowave.com/cables/sr-086-coax-cables/`
   - usable support:
     - semi-rigid cable assemblies are a real cable-owner family
     - semi-rigid coaxial assembly language exists on official cable-owner pages
   - caution:
     - these pages are product-family pages, so they support family identity more than generic educational taxonomy

## Connector-owner sources

6. `TE Connectivity` BNC connector family page
   - URL: `https://www.te.com/en/products/connectors/rf-connectors/coax-connectors/intersection/bnc-connectors.html`
   - usable support:
     - official coaxial connector families are offered in both 50 ohm and 75 ohm variants
     - connector-side impedance variants are real and productized, not draft invention

## Checked but not strong enough for generic RF-cable promotion

7. `Samtec` micro-coax and twinax high-speed pages
   - URL: `https://www.samtec.com/high-speed-cable/micro-coax-twinax/coax/`
   - URL: `https://www.samtec.com/high-speed-cable/micro-coax-twinax/qseries/`
   - finding:
     - useful for proving micro-coax and twinax product-family existence in high-speed interconnects
     - not strong enough to justify presenting twinax as a generic RF cable explainer branch in this draft

8. `NI` triaxial product / guarding pages
   - URL: `https://www.ni.com/en-ca/support/model.triaxm-triaxm.html`
   - URL: `https://www.ni.com/docs/en-US/bundle/pxie-4144/page/using-guard.html`
   - finding:
     - useful for instrument-side triax / guarding context
     - not strong enough to justify triax as a generic mainstream RF cable taxonomy branch in this draft

# Narrowest Source-Backed Promotion Candidate

## Candidate lane

`RF cable identity reduced to coaxial-centered identity plus impedance-matching context`

## Why this is the narrowest promotable layer

The official-source pack is strongest when the draft is reduced to:

- coaxial cable as the central, source-backed cable form for this article lane
- semi-rigid and micro-coax as coaxial subfamily names only
- impedance matching as a boundary concept for cables and connectors
- existence of 50 ohm and 75 ohm coaxial systems / connector variants

The official-source pack is not strong enough for:

- a broad “all RF cable types” explainer
- universal application rules
- performance rankings
- supplier-selection or custom-manufacturer claims

# Exact Conservative Unlock

The following appears promotable to `source_backed_fact_layer_partial` if kept this narrow:

1. Identity
   - `RF cable` language may be narrowed to `coaxial cable / coaxial cable assembly` identity rather than a broad umbrella for every adjacent cable family.
   - Conservative support exists for saying a coaxial cable has a center conductor, dielectric, metallic shield, and outer insulating layer, and is used for RF signal transmission.

2. Taxonomy boundary
   - It is supportable to name `semi-rigid` and `micro-coaxial` as coaxial-family variants because official cable-owner pages explicitly present them that way.
   - This should be framed as `coaxial-family examples`, not as a complete universal RF-cable taxonomy.

3. Impedance-context boundary
   - It is supportable to say characteristic impedance matters in RF interconnect paths and that cables / connectors should be impedance-matched to reduce reflections.
   - It is supportable to say official coaxial ecosystems include both `50 ohm` and `75 ohm` variants.
   - It is not yet supportable from this lane alone to turn that into a universal selection rule like `50 ohm means communications, 75 ohm means broadcast` across all RF cable contexts.

## Recommended fact-shape if promoted later

- `coaxial cable structure and RF-signal role`
- `coaxial-family variants: semi-rigid and micro-coax`
- `impedance-matching boundary for RF cable and connector chains`
- `50 ohm and 75 ohm variant existence without overgeneralized application mapping`

# Blocked Residual Claims

These remain blocked even after this recovery pass.

## Still blocked: broad taxonomy

- treating `twinax`, `triax`, `micro-coax`, `semi-rigid`, `coaxial`, and example trade families as one settled generic RF-cable taxonomy
- presenting `twinax` or `triax` as mainstream RF cable branches from this draft's current framing

## Still blocked: example-family promotion

- `RG-58`, `RG-213`, and `LMR` application-fit claims from the draft
- any comparative language such as lightweight, high-power, low-loss, or “best for” without exact product-scoped sourcing

## Still blocked: impedance application rules

- `50 ohm for communication systems` as a universal rule
- `75 ohm for broadcast and video systems` as a universal rule
- any implication that impedance choice can be safely taught without connector, system, and measurement context

## Still blocked: performance and environment

- low-loss claims
- shielding-effectiveness claims
- crosstalk-reduction claims
- flexibility / durability rankings
- long-distance or high-frequency superiority claims
- environmental suitability claims

## Still blocked: application mapping

- telecom
- broadcasting
- aerospace
- defense
- medical
- IoT
- automotive
- test-equipment

These may be true for specific products, but this lane did not recover article-safe generic source support for them.

## Still blocked: commercial and supplier claims

- sourcing difficulty claims
- reliable manufacturer-selection guidance
- custom RF cable procurement claims
- all `HILPCB` service, quality, lead-time, capability, integration, and custom-manufacturing claims

# Residual Gaps

The main gaps preventing a broader unlock are:

1. no strong generic official source that cleanly treats `twinax` and `triax` as part of a general RF-cable explainer rather than as high-speed or instrumentation-specialty branches
2. no official-source pack here for attenuation, VSWR, return-loss, shielding, or cable-loss comparisons at article-safe generality
3. no dated capability evidence for HILPCB custom RF cable production or sourcing claims
4. no source-backed bridge from example cable names like `RG-58` or `LMR` to the draft's application recommendations

# Recommended Next Record Set

If a future session wants to widen this lane safely, the next best records would be:

1. one stronger connector-owner or cable-owner educational page that directly compares `50 ohm` and `75 ohm` without collapsing into oversimplified application rules
2. one stronger official page for `twinax` identity in RF or interconnect context
3. one stronger official page for `triax` identity outside narrow guarding / electrometer instrumentation
4. dated internal capability evidence if commercial RF-cable service claims are ever to be promoted

# Final Judgment

## Changed file

- `/code/blogs/llm_wiki/logs/p4-59b-2025-11-10-rf-cable-official-source-recovery-scout.md`

## Sources checked

- `NI`
- `Keysight`
- `Amphenol RF`
- `Times Microwave Systems`
- `TE Connectivity`
- `Samtec`

## Lane outcome

- lane now appears `promotable to source_backed_fact_layer_partial`
- but only for a `coaxial-centered RF cable identity + impedance-boundary` layer
- the original draft's broader RF-cable taxonomy, performance, application, and supplier story remains blocked

## Practical disposition

Promote only the narrow unlock above.

Do not promote:

- draft-originated numerics
- broad type-taxonomy claims
- application mappings
- product-family comparisons
- HILPCB custom-cable claims
