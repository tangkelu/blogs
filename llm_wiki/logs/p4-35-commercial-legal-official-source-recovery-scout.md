# P4-35 Commercial / Legal Official-Source Recovery Scout

Date: 2026-04-28
Model lane: `gpt-5.4`
Scope owner: official-source recovery scout only
Input drafts treated as claim inventory only:
- `/code/blogs/tmps/2025.10.1/en`
- `/code/blogs/tmps/2025.10.13/en`

## Scope

This scout covers only:
- commercial governance claim families around quotes, lead time, shipping/customs allocation, and MOQ
- legal-sensitive claim families around PCB copying, cloning, repair, rework, modification, and reverse-engineering boundaries

This scout does not upgrade draft prose into facts by itself. It records official sources that could later support fact cards, plus hard limits where official support is absent or narrower than the drafts imply.

## High-risk draft claim families inventoried

Commercial:
- quote validity, quote completeness, hidden-fee framing, engineering-review caveats
- lead-time promises, quick-turn ranges, shipping time inclusion, customs-delay handling
- landed-cost / duties / taxes allocation
- MOQ as if universal or fixed across the industry

Legal-sensitive:
- when cloning/copying/reverse engineering is lawful
- patent, trademark, copyright, trade-secret, and contract boundaries
- repair / modification / rework framed as legally safe by default
- DMCA / software-lock / circumvention implications
- IPC standards being used as if they authorize repair activity

## Official sources recovered

### 1) ICC Incoterms rules

- URL: https://iccwbo.org/business-solutions/incoterms-rules/
- Source owner: International Chamber of Commerce
- Supported claims:
  - Incoterms are standardized trade terms used in B2B sale contracts.
  - They allocate tasks, costs, and risks between seller and buyer.
  - Current ICC version is Incoterms 2020, effective January 1, 2020.
- Exact limits / non-claims:
  - This page does not set PCB pricing, manufacturing lead times, MOQ, or carrier delivery guarantees.
  - It is about contract allocation, not whether a shipment clears customs on time.
- Candidate fact IDs:
  - `P4-35-COMM-INCOTERMS-ALLOCATE-COST-RISK`
  - `P4-35-COMM-INCOTERMS-2020-EFFECTIVE-DATE`

### 2) ICC Incoterms Q&A on what the rules do and do not do

- URL: https://library.iccwbo.org/clp/clp-incoterms-qa-2020.htm?AGENT=ICC_CHN
- Source owner: International Chamber of Commerce
- Supported claims:
  - Incoterms describe obligations, risk transfer, and cost allocation.
  - Incoterms do not replace the sale contract or carriage contract.
- Exact limits / non-claims:
  - Not a source for manufacturing-time claims, quote validity windows, or customs duty rates.
- Candidate fact IDs:
  - `P4-35-COMM-INCOTERMS-SCOPE-LIMIT`

### 3) CBP Basic Importing and Exporting

- URL: https://www.cbp.gov/trade/basic-import-export
- Source owner: U.S. Customs and Border Protection
- Supported claims:
  - U.S. imports may involve duties, taxes, and fees.
  - Section 321 / de minimis is value-limited and not a universal exemption for all import situations.
- Exact limits / non-claims:
  - This page is high-level guidance, not a commodity-specific PCB tariff ruling.
  - It does not promise clearance timing.
- Candidate fact IDs:
  - `P4-35-COMM-CBP-DUTIES-TAXES-FEES-EXIST`
  - `P4-35-COMM-CBP-DEMINIMIS-NOT-UNIVERSAL`

### 4) CBP Tips for New Importers and Exporters

- URL: https://www.cbp.gov/trade/basic-import-export/importer-exporter-tips
- Source owner: U.S. Customs and Border Protection
- Supported claims:
  - Importers should understand entry requirements before import.
  - Even when using a customs broker, the importer of record remains responsible for entry correctness and applicable duties, taxes, and fees.
  - CBP may examine shipments, and the importer bears associated preparation / examination expense.
- Exact limits / non-claims:
  - Does not provide PCB-specific tariff classification.
  - Does not guarantee customs timing or broker cost levels.
- Candidate fact IDs:
  - `P4-35-COMM-CBP-IMPORTER-OF-RECORD-RESPONSIBILITY`
  - `P4-35-COMM-CBP-EXAM-COST-RISK`

