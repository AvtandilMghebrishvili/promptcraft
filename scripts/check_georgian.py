#!/usr/bin/env python3
"""Lint the Georgian side of the library.

Enforces the rules in references/georgian-style-guide.md that can be checked
mechanically. This does not replace human review — it catches the errors that
machine translation reliably produces.

Usage:  python3 scripts/check_georgian.py [--strict]
        --strict  treat warnings as failures too
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"

KA_BLOCK = re.compile(r"\*\*KA\*\*\s*\n```[a-z]*\n(.*?)\n```", re.S)
HEADING = re.compile(r"^###\s+([A-Z]{1,2}-\d{2})\s+·", re.M)

# Numeral immediately followed by a plural-marked noun. Georgian numerals take
# the singular: `200 სიტყვას`, never `200 სიტყვებს`.
NUMERAL_PLURAL = re.compile(r"(?<![-\d])\b\d+[ \t]+[ა-ჰ]{2,}ებ(?:ს|ი|ში|ად|ზე|თან|დან|ის)\b")

# Politeness padding — the prompt addresses the model, not a colleague.
POLITENESS = re.compile(r"გთხოვთ")

# Calques that machine translation produces and Georgians do not say.
CALQUES = {
    "დარწმუნდი": "→ `გადაამოწმე, რომ` / `აუცილებლად`",
    "თავისუფლად იგრძენ": "→ delete; it carries no instruction",
    "ტერმინებში": "→ `თვალსაზრისით`, or restructure",
    "ეს არის ის, რაც": "→ restructure",
    "მიზანი არის": "→ `მიზანია`",
    "ნაბიჯ-ნაბიჯ": "→ `ეტაპობრივად` / `დაშალე ეტაპებად`",
}

# Prompts whose output is Georgian should carry the naturalness line.
NATURALNESS = "ბუნებრივ ქართულად"

# Entries where the model writes Georgian prose — these should carry the line.
# Exempt: generator prompts (image/video/audio descriptor strings), code prompts
# whose output is code, and extraction contracts whose output is JSON. The
# orchestrator briefs in agents/ do produce Georgian prose and carry the line —
# that is checked by review, not here.
PROSE_CATEGORIES = {"text"}

# A KA block that is really an English block with Georgian words: if fewer than
# this share of its non-ASCII-capable characters are Georgian, flag it.
MIN_GEORGIAN_RATIO = 0.25


def georgian_ratio(text: str) -> float:
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 1.0
    georgian = [c for c in letters if "Ⴀ" <= c <= "ჿ"]
    return len(georgian) / len(letters)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    for path in sorted(p for p in LIBRARY.rglob("*.md") if p.name != "README.md"):
        rel = path.relative_to(ROOT).as_posix()
        category = path.parent.name
        text = path.read_text(encoding="utf-8")

        first = HEADING.search(text)
        entries_text = text[first.start():] if first else ""
        ids = HEADING.findall(entries_text)
        blocks = KA_BLOCK.findall(entries_text)

        if len(ids) != len(blocks):
            errors.append(f"{rel}: {len(ids)} entries but {len(blocks)} KA blocks")

        # ID sequence must be contiguous from 01.
        if ids:
            prefix = ids[0].split("-")[0]
            expected = [f"{prefix}-{n:02d}" for n in range(1, len(ids) + 1)]
            if ids != expected:
                errors.append(f"{rel}: ID sequence broken — got {ids[:3]}… expected {expected[:3]}…")

        for entry_id, ka in zip(ids, blocks):
            checked += 1
            where = f"{rel} [{entry_id}]"

            # Strip the English paste string from generator entries before checking.
            body = re.split(r"\n---\s*\n", ka)[0]

            ratio = georgian_ratio(body)
            if ratio < MIN_GEORGIAN_RATIO:
                errors.append(f"{where}: KA block is only {ratio:.0%} Georgian letters")

            for m in NUMERAL_PLURAL.finditer(body):
                errors.append(
                    f"{where}: numeral + plural noun: '{m.group(0)}' "
                    f"— Georgian numerals take the singular"
                )

            if POLITENESS.search(body):
                # Allowed only inside an explicit ban list.
                line = next(
                    (l for l in body.splitlines() if "გთხოვთ" in l), ""
                )
                if "აკრძალულ" not in line:
                    errors.append(f"{where}: politeness padding 'გთხოვთ' outside a ban list")

            for bad, fix in CALQUES.items():
                if bad in body:
                    errors.append(f"{where}: calque '{bad}' {fix}")

            if category in PROSE_CATEGORIES and NATURALNESS not in body:
                warnings.append(
                    f"{where}: missing the naturalness line "
                    f"('{NATURALNESS}, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე')"
                )

    print(f"checked {checked} Georgian blocks\n")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    if warnings and args.strict:
        print(f"\n0 errors, {len(warnings)} warning(s) — failing because --strict")
        return 1

    print(f"\nclean — 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
