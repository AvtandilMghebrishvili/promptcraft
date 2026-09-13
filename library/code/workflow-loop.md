# Workflow loop / სამუშაო ციკლი

One prompt per stage, one context per prompt. A context that has planned, implemented and reviewed
the same change carries three positions at once, and the most recent one always wins the argument.
The implementer inherits the planner's assumptions, the reviewer inherits the implementer's, and by
the time something is called "verified" nobody has looked at the work with clean eyes.
So: separate prompts, separate contexts, and every stage's output written so the next stage can
start from that output and nothing else.

ერთი ეტაპი — ერთი პრომპტი, ერთი პრომპტი — ერთი კონტექსტი. კონტექსტი, რომელმაც ერთი და იგივე
ცვლილება დაგეგმა, დააიმპლემენტირა და მერე თვითონვე გადახედა, სამ ურთიერთსაწინააღმდეგო პოზიციას
ატარებს და ბოლო პოზიცია ყოველთვის იმარჯვებს.
იმპლემენტატორი დამგეგმავის დაშვებებს იმემკვიდრებს, რევიუერი — იმპლემენტატორისას, და როცა ვინმე
ამბობს „გადამოწმებულია“, სამუშაოსთვის სუფთა თვალით სინამდვილეში არავის შეუხედავს.
ამიტომ: ცალკე პრომპტი, ცალკე კონტექსტი და ყოველი ეტაპის გამოსავალი ისე დაწერილი, რომ მომდევნო
ეტაპი მხოლოდ მას დაეყრდნოს.

---

## The loop / ციკლი

| # | Stage | Entry | What leaves the stage |
|---|---|---|---|
| 1 | Plan | WL-01 · WL-02 | an ordered plan, and the attack on it |
| 2 | Test | WL-03 | failing tests, and the one command that must go from fail to pass |
| 3 | Implement | WL-04 | a diff scoped to those tests and nothing else |
| 4 | Review | WL-05 · WL-06 | the author's own list, then ranked findings from a reviewer who never saw the conversation |
| 5 | Verify | WL-07 | pasted command output and exit codes |
| 6 | Remember | WL-08 | a rules-file entry, ready to paste |
| 7 | Improve | WL-09 | one standing rule or hook, with its cost |

Why not one mega-prompt: a context that already argued for a plan cannot review that plan — it
reviews its own reasoning and approves it. Stage isolation is the only way to get a genuine second
opinion out of the same model.

| # | ეტაპი | ჩანაწერი | რა გამოდის ეტაპიდან |
|---|---|---|---|
| 1 | დაგეგმვა | WL-01 · WL-02 | დალაგებული გეგმა და მასზე შეტევა |
| 2 | ტესტი | WL-03 | ჩავარდნილი ტესტები და ერთი ბრძანება, რომელმაც ჩავარდნიდან გატარებამდე უნდა მივიდეს |
| 3 | იმპლემენტაცია | WL-04 | დიფი, რომელიც მხოლოდ ამ ტესტებს ეხება |
| 4 | რევიუ | WL-05 · WL-06 | ჯერ ავტორის საკუთარი სია, მერე რანჟირებული შენიშვნები რევიუერისგან, რომელსაც საუბარი არ უნახავს |
| 5 | ვერიფიკაცია | WL-07 | ჩასმული გამოსავალი და გასვლის კოდები |
| 6 | დამახსოვრება | WL-08 | წესების ფაილის ჩანაწერი, ჩასასმელად მზა |
| 7 | გაუმჯობესება | WL-09 | ერთი მუდმივი წესი ან ჰუკი და მისი ფასი |

რატომ არა ერთი დიდი პრომპტი: კონტექსტი, რომელმაც გეგმა უკვე დაიცვა, ამ გეგმას ვერ გადახედავს —
ის საკუთარ მსჯელობას ხედავს და მას იწონებს. ეტაპების იზოლაცია ერთადერთი გზაა, ერთივე მოდელისგან
ნამდვილი მეორე აზრი მიიღო.

---

### WL-01 · Plan only, write no code
`claude-code` `cursor` `claude` — planning, scoping

**EN**
```
Plan an implementation. Produce the plan. Write no code.

<task>
{{task}}
</task>

<repo_facts>
Stack and test command: {{stack_and_test_command}}
Constraints I already know about: {{constraints}}
</repo_facts>

You may READ any file in the repo and run read-only commands: `rg`, `git log`, `git show`, `cat`,
`ls`, `npm run typecheck`.
NEVER create, edit, move or delete a file — not a stub, not a scratch file, not a notes file.
NEVER run a command that changes state: no `npm install`, no formatter, no migration, no
`git checkout`, no `git stash`.
Verify you stayed inside that: `git status --porcelain` must print nothing when you finish.

Base every step on a file you actually opened. If a step needs a fact the repo does not give you,
write `UNKNOWN: <what>` inside that step instead of assuming a value.

Output exactly these four sections:

1. STEPS — numbered, in the order they must be done. For each step:
   · what it changes, in one sentence
   · the files it touches, by path
   · risk — LOW (isolated, reversible) / MEDIUM (a caller's behaviour changes) / HIGH (schema,
     auth, money, data loss, a public interface), plus one line on what breaks if it goes wrong
   · the command that would show that step worked

2. THE DECISION FOR A HUMAN — exactly one. The choice the repo cannot settle by itself: a trade-off
   between two designs, a behaviour change a user would notice, a migration that cannot be undone.
   Give both options, the cost of each, and which you would take if forced to choose. If you believe
   there are several, take the one that is most expensive to reverse and leave the rest in STEPS.

3. WHAT I AM NOT DOING — the adjacent work this plan deliberately leaves alone, and why.

4. OPEN UNKNOWNS — every `UNKNOWN:` gathered, each with the command or the question that resolves it.

At most 8 steps. If the task genuinely needs more, it is two tasks — say so and split it rather
than writing step 9.

Handoff: this plan is the input to WL-02 and then to WL-04. Write it for a reader with no memory of
this conversation: no "as discussed", no pronoun pointing at something you said earlier.
```