### 5) FedEx international transit-time notes

- URL: https://www.fedex.com/en-us/please_notes/wgrt/us/us/pn_expintlresults.html
- Source owner: FedEx
- Supported claims:
  - FedEx transit-time results assume no clearance delays.
  - Transit results depend on ship date, weight, dimensions, declared/customs value, goods description, packaging, and address data.
  - FedEx’s shipping terms prevail over calculator output if there is a conflict.
- Exact limits / non-claims:
  - Carrier estimate only; not a PCB fabrication lead-time source.
  - Not a customs-law source.
- Candidate fact IDs:
  - `P4-35-COMM-FEDEX-TRANSIT-ASSUMES-NO-CLEARANCE-DELAY`
  - `P4-35-COMM-FEDEX-TRANSIT-DEPENDS-ON-CUSTOMS-DATA`

### 6) DHL customs duties and taxes guide

- URL: https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-duties-and-taxes.html
- Source owner: DHL Express
- Supported claims:
  - Most international shipments are subject to customs duties and taxes.
  - Duty rates are tied to HS code and customs valuation rules.
  - Missing or inaccurate documents can cause clearance delays.
- Exact limits / non-claims:
  - Carrier guidance, not a government tariff schedule.
  - Does not establish PCB-specific landed-cost percentages.
- Candidate fact IDs:
  - `P4-35-COMM-DHL-DUTIES-TAXES-MOST-INTERNATIONAL-SHIPMENTS`
  - `P4-35-COMM-DHL-DOC-ERRORS-CAN-DELAY-CLEARANCE`

### 7) DHL customs clearance documents guidance

- URL: https://www.dhl.com/us-en/home/express/shipping-and-tracking/customs/customs-clearance/customs-clearance-documents.html
- Source owner: DHL Express
- Supported claims:
  - Commercial invoice data is primary for customs processing.
  - Vague goods descriptions are not acceptable.
  - Incomplete or incorrect documents can lead to delays, fines, return, or destruction.
- Exact limits / non-claims:
  - Not a substitute for country-specific customs law.
  - Does not state manufacturing or procurement lead times.
- Candidate fact IDs:
  - `P4-35-COMM-DHL-COMMERCIAL-INVOICE-PRIMARY`
  - `P4-35-COMM-DHL-VAGUE-DESCRIPTIONS-NOT-ACCEPTABLE`

### 8) Sierra Circuits terms and conditions

- URL: https://www.protoexpress.com/terms-and-conditions/
- Source owner: Sierra Circuits / ProtoExpress
- Supported claims:
  - Company quote validity can be time-limited; Sierra states 30 days unless otherwise agreed.
  - Company quotes can be based on RFQ data and remain subject to change if customer data changes.
  - Sierra says quoting is not a full DFM analysis and does not guarantee all assembly/manufacturability issues are identified at quote stage.
  - Sierra states component availability can change and lead-time issues are not guaranteed away at order time.
- Exact limits / non-claims:
  - Company-specific policy only, not an industry-wide rule.
  - Not usable as a generic PCB market benchmark.
- Candidate fact IDs:
  - `P4-35-COMM-COMPANYQUOTE-SIERRA-30DAY-VALIDITY`
  - `P4-35-COMM-COMPANYQUOTE-SIERRA-SUBJECT-TO-RFQ-DATA`
  - `P4-35-COMM-COMPANYQUOTE-SIERRA-NOT-FULL-DFM`

### 9) USPTO patent term

- URL: https://www.uspto.gov/web/offices/pac/mpep/documents/2700_2701.htm
- Source owner: U.S. Patent and Trademark Office
- Supported claims:
  - U.S. patent term under 35 U.S.C. 154(a)(2) is generally 20 years from the U.S. filing date, subject to statutory details.
- Exact limits / non-claims:
  - This is not a freedom-to-operate determination for any board or circuit.
  - Patent-term statements alone do not tell whether a specific PCB is patented.
- Candidate fact IDs:
  - `P4-35-LEGAL-PATENT-TERM-GENERALLY-20Y-FROM-FILING`

### 10) USPTO trademark infringement

