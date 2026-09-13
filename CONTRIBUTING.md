# Contributing

[ქართულად](CONTRIBUTING.ka.md)

New prompts are welcome. One rule above all others: **an entry is not finished until both languages are right.**

---

## The bar

A prompt gets merged if it passes [`references/quality-checklist.md`](references/quality-checklist.md).
The short version:

**English side**
- Names a precise operation. Not `improve`, `optimise`, `help with`.
- One objective.
- Output format explicit: shape, length as a number, structure.
- Every `MUST` / `NEVER` in the first 30% of the prompt.
- A binary success criterion where the task has one.
- Agentic prompts carry all five File-scope elements, stop condition included. No exceptions.
- No chain-of-thought requests. No Tree/Graph of Thought.
- `{{variables}}` marked and descriptively named.

**Georgian side** — this is where entries usually fail review.
- Written from the intent, not translated from the English sentences.
- `შენ`-form imperative. No `გთხოვთ`.
- Numerals take the singular: `200 სიტყვას`, never `200 სიტყვებს`.
- Established loanwords kept; no invented purist compounds.
- No calques: `დარწმუნდი, რომ`, `თავისუფლად იგრძენი`, `ტერმინებში`, `ნაბიჯ-ნაბიჯ`.
- Ban lists written in Georgian — banning an English string in a Georgian prompt does nothing.
- Context referents adapted where the scenario is local: `ლარი`, `RS.ge`, `jobs.ge`, `ეროვნული გამოცდები`.
- The naturalness line present wherever the output is Georgian prose:
  `დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.`

Full standard: [`references/georgian-style-guide.md`](references/georgian-style-guide.md).

## Entry format

```markdown
### B-17 · Short descriptive title
`claude` `gpt` — tag, tag

**EN**
​```
[prompt]
​```

**KA**
​```
[prompt]
​```

---
```

For **generator files** (image, video, audio) the KA block is a Georgian *working version*
followed by `---` and then the English string that is actually pasted into the tool:

```markdown
**KA**
​```
[Georgian working version]
---
[English string to paste]
​```
```

IDs are sequential within a file and never reused. Prefixes are listed in
[`library/README.md`](library/README.md).

## Before you open a PR

```bash
python3 scripts/check_georgian.py   # must print "clean — 0 errors"
python3 scripts/build_csv.py        # regenerates data/prompts.csv
```

Commit the regenerated `data/prompts.csv` with your change. CI runs both and will fail the PR otherwise.

## If you only have one language

Open the PR anyway and say so in the description — English-only or Georgian-only is fine as a
starting point, and a maintainer will pair on the other half. What is not fine is machine-translating
the second half and submitting it as finished. That is the exact problem this repo exists to fix.

## Testing a prompt before submitting

Run it in the tool it targets, at least twice, with different inputs. If the output shape changes
between runs, the format is under-specified — fix that before submitting. If you cannot test it
(no access to the tool), say so in the PR.

## What gets rejected

- Machine-translated Georgian
- Prompts that are really a task ("write my report") rather than a reusable prompt
- Agentic prompts without a stop condition
- Jailbreaks, prompt-injection payloads, and anything designed to circumvent a model's safety behaviour
- Content copied verbatim from another repo. Synthesis and adaptation are the point; copying is not.
- Anything that needs an API key or paid account to be useful, without saying so

## Licence

By contributing you agree that library content is released under **CC0-1.0** (public domain)
and repo tooling under **MIT**.
