# Agentic coding / აგენტური კოდირება

Every prompt in this file uses the File-scope framework: start state, target state, allowed files,
forbidden actions, stop condition. Five elements, no exceptions — see
[`../../references/frameworks.md`](../../references/frameworks.md) §6.
An agent without a stop condition does not fail cleanly. It loops — try, fail, try differently, fail —
and that loop is the largest credit sink in this whole category of tool.
Put the standing rules below into your `CLAUDE.md` / `.cursorrules` / `AGENTS.md` once, then keep each
task prompt to what is genuinely task-specific.

ამ ფაილში ყოველი პრომპტი File-scope ფრეიმვორკზეა აგებული: საწყისი მდგომარეობა, სამიზნე მდგომარეობა,
დაშვებული ფაილები, აკრძალული მოქმედებები, გაჩერების პირობა. ხუთივე ელემენტი — გამონაკლისის გარეშე.
აგენტი, რომელსაც გაჩერების პირობა არ აქვს, უბრალოდ არ ჩავარდება — ის მარყუჟში შედის: სცადა, ვერ შეძლო,
სხვანაირად სცადა, ისევ ვერ შეძლო — და სწორედ ეს მარყუჟი ჭამს ყველაზე მეტ კრედიტს.
ქვემოთ მოცემული მუდმივი წესები ერთხელ ჩაწერე `CLAUDE.md`-ში, `.cursorrules`-ში ან `AGENTS.md`-ში და
პრომპტში მხოლოდ ის დატოვე, რაც კონკრეტულ ამოცანას ეხება.

---

## Standing rules / მუდმივი წესები

Write these once into your rules file. They are the lines you would otherwise retype in every task prompt.

ეს ერთხელ ჩაწერე წესების ფაილში. სწორედ ის ხაზებია, რომლებსაც სხვა შემთხვევაში ყოველ პრომპტში გაიმეორებდი.

**EN**
```
## Standing rules for this repo

Progress
- After each file you modify, print the path and one line describing the change.
- Before you start editing, print the list of files you intend to touch. If it is longer than
  what I gave you, stop and ask.

Ambiguity
- When an instruction is ambiguous, take the non-destructive reading, state which reading you took,
  and continue. NEVER guess in the destructive direction.

Failure
- If a command or tool call fails, STOP and report the exact error output. NEVER fabricate a result
  and continue on top of it.
- Retry a failing command at most 2 times. After the second failure, stop and report.

Never without asking
- NEVER install, add, remove or upgrade a package: no `npm install`, `pip install`, `go get`,
  `cargo add`, `brew install`.
- NEVER run `git push --force`, `git reset --hard`, `git clean -fd`, `rm -rf`, `DROP TABLE`,
  or delete a branch.
- NEVER commit or push unless I ask. Leave the work in the working tree.
- NEVER edit files outside the scope I listed. If the task needs one, stop and tell me which and why.
- NEVER reformat, re-sort imports, or "tidy" code you were not asked to change.
```

**KA**
```
## ამ რეპოს მუდმივი წესები

პროგრესი
- ყოველი შეცვლილი ფაილის შემდეგ დაბეჭდე მისი მისამართი და ერთი ხაზი ცვლილების აღწერით.
- სანამ რედაქტირებას დაიწყებ, ჩამოწერე ფაილები, რომლებსაც აპირებ შეეხო. თუ სია იმაზე გრძელია,
  რაც მოგეცი, შეჩერდი და მკითხე.

ბუნდოვანება
- როცა მითითება ორაზროვანია, აირჩიე ის წაკითხვა, რომელიც არაფერს შლის და არაფერს აზიანებს,
  დაწერე რომელი აირჩიე და გააგრძელე. არასდროს გამოიცნო დამანგრეველი მიმართულებით.

შეცდომა
- თუ ბრძანება ან ინსტრუმენტის გამოძახება ჩავარდა, შეჩერდი და მოახსენე ზუსტი შეცდომის ტექსტი.
  არასდროს გამოიგონო შედეგი და მასზე დაშენებით არ გააგრძელო.
- ჩავარდნილი ბრძანება ხელახლა სცადე მაქსიმუმ 2-ჯერ. მეორე ჩავარდნის შემდეგ შეჩერდი და მოახსენე.

არასდროს კითხვის გარეშე
- არასდროს დააინსტალირო, დაამატო, წაშალო ან განაახლო პაკეტი: არც `npm install`, არც `pip install`,
  არც `go get`, არც `cargo add`, არც `brew install`.
- არასდროს გაუშვა `git push --force`, `git reset --hard`, `git clean -fd`, `rm -rf`, `DROP TABLE`
  და არასდროს წაშალო ბრანჩი.
- არასდროს გააკეთო კომიტი ან push, სანამ არ გთხოვ. ცვლილებები სამუშაო ხეში დატოვე.
- არასდროს შეეხო ფაილს, რომელიც არეალში არ ჩამომიწერია. თუ ამოცანას ასეთი ფაილი სჭირდება,
  შეჩერდი და დამისახელე რომელი და რატომ.
- არასდროს გადააფორმატო კოდი, არ გადაალაგო იმპორტები და არ „დაალაგო“ ის, რისი შეცვლაც არ გთხოვე.
```

---

### AC-01 · Fix one failing test
`claude-code` `cursor` `cline` — testing, bugfix

**EN**
```
Fix one failing test. Do not widen the scope.

<start_state>
`tests/auth/test_session.py::test_expired_token_rejected` fails.
Reproduce: `pytest tests/auth/test_session.py::test_expired_token_rejected -x -q`
Current output: `AssertionError: assert 200 == 401`
</start_state>

<target_state>
That test passes and the test file is unchanged.
Verify: `pytest tests/auth -x -q` — every test in the directory passes.
</target_state>

<allowed_files>
src/auth/session.py
src/auth/tokens.py
</allowed_files>

<forbidden>
NEVER edit anything under tests/. The test is correct; the code is wrong.
NEVER change the token expiry constant to make the assertion pass.
NEVER add a try/except that swallows the failure.
NEVER install packages.
NEVER touch files outside <allowed_files>.
</forbidden>

<stop_condition>
Stop when `pytest tests/auth -x -q` passes.
Maximum 2 attempts. If it still fails after the second, STOP and report: what you changed,
the exact failure output, and your best hypothesis. Do not try a third approach.
</stop_condition>

Before you edit anything, print one line explaining why the test fails.
```

**KA**
```
გაასწორე ერთი ჩავარდნილი ტესტი. არეალი არ გააფართოვო.

<start_state>
ტესტი `tests/auth/test_session.py::test_expired_token_rejected` ვარდება.
გასამეორებელი ბრძანება: `pytest tests/auth/test_session.py::test_expired_token_rejected -x -q`
ამჟამინდელი შედეგი: `AssertionError: assert 200 == 401`
</start_state>

<target_state>
ეს ტესტი გადის და ტესტის ფაილი უცვლელი რჩება.
გადასამოწმებელი ბრძანება: `pytest tests/auth -x -q` — დირექტორიის ყველა ტესტი უნდა გავიდეს.
</target_state>

<allowed_files>
src/auth/session.py
src/auth/tokens.py
</allowed_files>

<forbidden>
არასდროს შეეხო tests/-ის ქვეშ არსებულ ფაილს. ტესტი სწორია, კოდია მცდარი.
არასდროს შეცვალო ტოკენის ვადის კონსტანტა მხოლოდ იმისთვის, რომ ტესტი გავიდეს.
არასდროს დაამატო try/except, რომელიც შეცდომას ჩაყლაპავს.
არასდროს დააინსტალირო პაკეტი.
არასდროს შეეხო ფაილს <allowed_files>-ის გარეთ.
</forbidden>

<stop_condition>
შეჩერდი, როცა `pytest tests/auth -x -q` გაივლის.
მაქსიმუმ 2 მცდელობა. თუ მეორის შემდეგაც ვარდება, შეჩერდი და მოახსენე: რა შეცვალე,
ზუსტად რა შეცდომა დაბრუნდა და რა ვარაუდი გაქვს. მესამე მიდგომა არ სცადო.
</stop_condition>

სანამ რედაქტირებას დაიწყებ, ერთ ხაზში დაწერე, რატომ ვარდება ტესტი.
```

