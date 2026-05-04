---
wiki_id: "wiki-processes-rf-cable-and-coaxial-identity-boundaries"
title: "RF cable and coaxial identity boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-rf-cable-coaxial-identity-and-impedance-boundary"
  - "methods-pcb-impedance-and-rf-measurement-method-boundary"
  - "methods-pcba-cable-harness-and-ic-programming-integration"
source_ids:
  - "amphenol-rf-coaxial-cable-guide"
  - "times-microwave-semi-rigid-coaxial-cables-page"
  - "te-connectivity-bnc-connectors-page"
  - "keysight-vna-system-impedance-help"
  - "keysight-e5055a-measurement-parameters-help"
  - "frontendapt-pcba-cable-assembly-page-en"
tags: ["rf-cable", "coaxial", "semi-rigid", "micro-coax", "50-ohm", "75-ohm", "identity-boundary"]
---

# Use This Page For

- Routing `RF cable` drafts into a safe coaxial-centered identity page.
- Separating coaxial family identity, impedance vocabulary, RF measurement vocabulary, and adjacent integration context from unsupported product-guide or supplier-guide claims.
- Preventing RF-cable drafts from turning into full taxonomy, performance, or sourcing articles.

# Core Boundary Rule

- Start with coaxial identity, not with cable recommendations.
- The current local corpus supports a conservative RF-cable lane only at coaxial-centered identity level.
- Safe local support covers:
  coaxial cable structure vocabulary, semi-rigid and micro-coax as coaxial-family variants, `50 ohm` and `75 ohm` impedance ecosystems, and measurement-boundary vocabulary.
- It does not support a complete RF-cable market or selection guide.

# Coaxial Identity Routing

## Coaxial Cable Structure

- Route `RF cable` language first through coaxial structure vocabulary:
  center conductor, dielectric, metallic shield, and outer insulating layer.
- This is the stable identity layer for the current lane.
- Do not let a coaxial-centered source set expand into a universal `all RF cables` taxonomy by default.

## Semi-Rigid And Micro-Coax

- Semi-rigid and micro-coax are safe to name as coaxial-family variants.
- Keep them as examples inside the coaxial family, not as proof that the lane now safely covers every adjacent interconnect family.
- Do not use these two variants to imply support for `twinax`, `triax`, or broader cable-system taxonomy.

# Impedance And Measurement Boundary

## 50 Ohm And 75 Ohm Context

- Safe local support exists for official `50 ohm` and `75 ohm` coaxial ecosystems.
- Write this as impedance-context vocabulary, not as a universal application-fit rule.
- Connector impedance, cable impedance, and measurement-reference impedance should stay distinct in copy.

## Measurement Vocabulary

- Route return loss, SWR, impedance, TDR, and VNA-style language through measurement-boundary framing.
- Safe wording:
  impedance matters in RF interconnect paths, and measurement vocabulary exists to characterize reflection and mismatch behavior.
- Unsafe wording:
  using measurement vocabulary as proof of finished cable performance, supplier capability, or system-level fit.

# Adjacent Integration Boundary

- Internal cable-assembly pages remain useful only as adjacent integration context.
- They support the idea that PCBA work can extend into cable, harness, and system-integration steps.
- They do not prove RF cable performance, custom-cable selection quality, or commercial sourcing posture.

| Draft signal | Safe route | Block if draft asks for |
| --- | --- | --- |
| `what is RF cable` | coaxial-centered identity and impedance context | full RF-cable taxonomy |
| `semi-rigid coax` | coaxial-family variant identity | broad product-selection guide |
| `50 ohm vs 75 ohm cable` | impedance-context boundary | universal application-fit rules |
| `RF cable assembly` | adjacent integration context | supplier capability, quality, or lead-time proof |
| `best RF cable` | stop at identity boundary | performance ranking or supplier-selection article |

# Stable Facts

- Coaxial cable identity is locally source-backed at conservative structure level.
- Semi-rigid and micro-coax are locally supportable as coaxial-family variants.
- Official source owners support both `50 ohm` and `75 ohm` coaxial connector ecosystems.
- Measurement-owner sources support RF reflection vocabulary such as return loss, SWR, and impedance at measurement-boundary level only.
- Internal cable-assembly context is usable only as adjacent integration framing.

# Engineering Boundaries

- Keep the page centered on coaxial identity and impedance context unless a future lane adds stronger owner-backed cable-family coverage.
- Keep connector impedance, cable impedance, and RF measurement vocabulary separate from performance guidance.
- Treat cable fabrication, harness integration, and IC-programming adjacency as broader system-integration context, not RF-cable authority.
- Require narrower owner datasheets or dated capability records before publishing attenuation, shielding, environment, or supplier-selection language.

# Blocked Claims

- full RF-cable taxonomy
- performance guide claims
- supplier-selection claims
- cost, lead-time, and yield claims

# Common Misreadings

- `RF cable` in this lane does not mean the whole RF interconnect market is now covered.
- Semi-rigid and micro-coax identity does not prove `twinax` or `triax` coverage.
- `50 ohm` and `75 ohm` ecosystem identity does not prove universal usage rules.
- Measurement vocabulary does not prove finished-cable performance.
- Internal cable-assembly context does not prove RF cable sourcing or custom-build authority.

# Must Refresh Before Publishing

- Any claim framed as current, latest, or standard choice
- Any connector-family listing, ecosystem comparison, or market recommendation
- Any attenuation, VSWR, return-loss, shielding, durability, or environment claim
- Any supplier-capability, lead-time, pricing, commercial-selection, or integration-quality statement

# Related Fact Cards

- `methods-rf-cable-coaxial-identity-and-impedance-boundary`
- `methods-pcb-impedance-and-rf-measurement-method-boundary`
- `methods-pcba-cable-harness-and-ic-programming-integration`

# Local Source Scope

- `amphenol-rf-coaxial-cable-guide`
- `times-microwave-semi-rigid-coaxial-cables-page`
- `te-connectivity-bnc-connectors-page`
- `keysight-vna-system-impedance-help`
- `keysight-e5055a-measurement-parameters-help`
- `frontendapt-pcba-cable-assembly-page-en`
