#!/usr/bin/env python3
from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from pathlib import Path


BLOGS_ROOT = Path("/code/hileap/frontendAPT/public/static/blogs")
TARGET_LOCALES = ["de", "it", "fr", "ru", "es", "ar"]


@dataclass(frozen=True)
class PostSpec:
    year: str
    month: str
    slug: str
    titles: dict[str, str]  # locale -> title
    descriptions: dict[str, str]  # locale -> description


POSTS: list[PostSpec] = [
    PostSpec(
        year="2025",
        month="06",
        slug="pcb-delamination-blistering",
        titles={
            "de": "PCB-Delamination & Blasenbildung: Ursachen, Prävention und Checkliste",
            "it": "Delaminazione e blistering PCB: cause, prevenzione e checklist",
            "fr": "Délamination et cloques PCB : causes, prévention et checklist",
            "ru": "Деламинация и вздутия PCB: причины, профилактика и чек‑лист",
            "es": "Delaminación y ampollas en PCB: causas, prevención y checklist",
            "ar": "انفصال الطبقات وفقاعات PCB: الأسباب والوقاية وقائمة التحقق",
        },
        descriptions={
            "de": "Erfahren Sie, was PCB-Delamination und Blasenbildung verursacht, wie Sie feuchtigkeitsbedingte Ausfälle verhindern und was Sie bei Material und Fertigung validieren sollten.",
            "it": "Scopri cosa causa la delaminazione e il blistering dei PCB, come prevenire i guasti dovuti all’umidità e cosa validare su materiali e produzione.",
            "fr": "Comprenez les causes de la délamination et des cloques PCB, comment prévenir les défaillances liées à l’humidité et quoi valider côté matériaux et fabrication.",
            "ru": "Узнайте, что вызывает деламинацию и вздутия PCB, как предотвратить отказы из‑за влаги и что проверять по материалам и производству.",
            "es": "Aprende qué causa la delaminación y las ampollas en PCB, cómo prevenir fallos por humedad y qué validar en materiales y fabricación.",
            "ar": "تعرّف على أسباب انفصال الطبقات والفقاعات في PCB، وكيف تمنع الأعطال الناتجة عن الرطوبة، وما الذي يجب التحقق منه في المواد والتصنيع.",
        },
    ),
    PostSpec(
        year="2025",
        month="07",
        slug="pcb-design-review-checklist",
        titles={
            "de": "PCB-Design-Review-Checkliste: DFM, SI/PI und Fertigung",
            "it": "Checklist di design review PCB: DFM, SI/PI e produzione",
            "fr": "Checklist de revue de conception PCB : DFM, SI/PI et fabrication",
            "ru": "Чек‑лист review дизайна PCB: DFM, SI/PI и производство",
            "es": "Checklist de revisión de diseño PCB: DFM, SI/PI y fabricación",
            "ar": "قائمة مراجعة تصميم PCB: ‏DFM وSI/PI والتصنيع",
        },
        descriptions={
            "de": "Praktische PCB-Design-Review-Checkliste für DFM/DFA, Signal- und Power-Integrity, mechanische Passung und Testbarkeit – um teure Re-Spins zu vermeiden.",
            "it": "Checklist pratica di design review PCB: DFM/DFA, integrità di segnale e potenza, vincoli meccanici e testabilità per evitare respin costosi.",
            "fr": "Checklist pratique de revue de conception PCB : DFM/DFA, intégrité signal/puissance, contraintes mécaniques et testabilité pour éviter des respins coûteux.",
            "ru": "Практический чек‑лист ревью PCB: DFM/DFA, целостность сигналов и питания, механика и тестопригодность — чтобы избежать дорогих респинов.",
            "es": "Checklist práctica de revisión de diseño PCB: DFM/DFA, integridad de señal y potencia, ajuste mecánico y testabilidad para evitar respins costosos.",
            "ar": "قائمة عملية لمراجعة تصميم PCB تشمل DFM/DFA وسلامة الإشارة والطاقة والتوافق الميكانيكي وقابلية الاختبار لتجنب إعادة التصميم المكلفة.",
        },
    ),
    PostSpec(
        year="2025",
        month="08",
        slug="ict-vs-flying-probe",
        titles={
            "de": "ICT vs Flying Probe: Abdeckung, Kosten und Durchlaufzeit",
            "it": "ICT vs Flying Probe: copertura, costi e tempi",
            "fr": "ICT vs Flying Probe : couverture, coût et délai",
            "ru": "ICT vs Flying Probe: покрытие, стоимость и сроки",
            "es": "ICT vs Flying Probe: cobertura, coste y plazo",
            "ar": "ICT مقابل Flying Probe: التغطية والتكلفة والمدة الزمنية",
        },
        descriptions={
            "de": "Vergleichen Sie ICT und Flying-Probe-Tests nach Abdeckung, Kosten (Fixture/NRE), Durchlaufzeit und DFT-Anforderungen – mit praxisnahen Auswahlregeln.",
            "it": "Confronta test ICT e flying probe per copertura, costo (fixture/NRE), tempi e requisiti DFT, con criteri pratici di scelta.",
            "fr": "Comparez les tests ICT et flying probe par couverture, coût (fixture/NRE), délai et exigences DFT, avec des critères de choix concrets.",
            "ru": "Сравнение ICT и flying probe по покрытию, стоимости (оснастка/NRE), срокам и требованиям DFT — с практическими правилами выбора.",
            "es": "Compara ICT vs flying probe por cobertura, coste (fixture/NRE), plazos y requisitos DFT, con criterios prácticos de selección.",
            "ar": "قارن بين اختبار ICT وFlying Probe من حيث التغطية والتكلفة (الفيكستشر/NRE) والمدة ومتطلبات DFT مع إرشادات اختيار عملية.",
        },
    ),
    PostSpec(
        year="2025",
        month="05",
        slug="coverlay-opening-rules",
        titles={
            "de": "Coverlay-Öffnungsregeln: Abstand, Toleranzen und typische Fehler",
            "it": "Regole per aperture coverlay: clearance, tolleranze ed errori comuni",
            "fr": "Règles d’ouverture de coverlay : dégagement, tolérance et erreurs courantes",
            "ru": "Правила окон coverlay: зазоры, допуски и типичные ошибки",
            "es": "Reglas de aperturas de coverlay: holgura, tolerancia y errores comunes",
            "ar": "قواعد فتحات الـCoverlay: الخلوص والتسامح والأخطاء الشائعة",
        },
        descriptions={
            "de": "Praktische Coverlay-Öffnungsregeln für Flex-PCBs: Oversize/Abstand, Toleranz, Stegbreite, Gang-Öffnungen und Validierung – um Squeeze-out zu vermeiden.",
            "it": "Regole pratiche per aperture coverlay su flex PCB: oversize/clearance, tolleranze, web width, gang openings e validazione per evitare squeeze-out.",
            "fr": "Règles pratiques d’ouverture de coverlay pour PCB flex : surcote/dégagement, tolérance, largeur de pont, gang openings et validation pour éviter le squeeze-out.",
            "ru": "Практические правила окон coverlay для flex PCB: зазор/оверайз, допуски, ширина перемычек, gang openings и валидация против squeeze‑out.",
            "es": "Reglas prácticas de aperturas de coverlay para flex PCB: holgura/sobredimensionado, tolerancia, ancho de puente, aperturas en grupo y validación para evitar squeeze-out.",
            "ar": "قواعد عملية لفتحات الـCoverlay في لوحات Flex PCB: الخلوص/الزيادة، التسامح، عرض الجسر، فتحات جماعية وخطوات تحقق لتجنب squeeze-out.",
        },
    ),
    PostSpec(
        year="2025",
        month="01",
        slug="pcb-traceability-lot-control",
        titles={
            "de": "PCB-Rückverfolgbarkeit & Loskontrolle: Daten, Kennzeichnung und Audit-Checkliste",
            "it": "Tracciabilità PCB e controllo lotti: dati, marcature e checklist audit",
            "fr": "Traçabilité PCB et contrôle de lot : données, marquage et checklist d’audit",
            "ru": "Трассируемость PCB и контроль партий: данные, маркировка и чек‑лист аудита",
            "es": "Trazabilidad PCB y control de lotes: datos, marcado y checklist de auditoría",
            "ar": "تتبّع PCB والتحكم بالدفعات: البيانات والوسم وقائمة تدقيق",
        },
        descriptions={
            "de": "Praxisleitfaden zu PCB-Rückverfolgbarkeit und Loskontrolle: UID-Formate, Kennzeichnung, MES-Verknüpfung, Aufbewahrung und Audit-Punkte für Lieferanten.",
            "it": "Guida pratica a tracciabilità PCB e controllo lotti: formati UID, marcatura, collegamento dati MES, retention e punti di audit del fornitore.",
            "fr": "Guide pratique sur la traçabilité PCB et le contrôle de lot : formats UID, marquage, liaison MES, conservation des données et points d’audit fournisseur.",
            "ru": "Практическое руководство по трассируемости PCB и контролю партий: форматы UID, маркировка, связка с MES, хранение данных и аудит поставщика.",
            "es": "Guía práctica de trazabilidad PCB y control de lotes: formatos UID, marcado, enlace de datos MES, retención y puntos de auditoría del proveedor.",
            "ar": "دليل عملي لتتبّع PCB والتحكم بالدفعات: صيغ UID، الوسم، ربط بيانات MES، الاحتفاظ بالسجلات ونقاط تدقيق المورّد.",
        },
    ),
    PostSpec(
        year="2025",
        month="04",
        slug="common-pcb-defects",
        titles={
            "de": "Häufige PCB-Defekte: Ursachen, Erkennung und Prävention",
            "it": "Difetti PCB comuni: cause, rilevamento e prevenzione",
            "fr": "Défauts PCB courants : causes, détection et prévention",
            "ru": "Типовые дефекты PCB: причины, обнаружение и профилактика",
            "es": "Defectos comunes de PCB: causas, detección y prevención",
            "ar": "عيوب PCB الشائعة: الأسباب والكشف والوقاية",
        },
        descriptions={
            "de": "Häufige PCB-Fertigungsdefekte: warum sie entstehen, wie man sie erkennt und welche Spezifikationen/DFM-Checks Ausschuss in der Produktion verhindern.",
            "it": "Difetti comuni nella produzione PCB: perché accadono, come rilevarli e quali specifiche/controlli DFM evitano perdite di resa in produzione.",
            "fr": "Défauts courants de fabrication PCB : pourquoi ils arrivent, comment les détecter et quelles spécifications/contrôles DFM évitent les pertes de rendement.",
            "ru": "Типовые дефекты производства PCB: почему возникают, как обнаруживать и какие спецификации/DFM‑проверки предотвращают потери выхода в серии.",
            "es": "Defectos comunes de fabricación de PCB: por qué ocurren, cómo detectarlos y qué especificaciones/chequeos DFM evitan pérdidas de rendimiento en producción.",
            "ar": "عيوب تصنيع PCB الشائعة: لماذا تحدث، وكيف تُكتشف، وما المواصفات/فحوصات DFM التي تمنع خسائر العائد في الإنتاج.",
        },
    ),
]