**KA**
```
დაგეგმე იმპლემენტაცია. შედეგი გეგმაა. კოდი არ დაწერო.

<task>
{{ამოცანა}}
</task>

<repo_facts>
სტეკი და ტესტის ბრძანება: {{სტეკი_და_ტესტი}}
შეზღუდვები, რომლებიც უკვე ვიცი: {{შეზღუდვები}}
</repo_facts>

შეგიძლია წაიკითხო რეპოს ნებისმიერი ფაილი და გაუშვა მხოლოდ კითხვადი ბრძანებები: `rg`, `git log`,
`git show`, `cat`, `ls`, `npm run typecheck`.
არასდროს შექმნა, შეასწორო, გადაიტანო ან წაშალო ფაილი — არც ჩანასახი, არც სამუშაო და არც სანოტო ფაილი.
არასდროს გაუშვა ბრძანება, რომელიც მდგომარეობას ცვლის: არც `npm install`, არც ფორმატერი, არც
მიგრაცია, არც `git checkout`, არც `git stash`.
გადაამოწმე, რომ ამ ფარგლებში დარჩი: დასრულებისას `git status --porcelain` ცარიელი უნდა იყოს.

ყოველი ეტაპი იმ ფაილს დააფუძნე, რომელიც მართლა გახსენი. თუ ეტაპს ისეთი ფაქტი სჭირდება, რომელსაც
რეპო არ გაძლევს, იმავე ეტაპში ჩაწერე `UNKNOWN: <რა>` და მნიშვნელობა არ გამოიცნო.

გამოსავალი — ზუსტად ეს ოთხი სექცია:

1. ეტაპები — დანომრილი, შესრულების თანმიმდევრობით. თითოეულზე:
   · რას ცვლის, ერთი წინადადებით
   · რომელ ფაილებს ეხება, მისამართებით
   · რისკი — დაბალი (იზოლირებული, უკან დასაბრუნებელი) / საშუალო (გამომძახებლის ქცევა იცვლება) /
     მაღალი (სქემა, ავტორიზაცია, ფული, მონაცემის დაკარგვა, საჯარო ინტერფეისი) და ერთი ხაზი იმაზე,
     რა ფუჭდება, თუ ეს ეტაპი ცუდად წავა
   · ბრძანება, რომელიც აჩვენებდა, რომ ეს ეტაპი გამოვიდა

2. გადაწყვეტილება ადამიანისთვის — ზუსტად ერთი. არჩევანი, რომელსაც რეპო თვითონ ვერ წყვეტს:
   ორ დიზაინს შორის კომპრომისი, ქცევის ცვლილება, რომელსაც მომხმარებელი შეამჩნევს, ან მიგრაცია,
   რომელიც უკან აღარ ბრუნდება. დაწერე ორივე ვარიანტი, თითოეულის ფასი და რომელს აირჩევდი, თუ
   არჩევა აუცილებელი იქნებოდა. თუ გგონია, რომ რამდენიმეა, აიღე ის, რომლის უკან დაბრუნებაც ყველაზე
   ძვირია, დანარჩენი კი ეტაპებში დატოვე.

3. რას არ ვაკეთებ — მეზობელი სამუშაო, რომელსაც ეს გეგმა შეგნებულად არ ეხება, და რატომ.

4. ღია უცნობები — ყველა `UNKNOWN:` ერთად, თითოეულთან ბრძანება ან კითხვა, რომელიც მას ხსნის.

მაქსიმუმ 8 ეტაპი. თუ ამოცანას მართლა მეტი სჭირდება, ეს ორი ამოცანაა — ეს დაწერე და გაყავი,
მე-9 ეტაპის დაწერის ნაცვლად.

გადაცემა: ეს გეგმა WL-02-ის, შემდეგ კი WL-04-ის შესატანი მასალაა. დაწერე ისე, თითქოს მკითხველს
ეს საუბარი არ უნახავს: არც „როგორც შევთანხმდით“, არც ნაცვალსახელი, რომელიც ადრე ნათქვამზე მიუთითებს.
```

---

### WL-02 · Critique the plan from a fresh context
`claude-code` `claude` `gpt` — review, planning

**EN**
```
You have not seen the conversation that produced this plan. That is the point. Attack it.

<plan>
{{plan}}
</plan>

<requirement>
{{requirement}}
</requirement>

You are not the author, and you are not rewriting the plan. Do not produce a corrected plan, a
"step 4b", or a section headed "here is how I would do it instead". You report; someone else decides.

Do not edit any file. Read-only commands only: `rg`, `git log`, `git show`, `cat`.
`git status --porcelain` must print nothing when you finish.

Output:

1. ASSUMPTIONS THE PLAN RESTS ON — quote the plan's own claim, then say whether it holds in this
   repo, with the file and line you checked, or write `NOT CHECKABLE HERE`. An assumption you could
   not check is a finding, not a footnote.

2. WHAT THIS BREAKS — for each step, the callers, tests, cron jobs, dashboards and consumers the
   plan does not name. Go and find them: `rg -n "<symbol>" --type ts`, `git log -S"<symbol>"`,
   `rg -n "<route>" tests/`. Name the file, not the possibility.

3. WHAT IS MISSING — ranked, each with the failure it lets through written as one concrete
   sentence: "a request with `items: []` reaches the proration call and divides by zero", not
   "error handling could be improved".

4. THE STEP I WOULD DELETE — the one step whose cost is highest relative to what the requirement
   actually asks for. If every step earns its place, say so in one line.

5. VERDICT — one of: PROCEED · PROCEED AFTER FIXING <n> · DO NOT PROCEED, plus the single reason.

At most 7 findings across sections 2 and 3 combined. If you have more, you are listing preferences
rather than defects — keep the 7 that would cost the most to discover later.

NEVER soften a finding because the plan is well written. A tidy plan resting on a wrong assumption
is more dangerous than a sloppy one.
NEVER invent a caller, a file or a line number you did not open.

Handoff: this goes back to WL-01's author, who revises the plan; the revised plan — not this
critique — is what WL-03 and WL-04 receive.
```

**KA**
```
შენ ეს გეგმა პირველად ხედავ და იმ საუბარს, რომელმაც ის წარმოშვა, არ იცნობ. სწორედ ეს არის საჭირო.
შეუტიე მას.

<plan>
{{გეგმა}}
</plan>

<requirement>
{{მოთხოვნა}}
</requirement>

შენ ავტორი არ ხარ და გეგმას არ გადაწერ. არც შესწორებული გეგმა დაწერო, არც „ეტაპი 4ბ“, არც სექცია
სათაურით „მე ასე გავაკეთებდი“. შენ შენიშვნებს წერ, გადაწყვეტილებას კი სხვა იღებს.

არცერთი ფაილი არ შეასწორო. მხოლოდ კითხვადი ბრძანებები: `rg`, `git log`, `git show`, `cat`.
დასრულებისას `git status --porcelain` ცარიელი უნდა იყოს.

გამოსავალი:

1. დაშვებები, რომლებზეც გეგმა დგას — ციტირებულად მოიყვანე გეგმის საკუთარი მტკიცება და დაწერე,
   მართლდება თუ არა ის ამ რეპოში: მიუთითე ფაილი და ხაზი, რომელიც შეამოწმე, ან დაწერე
   `NOT CHECKABLE HERE`. დაშვება, რომელიც ვერ შეამოწმე, შენიშვნაა და არა სქოლიო.

2. რას ამტვრევს ეს — ყოველ ეტაპზე დაასახელე გამომძახებლები, ტესტები, cron-ამოცანები, დაშბორდები
   და მომხმარებელი სერვისები, რომლებსაც გეგმა არ ახსენებს. მოძებნე ისინი:
   `rg -n "<symbol>" --type ts`, `git log -S"<symbol>"`, `rg -n "<route>" tests/`.
   დაასახელე ფაილი და არა შესაძლებლობა.

3. რა აკლია — რანჟირებული, თითოეულთან ის ჩავარდნა, რომელსაც გეგმა უშვებს, ერთი კონკრეტული
   წინადადებით: „მოთხოვნა `items: []`-ით პროპორციულ გაანგარიშებამდე აღწევს და ნულზე იყოფა“,
   და არა „შეცდომების დამუშავება გასაუმჯობესებელია“.

4. ეტაპი, რომელსაც ამოვიღებდი — ერთი ეტაპი, რომლის ფასიც ყველაზე მაღალია იმასთან შედარებით, რასაც
   მოთხოვნა რეალურად ითხოვს. თუ ყველა ეტაპი თავის ადგილს იმსახურებს, ეს ერთ ხაზში დაწერე.

5. დასკვნა — ერთი მათგანი: გააგრძელე · გააგრძელე <n> შესწორების შემდეგ · არ გააგრძელო,
   და ერთი მიზეზი.

მე-2 და მე-3 სექციაში ჯამში მაქსიმუმ 7 შენიშვნა. თუ მეტი გაქვს, უკვე გემოვნებას წერ და არა
დეფექტს — დატოვე ის 7 შენიშვნა, რომელთა მოგვიანებით აღმოჩენაც ყველაზე ძვირი დაჯდება.

არასდროს დაარბილო შენიშვნა იმიტომ, რომ გეგმა ლამაზად არის დაწერილი. მოწესრიგებული გეგმა მცდარ
დაშვებაზე უფრო საშიშია, ვიდრე უწესრიგო.
არასდროს გამოიგონო გამომძახებელი, ფაილი ან ხაზის ნომერი, რომელიც არ გაგიხსნია.

გადაცემა: ეს ბრუნდება WL-01-ის ავტორთან, რომელიც გეგმას ასწორებს; WL-03-სა და WL-04-ს შესწორებული
გეგმა გადაეცემა და არა ეს შენიშვნები.
```

