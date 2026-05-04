---
source_id: "ucamco-gerber-format-page"
title: "Official Gerber Format Website"
organization: "Ucamco"
source_type: "format_owner_page"
url: "https://www.ucamco.com/en/gerber"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-03"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["ucamco", "gerber", "pcb-data-transfer", "cad-cam", "fabrication-data"]
status: "active"
notes: "Official Ucamco Gerber overview page. Use for format identity, layer / attribute / job-file vocabulary, and CAD-to-CAM transfer framing; refresh before citing latest revision or current ecosystem support."
---

# Source Summary

## What It Covers

- Gerber as a PCB design-data-transfer format maintained by Ucamco
- Gerber layer-file scope for copper, solder mask, legend, drill, and route data
- Attribute metadata such as SMD pad, via pad, fiducial, and net-name information
- Gerber Job File scope for machine-readable fabrication characteristics such as thickness or finish

## Why It Matters

- Gives `cam-files.md`, `buying-pcb.md`, and adjacent file-package articles a primary format-owner anchor instead of relying on draft-originated CAM explanations.
- Supports guarded language that Gerber data belongs to the fabrication-data package while keeping PCBA test, BOM, pick-and-place, stackup, and engineering-review needs separate.

## Extraction Notes

- Safe for format identity, high-level data categories, and layer / attribute / job-file vocabulary.
- Do not extract exact syntax, implementation rules, acceptance criteria, or CAM-engineering correction workflow from this overview page.
- Do not use this page to claim that every design tool, CAM tool, or fabricator currently supports every Gerber revision or feature.

## Refresh Notes

- Refresh before citing the latest Gerber revision, current tool support, current viewer availability, or any Ucamco news item.
