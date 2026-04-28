# P4-15 Boundary-Scan / JTAG Blog Top-Tier Gap Plan

Date: 2026-04-27

## Purpose

Use the pilot draft `blogs/pilot/en/boundary-scan-jtag-high-speed-si.md` as a quality probe.

The draft is safe and publishable, but it is not yet a top-tier engineering article. This note converts the observed content defects into evidence-layer work so future prompt generation can produce a stronger article without inventing unsupported claims.

## Current Draft Verdict

- status: `safe_but_generic`
- publication risk: `low`
- top-tier readiness: `not_yet`
- reason:
  - The draft correctly avoids internal leakage, SI overclaims, coverage numerics, cost claims, and supplier-proof claims.
  - The draft does not yet provide enough concrete JTAG / DFT design-review depth.
  - The draft does not yet separate high-speed SI validation from JTAG access with enough practical engineering detail.
  - The draft has a method-comparison table, but it is still too generic to outperform specialist articles.
  - The conversion path exists, but the buyer action checklist is not yet sharp enough for an engineering review request.

## Defect-To-Data Map

| Draft defect | Evidence-layer gap | Needed support | Public-copy target after gap fill |
| --- | --- | --- | --- |
| JTAG section is directionally correct but generic | Need a JTAG / boundary-scan design-review checklist card | Device support, TAP pins, chain structure, reset behavior, BSDL / description-file needs, power-domain dependencies, programming/debug separation | A concrete pre-layout and pre-assembly JTAG review checklist |
| SI boundary is safe but thin | Need a high-speed SI separation card | Stackup, impedance, return path, via transitions, channel validation, timing/margin review, protocol/functional validation as separate layers | Clear explanation of what JTAG cannot prove and what remains in the SI validation plan |
| Test-method comparison is broad | Need a layered PCBA test-method selection card | Boundary-scan, ICT, flying probe, X-ray/AXI, FCT, programming/bring-up, file inputs, non-claims | Stronger method-selection matrix with engineering decision criteria |
| Quote handoff is present but not persuasive | Need a buyer action checklist tied to files and review outcomes | Gerber, drill, stackup, BOM, pick-and-place, schematic excerpts, test objectives, validation intent | More concrete CTA: submit files for DFT/test-access feasibility review |
| Article meets safety gates but not excellence gates | Need a topic-specific generation gate | Top-tier criteria and stop conditions for this topic | Prompt can reject safe-but-generic drafts and require richer engineering blocks |

## Subagent Work Split

Four independent `gpt-5.4` subagents were assigned:

- `JTAG / boundary-scan design-review specifics`
- `High-speed SI validation boundary`
- `PCBA test-method decision depth`
- `Boundary-scan blog top-tier rewrite gate`

Each agent owns a disjoint evidence area and must not edit the pilot blog directly.

## Non-Claims To Preserve

The stronger article must still not claim:

- exact fault coverage or coverage percentages
- cycle time, throughput, yield, cost savings, fixture payback, or lead-time numbers
- fixture elimination
- supplier approval, certification, qualification, compliance, or release authority
- high-speed performance proof from JTAG alone
- BER, eye-margin, jitter, insertion-loss, or protocol-conformance results without current verified evidence
- HILPCB-specific factory capability beyond public pages and dated support

## Completion Criteria

This P4-15 batch is complete when:

- new fact / gate cards cover the four gap areas above
- new `source_ids` resolve where source cards are added
- the update log records the defect-driven evidence fill
- the next rewrite plan can state exactly what to add to the pilot without adding unsupported numerics

## Rewrite Follow-Through

Status: `completed`

The pilot article was rewritten after the evidence gap fill:

- target file: `blogs/pilot/en/boundary-scan-jtag-high-speed-si.md`
- new posture: `engineering_review_checklist`
- added concrete JTAG review content:
  - `TDI / TDO / TCK / TMS`
  - optional `TRST/nTRST`
  - single-chain versus multi-chain intent
  - device order
  - connector access
  - BSDL or equivalent device-description files
  - mode-entry, reset, and power-state review
- added high-speed SI separation:
  - stackup and materials
  - controlled impedance
  - return-path continuity
  - via transitions and backdrill
  - channel measurement
  - timing / margin investigation
  - functional or protocol behavior
- upgraded method selection:
  - boundary-scan / JTAG
  - ICT
  - flying probe
  - X-ray / AXI
  - FCT
  - programming / bring-up
  - SI validation
- upgraded buyer action checklist:
  - fabrication files plus BOM, placement data, schematic excerpts, JTAG chain intent, BSDL / equivalent files, power-up constraints, test objectives, and production stage

Verification:

- public-blog internal leakage scan passed
- high-risk claim scan passed
- `BlogQuickQuoteInline` remains present
- FAQ markers remain present
- public-safe technical review line remains present
- `git diff --check` passed

The rewrite still does not unlock fault-coverage percentages, cycle time, cost, yield, fixture payback, supplier qualification, high-speed pass/fail, BER, eye-mask, jitter, insertion-loss, or protocol-conformance claims.