---

### AC-02 · Add an endpoint with validation
`claude-code` `cursor` `windsurf` — api, backend

**EN**
```
Add one HTTP endpoint with request validation.

<start_state>
`POST /api/invoices` does not exist.
Reproduce: `curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/invoices` → 404
The server runs with `npm run dev`. `zod` is already a dependency; `src/validation/` already
holds three schemas written in it — follow their style.
</start_state>

<target_state>
A valid body returns 201 and `{"id": "<uuid>", "status": "draft"}`.
An invalid body returns 400 and `{"error":"VALIDATION_FAILED","fields":["<field>", ...]}`.
A missing auth header returns 401 — handled by existing middleware, do not reimplement it.
Verify: `npm test -- invoices` passes, and
`curl -s -X POST localhost:3000/api/invoices -H 'Content-Type: application/json' -d '{}'`
returns 400 with the field list.
</target_state>

<allowed_files>
src/api/invoices.ts
src/validation/invoice-schema.ts
src/routes.ts
tests/api/invoices.test.ts
</allowed_files>

<forbidden>
NEVER modify the auth middleware in src/middleware/auth.ts.
NEVER change the database schema or add a migration.
NEVER install a validation library — use the zod version already in package.json.
NEVER return 500 for a bad request body.
NEVER touch files outside <allowed_files>.
</forbidden>

<stop_condition>
Stop when `npm test -- invoices` passes and both curl checks return the documented codes.
Maximum 2 attempts after the first full test run. If the tests still fail, STOP and report the
failing assertion and the response body you actually got. Do not restructure the route to try again.
</stop_condition>

Write the test file first, then the implementation.
```

**KA**
```
დაამატე ერთი HTTP ენდპოინტი მოთხოვნის ვალიდაციით.

<start_state>
`POST /api/invoices` არ არსებობს.
გასამეორებელი ბრძანება: `curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/invoices` → 404
სერვერი იდგმება `npm run dev`-ით. `zod` უკვე დამოკიდებულებაშია; `src/validation/`-ში სამი სქემა
უკვე მასზეა დაწერილი — იმავე სტილს მიჰყევი.
</start_state>

<target_state>
სწორ მოთხოვნაზე ბრუნდება 201 და `{"id": "<uuid>", "status": "draft"}`.
არასწორზე — 400 და `{"error":"VALIDATION_FAILED","fields":["<field>", ...]}`.
ავტორიზაციის ჰედერის გარეშე — 401; ამას არსებული middleware უკვე აკეთებს, თავიდან არ დაწერო.
გადასამოწმებელი ბრძანება: `npm test -- invoices` უნდა გავიდეს და
`curl -s -X POST localhost:3000/api/invoices -H 'Content-Type: application/json' -d '{}'`
უნდა დააბრუნოს 400 და ველების სია.
</target_state>

<allowed_files>
src/api/invoices.ts
src/validation/invoice-schema.ts
src/routes.ts
tests/api/invoices.test.ts
</allowed_files>

<forbidden>
არასდროს შეცვალო ავტორიზაციის middleware ფაილში src/middleware/auth.ts.
არასდროს შეეხო ბაზის სქემას და არ დაამატო მიგრაცია.
არასდროს დააინსტალირო ვალიდაციის ბიბლიოთეკა — იმუშავე package.json-ში არსებული zod-ით.
არასდროს დააბრუნო 500 არასწორი მოთხოვნის სხეულზე.
არასდროს შეეხო ფაილს <allowed_files>-ის გარეთ.
</forbidden>

<stop_condition>
შეჩერდი, როცა `npm test -- invoices` გაივლის და ორივე curl-შემოწმება მითითებულ კოდს დააბრუნებს.
პირველი სრული გაშვების შემდეგ მაქსიმუმ 2 მცდელობა. თუ ტესტები კვლავ ვარდება, შეჩერდი და მოახსენე,
რომელი მტკიცება ჩავარდა და რა სხეული დაბრუნდა რეალურად. ხელახლა არ გადააწყო როუტი.
</stop_condition>

ჯერ ტესტის ფაილი დაწერე, მერე იმპლემენტაცია.
```

---

### AC-03 · Migrate one component to a new API
`claude-code` `cursor` `cline` — frontend, migration

**EN**
```
Migrate one component to the new library API. One component only.

<start_state>
`src/components/DataTable.tsx` uses the TanStack Table v7 API (`useTable`, `usePagination`).
v8 is already installed (`@tanstack/react-table@8.20.5` in package.json); v7 was removed.
Reproduce: `npm run typecheck` → 14 errors, all inside src/components/DataTable.tsx.
</start_state>

<target_state>
The component uses the v8 API (`useReactTable`, `getCoreRowModel`, `getPaginationRowModel`).
Its props are byte-identical to what they are now — every caller keeps working untouched.
Verify: `npm run typecheck` reports 0 errors AND `npm test -- DataTable` passes.
</target_state>

<allowed_files>
src/components/DataTable.tsx
src/types/table.ts
tests/components/DataTable.test.tsx
</allowed_files>

<forbidden>
NEVER change the exported props interface of DataTable. If v8 makes a prop impossible, STOP and ask.
NEVER migrate any other component, even if it has the same errors.
NEVER update any file under src/pages/ that renders DataTable.
NEVER install or downgrade a package.
NEVER add `@ts-expect-error` or `any` to silence a type error.
</forbidden>

<stop_condition>
Stop when `npm run typecheck` is clean and `npm test -- DataTable` passes.
Maximum 2 attempts. If type errors remain after the second, STOP and report the remaining errors
verbatim with the v8 API you tried for each. Do not switch to a different table library.
</stop_condition>
```

**KA**
```
გადაიყვანე ერთი კომპონენტი ბიბლიოთეკის ახალ API-ზე. მხოლოდ ერთი კომპონენტი.

<start_state>
`src/components/DataTable.tsx` იყენებს TanStack Table v7-ის API-ს (`useTable`, `usePagination`).
v8 უკვე დაინსტალირებულია (`@tanstack/react-table@8.20.5` package.json-ში), v7 ამოღებულია.
გასამეორებელი ბრძანება: `npm run typecheck` → 14 შეცდომა, ყველა src/components/DataTable.tsx-ში.
</start_state>

<target_state>
კომპონენტი მუშაობს v8-ის API-ზე (`useReactTable`, `getCoreRowModel`, `getPaginationRowModel`).
მისი props ზუსტად იგივე რჩება — ყველა გამომძახებელი ფაილი უცვლელად აგრძელებს მუშაობას.
გადასამოწმებელი ბრძანება: `npm run typecheck` 0 შეცდომით და `npm test -- DataTable` გასული.
</target_state>

<allowed_files>
src/components/DataTable.tsx
src/types/table.ts
tests/components/DataTable.test.tsx
</allowed_files>

<forbidden>
არასდროს შეცვალო DataTable-ის ექსპორტირებული props-ინტერფეისი. თუ v8-ზე რომელიმე prop შეუძლებელია,
შეჩერდი და მკითხე.
არასდროს გადაიყვანო სხვა კომპონენტი, თუნდაც იმავე შეცდომებით ვარდებოდეს.
არასდროს შეეხო src/pages/-ის ფაილებს, რომლებიც DataTable-ს ხატავენ.
არასდროს დააინსტალირო ან დაწიო პაკეტის ვერსია.
არასდროს დაამატო `@ts-expect-error` ან `any` ტიპის შეცდომის ჩასაჩუმებლად.
</forbidden>

<stop_condition>
შეჩერდი, როცა `npm run typecheck` სუფთაა და `npm test -- DataTable` გადის.
მაქსიმუმ 2 მცდელობა. თუ მეორის შემდეგაც რჩება ტიპის შეცდომები, შეჩერდი და სიტყვასიტყვით მოახსენე
დარჩენილი შეცდომები და თითოეულზე რა v8-API სცადე. სხვა ცხრილის ბიბლიოთეკაზე არ გადახვიდე.
</stop_condition>
```

