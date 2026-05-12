---
fact_id: "standards-jeita-public-bga-fbga-flga-geometry-surfaces-below-1p50mm-boundary"
title: "Public JEITA geometry-bearing BGA and fine-pitch socket-mounting surfaces are broader than a single guide, but still stop below reusable 1.50 mm BGA geometry"
topic: "JEITA public BGA/FBGA/FLGA geometry surfaces below 1.50 mm boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "jeita-edr-7315b-bga-design-guide"
  - "jeita-ed-7306-bga-fbga-flga-warpage-standard"
  - "jeita-edr-7712-fbga-socket-mounting-pattern-guide"
  - "jeita-edr-7713-flga-socket-mounting-pattern-guide"
tags: ["jeita", "bga", "fbga", "flga", "socket-mounting-pattern", "public-geometry", "1.27-mm", "0.80-mm", "1.50-mm", "boundary"]
---

# Canonical Summary

> Public JEITA standards-side coverage is broader than one `EDR-7315B` BGA guide alone. The public JEITA stack now includes one BGA design guide with visible geometry-bearing content, one BGA/FBGA/FLGA warpage standard with visible BGA/FBGA pitch columns through `1.27 mm`, and two public FBGA/FLGA socket-mounting-pattern guides with visible printed-circuit-board rows at `0.80`, `0.65`, `0.50`, and `0.40`. This materially strengthens the repo's public JEITA geometry/process surface stack. It still does not expose one reusable public `1.50 mm` BGA land-pattern or geometry row, so it does not reopen the current `1.50 mm` residual.

## Stable Facts

- Public JEITA access is not limited to metadata or one BGA guide identity only.
- `JEITA EDR-7315B` publicly exposes geometry-bearing BGA guide content with visible coverage at `1.27 mm` and `1.00 mm`.
- `JEITA ED-7306` publicly exposes `Table 1 Maximum permissible package warpages for BGA and FBGA` with visible pitch columns `0.4`, `0.5`, `0.65`, `0.8`, `1.0`, and `1.27`.
- `JEITA EDR-7712` publicly exposes recommended socket mounting pattern content for printed circuit board design with visible terminal-distance rows `0.80`, `0.65`, `0.50`, and `0.40`.
- `JEITA EDR-7713` publicly exposes recommended socket mounting pattern content for printed circuit board design with visible `e` / through-hole rows `0.80`, `0.65`, `0.50`, and `0.40`.
- None of these surfaced public JEITA documents expose one reusable public `1.50 mm` BGA land-pattern or geometry row.

## Conditions And Methods

- Use this card when a prompt needs a stronger public JEITA standards-side anchor than one single BGA guide, TOC-only visibility, or standards discoverability alone.
- Pair it with:
  - [jeita-edr-7315b-bga-public-geometry-below-1p50mm-boundary.md](/code/blogs/llm_wiki/facts/standards/jeita-edr-7315b-bga-public-geometry-below-1p50mm-boundary.md)
  - [ipc-7095e-bga-clause-title-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/ipc-7095e-bga-clause-title-visibility-boundary.md)
  - [ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md)
- Keep the safe reusable rule at:
  - public JEITA has multiple real geometry/process-bearing package and PCB surfaces
  - visible public JEITA payload still stops below reusable `1.50 mm` BGA geometry
  - broader public JEITA access != `1.50 mm` reopen

## Limits And Non-Claims

- This card does not provide one public `1.50 mm` JEITA BGA geometry row.
- It does not provide one public `1.50 mm` JEITA land-pattern rule.
- It does not authorize pad diameters, solder-mask openings, or BGA package-variation rules for `1.50 mm`.
- It does not convert fine-pitch FBGA/FLGA socket guidance into cross-family BGA closure.
- It does not close the `1.50 mm` package residual.

## Relationship To Local PCB资料 Intake

- This card raises the standards-side public JEITA stack above `EDR-7315B alone` by adding one BGA/FBGA warpage table surface and two fine-pitch printed-circuit-board socket-mounting surfaces.
- It also tightens the continuation rule by showing that even broader public JEITA geometry/process access can still remain below the reopen gate when visible rows stop at `1.27 mm` or `0.80 mm`.

## Source Links

- https://home.jeita.or.jp/tsc/std-pdf/EDR-7315B.pdf
- https://home.jeita.or.jp/tsc/std-pdf/ED-7306_E.pdf
- https://home.jeita.or.jp/tsc/std-pdf/EDR-7712.pdf
- https://home.jeita.or.jp/tsc/std-pdf/EDR-7713.pdf
