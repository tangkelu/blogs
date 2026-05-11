---
fact_id: "methods-renesas-1p50mm-bga-package-drawing-prbg0225cb-a"
title: "Renesas PRBG0225CB-A proves a second current-public owner publishes a named 1.50 mm BGA package drawing"
topic: "Renesas 1.50 mm BGA package drawing for the named PRBG0225CB-A package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_outline_document"
canonical_unit_policy: "Preserve the original Renesas package identity and pitch wording such as 225-pin Plastic BGA, PRBG0225CB-A, e = 1.50, and b = 0.75. Do not invent or normalize recommended land-pattern geometry that was not directly landed."
source_ids:
  - "renesas-prbg0225cb-a-1p50mm-bga-package-drawing"
tags: ["renesas", "bga225", "prbg0225cb-a", "1.50-mm-pitch", "package-drawing", "second-owner", "source-coverage"]
---

# Canonical Summary

> Renesas publishes a current-public named-package drawing for `PRBG0225CB-A` that directly exposes `225-pin Plastic BGA` identity plus a printed `e = 1.50` pitch statement. This is strong enough to prove that the `PCB资料` `1.50 mm` residual is no longer limited to one NXP owner-scoped exact row. This card is a source-coverage and named-package identity landing only. It does not admit recommended land-pattern geometry from the Renesas drawing.

## Exact Data Scope

- exact for:
  - the printed package class `225-pin Plastic BGA`
  - the named package identity `PRBG0225CB-A`
  - the printed pitch statement `e = 1.50`
  - the printed ball-size statement `b = 0.75`
- not exact for:
  - recommended PCB-land geometry not directly landed
  - all `1.50 mm` BGA packages
  - cross-vendor `1.50 mm pitch -> land pattern` rules
  - universal package-library defaults

## Admitted Data

- Renesas prints this package class:
  - `225-pin Plastic BGA`
- Renesas prints this named package identity:
  - `PRBG0225CB-A`
- Renesas prints this pitch statement:
  - `e = 1.50`
- Renesas prints this ball-size statement:
  - `b = 0.75`

## Conditions And Methods

- Treat this card as proof that a second current-public owner route exists for a named `1.50 mm` BGA package.
- Keep the `1.50 mm` pitch statement attached to the Renesas `PRBG0225CB-A` package identity and drawing context.
- Use this card when a prompt needs to explain that `1.50 mm` package coverage is no longer a single-owner surface.
- If a later prompt needs actual land-pattern geometry from Renesas, reopen for a direct owner land-pattern document rather than extrapolating from this drawing.
- Pair this card with:
  - [nxp-1p50mm-bga225-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-1p50mm-bga225-reflow-footprint.md)
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)

## Limits And Non-Claims

- This card does not authorize Renesas recommended land-pattern geometry.
- It does not authorize a universal `1.50 mm` BGA conversion table.
- It does not authorize package-library defaults outside the named `PRBG0225CB-A` drawing.
- It does not close connector-origin or installation-mark residuals.

## Relationship To Local PCB资料 Intake

- This card gives the package lane its first directly verified current-public second-owner `1.50 mm` named-package drawing.
- It narrows the residual state from `one NXP exact row only` to `one NXP exact row plus one Renesas named-package drawing`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Source Links

- https://www.renesas.com/us/en/document/psp/package-drawing-225-pin-plastic-bga-prbg0225cb-a
