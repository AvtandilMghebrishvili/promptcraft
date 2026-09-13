# Debugging / დებაგინგი

Every prompt in this file separates diagnosis from repair. A model that is allowed to edit while it
is still guessing writes a plausible patch for a cause it never established — and tomorrow you debug
the patch instead of the bug. Name the cause, name the evidence, name the cheapest check that would
kill it. Only then touch code.

ამ ფაილში ყოველი პრომპტი დიაგნოზს შეკეთებისგან მიჯნავს. მოდელი, რომელსაც რედაქტირების უფლება ჯერ
კიდევ გამოცნობის ეტაპზე აქვს, წერს დამაჯერებელ შესწორებას მიზეზისთვის, რომელიც არც დაუდასტურებია —
და ხვალ უკვე ამ შესწორებას დაადებუგებ და არა ბაგს. დაასახელე მიზეზი, დაასახელე მისი მტკიცებულება და
დაასახელე ყველაზე იაფი შემოწმება, რომელიც მას მოკლავდა. კოდს მხოლოდ ამის შემდეგ შეეხე.

---

### DB-01 · Read a stack trace, rank the causes
`claude` `gpt` `claude-code` — triage, stack-trace

**EN**
```
You are a debugger. Read the stack trace and name the causes. Fix nothing.

<stack_trace>
{{stack_trace}}
</stack_trace>

<context>
Language and runtime: {{runtime}}
What the user was doing when it happened: {{user_action}}
Frequency: {{frequency}}
Last deploy before it started: {{last_deploy}}
</context>

Base every claim on the supplied output. If the evidence does not distinguish between two causes,
say so and name the check that would. NEVER invent a frame, a file, a line number or a value that
is not in the trace.

Do not edit any files. Analysis only.
NEVER propose a fix until you have named the cause and the evidence for it.

Output exactly these three sections:

1. THE FAILING FRAME — the first frame in our code rather than in a library, with file and line,
   and the value that must have been wrong for that line to throw. If the first non-library frame
   is ambiguous, name both and say why.

2. THREE CAUSES, RANKED — for each one:
   · the cause in one sentence
   · the lines of the trace that support it
   · what in the trace argues against it
   · the cheapest check that would confirm or kill it — a command, a log query, or a single print
     statement. Say which of the three it is.

3. WHAT THE TRACE CANNOT TELL US — the input value, log line or environment variable you would
   need, and why the trace alone cannot settle it.

When two causes are equally likely, rank first the one whose discriminating check is cheaper.
```

**KA**
```
შენ ხარ დებაგერი. წაიკითხე სტეკ-ტრეისი და დაასახელე მიზეზები. არაფერი გაასწორო.

<stack_trace>
{{სტეკ_ტრეისი}}
</stack_trace>

<context>
ენა და გარემო: {{გარემო}}
რას აკეთებდა მომხმარებელი ამ მომენტში: {{მოქმედება}}
სიხშირე: {{სიხშირე}}
ბოლო დეპლოი დაწყებამდე: {{დეპლოი}}
</context>

ყოველი მტკიცება მოცემულ გამოსავალს დააფუძნე. თუ მტკიცებულება ორ მიზეზს ერთმანეთისგან ვერ არჩევს,
ეს პირდაპირ დაწერე და დაასახელე შემოწმება, რომელიც გაარჩევდა. არასდროს გამოიგონო ფრეიმი, ფაილი,
ხაზის ნომერი ან მნიშვნელობა, რომელიც ტრეისში არ წერია.

არცერთი ფაილი არ შეასწორო. მხოლოდ ანალიზი.
არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.

გამოსავალი — ზუსტად ეს სამი სექცია:

1. ჩავარდნილი ფრეიმი — პირველი ფრეიმი ჩვენს კოდში და არა ბიბლიოთეკაში: ფაილი და ხაზი, და ის
   მნიშვნელობა, რომელიც არასწორი უნდა ყოფილიყო, რომ ამ ხაზს შეცდომა აეგდო. თუ პირველი
   არაბიბლიოთეკური ფრეიმი ორაზროვანია, ორივე დაასახელე და ახსენი, რატომ.

2. სამი მიზეზი, რანჟირებული — თითოეულზე:
   · მიზეზი ერთი წინადადებით
   · ტრეისის ხაზები, რომლებიც მას ადასტურებენ
   · რა ეწინააღმდეგება მას ტრეისში
   · ყველაზე იაფი შემოწმება, რომელიც მას დაადასტურებს ან მოკლავს — ბრძანება, ლოგის მოთხოვნა ან
     ერთი print. მიუთითე, სამიდან რომელია.

3. რას ვერ გვეუბნება ტრეისი — შემავალი მნიშვნელობა, ლოგის ხაზი ან გარემოს ცვლადი, რომელიც
   დაგჭირდებოდა, და რატომ ვერ წყვეტს ამას მარტო ტრეისი.

როცა ორი მიზეზი თანაბრად სავარაუდოა, წინ ის დააყენე, რომლის გამრჩევი შემოწმებაც უფრო იაფია.
```

---

### DB-02 · Design a minimal reproduction
`claude` `gpt` `claude-code` — reproduction, isolation

**EN**
```
Design the smallest program that still shows this bug. Design it — do not write the fix.

<bug>
What I see: {{symptom}}
Where: {{where}}
The code path involved, as far as I know it: {{path}}
</bug>

<current_repro>
{{current_repro}}
</current_repro>

The current reproduction needs the whole application. I want one file that runs in under 5 seconds.

Base every claim on the supplied code and output. If you need a value I did not give you, write
`UNKNOWN: <what>` and carry on — NEVER guess it.

Work by subtraction, not by rewriting:
- Start from <current_repro> and name, in order, each layer you would remove: the database, the
  HTTP layer, the queue, the auth middleware, the ORM, the framework itself.
- For each removal, state what it proves if the bug SURVIVES it and what it proves if the bug
  DISAPPEARS. A removal that proves nothing either way is not worth doing — drop it from the list.

Output:
1. REMOVAL ORDER — numbered, each with its survives/disappears pair.
2. THE TARGET REPRO — a single file: fake data inline, no network, no database, and the exact
   command that runs it.
3. THE ASSERTION — the one line that is true in a working system and false in a broken one.
4. IF IT DOES NOT REPRODUCE — the three most likely reasons the minimal version is too minimal,
   each with the layer you would put back first.

Do not edit any files in the repo. Print the repro as a code block and I will place it myself.
```

