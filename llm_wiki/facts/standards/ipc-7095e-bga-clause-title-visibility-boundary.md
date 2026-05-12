---
fact_id: "standards-ipc-7095e-bga-clause-title-visibility-boundary"
title: "Public IPC-7095E surface shows SMD/NSMD definitions plus BGA clause and figure-title visibility, not reusable geometry criteria"
topic: "IPC-7095E BGA visible definitions and clause-title visibility boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "ipc-7095e-toc"
tags: ["ipc", "ipc-7095e", "bga", "land-pattern", "toc", "topic-visibility", "boundary"]
---

# Canonical Summary

> The public `IPC-7095E` surface is strong enough to show that BGA implementation guidance includes visible SMD / NSMD BGA-land definitions, explicit clause-level topics for attachment sites, land diameter, land-definition styles, via size/location, and solder-mask effects, and visible figure-title labels for BGA solder-land and land-pattern examples. This strengthens standards-side visibility for the `1.50 mm` package lane. It does not expose reusable geometry values or criteria.

## Stable Facts

- Public IPC TOC access exists for `IPC-7095E`.
- The public surface visibly exposes body-level terminology definitions for:
  - `Solder-Mask-Defined (SMD) BGA Land`
  - `Non-Solder-Mask Defined (NSMD) BGA Land`
- The public surface visibly exposes BGA implementation clause titles including:
  - `Solder-Mask-Defined (SMD) BGA Land`
  - `Non-Solder-Mask Defined (NSMD) BGA Land`
  - `Land Patterns and Printed Board Considerations`
  - `BGA Package Pitch`
  - `Land Pattern Design`
  - `Ball Size Relationships`
- The public surface also visibly exposes attachment-site clause titles including:
  - `Land Diameter Size and Its Impact on Routing`
  - `Solder-Mask-Defined (SMD) Land and Metal-Defined Land Designs`
  - `Metal-Defined Lands`
  - `Solder-Mask-Defined (SMD) Lands`
  - `Via Size and Location`
  - `Parameters Affecting Solder Mask on BGAs`
- The public surface also visibly exposes figure-title labels including:
  - `Figure 6-2 Solder Lands for BGA Components`
  - `Figure 6-3 Metal-Defined Land Attachment Profile`
  - `Figure 6-5 Solder Joint Geometry Contrast`
  - `Figure 6-10 Balls Anywhere Land Pattern Design for a Balls Anywhere BGA Component`
- The public surface therefore gives the repo one stronger standards-side clause-and-figure-discovery anchor than plain standards identity alone.

## Conditions And Methods

- Use this card when a prompt needs to explain that public IPC material visibly treats BGA land-pattern design, SMD/NSMD terminology, land diameter, via placement, and solder-mask effects as named standards topics.
- Pair this card with:
  - [j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md)
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)
  - [ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md)
- Keep the safe reusable rule at:
  - public surface = visible terminology definitions plus clause/figure-title visibility
  - public surface may expose `Land Pattern Design` / `Ball Size Relationships`
  - public surface != geometry criteria
  - public surface != exact replacement row

## Limits And Non-Claims

- This card does not provide `1.50 mm` land-pattern geometry.
- It does not provide pad-diameter values or solder-mask openings.
- It does not convert visible definition text or figure titles into a formal public standards row.
- It does not reopen the `1.50 mm` residual by itself.

## Relationship To Local PCB资料 Intake

- This card adds one more public standards-side visibility anchor above pure standards identity and above `J-STD-013` TOC-only topic visibility.
- It helps explain that public IPC material visibly defines SMD / NSMD BGA lands and names BGA land-pattern, routing, via, and solder-mask topics, while clause-level geometry remains non-public.

## Source Links

- https://www.ipc.org/TOC/IPC-7095E_toc.pdf