---

### WL-03 · Write the failing tests first
`claude-code` `cursor` `codex` — testing, tdd

**EN**
```
Write the tests that define done. Write no implementation.

<requirement>
{{requirement}}
</requirement>

<plan>
{{revised_plan}}
</plan>

<start_state>
The behaviour does not exist yet: `src/billing/proration.ts` exports nothing named `prorate`.
Reproduce: `rg -n "export function prorate" src/` → no output.
The suite is green right now: `npm test` exits 0.
</start_state>

<target_state>
`npm test -- proration` FAILS, and it fails on assertions about behaviour — not on a syntax error
and not on a missing import you could have avoided writing.
Every other test still passes: `npm test` fails only in tests/billing/proration.test.ts.
</target_state>

<allowed_files>
tests/billing/proration.test.ts   (create it)
tests/billing/fixtures/subscriptions.json   (create it if you need fixtures)
</allowed_files>

<forbidden>
NEVER create or edit any file under src/. Not a stub, not an empty function, not a type declaration.
If the test cannot import the module, that IS the correct failing state — leave it failing.
NEVER write a test that passes today. A green test at this stage defines nothing.
NEVER write `expect(result).toBeDefined()` or `assert result is not None` as the whole assertion.
NEVER mock the unit under test.
NEVER install a test library — the repo uses vitest and it is already configured.
</forbidden>

<stop_condition>
Stop when `npm test -- proration` fails on assertions and `npm test` fails in no other file.
Maximum 2 attempts at getting the test file to run at all. If it still cannot be collected after
the second, STOP and report the collection error verbatim — do not start writing src/ to fix it.
</stop_condition>

Output, above the test file:

1. THE COMMAND — the single command that must go from fail to pass:
   `npm test -- proration`. Print the current failure output under it.
2. THE CASES — one line per test: the input, the expected output, and which line of <requirement>
   it comes from. A case with no line of the requirement behind it does not belong here.
3. WHAT THESE TESTS DO NOT COVER — what stays unverified after they all go green.

Cover the edges, not three shapes of the happy path: a zero-length period, a cancellation on the
first day of the cycle, a plan change on the last day, and an amount that does not divide evenly.

Handoff: THE COMMAND is WL-04's stop condition and one row of WL-07's verification table.
```

**KA**
```
დაწერე ტესტები, რომლებიც განსაზღვრავს, რა ნიშნავს „გაკეთებულია“. იმპლემენტაცია არ დაწერო.

<requirement>
{{მოთხოვნა}}
</requirement>

<plan>
{{შესწორებული_გეგმა}}
</plan>

<start_state>
ეს ქცევა ჯერ არ არსებობს: `src/billing/proration.ts` არაფერს აექსპორტებს სახელით `prorate`.
გასამეორებელი ბრძანება: `rg -n "export function prorate" src/` → ცარიელი გამოსავალი.
ტესტები ამჟამად მწვანეა: `npm test` სრულდება 0 კოდით.
</start_state>

<target_state>
`npm test -- proration` ვარდება და ვარდება ქცევის მტკიცებებზე — არც სინტაქსის შეცდომაზე და არც
იმპორტზე, რომლის დაწერაც თავიდან შეგეძლო აგერიდებინა.
დანარჩენი ტესტები კვლავ გადის: `npm test` მხოლოდ tests/billing/proration.test.ts-ში ვარდება.
</target_state>

<allowed_files>
tests/billing/proration.test.ts   (შექმენი)
tests/billing/fixtures/subscriptions.json   (შექმენი, თუ ფიქსტურები დაგჭირდება)
</allowed_files>

<forbidden>
არასდროს შექმნა ან შეასწორო ფაილი src/-ის ქვეშ. არც ჩანასახი, არც ცარიელი ფუნქცია, არც ტიპის აღწერა.
თუ ტესტი მოდულს ვერ აიმპორტებს, სწორედ ეს არის სწორი ჩავარდნილი მდგომარეობა — ჩავარდნილი დატოვე.
არასდროს დაწერო ტესტი, რომელიც დღეს გადის. ამ ეტაპზე მწვანე ტესტი არაფერს განსაზღვრავს.
არასდროს დაწერო `expect(result).toBeDefined()` ან `assert result is not None` ერთადერთ მტკიცებად.
არასდროს გააკეთო mock იმ ერთეულზე, რომელსაც ტესტავ.
არასდროს დააინსტალირო სატესტო ბიბლიოთეკა — რეპო vitest-ზე მუშაობს და ის უკვე კონფიგურირებულია.
</forbidden>

<stop_condition>
შეჩერდი, როცა `npm test -- proration` მტკიცებებზე ვარდება და `npm test` სხვა ფაილში აღარ ვარდება.
ტესტის ფაილის საერთოდ ასამუშავებლად მაქსიმუმ 2 მცდელობა. თუ მეორის შემდეგაც ვერ აიკრიფება,
შეჩერდი და სიტყვასიტყვით მოახსენე შეცდომა — src/-ის წერა მის გასასწორებლად არ დაიწყო.
</stop_condition>

ტესტის ფაილის ზემოთ დაწერე:

1. ბრძანება — ერთი ბრძანება, რომელმაც ჩავარდნიდან გატარებამდე უნდა მივიდეს:
   `npm test -- proration`. ქვემოთ დაბეჭდე მისი ამჟამინდელი ჩავარდნის გამოსავალი.
2. შემთხვევები — თითო ტესტზე ერთი ხაზი: შემავალი მონაცემი, მოსალოდნელი შედეგი და <requirement>-ის
   რომელი ხაზიდან მოდის ის. შემთხვევას, რომლის უკანაც მოთხოვნის ხაზი არ დგას, აქ ადგილი არ აქვს.
3. რას არ ფარავს ეს ტესტები — რა რჩება გადაუმოწმებელი მაშინაც კი, როცა ყველა მათგანი გამწვანდება.

დაფარე კიდეები და არა წარმატებული სცენარის სამი ვარიაცია: ნულოვანი ხანგრძლივობის პერიოდი,
გაუქმება ციკლის პირველ დღეს, გეგმის შეცვლა ბოლო დღეს და თანხა, რომელიც მთლიანად არ იყოფა.

გადაცემა: „ბრძანება“ არის WL-04-ის გაჩერების პირობა და WL-07-ის ვერიფიკაციის ცხრილის ერთი სტრიქონი.
```