**KA**
```
შეადგინე ყველაზე მცირე პროგრამა, რომელშიც ეს ბაგი ისევ ჩანს. მხოლოდ შეადგინე — გამოსწორება არ დაწერო.

<bug>
რას ვხედავ: {{სიმპტომი}}
სად: {{სად}}
კოდის გზა, რამდენადაც ვიცი: {{გზა}}
</bug>

<current_repro>
{{ამჟამინდელი_გამეორება}}
</current_repro>

ამჟამინდელ გამეორებას მთელი აპლიკაცია სჭირდება. მე მინდა ერთი ფაილი, რომელიც 5 წამზე ნაკლებში გაეშვება.

ყოველი მტკიცება მოცემულ კოდსა და გამოსავალს დააფუძნე. თუ მნიშვნელობა, რომელიც გჭირდება, არ მოგეცი,
დაწერე `UNKNOWN: <რა>` და გააგრძელე — არასდროს გამოიცნო იგი.

იმუშავე გამოკლებით და არა გადაწერით:
- დაიწყე <current_repro>-დან და თანმიმდევრობით დაასახელე, რომელ ფენას ამოაგდებდი: ბაზას,
  HTTP-ფენას, რიგს, ავტორიზაციის middleware-ს, ORM-ს, თვითონ ფრეიმვორკს.
- ყოველ ამოგდებაზე დაწერე, რას ამტკიცებს ის, თუ ბაგი გადარჩება, და რას — თუ ბაგი გაქრება.
  ამოგდება, რომელიც ვერც ერთს ამტკიცებს და ვერც მეორეს, არ ღირს — სიიდან ამოიღე.

გამოსავალი:
1. ამოგდების თანმიმდევრობა — დანომრილი, თითოეულთან წყვილი „თუ გადარჩა / თუ გაქრა“.
2. სამიზნე გამეორება — ერთი ფაილი: ხელოვნური მონაცემები პირდაპირ კოდში, ქსელის და ბაზის გარეშე,
   და ზუსტი ბრძანება მის გასაშვებად.
3. მტკიცება — ერთი ხაზი, რომელიც მუშა სისტემაში ჭეშმარიტია და გაფუჭებულში — მცდარი.
4. თუ ბაგი არ მეორდება — სამი ყველაზე სავარაუდო მიზეზი, რატომ აღმოჩნდა მინიმალური ვერსია ზედმეტად
   მინიმალური, და თითოეულთან ის ფენა, რომელსაც პირველად დააბრუნებდი.

რეპოში არცერთი ფაილი არ შეასწორო. გამეორება დაბეჭდე კოდის ბლოკად — ჩასმას თვითონ მოვახერხებ.
```

---

### DB-03 · Bisect a regression between two commits
`claude-code` `cursor` `gpt` — regression, git

**EN**
```
Plan a bisect and tell me how to read its result. The goal is a commit, not a patch.

<regression>
Good: `{{good_ref}}` — evidence: {{good_evidence}}
Bad:  `{{bad_ref}}`  — evidence: {{bad_evidence}}
Commits between them: {{commit_count}}
Build and test commands: {{commands}}
</regression>

Base every claim on the supplied evidence. If the good evidence and the bad evidence do not measure
the same thing, STOP and say so — a bisect run on an inconsistent test finds a random commit and
you will trust it.

The check that separates good from bad must be exact, fast and non-interactive. Write it first.

Output:

1. THE CHECK SCRIPT — `bisect-check.sh`: exit 0 for good, exit 1 for bad, `exit 125` for a commit
   that cannot be built or tested at all. Say which line does which.

2. THE COMMANDS, in order —
   `git bisect start <bad> <good>`
   `git bisect run ./bisect-check.sh`
   `git bisect reset`
   and what the output of each looks like, including how many steps ≈log2({{commit_count}}) means.

3. TRAPS TO CHECK BEFORE STARTING —
   · does the check itself exist in every commit in the range? (if not, it belongs outside the tree)
   · do dependencies need reinstalling per commit, and does the script do it?
   · is the symptom intermittent? If it is, bisect is the wrong tool — say so instead of proceeding.
   · are there merge commits whose parents were never individually green?

4. AFTER THE FIRST BAD COMMIT — what `git show <sha>` must contain for that commit to genuinely
   explain the regression, and what it means if the diff looks unrelated to the symptom (the commit
   may have exposed an older bug rather than introduced one).

Do not edit any files. Analysis only.
```

**KA**
```
დაგეგმე bisect და ამიხსენი, როგორ წავიკითხო მისი შედეგი. მიზანი კომიტია და არა შესწორება.

<regression>
კარგი: `{{good_ref}}` — მტკიცებულება: {{კარგის_მტკიცებულება}}
ცუდი: `{{bad_ref}}` — მტკიცებულება: {{ცუდის_მტკიცებულება}}
კომიტი მათ შორის: {{კომიტების_რაოდენობა}}
აგებისა და ტესტირების ბრძანებები: {{ბრძანებები}}
</regression>

ყოველი მტკიცება მოცემულ მტკიცებულებას დააფუძნე. თუ კარგისა და ცუდის მტკიცებულება ერთსა და იმავეს
არ ზომავს, შეჩერდი და ეს დაწერე — არათანმიმდევრულ ტესტზე გაშვებული bisect შემთხვევით კომიტს იპოვის,
შენ კი დაუჯერებ.

შემოწმება, რომელიც კარგს ცუდისგან არჩევს, უნდა იყოს ზუსტი, სწრაფი და ინტერაქციის გარეშე. ჯერ ის დაწერე.

გამოსავალი:

1. შემოწმების სკრიპტი — `bisect-check.sh`: კარგზე 0, ცუდზე 1, ხოლო კომიტზე, რომელიც საერთოდ ვერ
   აიგება ან ვერ დატესტდება — `exit 125`. მიუთითე, რომელი ხაზი რას აკეთებს.

2. ბრძანებები, თანმიმდევრობით —
   `git bisect start <bad> <good>`
   `git bisect run ./bisect-check.sh`
   `git bisect reset`
   და როგორ გამოიყურება თითოეულის გამოსავალი, მათ შორის რას ნიშნავს ≈log2({{კომიტების_რაოდენობა}}) ნაბიჯი.

3. რა უნდა შემოწმდეს დაწყებამდე —
   · არსებობს თუ არა თვითონ შემოწმება დიაპაზონის ყველა კომიტში? (თუ არა, სკრიპტს ხის გარეთ ადგილი აქვს)
   · სჭირდება თუ არა დამოკიდებულებების ხელახლა დაყენება ყოველ კომიტზე და აკეთებს თუ არა ამას სკრიპტი?
   · სიმპტომი დროდადრო ჩნდება? თუ ასეა, bisect არასწორი ინსტრუმენტია — ეს დაწერე და ნუ გააგრძელებ.
   · არის თუ არა დიაპაზონში merge-კომიტი, რომლის მშობლებიც ცალ-ცალკე არასდროს ყოფილა მწვანე?

4. პირველი ცუდი კომიტის შემდეგ — რა უნდა ეწეროს `git show <sha>`-ში, რომ ამ კომიტმა რეგრესია
   მართლა ახსნას, და რას ნიშნავს, თუ დიფს სიმპტომთან კავშირი არ ეტყობა (შესაძლოა, კომიტმა ძველი
   ბაგი გამოააშკარავა და არა ახალი შემოიტანა).

არცერთი ფაილი არ შეასწორო. მხოლოდ ანალიზი.
```

