# P4-315 Package Residual Authority Recovery

Date: 2026-05-08
Parent inputs:
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `/code/blogs/llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md`
- `/code/blogs/llm_wiki/logs/p4-304-2026-5-8-pcb-ziliao-package-pin1-origin-authority-gap-tightening.md`
- `/code/blogs/llm_wiki/logs/p4-306-2026-5-8-package-pin1-origin-kicad-official-doc-tightening.md`
- `/code/blogs/llm_wiki/logs/p4-307-2026-5-8-package-bga-official-replacement-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-308-2026-5-8-intel-bga-land-pad-guideline-landing.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/docs/superpowers/plans/2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan.md`
- `/root/.codex/skills/llm-wiki-workflow/SKILL.md`
Execution mode: `controller_owned_source_scouting_only`

## Purpose

Scout the remaining public authority surface for the open `package` residuals named in `P4-309`:

- `0.75 mm` pitch replacement
- `1.50 mm` pitch replacement
- connector-origin defaulting
- installation-mark conventions

This lane does not create facts, wiki pages, or source records.
It only names candidate official source classes, their exact safe scope, what is still unresolved, and the safest next landing route.

## Current Boundary Carried Forward

From `P4-304`, `P4-306`, `P4-307`, and `P4-308`, the safe starting position remains:

- exact BGA replacements already exist for `1.27 mm`, `1.00 mm`, `0.80 mm`, `0.50 mm`, and one `0.4 mm VBGA/WLCSP` route
- `0.75 mm` and `1.50 mm` remain open residual pitch classes
- KiCad strengthens `pin-1 / origin` only as CAD-owner library convention
- connector-origin defaulting and standards-grade installation-mark authority remain unresolved

## Source Candidate Classes

### 1. `0p75_mm_pitch_replacement`

#### Candidate class A: package-owner package drawings with embedded recommended land pattern

Public examples found:

- Microchip `196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]` package drawing  
  `https://ww1.microchip.com/downloads/en/DeviceDoc/196B_TFBGA_11x11_%5BBAB%5D_C04-21141a.pdf`
- Microchip `176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]` package drawing  
  `https://ww1.microchip.com/downloads/en/DeviceDoc/176B_TFBGA_11x11x1_19mm_4LX_C04-00481a.pdf`
- Microchip `169-Ball Thin Fine Pitch Ball Grid Array (7G)` package drawing  
  `https://ww1.microchip.com/downloads/en/DeviceDoc/169L_TFBGA_10x10_7G_C04-377C-J.pdf`

Exact safe scope:

- owner-scoped `0.75 BSC` package drawings
- exact land-pattern geometry only for the named package drawing
- safe for package-specific replacement rows

Not safe to claim:

- a universal `0.75 mm pitch -> one pad diameter` rule
- cross-vendor equivalence
- any rewrite that drops package code, owner, or drawing context

#### Candidate class B: package-owner package-identity pages that confirm public `0.75 mm` package families

Public examples found:

- NXP `SOT1908-1: FBGA448`  
  `https://www.nxp.com/docs/en/package-information/SOT1908-1.pdf`
- NXP `SOT2031-1: FBGA576`  
  `https://www.nxp.com/docs/en/package-information/SOT2031-1.pdf`
- NXP `SOT1899-1: BGA1313`  
  `https://www.nxp.com/docs/en/package-information/SOT1899-1.pdf`
- Microchip `SAMA5D2` package table showing `TFBGA196` at `0.75 mm` pitch  
  `https://onlinedocs.microchip.com/oxy/GUID-5474CCCD-F385-4AD7-9759-539BB1019357-en-US-10/GUID-67BD5FAB-2B03-4C10-B316-C92ABAFB50F1.html`

Exact safe scope:

- public proof that named owners still publish `0.75 mm` BGA/TFBGA package families
- package identity, ball count, body size, and pitch confirmation
- discovery support for later package-owner row replacement

Not safe to claim:

