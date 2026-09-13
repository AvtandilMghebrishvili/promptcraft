# Tool routing / ინსტრუმენტების მიხედვით მარშრუტიზაცია

Same intent, seven different prompts. This file is the syntax map.

ერთი და იგივე განზრახვა — შვიდი სხვადასხვა პრომპტი. ეს ფაილი სინტაქსის რუკაა.

---

## Production LLMs — Claude, GPT, Gemini, Llama, Mistral

**Structure with XML tags** whenever the prompt has more than one section. Models are trained
on this and it survives long context far better than markdown headers.

```
<context>…</context>
<task>…</task>
<rules>…</rules>
<output_format>…</output_format>
```

**Rules**
- Constraints in the first 30%. Attention decays down the prompt.
- `MUST` / `NEVER`, not `should` / `try to avoid`.
- Positive directives: `Write in short declarative sentences` beats `Don't be verbose`.
- Role assignment only when it changes vocabulary or judgement. Stacked titles do nothing.
- Long reference material goes *before* the instruction, not after — the instruction should be the
  last thing the model reads.
- One example is worth three paragraphs of format description.

**Georgian output** — add the naturalness line and name the register:
```
დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
რეგისტრი: ნახევრად ოფიციალური.
```

---

## Reasoning models — o-series, DeepSeek-R1, Qwen thinking modes

**Give less, not more.** This is the counterintuitive one.

**Do**
- State the problem and the success criterion.
- Provide the raw material.
- Stop.

**Do not**
- "Think step by step" — it already does
- "Show your reasoning" — degrades the answer
- Few-shot examples — anchors it to your approach
- Role assignment — no measured benefit
- Structured decomposition — fights its internal planning

```
Here is a query that returns duplicate rows and the schema it runs against.
Return a corrected query returning exactly one row per customer with their
most recent order date.

{{query}}
{{schema}}
```

If you need justification, ask for it **after**: `Then, in two sentences, state what was wrong.`

---

## Agentic coding — Claude Code, Cursor, Cline, Windsurf, Devin, Copilot, Codex

**Use the File-scope framework. Every time.** See `frameworks.md` §6.

Five mandatory elements:

| Element | Without it |
|---|---|
| Start state + reproduction command | Fixes an imagined bug |
| Target state + verification command | "Done" is a guess |
| Allowed files | Refactors the whole repo |
| Forbidden actions | Installs packages, changes schema, force-pushes |
| **Stop condition** | **Runaway loop — the biggest credit sink there is** |

Add for anything non-trivial:
```
After each file you modify, print the filename and one line describing the change.
If an instruction is ambiguous, choose the non-destructive reading and state which you chose.
If a tool call fails, STOP and report. NEVER fabricate the result.
Retry at most twice, then stop.
```

**Rules files** (`.cursorrules`, `CLAUDE.md`, `AGENTS.md`) carry the standing constraints —
stack, conventions, forbidden paths. The per-task prompt then carries only what is task-specific.
Do not repeat the rules file in the prompt.

---

## Image — Midjourney, DALL·E / GPT-Image, Flux, Stable Diffusion, Ideogram

**Comma-separated descriptors, weighted by position.** Subject first, technical parameters last.

```
subject, action, setting, composition, lighting, style/medium, technical params
```

**Rules**
- **Describe the image, not the act of making it.** Skip "a photo of" — name the medium at the end instead.
- Earlier tokens carry more weight. Never lead with the style.
- Concrete beats abstract: `single shaft of window light from camera left` beats `dramatic lighting`.
- Negatives are handled differently per tool — Midjourney `--no x`, SD a separate negative field,
  GPT-Image prefers a positive restatement (`an empty street` beats "no people").
- Name the lens and film stock when you want photographic realism: `85mm, f/1.8, Kodak Portra 400`.

**Per-tool**

| Tool | Notes |
|---|---|
| **Midjourney** | Parameters at the end: `--ar 16:9 --style raw --stylize 250 --no text`. `--style raw` for photographic, default for illustrative. `--sref <url>` for style reference. |
| **GPT-Image / DALL·E** | Responds to full natural-language sentences better than the others. Best in class for text rendering inside images — spell the text exactly and put it in quotes. Positive phrasing only. |
| **Nano Banana 2** | A creative director's brief in full sentences — subject, composition, action, location, style, edit instruction. Comma descriptor strings underperform. Holds about 5 characters and 14 objects consistent; takes up to 14 reference images. Editing works by semantic masking (name what changes, name what must stay identical) across several turns, not one giant prompt. 512px–4K, 14 ratios including 21:9 and 8:1. |
| **Flux** | Excellent prompt adherence; long descriptive sentences work. Strong at text and hands. |
| **Stable Diffusion** | Token weighting `(word:1.3)`, separate negative prompt field, LoRA/checkpoint dependent — the checkpoint affects style more than your prompt does. |
| **Ideogram** | Typography and logo work; state the text and the typographic style explicitly. |

---

## Video — Sora, Veo, Runway, Kling, Pika, Luma

**One continuous shot per prompt** unless the tool supports cuts. Use the Shot spec framework.

