---
source_id: "usb-if-type-c-functional-test-spec-2024-03-03"
title: "USB Type-C Functional Test Specification 2024-03-03"
organization: "USB Implementers Forum"
source_type: "test_specification"
url: "https://www.usb.org/sites/default/files/USB%20Type%20C%20Functional%20Test%20Specification%202024%2003%2003.pdf"
jurisdiction: "global"
published_at: "2024-03-03"
checked_at: "2026-04-27"
trust_tier: "t1"
stability: "versioned_pdf"
must_refresh: true
topic_tags: ["usb-if", "usb-type-c", "functional-test", "vif", "compliance", "connector"]
status: "active"
notes: "Official USB-IF functional-test PDF. Use for test-flow and VIF vocabulary only unless exact test requirements are separately extracted."
---

# Source Summary

## What It Covers

- USB Type-C functional test context
- Product implementation data such as `VIF` fields used by test software
- State, attachment, VCONN, and USB PD implementation context for functional testing

## Why It Matters

- Supports conservative public wording that Type-C charger boards may require product-specific powered bring-up and functional-test inputs rather than a generic one-size-fits-all FCT script.

## Extraction Notes

- Safe for vocabulary such as `Product Under Test`, `VIF`, `state machine`, `functional test`, and implementation-specific applicability.
- Do not extract test limits, timing values, voltage/current values, or pass/fail rules into general blog claims without a separate parameter governance pass.

## Refresh Notes

- Refresh before publication if a draft cites current Type-C functional-test requirements, exact timers, exact electrical limits, or compliance behavior.