- PCB land-pattern geometry from these pages alone
- a complete replacement for the blocked handbook table

### 2. `1p50_mm_pitch_replacement`

#### Candidate class A: standards-adjacent public abstract pages for coarse-pitch ball and column package design guides

Public examples found:

- IEC `60191-6-2:2001` abstract pages naming `1.50 mm`, `1.27 mm`, and `1.00 mm` pitch ball and column terminal packages  
  `https://www.intertekinform.com/en-us/standards/iec-60191-6-2-2001-563493_saig_iec_iec_1285248/`
  `https://standards.iteh.ai/catalog/standards/iec/1cf9243a-2f13-4dd2-964d-645552867f3b/iec-60191-6-2-2001`

Exact safe scope:

- standards-adjacent confirmation that `1.50 mm` coarse-pitch ball / column package classes exist as a formal design-guide family
- terminology, pitch-family existence, and drawing-governance discovery

Not safe to claim:

- exact numeric land-pattern rows from the abstract page
- free/public full-table access
- direct replacement closure for the handbook row

#### Candidate class B: standards-owner discovery portals

Public examples found:

- JEDEC public search portal / registered-outline surface  
  `https://www.jedec.org/`

Exact safe scope:

- discovery surface for registered package outlines and possible BGA family documents
- route planning only

Not safe to claim:

- that a usable `1.50 mm` public row is already in hand
- that JEDEC search alone closes the residual

#### Candidate class C: package-owner coarse-pitch package search surfaces

Public examples found:

- NXP package search / package catalog surface  
  `https://www.nxp.com/packages/search?q=&type=0`

Exact safe scope:

- discovery entry for older coarse-pitch BGA package families
- helps decide whether a vendor-specific `1.50 mm` owner drawing is publicly reachable

Not safe to claim:

- any exact `1.50 mm` package recommendation until a specific owner document is found

### 3. `connector_origin_defaulting`

#### Candidate class A: CAD-owner library convention docs

Public example found:

- KiCad Library Conventions  
  `https://klc.kicad.org/`

Exact safe scope:

- official KiCad library convention for footprint orientation
- connector-specific convention support such as multi-purpose connectors oriented horizontally with `pin 1` on the left side
- fabrication-layer arrow indicator next to connector `pin 1`

Not safe to claim:

- universal connector-origin truth
- package-owner approval for all connector families

#### Candidate class B: connector-owner recommended PCB layout / footprint drawings

Public examples found:

- Molex sales drawing with recommended PCB layout and explicit pin numbering  
  `https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/105/105133/1051330002_sd.pdf`
- Samtec footprint drawing surface  
  `https://suddendocs.samtec.com/prints/mb1-1xx-xx-xx-s-xx-sl-x-footprint.pdf`
- Amphenol connector drawing with `ARROW MARK`, `CONNECTOR FRONT SIDE`, and `PIN-1`  
  `https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/10178546.pdf`

Exact safe scope:

- series-specific connector orientation, front-side reference, and `pin-1` marking conventions
- safe as connector-owner evidence for that connector family only

Not safe to claim:

- one default origin or left/right convention across all connector owners and all connector styles
- interchangeability between wire-to-board, board-to-board, USB, mezzanine, and sensor connectors

### 4. `installation_mark_conventions`

#### Candidate class A: CAD-owner footprint-marking conventions

Public example found:

- KiCad Library Conventions  
  `https://klc.kicad.org/`

Exact safe scope:

- `F.SilkS` polarity / `pin-1` designator expectations
- `F.Fab` bevel near `pin-1` for IC packages
- `F.Fab` small arrow next to `pin-1` for connectors

Not safe to claim:

- standards-owner universal installation-mark geometry
- mandatory manufacturing acceptance criteria outside KiCad library governance

#### Candidate class B: package-owner package-outline and packaging-spec pin-1 index rules

Public examples found:

- Microchip packaging-spec pages repeatedly stating `Pin 1 visual index feature may vary, but must be located within the hatched area`  
  `https://ww1.microchip.com/downloads/en/PackagingSpec/00000049BN%20.pdf`
  `https://ww1.microchip.com/downloads/en/PackagingSpec/00049BE.pdf`