---

### AC-04 · Add test coverage to an untested module
`claude-code` `cursor` `codex` — testing, coverage

**EN**
```
Write tests for a module that has none. Do not change the module.

<start_state>
`src/pricing/discount.py` has no tests.
Reproduce: `pytest --cov=src/pricing/discount --cov-report=term-missing tests/ -q` → 0% for that file.
The module exports: `apply_tiered_discount`, `apply_promo_code`, `stack_discounts`.
</start_state>

<target_state>
Line coverage for src/pricing/discount.py is at least 85%.
Verify: `pytest tests/pricing -q` passes AND
`pytest --cov=src/pricing/discount --cov-report=term-missing tests/ -q` reports ≥85%.
</target_state>

<allowed_files>
tests/pricing/test_discount.py   (create it)
tests/pricing/__init__.py         (create if missing)
</allowed_files>

<forbidden>
NEVER edit src/pricing/discount.py. If a test exposes a bug, write the test as `xfail` with a
comment naming the bug and report it to me — do NOT fix the code.
NEVER mock a function from this module in a test of this module.
NEVER write a test whose only assertion is `assert result is not None`.
NEVER install packages — pytest and pytest-cov are already available.
</forbidden>

<stop_condition>
Stop when coverage is ≥85% and `pytest tests/pricing -q` passes.
Maximum 2 rounds of adding tests after the first coverage run. If you cannot reach 85%, STOP and
report which lines are still uncovered and why they are hard to reach.
</stop_condition>

Cover the edges, not three variations of the happy path: zero quantity, negative price,
an expired promo code, two discounts that would exceed 100% when stacked.
```

**KA**
```
დაწერე ტესტები მოდულისთვის, რომელსაც ტესტი არ აქვს. თვითონ მოდული არ შეცვალო.

<start_state>
`src/pricing/discount.py` ტესტების გარეშეა.
გასამეორებელი ბრძანება: `pytest --cov=src/pricing/discount --cov-report=term-missing tests/ -q` → 0%.
მოდული აექსპორტებს ფუნქციებს: `apply_tiered_discount`, `apply_promo_code`, `stack_discounts`.
</start_state>

<target_state>
src/pricing/discount.py-ის ხაზების დაფარვა მინიმუმ 85%-ია.
გადასამოწმებელი ბრძანება: `pytest tests/pricing -q` გადის და
`pytest --cov=src/pricing/discount --cov-report=term-missing tests/ -q` აჩვენებს ≥85%-ს.
</target_state>

<allowed_files>
tests/pricing/test_discount.py   (შექმენი)
tests/pricing/__init__.py         (შექმენი, თუ არ არსებობს)
</allowed_files>

<forbidden>
არასდროს შეასწორო src/pricing/discount.py. თუ ტესტმა ბაგი გამოააშკარავა, დაწერე ტესტი `xfail`-ით,
კომენტარში დაასახელე ბაგი და მომახსენე — კოდი არ გაასწორო.
არასდროს გააკეთო mock ამავე მოდულის ფუნქციაზე ამავე მოდულის ტესტში.
არასდროს დაწერო ტესტი, რომლის ერთადერთი მტკიცებაა `assert result is not None`.
არასდროს დააინსტალირო პაკეტი — pytest და pytest-cov უკვე ხელმისაწვდომია.
</forbidden>

<stop_condition>
შეჩერდი, როცა დაფარვა ≥85%-ია და `pytest tests/pricing -q` გადის.
პირველი გაზომვის შემდეგ ტესტების დამატების მაქსიმუმ 2 რაუნდი. თუ 85%-ს ვერ მიაღწევ, შეჩერდი და
მოახსენე, რომელი ხაზები დარჩა დაუფარავი და რატომ არის მათზე მოხვედრა რთული.
</stop_condition>

დაფარე კიდეები და არა ერთი და იმავე წარმატებული სცენარის სამი ვარიაცია: ნულოვანი რაოდენობა,
უარყოფითი ფასი, ვადაგასული პრომოკოდი და ორი ფასდაკლება, რომელთა ჯამიც 100%-ს გადააჭარბებდა.
```

---

### AC-05 · Rename and move a module across the repo
`claude-code` `cursor` `windsurf` — refactoring, repo-wide

**EN**
```
Move and rename one package. This is a mechanical change — no logic moves with it.

<start_state>
`src/utils/helpers.go` (package `utils`) holds date and currency formatting used across the repo.
Reproduce the reference count: `rg -l "internal/utils" --type go | wc -l` → 23 files.
`go build ./...` and `go test ./...` currently pass.
</start_state>

<target_state>
The file lives at `src/internal/format/format.go` with package name `format`.
Every importer uses the new path.
Verify, in this order:
  `rg -n "internal/utils" --type go`   → no output
  `go build ./...`                      → exits 0
  `go test ./...`                       → exits 0
  `gofmt -l src/`                        → no output
</target_state>

<allowed_files>
src/internal/format/format.go   (new)
src/utils/helpers.go            (delete after the move)
every .go file listed by `rg -l "internal/utils" --type go`
</allowed_files>

<forbidden>
NEVER change a single function body. The diff must be limited to the package clause, the file
location, and import lines.
NEVER rename an exported identifier while moving it.
NEVER leave a compatibility shim or a re-export in src/utils/.
NEVER touch go.mod, go.sum, or anything under vendor/.
NEVER run `git mv` — create, edit imports, verify, then delete.
</forbidden>

<stop_condition>
Stop when all four verification commands above pass in order.
Maximum 2 attempts at fixing the build. If `go build ./...` still fails after the second, STOP and
report the remaining compile errors and the files still referencing the old path. Do not start
reverting files on your own.
</stop_condition>

First print the full list of files you will edit, from `rg -l`. Wait for nothing — but if the list
is longer than 23 files, stop and tell me before editing anything.
```

**KA**
```
გადაიტანე და გადაარქვი ერთი პაკეტი. ეს მექანიკური ცვლილებაა — ლოგიკა მასთან ერთად არ მოძრაობს.

<start_state>
`src/utils/helpers.go` (პაკეტი `utils`) შეიცავს თარიღისა და ვალუტის ფორმატირებას, რომელსაც მთელი
რეპო იყენებს.
მიმართვების დასათვლელი ბრძანება: `rg -l "internal/utils" --type go | wc -l` → 23 ფაილი.
`go build ./...` და `go test ./...` ამჟამად გადის.
</start_state>

<target_state>
ფაილი დევს მისამართზე `src/internal/format/format.go`, პაკეტის სახელით `format`.
ყველა იმპორტი ახალ მისამართს იყენებს.
გადაამოწმე ზუსტად ამ თანმიმდევრობით:
  `rg -n "internal/utils" --type go`   → ცარიელი გამოსავალი
  `go build ./...`                      → 0 კოდით სრულდება
  `go test ./...`                       → 0 კოდით სრულდება
  `gofmt -l src/`                        → ცარიელი გამოსავალი
</target_state>

<allowed_files>
src/internal/format/format.go   (ახალი)
src/utils/helpers.go            (გადატანის შემდეგ წაშალე)
ყველა .go ფაილი, რომელსაც `rg -l "internal/utils" --type go` დააბრუნებს
</allowed_files>

<forbidden>
არასდროს შეცვალო ფუნქციის სხეული. დიფში მხოლოდ პაკეტის სტრიქონი, ფაილის ადგილმდებარეობა და
იმპორტის ხაზები უნდა ჩანდეს.
არასდროს გადაარქვა ექსპორტირებულ იდენტიფიკატორს სახელი გადატანისას.
არასდროს დატოვო თავსებადობის შიმი ან ხელახალი ექსპორტი src/utils/-ში.
არასდროს შეეხო go.mod-ს, go.sum-ს და vendor/-ის შიგთავსს.
არასდროს გაუშვა `git mv` — შექმენი, შეასწორე იმპორტები, გადაამოწმე და მერე წაშალე ძველი.
</forbidden>

<stop_condition>
შეჩერდი, როცა ოთხივე გადამოწმება თანმიმდევრობით გაივლის.
ბილდის გასწორების მაქსიმუმ 2 მცდელობა. თუ `go build ./...` მეორის შემდეგაც ვარდება, შეჩერდი და
მოახსენე დარჩენილი კომპილაციის შეცდომები და ფაილები, რომლებიც ჯერ კიდევ ძველ მისამართზე მიუთითებენ.
ფაილების დაბრუნება თვითნებურად არ დაიწყო.
</stop_condition>

ჯერ დაბეჭდე `rg -l`-ის სრული სია იმ ფაილებისა, რომლებსაც შეასწორებ. თუ სია 23 ფაილზე გრძელია,
შეჩერდი და მომახსენე, სანამ რამეს შეცვლი.
```

