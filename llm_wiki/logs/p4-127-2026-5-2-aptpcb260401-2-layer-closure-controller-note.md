Date: 2026-05-02
Lane: `P4-127 APTPCB260401 2-layer closure controller`
Input: `logs/p4-31-aptpcb260401-2-layer-blog-ingestion-map.md`, `logs/p4-125-2026-5-2-knowledge-base-distance-and-subagent-roadmap.md`, `logs/p4-119-2026-5-2-post-p4-118-residual-lane-recheck.md`, `logs/backlog.md`
Output: `logs/p4-127-2026-5-2-aptpcb260401-2-layer-closure-controller-note.md`
Scope status: `controller_only`
Evidence status: `claim_family_closure_ranked`

# Purpose

Convert the unresolved `APTPCB260401` `2-layer` claim families into one explicit closure-controller ranking so the batch no longer sits as one mixed residual.

This pass does not:

- create or update `sources/`, `facts/`, or `wiki/`
- reopen draft-to-data promotion
- assert any new numeric, material, finish, cost, lead-time, supplier, or capability fact
- change the existing claim-family-level boundary from `P4-31`

# Baseline

`P4-31` already made the batch deletion-safe at claim-family level and explicitly blocked:

- draft-originated `2-layer` design-rule numerics and stackup defaults
- material values
- impedance and thermal calculations
- finish chemistry claims
- cost and lead-time claims
- supplier proof and `APTPCB` capability proof

`P4-125` then identified this exact subset as a priority closure family because it still lacks source-backed closure for those unresolved classes, but it did not place the whole subset into explicit hold-only status like `20-layer` or `22-layer`.

# Closure Ranking

## 1. `source_recovery_now`

These families are structurally recoverable from public official sources and can justify a future bounded source lane.

### A. material exact-value families

Includes:

- exact product or exact family values for `FR-4`, high-`Tg` FR-4, `PTFE`, Rogers, ceramic / alumina / `AlN`, `IMS` / aluminum-core, copper-core, and polyimide variants appearing in the `2-layer` batch

Why this is `source_recovery_now`:

- the repo already has adjacent material coverage and a named roadmap for deeper product-grade recovery
- the unresolved gap is mostly exact-value depth, not a structural authority ceiling
- official datasheets and product pages can close bounded value families without relying on draft prose

Boundary:

- recover exact material values only from product-grade or current official material sources
- do not treat recovered values as universal `2-layer` defaults

### B. finish chemistry identity families

Includes:

- `ENIG`, `ENEPIG`, `OSP`, `HASL`, and lead-free `HASL` chemistry / process-identity source gaps

Why this is `source_recovery_now`:

- `P4-31` already named finish-source supplementation as a future source need
- official finish documentation or official standards metadata can support bounded chemistry / process identity better than the current draft-only posture

Boundary:

- this lane can recover chemistry identity, finish-type distinctions, and guarded process framing
- it does not by itself unlock shelf life, thickness, planarity, black-pad prevention, solderability ranking, or production-readiness proof

## 2. `tracker_only`

These families are not the right immediate source-recovery lane, but they are not permanent holds. They should stay visible in trackers until a narrower evidence path or dependent source lane exists.

### A. impedance calculation families

Includes:

- controlled-impedance formulas, geometry-to-ohms examples, and `2-layer` impedance feasibility wording

Why this is `tracker_only`:

- generic reusable `2-layer` impedance outcomes are not recoverable as one public universal table
- any safe recovery depends on exact stackup, dielectric, copper, geometry, and tolerance context
- current value is more likely to come from method-boundary framing or exact material-backed examples later, not from a batch-wide recovery pass now

### B. thermal calculation families

Includes:

- thermal-resistance examples, `LED` heat-spreading outcomes, copper-core vs aluminum-core thermal comparisons, and generic heat-performance calculations

Why this is `tracker_only`:

- these claims are condition-sensitive and usually collapse without exact material, board, copper, mounting, and airflow context
- a later lane may recover method framing or exact platform data, but a general `2-layer` closure pass cannot safely unlock them now

### C. non-universal numeric framing tied to exact future evidence packs

Includes:

- context-dependent numeric phrasing that may become admissible only after exact material or finish sources land

Why this is `tracker_only`:

- the class is not inherently impossible
- it is merely not ready as a batch-wide recovery target before upstream exact-source lanes land

## 3. `hold_only`

These families are structurally blocked by dynamic commercial evidence, dated supplier-only proof, or non-reusable universalization pressure. They should not open as public source-recovery lanes now.

### A. universal `2-layer` design-rule numerics

Includes:

- fixed stackup defaults
- trace / space, drill, pad, annular-ring, current-capacity, copper, tolerance, and similar generic numeric tables

Why this is `hold_only`:

- the batch asks for reusable general `2-layer` numerics, but those are not one stable public truth class
- they vary by exact material, board thickness, copper weight, fab flow, impedance target, and capability window
- reopening them now would predictably collapse into overgeneralized or supplier-marketing numerics

### B. cost and lead-time families

Includes:

- price ladders, savings claims, prototype vs production cost logic, quick-turn windows, and schedule promises

Why this is `hold_only`:

- these are dynamic commercial claims
- the evidence path is dated supplier-specific or quote-specific, not a reusable public knowledge-base lane

### C. supplier proof families

Includes:

- direct-factory proof, equipment proof, quality-proof, audit-proof, qualification-proof, and supplier-status assertions

Why this is `hold_only`:

- these require dated supplier-scoped evidence and admissibility review
- public marketing pages do not safely close this class

### D. `APTPCB` capability proof families

Includes:

- quick-turn capability, production scale, yield, inspection coverage, material stocking, process-limit claims, and sector-readiness proof tied to `APTPCB`

Why this is `hold_only`:

- this is dated capability-record territory, not general public source recovery
- the missing ceiling is supplier-owned proof, not missing generic reference material

# Ranked Closure Result

1. `source_recovery_now`
   - material exact-value families
   - finish chemistry identity families
2. `tracker_only`
   - impedance calculation families
   - thermal calculation families
   - dependent non-universal numeric framing that needs upstream exact-source lanes first
3. `hold_only`
   - universal `2-layer` design-rule numerics
   - cost and lead-time families
   - supplier proof families
   - `APTPCB` capability proof families

# Controller Decision

The `APTPCB260401` `2-layer` subset should not be treated as one undifferentiated residual anymore.

Default next move:

- if this subset is reopened, open only the `source_recovery_now` portion first
- keep `tracker_only` families visible but inactive until narrower exact-source conditions exist
- keep `hold_only` families closed unless dated supplier or capability evidence materially changes the ceiling

# Status

- active continuation state: `aptpcb260401_2_layer_closure_ranked`
- repo effect: `controller_note_only`
- readiness change: `none`