---

### DB-04 · Why this test is flaky, and how to prove it
`claude` `gpt` `claude-code` — testing, flakiness

**EN**
```
Explain why this test is flaky and name the command that proves it. Do not make it pass.

<test>
{{test_code}}
</test>

<evidence>
Pass rate: {{pass_rate}} over {{runs}} runs
Output when it fails: {{failure_output}}
CI runs the suite with: {{runner_flags}}
Does it fail in isolation: {{isolation_result}}
</evidence>

Base every claim on the supplied test code and output. If the evidence does not distinguish between
two causes, say so and name the check that would.

Check the causes against this list and discard the ones the evidence rules out:
shared mutable state between tests · test-order dependence · real clock or timezone · unseeded
randomness · a real network or filesystem call · an unawaited promise or a missing join · a fixed
sleep standing in for a condition · parallel workers sharing a database, a port or a temp directory.

Output:
1. RANKED CAUSES (3) — evidence for, evidence against, and the one check that separates it from
   the cause ranked next to it.
2. THE PROOF COMMAND — the exact command that makes it fail reliably rather than occasionally,
   for example `pytest tests/ -p no:randomly --count 50 -x`, or the test run alone versus run inside
   its file. Say what result confirms the top cause and what result refutes it.
3. THE QUARANTINE LINE — how to mark it known-flaky today without deleting it, skipping it or
   weakening its assertion.

NEVER propose a fix until you have named the cause and the evidence for it.
NEVER offer a retry wrapper, a longer timeout or `.skip` as the answer — each of those hides the
cause and keeps the bug.
```

**KA**
```
ახსენი, რატომ არის ეს ტესტი არასტაბილური, და დაასახელე ბრძანება, რომელიც ამას დაამტკიცებს.
გატარება არ სცადო.

<test>
{{ტესტის_კოდი}}
</test>

<evidence>
გატარების მაჩვენებელი: {{მაჩვენებელი}} — {{გაშვებები}} გაშვებაზე
რა ბრუნდება ჩავარდნისას: {{ჩავარდნის_გამოსავალი}}
CI ტესტებს ასე უშვებს: {{ფლაგები}}
ვარდება თუ არა ცალკე გაშვებისას: {{ცალკე_გაშვება}}
</evidence>

ყოველი მტკიცება მოცემულ კოდსა და გამოსავალს დააფუძნე. თუ მტკიცებულება ორ მიზეზს ერთმანეთისგან
ვერ არჩევს, ეს დაწერე და დაასახელე შემოწმება, რომელიც გაარჩევდა.

გადაამოწმე მიზეზები ამ სიის მიხედვით და ამოაგდე ის, რასაც მტკიცებულება გამორიცხავს:
საერთო ცვალებადი მდგომარეობა ტესტებს შორის · ტესტების თანმიმდევრობაზე დამოკიდებულება · რეალური
საათი ან დროის სარტყელი · თესლის გარეშე დარჩენილი შემთხვევითობა · რეალური ქსელის ან ფაილური
სისტემის გამოძახება · დაუცდელი promise ან გამოტოვებული join · ფიქსირებული sleep პირობის ნაცვლად ·
პარალელური worker-ები, რომლებიც ერთსა და იმავე ბაზას, პორტს ან დროებით დირექტორიას იზიარებენ.

გამოსავალი:
1. რანჟირებული მიზეზები (3) — სასარგებლო მტკიცებულება, საწინააღმდეგო მტკიცებულება და ერთი
   შემოწმება, რომელიც მას მომდევნო მიზეზისგან გაარჩევს.
2. დამადასტურებელი ბრძანება — ზუსტი ბრძანება, რომლითაც ტესტი სტაბილურად ვარდება და არა დროდადრო:
   მაგალითად `pytest tests/ -p no:randomly --count 50 -x`, ან ტესტის ცალკე გაშვება მისივე ფაილში
   გაშვებასთან შედარებით. დაწერე, რომელი შედეგი ადასტურებს მთავარ ვარაუდს და რომელი — უარყოფს.
3. კარანტინის ხაზი — როგორ მოვნიშნო ის დღესვე როგორც ცნობილი არასტაბილური ისე, რომ არც წაიშალოს,
   არც გამოირთოს და არც მისი მტკიცება დასუსტდეს.

არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
არასდროს შემომთავაზო პასუხად ხელახლა ცდის wrapper-ი, გაზრდილი ტაიმაუტი ან `.skip` — თითოეული
მიზეზს მალავს და ბაგს ტოვებს.
```

---

### DB-05 · Race condition analysis
`claude` `gpt` `gemini` — concurrency, analysis

**EN**
```
Analyse this code for a race condition. Reason about interleavings, not about style.

<code>
{{code}}
</code>

<symptom>
What goes wrong: {{symptom}}
Concurrency model: {{model}}   (threads / goroutines / async tasks / separate processes / replicas)
How often: {{frequency}}
Under what load it appears: {{load}}
</symptom>

Base every claim on the supplied code. NEVER assume a lock, a transaction, an atomic operation or a
single-threaded event loop that is not visible in the code — if you cannot see what protects a value,
treat it as unprotected and say so.

For every piece of shared state, give:
· its name and where it lives — process memory, a database row, a cache key, a file
· every read and every write, with the line number
· whether a read and its write are separated by a point where another worker can run: an `await`,
  a channel operation, an I/O call, a lock release, a transaction boundary
· the interleaving that breaks it, written as an ordered trace — T1 line X, T2 line Y, T1 line Z —
  and the wrong value it leaves behind

Output:
1. SHARED STATE TABLE, as above.
2. THE WINNING INTERLEAVING — the ordered trace, and the symptom a user would observe from it.
   State whether that matches <symptom>. If it does not, say so plainly rather than adjusting the
   trace until it fits.
3. WHY THE OBVIOUS READING IS WRONG — the one check-then-act, read-modify-write or double-checked
   pattern here that looks safe and is not.
4. THE DISCRIMINATING TEST — how to make the race fire on demand: a sleep injected at a named line,
   a stress loop with N workers, `go test -race`, a thread sanitiser, or a forced two-replica run.
   Say what a passing run would and would not prove.

Do not edit any files. Analysis only.
NEVER propose a fix until you have named the cause and the evidence for it.
```