---

### WL-04 · Implement against the tests, nothing else
`claude-code` `cursor` `windsurf` — implementation, file-scope

**EN**
```
Make the tests from WL-03 pass. Make nothing else happen.

<plan>
{{revised_plan}}
</plan>

<start_state>
`npm test -- proration` fails: 6 of 6 assertions in tests/billing/proration.test.ts fail, the first
with `TypeError: prorate is not a function`.
Reproduce: `npm test -- proration`.
Everything else is green: `npm test` fails only in that file, `npm run typecheck` → 0 errors.
</start_state>

<target_state>
`npm test -- proration` exits 0, and `npm test` exits 0 — no other test changed behaviour.
`npm run typecheck` → 0 errors.
`npx eslint src/billing` → no output.
</target_state>

<allowed_files>
src/billing/proration.ts   (new)
src/billing/index.ts        (one export line)
</allowed_files>

<forbidden>
NEVER edit tests/billing/proration.test.ts or anything else under tests/. The tests are the
specification. If an assertion is genuinely wrong, STOP and name it and say why — do not change it.
NEVER implement anything <plan> does not list. No extra parameter, no options object, no feature
flag, no "while I was here" tidy of a neighbouring function.
NEVER special-case a test input to make an assertion pass.
NEVER add `any`, `@ts-expect-error` or a cast to silence a type error.
NEVER install a package.
NEVER commit, amend or push. Leave the work in the working tree.
NEVER touch a file outside <allowed_files>. If the task needs one, STOP and tell me which and why.
</forbidden>

<stop_condition>
Stop when `npm test`, `npm run typecheck` and `npx eslint src/billing` all pass.
Maximum 3 attempts after the first full test run. After the third, STOP and report: the diff so
far, which assertions still fail, their exact output, and your best hypothesis. Do not start over
from scratch and do not switch approach a fourth time.
</stop_condition>

After each file you write, print its path and one line on what it does.

Handoff: `git diff` plus the new-file list from `git status --porcelain` is the input to WL-05 and
WL-06. Do not squash, amend, reformat or tidy it — the reviewer must read what you actually did.
```

**KA**
```
გაატარე WL-03-ის ტესტები. სხვა არაფერი მოხდეს.

<plan>
{{შესწორებული_გეგმა}}
</plan>

<start_state>
`npm test -- proration` ვარდება: tests/billing/proration.test.ts-ის 6 მტკიცებიდან 6 ვარდება,
პირველი — შეცდომით `TypeError: prorate is not a function`.
გასამეორებელი ბრძანება: `npm test -- proration`.
დანარჩენი მწვანეა: `npm test` მხოლოდ ამ ფაილში ვარდება, `npm run typecheck` → 0 შეცდომა.
</start_state>

<target_state>
`npm test -- proration` სრულდება 0 კოდით და `npm test` სრულდება 0 კოდით — სხვა არცერთ ტესტს ქცევა
არ შეცვლია.
`npm run typecheck` → 0 შეცდომა.
`npx eslint src/billing` → ცარიელი გამოსავალი.
</target_state>

<allowed_files>
src/billing/proration.ts   (ახალი)
src/billing/index.ts        (ერთი ხაზი ექსპორტისთვის)
</allowed_files>

<forbidden>
არასდროს შეასწორო tests/billing/proration.test.ts და არაფერი tests/-ის ქვეშ. ტესტები
სპეციფიკაციაა. თუ რომელიმე მტკიცება მართლა მცდარია, შეჩერდი, დაასახელე ის და ახსენი რატომ —
შეცვლა არ სცადო.
არასდროს დააიმპლემენტირო ის, რაც <plan>-ში არ წერია. არც დამატებითი პარამეტრი, არც ოპციების
ობიექტი, არც ფიჩერ-ფლაგი, არც მეზობელი ფუნქციის „რაკი აქ ვიყავი“ ტიპის დალაგება.
არასდროს გაუკეთო სატესტო მნიშვნელობას ცალკე შემთხვევა მხოლოდ იმისთვის, რომ მტკიცება გავიდეს.
არასდროს დაამატო `any`, `@ts-expect-error` ან cast ტიპის შეცდომის ჩასაჩუმებლად.
არასდროს დააინსტალირო პაკეტი.
არასდროს გააკეთო კომიტი, amend ან push. სამუშაო ხეში დატოვე.
არასდროს შეეხო ფაილს <allowed_files>-ის გარეთ. თუ ამოცანას ასეთი ფაილი სჭირდება, შეჩერდი და
დამისახელე რომელი და რატომ.
</forbidden>

<stop_condition>
შეჩერდი, როცა `npm test`, `npm run typecheck` და `npx eslint src/billing` სამივე გაივლის.
პირველი სრული გაშვების შემდეგ მაქსიმუმ 3 მცდელობა. მესამის შემდეგ შეჩერდი და მოახსენე: აქამდე
გაკეთებული დიფი, რომელი მტკიცებები ვარდება ჯერ კიდევ, მათი ზუსტი გამოსავალი და რა ვარაუდი გაქვს.
თავიდან არ დაიწყო და მეოთხედ მიდგომა არ შეცვალო.
</stop_condition>

ყოველი დაწერილი ფაილის შემდეგ დაბეჭდე მისი მისამართი და ერთი ხაზი იმაზე, რას აკეთებს.

გადაცემა: `git diff` და `git status --porcelain`-ის ახალი ფაილების სია WL-05-ისა და WL-06-ის
შესატანი მასალაა. არ შეკუმშო, არ გააკეთო amend, არ გადააფორმატო და არ დაალაგო — რევიუერმა ზუსტად
ის უნდა წაიკითხოს, რაც გააკეთე.
```

---

### WL-05 · Self-review the diff before handoff
`claude-code` `cursor` `cline` — review, self-check

**EN**
```
Review your own diff against the plan before anyone else sees it. Change nothing.

<plan>
{{revised_plan}}
</plan>

<diff>
Produce it yourself: `git diff`, plus `git status --porcelain` for files you added.
</diff>

Read the diff line by line. Do not work from memory — your memory of what you intended is exactly
the thing being tested here, and the diff is the only evidence.

Do not edit any file during this task. This produces a list, not a commit.
NEVER fix something you find. Write it down and move on. Fixing while reviewing turns the review
into another implementation pass that nobody reviews.
NEVER re-run the tests here — that is WL-07's job, and a green suite is not what this stage checks.

First line of your output: the file count from `git diff --stat` and the file count in
<allowed_files>. If they differ, say so before anything else.

Then exactly two lists and one line:

1. IN THE DIFF, NOT IN THE PLAN — every change the plan did not ask for, with file and line:
   a renamed variable, a reordered import, a changed log message, a widened type, an extracted
   helper, a formatting sweep. Mark each NEEDED (the plan could not work without it — say why) or
   REMOVE (scope creep).

2. IN THE PLAN, NOT IN THE DIFF — every step of <plan> with no matching change, marked
   DONE ELSEWHERE (name the file) · NOT NEEDED (say why the plan was wrong) · NOT DONE.

3. ONE LINE — the change in this diff a reviewer is most likely to miss, and why it is easy to miss.

If both lists are empty, say so in one line. That is a valid and good result; do not manufacture
an entry to look thorough.

Handoff: WL-06 gets the diff and the requirement only — it never sees this list. This one goes to
me, so I can tell whether the diff still matches the plan I approved.
```