- URL: https://www.uspto.gov/page/about-trademark-infringement
- Source owner: U.S. Patent and Trademark Office
- Supported claims:
  - Trademark infringement is unauthorized use of a trademark in a way likely to cause confusion, deception, or mistake about source.
- Exact limits / non-claims:
  - This page does not say every use of a mark is infringing.
  - It does not analyze nominative fair use or any particular PCB marking scenario.
- Candidate fact IDs:
  - `P4-35-LEGAL-TRADEMARK-INFRINGMENT-LIKELY-CONFUSION`

### 11) USPTO trademark process basics

- URL: https://www.uspto.gov/trademarks/basics/trademark-process
- Source owner: U.S. Patent and Trademark Office
- Supported claims:
  - Trademarks protect brand names and logos.
  - Patents protect inventions.
  - Copyright protects original artistic or literary works.
- Exact limits / non-claims:
  - This is definitional guidance, not case-specific infringement analysis.
- Candidate fact IDs:
  - `P4-35-LEGAL-IP-TYPE-DISTINCTIONS-USPTO`

### 12) USPTO trade secret resources

- URL: https://www.uspto.gov/ip-policy/trade-secret-policy/trade-secrets-additional-information-and-resources
- Source owner: U.S. Patent and Trademark Office
- Supported claims:
  - Economic Espionage Act criminalizes trade-secret theft in specified circumstances.
  - Defend Trade Secrets Act created a federal civil cause of action for misappropriation.
- Exact limits / non-claims:
  - This page does not define whether a given PCB sample was lawfully obtained.
  - It does not turn all reverse engineering into misappropriation; acquisition path still matters.
- Candidate fact IDs:
  - `P4-35-LEGAL-TRADESECRET-EAA-DTSA-EXIST`

### 13) U.S. Copyright Office FAQ: what copyright protects

- URL: https://www.copyright.gov/help/faq/faq-protect.html
- Source owner: U.S. Copyright Office
- Supported claims:
  - Copyright protects original works of authorship.
  - Copyright does not protect facts, ideas, systems, or methods of operation, though expression may be protected.
- Exact limits / non-claims:
  - This is not a PCB-layout-specific ruling.
  - It does not answer, by itself, whether a specific board artwork is protected or infringed.
- Candidate fact IDs:
  - `P4-35-LEGAL-COPYRIGHT-EXPRESSION-NOT-IDEA-SYSTEM`

### 14) U.S. Copyright Office Section 1201 overview

- URL: https://www.copyright.gov/1201/
- Source owner: U.S. Copyright Office
- Supported claims:
  - DMCA Section 1201 generally prohibits circumvention of access controls.
  - Current temporary exemptions from the 2024 rulemaking remain in force for October 2024 through October 2027.
- Exact limits / non-claims:
  - This is about circumvention of access controls, not general patent, trademark, or trade-secret legality.
  - An exemption does not equal blanket permission to copy products.
- Candidate fact IDs:
  - `P4-35-LEGAL-DMCA-1201-GENERAL-PROHIBITION`
  - `P4-35-LEGAL-DMCA-2024-2027-TEMP-EXEMPTIONS`

### 15) U.S. Copyright Office 2024 petitions / current exemption categories

- URL: https://www.copyright.gov/1201/2024/petitions/renewal/
- Source owner: U.S. Copyright Office
- Supported claims:
  - Existing exemption categories include diagnosis / maintenance / repair for certain classes such as motorized land vehicles, marine vessels, agricultural vehicles/vessels, consumer devices, and medical devices/systems.
  - Existing interoperability / jailbreaking categories exist for certain device classes such as smartphones, smart TVs, voice assistants, routers, and dedicated network devices.
- Exact limits / non-claims:
  - This page lists exemption classes in the proceeding context; it is not a universal right-to-repair statute.
  - It does not grant a generic exemption for all industrial or commercial PCB-controlled equipment.
- Candidate fact IDs:
  - `P4-35-LEGAL-DMCA-EXEMPTION-CATEGORIES-REPAIR`
  - `P4-35-LEGAL-DMCA-EXEMPTION-CATEGORIES-INTEROPERABILITY`

### 16) Copyright Office 2024 Register recommendation snippet on commercial / industrial expansion