- Microchip package drawings that include `SILK SCREEN` and recommended land-pattern panels for specific BGAs

Exact safe scope:

- package-owner control over where the package `pin 1` visual index belongs
- package-body orientation and package-mark boundary only

Not safe to claim:

- PCB assembly-document conventions from package-body rules alone
- one generic visual-shape rule for all package families

#### Candidate class C: product datasheet package-info warnings that separate product marking from placement orientation

Public example found:

- ST `ESDARF02-1BU2CK` package information stating product marking may rotate and only `pin 1 mark` should be used for placement orientation  
  `https://www.st.com/content/ccc/resource/technical/document/datasheet/6d/11/74/c3/f2/d5/43/1b/DM00090692.pdf/files/DM00090692.pdf/jcr%3Acontent/translations/en.DM00090692.pdf`

Exact safe scope:

- owner-scoped warning that top marking is not a reliable installation orientation cue
- safe support for `use pin-1 mark, not arbitrary product text rotation`

Not safe to claim:

- universal installation-mark style or size rules
- cross-vendor placement doctrine from a single ST package example

## What Remains Unresolved

1. `1.50 mm` exact replacement is still unresolved.
   Public scouting found standards-adjacent discovery surfaces, but no clean owner-public recommended land-pattern row was confirmed in this pass.

2. `0.75 mm` has usable owner candidates, but only at package-owner scope.
   A later landing must stay tied to named package drawings and must not collapse Microchip, NXP, or any future vendor rows into one generic pitch law.

3. `connector-origin defaulting` is still unresolved at universal-rule level.
   Current public candidates split between CAD-library convention and connector-series-specific owner drawings.

4. `installation-mark conventions` are still fragmented across three authority layers:
   package-body index rules, CAD-library footprint-marking rules, and product-specific placement warnings.

5. No public scouting result in this pass justifies:
   - one universal connector origin
   - one universal installation-mark shape
   - one universal `0.75 mm` or `1.50 mm` pad-diameter rule

## Safest Next Landing Strategy

1. `0.75 mm` should be the first follow-up landing.
   Use one package-owner drawing that already contains `0.75 BSC` plus `RECOMMENDED LAND PATTERN`, and keep the resulting fact strictly owner-scoped and package-scoped.

2. `1.50 mm` should stay in `discovery_hold` unless a public owner package drawing or application note with explicit land-pattern guidance is found.
   The current safest route is standards-adjacent discovery first, not fact landing.

3. `connector-origin` should land only as a bounded convention note if needed:
   combine one CAD-owner convention source and one connector-owner drawing, and explicitly mark the result as `library/series convention only`.

4. `installation-mark` should land only as a layered boundary note if needed:
   combine one CAD-owner footprint-marking convention, one package-owner `pin 1` visual-index rule, and one product-owner placement warning.

5. Do not reopen a universal package-governance fact card through this lane unless a stronger cross-owner standards source becomes public and specific enough to justify it.

## Recommended Next Action

Recommended next action: `land_one_owner_scoped_0p75_mm_replacement_candidate_and_keep_1p50_connector_installation_on_scouting_hold`

Priority order:

1. Microchip `0.75 mm` BGA package drawing with embedded recommended land pattern
2. public owner search for a real `1.50 mm` coarse-pitch BGA package drawing or app note
3. bounded connector-origin convention recovery using KiCad + one connector-owner drawing
4. bounded installation-mark convention recovery using KiCad + one package-owner warning source

## Status

`scouting_complete_with_partial_public_recovery_routes`

What is complete:

- candidate public source classes are identified for all four residuals
- exact scope boundaries are explicit
- the safest next landing order is explicit

What is not complete:

- no facts, wiki pages, or source records were created
- no `1.50 mm` exact-data replacement source was closed
- no universal connector-origin or installation-mark rule was recovered