---

### AC-06 · Add structured logging to one service
`claude-code` `cursor` `cline` — observability, backend

**EN**
```
Replace ad-hoc logging in one service with the project logger.

<start_state>
`src/services/payments.ts` logs with `console.log` and `console.error` in 7 places.
Reproduce: `rg -n "console\.(log|error|warn)" src/services/payments.ts` → 7 matches.
The project logger is `src/lib/logger.ts` (pino). `src/services/orders.ts` already uses it —
copy its call style.
</start_state>

<target_state>
Every log call in payments.ts goes through the project logger with structured fields.
Verify:
  `rg -n "console\." src/services/payments.ts`  → no output
  `npm test -- payments`                         → passes
  `LOG_LEVEL=debug npm run dev` then one test payment → each line is valid JSON with
  `request_id`, `amount`, `currency`, `status`.
</target_state>

<allowed_files>
src/services/payments.ts
tests/services/payments.test.ts
</allowed_files>

<forbidden>
NEVER log a card number, CVV, full card token, customer email, or a full request or response body.
Log only: request_id, amount, currency, provider, status, duration_ms, error_code.
NEVER add a new logging library or a transport.
NEVER change the log level configuration in src/lib/logger.ts.
NEVER convert an existing error path into a log-and-continue path — if it throws today, it throws
after your change.
NEVER touch other services, even the ones with the same console.log problem.
</forbidden>

<stop_condition>
Stop when the rg check is empty and `npm test -- payments` passes.
Maximum 2 attempts. If a test breaks because it asserted on console output, STOP and report it —
do not rewrite the assertion without telling me.
</stop_condition>
```

**KA**
```
შეცვალე ერთი სერვისის უწესრიგო ლოგირება პროექტის ლოგერით.

<start_state>
`src/services/payments.ts` 7 ადგილას წერს `console.log`-ითა და `console.error`-ით.
გასამეორებელი ბრძანება: `rg -n "console\.(log|error|warn)" src/services/payments.ts` → 7 დამთხვევა.
პროექტის ლოგერია `src/lib/logger.ts` (pino). `src/services/orders.ts` უკვე იყენებს მას —
გამოძახების იმავე სტილს მიჰყევი.
</start_state>

<target_state>
payments.ts-ში ყოველი ლოგი პროექტის ლოგერზე გადის, სტრუქტურირებული ველებით.
გადაამოწმე:
  `rg -n "console\." src/services/payments.ts`  → ცარიელი გამოსავალი
  `npm test -- payments`                         → გადის
  `LOG_LEVEL=debug npm run dev` და ერთი სატესტო გადახდა → ყოველი ხაზი ვალიდური JSON-ია და
  შეიცავს ველებს `request_id`, `amount`, `currency`, `status`.
</target_state>

<allowed_files>
src/services/payments.ts
tests/services/payments.test.ts
</allowed_files>

<forbidden>
არასდროს ჩაწერო ლოგში ბარათის ნომერი, CVV, ბარათის სრული ტოკენი, კლიენტის ელფოსტა ან მოთხოვნისა
და პასუხის სრული სხეული. ლოგში მხოლოდ ეს ველები: request_id, amount, currency, provider, status,
duration_ms, error_code.
არასდროს დაამატო ლოგირების ახალი ბიბლიოთეკა ან ტრანსპორტი.
არასდროს შეცვალო ლოგის დონის კონფიგურაცია ფაილში src/lib/logger.ts.
არასდროს აქციო არსებული შეცდომის გზა „ჩაწერე ლოგში და გააგრძელე“ ქცევად — თუ დღეს შეცდომას
აგდებს, შენი ცვლილების შემდეგაც უნდა აგდებდეს.
არასდროს შეეხო სხვა სერვისს, თუნდაც იმავე console.log-ის პრობლემა ჰქონდეს.
</forbidden>

<stop_condition>
შეჩერდი, როცა rg-შემოწმება ცარიელია და `npm test -- payments` გადის.
მაქსიმუმ 2 მცდელობა. თუ რომელიმე ტესტი იმიტომ ჩავარდა, რომ console-ის გამოსავალს ამოწმებდა,
შეჩერდი და მომახსენე — მტკიცება ჩემი ცოდნის გარეშე არ გადაწერო.
</stop_condition>
```

---

### AC-07 · Fix a measured performance regression
`claude-code` `cursor` `devin` — performance, database

**EN**
```
Fix one measured regression. Measure before and after. Do not hide it behind a cache.

<start_state>
`GET /api/search?q=tbilisi` went from ~120ms to ~2.4s after commit a3f19c2.
Reproduce: `hyperfine --warmup 2 'curl -s "localhost:3000/api/search?q=tbilisi"'` → mean ≈ 2.4s
The budget test also fails: `pytest tests/perf/test_search.py -q` → `AssertionError: 2412ms > 300ms`
`git show a3f19c2 --stat` shows the change was in src/db/queries.py.
</start_state>

<target_state>
Mean response time under 300ms for that query, with an identical result set and identical ordering.
Verify:
  `pytest tests/perf/test_search.py -q`  → passes
  `pytest tests/api/test_search.py -q`   → still passes (correctness unchanged)
  `hyperfine --warmup 2 'curl -s "localhost:3000/api/search?q=tbilisi"'` → mean < 300ms
</target_state>

<allowed_files>
src/api/search.py
src/db/queries.py
</allowed_files>

<forbidden>
NEVER add a cache, memoization, or a TTL layer. I want the query fixed, not the symptom hidden.
NEVER change the result set or its ordering. If a faster query returns different rows, it is wrong.
NEVER add a database index — that is a migration and needs my approval. Propose it instead.
NEVER raise the 300ms budget in the test.
NEVER install packages.
</forbidden>

<stop_condition>
Work in this loop: measure → make ONE change → measure again.
Maximum 2 changes. If mean time is still over 300ms after the second measurement, STOP and report,
for each attempt: what you changed, the hyperfine mean, and the `EXPLAIN ANALYZE` output of the
query. Do not try a third change.
</stop_condition>

Before changing anything, print the `EXPLAIN ANALYZE` output for the current query and one line
naming the cause.
```