- URL: https://www.copyright.gov/1201/2024/2024_Section_1201_Registers_Recommendation.pdf
- Source owner: U.S. Copyright Office
- Supported claims:
  - The 2024 recommendation discusses requests to expand repair exemptions to commercial / industrial equipment.
  - The recommendation text indicates broader right-to-repair issues extend beyond Section 1201 and may require broader solutions than this rulemaking.
- Exact limits / non-claims:
  - This does not create a blanket commercial-equipment exemption.
  - Use carefully; scope is anti-circumvention only.
- Candidate fact IDs:
  - `P4-35-LEGAL-DMCA-COMMERCIAL-INDUSTRIAL-NOT-BLANKETLY-COVERED`

### 17) IPC-7711C/7721C scope

- URL: https://www.ipc.org/TOC/IPC-TOC-7711-21C.pdf
- Source owner: IPC
- Supported claims:
  - IPC-7711C/7721C is the IPC document for rework, modification, and repair of electronic assemblies.
- Exact limits / non-claims:
  - Standard scope only; not a legal authorization to perform repair or copying.
  - Does not validate a supplier’s current capability or success rate.
- Candidate fact IDs:
  - `P4-35-QUALITY-IPC7711-7721-SCOPE-REWORK-MOD-REPAIR`

### 18) IPC-A-610 scope / limit

- URL: https://www.ipc.org/TOC/IPC-A-610G.pdf
- Source owner: IPC
- Supported claims:
  - IPC-A-610 is an acceptability standard for electronic assemblies.
  - The standard’s own scope states it is not intended to authorize repair / modification / change of the customer’s product.
- Exact limits / non-claims:
  - This directly blocks using IPC-A-610 as a legal or contractual authorization source.
- Candidate fact IDs:
  - `P4-35-QUALITY-IPCA610-DOES-NOT-AUTHORIZE-REPAIR`

## Candidate fact upgrades with best official support

These are the cleanest later-upgrade candidates from this lane.

- `P4-35-COMM-INCOTERMS-ALLOCATE-COST-RISK`
  - Best sources: ICC pages above
  - Safe use: contract-role framing for quotes and shipping terms

- `P4-35-COMM-CBP-IMPORTER-OF-RECORD-RESPONSIBILITY`
  - Best sources: CBP importer tips
  - Safe use: landed-cost / customs-responsibility governance

- `P4-35-COMM-FEDEX-TRANSIT-ASSUMES-NO-CLEARANCE-DELAY`
  - Best sources: FedEx international transit notes
  - Safe use: shipping estimate caveats, not manufacturing lead-time promises

- `P4-35-COMM-DHL-DOC-ERRORS-CAN-DELAY-CLEARANCE`
  - Best sources: DHL customs documentation pages
  - Safe use: documentation-completeness guidance for shipping / delivery expectations

- `P4-35-COMM-COMPANYQUOTE-SIERRA-30DAY-VALIDITY`
  - Best sources: Sierra terms page
  - Safe use: example of company-specific quote-validity governance only

- `P4-35-COMM-COMPANYQUOTE-SIERRA-NOT-FULL-DFM`
  - Best sources: Sierra terms page
  - Safe use: example that quoted price is not equivalent to full engineering release

- `P4-35-LEGAL-PATENT-TERM-GENERALLY-20Y-FROM-FILING`
  - Best sources: USPTO MPEP / statute excerpt
  - Safe use: general patent-duration boundary only

- `P4-35-LEGAL-TRADEMARK-INFRINGMENT-LIKELY-CONFUSION`
  - Best sources: USPTO infringement page
  - Safe use: logo / mark copying caution

- `P4-35-LEGAL-TRADESECRET-EAA-DTSA-EXIST`
  - Best sources: USPTO trade secret resources
  - Safe use: caution where board/sample/data acquisition is confidential or restricted

- `P4-35-LEGAL-COPYRIGHT-EXPRESSION-NOT-IDEA-SYSTEM`
  - Best sources: Copyright Office FAQ
  - Safe use: narrow distinction between system/function and expression

- `P4-35-LEGAL-DMCA-1201-GENERAL-PROHIBITION`
  - Best sources: Copyright Office 1201 overview
  - Safe use: software-lock / access-control boundary discussions

