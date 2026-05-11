---
fact_id: "methods-renesas-1p50mm-bga-lga-mount-pad-dimensions-row"
title: "Renesas BGA/LGA mount-pad values are reusable only as the Renesas 1.50 mm pitch row"
topic: "Renesas 1.50 mm BGA/LGA mount-pad dimensions row"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_bga_lga_mount_pad_pitch_row"
canonical_unit_policy: "Preserve original Renesas row labels such as Lead pitch(mm) and φ(mm). Do not normalize this row into a universal 1.50 mm pitch conversion table."
source_ids:
  - "renesas-bga-lga-mount-pad-dimensions-common-pitches"
tags: ["renesas", "bga", "lga", "1.50-mm-pitch", "mount-pad", "exact-data", "second-owner"]
---

# Canonical Summary

> Renesas publishes a current-public one-page `BGA,LGA Mount Pad Dimensions` table that directly exposes a `1.50 mm` lead-pitch row with a corresponding `φ(mm) 0.55 to 0.65` mount-pad range. This is strong enough to raise the `PCB资料` `1.50 mm` package residual above `one NXP exact row + one Renesas named-package drawing`. This card is a Renesas document-scoped exact row only. It does not authorize a universal `1.50 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - the printed document class `BGA,LGA Mount Pad Dimensions`
  - the printed lead-pitch row `1.50`
  - the corresponding printed mount-pad range `φ(mm) 0.55 to 0.65`
  - the document note that the mount pad should match package land diameter in this Renesas context
- not exact for:
  - all Renesas BGA packages
  - all vendors at `1.50 mm`
  - generic handbook `MIN / MAX / recommended` closeout
  - package-library defaults outside this Renesas document context

## Admitted Data

- Renesas prints this document class:
  - `BGA,LGA Mount Pad Dimensions`
- Renesas prints this pitch row:
  - `Lead pitch(mm) 1.50`
- Renesas prints this corresponding range:
  - `φ(mm) 0.55 to 0.65`

## Conditions And Methods

- Treat this card as one Renesas owner-scoped exact row for common-pitch BGA/LGA mount pads.
- Keep the `1.50` row and the `φ(mm) 0.55 to 0.65` range attached to the Renesas document context.
- Use this card when a prompt needs one more current-public `1.50 mm` owner exact row and can stay inside Renesas document scope.
- Pair this card with:
  - [nxp-1p50mm-bga225-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-1p50mm-bga225-reflow-footprint.md)
  - [renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md](/code/blogs/llm_wiki/facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md)
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)

## Limits And Non-Claims

- This card does not authorize a universal `1.50 mm` BGA/LGA conversion table.
- It does not authorize package-family-specific geometry not printed in the Renesas row.
- It does not authorize cross-vendor defaulting or handbook table closeout.
- It does not close `connector-origin` or `installation-mark` residuals.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one current-public second-owner exact row for `1.50 mm`.
- It narrows the residual state from `one NXP exact row + one Renesas named-package drawing` to `one NXP exact row + one Renesas named-package drawing + one Renesas exact row`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Source Links

- https://www.renesas.com/en/document/cpt/mount-pad-bga-lga-fig0013e
