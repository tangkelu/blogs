## Module: Capability + ordering (enable when intent is transactional: manufacturer/service/quote/MOQ/lead time/cost)

When this module is enabled, the article must include:

### Capability snapshot (only use our allowed capability reference)
Add a compact table:
`Parameter | Standard | Advanced | Notes`
- 10–14 rows, using only capabilities provided in the base template’s “Capability reference”.
- Do not invent certifications, equipment brands, or tighter numbers.

### Lead time & MOQ table
Add a table:
`Order type | Typical lead time | MOQ | Key drivers`
- Include prototype / small batch / production rows.

### RFQ / DFM checklist (quote-ready)
Add a bullet list: “What to send for DFM/quote” (8–12 items), covering:
- design data (Gerbers/ODB++/IPC-2581), drill, stackup, fab notes
- quantity (proto + production), target lead time, special requirements (impedance/testing/acceptance)
- assembly inputs if relevant (BOM/centroid)

### Tone guardrails
- Keep it factual and practical; the “ordering” content must not overwhelm the technical answer.
- If the page is primarily definition/how-to, keep this module short (1–2 sections max).