**KA**
```
გადახედე საკუთარ დიფს გეგმასთან შედარებით, სანამ მას სხვა ნახავს. არაფერი შეცვალო.

<plan>
{{შესწორებული_გეგმა}}
</plan>

<diff>
თვითონ აიღე: `git diff` და დამატებული ფაილებისთვის `git status --porcelain`.
</diff>

წაიკითხე დიფი ხაზ-ხაზ. მეხსიერებით არ იმუშაო — სწორედ შენი მეხსიერება იმისა, თუ რა გინდოდა,
არის აქ შესამოწმებელი, ერთადერთი მტკიცებულება კი დიფია.

ამ ამოცანის მსვლელობისას არცერთი ფაილი არ შეასწორო. შედეგი სიაა და არა კომიტი.
არასდროს გაასწორო ის, რასაც იპოვი. ჩაწერე და გააგრძელე. რევიუს დროს გასწორება რევიუს კიდევ ერთ
იმპლემენტაციის ეტაპად აქცევს, რომელსაც უკვე აღარავინ ხედავს.
არასდროს გაუშვა აქ ტესტები — ეს WL-07-ის საქმეა და მწვანე ტესტები ამ ეტაპზე შესამოწმებელი არ არის.

გამოსავლის პირველი ხაზი: ფაილების რაოდენობა `git diff --stat`-ის მიხედვით და ფაილების რაოდენობა
<allowed_files>-ში. თუ ისინი არ ემთხვევა, ეს ყველაფერზე ადრე დაწერე.

შემდეგ ზუსტად ორი სია და ერთი ხაზი:

1. დიფშია, გეგმაში არ არის — ყოველი ცვლილება, რომელიც გეგმას არ უთხოვია, ფაილითა და ხაზით:
   გადარქმეული ცვლადი, გადალაგებული იმპორტი, შეცვლილი ლოგის ტექსტი, გაფართოებული ტიპი, გამოტანილი
   დამხმარე ფუნქცია, ფორმატირების გასწორება. თითოეული მონიშნე: საჭირო (გეგმა მის გარეშე ვერ
   იმუშავებდა — დაწერე რატომ) ან ამოსაღები (არეალის გაფართოებაა).

2. გეგმაშია, დიფში არ არის — <plan>-ის ყოველი ეტაპი, რომელსაც ცვლილება არ შეესაბამება, მონიშნული:
   სხვაგან გაკეთდა (დაასახელე ფაილი) · საჭირო არ იყო (დაწერე, რატომ იყო გეგმა მცდარი) · არ გაკეთდა.

3. ერთი ხაზი — ამ დიფის ის ცვლილება, რომელსაც რევიუერი ყველაზე დიდი ალბათობით გამოტოვებს,
   და რატომაა მისი გამოტოვება ადვილი.

თუ ორივე სია ცარიელია, ეს ერთ ხაზში დაწერე. ეს კარგი და სრულფასოვანი შედეგია — საფუძვლიანობის
საჩვენებლად ჩანაწერი არ გამოიგონო.

გადაცემა: WL-06 მხოლოდ დიფსა და მოთხოვნას იღებს — ამ სიას ის ვერასდროს ნახავს. ეს სია მე მეკუთვნის,
რომ დავინახო, კვლავ ემთხვევა თუ არა დიფი იმ გეგმას, რომელიც დავამტკიცე.
```

---

### WL-06 · Fresh-context review of the diff
`claude-code` `claude` `gpt` — review, code-review

**EN**
```
Review a diff. You are being given the diff and the requirement, and nothing else: no plan
discussion, no implementation conversation, no author's explanation. That is deliberate — whatever
the implementer assumed, you must not inherit it.

<requirement>
{{requirement}}
</requirement>

<diff>
{{diff}}
</diff>

If a hunk only makes sense with context you were not given, that is a finding, not a gap in your
briefing. Write it as:
`UNEXPLAINED: <file>:<line> — <what it does that <requirement> does not ask for>`.

You may read the repo to check a caller, a type or an existing test. Do not edit anything, and do
not write a corrected version of any hunk — writing the patch is the author's job, and reading your
own patch is how a reviewer stops checking and starts defending.

Report AT MOST 7 findings, ranked by the cost of missing them. Fewer is fine; padding a review to
seven is worse than reporting three. For each:

  · FILE:LINE
  · SEVERITY — BLOCKER (wrong result, data loss, security, breaks an existing caller) /
    MAJOR (correct today, fails on a real input) / MINOR (maintainability)
  · THE FAILURE SCENARIO — concrete inputs and state → the wrong output or the crash.
    "Could be null" is not a finding. "`prorate(sub, 0)` on a subscription cancelled mid-cycle
    returns `-Infinity`, and we write that straight into `invoices.amount_minor`" is a finding.
  · THE CHEAPEST CHECK — the command, test case or query that confirms or kills it.

Rules:
- NEVER report style, formatting, naming or import order unless it changes behaviour. A linter is
  cheaper than you are.
- NEVER report a finding you cannot attach a concrete failure scenario to. Delete it instead.
- NEVER approve because the diff is small, and never object because it is large.
- NEVER assume a test covers something because a test file was touched. Open it.
- If the diff does not satisfy <requirement> at all, say that in the first line and stop ranking.

End with one line: APPROVE · APPROVE WITH <n> FIXES · REJECT, and the single finding that decides it.

Handoff: BLOCKER and MAJOR findings go back to WL-04 as a new scoped task — one task per finding,
with its failure scenario as the start state. Nothing here goes to WL-07 until it is fixed.
```

