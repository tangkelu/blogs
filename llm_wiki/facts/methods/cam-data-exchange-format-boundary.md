---
fact_id: "methods-cam-data-exchange-format-boundary"
title: "CAM and fabrication-data articles can cite official Gerber, IPC-DPMX, and ODB++ identities, but not format-superiority or supplier-capability claims"
topic: "CAM data exchange format boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "ucamco-gerber-format-page"
  - "ucamco-gerber-downloads-page"
  - "ipc-dpmx-ipc-2581-consortium-home-page"
  - "ipc-dpmx-ipc-2581-consortium-about-page"
  - "siemens-odb-plus-plus-page"
  - "siemens-odb-plus-plus-resources-faq"
tags: ["cam", "gerber", "ipc-dpmx", "ipc-2581", "odb++", "fabrication-data", "assembly-data", "file-package"]
---

# Canonical Summary

> Official Ucamco, IPC-DPMX, and Siemens ODB++ sources support format identity and manufacturing-data-exchange vocabulary for Gerber, IPC-DPMX / IPC-2581, and ODB++. They do not prove that a given file package is complete, that a fabricator supports every format feature, that CAM corrections will catch design errors, or that any format choice improves yield, cost, lead time, or quality.

## Stable Facts

- Ucamco is the official Gerber format owner and describes Gerber as a PCB design-data-transfer format used for fabrication data.
- Ucamco's Gerber overview supports layer-file vocabulary such as copper, solder mask, legend, drill, and route data.
- Ucamco's Gerber overview supports attribute vocabulary for metadata such as pad / via / fiducial identity and net-name information.
- Ucamco's Gerber overview supports Gerber Job File vocabulary for machine-readable fabrication characteristics such as thickness or finish.
- Ucamco's downloads page is the official route for Gerber specifications, schema, examples, and test files; it must be refreshed before citing the latest revision.
- The IPC-DPMX / IPC-2581 Consortium page supports IPC-DPMX / IPC-2581 identity as a standard for PCB and assembly manufacturing description data and transfer methodology.
- The IPC-DPMX about page supports consortium / supply-chain category vocabulary across OEM, EDA / DFM / CAM, fabricator, assembler, and test-company participants.
- Siemens describes ODB++ as a structured data-exchange format family for design, process, and manufacturing information flows across the PCB design-through-manufacturing chain.
- Siemens states that the ODB++ specification is available for download to registered users and that the format supports controlled content segmentation in a handoff package.

## Conditions And Methods

- Use this card for `cam-files.md`, `buying-pcb.md`, PCB file-package checklists, and CAD-to-CAM data-exchange explanations.
- Keep Gerber, Gerber Job, IPC-DPMX / IPC-2581, and ODB++ as data-exchange formats, not as substitutes for engineering review.
- Pair this card with `methods-pcba-test-method-input-package-boundary` when a prompt moves from bare-board fabrication data into BOM, pick-and-place, schematic, programming, or functional-test requirements.
- Use `ucamco-gerber-downloads-page` only as a specification index unless a future extraction pass records a specific PDF revision.
- Use IPC-DPMX / IPC-2581 sources for standards-family identity and data-exchange scope, not for adoption or implementation proof.
- Use Siemens ODB++ sources for owner-scoped format identity, specification-availability, and guarded handoff-structure language, not for manufacturer-acceptance or process-benefit proof.

## Limits And Non-Claims

- This card does not define a universal minimum manufacturing file package.
- It does not claim Gerber, IPC-DPMX / IPC-2581, ODB++, drill files, netlists, BOMs, or pick-and-place files are interchangeable.
- It does not prove that an APT / HIL / customer / fabricator workflow accepts or prefers any specific data format.
- It does not support universal CAM correction, DFM success, yield improvement, cost reduction, faster quote, or fewer-revision claims.
- It does not support current tool-support rankings or format-superiority comparisons.

## Open Questions

- Add a dated internal file-intake capability record before writing supplier-specific ODB++, IPC-DPMX / IPC-2581, or Gerber acceptance and CAM-review depth.

## Source Links

- https://www.ucamco.com/en/gerber
- https://www.ucamco.com/en/gerber/downloads
- https://www.ipc2581.com/
- https://www.ipc2581.com/about/
- https://www.siemens.com/en-us/products/pcb/odb-plus-plus/
- https://www.siemens.com/en-us/products/pcb/odb-plus-plus/resources/
