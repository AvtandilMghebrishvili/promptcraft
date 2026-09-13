#!/usr/bin/env python3
"""Build data/prompts.csv from the markdown library.

Every library entry looks like:

    ### XX-01 · Title
    `tool` `tool` — tag, tag

    **EN**
    ```
    ...
    ```

    **KA**
    ```
    ...
    ```

In the generator files (image, video, audio) the KA block additionally contains a
`---` separator followed by the English string that is actually pasted into the tool.
That paste string is dropped here; the CSV carries the Georgian working version.

Usage:  python3 scripts/build_csv.py
"""

from __future__ import annotations

import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"
OUT = ROOT / "data" / "prompts.csv"

HEADING = re.compile(r"^###\s+([A-Z]{1,2}-\d{2})\s+·\s+(.+?)\s*$", re.M)
META = re.compile(r"^((?:`[^`]+`\s*)+)(?:—\s*(.*))?$")
BLOCK = re.compile(r"\*\*(EN|KA)\*\*\s*\n```[a-z]*\n(.*?)\n```", re.S)

FIELDS = [
    "id",
    "category",
    "file",
    "title_en",
    "title_ka",
    "prompt_en",
    "prompt_ka",
    "tools",
    "tags",
]


def split_title(raw: str) -> tuple[str, str]:
    """`Cold outreach email` or `Cold outreach email / ცივი წერილი` -> (en, ka)."""
    if " / " in raw:
        en, ka = raw.split(" / ", 1)
        return en.strip(), ka.strip()
    return raw.strip(), ""


def strip_paste_string(ka: str) -> str:
    """Drop the trailing `---` + English paste string from generator entries."""
    parts = re.split(r"\n---\s*\n", ka)
    return parts[0].strip()


def parse_file(path: pathlib.Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    category = path.parent.name
    rel = path.relative_to(ROOT).as_posix()

    rows: list[dict[str, str]] = []
    matches = list(HEADING.finditer(text))

    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]

        title_en, title_ka = split_title(m.group(2))

        tools, tags = "", ""
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            meta = META.match(line)
            if meta:
                tools = " ".join(re.findall(r"`([^`]+)`", meta.group(1)))
                tags = (meta.group(2) or "").strip()
            break

        blocks = dict(BLOCK.findall(body))
        prompt_en = blocks.get("EN", "").strip()
        prompt_ka = strip_paste_string(blocks.get("KA", ""))

        if not prompt_en and not prompt_ka:
            print(f"  warn: {m.group(1)} in {rel} has no prompt block", file=sys.stderr)

        rows.append(
            {
                "id": m.group(1),
                "category": category,
                "file": rel,
                "title_en": title_en,
                "title_ka": title_ka,
                "prompt_en": prompt_en,
                "prompt_ka": prompt_ka,
                "tools": tools,
                "tags": tags,
            }
        )
    return rows


def main() -> int:
    files = sorted(p for p in LIBRARY.rglob("*.md") if p.name != "README.md")
    rows: list[dict[str, str]] = []
    for path in files:
        found = parse_file(path)
        print(f"{path.relative_to(ROOT)}: {len(found)}")
        rows.extend(found)

    ids = [r["id"] for r in rows]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"ERROR: duplicate ids: {sorted(dupes)}", file=sys.stderr)
        return 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nwrote {OUT.relative_to(ROOT)} — {len(rows)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
