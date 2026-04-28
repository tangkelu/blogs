---
source_id: "xjtag-jtag-chains"
title: "JTAG Chains"
organization: "XJTAG"
source_type: "technical_guide"
url: "https://docs.xjtag.com/xjtag/current/concepts/chain.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-27"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["jtag", "boundary-scan", "chain", "tdi", "tdo", "tck", "tms", "trst", "dft"]
status: "active"
notes: "Vendor documentation. Use for conservative chain-topology and signal-connectivity framing only."
---

# Source Summary

## What It Covers

- JTAG chain topology at board level
- TDI to TDO serial path through multiple devices
- Shared TCK/TMS and optional nTRST connectivity
- Possibility of multiple separate JTAG chains on one PCB

## Why It Matters

- It is a practical public source for turning generic `JTAG` copy into concrete review items about chain order, shared control signals, and whether a board has one chain or multiple chains.

## Extraction Notes

- Safe for statements that a JTAG chain uses TDI/TDO as the serial path and shares TCK/TMS plus optional nTRST across devices.
- Safe for the idea that some boards expose multiple separate chains.
- Do not convert this page into claims about guaranteed chain performance, fixture design, production coverage, or universal connector conventions.

## Refresh Notes

- Refresh if XJTAG changes documentation URLs or terminology around chain setup.
