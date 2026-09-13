# Anti-patterns / ანტი-პატერნები

37 ways a prompt burns credits and returns the wrong thing, in six categories.
Each entry: the symptom, why it happens, and the fix.

37 გზა, რომლითაც პრომპტი კრედიტს ჭამს და არასწორ შედეგს აბრუნებს, ექვს კატეგორიად.
თითოეულში: სიმპტომი, მიზეზი და გამოსწორება.

**Diagnostic order.** When a prompt fails, check in this sequence — the earlier categories
account for most failures: **Scope → Task → Format → Context → Reasoning → Agentic.**

---

## A. Task failures / ამოცანის შეცდომები

### A1. Vague verb
`improve`, `optimise`, `help with`, `make better`, `clean up`, `enhance`
→ The model picks its own target. Different target every run.
**Fix:** name the operation. `rewrite`, `shorten to 200 words`, `extract`, `rank by`, `classify into`.
**ქართულად:** `გააუმჯობესე` → `შეამოკლე 200 სიტყვამდე`.

### A2. Two objectives in one prompt
"Summarise this and also suggest improvements and format it as a table."
→ The model does one well and the others poorly, and you cannot tell which failed.
**Fix:** one prompt, one objective. Chain them if you need all three.

### A3. No success criterion
→ "Done" is a vibe. You cannot evaluate the output and neither can the model.
**Fix:** something binary. `passes tests/auth`, `fits in 3 slides`, `every claim has a source`.

### A4. Emotional intensity instead of specification
"This is REALLY important, please be VERY careful and thorough!!!"
→ Carries no information. Costs tokens. Some models get *more* hedging, not less.
**Fix:** replace the emphasis with the actual requirement it was standing in for.

### A5. Unbounded scope
"Write everything I need to know about X."
→ Either a shallow listicle or a runaway generation.
**Fix:** cap it. `the 5 things that most often go wrong`, `800 words`, `for someone who already knows Y`.

### A6. Asking for the prompt when you want the task
"Give me a prompt to write my quarterly report."
→ Two round trips for one deliverable.
**Fix:** if you want the report, ask for the report. Prompts are for reuse.

### A7. Role assignment that changes nothing
"You are a world-class expert genius senior principal architect."
→ Stacked titles do not improve output. One relevant role does.
**Fix:** `You are a security reviewer` — or drop the role entirely if the task is unambiguous.

---

## B. Context failures / კონტექსტის შეცდომები

### B1. Unstated assumption
You know it is a B2B SaaS in Georgia. The model assumes US consumer retail.
**Fix:** one line of domain context beats three paragraphs of correction later.

### B2. No grounding constraint on a factual task
→ The model fills gaps with plausible fabrication. This is the single largest source of wrong output.
**Fix:** `Use ONLY the material below. If it is not stated, write "not stated". NEVER infer.`

### B3. Prior attempts not mentioned
"Fix this." (You already tried three things.)
→ The model proposes attempt #1 again.
**Fix:** `Already tried and failed: X (error Y), Z (no change). Do not repeat these.`

### B4. Whole codebase / whole document pasted
→ The relevant signal is 2% of the context. Attention spreads. Cost multiplies.
**Fix:** paste the relevant function and its callers. Describe the rest in two lines.

### B5. Context contradicting itself across a session
Turn 3 said "keep it formal." Turn 11 says "make it punchy."
→ The model follows the most recent and you get whiplash.
**Fix:** restate the full constraint set when you change direction.

### B6. Georgian context left as English context
A budgeting prompt in Georgian that talks about `401(k)`, `IRS`, `Thanksgiving sales`.
→ The output is Georgian words describing a country the reader does not live in.
**Fix:** swap the referents. See `georgian-style-guide.md` §5.

### B7. Audience unstated on explanatory tasks
→ The model aims at "generic educated adult" and lands between your two actual audiences.
**Fix:** `for a CFO with no technical background` / `for a junior developer on their first week`.

---

## C. Format failures / ფორმატის შეცდომები

### C1. Output shape unstated
→ Different structure every run. Impossible to automate, tedious to read.
**Fix:** state it. Table with named columns, JSON with named keys, exactly 5 bullets.

### C2. Length unstated or stated vaguely
"Keep it brief." → brief means 80 words to you and 400 to the model.
**Fix:** a number. `under 150 words`, `3 sentences`, `one paragraph`.

### C3. Format specified but not enforced
"Output JSON." → you get JSON inside a markdown fence with a sentence of preamble.
**Fix:** `Output a single JSON object. No markdown fence. No text before or after.`

### C4. Aesthetic adjectives instead of measurable specs
"Make the design modern and clean."
→ Meaningless. Every model has a different "modern."
**Fix:** `8px grid, one accent colour, system font stack, no gradients, no shadows`.

### C5. Example given in the wrong format
You show a markdown example but ask for JSON.
→ The model follows the example, not the instruction. Examples outweigh instructions.
**Fix:** every example must be in the exact target format.

### C6. Ban lists written in the wrong language
A Georgian prompt that bans the English string `"high quality"`.
→ The model generates `„მაღალი ხარისხის“` and the ban never fires.
**Fix:** write bans in the output language.