**KA**
```
გადახედე დიფს. შენ გეძლევა დიფი და მოთხოვნა — სხვა არაფერი: არც გეგმის განხილვა, არც
იმპლემენტაციის საუბარი, არც ავტორის ახსნა. ეს შეგნებულად ხდება: რაც იმპლემენტატორს ეგონა,
შენ არ უნდა გადმოგყვეს.

<requirement>
{{მოთხოვნა}}
</requirement>

<diff>
{{დიფი}}
</diff>

თუ რომელიმე ნაწილს აზრი მხოლოდ იმ კონტექსტში აქვს, რომელიც არ მოგეცი, ეს შენიშვნაა და არა
შენი მასალის ხარვეზი. ასე დაწერე:
`UNEXPLAINED: <file>:<line> — <რას აკეთებს, რასაც <requirement> არ ითხოვს>`.

შეგიძლია რეპო წაიკითხო, რომ გამომძახებელი, ტიპი ან არსებული ტესტი შეამოწმო. არაფერი შეასწორო და
არცერთი ნაწილის შესწორებული ვერსია არ დაწერო — შესწორება ავტორის საქმეა, საკუთარი შესწორების
კითხვა კი სწორედ ის მომენტია, როცა რევიუერი შემოწმებას წყვეტს და თავის დაცვას იწყებს.

მოახსენე მაქსიმუმ 7 შენიშვნა, რანჟირებული მათი გამოტოვების ფასის მიხედვით. ნაკლები ნორმალურია;
რევიუს შვიდამდე გაბერვა უარესია, ვიდრე სამი შენიშვნა. თითოეულზე:

  · FILE:LINE
  · სიმძიმე — BLOCKER (მცდარი შედეგი, მონაცემის დაკარგვა, უსაფრთხოება, არსებული გამომძახებლის
    გატეხვა) / MAJOR (დღეს სწორია, რეალურ მონაცემზე ჩავარდება) / MINOR (მხარდაჭერადობა)
  · ჩავარდნის სცენარი — კონკრეტული შემავალი მონაცემი და მდგომარეობა → მცდარი შედეგი ან კრახი.
    „შეიძლება null იყოს“ შენიშვნა არ არის. „`prorate(sub, 0)` ციკლის შუაში გაუქმებულ გამოწერაზე
    აბრუნებს `-Infinity`-ს და ჩვენ ამას პირდაპირ `invoices.amount_minor`-ში ვწერთ“ — შენიშვნაა.
  · ყველაზე იაფი შემოწმება — ბრძანება, სატესტო შემთხვევა ან მოთხოვნა, რომელიც მას დაადასტურებს
    ან მოკლავს.

წესები:
- არასდროს მოახსენო სტილი, ფორმატირება, სახელები ან იმპორტების თანმიმდევრობა, თუ ისინი ქცევას არ
  ცვლიან. ლინტერი შენზე იაფია.
- არასდროს მოახსენო შენიშვნა, რომელსაც კონკრეტულ ჩავარდნის სცენარს ვერ მიაბამ. სანაცვლოდ წაშალე.
- არასდროს დაეთანხმო იმიტომ, რომ დიფი პატარაა, და არასდროს გაასაჩივრო იმიტომ, რომ დიდია.
- არასდროს ჩათვალო, რომ ტესტი რამეს ფარავს, მხოლოდ იმიტომ, რომ ტესტის ფაილს შეეხნენ. გახსენი ის.
- თუ დიფი <requirement>-ს საერთოდ არ აკმაყოფილებს, ეს პირველივე ხაზში დაწერე და რანჟირება შეწყვიტე.

დაასრულე ერთი ხაზით: დამტკიცდეს · დამტკიცდეს <n> შესწორების შემდეგ · უარყოფილია,
და დაასახელე ერთი შენიშვნა, რომელიც ამას წყვეტს.

გადაცემა: BLOCKER და MAJOR შენიშვნები WL-04-ს უბრუნდება ახალ, შემოსაზღვრულ ამოცანად — თითო
შენიშვნაზე თითო ამოცანა, საწყის მდგომარეობად კი მისი ჩავარდნის სცენარი. მათ გასწორებამდე
WL-07-მდე არაფერი მიდის.
```

---

### WL-07 · Verify by running, never by reading
`claude-code` `cursor` `codex` — verification, ci

**EN**
```
Run the verification commands and report what they actually printed. Reading the diff proves nothing.

<commands>
1. `npm ci`
2. `npm run typecheck`
3. `npm test`
4. `npm test -- proration`
5. `npx eslint src/billing`
6. `go test ./...`          (only if this repo has a Go service — drop the row if not)
</commands>

Run every command in <commands>, in that order, on the branch under test. For each one report: the
command, the exit code, and the last 20 lines of its output pasted verbatim. If you cut output, say
how many lines you cut and from which end.

NEVER report a command as passing unless you ran it in this session and saw its output.
NEVER infer a result from the code, the diff, the plan, a review or an earlier run. If you did not
see the output, the status is NOT RUN — and NOT RUN is an acceptable answer here. A fabricated pass
is not.
NEVER edit a file to make a command pass. If a command fails, it failed; that is the report.
NEVER re-run a failing command with different flags, a narrower path or a disabled rule and report
that run instead. Report the command as written in <commands>.
NEVER paraphrase output. Paste it.
NEVER install or upgrade anything to get a command to run.

Run each command once. A second run is allowed only when the first failure names a transient cause
(network, port already in use, a container that had not started) — and then report BOTH runs.

If a command cannot run at all — missing binary, missing environment variable, no network — report
`CANNOT RUN: <command> — <exact error>` and continue with the rest of the list.

Output:
1. THE TABLE — command · exit code · PASS / FAIL / NOT RUN / CANNOT RUN
2. THE OUTPUT — pasted, for every row that is not PASS
3. ONE LINE — SHIP or DO NOT SHIP, and the row that decides it. If any row is FAIL, NOT RUN or
   CANNOT RUN, the answer is DO NOT SHIP.

Handoff: this table is the evidence WL-08 records. A lesson without a row here is a story, not a
finding.
```

**KA**
```
გაუშვი გადამოწმების ბრძანებები და მოახსენე, რა დაბეჭდეს მათ სინამდვილეში. დიფის კითხვა არაფერს ამტკიცებს.

<commands>
1. `npm ci`
2. `npm run typecheck`
3. `npm test`
4. `npm test -- proration`
5. `npx eslint src/billing`
6. `go test ./...`          (მხოლოდ თუ რეპოში Go-სერვისია — თუ არა, ეს სტრიქონი ამოაგდე)
</commands>

გაუშვი <commands>-ის ყოველი ბრძანება ამავე თანმიმდევრობით, სატესტო ბრანჩზე. თითოეულზე მოახსენე:
ბრძანება, გასვლის კოდი და გამოსავლის ბოლო 20 ხაზი სიტყვასიტყვით ჩასმული. თუ გამოსავალი მოჭერი,
დაწერე, რამდენი ხაზი და რომელი მხრიდან.

არასდროს მოახსენო ბრძანება გავლილად, თუ ის ამ სესიაში არ გაგიშვია და მისი გამოსავალი არ გინახავს.
არასდროს გამოიტანო შედეგი კოდიდან, დიფიდან, გეგმიდან, რევიუდან ან წინა გაშვებიდან. თუ გამოსავალი
არ გინახავს, სტატუსია NOT RUN — და NOT RUN აქ სრულფასოვანი პასუხია. გამოგონილი „გავიდა“ — არა.
არასდროს შეასწორო ფაილი, რომ ბრძანება გაიაროს. თუ ბრძანება ჩავარდა, ის ჩავარდა; სწორედ ეს არის ანგარიში.
არასდროს გაუშვა ჩავარდნილი ბრძანება სხვა ფლაგებით, უფრო ვიწრო მისამართით ან გამორთული წესით და
მისი შედეგი არ მოახსენო. მოახსენე ბრძანება ისე, როგორც <commands>-შია დაწერილი.
არასდროს გადმოთქვა გამოსავალი შენი სიტყვებით. ჩასვი.
არასდროს დააინსტალირო და არ განაახლო არაფერი იმისთვის, რომ ბრძანება გაეშვას.

ყოველი ბრძანება ერთხელ გაუშვი. მეორე გაშვება მხოლოდ მაშინ დაიშვება, როცა პირველი ჩავარდნა დროებით
მიზეზს ასახელებს (ქსელი, დაკავებული პორტი, აუმაღლებელი კონტეინერი) — და მაშინ ორივე გაშვება მოახსენე.

თუ ბრძანება საერთოდ ვერ ეშვება — არ არსებობს ორობითი ფაილი, აკლია გარემოს ცვლადი, არ არის ქსელი —
მოახსენე `CANNOT RUN: <command> — <ზუსტი შეცდომა>` და სიის დანარჩენი ნაწილი მაინც გაიარე.

გამოსავალი:
1. ცხრილი — ბრძანება · გასვლის კოდი · PASS / FAIL / NOT RUN / CANNOT RUN
2. გამოსავალი — ჩასმული ყოველი სტრიქონისთვის, რომელიც PASS არ არის
3. ერთი ხაზი — გაეშვას თუ არ გაეშვას, და რომელი სტრიქონი წყვეტს ამას. თუ თუნდაც ერთი სტრიქონი
   FAIL, NOT RUN ან CANNOT RUN არის, პასუხია: არ გაეშვას.

გადაცემა: ეს ცხრილი არის ის მტკიცებულება, რომელსაც WL-08 იწერს. დასკვნა, რომლის უკანაც აქ სტრიქონი
არ დგას, ამბავია და არა შენიშვნა.
```

