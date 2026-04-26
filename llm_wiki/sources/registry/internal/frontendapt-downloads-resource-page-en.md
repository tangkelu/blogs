---
source_id: "frontendapt-downloads-resource-page-en"
title: "APTPCB English Downloads Registry JSON"
organization: "APTPCB"
source_type: "internal_resource_page"
url: "/code/hileap/frontendAPT/public/static/resources/en/downloads.json"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-04-24"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "aptpcb", "downloads", "resource-registry", "library", "files"]
status: "active"
notes: "Internal APT downloads registry JSON used to hold the current downloadable-file list and update metadata for the resources section."
---

# Source Summary

## What It Covers

- Download registry structure
- update timestamp field and file-list container

## Why It Matters

- Useful internal support for how the downloads library is populated even when the current registry content is sparse.

## Extraction Notes

- Treat this as a structural registry source, not a fact source
- Prefer the surfaced resource pages or underlying files for substantive claims

## Refresh Notes

- Re-check when the downloads registry begins carrying populated entries