**KA**
```
გააანალიზე ეს კოდი და იპოვე race condition. იმსჯელე თანმიმდევრობების გადაჯაჭვაზე და არა სტილზე.

<code>
{{კოდი}}
</code>

<symptom>
რა ფუჭდება: {{სიმპტომი}}
კონკურენტულობის მოდელი: {{მოდელი}}   (thread / goroutine / async-ამოცანა / ცალკე პროცესი / რეპლიკა)
რამდენად ხშირად: {{სიხშირე}}
რა დატვირთვაზე ჩნდება: {{დატვირთვა}}
</symptom>

ყოველი მტკიცება მოცემულ კოდს დააფუძნე. არასდროს იგულისხმო ბოქლომი, ტრანზაქცია, ატომური ოპერაცია ან
ერთნაკადიანი event loop, რომელიც კოდში არ ჩანს — თუ ვერ ხედავ, რა იცავს მნიშვნელობას, ჩათვალე
დაუცველად და ეს დაწერე.

საერთო მდგომარეობის ყოველ ნაწილზე მოგვეცი:
· სახელი და სად ინახება — პროცესის მეხსიერება, ბაზის სტრიქონი, ქეშის გასაღები, ფაილი
· ყოველი წაკითხვა და ყოველი ჩაწერა, ხაზის ნომრით
· ყოფს თუ არა წაკითხვასა და ჩაწერას წერტილი, სადაც სხვა worker-ს გაშვება შეუძლია: `await`,
  არხზე ოპერაცია, I/O-გამოძახება, ბოქლომის გათავისუფლება, ტრანზაქციის საზღვარი
· გადაჯაჭვა, რომელიც ამას ამტვრევს, დაწერილი მოწესრიგებულ ტრეისად — T1 ხაზი X, T2 ხაზი Y,
  T1 ხაზი Z — და რა არასწორი მნიშვნელობა რჩება შედეგად

გამოსავალი:
1. საერთო მდგომარეობის ცხრილი, ზემოთ აღწერილი ველებით.
2. გამარჯვებული გადაჯაჭვა — მოწესრიგებული ტრეისი და ის სიმპტომი, რომელსაც მომხმარებელი დაინახავდა.
   დაწერე, ემთხვევა თუ არა ის <symptom>-ს. თუ არ ემთხვევა, ეს პირდაპირ თქვი და ტრეისი მის
   მოსარგებად არ გადააკეთო.
3. რატომ არის აშკარა წაკითხვა მცდარი — ერთი check-then-act, read-modify-write ან ორმაგი შემოწმების
   პატერნი ამ კოდში, რომელიც უსაფრთხოდ გამოიყურება და არ არის.
4. გამრჩევი ტესტი — როგორ ავაფეთქოთ race მოთხოვნისამებრ: დასახელებულ ხაზზე ჩამატებული sleep,
   დატვირთვის ციკლი N worker-ით, `go test -race`, thread sanitiser ან იძულებითი ორრეპლიკიანი გაშვება.
   დაწერე, რას დაამტკიცებდა და რას ვერ დაამტკიცებდა წარმატებული გაშვება.

არცერთი ფაილი არ შეასწორო. მხოლოდ ანალიზი.
არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
```

---

### DB-06 · Memory leak investigation
`claude` `gpt` `claude-code` — memory, profiling

**EN**
```
Find what is retaining memory. Do not tune the garbage collector.

<evidence>
RSS over time: {{rss_series}}
Heap snapshot diff between {{t1}} and {{t2}}: {{snapshot_diff}}
Process and runtime: {{process}}
Restart interval that currently keeps it alive: {{restart_interval}}
What changed before it started: {{change}}
</evidence>

Base every claim on the supplied snapshots and numbers. If the diff does not show what holds a
reference, say so and name the capture that would show it. NEVER quote a size or a count that is
not printed in the evidence.

Answer in this order:

1. GROWING OR FRAGMENTED — is total live-object size growing, or is RSS growing while live size
   stays flat? Quote the two numbers that decide it. These are different bugs, and the second one
   is allocator fragmentation, not a leak. If the evidence cannot separate them, say so.

2. THE TOP 3 RETAINED SETS — object type, count delta, retained size delta, taken from the diff.

3. WHO HOLDS THE REFERENCE — for each set, the retainer chain as it appears in the snapshot.
   Where the chain is truncated in the evidence, write `RETAINER UNKNOWN` and name the capture
   that would complete it.

4. THE USUAL SUSPECTS, CHECKED AGAINST THE EVIDENCE — a module-level cache with no eviction ·
   a listener added per request and never removed · a closure capturing a large scope · an unbounded
   queue or buffer · connections or file handles never closed · an accumulating log or metrics buffer.
   For each: does the evidence support it, contradict it, or say nothing at all?

5. THE CONFIRMING CAPTURE — the exact command (`node --heapsnapshot-signal=SIGUSR2`,
   `jmap -histo:live <pid>`, `py-spy dump --pid <pid>`, `go tool pprof /debug/pprof/heap`) and what
   the next snapshot must show for the top hypothesis to survive.

NEVER propose a fix until you have named the cause and the evidence for it.
```

**KA**
```
იპოვე, რა იკავებს მეხსიერებას. ნაგვის შემგროვებლის კონფიგურაციას ნუ შეეხები.

<evidence>
RSS დროში: {{rss_დინამიკა}}
heap-სნეპშოტების სხვაობა {{t1}}-სა და {{t2}}-ს შორის: {{სნეპშოტის_სხვაობა}}
პროცესი და გარემო: {{პროცესი}}
გადატვირთვის ინტერვალი, რომელიც ამჟამად აცოცხლებს: {{გადატვირთვა}}
რა შეიცვალა დაწყებამდე: {{ცვლილება}}
</evidence>

ყოველი მტკიცება მოცემულ სნეპშოტებსა და ციფრებს დააფუძნე. თუ სხვაობა არ აჩვენებს, ვინ იკავებს
მიმართვას, ეს დაწერე და დაასახელე ჩაჭერა, რომელიც ამას აჩვენებდა. არასდროს დაასახელო ზომა ან
რაოდენობა, რომელიც მტკიცებულებაში არ წერია.

უპასუხე ამ თანმიმდევრობით:

1. იზრდება თუ ფრაგმენტირდება — იზრდება ცოცხალი ობიექტების ჯამური ზომა, თუ RSS იზრდება მაშინ,
   როცა ცოცხალი ზომა უცვლელია? დაასახელე ორი ციფრი, რომელიც ამას წყვეტს. ეს ორი სხვადასხვა ბაგია
   და მეორე ალოკატორის ფრაგმენტაციაა და არა გაჟონვა. თუ მტკიცებულება მათ ვერ არჩევს, ეს დაწერე.

2. სამი ყველაზე მძიმე შენარჩუნებული ნაკრები — ობიექტის ტიპი, რაოდენობის სხვაობა და შენარჩუნებული
   ზომის სხვაობა, სნეპშოტების სხვაობიდან აღებული.

3. ვინ იკავებს მიმართვას — თითოეულ ნაკრებზე მიმკავებელთა ჯაჭვი ისე, როგორც სნეპშოტში ჩანს.
   სადაც ჯაჭვი მტკიცებულებაში წყდება, დაწერე `RETAINER UNKNOWN` და დაასახელე ჩაჭერა, რომელიც
   მას შეავსებდა.

4. ჩვეული ეჭვმიტანილები, მტკიცებულებასთან შედარებული — მოდულის დონის ქეში გაწმენდის გარეშე ·
   ყოველ მოთხოვნაზე დამატებული listener, რომელიც არასდროს იშლება · closure, რომელიც დიდ სფეროს
   იჭერს · უსაზღვრო რიგი ან ბუფერი · დაუხურავი კავშირები ან ფაილის დესკრიპტორები · დაგროვებადი
   ლოგის ან მეტრიკების ბუფერი.
   თითოეულზე: ადასტურებს მას მტკიცებულება, ეწინააღმდეგება თუ საერთოდ არაფერს ამბობს?

5. დამადასტურებელი ჩაჭერა — ზუსტი ბრძანება (`node --heapsnapshot-signal=SIGUSR2`,
   `jmap -histo:live <pid>`, `py-spy dump --pid <pid>`, `go tool pprof /debug/pprof/heap`) და რა
   უნდა აჩვენოს შემდეგმა სნეპშოტმა, რომ მთავარი ვარაუდი გადარჩეს.

არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
```

