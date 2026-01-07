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
        month="03",
        slug="flex-pcb-teardrop-and-pad-anchoring-best-practices",
        titles={
            "en": "Flex PCB Teardrops & Pad Anchoring: Design Rules, When to Use, and Checklist",
            "de": "Flex-PCB-Teardrops & Pad-Verankerung: Designregeln, Einsatzfälle und Checkliste",
            "it": "Teardrop e ancoraggio pad su Flex PCB: regole di design, quando usarli e checklist",
            "fr": "Teardrops et ancrage de pads sur Flex PCB : règles, cas d’usage et checklist",
            "ru": "Teardrop и анкеровка площадок в Flex PCB: правила, когда применять и чек‑лист",
            "es": "Teardrops y anclaje de pads en Flex PCB: reglas, cuándo usarlos y checklist",
            "ar": "Teardrop وتثبيت البادات في Flex PCB: قواعد التصميم ومتى تستخدمها وقائمة تحقق",
        },
        descriptions={
            "en": "Learn when flex PCB teardrops and pad anchoring prevent pad lifting and trace cracks, what to specify to your fab, and how to validate reliability.",
            "de": "Wann Flex-PCB-Teardrops und Pad-Verankerungen Pad-Lifting und Leiterbahnbrüche verhindern, was Sie beim Hersteller spezifizieren und wie Sie die Zuverlässigkeit validieren.",
            "it": "Quando teardrop e ancoraggi pad su Flex PCB evitano sollevamento pad e cricche, cosa specificare al produttore e come validare l’affidabilità.",
            "fr": "Quand les teardrops et l’ancrage de pads sur flex PCB évitent le décollement et les fissures, quoi spécifier au fabricant et comment valider la fiabilité.",
            "ru": "Когда teardrop и анкеровка площадок на гибких платах предотвращают отрыв пятака и трещины дорожек, что задать производителю и как валидировать надежность.",
            "es": "Cuándo los teardrops y el anclaje de pads en flex PCB evitan levantamiento de pads y grietas, qué especificar al fabricante y cómo validar la fiabilidad.",
            "ar": "متى تمنع teardrop وتثبيت البادات في لوحات الـFlex PCB رفع الباد وتشققات المسارات، وما الذي يجب تحديده للمصنع وكيف تتحقق من الاعتمادية.",
        },
        en_h2_renames={
            "flex pcb teardrop and pad anchoring best practices: what this playbook covers (and who it’s for)": "What this guide covers (and who it’s for)",
            "When flex pcb teardrop and pad anchoring best practices is the right approach (and when it isn’t)": "When to use teardrops and pad anchoring (and when not to)",
            "Requirements you must define before quoting": "Specs & requirements (before quoting)",
            "The hidden risks that break scale-up": "Manufacturing risks (root causes & prevention)",
            "Validation plan (what to test, when, and what “pass” means)": "Validation & acceptance (tests and pass criteria)",
            "Decision guidance (trade-offs you can actually choose)": "Decision guidance (trade-offs you can choose)",
            "Conclusion": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="08",
        slug="wellness-device-fcc-compliance-pcb",
        titles={
            "en": "FCC Compliance for Wellness Devices: PCB Design, Pre-Scan, and Production Checklist",
            "de": "FCC-Compliance für Wellness-Geräte: PCB-Layout, Pre-Scan und Produktions-Checkliste",
            "it": "Conformità FCC per dispositivi wellness: design PCB, pre-scan e checklist di produzione",
            "fr": "Conformité FCC pour appareils wellness : design PCB, pré-scan et checklist de production",
            "ru": "Соответствие FCC для wellness‑устройств: дизайн PCB, pre‑scan и чек‑лист производства",
            "es": "Cumplimiento FCC para dispositivos wellness: diseño PCB, pre-scan y checklist de producción",
            "ar": "الامتثال لـ FCC لأجهزة الـWellness: تصميم PCB وpre-scan وقائمة إنتاج",
        },
        descriptions={
            "en": "A practical guide to passing FCC for wellness devices: PCB layout choices, grounding/shielding, pre-scan steps, and what to lock before mass production.",
            "de": "Praxisleitfaden für FCC bei Wellness-Geräten: PCB-Layout, Masseführung/Abschirmung, Pre-Scan-Schritte und was vor der Serienfertigung fixiert sein muss.",
            "it": "Guida pratica per superare FCC: scelte di layout PCB, massa/schermatura, passi di pre-scan e cosa bloccare prima della produzione in serie.",
            "fr": "Guide pratique pour réussir la FCC : choix de layout PCB, masses/blindage, étapes de pré-scan et points à verrouiller avant la production.",
            "ru": "Практический гид по FCC: решения по компоновке PCB, земля/экранирование, шаги pre‑scan и что зафиксировать перед серийным выпуском.",
            "es": "Guía práctica para pasar FCC: decisiones de layout PCB, masa/apantallamiento, pasos de pre-scan y qué cerrar antes de producción.",
            "ar": "دليل عملي لاجتياز FCC: قرارات تخطيط PCB، التأريض/التدريع، خطوات pre-scan، وما الذي يجب تثبيته قبل الإنتاج الكمي.",
        },
        en_h2_renames={
            "What wellness device fcc compliance pcb really means (scope & boundaries)": "What FCC compliance means for wellness devices (scope & boundaries)",
            "Selection guidance by scenario (trade-offs)": "Design choices by scenario (trade-offs)",
            "From design to manufacturing (implementation checkpoints)": "Implementation checkpoints (design to manufacturing)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="06",
        slug="rigid-flex-impedance-control-and-stackup-planning",
        titles={
            "en": "Rigid-Flex Impedance Control & Stackup Planning: Rules, Tolerances, and DFM Checklist",
            "de": "Impedanzkontrolle & Stackup-Planung bei Starrflex: Regeln, Toleranzen und DFM-Checkliste",
            "it": "Controllo d’impedenza e pianificazione stackup rigid-flex: regole, tolleranze e checklist DFM",
            "fr": "Contrôle d’impédance et planification de stackup rigid-flex : règles, tolérances et checklist DFM",
            "ru": "Контроль импеданса и планирование стек‑апа rigid‑flex: правила, допуски и DFM‑чек‑лист",
            "es": "Control de impedancia y planificación de stackup en rigid-flex: reglas, tolerancias y checklist DFM",
            "ar": "التحكم في الممانعة وتخطيط الـStackup في Rigid‑Flex: القواعد والتسامحات وقائمة DFM",
        },
        descriptions={
            "en": "Plan controlled-impedance rigid-flex boards with the right materials, stackup, and tolerances—plus manufacturing risks and validation tests.",
            "de": "So planen Sie kontrollierte Impedanz in Starrflex: Materialien, Stackup und Toleranzen – plus Fertigungsrisiken und Validierungstests.",
            "it": "Pianifica rigid-flex a impedenza controllata con materiali, stackup e tolleranze giuste, più rischi di produzione e test di validazione.",
            "fr": "Planifiez des rigid-flex à impédance contrôlée : matériaux, stackup et tolérances, avec risques de fabrication et tests de validation.",
            "ru": "Как спланировать rigid‑flex с контролируемым импедансом: материалы, стек‑ап и допуски, а также риски производства и тесты приемки.",
            "es": "Planifica placas rigid-flex con impedancia controlada: materiales, stackup y tolerancias, además de riesgos de fabricación y pruebas de validación.",
            "ar": "خطّط لوحات rigid‑flex بممانعة مضبوطة عبر اختيار المواد والـstackup والتسامحات، مع مخاطر التصنيع وخطة اختبار/قبول.",
        },
        en_h2_renames={
            "rigid flex impedance control and stackup planning: definition, scope, and who this guide is for": "Rigid-flex impedance control: definition, scope, and who this guide is for",
            "When to use rigid flex impedance control and stackup planning (and when a standard approach is better)": "When to use controlled impedance in rigid-flex (and when not to)",
            "rigid flex impedance control and stackup planning specifications (materials, stackup, tolerances)": "Specs to define (materials, stackup, tolerances)",
            "rigid flex impedance control and stackup planning manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "rigid flex impedance control and stackup planning validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "rigid flex impedance control and stackup planning supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose rigid flex impedance control and stackup planning (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "rigid flex impedance control and stackup planning FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, materials, testing)",
            "Resources for rigid flex impedance control and stackup planning (related pages and tools)": "Related pages & tools",
            "Request a quote for rigid flex impedance control and stackup planning (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: rigid flex impedance control and stackup planning next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="08",
        slug="mt-ferrule-connector-interface-impedance-control",
        titles={
            "en": "MT Ferrule Interface Impedance Control: PCB Layout Rules and Measurement Plan",
            "de": "Impedanzkontrolle an MT-Ferrule-Schnittstellen: Layout-Regeln und Messplan",
            "it": "Controllo d’impedenza all’interfaccia MT ferrule: regole di layout PCB e piano di misura",
            "fr": "Contrôle d’impédance à l’interface MT ferrule : règles de layout PCB et plan de mesure",
            "ru": "Контроль импеданса на интерфейсе MT ferrule: правила разводки PCB и план измерений",
            "es": "Control de impedancia en la interfaz MT ferrule: reglas de layout PCB y plan de medición",
            "ar": "التحكم في الممانعة عند واجهة MT Ferrule: قواعد تخطيط PCB وخطة القياس",
        },
        descriptions={
            "en": "Control impedance at MT ferrule/connector interfaces with the right geometry, materials, transitions, and a practical measurement/validation plan.",
            "de": "Wie Sie die Impedanz an MT-Ferrule/Connector-Übergängen steuern: Geometrie, Materialien, Übergänge sowie Mess- und Validierungsplan.",
            "it": "Come controllare l’impedenza alle interfacce MT ferrule/connettore: geometrie, materiali, transizioni e piano pratico di misura/validazione.",
            "fr": "Contrôler l’impédance aux interfaces MT ferrule/connecteur : géométries, matériaux, transitions et plan de mesure/validation.",
            "ru": "Как контролировать импеданс в переходах MT ferrule/коннектор: геометрия, материалы, переходы и практический план измерений/валидации.",
            "es": "Cómo controlar la impedancia en interfaces MT ferrule/conector: geometría, materiales, transiciones y un plan práctico de medición/validación.",
            "ar": "كيفية ضبط الممانعة في واجهات MT ferrule/الموصل: الهندسة والمواد والانتقالات وخطة عملية للقياس والتحقق.",
        },
        en_h2_renames={
            "What MT ferrule connector interface impedance control really means (scope & boundaries)": "What impedance control means at MT ferrule interfaces (scope & boundaries)",
            "MT ferrule connector interface impedance control metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose MT ferrule connector interface impedance control: selection guidance by scenario (trade-offs)": "How to choose an approach (trade-offs by scenario)",
            "MT ferrule connector interface impedance control implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "MT ferrule connector interface impedance control common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "MT ferrule connector interface impedance control FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing, acceptance criteria)",
            "Resources for MT ferrule connector interface impedance control (related pages and tools)": "Related pages & tools",
            "Conclusion: MT ferrule connector interface impedance control next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="industrial-grade-igbt-gan-driver-board",
        titles={
            "en": "IGBT/GaN Driver Board Layout: Isolation, Gate Loop, EMI, and Debug Checklist",
            "de": "Layout für IGBT/GaN-Treiberplatinen: Isolation, Gate-Loop, EMI und Debug-Checkliste",
            "it": "Layout scheda driver IGBT/GaN: isolamento, gate loop, EMI e checklist di debug",
            "fr": "Layout d’une carte driver IGBT/GaN : isolation, boucle de gate, EMI et checklist de debug",
            "ru": "Разводка платы драйвера IGBT/GaN: изоляция, gate‑loop, EMI и чек‑лист отладки",
            "es": "Layout de placa driver IGBT/GaN: aislamiento, bucle de puerta, EMI y checklist de depuración",
            "ar": "تخطيط لوحة قيادة IGBT/GaN: العزل وحلقة البوابة وEMI وقائمة تحقق للتصحيح",
        },
        descriptions={
            "en": "Design an industrial IGBT/GaN driver PCB with low-inductance gate loops, robust isolation/creepage, EMI control, and troubleshooting steps.",
            "de": "Entwerfen Sie industrielle IGBT/GaN-Treiber-PCBs: geringe Gate-Schleifeninduktivität, Isolation/Kriechstrecken, EMI-Kontrolle und Troubleshooting.",
            "it": "Progetta PCB driver IGBT/GaN industriali: loop di gate a bassa induttanza, isolamento/creepage, controllo EMI e troubleshooting.",
            "fr": "Concevez un PCB driver IGBT/GaN industriel : boucle de gate faible inductance, isolation/creepage, maîtrise EMI et dépannage.",
            "ru": "Проектирование PCB драйвера IGBT/GaN: минимальная индуктивность gate‑loop, изоляция/критические расстояния, EMI и шаги диагностики.",
            "es": "Diseña un PCB driver IGBT/GaN industrial: bucle de puerta de baja inductancia, aislamiento/creepage, control EMI y troubleshooting.",
            "ar": "صمّم PCB لدارة قيادة IGBT/GaN صناعية: حلقة بوابة منخفضة الحث، عزل ومسافات زحف/تفريغ، ضبط EMI وخطوات استكشاف الأعطال.",
        },
        en_h2_renames={
            "When industrial-grade IGBT/GaN driver board applies (and when it doesn’t)": "When this driver-board approach applies (and when it doesn’t)",
            "Rules & specifications": "Layout rules & specifications",
            "Implementation steps": "Implementation steps (layout to build)",
            "Conclusion": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="02",
        slug="how-to-design-test-points-for-ict-on-dense-pcbs",
        titles={
            "en": "ICT Test Points on Dense PCBs: Size, Spacing, Accessibility, and Fixture Tips",
            "de": "ICT-Testpunkte auf dichten PCBs: Größe, Abstand, Zugänglichkeit und Fixture-Tipps",
            "it": "Test point ICT su PCB dense: dimensioni, spaziatura, accessibilità e consigli per la fixture",
            "fr": "Points de test ICT sur PCB denses : taille, espacement, accessibilité et conseils de fixture",
            "ru": "Тест‑пойнты для ICT на плотных PCB: размер, шаг, доступ и советы по фикстуре",
            "es": "Puntos de prueba para ICT en PCB densas: tamaño, separación, acceso y consejos de fixture",
            "ar": "نقاط اختبار ICT على PCB كثيفة: المقاس والتباعد وإمكانية الوصول ونصائح للفكستشر",
        },
        descriptions={
            "en": "A DFT guide for ICT on dense boards: test-point rules, spacing/keepouts, probe access, and how to reduce fixture cost without losing coverage.",
            "de": "DFT-Leitfaden für ICT auf dichten Platinen: Testpunktregeln, Abstände/Keepouts, Probe-Zugang und wie Sie Fixture-Kosten senken ohne Coverage zu verlieren.",
            "it": "Guida DFT per ICT su schede dense: regole test point, spaziature/keepout, accesso sonde e come ridurre il costo fixture senza perdere copertura.",
            "fr": "Guide DFT pour l’ICT sur cartes denses : règles de points de test, espacements/keepouts, accès sondes et réduction du coût de fixture sans perdre la couverture.",
            "ru": "DFT‑гайд для ICT: правила тест‑пойнтов, расстояния/keepout, доступ щупов и как снизить стоимость фикстуры без потери покрытия.",
            "es": "Guía DFT para ICT: reglas de test points, separación/keepouts, acceso de sondas y cómo bajar el coste de la fixture sin perder cobertura.",
            "ar": "دليل DFT لاختبار ICT على لوحات كثيفة: قواعد نقاط الاختبار، التباعد/مناطق المنع، وصول المجسات، وتقليل تكلفة الـfixture دون فقد التغطية.",
        },
        en_h2_renames={
            "What how to design test points for ict on dense pcbs really means (scope & boundaries)": "What ICT test-point design means on dense PCBs (scope & boundaries)",
            "how to design test points for ict on dense pcbs metrics that matter (how to evaluate quality)": "Metrics that matter (coverage, access, and cost)",
            "How to choose how to design test points for ict on dense pcbs: selection guidance by scenario (trade-offs)": "How to choose test-point strategy (trade-offs)",
            "how to design test points for ict on dense pcbs implementation checkpoints (design to manufacturing)": "Implementation checkpoints (layout to fixture)",
            "how to design test points for ict on dense pcbs common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "how to design test points for ict on dense pcbs FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (fixture cost, lead time, probe sizes, coverage)",
            "Resources for how to design test points for ict on dense pcbs (related pages and tools)": "Related pages & tools",
            "how to design test points for ict on dense pcbs glossary (key terms)": "Glossary (key terms)",
            "Conclusion: how to design test points for ict on dense pcbs next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="rf-front-end-low-noise-pcb-low-volume",
        titles={
            "en": "Low-Noise RF Front-End PCBs (Low Volume): Layout Rules, Materials, and Test Plan",
            "de": "Low-Noise RF-Front-End-PCBs (Kleinserie): Layout-Regeln, Materialien und Testplan",
            "it": "PCB RF front-end a basso rumore (bassi volumi): regole di layout, materiali e piano test",
            "fr": "PCB RF front-end faible bruit (petites séries) : règles de layout, matériaux et plan de test",
            "ru": "Низкошумные PCB RF фронт‑энда (малые серии): правила разводки, материалы и план тестов",
            "es": "PCB de front-end RF de bajo ruido (bajo volumen): reglas de layout, materiales y plan de pruebas",
            "ar": "لوحات PCB لواجهة RF منخفضة الضجيج (إنتاج منخفض): قواعد التخطيط والمواد وخطة الاختبار",
        },
        descriptions={
            "en": "Build low-noise RF front-end PCBs in low volume with the right stackup, grounding, via fences, and a practical validation checklist.",
            "de": "Low-Noise RF-Front-End-PCBs in kleinen Stückzahlen: passender Stackup, Masseführung, Via-Fences und eine praktische Validierungs-Checkliste.",
            "it": "Realizza PCB RF front-end low noise in piccoli lotti: stackup, massa, via fence e checklist pratica di validazione.",
            "fr": "Produire des PCB RF front-end low-noise en faible volume : stackup, masses, via fences et checklist de validation.",
            "ru": "Как делать низкошумные PCB RF фронт‑энда в малом объеме: стек‑ап, земля, via‑fence и практический чек‑лист валидации.",
            "es": "Fabrica PCB RF low-noise en bajo volumen: stackup, masa, vallas de vías y checklist práctica de validación.",
            "ar": "أنشئ PCB لواجهة RF منخفضة الضجيج بكميات صغيرة عبر اختيار stackup مناسب وتأريض جيد وحواجز vias وخطة تحقق عملية.",
        },
        en_h2_renames={
            "What RF front-end low noise PCB low volume really means (scope & boundaries)": "What “low-noise RF front-end PCB” means (scope & boundaries)",
            "RF front-end low noise PCB low volume metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose RF front-end low noise PCB low volume: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "RF front-end low noise PCB low volume implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "RF front-end low noise PCB low volume common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "RF front-end low noise PCB low volume FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing, acceptance criteria)",
            "Resources for RF front-end low noise PCB low volume (related pages and tools)": "Related pages & tools",
            "RF front-end low noise PCB low volume glossary (key terms)": "Glossary (key terms)",
            "Conclusion: RF front-end low noise PCB low volume next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="dual-channel-safety-control-pcb-mass-production",
        titles={
            "en": "Dual-Channel Safety Control PCB (Mass Production): Architecture, DFM, and Test Checklist",
            "de": "Dual-Channel Safety-Control-PCB (Serienfertigung): Architektur, DFM und Test-Checkliste",
            "it": "PCB di controllo safety a doppio canale (produzione): architettura, DFM e checklist di test",
            "fr": "PCB de contrôle safety double canal (production) : architecture, DFM et checklist de test",
            "ru": "Плата safety‑контроля с двумя каналами (серия): архитектура, DFM и чек‑лист тестов",
            "es": "PCB de control safety de doble canal (producción): arquitectura, DFM y checklist de pruebas",
            "ar": "لوحة تحكم أمان ثنائية القناة (إنتاج كمي): البنية وDFM وقائمة تحقق للاختبار",
        },
        descriptions={
            "en": "Take a dual-channel safety control board to mass production: redundancy rules, isolation, manufacturing risks, and acceptance tests.",
            "de": "Dual-Channel Safety-Control in Serie: Redundanzregeln, Isolation, Fertigungsrisiken und Abnahmeprüfungen.",
            "it": "Porta una scheda safety dual-channel in produzione: regole di ridondanza, isolamento, rischi di fabbricazione e test di accettazione.",
            "fr": "Industrialiser un contrôle safety double canal : règles de redondance, isolation, risques de fabrication et tests d’acceptation.",
            "ru": "Вывод dual‑channel safety control в серию: правила резервирования, изоляция, риски производства и приемочные испытания.",
            "es": "Lleva un control safety dual-channel a producción: reglas de redundancia, aislamiento, riesgos de fabricación y pruebas de aceptación.",
            "ar": "تحويل لوحة تحكم أمان ثنائية القناة إلى إنتاج كمي: قواعد التكرار، العزل، مخاطر التصنيع، واختبارات القبول.",
        },
        en_h2_renames={
            "Dual-channel safety control PCB mass production: definition, scope, and who this guide is for": "Dual-channel safety control PCB: definition, scope, and who this guide is for",
            "When to use Dual-channel safety control PCB mass production (and when a standard approach is better)": "When to use a dual-channel safety architecture (and when not to)",
            "Dual-channel safety control PCB mass production specifications (materials, stackup, tolerances)": "Specs to define (materials, isolation, stackup, tolerances)",
            "Dual-channel safety control PCB mass production manufacturing risks (root causes and prevention)": "Manufacturing risks (root causes & prevention)",
            "Dual-channel safety control PCB mass production validation and acceptance (tests and pass criteria)": "Validation & acceptance (tests and pass criteria)",
            "Dual-channel safety control PCB mass production supplier qualification checklist (RFQ, audit, traceability)": "Supplier qualification checklist (RFQ, audit, traceability)",
            "How to choose Dual-channel safety control PCB mass production (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "Dual-channel safety control PCB mass production FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (cost, lead time, DFM files, materials, testing)",
            "Resources for Dual-channel safety control PCB mass production (related pages and tools)": "Related pages & tools",
            "Request a quote for Dual-channel safety control PCB mass production (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: Dual-channel safety control PCB mass production next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="06",
        slug="fpc-panelization-and-carriers",
        titles={
            "en": "FPC Panelization & Carriers: Rail Design, Tooling Holes, and Assembly Checklist",
            "de": "FPC-Nutzen & Carrier: Rails, Werkzeugbohrungen und Bestückungs-Checkliste",
            "it": "Panelizzazione FPC e carrier: rail, fori di tooling e checklist di assemblaggio",
            "fr": "Panelisation FPC et carriers : rails, trous de tooling et checklist d’assemblage",
            "ru": "Панелизация FPC и карьеры: рейлы, tooling‑отверстия и чек‑лист сборки",
            "es": "Panelización de FPC y carriers: rails, taladros de tooling y checklist de ensamblaje",
            "ar": "تجميع (Panelization) الـFPC وحوامل النقل: تصميم القضبان وثقوب التثبيت وقائمة التجميع",
        },
        descriptions={
            "en": "A practical guide to panelizing FPCs: carriers/rails, breakaway design, tooling features, and how to protect SMT yield.",
            "de": "Praxisleitfaden für FPC-Nutzen: Carrier/Rails, Breakaway-Design, Tooling-Features und wie Sie SMT-Yield schützen.",
            "it": "Guida pratica alla panelizzazione FPC: carrier/rail, breakaway, feature di tooling e come proteggere la resa SMT.",
            "fr": "Guide pratique de panelisation FPC : carriers/rails, breakaway, fonctionnalités de tooling et protection du rendement SMT.",
            "ru": "Практическое руководство по панелизации FPC: carriers/рейлы, отрывные перемычки, tooling‑элементы и как сохранить выходность SMT.",
            "es": "Guía práctica para panelizar FPC: carriers/rails, diseño de separación, features de tooling y cómo proteger el rendimiento en SMT.",
            "ar": "دليل عملي لعمل panelization لـFPC: الحوامل/القضبان، تصميم الفصل، ميزات tooling، وكيف تحمي عائد SMT.",
        },
        en_h2_renames={
            "What FPC panelization and carriers really means (scope & boundaries)": "What FPC panelization and carriers mean (scope & boundaries)",
            "Selection guidance by scenario (trade-offs)": "Panelization options by scenario (trade-offs)",
            "From design to manufacturing (implementation checkpoints)": "Implementation checkpoints (design to manufacturing)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="11",
        slug="coverlay-vs-solder-mask-on-fpc",
        titles={
            "en": "Coverlay vs Solder Mask on FPC: When to Use Each and How to Specify Openings",
            "de": "Coverlay vs Lötstopplack bei FPC: Einsatzfälle und Spezifikation der Öffnungen",
            "it": "Coverlay vs solder mask su FPC: quando usare cosa e come specificare le aperture",
            "fr": "Coverlay vs solder mask sur FPC : quand utiliser quoi et comment spécifier les ouvertures",
            "ru": "Coverlay vs solder mask на FPC: когда что применять и как задавать окна",
            "es": "Coverlay vs solder mask en FPC: cuándo usar cada uno y cómo especificar aperturas",
            "ar": "Coverlay مقابل Solder Mask على FPC: متى تستخدم كل منهما وكيف تحدد فتحات اللحام",
        },
        descriptions={
            "en": "Compare coverlay and solder mask for flex PCBs: durability, fine‑pitch limits, opening tolerances, and DFM notes for your fab.",
            "de": "Coverlay vs Lötstopplack für Flex-PCBs: Haltbarkeit, Fine‑Pitch‑Grenzen, Öffnungstoleranzen und DFM-Hinweise für den Hersteller.",
            "it": "Confronto coverlay e solder mask per flex PCB: durata, limiti fine‑pitch, tolleranze delle aperture e note DFM per il produttore.",
            "fr": "Comparer coverlay et solder mask sur flex PCB : durabilité, limites fine‑pitch, tolérances d’ouverture et notes DFM pour le fabricant.",
            "ru": "Сравнение coverlay и solder mask для гибких плат: долговечность, ограничения по fine‑pitch, допуски окон и DFM‑заметки для фабрики.",
            "es": "Compara coverlay y solder mask en flex PCB: durabilidad, límites de paso fino, tolerancias de aperturas y notas DFM para tu fabricante.",
            "ar": "قارن بين coverlay وsolder mask في لوحات الفليكس: المتانة، حدود الـfine‑pitch، تسامحات الفتحات، وملاحظات DFM للمصنع.",
        },
        en_h2_renames={
            "What coverlay vs solder mask on FPC really means (scope & boundaries)": "Coverlay vs solder mask on FPC: what it means (scope & boundaries)",
            "coverlay vs solder mask on FPC metrics that matter (how to evaluate quality)": "Metrics that matter (durability, pitch, tolerance)",
            "How to choose coverlay vs solder mask on FPC: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "coverlay vs solder mask on FPC implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "coverlay vs solder mask on FPC common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "coverlay vs solder mask on FPC FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing, acceptance criteria)",
            "Resources for coverlay vs solder mask on FPC (related pages and tools)": "Related pages & tools",
            "coverlay vs solder mask on FPC glossary (key terms)": "Glossary (key terms)",
            "Conclusion: coverlay vs solder mask on FPC next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="industrial-grade-dual-channel-safety-control-pcb",
        titles={
            "en": "Industrial Dual-Channel Safety Control PCB: Architecture, DFM, and Acceptance Tests",
            "de": "Industrielles Dual-Channel-Safety-Control-PCB: Architektur, DFM und Abnahmetests",
            "it": "PCB safety control dual-channel industriale: architettura, DFM e test di accettazione",
            "fr": "PCB de contrôle safety double canal industriel : architecture, DFM et tests d’acceptation",
            "ru": "Промышленная dual‑channel safety‑плата: архитектура, DFM и приемочные тесты",
            "es": "PCB de control safety dual-channel industrial: arquitectura, DFM y pruebas de aceptación",
            "ar": "لوحة تحكم أمان ثنائية القناة صناعية: البنية وDFM واختبارات القبول",
        },
        descriptions={
            "en": "A practical guide to industrial dual-channel safety PCBs: redundancy rules, isolation, DFM risks, and acceptance tests for production.",
            "de": "Praxisleitfaden für industrielle Dual-Channel-Safety-PCBs: Redundanzregeln, Isolation, DFM-Risiken und Abnahmetests für die Serie.",
            "it": "Guida pratica ai PCB safety dual-channel industriali: regole di ridondanza, isolamento, rischi DFM e test di accettazione in produzione.",
            "fr": "Guide pratique des PCB safety double canal industriels : redondance, isolation, risques DFM et tests d’acceptation en production.",
            "ru": "Практическое руководство по промышленным dual‑channel safety PCB: резервирование, изоляция, риски DFM и приемочные испытания.",
            "es": "Guía práctica de PCB safety dual-channel industriales: redundancia, aislamiento, riesgos DFM y pruebas de aceptación para producción.",
            "ar": "دليل عملي للوحات أمان ثنائية القناة الصناعية: قواعد التكرار، العزل، مخاطر DFM، واختبارات القبول للإنتاج.",
        },
        en_h2_renames={
            "What industrial-grade Dual-channel safety control PCB really means (scope & boundaries)": "What “dual-channel safety control PCB” means (scope & boundaries)",
            "industrial-grade Dual-channel safety control PCB metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose industrial-grade Dual-channel safety control PCB: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "industrial-grade Dual-channel safety control PCB implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "industrial-grade Dual-channel safety control PCB common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "industrial-grade Dual-channel safety control PCB FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing, acceptance criteria)",
            "Resources for industrial-grade Dual-channel safety control PCB (related pages and tools)": "Related pages & tools",
            "industrial-grade Dual-channel safety control PCB glossary (key terms)": "Glossary (key terms)",
            "Conclusion: industrial-grade Dual-channel safety control PCB next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="01",
        slug="automotive-grade-osfp-800g-transceiver-board",
        titles={
            "en": "Automotive-Grade OSFP 800G Transceiver Board: SI/PI, Thermal, and Reliability Checklist",
            "de": "Automotive-Grade OSFP-800G-Transceiver-Board: SI/PI, Thermik und Zuverlässigkeits-Checkliste",
            "it": "Scheda transceiver OSFP 800G automotive-grade: SI/PI, termica e checklist affidabilità",
            "fr": "Carte transceiver OSFP 800G automotive-grade : SI/PI, thermique et checklist fiabilité",
            "ru": "Плата трансивера OSFP 800G automotive‑grade: SI/PI, тепловой расчет и чек‑лист надежности",
            "es": "Placa transceiver OSFP 800G automotive-grade: SI/PI, térmica y checklist de fiabilidad",
            "ar": "لوحة Transceiver ‏OSFP 800G بمعيار سيارات: ‏SI/PI والحرارة وقائمة تحقق للاعتمادية",
        },
        descriptions={
            "en": "Design and build OSFP 800G boards for automotive environments: high-speed routing, power integrity, thermal design, and reliability validation.",
            "de": "OSFP-800G-Boards für Automotive: High-Speed-Routing, Power-Integrity, Thermik und Zuverlässigkeitsvalidierung.",
            "it": "Progetta schede OSFP 800G per ambiente automotive: routing ad alta velocità, power integrity, termica e validazione affidabilità.",
            "fr": "Concevoir des cartes OSFP 800G pour l’automotive : routage haut débit, power integrity, thermique et validation fiabilité.",
            "ru": "Проектирование OSFP 800G плат для automotive: высокоскоростная трассировка, целостность питания, тепловой дизайн и валидация надежности.",
            "es": "Diseña placas OSFP 800G para automoción: ruteo high-speed, integridad de potencia, térmica y validación de fiabilidad.",
            "ar": "تصميم لوحات OSFP 800G لبيئات السيارات: توجيه عالي السرعة، سلامة الطاقة، التصميم الحراري، والتحقق من الاعتمادية.",
        },
        en_h2_renames={
            "What automotive-grade OSFP 800G transceiver board really means (scope & boundaries)": "What “OSFP 800G transceiver board” means (scope & boundaries)",
            "automotive-grade OSFP 800G transceiver board metrics that matter (how to evaluate quality)": "Metrics that matter (how to evaluate quality)",
            "How to choose automotive-grade OSFP 800G transceiver board: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "automotive-grade OSFP 800G transceiver board implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "automotive-grade OSFP 800G transceiver board common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "automotive-grade OSFP 800G transceiver board FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, materials, testing, acceptance criteria)",
            "Resources for automotive-grade OSFP 800G transceiver board (related pages and tools)": "Related pages & tools",
            "automotive-grade OSFP 800G transceiver board glossary (key terms)": "Glossary (key terms)",
            "Conclusion: automotive-grade OSFP 800G transceiver board next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="12",
        slug="rogers-ptfe-hybrid-stackup-manufacturing",
        titles={
            "en": "Rogers/PTFE Hybrid Stackups: Build Rules, Lamination Risks, and DFM Checklist",
            "de": "Rogers/PTFE-Hybrid-Stackups: Aufbau-Regeln, Laminationsrisiken und DFM-Checkliste",
            "it": "Stackup ibridi Rogers/PTFE: regole di build, rischi di laminazione e checklist DFM",
            "fr": "Stackups hybrides Rogers/PTFE : règles de fabrication, risques de lamination et checklist DFM",
            "ru": "Гибридные стек‑апы Rogers/PTFE: правила сборки, риски ламинации и DFM‑чек‑лист",
            "es": "Stackups híbridos Rogers/PTFE: reglas de fabricación, riesgos de laminación y checklist DFM",
            "ar": "Stackup هجين Rogers/PTFE: قواعد التصنيع ومخاطر التصفيح وقائمة DFM",
        },
        descriptions={
            "en": "How to manufacture Rogers/PTFE hybrid stackups: material pairing, surface prep, lamination cycle risks, and acceptance tests for RF performance.",
            "de": "So fertigen Sie Rogers/PTFE-Hybrid-Stackups: Materialpaarung, Oberflächenvorbereitung, Laminationsrisiken und Abnahmetests für RF-Performance.",
            "it": "Come produrre stackup ibridi Rogers/PTFE: abbinamento materiali, preparazione superfici, rischi del ciclo di laminazione e test di accettazione RF.",
            "fr": "Fabriquer des stackups hybrides Rogers/PTFE : choix matériaux, préparation surface, risques de cycle de lamination et tests d’acceptation RF.",
            "ru": "Как производить гибридные стек‑апы Rogers/PTFE: подбор материалов, подготовка поверхности, риски цикла ламинации и RF‑приемка.",
            "es": "Cómo fabricar stackups híbridos Rogers/PTFE: selección de materiales, preparación de superficie, riesgos de laminación y pruebas de aceptación RF.",
            "ar": "كيفية تصنيع stackup هجين Rogers/PTFE: اختيار المواد، تحضير السطح، مخاطر دورة التصفيح، واختبارات قبول أداء RF.",
        },
        en_h2_renames={
            "What Rogers/PTFE hybrid stackup manufacturing really means (scope & boundaries)": "What Rogers/PTFE hybrid stackups mean (scope & boundaries)",
            "Selection guidance by scenario (trade-offs)": "Selection guidance by scenario (trade-offs)",
            "From design to manufacturing (implementation checkpoints)": "Implementation checkpoints (design to manufacturing)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="12",
        slug="three-phase-inverter-control-pcb-layout",
        titles={
            "en": "Three-Phase Inverter Control PCB Layout: Isolation, Current Sense, and EMI Checklist",
            "de": "PCB-Layout für 3-Phasen-Invertersteuerung: Isolation, Strommessung und EMI-Checkliste",
            "it": "Layout PCB controllo inverter trifase: isolamento, current sense e checklist EMI",
            "fr": "Layout PCB de contrôle d’onduleur triphasé : isolation, mesure de courant et checklist EMI",
            "ru": "Разводка платы управления трехфазным инвертором: изоляция, измерение тока и EMI‑чек‑лист",
            "es": "Layout PCB de control de inversor trifásico: aislamiento, sensado de corriente y checklist EMI",
            "ar": "تخطيط PCB للتحكم في عاكس ثلاثي الطور: العزل وقياس التيار وقائمة EMI",
        },
        descriptions={
            "en": "Layout guidance for three-phase inverter control PCBs: isolation/creepage, gate-loop hygiene, current sensing, and EMI-safe routing.",
            "de": "Layout-Leitfaden für 3-Phasen-Invertersteuerung: Isolation/Kriechstrecken, Gate-Loop, Strommessung und EMI-sicheres Routing.",
            "it": "Linee guida layout per controllo inverter trifase: isolamento/creepage, gate loop, misura corrente e routing EMI-safe.",
            "fr": "Conseils de layout pour contrôle d’onduleur triphasé : isolation/creepage, boucle de gate, mesure de courant et routage EMI-safe.",
            "ru": "Рекомендации по разводке: изоляция/критические расстояния, gate‑loop, датчики тока и EMI‑безопасная трассировка.",
            "es": "Guía de layout: aislamiento/creepage, gate loop, sensado de corriente y ruteo seguro para EMI.",
            "ar": "إرشادات تخطيط: العزل ومسافات الزحف، حلقة البوابة، قياس التيار، وتوجيه مسارات آمنة ضد EMI.",
        },
        en_h2_renames={
            "What Three-phase inverter control PCB layout really means (scope & boundaries)": "What “three-phase inverter control PCB” means (scope & boundaries)",
            "Selection guidance by scenario (trade-offs)": "Design choices by scenario (trade-offs)",
            "From design to manufacturing (implementation checkpoints)": "Implementation checkpoints (design to manufacturing)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="11",
        slug="how-to-prepare-bom-for-turnkey-pcb-assembly",
        titles={
            "en": "How to Prepare a BOM for Turnkey PCB Assembly (DFM Checklist + Common Mistakes)",
            "de": "BOM für Turnkey-PCB-Assembly vorbereiten (DFM-Checkliste + typische Fehler)",
            "it": "Come preparare una BOM per assemblaggio PCB turnkey (checklist DFM + errori comuni)",
            "fr": "Comment préparer une BOM pour l’assemblage PCB turnkey (checklist DFM + erreurs fréquentes)",
            "ru": "Как подготовить BOM для turnkey PCB assembly (DFM‑чек‑лист + частые ошибки)",
            "es": "Cómo preparar una BOM para ensamblaje PCB turnkey (checklist DFM + errores comunes)",
            "ar": "كيفية تجهيز BOM لتجميع PCB بنظام Turnkey (قائمة DFM + أخطاء شائعة)",
        },
        descriptions={
            "en": "A turnkey BOM checklist: required columns, alternates, lifecycle data, and how to avoid sourcing delays and assembly rework.",
            "de": "Turnkey-BOM-Checkliste: Pflichtspalten, Alternativen, Lifecycle-Daten und wie Sie Beschaffungsverzögerungen und Nacharbeit vermeiden.",
            "it": "Checklist BOM turnkey: colonne richieste, alternative, dati lifecycle e come evitare ritardi di approvvigionamento e rework in assemblaggio.",
            "fr": "Checklist BOM turnkey : colonnes requises, alternatives, données lifecycle et comment éviter retards d’approvisionnement et retouches d’assemblage.",
            "ru": "Чек‑лист turnkey‑BOM: обязательные поля, альтернативы, жизненный цикл компонентов и как избежать задержек закупки и переделок.",
            "es": "Checklist de BOM turnkey: columnas obligatorias, alternativos, datos de ciclo de vida y cómo evitar retrasos de compra y retrabajos.",
            "ar": "قائمة BOM لـTurnkey: الأعمدة المطلوبة، البدائل، بيانات دورة حياة القطع، وتجنّب تأخير التوريد وإعادة العمل.",
        },
        en_h2_renames={
            "how to prepare bom for turnkey pcb assembly: what this playbook covers (and who it’s for)": "What this guide covers (and who it’s for)",
            "When how to prepare bom for turnkey pcb assembly is the right approach (and when it isn’t)": "When turnkey assembly is a good fit (and when it isn’t)",
            "Requirements you must define before quoting": "BOM requirements (before quoting)",
            "The hidden risks that break scale-up": "Hidden BOM issues that delay builds",
            "Validation plan (what to test, when, and what “pass” means)": "Validation & acceptance (what to check before build)",
            "Decision guidance (trade-offs you can actually choose)": "Decision guidance (trade-offs you can choose)",
            "Conclusion": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="06",
        slug="ipc-a-610-acceptance-criteria-overview",
        titles={
            "en": "IPC-A-610 Acceptance Criteria: What to Check (SMT, THT, Rework) and How to Use It",
            "de": "IPC-A-610 Akzeptanzkriterien: Prüfpunkte (SMT, THT, Rework) und Anwendung",
            "it": "Criteri di accettazione IPC-A-610: cosa controllare (SMT, THT, rework) e come usarli",
            "fr": "Critères d’acceptation IPC-A-610 : quoi vérifier (SMT, THT, retouche) et comment l’utiliser",
            "ru": "Критерии приемки IPC‑A‑610: что проверять (SMT, THT, ремонт) и как применять",
            "es": "Criterios de aceptación IPC-A-610: qué revisar (SMT, THT, retrabajo) y cómo usarlo",
            "ar": "معايير القبول IPC‑A‑610: ما الذي تفحصه (SMT وTHT وإعادة العمل) وكيف تستخدمه",
        },
        descriptions={
            "en": "An engineer-friendly overview of IPC-A-610: acceptance classes, common defect limits, and how to apply criteria in inspection and supplier quality.",
            "de": "Ingenieursfreundlicher Überblick zu IPC-A-610: Klassen, typische Fehlertoleranzen und Anwendung in Prüfung und Lieferantenqualität.",
            "it": "Panoramica pratica su IPC-A-610: classi di accettazione, limiti difetti comuni e come applicare i criteri in ispezione e qualità fornitori.",
            "fr": "Vue d’ensemble pratique d’IPC-A-610 : classes, limites de défauts courants et application en inspection et qualité fournisseur.",
            "ru": "Практический обзор IPC‑A‑610: классы приемки, пределы дефектов и применение в инспекции и качестве поставщика.",
            "es": "Resumen práctico de IPC-A-610: clases de aceptación, límites de defectos comunes y cómo aplicarlo en inspección y calidad de proveedores.",
            "ar": "نظرة عملية على IPC‑A‑610: فئات القبول، حدود العيوب الشائعة، وكيفية تطبيقها في الفحص وجودة المورّد.",
        },
        en_h2_renames={
            "What ipc-a-610 acceptance criteria overview really means (scope & boundaries)": "What IPC-A-610 means (scope & boundaries)",
            "ipc-a-610 acceptance criteria overview metrics that matter (how to evaluate quality)": "What to check (acceptance criteria by area)",
            "How to choose ipc-a-610 acceptance criteria overview: selection guidance by scenario (trade-offs)": "How to use IPC-A-610 (by scenario)",
            "ipc-a-610 acceptance criteria overview implementation checkpoints (design to manufacturing)": "Implementation checkpoints (inspection to supplier control)",
            "ipc-a-610 acceptance criteria overview common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "ipc-a-610 acceptance criteria overview FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (classes, rework limits, documentation)",
            "Resources for ipc-a-610 acceptance criteria overview (related pages and tools)": "Related pages & tools",
            "ipc-a-610 acceptance criteria overview glossary (key terms)": "Glossary (key terms)",
            "Conclusion: ipc-a-610 acceptance criteria overview next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="04",
        slug="high-temperature-storage-hts-test-for-pcb",
        titles={
            "en": "High-Temperature Storage (HTS) Test for PCBs: Purpose, Conditions, and Pass/Fail Criteria",
            "de": "High-Temperature-Storage-(HTS)-Test für PCBs: Zweck, Bedingungen und Pass/Fail-Kriterien",
            "it": "Test HTS (High-Temperature Storage) per PCB: scopo, condizioni e criteri pass/fail",
            "fr": "Test HTS (High-Temperature Storage) pour PCB : objectif, conditions et critères pass/fail",
            "ru": "Испытание HTS (High‑Temperature Storage) для PCB: цель, режимы и критерии pass/fail",
            "es": "Prueba HTS (High-Temperature Storage) para PCB: propósito, condiciones y criterios de aprobado/reprobado",
            "ar": "اختبار HTS للـPCB: الهدف والظروف ومعايير النجاح/الفشل",
        },
        descriptions={
            "en": "Explain HTS testing for PCBs: what it stresses, typical temperatures/durations, sample prep, and how to interpret failures after storage aging.",
            "de": "HTS-Prüfung für PCBs: Belastungsziel, typische Temperaturen/Dauern, Probenvorbereitung und Interpretation von Ausfällen nach Alterung.",
            "it": "Spiegazione del test HTS: cosa sollecita, temperature/durate tipiche, preparazione campioni e interpretazione dei guasti dopo aging.",
            "fr": "Comprendre le test HTS : ce qu’il sollicite, températures/durées typiques, préparation d’échantillons et lecture des défaillances après vieillissement.",
            "ru": "HTS‑тестирование PCB: что нагружается, типовые температуры/время, подготовка образцов и интерпретация отказов после старения.",
            "es": "Prueba HTS en PCB: qué estresa, temperaturas/duraciones típicas, preparación de muestras y cómo interpretar fallos tras el envejecimiento.",
            "ar": "شرح اختبار HTS: ما الذي يختبره، درجات الحرارة/المدة الشائعة، تحضير العينات، وكيف تفسر الأعطال بعد التعتيق.",
        },
        en_h2_renames={
            "high temperature storage (hts) test for pcb: definition, scope, and who this guide is for": "HTS test: definition, scope, and who this guide is for",
            "When to use high temperature storage (hts) test for pcb (and when a standard approach is better)": "When to use HTS (and when another test fits better)",
            "high temperature storage (hts) test for pcb specifications (materials, stackup, tolerances)": "Test conditions to define (temp, time, sample size)",
            "high temperature storage (hts) test for pcb manufacturing risks (root causes and prevention)": "Common failure modes (root causes & prevention)",
            "high temperature storage (hts) test for pcb validation and acceptance (tests and pass criteria)": "Validation & acceptance (pass/fail criteria)",
            "high temperature storage (hts) test for pcb supplier qualification checklist (RFQ, audit, traceability)": "Supplier checklist (RFQ, traceability, reports)",
            "How to choose high temperature storage (hts) test for pcb (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "high temperature storage (hts) test for pcb FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (conditions, duration, sample prep, reporting)",
            "Resources for high temperature storage (hts) test for pcb (related pages and tools)": "Related pages & tools",
            "Request a quote for high temperature storage (hts) test for pcb (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: high temperature storage (hts) test for pcb next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="05",
        slug="ethercat-interface-pcb-best-practices",
        titles={
            "en": "EtherCAT Interface PCB Best Practices: Routing, Isolation, EMC, and Test Checklist",
            "de": "EtherCAT-Schnittstellen-PCB Best Practices: Routing, Isolation, EMC und Test-Checkliste",
            "it": "Best practice PCB per interfaccia EtherCAT: routing, isolamento, EMC e checklist test",
            "fr": "Bonnes pratiques PCB d’interface EtherCAT : routage, isolation, CEM et checklist de test",
            "ru": "EtherCAT‑интерфейс PCB: best practices по трассировке, изоляции, EMC и тестам",
            "es": "Buenas prácticas de PCB para interfaz EtherCAT: ruteo, aislamiento, EMC y checklist de pruebas",
            "ar": "أفضل ممارسات PCB لواجهة EtherCAT: التوجيه والعزل وEMC وقائمة الاختبار",
        },
        descriptions={
            "en": "Design EtherCAT interface boards: differential routing, isolation, grounding/shielding, connector layout, and tests to pass EMC reliably.",
            "de": "EtherCAT-Boards auslegen: Differenzialrouting, Isolation, Masse/Schirmung, Connector-Layout und Tests für zuverlässige EMC.",
            "it": "Progetta interfacce EtherCAT: routing differenziale, isolamento, massa/schermatura, layout connettori e test per superare EMC.",
            "fr": "Concevoir des interfaces EtherCAT : routage différentiel, isolation, masses/blindage, layout connecteurs et tests pour réussir la CEM.",
            "ru": "Проектирование EtherCAT интерфейсов: диф‑трассировка, изоляция, земля/экранирование, компоновка коннекторов и EMC‑тесты.",
            "es": "Diseño de interfaces EtherCAT: ruteo diferencial, aislamiento, masa/apantallado, layout de conectores y pruebas para pasar EMC.",
            "ar": "تصميم لوحات EtherCAT: توجيه تفاضلي، عزل، تأريض/تدريع، تخطيط الموصل، واختبارات لاجتياز EMC بثقة.",
        },
        en_h2_renames={
            "What EtherCAT interface PCB best practices really means (scope & boundaries)": "What “EtherCAT interface PCB” means (scope & boundaries)",
            "EtherCAT interface PCB best practices metrics that matter (how to evaluate quality)": "Metrics that matter (signal, isolation, EMC)",
            "How to choose EtherCAT interface PCB best practices: selection guidance by scenario (trade-offs)": "How to choose (trade-offs by scenario)",
            "EtherCAT interface PCB best practices implementation checkpoints (design to manufacturing)": "Implementation checkpoints (design to manufacturing)",
            "EtherCAT interface PCB best practices common mistakes (and the correct approach)": "Common mistakes (and the correct approach)",
            "EtherCAT interface PCB best practices FAQ (cost, lead time, materials, testing, acceptance criteria)": "FAQ (cost, lead time, isolation, EMC testing)",
            "Resources for EtherCAT interface PCB best practices (related pages and tools)": "Related pages & tools",
            "EtherCAT interface PCB best practices glossary (key terms)": "Glossary (key terms)",
            "Conclusion: EtherCAT interface PCB best practices next steps": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="pi-shrinkage-and-dimensional-control",
        titles={
            "en": "Polyimide (PI) Shrinkage & Dimensional Control: Tolerances, Compensation, and Process Tips",
            "de": "Polyimid-(PI)-Schrumpfung & Maßhaltigkeit: Toleranzen, Kompensation und Prozess-Tipps",
            "it": "Ritiro del poliimmide (PI) e controllo dimensionale: tolleranze, compensazione e consigli processo",
            "fr": "Retrait du polyimide (PI) et contrôle dimensionnel : tolérances, compensation et conseils process",
            "ru": "Усадка полиимида (PI) и размерный контроль: допуски, компенсация и советы по процессу",
            "es": "Contracción de poliimida (PI) y control dimensional: tolerancias, compensación y consejos de proceso",
            "ar": "انكماش البولي إيميد (PI) والتحكم بالأبعاد: التسامحات والتعويض ونصائح العملية",
        },
        descriptions={
            "en": "Understand PI shrinkage in flex/rigid-flex: what drives variation, how fabs compensate, and what tolerances to use in drawings and DFM.",
            "de": "PI-Schrumpfung in Flex/Starrflex: Ursachen der Variation, Kompensation in der Fertigung und sinnvolle Toleranzen für Zeichnung und DFM.",
            "it": "Capire il ritiro PI in flex/rigid-flex: cause della variabilità, compensazioni di fabbrica e tolleranze in disegni e DFM.",
            "fr": "Comprendre le retrait PI en flex/rigid-flex : facteurs de variation, compensation usine et tolérances à utiliser en plan et DFM.",
            "ru": "Усадка PI в flex/rigid‑flex: причины разброса, компенсация на фабрике и какие допуски закладывать в чертежи/DFM.",
            "es": "Contracción PI en flex/rigid-flex: causas de variación, compensación en fábrica y tolerancias para planos/DFM.",
            "ar": "فهم انكماش PI في flex/rigid‑flex: أسباب التفاوت، كيف يعوّض المصنع، وما التسامحات المناسبة في الرسومات وDFM.",
        },
        en_h2_renames={
            "What PI shrinkage and dimensional control really means (scope & boundaries)": "What PI shrinkage means (scope & boundaries)",
            "Selection guidance by scenario (trade-offs)": "How to manage shrinkage (options and trade-offs)",
            "From design to manufacturing (implementation checkpoints)": "Implementation checkpoints (design to manufacturing)",
            "Conclusion (next steps)": "Conclusion (next steps)",
        },
    ),
    PostSpec(
        year="2025",
        month="10",
        slug="pcba-functional-test-fct-planning-guide",
        titles={
            "en": "PCBA Functional Test (FCT) Planning: Coverage, Fixtures, Logging, and Production Checklist",
            "de": "PCBA Functional Test (FCT) Planung: Coverage, Fixtures, Logging und Produktions-Checkliste",
            "it": "Pianificazione test funzionale PCBA (FCT): copertura, fixture, logging e checklist produzione",
            "fr": "Planification de test fonctionnel PCBA (FCT) : couverture, fixtures, logs et checklist production",
            "ru": "Планирование функционального теста PCBA (FCT): покрытие, фикстуры, логирование и чек‑лист",
            "es": "Planificación de prueba funcional PCBA (FCT): cobertura, fixtures, registro y checklist de producción",
            "ar": "تخطيط اختبار FCT لـPCBA: التغطية والـfixtures وتسجيل البيانات وقائمة الإنتاج",
        },
        descriptions={
            "en": "A production-minded FCT guide: define coverage, write test limits, plan fixtures, log data for traceability, and reduce false fails.",
            "de": "FCT-Leitfaden für die Serie: Coverage definieren, Grenzwerte festlegen, Fixtures planen, Daten für Traceability loggen und False Fails reduzieren.",
            "it": "Guida FCT orientata alla produzione: definire la copertura, limiti di test, fixture, logging per tracciabilità e ridurre falsi scarti.",
            "fr": "Guide FCT orienté production : définir la couverture, limites de test, fixtures, logs pour la traçabilité et réduire les faux défauts.",
            "ru": "FCT‑гайд для серии: определить покрытие, лимиты, фикстуры, логирование для трассируемости и снижение ложных отказов.",
            "es": "Guía FCT para producción: definir cobertura, límites, fixtures, registrar datos para trazabilidad y reducir falsos fallos.",
            "ar": "دليل FCT للإنتاج: حدّد التغطية، حدود القياس، خطّط الـfixtures، سجّل البيانات للتتبّع، وقلّل الأعطال الكاذبة.",
        },
        en_h2_renames={
            "pcba functional test (fct) planning guide: definition, scope, and who this guide is for": "FCT planning: definition, scope, and who this guide is for",
            "When to use pcba functional test (fct) planning guide (and when a standard approach is better)": "When to use FCT (and when another test fits better)",
            "pcba functional test (fct) planning guide specifications (materials, stackup, tolerances)": "What to define (coverage, limits, fixtures, logs)",
            "pcba functional test (fct) planning guide manufacturing risks (root causes and prevention)": "Risks that cause false fails (and how to prevent them)",
            "pcba functional test (fct) planning guide validation and acceptance (tests and pass criteria)": "Validation & acceptance (pass/fail criteria)",
            "pcba functional test (fct) planning guide supplier qualification checklist (RFQ, audit, traceability)": "Supplier checklist (RFQ, audit, traceability)",
            "How to choose pcba functional test (fct) planning guide (trade-offs and decision rules)": "Decision guidance (trade-offs and decision rules)",
            "pcba functional test (fct) planning guide FAQ (cost, lead time, DFM files, materials, testing)": "FAQ (fixture cost, lead time, logs, limits)",
            "Resources for pcba functional test (fct) planning guide (related pages and tools)": "Related pages & tools",
            "Request a quote for pcba functional test (fct) planning guide (DFM review + pricing)": "Request a quote (DFM review + pricing)",
            "Conclusion: pcba functional test (fct) planning guide next steps": "Conclusion (next steps)",
        },
    ),
]


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
    def _yaml_single_quote(value: str) -> str:
        return "'" + value.replace("'", "''") + "'"

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
