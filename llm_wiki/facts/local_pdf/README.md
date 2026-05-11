# Local PDF Facts

This layer stores curated facts that come from repo-accepted local PDF evidence rather than official-source replacement.

Rules:

- these cards may be used in blog body
- they must keep explicit scope
- they must not be rewritten as official standards, manufacturer datasheets, certification proof, or live capability promises
- every card must point back to `pdf_evidence/pcb_ziliao/` or another explicitly governed evidence layer

Required fields:

- `fact_id`
- `title`
- `authority_class`
- `allowed_for`
- `not_allowed_for`
- `evidence_ids`
- `scope_type`
- `confidence`
- `limits_and_non_claims`

Current first slice:

- package structural visuals promoted for non-numeric footprint-review explanation
- PCBA local images retained as evidence-only because the safe claim layer already exists in the admitted boundary facts