- `P4-35-LEGAL-DMCA-EXEMPTION-CATEGORIES-REPAIR`
  - Best sources: Copyright Office 2024 proceeding pages
  - Safe use: narrow description of current exemption classes and dates

- `P4-35-QUALITY-IPCA610-DOES-NOT-AUTHORIZE-REPAIR`
  - Best sources: IPC-A-610 scope snippet
  - Safe use: blocking misuse of IPC acceptability standards as legal permission

## Blocked or only partially supportable draft claim families

### Commercial claims blocked

- Universal PCB price benchmarks, markups, and hidden-fee percentages
  - Draft examples like "prices vary 300%", "hidden fees average 18-35%", "fair price 40% below highest quote" are not supported by official sources recovered.

- Universal PCB production lead-time ranges
  - Draft ranges such as `2-layer 24-48h`, `4-layer 3-5 days`, `7-14 day typical runs`, or fixed quick-turn premiums are not supported by official/government/standards sources here.
  - Carrier sources only support shipping-estimate caveats, not fab-cycle facts.

- MOQ framed as an industry-wide fixed rule
  - Recovered sources support that MOQ is policy / process dependent, but no official universal PCB MOQ standard was found.
  - Keep MOQ blocked unless tied to a specific supplier’s official terms page and clearly labeled as supplier-specific.

- Duties / VAT / GST percentages stated generically
  - Draft percentages in logistics pages are too country- and commodity-specific for upgrade from the recovered official set.

### Legal-sensitive claims blocked or narrowed

- "Courts generally support cloning for maintenance and repair"
  - Too broad. Recovered official sources support only narrower propositions: DMCA anti-circumvention exists; some temporary exemptions exist; IP/trade-secret/trademark rules still apply.
  - No official court/government source recovered that cleanly authorizes broad PCB cloning for maintenance.

- "Clean-room reverse engineering is legally defensible" as a broad statement
  - Not upgraded from current official set.
  - Needs case law / formal legal authority, which this lane did not rely on.

- "PCB artwork is copyrightable" as a categorical claim
  - Current official set supports expression-vs-idea distinction only.
  - Specific PCB-layout copyrightability remains fact- and doctrine-sensitive; keep blocked.

- "Many purchase agreements prohibit reverse engineering or duplication"
  - Plausible, but not a reusable official fact from the recovered sources.
  - Could only be stated as contract-specific if sourced to actual terms.

- "Educational and research purposes are generally permitted"
  - Too broad for upgrade.
  - IP and contract restrictions can still apply.

- "Exact duplication maintains FDA approval"
  - Not supported by official FDA/Copyright/USPTO sources recovered here.
  - High-stakes regulatory claim; keep blocked.

- Broad lawful-competitor-analysis claims
  - Current official set does not provide a simple official rule authorizing competitor board reverse engineering in general.

## Residual gaps

- No strong official source recovered for universal PCB MOQ governance.
- No strong official source recovered for universal PCB quote-price benchmarks or hidden-fee percentages.
- No strong official source recovered for universal PCB fab lead-time ranges.
- No official-source recovery yet for non-U.S. legal boundaries; current legal sources are U.S.-heavy.
- No case-law lane was used here; that leaves some reverse-engineering / cloning boundary questions intentionally unresolved.
- No product- or jurisdiction-specific customs classification work was done for PCB/PCBA HS codes or tariff treatment.

## Practical editorial guardrails for downstream use

- Safe:
  - "Incoterms allocate seller/buyer costs, tasks, and risk."
  - "Importer of record remains responsible for entry correctness and applicable duties/taxes/fees."
  - "Carrier transit estimates assume no customs-clearance delay."
  - "DMCA Section 1201 generally prohibits circumvention; temporary exemptions are limited and class-specific."
  - "IPC repair/rework standards define technical practice scope; they do not themselves authorize the work legally."

- Unsafe without more sourcing:
  - current PCB market price averages
  - universal lead-time promises
  - universal MOQ rules
  - blanket legality of cloning / copying / reverse engineering
  - regulatory or legal outcomes for a specific board, customer, or jurisdiction

## Lane result

- Allowed edit made: `/code/blogs/llm_wiki/logs/p4-35-commercial-legal-official-source-recovery-scout.md`
- No tracker, registry, wiki, facts, or unrelated log edits made.