**KA**
```
გაასწორე ერთი გაზომილი რეგრესია. გაზომე ცვლილებამდე და ცვლილების შემდეგ. ქეშით არ დამალო.

<start_state>
`GET /api/search?q=tbilisi` კომიტ a3f19c2-ის შემდეგ ~120მწმ-დან ~2.4წმ-მდე გაიზარდა.
გასამეორებელი ბრძანება: `hyperfine --warmup 2 'curl -s "localhost:3000/api/search?q=tbilisi"'`
→ საშუალო ≈ 2.4წმ
ბიუჯეტის ტესტიც ვარდება: `pytest tests/perf/test_search.py -q` → `AssertionError: 2412ms > 300ms`
`git show a3f19c2 --stat` აჩვენებს, რომ ცვლილება src/db/queries.py-ში იყო.
</start_state>

<target_state>
ამ მოთხოვნის საშუალო დრო 300მწმ-ზე ნაკლებია, შედეგების ნაკრები და მათი თანმიმდევრობა კი — უცვლელი.
გადაამოწმე:
  `pytest tests/perf/test_search.py -q`  → გადის
  `pytest tests/api/test_search.py -q`   → კვლავ გადის (სისწორე არ შეცვლილა)
  `hyperfine --warmup 2 'curl -s "localhost:3000/api/search?q=tbilisi"'` → საშუალო < 300მწმ
</target_state>

<allowed_files>
src/api/search.py
src/db/queries.py
</allowed_files>

<forbidden>
არასდროს დაამატო ქეში, მემოიზაცია ან TTL-ფენა. მინდა მოთხოვნა გასწორდეს და არა სიმპტომი დაიმალოს.
არასდროს შეცვალო შედეგების ნაკრები ან მათი თანმიმდევრობა. თუ უფრო სწრაფი მოთხოვნა სხვა სტრიქონებს
აბრუნებს, ის არასწორია.
არასდროს დაამატო ბაზის ინდექსი — ეს მიგრაციაა და ჩემს თანხმობას საჭიროებს. სანაცვლოდ შემომთავაზე.
არასდროს გაზარდო ტესტში 300მწმ-ის ბიუჯეტი.
არასდროს დააინსტალირო პაკეტი.
</forbidden>

<stop_condition>
იმუშავე ამ ციკლით: გაზომე → შეიტანე ერთი ცვლილება → ხელახლა გაზომე.
მაქსიმუმ 2 ცვლილება. თუ მეორე გაზომვის შემდეგაც 300მწმ-ზე მეტია, შეჩერდი და თითოეულ მცდელობაზე
მოახსენე: რა შეცვალე, რა საშუალო აჩვენა hyperfine-მა და რა დააბრუნა `EXPLAIN ANALYZE`-მა.
მესამე ცვლილება არ სცადო.
</stop_condition>

სანამ რამეს შეცვლი, დაბეჭდე ამჟამინდელი მოთხოვნის `EXPLAIN ANALYZE` და ერთი ხაზი მიზეზის დასახელებით.
```

---

### AC-08 · Upgrade one dependency and fix the breakage
`claude-code` `cursor` `codex` — dependencies, maintenance

**EN**
```
Upgrade exactly one dependency and repair what it breaks. Nothing else.

<start_state>
`requirements.txt` pins `pydantic==1.10.13`. We need 2.9.2.
Reproduce the current green state first: `pytest -q` passes, `ruff check src` is clean.
Then reproduce the breakage: change the pin, `pip install -r requirements.txt`, `pytest -q`.
</start_state>

<target_state>
`requirements.txt` pins `pydantic==2.9.2` and nothing else in that file changed.
Verify:
  `git diff requirements.txt`  → exactly one changed line
  `pytest -q`                   → passes
  `ruff check src`              → clean
</target_state>

<allowed_files>
requirements.txt
src/models/user.py
src/models/order.py
src/api/schemas.py
</allowed_files>

<forbidden>
NEVER upgrade, add, or remove any other package. The diff in requirements.txt is one line.
NEVER edit a test to make it pass. If pydantic v2 genuinely changes validation behaviour, STOP and
report which test, which field, and what the old and new behaviour are — I decide, not you.
NEVER add `# type: ignore` or `model_config = ConfigDict(extra="allow")` to silence a failure.
NEVER touch files under migrations/ or alembic/.
</forbidden>

<stop_condition>
Stop when `pytest -q` passes and `ruff check src` is clean.
Maximum 3 attempts — this has a wider surface than a normal fix. After the third, STOP and report
the remaining failures grouped by root cause, and whether each is a v2 behaviour change or our bug.
</stop_condition>

After each file you modify, print the path and the v1→v2 API you replaced in it.
```

**KA**
```
განაახლე ზუსტად ერთი დამოკიდებულება და გაასწორე ის, რასაც ის ამტვრევს. სხვა არაფერი.

<start_state>
`requirements.txt`-ში ჩამაგრებულია `pydantic==1.10.13`. გვჭირდება 2.9.2.
ჯერ დაადასტურე ამჟამინდელი მწვანე მდგომარეობა: `pytest -q` გადის, `ruff check src` სუფთაა.
შემდეგ გაიმეორე ჩავარდნა: შეცვალე ვერსია, გაუშვი `pip install -r requirements.txt` და `pytest -q`.
</start_state>

<target_state>
`requirements.txt`-ში წერია `pydantic==2.9.2` და ამ ფაილში სხვა არაფერი შეცვლილა.
გადაამოწმე:
  `git diff requirements.txt`  → ზუსტად ერთი შეცვლილი ხაზი
  `pytest -q`                   → გადის
  `ruff check src`              → სუფთაა
</target_state>

<allowed_files>
requirements.txt
src/models/user.py
src/models/order.py
src/api/schemas.py
</allowed_files>

<forbidden>
არასდროს განაახლო, დაამატო ან წაშალო სხვა პაკეტი. requirements.txt-ის დიფი ერთი ხაზია.
არასდროს შეასწორო ტესტი მისი გასატარებლად. თუ pydantic v2 ნამდვილად ცვლის ვალიდაციის ქცევას,
შეჩერდი და მოახსენე, რომელი ტესტი, რომელი ველი და როგორ იქცეოდა ძველი და როგორ იქცევა ახალი —
გადაწყვეტილებას მე ვიღებ და არა შენ.
არასდროს დაამატო `# type: ignore` ან `model_config = ConfigDict(extra="allow")` ჩავარდნის ჩასაჩუმებლად.
არასდროს შეეხო migrations/-ისა და alembic/-ის ფაილებს.
</forbidden>

<stop_condition>
შეჩერდი, როცა `pytest -q` გაივლის და `ruff check src` სუფთა იქნება.
მაქსიმუმ 3 მცდელობა — აქ ზედაპირი ჩვეულებრივ შესწორებაზე ფართოა. მესამის შემდეგ შეჩერდი და მოახსენე
დარჩენილი ჩავარდნები, დაჯგუფებული მიზეზების მიხედვით, და თითოეულზე მიუთითე, v2-ის ქცევის
ცვლილებაა თუ ჩვენი ბაგი.
</stop_condition>

ყოველი შესწორებული ფაილის შემდეგ დაბეჭდე მისი მისამართი და რომელი v1→v2 API ჩაანაცვლე მასში.
```

---

### AC-09 · Implement a feature from a written spec
`claude-code` `cursor` `devin` `windsurf` — feature, spec-driven

**EN**
```
Implement exactly what the spec says. Nothing it does not say.

<spec>
{{spec}}
</spec>

<start_state>
`src/features/export/` does not exist.
Reproduce: `ls src/features/export` → No such file or directory.
Everything else in the repo is green: `npm test` passes on the current HEAD.
</start_state>

<target_state>
Every acceptance criterion in <spec> is met, and each one has a command that proves it.
Verify:
  `npm test -- export`  → passes
  `npm run typecheck`   → 0 errors
  then run each acceptance command from the spec and paste its output.
If any acceptance criterion in <spec> has no runnable command attached, STOP before writing any
code and ask me for one.
</target_state>