def _wrap_description(text: str) -> str:
    # Keep Arabic/Russian wrapping minimal; just ensure no trailing spaces.
    return "\n".join(textwrap.wrap(text.strip(), width=78, break_long_words=False, break_on_hyphens=False))


def _split_frontmatter(md: str) -> tuple[str, str, str] | None:
    if not md.startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    fm_block = parts[0] + "\n---\n"
    body = parts[1]
    # fm_block includes starting --- and ending --- line
    return fm_block, body, parts[0]


def _update_frontmatter(fm_text: str, *, title: str, description: str) -> str:
    # Replace title and description (support both simple and folded style).
    lines = fm_text.splitlines()
    out: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^title:\s*", line):
            out.append(f"title: {title!r}")
            i += 1
            continue

        if re.match(r"^description:\s*", line):
            # Skip existing description line and any indented continuation lines.
            out.append("description: >-")
            wrapped = _wrap_description(description)
            for wline in wrapped.splitlines():
                out.append(f"  {wline}")
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                i += 1
            continue

        out.append(line)
        i += 1

    # Ensure title/description exist; if not, inject before closing ---.
    if not any(l.startswith("title:") for l in out):
        out.insert(1, f"title: {title!r}")
    if not any(l.startswith("description:") for l in out):
        insert_at = 2
        out.insert(insert_at, "description: >-")
        for wline in _wrap_description(description).splitlines():
            out.insert(insert_at + 1, f"  {wline}")
            insert_at += 1

    return "\n".join(out) + "\n"


def _ensure_h1(body: str, title: str) -> str:
    stripped = body.lstrip("\n")
    # If first non-empty line is an H1, replace it.
    m = re.match(r"^(#\s+.*)\n", stripped)
    if m:
        rest = stripped[m.end() :]
        return f"# {title}\n\n{rest.lstrip()}"
    # Otherwise insert at top.
    return f"# {title}\n\n{stripped}"


def main() -> int:
    changed = 0
    for post in POSTS:
        for locale in TARGET_LOCALES:
            title = post.titles.get(locale)
            desc = post.descriptions.get(locale)
            if not title or not desc:
                continue
            md_path = BLOGS_ROOT / post.year / post.month / locale / f"{post.slug}.md"
            if not md_path.exists():
                continue
            raw = md_path.read_text(encoding="utf-8", errors="ignore")
            parts = _split_frontmatter(raw)
            if not parts:
                continue
            fm_block, body, fm_without_end = parts
            fm_updated = _update_frontmatter(fm_without_end, title=title, description=desc)
            body_updated = _ensure_h1(body, title)
            new_text = fm_updated + "---\n" + body_updated.lstrip("\n")
            if new_text != raw:
                md_path.write_text(new_text, encoding="utf-8")
                changed += 1

    print(f"updated_files={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