```
[shot size]. [subject + one action]. Camera: [movement + speed].
Lighting: [source, quality, direction]. Mood: [one word or phrase].
Audio: [diegetic sound, music or none]. Duration: [seconds].
```

**Rules**
- Name the shot size or the model picks wide when you wanted a close-up.
- Name the camera movement or the model adds a gratuitous orbit.
- **One action per shot.** Two competing actions produce morphing.
- Specify audio explicitly, including `no music` — otherwise you get generic stock score.
- Bound the duration.
- Hands, text, and crowds remain the weak points across all tools. Design around them.

**Per-tool**

| Tool | Notes |
|---|---|
| **Sora** | Longest coherent shots, strongest physics. Handles multi-beat descriptions within one shot. |
| **Seedance 2.5** | 4–15s, 480p/720p/1080p, six ratios, MP4 with synced audio. The only one here that takes mixed reference input in one generation — up to 9 images, 3 clips, 3 audio files, addressed in the prompt as `@image1`, `@video1`, `@audio1` — and timecoded multi-shot blocks (`[0:00–0:04] AERIAL WIDE — …`). Aim for 60–100 words with the first 30 establishing the scene. |
| **Veo** | Best native audio generation — specify the soundscape in detail; it will deliver it. |
| **Runway** | Strong image-to-video. Prompt the *motion*, let the source image carry the composition. |
| **Kling** | Strong on human motion and faces. Start/end frame control. |
| **Pika** | Fast iteration, good for effects and stylised work. |
| **Luma** | Good camera-move control; name the move in camera-operator vocabulary. |

---

## Audio — ElevenLabs, Suno, Udio, TTS

**Speech**
```
[emotion] [pace] [emphasis markers] [pause markers]
```
Mark pauses with punctuation or explicit tags rather than describing them. Give the emotional
state, not the performance instruction: `quietly furious` beats `say this angrily`.

**Music**
```
[genre] [instrumentation] [BPM] [key/mood] [structure] [vocals or instrumental] [reference era]
```
```
Georgian polyphonic vocals over slow downtempo electronics, 78 BPM, minor,
intro–verse–chorus–outro, male three-part harmony, analogue tape warmth
```

---

## Orchestrators & automation — Perplexity, Manus, n8n, Zapier, Make

**Describe the deliverable, not the steps.** These systems decompose internally and step-scripting
makes them worse.

```
❌ First search for X, then open the top three results, then extract Y, then…
✅ Deliverable: a table of the five vendors with pricing, contract minimum, and Georgian
   availability. Every figure must link to its source. If a vendor does not publish pricing,
   write "not published" — never estimate.
```

For **workflow tools** (n8n, Zapier, Make) the AI node is doing structured extraction —
use the Contract framework (`frameworks.md` §9). The critical clause is failure behaviour:

```
If the input does not contain the required fields, return {"error":"MISSING_FIELDS"}
and nothing else. NEVER fabricate values to complete the schema.
```

---

## One intent, seven prompts

Intent: *make something about a Tbilisi wine bar's new tasting series.*

| Tool | Prompt |
|---|---|
| **Claude** | `<context>Natural-wine bar in Tbilisi, new monthly tasting series.</context><task>Write the launch Instagram caption.</task><rules>40–60 words. MUST open with a concrete detail, not an announcement. NEVER use "join us" or "don't miss".</rules><output_format>Caption, one line break, three hashtags.</output_format>` |
| **o-series** | `Write the launch Instagram caption for a Tbilisi natural-wine bar's monthly tasting series. 40–60 words, opens with a concrete detail, no "join us".` |
| **Midjourney** | `hand pouring amber wine into a stemless glass, close-up, dim stone marani interior, single warm window light from camera left, condensation on glass, documentary photography, 85mm f/1.8, Kodak Portra 400 --ar 4:5 --style raw` |
| **Sora** | `Medium close-up. A hand tilts a clay jug and pours amber wine into a glass, filling it halfway. Camera: static. Lighting: single warm window light from frame left, deep shadow behind. Mood: unhurried. Audio: liquid pouring, faint room tone, no music. Duration: 4s.` |
| **Suno** | `Slow downtempo instrumental, upright bass and brushed drums, 72 BPM, minor, warm analogue tape, no vocals, loopable 30s bed` |
| **Claude Code** | `<start_state>Event page at src/pages/events.tsx renders a hardcoded list.</start_state><target_state>It reads from src/data/events.json. npm run build passes.</target_state><allowed_files>src/pages/events.tsx, src/data/events.json, src/types/event.ts</allowed_files><forbidden>NEVER install packages. NEVER touch other files.</forbidden><stop_condition>Stop when npm run build passes. After two failed attempts, STOP and report.</stop_condition>` |
| **n8n** | `INPUT: one event RSVP email. EXTRACT: name, email, guest_count (integer), dietary_note (string or null). RULES: if guest_count is not stated, use 1. NEVER infer a dietary note. OUTPUT: a single JSON object, no markdown fence. If the email is not an RSVP, return {"error":"NOT_RSVP"}.` |
