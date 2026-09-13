# Quality checklist / ხარისხის ჩეკლისტი

Run before you ship a prompt. Fix what fails — do not report it.

გაუშვი, სანამ პრომპტს გაუშვებ. გაასწორე ის, რაც ვერ გადის — და არა უბრალოდ დააფიქსირე.

---

## 1. Targeting

- [ ] The target tool is identified and named
- [ ] The syntax matches that tool (XML for LLMs, comma descriptors for image, shot spec for video, file-scope for agents)
- [ ] The prompt would be *wrong* for a different tool — if it works everywhere, it is under-specified

## 2. Structure

- [ ] Every `MUST` and `NEVER` sits in the first 30% of the prompt
- [ ] Long reference material comes before the instruction, not after
- [ ] Strongest signal words: `MUST` not `should`, `NEVER` not `avoid`, `exactly 4` not `a few`
- [ ] Directives are positive where a positive form exists
- [ ] No stacked role titles; the role (if any) changes the output

## 3. Specification

- [ ] The verb names a precise operation — not `improve`, `optimise`, `help with`
- [ ] Exactly one objective
- [ ] Output format explicit: shape, length, structure
- [ ] Length is a number
- [ ] Success criterion is binary and checkable
- [ ] Audience stated if the task is explanatory
- [ ] If the format is unusual, one example in the exact target format

## 4. Grounding

- [ ] Factual tasks carry a grounding constraint: `Use ONLY the material below. If not stated, write "not stated". NEVER infer.`
- [ ] Failed prior attempts are listed, if there were any
- [ ] No whole-codebase / whole-document paste where an extract would do

## 5. Scope — agentic prompts only

- [ ] Start state with a reproduction command
- [ ] Target state with a verification command
- [ ] `allowed_files` listed as paths, one per line
- [ ] `forbidden` names the specific expensive mistakes
- [ ] **Stop condition present, with an attempt cap**
- [ ] Failure behaviour for tool calls: stop and report, never fabricate
- [ ] Destructive operations gated behind a stop-and-ask
- [ ] Progress reporting requested

## 6. Reasoning hygiene

- [ ] No request for chain of thought or hidden reasoning
- [ ] No step-by-step scaffolding on a reasoning model
- [ ] No few-shot examples on a reasoning model unless tightly aligned
- [ ] No Tree of Thought / Graph of Thought / Mixture of Experts
- [ ] Analysis tasks carry an audit contract — every conclusion cites what it rests on

## 7. Token efficiency

- [ ] Every sentence changes the output. Delete anything that does not.
- [ ] No emphatic padding ("this is really important", "please be thorough")
- [ ] No restating the rules file inside the task prompt
- [ ] No politeness formulas

## 8. Usability

- [ ] `{{variables}}` marked clearly and named descriptively
- [ ] Variable names are in the prompt's own language — `{{კომპანია}}` in a Georgian prompt
- [ ] Someone who did not write it can use it without asking a question

## 9. Georgian — if the prompt is Georgian or produces Georgian

- [ ] Addresses the model in `შენ`-form imperative
- [ ] No `გთხოვთ` padding
- [ ] Every numeral followed by a singular noun (`200 სიტყვას`, not `200 სიტყვებს`)
- [ ] Reads aloud as Georgian — no English word-order transposition
- [ ] Loanwords where the field uses loanwords; no invented purist compounds
- [ ] No calques: `დარწმუნდი რომ`, `თავისუფლად იგრძენი`, `ტერმინებში`
- [ ] Banned phrases written in Georgian, not English
- [ ] Context referents adapted — `ლარი`, `RS.ge`, `ეროვნული გამოცდები`, `jobs.ge`
- [ ] Naturalness line present when the output is Georgian:
      `დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.`
- [ ] Covers the same functional ground as the English version — verified by function, not sentence count

## 10. Final

- [ ] Read the prompt as if you were the model. Is there anything you would have to guess?
- [ ] If yes, that guess is your next failure. Specify it.

---

## The 60-second version

Six questions. If all six have an answer inside the prompt, ship it.

1. Which tool?
2. What exactly must it do?
3. What shape and length is the answer?
4. What must it never do?
5. How do I know it succeeded?
6. When does it stop?

**60-წამიანი ვერსია** — ექვსი კითხვა. თუ ექვსივეს პასუხი პრომპტშივეა, გაუშვი.

1. რომელი ინსტრუმენტი?
2. ზუსტად რა უნდა გააკეთოს?
3. რა ფორმისა და სიგრძისაა პასუხი?
4. რა არ უნდა გააკეთოს არასდროს?
5. საიდან გავიგებ, რომ გამოვიდა?
6. როდის უნდა გაჩერდეს?