---

### DB-07 · Read a performance profile
`claude` `gpt` `gemini` — performance, profiling

**EN**
```
Read this profile and tell me where the time actually goes. Optimise nothing.

<profile>
{{profiler_output}}
</profile>

<context>
Profiler and mode: {{profiler}}   (sampling or instrumenting; wall clock or CPU)
What was running during the capture: {{workload}}
Duration and sample count: {{duration}}
The number I am trying to move: {{target}}
</context>

Base every number on the supplied profile. NEVER quote a figure you did not read there, and NEVER
convert a percentage into milliseconds unless the total duration is given.

Answer in this order:

1. SELF VERSUS TOTAL — the top 5 by self time and the top 5 by total time, as two separate lists.
   Then name the frames that are high in total and near zero in self: those are callers, not costs,
   and optimising them is optimising nothing.

2. CPU OR WAITING — does this profile measure wall clock or CPU? If wall clock, name the frames
   that are blocked on I/O, a lock or a network call rather than computing. If the mode is not
   stated in <context>, say that the answer depends on it and stop there rather than assuming.

3. THE SAMPLING FLOOR — the frames whose sample counts are low enough to be noise. State the count
   you treat as the floor and why, given {{duration}}.

4. THE ONE PLACE TO LOOK — the single frame that, if it cost zero, would move {{target}} the most.
   Show the arithmetic, and state the ceiling: even at zero, {{target}} cannot go below X.

5. WHAT THIS PROFILE DOES NOT COVER — startup, GC pauses, another process, time before the first
   sample, anything running off this thread.

NEVER propose a fix until you have named the cause and the evidence for it.
```

**KA**
```
წაიკითხე ეს პროფაილი და მითხარი, სად მიდის დრო სინამდვილეში. არაფერი დააოპტიმიზირო.

<profile>
{{პროფაილერის_გამოსავალი}}
</profile>

<context>
პროფაილერი და რეჟიმი: {{პროფაილერი}}   (სემპლირება თუ ინსტრუმენტირება; რეალური დრო თუ CPU)
რა იყო გაშვებული ჩაწერისას: {{დატვირთვა}}
ხანგრძლივობა და სემპლების რაოდენობა: {{ხანგრძლივობა}}
ციფრი, რომლის შემცირებაც მინდა: {{სამიზნე}}
</context>

ყოველი ციფრი მოცემულ პროფაილს დააფუძნე. არასდროს დაასახელო მაჩვენებელი, რომელიც იქ არ წაგიკითხავს,
და არასდროს გადაიყვანო პროცენტი მილიწამებში, თუ ჯამური ხანგრძლივობა მოცემული არ არის.

უპასუხე ამ თანმიმდევრობით:

1. საკუთარი დრო და ჯამური დრო — საუკეთესო 5 საკუთარი დროით და საუკეთესო 5 ჯამური დროით, ორ ცალკე
   სიად. შემდეგ დაასახელე ფრეიმები, რომლებსაც ჯამური დრო დიდი აქვთ და საკუთარი — ნულთან ახლოს:
   ესენი გამომძახებლები არიან და არა ხარჯი, და მათი ოპტიმიზაცია არაფრის ოპტიმიზაციაა.

2. CPU თუ ლოდინი — ეს პროფაილი რეალურ დროს ზომავს თუ CPU-ს? თუ რეალურ დროს, დაასახელე ფრეიმები,
   რომლებიც I/O-ზე, ბოქლომზე ან ქსელის გამოძახებაზე დგანან და არა თვლიან. თუ რეჟიმი <context>-ში
   მითითებული არ არის, დაწერე, რომ პასუხი სწორედ ამაზეა დამოკიდებული, და აქვე შეჩერდი — ნუ ივარაუდებ.

3. სემპლირების ზღვარი — ფრეიმები, რომელთა სემპლების რაოდენობაც უკვე ხმაურია. დაასახელე, რომელ
   რაოდენობას თვლი ზღვრად და რატომ, {{ხანგრძლივობა}}-ის გათვალისწინებით.

4. ერთი ადგილი, სადაც უნდა ვიყურო — ერთი ფრეიმი, რომელიც ნულოვანი ხარჯის შემთხვევაში {{სამიზნე}}-ს
   ყველაზე მეტად დასწევდა. აჩვენე არითმეტიკა და დაასახელე ჭერი: ნულზეც კი {{სამიზნე}} X-ზე ქვემოთ
   ვერ ჩამოვა.

5. რას არ ფარავს ეს პროფაილი — გაშვების ეტაპს, GC-ის პაუზებს, სხვა პროცესს, პირველ სემპლამდე
   გასულ დროს და ყველაფერს, რაც ამ thread-ის გარეთ მუშაობს.

არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
```

---

### DB-08 · Works locally, fails in production
`claude` `gpt` `claude-code` — environment, production

**EN**
```
It works on my machine and fails in production. Enumerate the differences. Do not guess at a fix.

<symptom>
Local: {{local_result}}
Production: {{prod_result}}
They diverge here: {{difference}}
Started: {{started}}
</symptom>

<what_i_know>
Local: {{local_env}}
Production: {{prod_env}}
</what_i_know>

Walk this list. For each item give the local value, the production value, and `UNKNOWN` where I did
not give you one. NEVER fill an unknown with a typical or default value — an invented delta is worse
than a missing one.

· runtime version down to the patch level, and build flags
· the lockfile actually installed, and whether dev dependencies are present
· environment variables, including ones set to an empty string rather than unset
· timezone, locale, and system clock skew
· filesystem case sensitivity, path separators, and file permissions
· available memory and CPU count, and any worker or pool size derived from it
· network egress: DNS resolution, proxy, TLS trust store, outbound firewall rules
· database version, pool size, isolation level, and whether the data is a sanitised dump or live
· reverse proxy or load balancer in front: body size limit, read timeout, header rewriting, buffering
· instance count — one process locally, N in production, so anything per-process is now per-instance
· read-only filesystem, container user id, ephemeral storage, missing system packages
· build step: minification, tree shaking, NODE_ENV / DEBUG flags, stripped source maps

Output:
1. DELTA TABLE — item · local · production · could this produce <symptom>? yes / no / unknown
2. THE THREE DELTAS THAT COULD PRODUCE THIS SYMPTOM, RANKED — each with the cheapest check,
   preferring a check that runs against production and changes nothing: an env dump, a version
   endpoint, one added log line.
3. WHAT MUST BE MEASURED IN PRODUCTION before anyone edits code.

Base every claim on the supplied environment data. If the evidence does not distinguish between two
deltas, say so and name the check that would.
Do not edit any files. Analysis only.
```

