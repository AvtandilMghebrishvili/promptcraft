# Prompt frameworks / პრომპტის ფრეიმვორკები

Ten structures. The skill picks one silently — you should never see the name in a finished prompt.
Pick by task shape, not by fashion.

ათი სტრუქტურა. სკილი ირჩევს ჩუმად — მზა პრომპტში ფრეიმვორკის სახელი არასდროს ჩანს.
აირჩიე ამოცანის ფორმის მიხედვით და არა მოდის.

---

## 1. RTF — Role, Task, Format

The default. Short, everyday requests where the output shape is simple.

**Structure:** who the model is → what to do → what shape the answer takes.

```
You are a technical editor. Rewrite the paragraph below so a non-engineer
can follow it. Output: the rewritten paragraph only, same length or shorter.
```
```
შენ ხარ ტექნიკური რედაქტორი. გადაწერე ქვემოთ მოცემული აბზაცი ისე, რომ
არაინჟინერმაც გაიგოს. გამოსავალი: მხოლოდ გადაწერილი აბზაცი, იმავე სიგრძის ან უფრო მოკლე.
```

**Use for:** rewriting, summarising, quick classification, one-off questions.
**Do not use for:** anything with more than two constraints.

---

## 2. CO-STAR — Context, Objective, Style, Tone, Audience, Response

Business and marketing writing, where *how* it sounds matters as much as *what* it says.

```
<context>A Tbilisi wine bar launching a natural-wine tasting series.</context>
<objective>Write the Instagram caption announcing the first event.</objective>
<style>Conversational, concrete, no marketing superlatives.</style>
<tone>Warm, slightly irreverent.</tone>
<audience>25–40, Tbilisi, drinks wine regularly, allergic to being sold to.</audience>
<response>One caption, 40–60 words, one line break, three hashtags at the end.</response>
```
```
<კონტექსტი>თბილისური ღვინის ბარი იწყებს ნატურალური ღვინის დეგუსტაციების სერიას.</კონტექსტი>
<მიზანი>დაწერე Instagram-ის ტექსტი პირველი ღონისძიების ასანონსებლად.</მიზანი>
<სტილი>სასაუბრო, კონკრეტული, სარეკლამო გადაჭარბებების გარეშე.</სტილი>
<ტონი>თბილი, ოდნავ თამამი.</ტონი>
<აუდიტორია>25–40 წელი, თბილისი, რეგულარულად სვამს ღვინოს, ვერ იტანს პირდაპირ გაყიდვას.</აუდიტორია>
<გამოსავალი>ერთი ტექსტი, 40–60 სიტყვა, ერთი აბზაცის გამოტოვება, ბოლოს სამი ჰეშთეგი.</გამოსავალი>

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

**Use for:** ads, social copy, landing pages, client emails, brand voice work.

---

## 3. RISEN — Role, Instructions, Steps, End goal, Narrowing

Professional multi-step work with real constraints. The workhorse for analysis and planning.

```
<role>Operations consultant for small manufacturers.</role>
<instructions>Produce a 90-day plan to cut order-to-delivery time.</instructions>
<steps>
1. Identify the three slowest stages from the data provided.
2. For each, name one intervention and its cost.
3. Sequence them by dependency.
</steps>
<end_goal>A plan the owner can start on Monday without hiring anyone.</end_goal>
<narrowing>Budget ceiling ₾15,000. No new software. No headcount.</narrowing>
```

**Use for:** strategy, operations, research plans, curriculum design, audits.
**Key property:** `narrowing` is where you kill the generic answer. Without it you get a McKinsey deck.

---

## 4. TCREI — Task, Context, References, Evaluate, Iterate

Research and analysis where the answer must be grounded in supplied material.

```
<task>Compare the three vendor proposals attached and recommend one.</task>
<context>We are a 40-person company replacing our CRM. Migration risk is our top concern.</context>
<references>Use ONLY the three proposals below. If a proposal does not state something, write "not stated" — do not infer.</references>
<evaluate>Score each on: migration effort, total 3-year cost, support SLA, exit cost.</evaluate>
<iterate>End with the single question whose answer would most change your recommendation.</iterate>
```

**Use for:** vendor selection, literature review, competitive analysis, due diligence.
**Key property:** `references` with an explicit "do not infer" clause is the strongest available
anti-hallucination lever for grounded tasks.

---

## 5. Few-shot — Instruction + 2–5 worked pairs

When the output format is unusual, or the judgement call is hard to describe but easy to demonstrate.

```
Classify each support message by urgency. Output the label only.

Message: "The payment page is down, nobody can check out."
Label: P0

Message: "Can you add dark mode at some point?"
Label: P3

Message: "Invoice #4412 has the wrong VAT rate."
Label: P2

Message: {{message}}
Label:
```

**Rules that matter:**
- 2–5 examples. Beyond 5, returns diminish and cost climbs.
- Examples must cover the *edges*, not three variations of the easy case.
- Keep them consistent in format down to the whitespace. Inconsistency teaches inconsistency.
- On reasoning models, few-shot often *hurts*. Use zero-shot unless the examples are tightly aligned.

---

## 6. File-scope — Start, Target, Allowed, Forbidden, Stop

**Mandatory for every agentic coding prompt.** No exceptions.

```
<start_state>
`POST /api/orders` returns 500 when `items` is empty. Reproduce with `npm run test:orders`.
</start_state>

