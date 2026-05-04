---
source_id: "ansys-coplanar-waveguide-driven-terminal"
title: "Co-Planar Waveguide (Driven Terminal)"
organization: "Ansys"
source_type: "software_official_docs"
url: "https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/HFSS/Content/GettingStarted/CoPlanarWaveguideDrivenTerminal.htm"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-30"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["ansys", "cpw", "coplanar-waveguide", "rf", "transmission-line", "structure"]
status: "active"
notes: "Official Ansys HFSS help page. Use for guarded CPW structure identity and conductor-role vocabulary, not for board-level performance, probing, or supplier-capability claims."
---

# Source Summary

## What It Covers

- `CPW` as a transmission-line structure in HFSS help
- center signal trace with two coplanar side-ground conductors
- geometry-sensitive context where signal width and gap affect characteristic impedance

## Why It Matters

- Provides a current official/public source for conservative `CPW` topology wording in board-context transmission-line discussions.

## Extraction Notes

- Safe for guarded `CPW` structure identity such as `signal trace between two coplanar side grounds`.
- Safe for high-level wording that the geometry participates in impedance setting.
- Do not turn this modeling page into generic RF performance claims, mmWave-superiority claims, probing claims, or supplier-capability proof.

## Refresh Notes

- Refresh before publication if a draft cites current screenshots, solver workflow, field plots, or live help-page details as if they were evergreen design rules.