**KA**
```
ლოკალურად მუშაობს, პროდაქშენში კი ვარდება. ჩამოწერე განსხვავებები. გამოსწორება არ გამოიცნო.

<symptom>
ლოკალურად: {{ლოკალური_შედეგი}}
პროდაქშენში: {{პროდაქშენის_შედეგი}}
სად იშლება გზა: {{განსხვავება}}
როდის დაიწყო: {{დაწყება}}
</symptom>

<what_i_know>
ლოკალური: {{ლოკალური_გარემო}}
პროდაქშენი: {{პროდაქშენის_გარემო}}
</what_i_know>

გაიარე ეს სია. ყოველ პუნქტზე დაწერე ლოკალური მნიშვნელობა, პროდაქშენის მნიშვნელობა და `UNKNOWN` იქ,
სადაც ეს არ მოგეცი. არასდროს შეავსო უცნობი ტიპური ან ნაგულისხმევი მნიშვნელობით — გამოგონილი
სხვაობა უარესია, ვიდრე გამოტოვებული.

· გარემოს ვერსია პატჩის დონემდე და აგების ფლაგები
· რეალურად დაინსტალირებული lockfile და არის თუ არა სადეველოპმენტო დამოკიდებულებები
· გარემოს ცვლადები, მათ შორის ის, რომლებიც ცარიელ სტრიქონზეა დაყენებული და არა გამორთული
· დროის სარტყელი, ლოკალი და სისტემური საათის აცდენა
· ფაილური სისტემის რეგისტრზე მგრძნობელობა, გზის გამყოფები და ფაილების უფლებები
· ხელმისაწვდომი მეხსიერება და CPU-ების რაოდენობა და ყველაფერი, რაც მათგან გამომდინარეობს (worker-ები, პულები)
· ქსელი გარეთ: DNS, პროქსი, TLS-სერტიფიკატების საცავი, გამავალი ფაიერვოლის წესები
· ბაზის ვერსია, პულის ზომა, იზოლაციის დონე და მონაცემები გაწმენდილი დამპია თუ ცოცხალი
· წინ მდგარი reverse proxy ან ბალანსერი: სხეულის ზომის ლიმიტი, ტაიმაუტი, ჰედერების გადაწერა, ბუფერიზაცია
· ინსტანსების რაოდენობა — ლოკალურად ერთი პროცესი, პროდაქშენში N, ანუ ყველაფერი, რაც პროცესზე იყო, ახლა ინსტანსზეა
· მხოლოდ წასაკითხი ფაილური სისტემა, კონტეინერის მომხმარებლის id, დროებითი საცავი, დაკლებული სისტემური პაკეტები
· აგების ეტაპი: მინიფიკაცია, tree shaking, NODE_ENV / DEBUG, ამოჭრილი source map-ები

გამოსავალი:
1. სხვაობების ცხრილი — პუნქტი · ლოკალური · პროდაქშენი · შეუძლია თუ არა ამან <symptom> გამოიწვიოს?
   კი / არა / უცნობია
2. სამი სხვაობა, რომელსაც ეს სიმპტომი შეუძლია გამოიწვიოს, რანჟირებული — თითოეულთან ყველაზე იაფი
   შემოწმება; უპირატესობა მიეცი იმას, რაც პროდაქშენზე გაეშვება და არაფერს ცვლის: გარემოს ცვლადების
   ამობეჭდვა, ვერსიის ენდპოინტი, ერთი დამატებული ლოგის ხაზი.
3. რა უნდა გაიზომოს პროდაქშენში, სანამ ვინმე კოდს შეეხება.

ყოველი მტკიცება მოცემულ მონაცემებს დააფუძნე. თუ მტკიცებულება ორ სხვაობას ერთმანეთისგან ვერ არჩევს,
ეს დაწერე და დაასახელე შემოწმება, რომელიც გაარჩევდა.
არცერთი ფაილი არ შეასწორო. მხოლოდ ანალიზი.
```

---

### DB-09 · What I already ruled out
`claude` `gpt` `gemini` — method, hypothesis

**EN**
```
I have been on this bug for hours. Here is what is already dead. Do not send me back through it.

<bug>
{{symptom}}
</bug>

<already_ruled_out>
Tried: {{attempt_1}} → result: {{result_1}} → I concluded: {{ruled_out_1}}
Tried: {{attempt_2}} → result: {{result_2}} → I concluded: {{ruled_out_2}}
Tried: {{attempt_3}} → result: {{result_3}} → I concluded: {{ruled_out_3}}
</already_ruled_out>

Rules:
- NEVER propose anything in <already_ruled_out>, and never a reworded version of it.
- Before proposing anything, restate in one line what each attempt actually eliminated. Where I
  claimed more than the result supports, say so — an attempt that was run wrong, or on the wrong
  build, eliminates nothing, and telling me that is more useful than a new hypothesis.
- Base every claim on the supplied results. If the evidence does not distinguish between two
  surviving causes, say so and name the check that would.

Output:
1. WHAT IS ACTUALLY ELIMINATED — one line per attempt. Mark every conclusion of mine you disagree
   with and say why.
2. WHAT IS STILL ALIVE — the hypotheses that survive all of the above, ranked, each with the
   evidence that keeps it alive.
3. THE NEXT CHECK — exactly one, chosen because it splits the surviving hypotheses roughly in half,
   NOT because it tests the most likely one. Say which hypotheses a positive result kills and which
   a negative result kills.
4. THE UNTESTED ASSUMPTION — the thing everyone, me included, has treated as given: that the build
   under test is the build deployed, that the log line comes from the code I am reading, that the
   input is what I think it is.

NEVER propose a fix until you have named the cause and the evidence for it.
```