---

### WL-08 · Remember what this session learned
`claude-code` `claude` `cursor` — memory, rules-file

**EN**
```
Extract what this session learned into a rules-file entry. The output is text I paste, not a change
you make.

<session>
The task: {{task}}
The diff: {{diff}}
What failed on the way, and how it was resolved: {{failures}}
The verification table: {{verification_table}}
Rules the file already contains: {{existing_rules}}
</session>

Do not edit any file, including CLAUDE.md, .cursorrules and AGENTS.md themselves. Print the entry;
I paste it.
NEVER write a rule about this session's incident rather than this repo's behaviour ("the staging DB
was down on Tuesday" is not a rule).
NEVER restate something already in <existing_rules>. If a candidate is covered, write
`already covered by: <line>` and drop it.
NEVER write general software advice. "Write good tests" is true everywhere and changes nothing here.

Keep a candidate lesson only if all three hold:
  · it will still be true next month
  · it is specific to this repo, not to software in general
  · a session that did not know it would do a specific wrong thing, and you can name that thing

Output, first, a block ready to paste into CLAUDE.md / .cursorrules / AGENTS.md:

## <area>
- <rule, written as an instruction in the imperative>
- <rule>

For example:
- Money is `bigint` minor units everywhere. NEVER introduce a float amount. `src/billing/money.ts`
  is the only file where a conversion happens.

At most 5 rules. A rules file nobody reads to the end changes no behaviour.

Then, outside the pasteable block, two short sections:

· WHAT FAILED AND WHY — one line per failure, the cause and not the symptom, each tied to a row of
  {{verification_table}} or a named attempt. This is the evidence for the rules above; if a rule has
  no line here, delete the rule.

· WHAT NOT TO REPEAT — the specific wrong move a future session would make by default, written so
  it is recognisable before it is made: "do not add a Prisma import under src/billing/ — that layer
  is deliberately storage-free and the repository interface lives in src/billing/ports.ts".

Handoff: the WHAT FAILED AND WHY section is what WL-09 reads across several sessions. Write it so
it is still legible next to four other sessions' notes.
```

**KA**
```
ამოკრიბე, რა ისწავლა ამ სესიამ, და ჩამოაყალიბე წესების ფაილის ჩანაწერად. შედეგი ტექსტია, რომელსაც
მე ჩავსვამ, და არა ცვლილება, რომელსაც შენ შეიტან.

<session>
ამოცანა: {{ამოცანა}}
დიფი: {{დიფი}}
რა ჩავარდა გზაში და როგორ გადაწყდა: {{ჩავარდნები}}
ვერიფიკაციის ცხრილი: {{ვერიფიკაციის_ცხრილი}}
წესები, რომლებიც ფაილში უკვე წერია: {{არსებული_წესები}}
</session>

არცერთი ფაილი არ შეასწორო, მათ შორის არც CLAUDE.md, არც .cursorrules და არც AGENTS.md.
დაბეჭდე ჩანაწერი; ჩასმას მე მოვახერხებ.
არასდროს დაწერო წესი ამ სესიის შემთხვევაზე და არა ამ რეპოს ქცევაზე („სამშაბათს სატესტო ბაზა ჩაწვა“
წესი არ არის).
არასდროს გაიმეორო ის, რაც <existing_rules>-ში უკვე წერია. თუ კანდიდატი დაფარულია, დაწერე
`already covered by: <ხაზი>` და ამოაგდე.
არასდროს დაწერო ზოგადი რჩევა პროგრამირებაზე. „დაწერე კარგი ტესტები“ ყველგან სწორია და აქ არაფერს ცვლის.

კანდიდატი გაკვეთილი დატოვე მხოლოდ მაშინ, თუ სამივე პირობა სრულდება:
  · ის მომავალ თვესაც ასევე იქნება
  · ის სწორედ ამ რეპოს ეხება და არა ზოგადად პროგრამირებას
  · სესია, რომელმაც ეს არ იცის, კონკრეტულ შეცდომას დაუშვებს — და ამ შეცდომის დასახელება შეგიძლია

გამოსავალი — ჯერ ბლოკი, მზა იმისთვის, რომ CLAUDE.md-ში, .cursorrules-ში ან AGENTS.md-ში ჩაისვას:

## <სფერო>
- <წესი, დაწერილი ბრძანებითი კილოთი>
- <წესი>

მაგალითად:
- ფული ყველგან `bigint`-ია, მცირე ერთეულებში. არასდროს შემოიტანო float-თანხა. `src/billing/money.ts`
  ერთადერთი ფაილია, სადაც კონვერტაცია ხდება.

მაქსიმუმ 5 წესი. წესების ფაილი, რომელსაც ბოლომდე არავინ კითხულობს, ქცევას არ ცვლის.

შემდეგ, ჩასასმელი ბლოკის გარეთ, ორი მოკლე სექცია:

· რა ჩავარდა და რატომ — თითო ჩავარდნაზე ერთი ხაზი, მიზეზი და არა სიმპტომი, თითოეული მიბმული
  {{ვერიფიკაციის_ცხრილი}}-ის სტრიქონზე ან დასახელებულ მცდელობაზე. ეს არის ზემოთ დაწერილი წესების
  მტკიცებულება; თუ წესს აქ ხაზი არ შეესაბამება, ის წესი წაშალე.

· რა არ უნდა გაკეთდეს ხელახლა — კონკრეტული მცდარი ნაბიჯი, რომელსაც მომავალი სესია ავტომატურად
  გადადგამდა, დაწერილი ისე, რომ მისი ამოცნობა ნაბიჯის გადადგმამდე შეიძლებოდეს: „src/billing/-ის
  ქვეშ Prisma-ს იმპორტი არ დაამატო — ეს ფენა შეგნებულად საცავისგან დამოუკიდებელია და რეპოზიტორის
  ინტერფეისი src/billing/ports.ts-შია“.

გადაცემა: სექცია „რა ჩავარდა და რატომ“ არის ის, რასაც WL-09 რამდენიმე სესიის მასშტაბით კითხულობს.
დაწერე ისე, რომ ის სხვა ოთხი სესიის ჩანაწერის გვერდითაც იკითხებოდეს.
```

---

### WL-09 · Find the recurring failure, propose one rule
`claude-code` `claude` `gpt` — retrospective, tooling

