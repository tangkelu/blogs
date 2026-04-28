---
fact_id: "methods-parameter-scope-test-inspection-optical-method-dimensions"
title: "Optical and X-ray inspection pages support named measurement dimensions, not universal accept/reject or coverage claims"
topic: "Test and inspection optical method dimensions"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "koh-young-spi-technology"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "koh-young-aoi-technology"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "ipc-a-610h-toc"
  - "ipc-j-std-001j-toc"
tags: ["spi", "aoi", "x-ray", "axi", "inspection", "bga", "qfn", "pcba-testing"]
---

# Canonical Summary

> The current source layer supports concrete method-language for `SPI`, `AOI`, and `X-ray`: SPI can be described with paste-deposit measurement dimensions such as volume, area, height, alignment, and print-defect patterns; AOI can be described with 2D/3D optical inspection scope plus visibility limits; X-ray can be described as the hidden-joint and internal-defect visibility layer for dense packages. None of these sources authorize universal defect-detection rates, inspection coverage percentages, or class-specific accept/reject thresholds.

## Stable Facts

- Koh Young frames SPI as a three-dimensional solder-paste measurement problem where volume matters for process control.
- The internal APT SPI page places SPI after printing and before component placement and ties it to layered downstream quality gates.
- Koh Young and the internal APT AOI page both support AOI as an optical / geometric inspection layer rather than an electrical proof layer.
- Koh Young and the internal APT AOI page both support the idea that visibility, shadowing, and hidden geometry limit simpler optical approaches.
- The internal X-ray page supports X-ray and CT language for hidden solder joints and internal defect visibility in dense-package assemblies such as BGA, QFN, and CSP.
- Public IPC TOC metadata supports naming `IPC-A-610H` and `J-STD-001J` as standards anchors for assembly acceptability and soldered-assembly scope, but not clause-level thresholds.

## Named Parameters And Method Dimensions

- `SPI`:
  `paste volume`, `paste area`, `paste height`, `alignment / offset`, `bridging`, `missing paste`, and `trend monitoring` are named in the internal APT SPI page, while Koh Young independently supports `3D` and `volume` framing.
- `AOI`:
  `2D AOI`, `3D AOI`, `bare-board AOI`, `SMT AOI`, `component placement`, `solder-joint formation`, `polarity`, and geometry-related defect language are named in the internal APT AOI page; Koh Young supports `components`, `solder joints`, `patterns`, `foreign material`, and optical `shadowing` / `hidden geometry` limits.
- `X-ray / CT`:
  `2D`, `2.5D`, and `3D CT` framing plus hidden-joint defect vocabulary such as `voids`, `bridges`, `cold joints`, `BGA`, `QFN`, and `CSP` are named in the internal APT X-ray page.
- `Standards anchors`:
  `IPC-A-610H` and `J-STD-001J` can be used as identity anchors for workmanship / soldered-assembly context only.

## Scope And Non-Generalization

- Use these dimensions to explain what the inspection method looks at, when it belongs in the process, and why one optical layer does not replace another.
- Treat `SPI volume / area / height` as measurement vocabulary, not as proof that a given print is automatically acceptable.
- Treat `AOI 3D` and `shadowing / hidden geometry` language as scope boundaries, not as proof of complete visibility under every package.
- Treat `X-ray / CT` as hidden-joint visibility language, not as permission to publish void thresholds, bridge thresholds, or mandatory sampling plans.
- Do not derive inspection coverage, defect-detection rate, first-pass yield, cycle time, or pass/fail percentages from these sources.
- Do not turn IPC TOC metadata into class-specific inspection or soldering acceptance criteria.

## Blog Usage

- `low-void BGA`:
  Safe support for wording such as `SPI tracks upstream paste-deposit dimensions` and `X-ray is the layer used to inspect hidden solder-joint conditions such as voiding or concealed bridges`. Not safe support for universal void thresholds or BGA pass/fail rules.
- `type-c charger`:
  Safe support for layered assembly-inspection wording around `SPI`, `AOI`, and selective `X-ray` for dense or hidden-joint areas. Not safe support for charger reliability, safety, or certification claims.
- `FAI`:
  Use only as a companion card when a draft needs to say that first-build inspection can include optical gates; this card does not make `FAI` itself the source of performance validation.

## Source Links

- https://kohyoung.com/en/solder-paste-inspection-technology/
- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- https://kohyoung.com/en/automated-optical-inspection-technology/
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
