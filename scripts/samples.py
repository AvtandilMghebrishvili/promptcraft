#!/usr/bin/env python3
"""Manage sample images for library entries.

The library is text. Sample images make it browsable. This tool keeps the two in
sync without ever leaving a broken image on the page: an `<img>` line is written
into an entry only once the file actually exists.

    python3 scripts/samples.py status          what has a sample, what does not
    python3 scripts/samples.py list            what to generate next, with filenames
    python3 scripts/samples.py list --file nano-banana
    python3 scripts/samples.py embed           insert/refresh <img> lines (safe to re-run)
    python3 scripts/samples.py gallery         rebuild library/GALLERY.md

Workflow: run `list`, generate the images, save them under assets/samples/<file>/<ID>.<ext>,
then run `embed` and `gallery`.

სურათების სამართავი ინსტრუმენტი. `list` გეტყვის რა დააგენერირო და რა სახელით შეინახო;
`embed` ჩასვამს სურათებს ჩანაწერებში; `gallery` ააგებს გალერეას.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"
SAMPLES = ROOT / "assets" / "samples"

EXTS = (".webp", ".png", ".jpg", ".jpeg", ".gif")

HEADING = re.compile(r"^### ([A-Z]{1,2}-\d{2}) · (.+?)$", re.M)
IMG_LINE = re.compile(r"^<img src=\"[^\"]*assets/samples/[^\"]*\"[^>]*>\n\n", re.M)

# Only these categories produce something you can look at.
VISUAL = {"image", "video"}


def entry_blocks(path: pathlib.Path):
    """Yield (entry_id, title, start, end) for every entry in a library file."""
    text = path.read_text(encoding="utf-8")
    heads = list(HEADING.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        yield m.group(1), m.group(2).strip(), m.start(), end


def visual_files():
    return sorted(
        p for p in LIBRARY.rglob("*.md")
        if p.name != "README.md" and p.parent.name in VISUAL
    )


def sample_for(stem: str, entry_id: str) -> pathlib.Path | None:
    folder = SAMPLES / stem
    for ext in EXTS:
        candidate = folder / f"{entry_id}{ext}"
        if candidate.exists():
            return candidate
    return None


def paste_string(path: pathlib.Path, start: int, end: int) -> str:
    """The English string a generator actually receives."""
    seg = path.read_text(encoding="utf-8")[start:end]
    blocks = re.findall(r"\*\*(EN|KA)\*\*\s*\n```[a-z]*\n(.*?)\n```", seg, re.S)
    ka = next((b for k, b in blocks if k == "KA"), "")
    if "\n---\n" in ka:                      # generator entries carry the paste string
        return ka.rsplit("\n---\n", 1)[1].strip()
    return next((b for k, b in blocks if k == "EN"), "").strip()


def cmd_status(_args) -> int:
    total = have = 0
    for path in visual_files():
        stem = path.stem
        rows = list(entry_blocks(path))
        got = [e for e, _t, _s, _x in rows if sample_for(stem, e)]
        total += len(rows)
        have += len(got)
        bar = "█" * round(12 * len(got) / max(len(rows), 1))
        print(f"  {stem:20} {len(got):>3}/{len(rows):<3} {bar}")
    pct = 100 * have / max(total, 1)
    print(f"\n  {have}/{total} entries have a sample image ({pct:.0f}%)")
    print(f"  drop files in {SAMPLES.relative_to(ROOT)}/<file>/<ID>.webp, then run: embed, gallery")
    return 0


def cmd_list(args) -> int:
    n = 0
    for path in visual_files():
        stem = path.stem
        if args.file and args.file not in stem:
            continue
        missing = [(e, t, s, x) for e, t, s, x in entry_blocks(path) if not sample_for(stem, e)]
        if not missing:
            continue
        print(f"\n{'=' * 72}\n{stem}  —  {len(missing)} to generate\n{'=' * 72}")
        for entry_id, title, s, x in missing:
            n += 1
            print(f"\n[{n}] {entry_id} · {title}")
            print(f"    save as: assets/samples/{stem}/{entry_id}.webp")
            print("    ---")
            for line in paste_string(path, s, x).splitlines():
                print(f"    {line}")
    if n == 0:
        print("nothing missing — every visual entry has a sample")
    else:
        print(f"\n{n} images to generate. Save each one at the path shown, then run:")
        print("  python3 scripts/samples.py embed && python3 scripts/samples.py gallery")
    return 0


def cmd_embed(_args) -> int:
    changed = 0
    for path in visual_files():
        stem = path.stem
        text = path.read_text(encoding="utf-8")
        out = []
        cursor = 0
        for entry_id, _title, start, end in entry_blocks(path):
            seg = text[start:end]
            seg = IMG_LINE.sub("", seg)                       # drop any previous line
            f = sample_for(stem, entry_id)
            if f:
                rel = f"../../assets/samples/{stem}/{f.name}"
                tag = f'<img src="{rel}" width="520" alt="{entry_id} sample output">\n\n'
                # insert right after the tag line (the line under the heading)
                lines = seg.split("\n")
                insert_at = 2 if len(lines) > 2 else len(lines)
                seg = "\n".join(lines[:insert_at]) + "\n\n" + tag + "\n".join(lines[insert_at:]).lstrip("\n")
            out.append(text[cursor:start])
            out.append(seg)
            cursor = end
        out.append(text[cursor:])
        new = "".join(out)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print(f"  updated {path.relative_to(ROOT)}")
    print(f"{changed} file(s) updated" if changed else "nothing to change")
    return 0


def cmd_gallery(_args) -> int:
    lines = [
        "# Gallery / გალერეა",
        "",
        "Every entry that has a sample image, in one place. Click a thumbnail to jump to the prompt.",
        "",
        "ყველა ჩანაწერი, რომელსაც სურათი აქვს, ერთ გვერდზე. დააწკაპე და პრომპტზე გადახვალ.",
        "",
        "Rebuild with `python3 scripts/samples.py gallery`.",
        "",
    ]
    shown = 0
    for path in visual_files():
        stem = path.stem
        rows = [(e, t) for e, t, _s, _x in entry_blocks(path) if sample_for(stem, e)]
        if not rows:
            continue
        rel_md = path.relative_to(LIBRARY).as_posix()
        lines += ["---", "", f"## {stem}", "", f"[{rel_md}]({rel_md})", ""]
        for i in range(0, len(rows), 3):
            chunk = rows[i:i + 3]
            cells, subs = [], []
            for entry_id, title in chunk:
                f = sample_for(stem, entry_id)
                src = f"../assets/samples/{stem}/{f.name}"
                anchor = re.sub(r"[^a-z0-9]+", "-", f"{entry_id} {title}".lower()).strip("-")
                cells.append(f'<a href="{rel_md}#{anchor}"><img src="{src}" width="260" alt="{entry_id}"></a>')
                subs.append(f"**{entry_id}** {title}")
                shown += 1
            lines += ["| " + " | ".join(cells) + " |",
                      "|" + "---|" * len(chunk),
                      "| " + " | ".join(subs) + " |", ""]
    if shown == 0:
        lines += ["---", "", "_No sample images yet. Run `python3 scripts/samples.py list` to see what to generate._", ""]
    (LIBRARY / "GALLERY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote library/GALLERY.md — {shown} image(s)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("status").set_defaults(fn=cmd_status)
    p = sub.add_parser("list"); p.add_argument("--file", help="only this library file, e.g. nano-banana"); p.set_defaults(fn=cmd_list)
    sub.add_parser("embed").set_defaults(fn=cmd_embed)
    sub.add_parser("gallery").set_defaults(fn=cmd_gallery)
    args = ap.parse_args()
    if not getattr(args, "fn", None):
        ap.print_help()
        return 1
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
