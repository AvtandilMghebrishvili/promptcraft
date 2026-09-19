# Credits & prior art / წყაროები და წინამორბედები

**Every prompt in this repository is original.** Nothing here was copied from another
collection. What we took from the projects below is *method* — how a skill should be
structured, which techniques survive contact with a model, what a good video prompt
contains — and then wrote our own content from scratch, in two languages.

**ამ რეპოში ყველა პრომპტი ორიგინალურია.** არაფერი დაკოპირებულა სხვა კრებულიდან. ქვემოთ
ჩამოთვლილი პროექტებიდან ავიღეთ *მეთოდი* — როგორ უნდა იყოს სკილი აგებული, რომელი ტექნიკა
უძლებს მოდელთან შეხებას, რა უნდა ეწეროს კარგ ვიდეო-პრომპტში — და შემდეგ საკუთარი შიგთავსი
დავწერეთ ნულიდან, ორ ენაზე.

---

## What we learned from / რისგან ვისწავლეთ

| Project | What the method gave us |
|---|---|
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | The skill shape: detect the target tool, extract intent across dimensions, route to a framework silently, audit before delivery. |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | That a library needs a machine-readable export next to the markdown, and that contribution friction decides whether a repo grows. |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Which techniques are evidence-backed and which are folklore — the basis for what `references/frameworks.md` ships and what it refuses to. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | How production agents are really instructed: scope declarations, stop conditions, tool contracts, failure behaviour. |
| [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) | Video prompt anatomy — shot, movement, lighting, audio — and that each tool needs its own guide. |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | The split between a standing rules file and a per-task prompt. |
| [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | The gap between published prompting advice and what shipped products actually put in their system prompts. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | XML structuring, constraint placement, and why front-loading rules matters. |
| [willwulfken/MidJourney-Styles-and-Keywords-Reference](https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference) | That descriptor order changes the result, and how large a style vocabulary really is. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The harness layer — rules, skills, agents, hooks — and running the engineering loop as separate prompts so no single context carries every perspective at once. |
| [meigen.ai](https://www.meigen.ai/) | Coverage gaps: Nano Banana, Seedance, and reverse prompting as a technique in its own right. |

---

## External collections worth browsing / გარე კრებულები, რომლებიც ღირს ნახვად

These are other people's work. We link to them rather than reproduce them — the prompts
inside were written by named individuals and belong to those authors, whatever licence the
surrounding repository carries.

ეს სხვისი ნაშრომია. ვაკეთებთ ბმულს და არ ვიმეორებთ — შიგნით არსებული პრომპტები კონკრეტულმა
ადამიანებმა დაწერეს და მათ ეკუთვნით, მიუხედავად იმისა, რა ლიცენზია აქვს თავად რეპოს.

| Collection | What you will find there |
|---|---|
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) | A curated gallery of Nano Banana prompts with sample outputs, gathered from creators on Twitter, WeChat and Replicate, each credited to its author. Categories: photorealism, creative experiments, education, e-commerce, workplace, photo editing and restoration, interior design, social media, daily life and translation, avatars. |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) · [prompts.chat](https://prompts.chat) | The largest community prompt list, browsable and copyable in the browser. |
| [willwulfken/MidJourney-Styles-and-Keywords-Reference](https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference) | A very large visual reference of style and keyword results. |
| [meigen.ai](https://www.meigen.ai/) | A free gallery with an image-to-prompt tool and character reuse. |

**Our coverage of the same ground** is in [`library/image/nano-banana.md`](library/image/nano-banana.md)
(30 entries), written independently and in both languages.

---

## Licence / ლიცენზია

- Prompts and library content: **CC0-1.0** — public domain. Use them commercially, no attribution required.
- Skill, scripts and tooling: **MIT**.

See [`LICENSE`](LICENSE).
