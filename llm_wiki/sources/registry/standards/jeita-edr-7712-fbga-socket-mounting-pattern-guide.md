---
source_id: "jeita-edr-7712-fbga-socket-mounting-pattern-guide"
title: "JEITA EDR-7712 FBGA socket mounting pattern guide"
organization: "JEITA"
source_type: "standard"
url: "https://home.jeita.or.jp/tsc/std-pdf/EDR-7712.pdf"
jurisdiction: "japan"
published_at: ""
checked_at: "2026-05-12"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["jeita", "edr-7712", "fbga", "socket", "mounting-pattern", "printed-circuit-board", "0.80-mm", "0.65-mm", "0.50-mm", "0.40-mm"]
status: "active"
notes: "Official JEITA public PDF. Safe for the bounded fact that this report publicly includes `Recommended Socket Mounting Pattern on Printed Circuit Board` for FBGA-class sockets and visibly lists terminal-distance rows `e = 0.80`, `0.65`, `0.50`, and `0.40`. Do not infer one public `1.50 mm` BGA geometry row or a universal PCB land-pattern rule from this source."
---

# Source Summary

## What It Covers

- official JEITA public FBGA socket guide
- recommended socket mounting pattern on printed circuit board
- visible terminal-distance rows for fine-pitch classes `0.80`, `0.65`, `0.50`, and `0.40`

## Why It Matters

- Adds one more real public JEITA PCB-geometry surface instead of pure document discoverability
- Sharpens the repo's standards-side boundary because the public PCB mounting-pattern content is real but still confined to fine-pitch FBGA classes below `1.50 mm`

## Extraction Notes

- Safe for guarded wording that `JEITA EDR-7712` publicly includes recommended socket mounting pattern content for printed circuit board design
- Safe for guarded wording that the visible terminal-distance rows stop at `0.80`, `0.65`, `0.50`, and `0.40`
- Do not rewrite this FBGA socket guide into one public `1.50 mm` BGA land-pattern rule
- Do not universalize socket-mounting guidance into cross-family PCB footprint doctrine

## Refresh Notes

- Refresh before publication because public standards-owner PDF locations can move
- Preserve the `public fine-pitch FBGA socket-mounting surface below 1.50 mm` framing whenever reusing this source