**KA**
```
ამ ბაგზე უკვე საათებია ვზივარ. ქვემოთ წერია, რა არის უკვე მკვდარი. იმავე წრეზე ნუ დამაბრუნებ.

<bug>
{{სიმპტომი}}
</bug>

<already_ruled_out>
ვცადე: {{მცდელობა_1}} → შედეგი: {{შედეგი_1}} → დავასკვენი: {{გამოირიცხა_1}}
ვცადე: {{მცდელობა_2}} → შედეგი: {{შედეგი_2}} → დავასკვენი: {{გამოირიცხა_2}}
ვცადე: {{მცდელობა_3}} → შედეგი: {{შედეგი_3}} → დავასკვენი: {{გამოირიცხა_3}}
</already_ruled_out>

წესები:
- არასდროს შემომთავაზო ის, რაც <already_ruled_out>-შია, და არც მისი სხვა სიტყვებით გადათქმული ვარიანტი.
- სანამ რამეს შემომთავაზებ, თითო ხაზში გადმომიწერე, რა გამორიცხა თითოეულმა მცდელობამ სინამდვილეში.
  სადაც მე შედეგზე მეტი დავასკვენი, ეს დაწერე — მცდელობა, რომელიც არასწორად ან არასწორ ბილდზე
  გაეშვა, არაფერს გამორიცხავს, და ამის თქმა ჩემთვის ახალ ჰიპოთეზაზე სასარგებლოა.
- ყოველი მტკიცება მოცემულ შედეგებს დააფუძნე. თუ მტკიცებულება ორ გადარჩენილ მიზეზს ერთმანეთისგან
  ვერ არჩევს, ეს დაწერე და დაასახელე შემოწმება, რომელიც გაარჩევდა.

გამოსავალი:
1. რა გამოირიცხა სინამდვილეში — თითო მცდელობაზე ერთი ხაზი. მონიშნე ჩემი ყოველი დასკვნა, რომელსაც
   არ ეთანხმები, და ახსენი, რატომ.
2. რა რჩება ცოცხალი — ჰიპოთეზები, რომლებმაც ყველაფერი ზემოთქმული გადაიტანეს, რანჟირებული და
   თითოეულთან მტკიცებულება, რომელიც მას აცოცხლებს.
3. შემდეგი შემოწმება — ზუსტად ერთი, არჩეული იმიტომ, რომ გადარჩენილ ჰიპოთეზას დაახლოებით შუაზე
   ყოფს და არა იმიტომ, რომ ყველაზე სავარაუდოს ამოწმებს. დაწერე, რომელ ჰიპოთეზას კლავს დადებითი
   პასუხი და რომელს — უარყოფითი.
4. დაუმოწმებელი დაშვება — ის, რაც ყველამ, ჩემი ჩათვლით, თავისთავად მივიღეთ: რომ დატესტილი ბილდი
   იგივეა, რაც გაშლილი; რომ ლოგის ხაზი სწორედ იმ კოდიდან მოდის, რომელსაც ვკითხულობ; რომ შემავალი
   მონაცემი ისაა, რაც მგონია.

არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
```

---

### DB-10 · Interpret a query plan
`claude` `gpt` `claude-code` — database, query-plan

**EN**
```
Read this query plan and tell me what the database is actually doing. Do not add an index yet.

<query>
{{sql}}
</query>

<plan>
{{explain_analyze_output}}
</plan>

<context>
Engine and version: {{engine}}
Row counts of the tables involved: {{table_sizes}}
Existing indexes on them: {{indexes}}
This query runs: {{frequency}}   (per request / per page load / nightly batch)
</context>

Base every claim on the supplied plan. NEVER state a cost, a time or a row count that is not printed
there, and NEVER claim an index exists unless the plan or <context> names it.

Answer in this order:

1. THE MOST EXPENSIVE NODE — the node with the highest actual total time, its loop count, and its
   actual time per loop. Read `actual time` and `rows`, not `cost`; cost is the planner's guess and
   this plan has real numbers in it.

2. ESTIMATE VERSUS ACTUAL — every node where estimated rows and actual rows differ by more than 10×.
   That is the planner being misled. Name what would mislead it here: stale statistics, correlated
   predicates, a function wrapping an indexed column, a type mismatch forcing a cast, a generic
   plan built for a prepared statement.

3. THE ACCESS PATTERN — for each scan: sequential or index, and whether a sequential scan is
   actually wrong here given {{table_sizes}}. On a 400-row table it is not wrong, and swapping it
   for an index scan would change nothing.

4. JOIN ORDER AND METHOD — nested loop, hash or merge, and whether the actual row counts justify
   the choice. A nested loop over 400k rows is the classic misestimate.

5. WHAT IS NOT IN THE PLAN — was it captured with `BUFFERS`? cold or warm cache? run with real
   parameter values or a generic prepared plan? Was `ANALYZE` actually used, or is this `EXPLAIN`
   alone with no measured times?

Only after all five: name the single change most likely to help, as a proposal, with the plan shape
you expect afterwards and the number that would show it worked.
NEVER propose a fix until you have named the cause and the evidence for it.
Do not run a migration and do not create an index.
```

**KA**
```
წაიკითხე მოთხოვნის ეს გეგმა და მითხარი, რას აკეთებს ბაზა სინამდვილეში. ინდექსს ჯერ ნუ დაამატებ.

<query>
{{sql}}
</query>

<plan>
{{explain_analyze_გამოსავალი}}
</plan>

<context>
ძრავა და ვერსია: {{ძრავა}}
ჩართული ცხრილების სტრიქონების რაოდენობა: {{ცხრილების_ზომა}}
არსებული ინდექსები: {{ინდექსები}}
ეს მოთხოვნა გაშვებულია: {{სიხშირე}}   (ყოველ მოთხოვნაზე / ყოველ გვერდზე / ღამის ბატჩში)
</context>

ყოველი მტკიცება მოცემულ გეგმას დააფუძნე. არასდროს დაასახელო ღირებულება, დრო ან სტრიქონების
რაოდენობა, რომელიც იქ არ წერია, და არასდროს თქვა, რომ ინდექსი არსებობს, თუ მას გეგმა ან <context>
არ ასახელებს.

უპასუხე ამ თანმიმდევრობით:

1. ყველაზე ძვირი კვანძი — კვანძი, რომელსაც ყველაზე დიდი `actual total time` აქვს, მისი ციკლების
   რაოდენობა და რეალური დრო ერთ ციკლზე. კითხულობ `actual time`-სა და `rows`-ს და არა `cost`-ს:
   `cost` დამგეგმავის ვარაუდია, ამ გეგმაში კი რეალური ციფრებია.

2. ვარაუდი და რეალობა — ყოველი კვანძი, სადაც ნავარაუდევი და რეალური სტრიქონები 10-ჯერ და მეტად
   განსხვავდება. სწორედ აქ არის დამგეგმავი შეცდომაში შეყვანილი. დაასახელე, რა შეჰყავს შეცდომაში:
   მოძველებული სტატისტიკა, ერთმანეთთან დაკავშირებული პირობები, ფუნქცია, რომელიც ინდექსირებულ
   სვეტს ახვევია, ტიპების შეუსაბამობა, რომელიც cast-ს იწვევს, ან prepared statement-ისთვის აგებული
   ზოგადი გეგმა.

3. წვდომის პატერნი — ყოველ სკანზე: თანმიმდევრული თუ ინდექსური, და მართლა არასწორია თუ არა
   თანმიმდევრული სკანი {{ცხრილების_ზომა}}-ის გათვალისწინებით. 400-სტრიქონიან ცხრილზე ის არასწორი
   არ არის და ინდექსურით ჩანაცვლება არაფერს შეცვლიდა.

4. join-ის თანმიმდევრობა და მეთოდი — nested loop, hash თუ merge, და ამართლებს თუ არა რეალური
   სტრიქონების რაოდენობა ამ არჩევანს. nested loop 400 ათას სტრიქონზე კლასიკური არასწორი ვარაუდია.

5. რა არ წერია გეგმაში — იყო თუ არა ის `BUFFERS`-ით აღებული? ქეში ცივია თუ თბილი? გაეშვა რეალური
   პარამეტრებით თუ ზოგადი prepared-გეგმით? `ANALYZE` მართლა გამოიყენე, თუ ეს მხოლოდ `EXPLAIN`-ია
   და გაზომილი დრო საერთოდ არ არის?

მხოლოდ ხუთივეს შემდეგ: დაასახელე ერთი ცვლილება, რომელიც ყველაზე მეტად უშველიდა — წინადადების
სახით, იმ გეგმის ფორმასთან ერთად, რომელსაც ელოდები, და იმ ციფრთან ერთად, რომელიც აჩვენებდა, რომ გამოვიდა.
არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
მიგრაცია არ გაუშვა და ინდექსი არ შექმნა.
```

