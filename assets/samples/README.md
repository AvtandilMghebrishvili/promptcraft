# Sample images / სანიმუშო სურათები

The library is text. These images make it browsable — and they are the fastest way to
tell whether a prompt is worth your time.

ბიბლიოთეკა ტექსტია. ეს სურათები მას დასათვალიერებელს ხდის — და ყველაზე სწრაფი გზაა
მიხვდე, ღირს თუ არა პრომპტი შენს დროს.

## How to fill this folder

```bash
python3 scripts/samples.py status               # what is covered, what is not
python3 scripts/samples.py list --file nano-banana   # what to generate, with the exact paste string
```

`list` prints, for every entry that has no image yet, the English string the generator
expects and the filename to save the result under. Generate, save, then:

```bash
python3 scripts/samples.py embed                # inserts the <img> into each entry
python3 scripts/samples.py gallery              # rebuilds library/GALLERY.md
```

`embed` only writes an `<img>` for a file that actually exists, so the pages never show a
broken image. Both commands are safe to re-run.

## Naming

```
assets/samples/<library file stem>/<ENTRY ID>.<ext>
assets/samples/nano-banana/NB-01.webp
assets/samples/midjourney/MJ-07.webp
assets/samples/sora-veo/SV-03.gif
```

Accepted: `.webp` `.png` `.jpg` `.jpeg` `.gif`. **Prefer `.webp`** — a 1024px webp is
usually under 150 KB, a png of the same image is over 1 MB, and a repo full of pngs
becomes slow to clone.

For video entries, save a short looping `.gif` or a single representative frame.

## Rules

- **Only images you generated yourself**, from the prompt in that entry. Never a result
  someone else produced and published — that is their work, whatever licence the page carries.
- **No recognisable real people.** The prompts are written to avoid this; keep it that way.
- **No real brands, logos or wordmarks** in the frame.
- Longest side ~1024px. There is no reason to ship 4K here.
- If a generation is a poor example of the prompt, leave the slot empty rather than filling
  it with something misleading.

## Order worth doing first

1. `nano-banana` — 30 entries, the most visually varied
2. `midjourney` — 15
3. `brand-product` — 11, the ones a business will actually copy
4. `gpt-image` — 11, shows the in-image typography
5. everything else
