#!/usr/bin/env python3
from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass, field
from pathlib import Path


BLOGS_ROOT = Path("/code/hileap/frontendAPT/public/static/blogs")
TARGET_LOCALES = ["en", "de", "it", "fr", "ru", "es", "ar"]


@dataclass(frozen=True)
class PostSpec:
    year: str
    month: str
    slug: str
    titles: dict[str, str]  # locale -> title
    descriptions: dict[str, str]  # locale -> description
    en_h2_renames: dict[str, str] = field(default_factory=dict)


POSTS: list[PostSpec] = [
    PostSpec(
        year="2025",
        month="01",
        slug="differential-microwave-routing-cryogenic",
        titles={
            "en": "Differential Microwave Routing at Cryogenic Temps: Stackup, Geometry, and Validation",
            "de": "Differenzielles Mikrowellen-Routing bei Kryo-Temperaturen: Stackup, Geometrie, Validierung",
            "it": "Routing differenziale a microonde in criogenia: stackup, geometria e validazione",
            "fr": "Routage micro-ondes différentiel en cryogénie : stackup, géométrie et validation",
            "ru": "Дифференциальная микроволновая трассировка при крио‑температурах: стек‑ап, геометрия, валидация",
            "es": "Ruteo diferencial de microondas a temperaturas criogénicas: stackup, geometría y validación",
            "ar": "توجيه ميكروويف تفاضلي عند درجات كريوجينية: الـStackup والهندسة وخطة التحقق",
        },
        descriptions={
            "en": "Design cryogenic differential microwave routes with the right stackup, impedance targets, transitions, and a practical validation plan.",
            "de": "Kryogenes differenzielles Mikrowellen-Routing: geeigneter Stackup, Impedanzziele, Übergänge und Validierungsplan.",
            "it": "Progetta routing differenziale a microonde in criogenia: stackup, obiettivi d’impedenza, transizioni e piano di validazione.",
            "fr": "Concevoir un routage micro-ondes différentiel en cryogénie : stackup, cibles d’impédance, transitions et plan de validation.",
            "ru": "Как проектировать крио‑диф‑микроволновые линии: стек‑ап, импеданс, переходы и практический план валидации.",
            "es": "Cómo diseñar ruteo diferencial de microondas en criogenia: stackup, impedancia, transiciones y plan de validación.",
            "ar": "كيفية تصميم مسارات ميكروويف تفاضلية للكريوجينيا: stackup، أهداف الممانعة، الانتقالات، وخطة تحقق عملية.",
        },
        en_h2_renames={
            "Key takeaways for differential microwave routing cryogenic": "Key Takeaways",
            "What differential microwave routing cryogenic really means (scope & boundaries)": "What this topic means (scope & boundaries)",
            "differential microwave routing cryogenic metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose differential microwave routing cryogenic: selection guidance by scenario (trade-offs)": "How to choose an approach (trade-offs by scenario)",
            "differential microwave routing cryogenic implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "differential microwave routing cryogenic common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "differential microwave routing cryogenic FAQ (cost, lead time, DFM files, stackup, impedance, Dk/Df)": "FAQ (stackup, impedance, Dk/Df, lead time)",
            "Resources for differential microwave routing cryogenic (related pages and tools)": "Related pages & tools",
            "differential microwave routing cryogenic glossary (key terms)": "Glossary (key terms)",
            "Conclusion: differential microwave routing cryogenic next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="08",
        slug="data-center-ultrasound-probe-interface-pcb",
        titles={
            "en": "Ultrasound Probe Interface PCB: Specs, Risks, and Production Checklist",
            "de": "Ultraschallsonden-Interface-PCB: Spezifikationen, Risiken und Produktions-Checkliste",
            "it": "PCB interfaccia sonda ultrasound: specifiche, rischi e checklist di produzione",
            "fr": "PCB d’interface de sonde ultrasound : spécifications, risques et checklist production",
            "ru": "Плата интерфейса ultrasound‑зонда: спецификации, риски и чек‑лист для серии",
            "es": "PCB de interfaz para sonda de ultrasonido: especificaciones, riesgos y checklist de producción",
            "ar": "لوحة واجهة مسبار الموجات فوق الصوتية: المواصفات والمخاطر وقائمة إنتاج",
        },
        descriptions={
            "en": "A buyer-ready checklist for probe interface PCBs: stackup/materials, critical risks, validation tests, and what to lock before production.",
            "de": "Beschaffungs-Checkliste für Probe-Interface-PCBs: Stackup/Materialien, kritische Risiken, Validierungstests und was vor Serie festgelegt sein muss.",
            "it": "Checklist per PCB interfaccia sonda: stackup/materiali, rischi critici, test di validazione e cosa definire prima della produzione.",
            "fr": "Checklist d’achat pour PCB d’interface de sonde : stackup/matériaux, risques critiques, tests de validation et points à verrouiller avant production.",
            "ru": "Чек‑лист для интерфейсных плат зонда: стек‑ап/материалы, ключевые риски, тесты валидации и что зафиксировать перед серией.",
            "es": "Checklist para PCB de interfaz de sonda: stackup/materiales, riesgos críticos, pruebas de validación y qué cerrar antes de producción.",
            "ar": "قائمة جاهزة للشراء: stackup/المواد، المخاطر الحرجة، اختبارات التحقق، وما الذي يجب تثبيته قبل الإنتاج.",
        },
        en_h2_renames={
            "data-center Ultrasound probe interface PCB: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use data-center Ultrasound probe interface PCB (and when a standard approach is better)": "When to use this approach (and when not to)",
            "data-center Ultrasound probe interface PCB specifications (materials, stackup, tolerances)": "Specs to define (materials, stackup, tolerances)",
            "data-center Ultrasound probe interface PCB manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "data-center Ultrasound probe interface PCB validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "data-center Ultrasound probe interface PCB supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose data-center Ultrasound probe interface PCB (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "data-center Ultrasound probe interface PCB FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for data-center Ultrasound probe interface PCB (related pages and tools)": "Related pages & tools",
            "Request a quote for data-center Ultrasound probe interface PCB (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: data-center Ultrasound probe interface PCB next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="06",
        slug="automotive-grade-sic-rectifier-board",
        titles={
            "en": "Automotive-Grade SiC Rectifier Boards: Layout, Thermal, and Reliability Checklist",
            "de": "Automotive-Grade SiC-Gleichrichterplatinen: Layout, Thermik und Zuverlässigkeits-Checkliste",
            "it": "Schede raddrizzatrici SiC automotive-grade: layout, termica e checklist affidabilità",
            "fr": "Cartes redresseur SiC automotive-grade : layout, thermique et checklist fiabilité",
            "ru": "Платы SiC‑выпрямителя automotive‑grade: разводка, тепловой дизайн и чек‑лист надежности",
            "es": "Placas rectificadoras SiC automotive-grade: layout, térmica y checklist de fiabilidad",
            "ar": "لوحات تقويم SiC بمعيار سيارات: التخطيط والحرارة وقائمة تحقق للاعتمادية",
        },
        descriptions={
            "en": "Design SiC rectifier boards for automotive environments: creepage/clearance, thermal paths, EMI control, and validation tests.",
            "de": "SiC-Gleichrichterplatinen für Automotive: Kriech-/Luftstrecken, Wärmeableitung, EMI-Kontrolle und Validierungstests.",
            "it": "Progetta schede raddrizzatrici SiC per automotive: creepage/clearance, gestione termica, EMI e test di validazione.",
            "fr": "Concevoir des cartes redresseur SiC pour l’automotive : creepage/clearance, thermique, EMI et tests de validation.",
            "ru": "Проектирование SiC‑выпрямителя для automotive: изоляционные расстояния, тепловые пути, EMI и тесты валидации.",
            "es": "Diseño de placas SiC para automoción: creepage/clearance, rutas térmicas, control EMI y pruebas de validación.",
            "ar": "تصميم لوحات SiC للسيارات: مسافات الزحف/التفريغ، مسارات الحرارة، التحكم في EMI، واختبارات التحقق.",
        },
        en_h2_renames={
            "What automotive-grade SiC rectifier board really means (scope & boundaries)": "What “SiC rectifier board” means (scope & boundaries)",
            "automotive-grade SiC rectifier board metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose automotive-grade SiC rectifier board: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "automotive-grade SiC rectifier board implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "automotive-grade SiC rectifier board common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "automotive-grade SiC rectifier board FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing)",
            "Resources for automotive-grade SiC rectifier board (related pages and tools)": "Related pages & tools",
            "automotive-grade SiC rectifier board glossary (key terms)": "Glossary (key terms)",
            "Conclusion: automotive-grade SiC rectifier board next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="05",
        slug="mri-compatible-pcb-materials-routing",
        titles={
            "en": "MRI-Compatible PCB Materials & Routing: Low-Magnetic Design Rules and Test Plan",
            "de": "MRI-kompatible PCB-Materialien & Routing: Low-Magnetic Designregeln und Testplan",
            "it": "Materiali e routing PCB compatibili MRI: regole low-magnetic e piano test",
            "fr": "Matériaux et routage PCB compatibles IRM : règles low-magnetic et plan de test",
            "ru": "MRI‑совместимые материалы и трассировка PCB: low‑magnetic правила и план испытаний",
            "es": "Materiales y ruteo de PCB compatibles con MRI: reglas low-magnetic y plan de pruebas",
            "ar": "مواد وتوجيه PCB المتوافق مع MRI: قواعد low‑magnetic وخطة اختبار",
        },
        descriptions={
            "en": "Choose low-magnetic materials and routing practices for MRI environments—plus how to verify performance and compliance.",
            "de": "Low-magnetische Materialien und Routing für MRI-Umgebungen – inklusive Verifikation von Performance und Compliance.",
            "it": "Scegli materiali low-magnetic e regole di routing per ambienti MRI, con verifiche di prestazioni e conformità.",
            "fr": "Choisir des matériaux low-magnetic et des règles de routage pour l’IRM, avec méthodes de vérification performance et conformité.",
            "ru": "Как выбирать low‑magnetic материалы и правила трассировки для MRI‑среды, а также как проверять характеристики и соответствие.",
            "es": "Cómo elegir materiales low-magnetic y prácticas de ruteo para entornos MRI, y cómo verificar desempeño y conformidad.",
            "ar": "اختر مواد low‑magnetic وقواعد توجيه مناسبة لبيئة MRI، مع خطوات للتحقق من الأداء والامتثال.",
        },
        en_h2_renames={
            "What MRI-compatible PCB materials routing really means (scope & boundaries)": "What MRI-compatible PCB design means (scope & boundaries)",
            "Related pages & tools": "Related pages & tools",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="03",
        slug="co-packaged-optics-baseboard-quality",
        titles={
            "en": "Co-Packaged Optics (CPO) Baseboards: Quality Risks, DFM Checks, and Validation",
            "de": "Co-Packaged-Optics-(CPO)-Baseboards: Qualitätsrisiken, DFM-Checks und Validierung",
            "it": "Baseboard Co-Packaged Optics (CPO): rischi qualità, controlli DFM e validazione",
            "fr": "Baseboards Co-Packaged Optics (CPO) : risques qualité, contrôles DFM et validation",
            "ru": "CPO‑baseboard: риски качества, DFM‑проверки и валидация",
            "es": "Baseboards Co-Packaged Optics (CPO): riesgos de calidad, chequeos DFM y validación",
            "ar": "لوحات CPO Baseboard: مخاطر الجودة وفحوصات DFM وخطة التحقق",
        },
        descriptions={
            "en": "A practical quality guide for CPO baseboards: critical failure modes, process controls, and what to validate before scaling production.",
            "de": "Praxisleitfaden zur Qualität von CPO-Baseboards: Ausfallmodi, Prozesskontrolle und Validierung vor dem Hochlauf.",
            "it": "Guida pratica qualità per baseboard CPO: failure mode critici, controlli di processo e cosa validare prima di scalare la produzione.",
            "fr": "Guide pratique qualité pour baseboards CPO : modes de défaillance critiques, contrôle process et validations avant montée en volume.",
            "ru": "Практический гид по качеству CPO‑baseboard: критические отказы, контроль процесса и что валидировать перед масштабированием.",
            "es": "Guía práctica de calidad para baseboards CPO: modos de fallo críticos, control de proceso y validaciones antes de escalar producción.",
            "ar": "دليل جودة عملي لـCPO baseboards: أعطال حرجة، ضبط العملية، وما الذي يجب التحقق منه قبل التوسع في الإنتاج.",
        },
        en_h2_renames={
            "What Co-packaged optics baseboard quality really means (scope & boundaries)": "What “CPO baseboard quality” means (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="11",
        slug="micro-interconnects-and-flex-in-implants",
        titles={
            "en": "Implant Flex PCBs & Micro-Interconnects: Materials, Reliability Risks, and Checklist",
            "de": "Implantat-Flex-PCBs & Mikro-Interconnects: Materialien, Zuverlässigkeitsrisiken, Checkliste",
            "it": "Flex PCB per impianti e micro-interconnect: materiali, rischi affidabilità e checklist",
            "fr": "Flex PCB d’implants et micro-interconnects : matériaux, risques fiabilité et checklist",
            "ru": "Flex PCB для имплантов и микро‑интерконнекты: материалы, риски и чек‑лист надежности",
            "es": "Flex PCB para implantes y micro-interconexiones: materiales, riesgos y checklist de fiabilidad",
            "ar": "Flex PCB للزرعات وmicro‑interconnects: المواد، مخاطر الاعتمادية، وقائمة تحقق",
        },
        descriptions={
            "en": "A buyer-friendly guide to implant flex and micro-interconnects: material choices, manufacturing risks, validation, and supplier questions.",
            "de": "Käuferfreundlicher Leitfaden zu Implantat-Flex und Mikro-Interconnects: Materialien, Fertigungsrisiken, Validierung und Lieferantenfragen.",
            "it": "Guida buyer-friendly su flex per impianti e micro-interconnect: materiali, rischi di produzione, validazione e domande al fornitore.",
            "fr": "Guide d’achat sur flex d’implants et micro-interconnects : matériaux, risques fabrication, validation et questions fournisseur.",
            "ru": "Покупательский гид по flex для имплантов и микро‑интерконнектам: материалы, риски производства, валидация и вопросы поставщику.",
            "es": "Guía de compra sobre flex para implantes y micro-interconexiones: materiales, riesgos de fabricación, validación y preguntas al proveedor.",
            "ar": "دليل جاهز للشراء: خيارات المواد، مخاطر التصنيع، خطة التحقق، وأسئلة تقييم المورّد للزرعات وmicro‑interconnects.",
        },
        en_h2_renames={
            "micro interconnects and flex in implants: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use micro interconnects and flex in implants (and when a standard approach is better)": "When to use this approach (and when not to)",
            "micro interconnects and flex in implants specifications (materials, stackup, tolerances)": "Specs to define (materials, stackup, tolerances)",
            "micro interconnects and flex in implants manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "micro interconnects and flex in implants validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "micro interconnects and flex in implants supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose micro interconnects and flex in implants (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "micro interconnects and flex in implants FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for micro interconnects and flex in implants (related pages and tools)": "Related pages & tools",
            "Request a quote for micro interconnects and flex in implants (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: micro interconnects and flex in implants next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="pcba-stencil-design-rules-for-fine-pitch",
        titles={
            "en": "Fine-Pitch Stencil Design Rules: Apertures, Thickness, and Print Checklist",
            "de": "Schablonendesign für Fine Pitch: Aperturen, Dicke und Druck-Checkliste",
            "it": "Regole stencil fine-pitch: aperture, spessore e checklist di stampa",
            "fr": "Règles de stencil fine-pitch : ouvertures, épaisseur et checklist d’impression",
            "ru": "Правила трафарета для fine‑pitch: апертуры, толщина и чек‑лист печати",
            "es": "Reglas de stencil para fine-pitch: aperturas, espesor y checklist de impresión",
            "ar": "قواعد تصميم الـStencil للـFine‑Pitch: الفتحات والسُمك وقائمة الطباعة",
        },
        descriptions={
            "en": "A practical stencil checklist for fine-pitch SMT: aperture reductions, thickness choice, paste release, and how to avoid bridging.",
            "de": "Praxis-Checkliste für Fine-Pitch-SMT: Apertur-Reduktion, Schablonendicke, Pastenfreigabe und Bridging vermeiden.",
            "it": "Checklist pratica stencil per SMT fine-pitch: riduzioni aperture, scelta spessore, rilascio pasta e come evitare bridging.",
            "fr": "Checklist pratique de stencil fine-pitch : réduction d’ouverture, épaisseur, libération de pâte et éviter les ponts.",
            "ru": "Практический чек‑лист по трафарету: редукция апертур, выбор толщины, выпуск пасты и предотвращение мостиков.",
            "es": "Checklist práctica de stencil: reducción de aperturas, espesor, liberación de pasta y cómo evitar puentes.",
            "ar": "قائمة عملية للـStencil: تقليل الفتحات، اختيار السُمك، تحرير المعجون، وتجنّب الجسور (bridging).",
        },
        en_h2_renames={
            "pcba stencil design rules for fine pitch: what this playbook covers (and who it’s for)": "What this guide covers (and who it’s for)",
            "When pcba stencil design rules for fine pitch is the right approach (and when it isn’t)": "When fine-pitch stencil rules matter most (and when they don’t)",
            "Requirements you must define before quoting": "What to define (before ordering the stencil)",
            "The hidden risks that break scale-up": "Common print defects (root causes & prevention)",
            "Validation plan (what to test, when, and what “pass” means)": "Validation & acceptance (print checks and criteria)",
            "Decision guidance (trade-offs you can actually choose)": "Decision guidance (trade-offs you can choose)",
            "Conclusion (soft CTA, no hype)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="waveguide-to-transition-fixture",
        titles={
            "en": "Waveguide-to-PCB Transition Fixtures: Design Rules and Measurement Checklist",
            "de": "Waveguide-zu-PCB-Übergangsfixturen: Designregeln und Mess-Checkliste",
            "it": "Fixture di transizione waveguide-to-PCB: regole di design e checklist di misura",
            "fr": "Fixations de transition waveguide-to-PCB : règles de design et checklist de mesure",
            "ru": "Фикстуры waveguide‑to‑PCB: правила конструкции и чек‑лист измерений",
            "es": "Fixtures de transición waveguide-to-PCB: reglas de diseño y checklist de medición",
            "ar": "فيكستشر انتقال Waveguide إلى PCB: قواعد التصميم وقائمة القياس",
        },
        descriptions={
            "en": "Build repeatable waveguide-to-PCB transition fixtures: alignment, grounding, launch design, and how to measure S-parameters reliably.",
            "de": "Reproduzierbare Waveguide-zu-PCB-Fixturen: Ausrichtung, Masse, Launch-Design und zuverlässige S-Parameter-Messung.",
            "it": "Fixture waveguide-to-PCB ripetibili: allineamento, massa, launch e come misurare S-parameter in modo affidabile.",
            "fr": "Fixtures waveguide-to-PCB reproductibles : alignement, masse, launch et mesure fiable des S-paramètres.",
            "ru": "Повторяемые waveguide‑to‑PCB фикстуры: выравнивание, земля, launch и надежные измерения S‑параметров.",
            "es": "Fixtures waveguide-to-PCB repetibles: alineación, masa, launch y medición fiable de parámetros S.",
            "ar": "إنشاء فيكستشر انتقال موثوق: المحاذاة، التأريض، تصميم الـlaunch، وكيف تقيس معاملات S بثبات.",
        },
        en_h2_renames={
            "What waveguide-to-PCB transition fixture really means (scope & boundaries)": "What “waveguide-to-PCB fixture” means (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="02",
        slug="shielding-and-grounding-fences-motor-pcb",
        titles={
            "en": "Motor PCBs: Shielding & Ground-Fence Design Rules (EMI Checklist)",
            "de": "Motor-PCBs: Abschirmung & Ground-Fence-Designregeln (EMI-Checkliste)",
            "it": "PCB per motori: regole schermatura e ground fence (checklist EMI)",
            "fr": "PCB moteur : règles de blindage et ground fences (checklist EMI)",
            "ru": "Моторные PCB: экранирование и ground‑fence правила (EMI‑чек‑лист)",
            "es": "PCB para motores: reglas de apantallado y ground fences (checklist EMI)",
            "ar": "لوحات PCB للمحركات: قواعد التدريع وحواجز التأريض (قائمة EMI)",
        },
        descriptions={
            "en": "Reduce motor-drive EMI with practical shielding and grounding fences: via spacing, return paths, keepouts, and validation tests.",
            "de": "EMI bei Motorantrieben reduzieren: Abschirmung und Ground-Fences mit Via-Abstand, Rückstrompfaden, Keepouts und Validierungstests.",
            "it": "Riduci EMI nei driver motore: schermatura e ground fence con spaziatura via, return path, keepout e test di validazione.",
            "fr": "Réduire l’EMI des motor drives : blindage et ground fences avec pas de vias, chemins de retour, keepouts et tests de validation.",
            "ru": "Снижение EMI в приводах: экранирование и ground‑fence с шагом vias, путями возврата, keepout и тестами валидации.",
            "es": "Reduce EMI en controladores de motor: apantallado y ground fences con espaciado de vías, retorno, keepouts y pruebas de validación.",
            "ar": "تقليل EMI في دوائر قيادة المحركات: التدريع وحواجز التأريض مع تباعد الـvias، مسارات العودة، مناطق المنع، واختبارات التحقق.",
        },
        en_h2_renames={
            "shielding and grounding fences motor PCB: what this playbook covers (and who it’s for)": "What this guide covers (and who it’s for)",
            "When shielding and grounding fences motor PCB is the right approach (and when it isn’t)": "When fences/shielding work (and when they don’t)",
            "Requirements you must define before finalizing the quote": "Specs & requirements (before quoting)",
            "The hidden risks that break scale-up": "Hidden risks (root causes & prevention)",
            "Validation plan (what to test, when, and what “pass” means)": "Validation & acceptance (tests and pass criteria)",
            "Decision guidance (trade-offs you can actually choose)": "Decision guidance (trade-offs you can choose)",
            "Request a quote": "Request a quote (DFM review + pricing)",
            "Conclusion": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="02",
        slug="high-speed-beamforming-module-board",
        titles={
            "en": "High-Speed Beamforming Module Boards: Stackup, SI/PI, and Validation Checklist",
            "de": "High-Speed Beamforming-Module-Boards: Stackup, SI/PI und Validierungs-Checkliste",
            "it": "Schede modulo beamforming high-speed: stackup, SI/PI e checklist di validazione",
            "fr": "Cartes de module beamforming high-speed : stackup, SI/PI et checklist validation",
            "ru": "Платы beamforming‑модуля high‑speed: стек‑ап, SI/PI и чек‑лист валидации",
            "es": "Placas de módulo beamforming high-speed: stackup, SI/PI y checklist de validación",
            "ar": "لوحات Beamforming عالية السرعة: الـStackup وSI/PI وقائمة تحقق للتحقق",
        },
        descriptions={
            "en": "Plan and validate beamforming module boards: high-speed routing, power integrity, thermal/EMI constraints, and acceptance tests.",
            "de": "Beamforming-Boards planen und validieren: High-Speed-Routing, Power-Integrity, Thermik/EMI und Abnahmetests.",
            "it": "Pianifica e valida schede beamforming: routing high-speed, power integrity, vincoli termici/EMI e test di accettazione.",
            "fr": "Planifier et valider des cartes beamforming : routage high-speed, power integrity, contraintes thermique/EMI et tests d’acceptation.",
            "ru": "Планирование и валидация beamforming‑плат: high‑speed трассировка, PI, тепловые/EMI ограничения и приемочные тесты.",
            "es": "Planifica y valida placas beamforming: ruteo high-speed, integridad de potencia, restricciones térmicas/EMI y pruebas de aceptación.",
            "ar": "خطّط وتحقق من لوحات beamforming: توجيه عالي السرعة، سلامة الطاقة، قيود الحرارة/EMI، واختبارات القبول.",
        },
        en_h2_renames={
            "What high-speed Beamforming module board really means (scope & boundaries)": "What “beamforming module board” means (scope & boundaries)",
            "high-speed Beamforming module board metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose high-speed Beamforming module board: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "high-speed Beamforming module board implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "high-speed Beamforming module board common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "high-speed Beamforming module board FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing)",
            "Resources for high-speed Beamforming module board (related pages and tools)": "Related pages & tools",
            "high-speed Beamforming module board glossary (key terms)": "Glossary (key terms)",
            "Conclusion: high-speed Beamforming module board next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="08",
        slug="emib-interconnect-board-validation",
        titles={
            "en": "EMIB Interconnect Boards: Validation Plan, Tests, and Acceptance Criteria",
            "de": "EMIB-Interconnect-Boards: Validierungsplan, Tests und Abnahmekriterien",
            "it": "Schede interconnect EMIB: piano di validazione, test e criteri di accettazione",
            "fr": "Cartes interconnect EMIB : plan de validation, tests et critères d’acceptation",
            "ru": "EMIB interconnect платы: план валидации, тесты и критерии приемки",
            "es": "Placas interconnect EMIB: plan de validación, pruebas y criterios de aceptación",
            "ar": "لوحات EMIB Interconnect: خطة التحقق والاختبارات ومعايير القبول",
        },
        descriptions={
            "en": "A practical validation guide for EMIB interconnect boards: what to test, sample plans, failure analysis, and acceptance reporting.",
            "de": "Praxisleitfaden zur Validierung von EMIB-Boards: was testen, Stichprobenpläne, Failure Analysis und Abnahme-Reporting.",
            "it": "Guida pratica validazione EMIB: cosa testare, piani campionamento, failure analysis e report di accettazione.",
            "fr": "Guide pratique validation EMIB : quoi tester, plans d’échantillonnage, analyse de défaillance et reporting d’acceptation.",
            "ru": "Практический гид по валидации EMIB: что тестировать, планы выборки, анализ отказов и отчетность по приемке.",
            "es": "Guía práctica de validación EMIB: qué probar, planes de muestreo, análisis de fallos e informe de aceptación.",
            "ar": "دليل عملي للتحقق من EMIB: ما الذي تختبره، خطط العيّنات، تحليل الأعطال، وتقارير القبول.",
        },
        en_h2_renames={
            "What EMIB interconnect board validation really means (scope & boundaries)": "What “EMIB validation” means (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="high-speed-mri-compatible-pcb-materials",
        titles={
            "en": "High-Speed MRI-Compatible PCB Materials: Selection, DFM Risks, and Checklist",
            "de": "High-Speed MRI-kompatible PCB-Materialien: Auswahl, DFM-Risiken und Checkliste",
            "it": "Materiali PCB MRI-compatibili high-speed: selezione, rischi DFM e checklist",
            "fr": "Matériaux PCB IRM compatibles high-speed : sélection, risques DFM et checklist",
            "ru": "High‑speed MRI‑совместимые материалы PCB: выбор, риски DFM и чек‑лист",
            "es": "Materiales PCB compatibles con MRI high-speed: selección, riesgos DFM y checklist",
            "ar": "مواد PCB متوافقة مع MRI عالية السرعة: الاختيار ومخاطر DFM وقائمة تحقق",
        },
        descriptions={
            "en": "Select MRI-friendly low-magnetic materials that still meet high-speed SI/PI needs—plus what to validate and document for suppliers.",
            "de": "MRI-freundliche low-magnetische Materialien auswählen und dennoch High-Speed SI/PI erfüllen – plus Validierung und Lieferantendokumentation.",
            "it": "Seleziona materiali low-magnetic MRI-friendly che soddisfino SI/PI high-speed, con validazioni e documentazione per i fornitori.",
            "fr": "Sélectionner des matériaux low-magnetic compatibles IRM tout en respectant SI/PI high-speed, avec validations et documentation fournisseur.",
            "ru": "Выбор low‑magnetic MRI‑совместимых материалов с учетом high‑speed SI/PI, плюс что валидировать и как документировать для поставщика.",
            "es": "Selecciona materiales low-magnetic compatibles con MRI y aptos para SI/PI high-speed, más validación y documentación para proveedores.",
            "ar": "اختر مواد low‑magnetic مناسبة لـMRI وتفي باحتياجات SI/PI عالية السرعة، مع ما يجب التحقق منه وتوثيقه للمورّدين.",
        },
        en_h2_renames={
            "high-speed MRI-compatible PCB materials: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use high-speed MRI-compatible PCB materials (and when a standard approach is better)": "When to use this approach (and when not to)",
            "high-speed MRI-compatible PCB materials specifications (materials, stackup, tolerances)": "Specs to define (materials, stackup, tolerances)",
            "high-speed MRI-compatible PCB materials manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "high-speed MRI-compatible PCB materials validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "high-speed MRI-compatible PCB materials supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose high-speed MRI-compatible PCB materials (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "high-speed MRI-compatible PCB materials FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for high-speed MRI-compatible PCB materials (related pages and tools)": "Related pages & tools",
            "Request a quote for high-speed MRI-compatible PCB materials (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: high-speed MRI-compatible PCB materials next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="data-center-servo-motor-driver-pcb",
        titles={
            "en": "Servo Motor Driver PCB: Power Layout, EMI Control, and Test Checklist",
            "de": "Servo-Motor-Treiber-PCB: Power-Layout, EMI-Kontrolle und Test-Checkliste",
            "it": "PCB driver servo motor: power layout, controllo EMI e checklist test",
            "fr": "PCB driver de servomoteur : power layout, contrôle EMI et checklist de test",
            "ru": "Плата драйвера серводвигателя: силовая разводка, EMI и чек‑лист тестов",
            "es": "PCB de driver de servomotor: layout de potencia, control EMI y checklist de pruebas",
            "ar": "لوحة Driver لمحرك سيرفو: تخطيط القدرة وضبط EMI وقائمة اختبار",
        },
        descriptions={
            "en": "Design reliable servo motor driver boards: current paths, grounding, EMC/EMI pitfalls, and validation tests for production.",
            "de": "Zuverlässige Servo-Driver-Boards: Strompfade, Masseführung, EMC/EMI-Fallstricke und Validierungstests für die Serie.",
            "it": "Schede driver servo affidabili: percorsi di corrente, massa, criticità EMC/EMI e test di validazione per la produzione.",
            "fr": "Cartes driver servo fiables : chemins de courant, masses, pièges EMC/EMI et tests de validation pour production.",
            "ru": "Надежные servo‑driver платы: токовые пути, земля, ловушки EMC/EMI и тесты валидации для серии.",
            "es": "Placas driver de servomotor fiables: rutas de corriente, masa, riesgos EMC/EMI y pruebas de validación para producción.",
            "ar": "لوحات قيادة سيرفو موثوقة: مسارات التيار، التأريض، أخطاء EMC/EMI الشائعة، واختبارات التحقق للإنتاج.",
        },
        en_h2_renames={
            "What data-center Servo motor driver PCB really means (scope & boundaries)": "What “servo motor driver PCB” means (scope & boundaries)",
            "data-center Servo motor driver PCB metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose data-center Servo motor driver PCB: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "data-center Servo motor driver PCB implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "data-center Servo motor driver PCB common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "data-center Servo motor driver PCB FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing)",
            "Resources for data-center Servo motor driver PCB (related pages and tools)": "Related pages & tools",
            "data-center Servo motor driver PCB glossary (key terms)": "Glossary (key terms)",
            "Conclusion: data-center Servo motor driver PCB next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="06",
        slug="three-phase-inverter-control-pcb-design",
        titles={
            "en": "Three-Phase Inverter Control PCB Design: Layout Rules, Isolation, and Test Checklist",
            "de": "3-Phasen-Invertersteuerung-PCB: Layoutregeln, Isolation und Test-Checkliste",
            "it": "PCB controllo inverter trifase: regole layout, isolamento e checklist test",
            "fr": "PCB de contrôle d’onduleur triphasé : règles de layout, isolation et checklist de test",
            "ru": "Плата управления трехфазным инвертором: правила разводки, изоляция и чек‑лист тестов",
            "es": "PCB de control de inversor trifásico: reglas de layout, aislamiento y checklist de pruebas",
            "ar": "PCB للتحكم في عاكس ثلاثي الطور: قواعد التخطيط والعزل وقائمة الاختبار",
        },
        descriptions={
            "en": "A production-minded checklist for inverter control PCBs: isolation/creepage, current sensing, grounding, EMI, and acceptance tests.",
            "de": "Checkliste für Inverter-Control-PCBs: Isolation/Kriechstrecken, Strommessung, Masse, EMI und Abnahmetests.",
            "it": "Checklist per PCB controllo inverter: isolamento/creepage, misura corrente, massa, EMI e test di accettazione.",
            "fr": "Checklist PCB contrôle onduleur : isolation/creepage, mesure de courant, masses, EMI et tests d’acceptation.",
            "ru": "Чек‑лист для плат управления инвертором: изоляция/зазоры, датчики тока, земля, EMI и приемочные тесты.",
            "es": "Checklist para PCB de control de inversor: aislamiento/creepage, sensado de corriente, masa, EMI y pruebas de aceptación.",
            "ar": "قائمة للإنتاج: العزل/مسافات الزحف، قياس التيار، التأريض، EMI، واختبارات القبول للوحات التحكم بالعاكس.",
        },
        en_h2_renames={
            "Three-phase inverter control PCB design: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use Three-phase inverter control PCB design (and when a standard approach is better)": "When to use this approach (and when not to)",
            "Three-phase inverter control PCB design specifications (materials, stackup, tolerances)": "Specs to define (materials, isolation, stackup, tolerances)",
            "Three-phase inverter control PCB design manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "Three-phase inverter control PCB design validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "Three-phase inverter control PCB design supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose Three-phase inverter control PCB design (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "Three-phase inverter control PCB design FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for Three-phase inverter control PCB design (related pages and tools)": "Related pages & tools",
            "Request a quote for Three-phase inverter control PCB design (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: Three-phase inverter control PCB design next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="04",
        slug="sic-mosfet-gate-driver-pcb-testing",
        titles={
            "en": "SiC MOSFET Gate Driver PCB Testing: What to Measure and How to Interpret Results",
            "de": "Testen von SiC-MOSFET-Gate-Driver-PCBs: Messgrößen und Ergebnisinterpretation",
            "it": "Test PCB gate driver SiC MOSFET: cosa misurare e come interpretare i risultati",
            "fr": "Tests de PCB driver de grille SiC MOSFET : quoi mesurer et comment interpréter",
            "ru": "Тестирование PCB драйвера затвора SiC MOSFET: что измерять и как интерпретировать",
            "es": "Pruebas de PCB driver de compuerta SiC MOSFET: qué medir y cómo interpretar resultados",
            "ar": "اختبار PCB لدرايفر بوابة SiC MOSFET: ماذا تقيس وكيف تفسر النتائج",
        },
        descriptions={
            "en": "A practical test guide for SiC gate driver boards: switching waveforms, ringing, dv/dt, isolation checks, and failure troubleshooting.",
            "de": "Praxisleitfaden für SiC-Gate-Driver-Tests: Schaltwellenformen, Ringing, dv/dt, Isolationschecks und Troubleshooting.",
            "it": "Guida pratica test driver SiC: forme d’onda di switching, ringing, dv/dt, controlli isolamento e troubleshooting.",
            "fr": "Guide pratique de test driver SiC : formes d’onde, ringing, dv/dt, vérifications d’isolation et dépannage.",
            "ru": "Практический тест‑гайд: формы переключения, ringing, dv/dt, проверка изоляции и диагностика отказов.",
            "es": "Guía práctica de pruebas: formas de conmutación, ringing, dv/dt, aislamiento y troubleshooting.",
            "ar": "دليل اختبار عملي: موجات التبديل، الرنين (ringing)، ‏dv/dt، فحوصات العزل، واستكشاف الأعطال.",
        },
        en_h2_renames={
            "What SiC MOSFET gate driver PCB testing really means (scope & boundaries)": "What this testing covers (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="03",
        slug="pcba-testing-strategy-aoi-xray-ict-fct",
        titles={
            "en": "PCBA Test Strategy: AOI vs X-Ray vs ICT vs FCT (Coverage + Cost Checklist)",
            "de": "PCBA-Teststrategie: AOI vs Röntgen vs ICT vs FCT (Coverage + Kosten-Checkliste)",
            "it": "Strategia test PCBA: AOI vs X-Ray vs ICT vs FCT (copertura + costi)",
            "fr": "Stratégie de test PCBA : AOI vs X-Ray vs ICT vs FCT (couverture + coûts)",
            "ru": "Стратегия тестирования PCBA: AOI vs X‑Ray vs ICT vs FCT (покрытие + стоимость)",
            "es": "Estrategia de pruebas PCBA: AOI vs Rayos X vs ICT vs FCT (cobertura + coste)",
            "ar": "استراتيجية اختبار PCBA: ‏AOI مقابل X‑Ray مقابل ICT مقابل FCT (التغطية + التكلفة)",
        },
        descriptions={
            "en": "Choose the right mix of AOI, X-ray, ICT, and FCT with a clear coverage model, fixture considerations, and production acceptance criteria.",
            "de": "Die richtige Mischung aus AOI, Röntgen, ICT und FCT: Coverage-Modell, Fixture-Aspekte und Abnahmekriterien für die Serie.",
            "it": "Scegli il mix AOI/X-ray/ICT/FCT con modello di copertura, considerazioni fixture e criteri di accettazione in produzione.",
            "fr": "Choisir le bon mix AOI/X-Ray/ICT/FCT : modèle de couverture, fixtures et critères d’acceptation en production.",
            "ru": "Как выбрать AOI/X‑ray/ICT/FCT: модель покрытия, фикстуры и критерии приемки для серии.",
            "es": "Cómo elegir AOI/Rayos X/ICT/FCT: modelo de cobertura, fixtures y criterios de aceptación para producción.",
            "ar": "كيف تختار مزيج AOI/X‑Ray/ICT/FCT: نموذج تغطية واضح، اعتبارات الـfixture، ومعايير القبول للإنتاج.",
        },
        en_h2_renames={
            "pcba testing strategy: aoi xray ict fct: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use pcba testing strategy: aoi xray ict fct (and when a standard approach is better)": "When to use each test (and when not to)",
            "pcba testing strategy: aoi xray ict fct specifications (materials, stackup, tolerances)": "What to define (coverage, limits, reports, fixtures)",
            "pcba testing strategy: aoi xray ict fct manufacturing risks (root causes and prevention)": "Risks that cause escapes (root causes & prevention)",
            "pcba testing strategy: aoi xray ict fct validation and acceptance (tests and pass criteria)": "Validation & acceptance (pass/fail criteria)",
            "pcba testing strategy: aoi xray ict fct supplier qualification checklist (RFQ, audit, traceability)": "Supplier checklist (RFQ, audit, traceability)",
            "How to choose pcba testing strategy: aoi xray ict fct (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "pcba testing strategy: aoi xray ict fct FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, fixtures, reporting)",
            "Resources for pcba testing strategy: aoi xray ict fct (related pages and tools)": "Related pages & tools",
            "Request a quote for pcba testing strategy: aoi xray ict fct (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: pcba testing strategy: aoi xray ict fct next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="fixture-design-for-emc-validation",
        titles={
            "en": "EMC Validation Fixture Design: Grounding, Cables, and Repeatability Checklist",
            "de": "Fixturendesign für EMC-Validierung: Masse, Kabel und Reproduzierbarkeits-Checkliste",
            "it": "Design fixture per validazione EMC: massa, cavi e checklist ripetibilità",
            "fr": "Design de fixtures pour validation CEM : masses, câbles et checklist de répétabilité",
            "ru": "Конструкция фикстур для EMC‑валидации: земля, кабели и чек‑лист повторяемости",
            "es": "Diseño de fixtures para validación EMC: masa, cables y checklist de repetibilidad",
            "ar": "تصميم Fixture للتحقق من EMC: التأريض، الكابلات، وقائمة قابلية التكرار",
        },
        descriptions={
            "en": "Design EMC fixtures that produce repeatable results: grounding, cable management, connectors, and how to avoid measurement artifacts.",
            "de": "EMC-Fixturen für reproduzierbare Ergebnisse: Masse, Kabelmanagement, Connectoren und wie man Messartefakte vermeidet.",
            "it": "Fixture EMC ripetibili: massa, gestione cavi, connettori e come evitare artefatti di misura.",
            "fr": "Fixtures CEM reproductibles : masses, gestion des câbles, connecteurs et éviter les artefacts de mesure.",
            "ru": "Фикстуры для повторяемых EMC результатов: земля, кабели, коннекторы и как избежать артефактов измерения.",
            "es": "Fixtures EMC repetibles: masa, gestión de cables, conectores y cómo evitar artefactos de medición.",
            "ar": "صمّم fixture يعطي نتائج ثابتة: التأريض، إدارة الكابلات، الموصلات، وكيف تتجنب شوائب القياس (artifacts).",
        },
        en_h2_renames={
            "What fixture design for EMC validation really means (scope & boundaries)": "What “EMC fixture design” means (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="board-handling-and-depanelization",
        titles={
            "en": "Board Handling & Depanelization: Prevent Cracks, Delamination, and Scrap",
            "de": "Board-Handling & Depanelisierung: Risse, Delamination und Ausschuss vermeiden",
            "it": "Handling schede e depanelizzazione: prevenire crepe, delaminazione e scarti",
            "fr": "Manipulation et dépanelisation : prévenir fissures, délamination et rebuts",
            "ru": "Обращение с платами и депанелизация: как предотвратить трещины, деламинацию и брак",
            "es": "Manejo de placas y depanelización: evita grietas, delaminación y desperdicio",
            "ar": "التعامل مع اللوحات وفصلها (Depanelization): تجنّب التشققات والديلاميناشن والهدر",
        },
        descriptions={
            "en": "A practical guide to safe handling and depanelization: tooling, support, scoring/tab rules, and how to reduce hidden damage.",
            "de": "Praxisleitfaden für Handling und Depanelisierung: Werkzeug, Unterstützung, V‑Cut/Tab‑Regeln und versteckte Schäden reduzieren.",
            "it": "Guida pratica a handling e depanelizzazione: tooling, supporto, regole V‑cut/tab e come ridurre danni nascosti.",
            "fr": "Guide pratique manipulation/dépanelisation : outillage, support, règles V‑cut/tabs et réduction des dommages cachés.",
            "ru": "Практическое руководство: оснастка, поддержка, правила V‑cut/tab и снижение скрытых повреждений.",
            "es": "Guía práctica: tooling, soporte, reglas de V‑cut/tabs y cómo reducir daño oculto en depanelización.",
            "ar": "دليل عملي: الأدوات والدعم، قواعد V‑cut/tabs، وكيف تقلّل الضرر الخفي أثناء depanelization.",
        },
        en_h2_renames={
            "What board handling and depanelization really means (scope & boundaries)": "What “handling & depanelization” means (scope & boundaries)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="gan-power-stage-pcb-impedance-control",
        titles={
            "en": "GaN Power Stage Impedance Control: Layout Rules, Stackup, and Acceptance Tests",
            "de": "Impedanzkontrolle in GaN-Power-Stages: Layoutregeln, Stackup und Abnahmetests",
            "it": "Controllo impedenza power stage GaN: regole layout, stackup e test di accettazione",
            "fr": "Contrôle d’impédance pour power stages GaN : règles de layout, stackup et tests d’acceptation",
            "ru": "Контроль импеданса GaN power stage: правила разводки, стек‑ап и приемочные тесты",
            "es": "Control de impedancia en power stage GaN: reglas de layout, stackup y pruebas de aceptación",
            "ar": "التحكم في ممانعة GaN Power Stage: قواعد التخطيط والـStackup واختبارات القبول",
        },
        descriptions={
            "en": "Control impedance and switching behavior in GaN power stages: stackup choices, loop inductance, measurement, and production acceptance.",
            "de": "Impedanz und Schaltverhalten bei GaN-Power-Stages kontrollieren: Stackup, Schleifeninduktivität, Messung und Serienabnahme.",
            "it": "Controlla impedenza e switching nei GaN power stage: scelte stackup, induttanza loop, misure e accettazione in produzione.",
            "fr": "Maîtriser l’impédance et le switching des power stages GaN : choix stackup, inductance de boucle, mesure et acceptation production.",
            "ru": "Контроль импеданса и переключения GaN: стек‑ап, индуктивность контуров, измерения и приемка в серии.",
            "es": "Controla impedancia y conmutación en GaN: stackup, inductancia de lazo, medición y aceptación en producción.",
            "ar": "اضبط الممانعة وسلوك التبديل في GaN: خيارات الـstackup، حث الحلقة، القياس، ومعايير القبول للإنتاج.",
        },
        en_h2_renames={
            "GaN power stage PCB impedance control: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use GaN power stage PCB impedance control (and when a standard approach is better)": "When to use this approach (and when not to)",
            "GaN power stage PCB impedance control specifications (materials, stackup, tolerances)": "Specs to define (materials, stackup, tolerances)",
            "GaN power stage PCB impedance control manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "GaN power stage PCB impedance control validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "GaN power stage PCB impedance control supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose GaN power stage PCB impedance control (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "GaN power stage PCB impedance control FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for GaN power stage PCB impedance control (related pages and tools)": "Related pages & tools",
            "Request a quote for GaN power stage PCB impedance control (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: GaN power stage PCB impedance control next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="automotive-grade-on-board-charger-pcb",
        titles={
            "en": "Automotive On-Board Charger PCB: Isolation, Thermal, and Production Checklist",
            "de": "Automotive On-Board-Charger-PCB: Isolation, Thermik und Produktions-Checkliste",
            "it": "PCB caricabatterie di bordo automotive: isolamento, termica e checklist produzione",
            "fr": "PCB chargeur embarqué automotive : isolation, thermique et checklist production",
            "ru": "Плата on‑board charger automotive: изоляция, тепловой дизайн и чек‑лист для серии",
            "es": "PCB de cargador a bordo automotive: aislamiento, térmica y checklist de producción",
            "ar": "PCB لشاحن على متن السيارة (OBC): العزل والحرارة وقائمة تحقق للإنتاج",
        },
        descriptions={
            "en": "Take an OBC PCB to production: creepage/clearance, thermal paths, EMC/EMI design, and acceptance tests with supplier deliverables.",
            "de": "OBC-PCB in die Serie bringen: Kriech-/Luftstrecken, Wärmeableitung, EMC/EMI-Design und Abnahmetests mit Lieferantendokumenten.",
            "it": "Porta un PCB OBC in produzione: creepage/clearance, percorsi termici, EMC/EMI e test di accettazione con deliverable fornitore.",
            "fr": "Industrialiser un PCB OBC : creepage/clearance, chemins thermiques, conception EMC/EMI et tests d’acceptation avec livrables fournisseur.",
            "ru": "Вывод OBC платы в серию: изоляционные расстояния, тепловые пути, EMC/EMI и приемочные тесты с отчетностью поставщика.",
            "es": "Lleva un PCB de OBC a producción: creepage/clearance, rutas térmicas, diseño EMC/EMI y pruebas de aceptación con entregables del proveedor.",
            "ar": "تحويل PCB الخاص بـOBC إلى إنتاج: مسافات الزحف/التفريغ، مسارات الحرارة، تصميم EMC/EMI، واختبارات قبول مع مخرجات المورّد.",
        },
        en_h2_renames={
            "automotive-grade On-board charger PCB: definition, scope, and who this guide is for": "Definition, scope, and who this guide is for",
            "When to use automotive-grade On-board charger PCB (and when a standard approach is better)": "When to use this approach (and when not to)",
            "automotive-grade On-board charger PCB specifications (materials, stackup, tolerances)": "Specs to define (materials, isolation, stackup, tolerances)",
            "automotive-grade On-board charger PCB manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "automotive-grade On-board charger PCB validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "automotive-grade On-board charger PCB supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose automotive-grade On-board charger PCB (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "automotive-grade On-board charger PCB FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, testing)",
            "Resources for automotive-grade On-board charger PCB (related pages and tools)": "Related pages & tools",
            "Request a quote for automotive-grade On-board charger PCB (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: automotive-grade On-board charger PCB next steps": "Conclusion (next steps)",
        },
    ),
]


def _yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _wrap_description(text: str) -> str:
    return "\n".join(
        textwrap.wrap(text.strip(), width=78, break_long_words=False, break_on_hyphens=False)
    )


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    fm_without_end = parts[0]  # includes opening ---
    body = parts[1]
    return fm_without_end, body


def _update_frontmatter(fm_text: str, *, title: str, description: str) -> str:
    lines = fm_text.splitlines()
    out: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^title:\s*", line):
            out.append(f"title: {_yaml_single_quote(title)}")
            i += 1
            continue

        if re.match(r"^description:\s*", line):
            out.append("description: >-")
            for wline in _wrap_description(description).splitlines():
                out.append(f"  {wline}")
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                i += 1
            continue

        out.append(line)
        i += 1

    if not any(l.startswith("title:") for l in out):
        out.insert(1, f"title: {_yaml_single_quote(title)}")

    if not any(l.startswith("description:") for l in out):
        insert_at = 2
        out.insert(insert_at, "description: >-")
        for wline in _wrap_description(description).splitlines():
            insert_at += 1
            out.insert(insert_at, f"  {wline}")

    return "\n".join(out) + "\n"


def _ensure_h1(body: str, title: str) -> str:
    stripped = body.lstrip("\n")
    m = re.match(r"^(#\s+.*)\n", stripped)
    if m:
        rest = stripped[m.end() :]
        return f"# {title}\n\n{rest.lstrip()}"
    return f"# {title}\n\n{stripped}"


def _rename_en_h2(body: str, renames: dict[str, str]) -> str:
    if not renames:
        return body
    out_lines: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            h = m.group(1)
            if h in renames:
                out_lines.append(f"## {renames[h]}")
                continue
        out_lines.append(line)
    return "\n".join(out_lines) + ("\n" if body.endswith("\n") else "")


def main() -> int:
    changed = 0
    missing = 0

    for post in POSTS:
        for locale in TARGET_LOCALES:
            title = post.titles.get(locale)
            desc = post.descriptions.get(locale)
            if not title or not desc:
                continue
            md_path = BLOGS_ROOT / post.year / post.month / locale / f"{post.slug}.md"
            if not md_path.exists():
                missing += 1
                print(f"missing: {md_path}")
                continue

            raw = md_path.read_text(encoding="utf-8", errors="ignore")
            parts = _split_frontmatter(raw)
            if not parts:
                print(f"skip(no-frontmatter): {md_path}")
                continue
            fm_without_end, body = parts

            fm_updated = _update_frontmatter(fm_without_end, title=title, description=desc)
            body_updated = _ensure_h1(body, title)
            if locale == "en":
                body_updated = _rename_en_h2(body_updated, post.en_h2_renames)

            new_text = fm_updated + "---\n" + body_updated.lstrip("\n")
            if new_text != raw:
                md_path.write_text(new_text, encoding="utf-8")
                changed += 1

    print(f"updated_files={changed} missing_files={missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

