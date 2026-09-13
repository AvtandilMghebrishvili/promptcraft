# Library / ბიბლიოთეკა

Every entry exists in English and Georgian. The Georgian is written from intent, not translated —
see [`../references/georgian-style-guide.md`](../references/georgian-style-guide.md).

ყველა ჩანაწერს აქვს ინგლისური და ქართული ვერსია. ქართული დაწერილია განზრახვიდან და არა ნათარგმნი —
იხ. [`../references/georgian-style-guide.md`](../references/georgian-style-guide.md).

---

## Categories

| Folder | File | Contents |
|---|---|---|
| **text/** | [`writing.md`](text/writing.md) | Drafting, editing, rewriting, tone, structure |
| | [`business.md`](text/business.md) | Sales, marketing, ops, HR, client communication |
| | [`education.md`](text/education.md) | Lesson design, assessment, explanation, feedback |
| | [`research.md`](text/research.md) | Grounded analysis, comparison, synthesis, extraction |
| | [`everyday.md`](text/everyday.md) | Personal planning, decisions, learning, admin |
| **image/** | [`midjourney.md`](image/midjourney.md) | Photographic, illustrative, stylised |
| | [`nano-banana.md`](image/nano-banana.md) | Creative-director briefs, character consistency, semantic-mask editing |
| | [`reverse-prompting.md`](image/reverse-prompting.md) | Image → prompt: descriptor, style, lighting extraction; prompt repair |
| | [`gpt-image.md`](image/gpt-image.md) | Natural-language prompts, in-image text, editing |
| | [`flux-sd.md`](image/flux-sd.md) | Flux and Stable Diffusion, weights, negatives |
| | [`brand-product.md`](image/brand-product.md) | Product shots, brand assets, mockups |
| **video/** | [`sora-veo.md`](video/sora-veo.md) | Narrative shots, physics, native audio |
| | [`seedance.md`](video/seedance.md) | `@image1` references, timecoded multi-shot, video extension |
| | [`runway-kling.md`](video/runway-kling.md) | Image-to-video, human motion, effects |
| | [`shot-language.md`](video/shot-language.md) | Reusable shot, movement and lighting vocabulary |
| **code/** | [`agentic.md`](code/agentic.md) | Claude Code, Cursor, Cline — scoped tasks |
| | [`workflow-loop.md`](code/workflow-loop.md) | plan → test → implement → review → verify → remember → improve, one prompt per stage |
| | [`debugging.md`](code/debugging.md) | Reproduction, isolation, root cause |
| | [`review-architecture.md`](code/review-architecture.md) | Review, refactor plans, design decisions |
| **audio/** | [`voice-music.md`](audio/voice-music.md) | TTS, narration, music beds, podcast production |
| **agents/** | [`automation.md`](agents/automation.md) | n8n, Zapier, Make, extraction contracts, orchestrators |

## How to read an entry

```
### B-03 · Cold outreach email
`claude` `gpt` — sales, b2b

**EN**
[prompt]

**KA**
[prompt]
```

- **ID** (`B-03`) — stable. Referenced in [`../data/prompts.csv`](../data/prompts.csv).
- **Tool tags** — which tools this is shaped for. A `midjourney` prompt will not work in Claude.
- **Topic tags** — for search.
- `{{variables}}` / `{{ცვლადები}}` — replace before use.

## Prefixes

`W` writing · `B` business · `E` education · `R` research · `D` everyday ·
`MJ` midjourney · `GI` gpt-image · `NB` nano banana · `FX` flux/sd · `BP` brand & product · `RP` reverse prompting ·
`SV` sora/veo · `SD` seedance · `RK` runway/kling · `SL` shot language ·
`AC` agentic coding · `WL` workflow loop · `DB` debugging · `RA` review & architecture ·
`AU` audio · `AG` agents & automation

## A note on two entry shapes

Most entries are **plain EN / KA** — two prompts, same job, each written natively.

Generator entries (image, video, audio) are **EN / KA-working-version + paste string**: the
Georgian block is there so you can compose and edit in Georgian, and after the `---` line comes
the English string you actually paste, because those models do not take Georgian reliably.

`reverse-prompting.md` is the exception inside `image/` — those are instruction prompts for a
vision-capable text model, so they use the plain two-block shape.