---

### DB-11 · Debug a failing CI pipeline from its log
`claude-code` `gpt` `cursor` — ci, logs

**EN**
```
Find out why CI failed. The log is the only evidence. Do not push a speculative fix.

<ci_log>
{{ci_log}}
</ci_log>

<context>
Pipeline and job: {{pipeline}}
Last green run: {{last_green}}
Changes since then: {{changes}}
Does it fail on a re-run of the same commit: {{rerun_result}}
Does it fail on another branch: {{other_branch}}
</context>

Base every claim on the supplied log, and quote the line or the timestamp for each one. NEVER infer
a step the log does not show running, and NEVER assume a command succeeded because the log does not
show it failing.

Answer in this order:

1. THE FIRST REAL ERROR — the earliest line that is a cause rather than a consequence. Later steps
   fail because an earlier one did; find where the cascade starts and quote that line.

2. WHICH LAYER — our code · our test · our pipeline configuration · a dependency resolved at build
   time · the runner image and its preinstalled tools · an external service. Quote the line that
   places it in that layer.

3. COMMIT OR RUNNER — does the log show this failing for a reason that lives in the commit, or for
   a reason that lives only in the runner? `{{rerun_result}}` is the main evidence here; if I did
   not give it to you, say so and name it as the first thing to obtain.

4. THREE CAUSES, RANKED — each with the cheapest check, preferring one that runs locally (the same
   container image, `act`, or the exact command from the log with the exact flags) over one that
   needs another CI run. Say what each check would rule out.

5. WHAT THE LOG HID — truncated output, a swallowed exit code, a step that printed nothing, a
   `continue-on-error`, a `set -e` that is missing, or a secret masked as `***` that may be empty
   rather than set.

NEVER propose a fix until you have named the cause and the evidence for it.
Do not edit any workflow file to make the job pass.
```

**KA**
```
გაარკვიე, რატომ ჩავარდა CI. ერთადერთი მტკიცებულება ლოგია. სავარაუდო შესწორება არ ატვირთო.

<ci_log>
{{ლოგი}}
</ci_log>

<context>
პაიფლაინი და job: {{პაიფლაინი}}
ბოლო მწვანე გაშვება: {{ბოლო_მწვანე}}
მას შემდეგ შესული ცვლილებები: {{ცვლილებები}}
ვარდება თუ არა იმავე კომიტის ხელახლა გაშვებისას: {{ხელახალი_გაშვება}}
ვარდება თუ არა სხვა ბრანჩზე: {{სხვა_ბრანჩი}}
</context>

ყოველი მტკიცება მოცემულ ლოგს დააფუძნე და თითოეულს მიაწერე ხაზი ან დროის ნიშნული. არასდროს
იგულისხმო ეტაპი, რომლის გაშვებაც ლოგში არ ჩანს, და არასდროს ჩათვალო ბრძანება წარმატებულად მხოლოდ
იმიტომ, რომ ლოგი მის ჩავარდნას არ აჩვენებს.

უპასუხე ამ თანმიმდევრობით:

1. პირველი ნამდვილი შეცდომა — ყველაზე ადრეული ხაზი, რომელიც მიზეზია და არა შედეგი. მომდევნო
   ეტაპები იმიტომ ვარდება, რომ წინა ჩავარდა; იპოვე, სად იწყება ეს ჯაჭვი, და ეს ხაზი ციტირებულად მოიყვანე.

2. რომელი ფენა — ჩვენი კოდი · ჩვენი ტესტი · პაიფლაინის კონფიგურაცია · აგებისას გადმოწეული
   დამოკიდებულება · runner-ის იმიჯი და მასში წინასწარ დაყენებული ინსტრუმენტები · გარე სერვისი.
   მოიყვანე ხაზი, რომელიც მას ამ ფენაში აქცევს.

3. კომიტი თუ runner — ლოგი აჩვენებს, რომ ჩავარდნის მიზეზი კომიტშია, თუ მიზეზი მხოლოდ runner-ში
   ცხოვრობს? მთავარი მტკიცებულება აქ `{{ხელახალი_გაშვება}}`-ა; თუ ის არ მოგეცი, ეს დაწერე და
   დაასახელე როგორც პირველი მოსაპოვებელი მონაცემი.

4. სამი მიზეზი, რანჟირებული — თითოეულთან ყველაზე იაფი შემოწმება; უპირატესობა მიეცი იმას, რაც
   ლოკალურად გაეშვება (იგივე კონტეინერის იმიჯი, `act` ან ლოგიდან აღებული ზუსტი ბრძანება ზუსტივე
   ფლაგებით) და არა იმას, რასაც CI-ის ახალი გაშვება სჭირდება. დაწერე, რას გამორიცხავდა თითოეული.

5. რა დამალა ლოგმა — მოჭრილი გამოსავალი, ჩაყლაპული exit-კოდი, ეტაპი, რომელმაც არაფერი დაბეჭდა,
   `continue-on-error`, დაკარგული `set -e` ან საიდუმლო, რომელიც `***`-ად ჩანს და შესაძლოა საერთოდ
   ცარიელი იყოს და არა დაყენებული.

არასდროს შემომთავაზო გამოსწორება, სანამ მიზეზს და მის მტკიცებულებას არ დაასახელებ.
workflow-ის ფაილი job-ის გასატარებლად არ შეასწორო.
```
