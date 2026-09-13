# Changelog

Upstream sources (see [`sources.yml`](sources.yml)) are re-checked **monthly**. When one of them
ships something worth taking, it is adapted — never copied — added to the library in both
languages, and recorded here.

წყაროები მოწმდება **ყოველთვიურად**. როცა რომელიმე მათგანში ღირებული სიახლე ჩნდება,
ის ადაპტირდება (და არა კოპირდება), ემატება ბიბლიოთეკას ორივე ენაზე და ფიქსირდება აქ.

---

## [0.2.0] — 2026-09-13

Integrated two new sources: [affaan-m/ECC](https://github.com/affaan-m/ECC) (the agent harness
layer) and [meigen.ai](https://www.meigen.ai/) (model coverage and reverse prompting).
**202 → 240 prompts.**

**Added**
- `references/agent-harness.md` — the four layers (rules · skills · agents · hooks), what belongs
  in a standing rules file and what does not, the plan → test → implement → review → verify →
  remember → improve loop, and context economics.
- `harness/` — drop-in standing-rules templates for `CLAUDE.md` / `AGENTS.md` / `.cursorrules` /
  `.windsurfrules` / `.clinerules`, in English (`rules.md`) and Georgian (`rules.ka.md`).
- `library/code/workflow-loop.md` — 9 prompts, one per stage of the loop, each stage isolated in
  its own prompt with its own scope and its own list of things it must not do.
- `library/image/nano-banana.md` — 11 prompts for Nano Banana 2: creative-director-brief style,
  character consistency via verbatim repeated description, semantic-mask editing, multi-turn
  refinement, in-image typography.
- `library/image/reverse-prompting.md` — 9 prompts that go from an image back to a generator
  prompt: descriptor extraction, style-only extraction, lighting extraction, character sheets,
  image diffing, prompt repair, brand style capture. Observation-only, with no real-person
  identification and no artist imitation.
- `library/video/seedance.md` — 9 prompts for Seedance 2.5: the 6-part 60–100 word formula,
  `@image1` / `@video1` / `@audio1` reference syntax, timecoded multi-shot sequences, video
  extension, motion transfer.

**Changed**
- `SKILL.md` — routing now covers Nano Banana and Seedance, reverse prompting, and points at the
  harness layer for standing constraints.
- `references/tool-routing.md` — added Nano Banana 2 and Seedance 2.5.
- `sources.yml` — two new sources with what was taken from each.

---

## [0.1.0] — 2026-09-13

Initial release. / პირველი გამოშვება.

**Added**
- `SKILL.md` — bilingual prompt-engineering skill: tool detection, nine-dimension intent
  extraction, silent framework routing, delivery audit.
- `references/` — frameworks (10), tool routing (7 tool families), anti-patterns (37 in 6
  categories), quality checklist, and the Georgian localisation style guide.
- `library/` — **202 prompts**, every one in English and Georgian:
  - `text/` 68 — writing 14, business 16, education 13, research 12, everyday 13
  - `image/` 46 — midjourney 15, gpt-image 11, flux & SD 9, brand & product 11
  - `video/` 29 — sora & veo 12, runway & kling 9, shot language 8 (+ 5 vocabulary tables)
  - `code/` 35 — agentic 13, debugging 11, review & architecture 11
  - `audio/` 11 — voice & music
  - `agents/` 13 — extraction contracts 8, orchestrator briefs 5
- `data/prompts.csv` — the whole library, machine-readable.
- `scripts/build_csv.py` — regenerates the CSV from the markdown.
- `scripts/check_georgian.py` — lints the Georgian side: numeral agreement, politeness padding,
  calques, ID sequence, missing naturalness lines.
- CI that runs both on every push and PR.

**Notes**
- Georgian entries are written from intent, not translated. Context referents are adapted to
  Georgia where the scenario is local (`ლარი`, `RS.ge`, `jobs.ge`, `ეროვნული გამოცდები`).
- Generator files (image, video, audio) carry a Georgian working version plus the English
  string that is actually pasted into the tool, because those models do not take Georgian reliably.

---

## Monthly review log / ყოველთვიური მიმოხილვის ჟურნალი

| Date | Sources checked | Outcome |
|---|---|---|
| 2026-09-13 | all 9 in `sources.yml` | Initial synthesis. |
| 2026-09-13 | + affaan-m/ECC, meigen.ai | Added the harness layer and its loop; added Nano Banana 2, Seedance 2.5 and reverse prompting. +38 prompts. |
