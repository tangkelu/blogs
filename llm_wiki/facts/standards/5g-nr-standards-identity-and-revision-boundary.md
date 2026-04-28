---
fact_id: "standards-5g-nr-identity-and-revision-boundary"
title: "5G NR standards references must separate identity from revision-sensitive claims"
topic: "5G NR standards identity and revision boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "3gpp-38-series"
  - "3gpp-ts-38104-archive"
tags: ["3gpp", "5g", "nr", "nsa", "base-station", "standards", "revision-boundary"]
---

# Canonical Summary

> For 5G NR blog rewrites, the public 3GPP 38-series index is safe for standards-family identity and document discovery, while the TS 38.104 archive is safe for dated snapshot handling. Neither source should be rewritten into an undated `latest revision` claim or into clause-level technical assertions without a fresh source check.

## Stable Facts

- The public 38-series index identifies NR-related specification families and is the correct public starting point for standards naming in 5G content.
- The TS 38.104 archive provides dated revision packages for a base-station radio specification path and therefore shows that revision-sensitive 5G claims must be anchored to a checked snapshot.
- These sources are sufficient to support high-level wording that `NR` belongs to the 3GPP 38-series standards family and that base-station standards references are revision-sensitive.
- For overview writing, `NSA` can be treated as an architectural or deployment-mode term that still requires standards-specific checking before any detailed technical expansion.

## Conditions And Methods

- Use this card for `5g-nsa-5g-telecom` and as a guardrail whenever any approved slug mentions `3GPP`, `NR`, `NSA`, or base-station standards.
- Keep standards references at the identity level unless a dated archive file has been checked for the exact statement being made.
- Prefer wording such as `3GPP 38-series`, `NR standards family`, `revision-sensitive`, and `requires dated archive verification`.
- Pair this card with `facts/standards/3gpp-38-series-and-38104.md` when the rewrite needs a stronger reminder that archive paths, not vague memory, control revision naming.

## Limits And Non-Claims

- This card does not authorize any `latest revision` claim without a fresh archive check on the publication date.
- It does not authorize `FR1`, `FR2`, or band/range values unless the exact dated primary source snapshot is recorded.
- It does not authorize clause-level radio requirements, conformance criteria, emissions limits, OTA details, or deployment-mandate language.
- It does not prove `NSA` implementation details, operator rollout posture, interoperability status, or current market adoption.

## Open Questions

- Add more 38-series archive cards only if future rewrites need dated evidence for a specific NR subtopic beyond base-station identity handling.
- Add a separate public-source boundary for `NSA` versus `SA` only if overview pages begin drifting into network-architecture specifics.

## Source Links

- https://www.3gpp.org/dynareport?code=38-series
- https://www.3gpp.org/ftp/specs/archive/38_series/38.104/