<allowed_files>
src/features/export/*        (new files, this directory only)
src/routes.ts                 (one line, to register the route)
tests/features/export.test.ts (new)
</allowed_files>

<forbidden>
NEVER implement anything the spec does not ask for — no extra flags, no "while I was here" options,
no admin endpoint that was not requested.
NEVER invent an acceptance criterion. Where the spec is silent, STOP and ask.
NEVER modify existing features to accommodate this one. If the spec requires it, stop and tell me.
NEVER install packages.
</forbidden>

<stop_condition>
Complete this in at most 25 tool calls.
Stop when `npm test -- export` and `npm run typecheck` pass and every acceptance command has been
run with its output shown.
Maximum 2 attempts at fixing a failing acceptance check. After the second, STOP and report which
criterion fails, the command, and the actual output.
</stop_condition>

Start by listing the acceptance criteria you extracted from <spec>, numbered, with the command for
each. Do not write code until that list is printed.
```

**KA**
```
დააიმპლემენტირე ზუსტად ის, რაც სპეციფიკაციაში წერია. ის, რაც არ წერია — არა.

<spec>
{{სპეციფიკაცია}}
</spec>

<start_state>
`src/features/export/` არ არსებობს.
გასამეორებელი ბრძანება: `ls src/features/export` → No such file or directory.
რეპოში დანარჩენი ყველაფერი მწვანეა: `npm test` ამჟამინდელ HEAD-ზე გადის.
</start_state>

<target_state>
<spec>-ის ყოველი მიღების კრიტერიუმი დაკმაყოფილებულია და თითოეულს აქვს ბრძანება, რომელიც ამას ადასტურებს.
გადაამოწმე:
  `npm test -- export`  → გადის
  `npm run typecheck`   → 0 შეცდომა
  შემდეგ გაუშვი სპეციფიკაციის ყოველი მიღების ბრძანება და ჩასვი მისი გამოსავალი.
თუ <spec>-ში რომელიმე კრიტერიუმს გასაშვები ბრძანება არ ახლავს, შეჩერდი კოდის წერამდე და მკითხე.
</target_state>

<allowed_files>
src/features/export/*        (ახალი ფაილები, მხოლოდ ამ დირექტორიაში)
src/routes.ts                 (ერთი ხაზი — როუტის დასარეგისტრირებლად)
tests/features/export.test.ts (ახალი)
</allowed_files>

<forbidden>
არასდროს დააიმპლემენტირო ის, რასაც სპეციფიკაცია არ ითხოვს — არც დამატებითი პარამეტრი, არც
„რაკი აქ ვიყავი“ ტიპის ოპცია, არც ადმინის ენდპოინტი, რომელიც არავის უთხოვია.
არასდროს გამოიგონო მიღების კრიტერიუმი. სადაც სპეციფიკაცია დუმს, შეჩერდი და მკითხე.
არასდროს გადააკეთო არსებული ფიჩერი ამის მოსარგებად. თუ სპეციფიკაცია ამას მოითხოვს, შეჩერდი და მომახსენე.
არასდროს დააინსტალირო პაკეტი.
</forbidden>

<stop_condition>
დაასრულე მაქსიმუმ 25 ინსტრუმენტის გამოძახებაში.
შეჩერდი, როცა `npm test -- export` და `npm run typecheck` გაივლის და ყოველი მიღების ბრძანება
გაშვებული იქნება ნაჩვენები გამოსავლით.
ჩავარდნილი კრიტერიუმის გასწორების მაქსიმუმ 2 მცდელობა. მეორის შემდეგ შეჩერდი და მოახსენე,
რომელი კრიტერიუმი ვარდება, რომელი ბრძანებით და რა გამოსავალი დაბრუნდა რეალურად.
</stop_condition>

დაიწყე იმით, რომ დანომრილად ჩამოწერო <spec>-იდან ამოკრებილი მიღების კრიტერიუმები და თითოეულის
შესამოწმებელი ბრძანება. სანამ ეს სია არ დაიბეჭდება, კოდი არ დაწერო.
```

---

### AC-10 · Wire a third-party API with failure handling
`claude-code` `cursor` `cline` — integration, resilience

**EN**
```
Replace a hardcoded value with a real API call, and handle every way that call can fail.

<start_state>
`src/services/fx.ts` returns a hardcoded GEL/USD rate of 2.70.
Reproduce: `rg -n "2.70" src/services/fx.ts` → one match.
The live source is the National Bank of Georgia:
`https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json` — no API key required.
Recorded responses for tests are in `tests/fixtures/nbg/`: `ok.json`, `malformed.json`, `500.txt`.
</start_state>

<target_state>
`getRate("USD")` fetches from the NBG endpoint with a 5s timeout, retries at most 2 times with
backoff, and on total failure returns the last cached rate plus a warning log. It NEVER throws into
the request path.
Verify: `npm test -- fx` passes, including the four failure tests: timeout, HTTP 500, malformed
JSON, and currency absent from the response.
</target_state>

<allowed_files>
src/services/fx.ts
src/services/fx-cache.ts        (new, if you need it)
tests/services/fx.test.ts
</allowed_files>

<forbidden>
NEVER call the live NBG endpoint from a test. Use the fixtures in tests/fixtures/nbg/.
NEVER catch an error and return a default rate silently — every fallback logs a warning with the
reason and the age of the cached rate.
NEVER retry more than 2 times, and NEVER retry an HTTP 4xx.
NEVER install an HTTP client — use the built-in `fetch`.
NEVER add an API key or a secret; this endpoint is public.
</forbidden>

<stop_condition>
Stop when `npm test -- fx` passes with all four failure tests present and passing.
Maximum 2 attempts. If a failure test still fails after the second, STOP and report which failure
mode is unhandled and what the code does instead. Do not delete or weaken the test.
</stop_condition>
```

**KA**
```
ჩაანაცვლე ჩაშენებული მნიშვნელობა რეალური API-გამოძახებით და დაამუშავე ყველა გზა, რომლითაც ის ჩავარდება.

<start_state>
`src/services/fx.ts` აბრუნებს GEL/USD-ის ჩაშენებულ კურსს 2.70.
გასამეორებელი ბრძანება: `rg -n "2.70" src/services/fx.ts` → ერთი დამთხვევა.
ცოცხალი წყაროა საქართველოს ეროვნული ბანკი:
`https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json` — გასაღები არ სჭირდება.
ჩაწერილი პასუხები ტესტებისთვის დევს `tests/fixtures/nbg/`-ში: `ok.json`, `malformed.json`, `500.txt`.
</start_state>

<target_state>
`getRate("USD")` მიმართავს NBG-ის ენდპოინტს 5-წამიანი ტაიმაუტით, ხელახლა ცდის მაქსიმუმ 2-ჯერ
დაყოვნებით, ხოლო სრული ჩავარდნისას აბრუნებს ბოლო ქეშირებულ კურსს და წერს გამაფრთხილებელ ლოგს.
მოთხოვნის გზაზე შეცდომას არასდროს აგდებს.
გადასამოწმებელი ბრძანება: `npm test -- fx` გადის, მათ შორის ოთხივე ჩავარდნის ტესტი: ტაიმაუტი,
HTTP 500, გაფუჭებული JSON და პასუხში ვალუტის არარსებობა.
</target_state>

<allowed_files>
src/services/fx.ts
src/services/fx-cache.ts        (ახალი, თუ დაგჭირდება)
tests/services/fx.test.ts
</allowed_files>

<forbidden>
არასდროს მიმართო ცოცხალ NBG-ენდპოინტს ტესტიდან. გამოიყენე `tests/fixtures/nbg/`-ის ფაილები.
არასდროს დაიჭირო შეცდომა და ჩუმად არ დააბრუნო ნაგულისხმევი კურსი — ყოველი დაბრუნება ლოგში წერს
მიზეზს და ქეშირებული კურსის ასაკს.
არასდროს გაიმეორო მოთხოვნა 2-ზე მეტჯერ და არასდროს გაიმეორო HTTP 4xx-ის შემთხვევაში.
არასდროს დააინსტალირო HTTP-კლიენტი — იმუშავე ჩაშენებული `fetch`-ით.
არასდროს დაამატო API-გასაღები ან საიდუმლო; ეს ენდპოინტი საჯაროა.
</forbidden>

<stop_condition>
შეჩერდი, როცა `npm test -- fx` გაივლის და ოთხივე ჩავარდნის ტესტი არსებობს და გადის.
მაქსიმუმ 2 მცდელობა. თუ მეორის შემდეგაც ვარდება რომელიმე მათგანი, შეჩერდი და მოახსენე, რომელი
ჩავარდნის სცენარი რჩება დაუმუშავებელი და რას აკეთებს კოდი მის ნაცვლად. ტესტი არ წაშალო და არ დაასუსტო.
</stop_condition>
```

---

### AC-11 · Database migration with a rollback
`claude-code` `cursor` `devin` — database, migrations

**EN**
```
Write one migration and the rollback that undoes it exactly.

<start_state>
The `orders` table has no `cancelled_at` column.
Reproduce: `psql $DATABASE_URL -c "\d orders"` → no cancelled_at in the output.
DATABASE_URL points at the local dev database only. Migrations run with node-pg-migrate:
`npm run migrate:up`, `npm run migrate:down`.
</start_state>

<target_state>
`orders.cancelled_at TIMESTAMPTZ NULL` exists, with a partial index on rows where it is not null.
The rollback removes both and leaves `\d orders` byte-identical to its current output.
Verify, in this exact order:
  `psql $DATABASE_URL -c "\d orders" > /tmp/before.txt`
  `npm run migrate:up && npm run migrate:down && npm run migrate:up`   → all three exit 0
  `npm run migrate:down && psql $DATABASE_URL -c "\d orders" > /tmp/after.txt`
  `diff /tmp/before.txt /tmp/after.txt`   → no output
</target_state>

<allowed_files>
migrations/1757779200000_add-orders-cancelled-at.js   (new)
src/db/schema.ts
</allowed_files>

<forbidden>
NEVER edit an existing migration file. Applied migrations are immutable.
NEVER write a down migration that silently destroys data. If the rollback loses data, say so in a
comment at the top and STOP to ask before running it.
NEVER add NOT NULL without a default on this table — it has ~2M rows.
NEVER run anything against a database other than the local DATABASE_URL.
NEVER run raw DDL in psql to "fix" a half-applied state.
</forbidden>

<stop_condition>
Stop when the up/down/up cycle and the diff check both pass.
Maximum 2 attempts. If `npm run migrate:down` errors at any point, STOP IMMEDIATELY and report the
error and the current state of the migrations table. Do not attempt a manual repair in psql.
</stop_condition>
```

**KA**
```
დაწერე ერთი მიგრაცია და rollback, რომელიც მას ზუსტად აბრუნებს უკან.

<start_state>
ცხრილ `orders`-ს არ აქვს სვეტი `cancelled_at`.
გასამეორებელი ბრძანება: `psql $DATABASE_URL -c "\d orders"` → გამოსავალში cancelled_at არ ჩანს.
DATABASE_URL მხოლოდ ლოკალურ სადეველოპმენტო ბაზაზე მიუთითებს. მიგრაციები node-pg-migrate-ზეა:
`npm run migrate:up`, `npm run migrate:down`.
</start_state>

<target_state>
არსებობს `orders.cancelled_at TIMESTAMPTZ NULL` და ნაწილობრივი ინდექსი იმ სტრიქონებზე, სადაც ის
არ არის null.
rollback ორივეს შლის და `\d orders`-ის გამოსავალს ზუსტად ისეთს ტოვებს, როგორიც ახლაა.
გადაამოწმე ზუსტად ამ თანმიმდევრობით:
  `psql $DATABASE_URL -c "\d orders" > /tmp/before.txt`
  `npm run migrate:up && npm run migrate:down && npm run migrate:up`   → სამივე 0 კოდით სრულდება
  `npm run migrate:down && psql $DATABASE_URL -c "\d orders" > /tmp/after.txt`
  `diff /tmp/before.txt /tmp/after.txt`   → ცარიელი გამოსავალი
</target_state>

<allowed_files>
migrations/1757779200000_add-orders-cancelled-at.js   (ახალი)
src/db/schema.ts
</allowed_files>

<forbidden>
არასდროს შეასწორო არსებული მიგრაციის ფაილი. გაშვებული მიგრაცია უცვლელია.
არასდროს დაწერო down-მიგრაცია, რომელიც ჩუმად შლის მონაცემებს. თუ rollback მონაცემს კარგავს,
ეს ფაილის თავში კომენტარად დაწერე და გაშვებამდე შეჩერდი და მკითხე.
არასდროს დაამატო NOT NULL ნაგულისხმევი მნიშვნელობის გარეშე — ამ ცხრილში ~2 მილიონი სტრიქონია.
არასდროს გაუშვა არაფერი ლოკალური DATABASE_URL-ის გარდა სხვა ბაზაზე.
არასდროს გაუშვა ხელით DDL psql-ში ნახევრად გაშვებული მდგომარეობის „გასასწორებლად“.
</forbidden>

<stop_condition>
შეჩერდი, როცა up/down/up ციკლიც გაივლის და diff-შემოწმებაც.
მაქსიმუმ 2 მცდელობა. თუ `npm run migrate:down` რომელიმე ეტაპზე შეცდომას დააბრუნებს, მაშინვე
შეჩერდი და მოახსენე შეცდომა და მიგრაციების ცხრილის ამჟამინდელი მდგომარეობა. psql-ში ხელით
შეკეთება არ სცადო.
</stop_condition>
```

---

### AC-12 · Read-only investigation
`claude-code` `cursor` `cline` `devin` — investigation, read-only

**EN**
```
Investigate and report. Change nothing. This task produces a document, not a diff.

<start_state>
Production logs show `ERR_CONNECTION_RESET` on `POST /api/upload` for about 3% of requests,
starting 2026-09-08. It does not reproduce locally.
Reproduce what you can, read-only:
  `git log --since=2026-09-01 --oneline -- src/api/upload.ts src/middleware/`
  `rg -n "maxBodySize|timeout|keepAlive" src/ nginx/`
  `npm run typecheck`   (read-only, safe)
</start_state>

<target_state>
A written report with: the three most likely causes ranked, the evidence for and against each,
the one command or log query that would confirm the top cause, and the smallest safe fix for it —
described, NOT applied.
Verify: `git status --porcelain` → no output. The working tree must be untouched.
</target_state>

<allowed_files>
NONE. This task is read-only.
You may READ any file in the repo and run read-only commands: rg, git log, git show, git diff,
cat, npm run typecheck, go vet.
You may NOT create, edit, move or delete any file, including scratch and note files.
</allowed_files>

<forbidden>
NEVER write to disk. No new file, no edit, not even a temporary one.
NEVER run a command that mutates state: no npm install, no go mod tidy, no formatter, no migration,
no git checkout, no git stash.
NEVER commit anything.
NEVER apply a fix, even an obvious one-line one. Describe it and stop.
</forbidden>

<stop_condition>
Complete this in at most 20 tool calls.
Stop when the report is written. If you have not found a confident cause within 20 calls, STOP and
report the three ranked hypotheses with the evidence you gathered, marking clearly what you could
not check and what you would need to check it.
</stop_condition>

Output sections: What I checked · Ranked causes (3) · Evidence for and against each ·
Confirming command · Proposed fix (not applied) · What I could not check
```

**KA**
```
გამოიკვლიე და მოახსენე. არაფერი შეცვალო. ამ ამოცანის შედეგი დოკუმენტია და არა დიფი.

<start_state>
პროდაქშენის ლოგებში `POST /api/upload`-ზე მოთხოვნების დაახლოებით 3%-ს უბრუნდება
`ERR_CONNECTION_RESET`; დაიწყო 2026-09-08-ს. ლოკალურად არ მეორდება.
გაიმეორე ის, რაც შეგიძლია, მხოლოდ კითხვით:
  `git log --since=2026-09-01 --oneline -- src/api/upload.ts src/middleware/`
  `rg -n "maxBodySize|timeout|keepAlive" src/ nginx/`
  `npm run typecheck`   (მხოლოდ კითხულობს, უსაფრთხოა)
</start_state>

<target_state>
წერილობითი დასკვნა, რომელშიც იქნება: სამი ყველაზე სავარაუდო მიზეზი რანჟირებული, თითოეულის
სასარგებლო და საწინააღმდეგო მტკიცებულება, ერთი ბრძანება ან ლოგის მოთხოვნა, რომელიც მთავარ ვარაუდს
დაადასტურებდა, და მისი ყველაზე მცირე უსაფრთხო გამოსწორება — აღწერილი და არა გაკეთებული.
გადასამოწმებელი ბრძანება: `git status --porcelain` → ცარიელი გამოსავალი. სამუშაო ხე უცვლელი უნდა იყოს.
</target_state>

<allowed_files>
არცერთი. ეს ამოცანა მხოლოდ კითხვისაა.
შეგიძლია წაიკითხო რეპოს ნებისმიერი ფაილი და გაუშვა მხოლოდ კითხვადი ბრძანებები: rg, git log,
git show, git diff, cat, npm run typecheck, go vet.
არ შეგიძლია შექმნა, შეასწორო, გადაიტანო ან წაშალო ფაილი — არც სამუშაო და არც სანოტო ფაილი.
</allowed_files>

<forbidden>
არასდროს ჩაწერო რამე დისკზე. არც ახალი ფაილი, არც შესწორება, არც დროებითი ფაილი.
არასდროს გაუშვა ბრძანება, რომელიც მდგომარეობას ცვლის: არც npm install, არც go mod tidy,
არც ფორმატერი, არც მიგრაცია, არც git checkout, არც git stash.
არასდროს გააკეთო კომიტი.
არასდროს გაასწორო კოდი, თუნდაც ერთხაზიანი და აშკარა შესწორება იყოს. აღწერე და შეჩერდი.
</forbidden>

<stop_condition>
დაასრულე მაქსიმუმ 20 ინსტრუმენტის გამოძახებაში.
შეჩერდი, როცა დასკვნა დაწერილია. თუ 20 გამოძახებაში დამაჯერებელ მიზეზამდე ვერ მიხვალ, შეჩერდი და
მოახსენე სამივე რანჟირებული ვარაუდი შეგროვებულ მტკიცებულებებთან ერთად; ცალკე მიუთითე, რისი
შემოწმება ვერ შეძელი და რა დაგჭირდებოდა ამისთვის.
</stop_condition>

გამოსავალი სექციებად: რა შევამოწმე · სამი რანჟირებული მიზეზი · თითოეულის სასარგებლო და
საწინააღმდეგო მტკიცებულება · დამადასტურებელი ბრძანება · შემოთავაზებული გამოსწორება (გაუკეთებელი) ·
რისი შემოწმება ვერ შევძელი
```

---

### AC-13 · Fix a CI failure from a pasted log
`claude-code` `cursor` `codex` `windsurf` — ci, bugfix

**EN**
```
Fix the code that made CI fail. Do not fix CI.

<ci_log>
{{ci_log}}
</ci_log>

<start_state>
The `build-and-test` job fails on branch `feat/checkout`. The log above is the full job output.
Reproduce locally with the exact commands the workflow runs, in order:
  `npm ci`
  `npm run lint`
  `npm test -- --ci --runInBand`
Report which of the three fails locally before you change anything. If none fails locally, STOP and
say so — the difference is environmental and I need to know that, not a guess at a fix.
</start_state>

<target_state>
All three commands pass locally, with the same Node version CI uses (see .nvmrc).
Verify: `npm ci && npm run lint && npm test -- --ci --runInBand` exits 0.
</target_state>

<allowed_files>
The source files named in <ci_log> only. List them before you start.
tests/ files only if the log shows the test itself is wrong — and say why.
</allowed_files>

<forbidden>
NEVER edit anything under .github/workflows/ to make the job pass. If the workflow itself is wrong,
STOP and tell me which step and why.
NEVER skip, `.skip`, `.only`, or delete a failing test.
NEVER change a dependency version to work around the failure.
NEVER increase a test timeout unless the log shows a genuine timeout, and say so if you do.
NEVER re-run CI hoping it is flaky. If you believe it is flaky, report the evidence from the log.
</forbidden>

<stop_condition>
Stop when the three commands pass locally.
Maximum 2 attempts. If they still fail after the second, STOP and report: which command, the exact
local output, how it differs from <ci_log>, and your best hypothesis. Do not try a third approach.
</stop_condition>

Start by printing one line: which of the three steps failed and the single line in <ci_log> that
says so.
```

**KA**
```
გაასწორე კოდი, რომლის გამოც CI ჩავარდა. თვითონ CI არ გაასწორო.

<ci_log>
{{ლოგი}}
</ci_log>

<start_state>
job `build-and-test` ვარდება ბრანჩზე `feat/checkout`. ზემოთ მოცემულია job-ის სრული გამოსავალი.
გაიმეორე ლოკალურად ზუსტად იმ ბრძანებებით, რომლებსაც workflow უშვებს, ამავე თანმიმდევრობით:
  `npm ci`
  `npm run lint`
  `npm test -- --ci --runInBand`
სანამ რამეს შეცვლი, მოახსენე, სამიდან რომელი ვარდება ლოკალურად. თუ ლოკალურად არცერთი ვარდება,
შეჩერდი და ეს პირდაპირ დაწერე — მაშინ განსხვავება გარემოშია და ეს უნდა ვიცოდე, და არა შენი ვარაუდი
გამოსწორებაზე.
</start_state>

<target_state>
სამივე ბრძანება ლოკალურად გადის, CI-ის იმავე Node-ის ვერსიაზე (იხ. .nvmrc).
გადასამოწმებელი ბრძანება: `npm ci && npm run lint && npm test -- --ci --runInBand` სრულდება 0 კოდით.
</target_state>

<allowed_files>
მხოლოდ ის საწყისი ფაილები, რომლებიც <ci_log>-შია დასახელებული. ჯერ ჩამოწერე ისინი.
tests/-ის ფაილები მხოლოდ მაშინ, თუ ლოგი აჩვენებს, რომ თვითონ ტესტია მცდარი — და დაწერე, რატომ.
</allowed_files>

<forbidden>
არასდროს შეასწორო .github/workflows/-ის ფაილი job-ის გასატარებლად. თუ თვითონ workflow-შია შეცდომა,
შეჩერდი და დამისახელე, რომელ ეტაპზე და რატომ.
არასდროს გამორთო ტესტი, არ დაუწერო `.skip` ან `.only` და არ წაშალო ჩავარდნილი ტესტი.
არასდროს შეცვალო დამოკიდებულების ვერსია პრობლემის გვერდის ავლით.
არასდროს გაზარდო ტესტის ტაიმაუტი, თუ ლოგი რეალურ ტაიმაუტს არ აჩვენებს — და თუ გაზრდი, ეს დაწერე.
არასდროს გადაუშვა CI იმ იმედით, რომ ტესტი არასტაბილურია. თუ ასე გგონია, მოიყვანე მტკიცებულება ლოგიდან.
</forbidden>

<stop_condition>
შეჩერდი, როცა სამივე ბრძანება ლოკალურად გაივლის.
მაქსიმუმ 2 მცდელობა. თუ მეორის შემდეგაც ვარდება, შეჩერდი და მოახსენე: რომელი ბრძანება, ზუსტად
რა გამოსავალი დაბრუნდა ლოკალურად, რით განსხვავდება ის <ci_log>-ისგან და რა ვარაუდი გაქვს.
მესამე მიდგომა არ სცადო.
</stop_condition>

დაიწყე ერთი ხაზით: სამი ეტაპიდან რომელი ჩავარდა და <ci_log>-ის რომელი ხაზი ამბობს ამას.
```