**EN**
```
Several sessions' notes are below. Find the failure that keeps happening and propose the one change
that would stop it.

<session_notes>
{{notes}}          — the WHAT FAILED AND WHY sections from several WL-08 runs
</session_notes>

<current_rules>
{{rules_file}}     — the current CLAUDE.md / .cursorrules / AGENTS.md
</current_rules>

<tooling>
Pre-commit hooks: {{hooks}}
CI jobs and what each runs: {{ci}}
</tooling>

Count before you conclude. A failure in one session is an incident; a failure in 3 or more of these
sessions is a pattern, and only patterns earn a rule.

Do not edit any file, and do not install a hook. You propose; I install.

Output:

1. THE RECURRENCE TABLE — every failure appearing in 2 or more sessions: the failure in one line,
   how many sessions, and which ones. Ordered by count. Stop the table at 5 rows.

2. THE ONE TO FIX — the top row, and why it is the top row even when another is more irritating:
   time lost per occurrence × number of occurrences.

3. WHY THE CURRENT RULES DID NOT CATCH IT — exactly one of: no rule covers it · a rule covers it
   but is phrased as advice rather than a prohibition · the rule exists but sits below the 40th line
   of <current_rules> and is being skipped · the rule cannot be enforced by reading alone.
   Quote the line, or state plainly that no line exists.

4. THE PROPOSAL — exactly one, and say which kind:
   · a standing rule — the exact line to add to <current_rules>, and which existing line it replaces
   · a hook — the exact command (`ruff check --select F401`, `npm run typecheck`, `go vet ./...`,
     `pytest -x -q tests/contracts`), where it runs (pre-commit / pre-push / CI), and what makes it
     exit non-zero
   · a test — the assertion that would have failed in each of those sessions, and where it lives
   Prefer a hook over a rule whenever the failure is mechanically detectable: a rule asks a model to
   remember, a hook does not care whether it remembered.

5. THE COST — what this adds to every future run: seconds per commit, the false positives you
   expect and what a developer does about one, and who it slows down on the day the rule is right
   but the exception is real. Then say plainly whether it is worth it. If it is not, answer
   DO NOT ADD — proposing nothing is a valid result of this prompt.

NEVER propose more than one change. A list of five improvements is a list nobody installs.
NEVER propose "be more careful", "double-check" or "pay closer attention" — those are not mechanisms.
NEVER count a failure twice because two sessions described it in different words; merge them and say
you merged them.

Handoff: whatever I install here becomes part of the standing rules that WL-01 through WL-08 read
on the next pass through the loop. Write the rule so it survives being read by a session that knows
nothing about these notes.
```

**KA**
```
ქვემოთ რამდენიმე სესიის ჩანაწერია. იპოვე ჩავარდნა, რომელიც მეორდება, და შემომთავაზე ერთი
ცვლილება, რომელიც მას შეაჩერებდა.

<session_notes>
{{ჩანაწერები}}    — რამდენიმე WL-08-ის სექცია „რა ჩავარდა და რატომ“
</session_notes>

<current_rules>
{{წესების_ფაილი}} — ამჟამინდელი CLAUDE.md / .cursorrules / AGENTS.md
</current_rules>

<tooling>
პრე-კომიტ ჰუკები: {{ჰუკები}}
CI-ის job-ები და რას უშვებს თითოეული: {{ci}}
</tooling>

ჯერ დათვალე და მერე დაასკვენი. ერთ სესიაში ნანახი ჩავარდნა ცალკეული შემთხვევაა; 3 ან მეტ სესიაში
ნანახი — პატერნი, და წესს მხოლოდ პატერნი იმსახურებს.

არცერთი ფაილი არ შეასწორო და ჰუკი არ დააყენო. შენ თავაზობ, მე ვაყენებ.

გამოსავალი:

1. გამეორებების ცხრილი — ყოველი ჩავარდნა, რომელიც 2 ან მეტ სესიაშია: ჩავარდნა ერთი ხაზით,
   რამდენ სესიაში და რომლებში. დალაგებული რაოდენობის მიხედვით. ცხრილი 5 სტრიქონზე გააჩერე.

2. რომელია გასასწორებელი — პირველი სტრიქონი და რატომაა ის პირველი მაშინაც კი, როცა სხვა უფრო
   მოსაბეზრებელია: თითო შემთხვევაზე დაკარგული დრო × შემთხვევათა რაოდენობა.

3. რატომ ვერ დაიჭირა ეს არსებულმა წესებმა — ზუსტად ერთი მათგანი: წესი საერთოდ არ არსებობს ·
   წესი არსებობს, მაგრამ რჩევადაა ჩამოყალიბებული და არა აკრძალვად · წესი არსებობს, მაგრამ
   <current_rules>-ის მე-40 ხაზს ქვემოთაა და მას ტოვებენ · წესი მხოლოდ კითხვით ვერ კონტროლდება.
   მოიყვანე ეს ხაზი ციტირებულად ან პირდაპირ დაწერე, რომ ასეთი ხაზი არ არსებობს.

4. წინადადება — ზუსტად ერთი, და დაასახელე, რომელი სახისაა:
   · მუდმივი წესი — ზუსტი ხაზი, რომელიც <current_rules>-ს უნდა დაემატოს, და რომელ არსებულ ხაზს
     ანაცვლებს
   · ჰუკი — ზუსტი ბრძანება (`ruff check --select F401`, `npm run typecheck`, `go vet ./...`,
     `pytest -x -q tests/contracts`), სად ეშვება (პრე-კომიტ / პრე-პუშ / CI) და რაზე ბრუნდება
     არანულოვანი კოდით
   · ტესტი — მტკიცება, რომელიც თითოეულ ამ სესიაში ჩავარდებოდა, და სად იდება ის
   როცა ჩავარდნა მექანიკურად აღმოსაჩენია, ჰუკს მიეცი უპირატესობა წესზე: წესი მოდელს დამახსოვრებას
   სთხოვს, ჰუკს კი არ აინტერესებს, დაიმახსოვრა თუ არა.

5. ფასი — რას მატებს ეს ყოველ მომავალ გაშვებას: წამები ერთ კომიტზე, მოსალოდნელი ცრუ გაფრთხილებები
   და რას აკეთებს დეველოპერი ასეთის დანახვისას, და ვის აფერხებს ის იმ დღეს, როცა წესი სწორია,
   გამონაკლისი კი რეალური. შემდეგ პირდაპირ დაწერე, ღირს თუ არა. თუ არ ღირს, პასუხია: არ დაემატოს —
   არაფრის შემოთავაზება ამ პრომპტის სრულფასოვანი შედეგია.

არასდროს შემომთავაზო ერთზე მეტი ცვლილება. ხუთი გაუმჯობესების სია ის სიაა, რომელსაც არავინ აყენებს.
არასდროს შემომთავაზო „იყავი ყურადღებით“, „ორჯერ გადაამოწმე“ ან „მეტი ყურადღება მიაქციე“ —
ეს მექანიზმები არ არის.
არასდროს დათვალო ერთი ჩავარდნა ორჯერ იმის გამო, რომ ორმა სესიამ ის სხვადასხვა სიტყვით აღწერა;
გააერთიანე ისინი და დაწერე, რომ გააერთიანე.

გადაცემა: რასაც აქედან დავაყენებ, მუდმივი წესების ნაწილი ხდება, რომელსაც WL-01-იდან WL-08-მდე
ყველა ეტაპი კითხულობს ციკლის მომდევნო გავლისას. დაწერე ეს წესი ისე, რომ მან გაუძლოს სესიას,
რომელმაც ამ ჩანაწერების შესახებ არაფერი იცის.
```