<target_state>
It returns 400 with `{"error":"EMPTY_CART"}`. `npm run test:orders` passes.
</target_state>

<allowed_files>
src/api/orders.ts
src/validation/order-schema.ts
tests/orders.test.ts
</allowed_files>

<forbidden>
NEVER modify files outside <allowed_files>.
NEVER change the database schema.
NEVER install packages.
</forbidden>

<stop_condition>
Stop when `npm run test:orders` passes. If it still fails after two attempts,
STOP and report what you tried and what the failure was. Do not try a third approach.
</stop_condition>
```

**Why each part exists:**
- `start_state` — without a reproduction command the agent fixes an imagined bug.
- `target_state` — without a verification command "done" is a guess.
- `allowed_files` — without a scope the agent refactors your whole repo.
- `forbidden` — the specific expensive mistakes, named.
- `stop_condition` — **the single highest-value line in agentic prompting.** Runaway loops are the
  largest credit sink in agentic tools by a wide margin.

---

## 7. Visual descriptor — Subject, Action, Setting, Composition, Lighting, Style, Technical

Image generation. Comma-separated, most important element first, technical parameters last.

```
elderly Georgian winemaker holding a clay qvevri lid, weathered hands in focus,
inside a dim stone marani, shallow depth of field, single shaft of window light
from camera left, warm amber falloff into deep shadow, documentary photography,
Kodak Portra 400 grain, 85mm, f/1.8 --ar 4:5
```

**Order matters** — generators weight earlier tokens more heavily. Lead with the subject,
never with the style.

**Describe the photograph that exists, not the process of making it.** "A photo of X" wastes
tokens; just describe X and name the medium at the end.

---

## 8. Shot spec — Shot size, Action, Camera, Lighting, Mood, Audio, Duration

Video generation. One continuous shot per prompt unless the tool explicitly supports cuts.

```
Medium close-up. A woman in her 30s sets a cup down on a café table and looks
off-frame left, holding the look. Camera: slow push-in, 10% over the shot.
Lighting: overcast daylight through a large window, soft, no fill. Mood: quiet
anticipation. Audio: distant espresso machine, muffled street, no music. Duration: 5s.
```

**Six failure modes this prevents:** unstated shot size (model picks wide, you wanted close),
unstated camera movement (model adds a gratuitous orbit), competing actions in one shot
(morphing), unspecified audio (generic stock music), no duration (awkward pacing),
cuts implied but not supported (chaos).

---

## 9. Contract — Input schema → Rules → Output schema → Failure behaviour

Structured extraction and automation. When the output feeds another system, not a human.

```
INPUT: one invoice as plain text.

EXTRACT:
- supplier_name (string)
- supplier_tax_id (string, 9 or 11 digits)
- invoice_date (ISO 8601)
- total_amount (number, no currency symbol)
- currency (3-letter code)
- line_items (array of {description, quantity, unit_price})

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- Amounts use "." as decimal separator regardless of source formatting.
- If the document is not an invoice, return {"error":"NOT_AN_INVOICE"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary, no explanation.
```

**Key property:** the failure behaviour clause. Without it, a model handed a non-invoice
will invent an invoice.

---

## 10. Bare — Task + success criterion

Reasoning models only. Give the problem and the definition of done. Nothing else.

```
Here is a failing SQL query and the schema. Return a corrected query that
produces one row per customer with their most recent order date.

{{query}}
{{schema}}
```

**What to leave out — deliberately:** role assignment, step-by-step instructions, "think carefully",
chain-of-thought requests, few-shot examples. On reasoning models each of these measurably degrades
output. The model already does the decomposition; your scaffolding fights it.

---

## Choosing: a decision path

```
Is the target an agentic coding tool?          → File-scope. Always. No alternative.
Is the target an image generator?              → Visual descriptor.
Is the target a video generator?               → Shot spec.
Is the target a reasoning model?               → Bare.
Does the output feed a machine, not a human?   → Contract.
Is the output shape unusual or hard to say?    → Few-shot.
Is it grounded in supplied documents?          → TCREI.
Does tone and register carry the work?         → CO-STAR.
Is it multi-step professional work?            → RISEN.
Everything else                                → RTF.
```

## What is deliberately not here

**Tree of Thought, Graph of Thought, Mixture of Experts, self-consistency voting.**
They produce impressive-looking prompts, multiply token cost several times over, and in
practice increase fabrication rather than reduce it. Use them only if you have measured a
benefit on your own task. This repo does not ship them.

**„გამოტოვებულია განზრახ“:** Tree of Thought, Graph of Thought, Mixture of Experts,
self-consistency voting — ლამაზი სახელები, გაზრდილი ტოკენების ხარჯი და პრაქტიკაში
გამოგონების მომატებული რისკი. გამოიყენე მხოლოდ მაშინ, თუ შენს ამოცანაზე თვითონ გაზომე სარგებელი.
