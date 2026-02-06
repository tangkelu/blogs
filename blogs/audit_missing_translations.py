import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GroupReport:
    group: Path
    base_lang: str
    langs: list[str]
    base_files: set[str]
    missing: dict[str, list[str]]
    extra: dict[str, list[str]]


def _collect_relative_files(root: Path, ext: str) -> set[str]:
    if not root.exists():
        return set()
    files: set[str] = set()
    for p in root.rglob(f"*{ext}"):
        if p.is_file():
            files.add(p.relative_to(root).as_posix())
    return files


def _discover_langs(group_dir: Path, base_lang: str) -> list[str]:
    langs: list[str] = []
    if not group_dir.exists():
        return langs
    for child in group_dir.iterdir():
        if not child.is_dir():
            continue
        name = child.name
        if name == base_lang:
            continue
        langs.append(name)
    langs.sort()
    return langs


def _parse_langs_arg(langs_arg: str | None) -> list[str] | None:
    if not langs_arg:
        return None
    parts = [p.strip() for p in langs_arg.split(",")]
    parts = [p for p in parts if p]
    return parts or None


def audit_group(group_dir: Path, base_lang: str, langs: list[str] | None, ext: str) -> GroupReport:
    base_dir = group_dir / base_lang
    base_files = _collect_relative_files(base_dir, ext)

    if langs is None:
        langs = _discover_langs(group_dir, base_lang)

    missing: dict[str, list[str]] = {}
    extra: dict[str, list[str]] = {}

    for lang in langs:
        lang_dir = group_dir / lang
        lang_files = _collect_relative_files(lang_dir, ext)
        missing_files = sorted(base_files - lang_files)
        extra_files = sorted(lang_files - base_files)
        if missing_files:
            missing[lang] = missing_files
        if extra_files:
            extra[lang] = extra_files

    return GroupReport(
        group=group_dir,
        base_lang=base_lang,
        langs=langs,
        base_files=base_files,
        missing=missing,
        extra=extra,
    )


def fill_missing(report: GroupReport, ext: str, dry_run: bool) -> int:
    created = 0
    base_dir = report.group / report.base_lang

    for lang, rel_paths in report.missing.items():
        lang_dir = report.group / lang
        for rel in rel_paths:
            src = base_dir / Path(rel)
            dst = lang_dir / Path(rel)
            if not src.exists():
                continue
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            created += 1

    return created


def _is_group_dir(p: Path, base_lang: str, ext: str) -> bool:
    base_dir = p / base_lang
    if not base_dir.exists() or not base_dir.is_dir():
        return False
    for _ in base_dir.rglob(f"*{ext}"):
        return True
    return False


def _expand_groups(paths: list[Path], scan_root: bool, base_lang: str, ext: str) -> list[Path]:
    groups: list[Path] = []
    if not scan_root:
        return paths

    for root in paths:
        if not root.exists() or not root.is_dir():
            continue
        for child in root.iterdir():
            if child.is_dir() and _is_group_dir(child, base_lang, ext):
                groups.append(child)

    groups.sort(key=lambda p: p.as_posix())
    return groups


def _print_report(report: GroupReport) -> None:
    group_name = report.group.name
    print(f"\n== {group_name} ==")
    print(f"base: {report.base_lang} files={len(report.base_files)}")

    if not report.langs:
        print("(no target languages found)")
        return

    for lang in report.langs:
        missing = report.missing.get(lang, [])
        extra = report.extra.get(lang, [])
        print(f"- {lang}: missing={len(missing)} extra={len(extra)}")
        if missing:
            for rel in missing:
                print(f"  MISSING {lang}/{rel}")
        if extra:
            for rel in extra:
                print(f"  EXTRA   {lang}/{rel}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Group directory path(s) like 1118-2-cccc. If --scan-root, treat them as roots.",
    )
    parser.add_argument("--base", default="cn")
    parser.add_argument("--langs", default=None, help="Comma-separated languages (default: auto-discover)")
    parser.add_argument("--ext", default=".md")
    parser.add_argument("--scan-root", action="store_true")
    parser.add_argument("--fill", action="store_true")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args(argv)

    base_lang: str = args.base
    ext: str = args.ext
    langs = _parse_langs_arg(args.langs)

    input_paths = [Path(p).resolve() for p in args.paths]
    groups = _expand_groups(input_paths, args.scan_root, base_lang, ext)

    if not groups:
        print("No groups found.")
        return 2

    any_missing = False
    total_created = 0

    for group in groups:
        if not _is_group_dir(group, base_lang, ext):
            continue
        report = audit_group(group, base_lang, langs, ext)
        _print_report(report)

        if report.missing:
            any_missing = True

        if args.fill and report.missing:
            created = fill_missing(report, ext, args.dry_run)
            total_created += created
            if created:
                print(f"  filled: {created} file(s){' (dry-run)' if args.dry_run else ''}")

    if args.fill:
        print(f"\nTotal filled: {total_created}{' (dry-run)' if args.dry_run else ''}")

    return 1 if any_missing and not args.fill else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