### C7. Numerals with plural nouns in Georgian
`200 სიტყვებს`, `5 დღეები`
→ Teaches the model to produce ungrammatical Georgian throughout.
**Fix:** `200 სიტყვას`, `5 დღე`. Georgian numerals take the singular.

---

## D. Scope failures / არეალის შეცდომები

### D1. No file scope on an IDE or agentic tool
→ The agent decides which files are relevant. It is wrong, expansively and expensively.
**Fix:** list the files it may touch. Explicitly.

### D2. No forbidden list
→ The agent installs packages, changes the schema, rewrites your config.
**Fix:** `NEVER install packages. NEVER modify migrations. NEVER touch files outside the list.`

### D3. **No stop condition** ← the expensive one
→ The agent loops: try, fail, try differently, fail, try differently… until your budget is gone.
**Fix:** `Stop when <command> passes. If it still fails after two attempts, STOP and report. Do not try a third approach.`

### D4. No verification command
→ The agent declares success based on its own reading of its own diff.
**Fix:** give it the command that proves it. `npm test`, `ruff check`, `curl localhost:3000/health`.

### D5. Destructive actions without a review gate
→ Deleted branch, dropped table, force-push.
**Fix:** `Before any destructive operation, STOP and ask. Never execute git push --force, rm -rf, or DROP.`

### D6. Silent agent
→ Twenty minutes of work, one line of output, no way to tell where it went wrong.
**Fix:** `After each file you modify, print the filename and one line describing the change.`

### D7. Scope stated in prose, not as a list
"Just work on the auth stuff."
→ "The auth stuff" is nine files to you and thirty to the agent.
**Fix:** paths, one per line.

---

## E. Reasoning failures / მსჯელობის შეცდომები

### E1. Requesting chain of thought
"Show your reasoning step by step."
→ On reasoning models this measurably degrades the answer and inflates cost.
**Fix:** ask for the answer. If you need the justification, ask for a short rationale *after* the answer.

### E2. Step-by-step scaffolding on a reasoning model
→ Your steps fight the model's internal decomposition, which is better than yours.
**Fix:** state the problem and the success criterion. Nothing else.

### E3. Few-shot examples on a reasoning model
→ Anchors it to the example's approach instead of reasoning from the problem.
**Fix:** zero-shot, unless the examples are extremely tightly aligned to the target.

### E4. Tree of Thought / Graph of Thought / Mixture of Experts
→ 3–10× token cost, increased fabrication, no reliable gain on ordinary tasks.
**Fix:** don't. If you must, measure it on your own task first.

### E5. Analysis task without an audit contract
"Analyse this data." → confident conclusions with no traceability.
**Fix:** `For each conclusion, cite the specific rows or figures it rests on. If the data does not support a conclusion, say so.`

### E6. Asking a model to self-score its own output
→ Reliably optimistic. Not a quality signal.
**Fix:** score against an external criterion, or run a separate pass with the criterion as the only input.

---

## F. Agentic failures / აგენტური შეცდომები

### F1. No starting state
→ The agent cannot reproduce the problem, so it fixes a different one.
**Fix:** the exact command and the exact output you see.

### F2. No target state
→ "Make it work" is not a target.
**Fix:** the exact command and the exact output you want to see.

### F3. Scripting the steps for an orchestrator
On Perplexity, Manus, or a multi-agent runner: "First search X, then open Y, then…"
→ These systems decompose internally. Your script overrides better planning with worse.
**Fix:** describe the finished deliverable and the acceptance criteria. Let it plan.

### F4. No failure behaviour for tool calls
→ An API returns 500, the agent invents the data and continues.
**Fix:** `If a tool call fails, STOP and report the error. NEVER fabricate the result.`

### F5. Unbounded retries
→ Same failed call, forty times.
**Fix:** `Retry at most twice, then stop.`

### F6. No budget or turn cap on long-running agents
**Fix:** `Complete this in at most 15 tool calls. If you are not done, stop and report progress.`

### F7. Assuming the agent remembers the last session
→ It does not, unless you gave it a file that says so.
**Fix:** restate the constraints, or point it at the file that holds them.

### F8. Letting the agent choose the verification
→ It picks the check its work already passes.
**Fix:** you name the command.

### F9. No handoff format on multi-agent work
→ Agent A's output is prose; Agent B needed JSON.
**Fix:** define the interface between stages as explicitly as an API contract.

### F10. Destructive default on ambiguity
→ Asked to "clean up the branch", the agent deletes it.
**Fix:** `When an instruction is ambiguous, choose the non-destructive interpretation and say which you chose.`

---

## Quick triage

| Symptom | Most likely cause |
|---|---|
| Burned a lot of credits, no result | D3 — no stop condition |
| Different output shape every run | C1 — format unstated |
| Confidently wrong facts | B2 — no grounding constraint |
| Ignored your length limit | C2, or the limit was at the bottom of the prompt |
| Agent touched files you did not expect | D1 — no file scope |
| Generic, could-be-anyone output | A1 + B7 — vague verb, no audience |
| Georgian output reads like a translation | see `georgian-style-guide.md` §6 |
| Reasoning model got worse when you added detail | E1/E2/E3 — scaffolding on a reasoning model |
