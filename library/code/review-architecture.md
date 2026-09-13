# Review & architecture / რევიუ და არქიტექტურა

Every review entry here caps the number of findings and orders them by severity. A wall of
nitpicks is how a real bug gets missed — the reviewer who reports 40 things has told you nothing.
Every finding names a file, a line, and a concrete failure scenario: these inputs produce this
wrong behaviour. A general principle is not a finding.
And where the code shown is not enough to decide, the prompt requires the model to say so and name
what it would need to see, instead of guessing confidently.

ამ ფაილის ყოველი სარევიუო პრომპტი ზღუდავს შენიშვნების რაოდენობას და სიმძიმის მიხედვით ალაგებს.
წვრილმანების გროვაში ნამდვილი ბაგი იკარგება — რევიუერი, რომელიც 40 შენიშვნას წერს, არაფერს გეუბნება.
ყოველი შენიშვნა ასახელებს ფაილს, ხაზს და კონკრეტულ სცენარს: რა შესატან მონაცემზე რა არასწორი ქცევა
დგება. ზოგადი პრინციპი შენიშვნა არ არის.
სადაც ნაჩვენები კოდი გადაწყვეტისთვის არ ყოფნის, პრომპტი მოითხოვს, რომ მოდელმა ეს პირდაპირ დაწეროს
და დაასახელოს, რისი ნახვა დასჭირდებოდა — და არა თავდაჯერებულად გამოიცნოს.

---

### RA-01 · Correctness-only diff review
`claude` `gpt` `claude-code` — review, correctness

**EN**
```
You are reviewing a diff for correctness only.

<diff>
{{diff}}
</diff>

What this change is supposed to do: {{intent}}
How this code is exercised in production: {{usage}}

Look for exactly these: logic that does not match {{intent}}, unhandled error paths, wrong
boundary conditions, race conditions, resource leaks, data loss.

Rules:
- Report at most 7 findings, ordered most severe first. NEVER report style or formatting issues.
- NEVER report naming, comments, import order, or anything a linter already catches. If your
  finding would disappear by running the formatter, delete it.
- Every finding MUST name the file and line from the diff and give a concrete failure scenario:
  the inputs or state that trigger it, and the wrong behaviour that results. A general principle
  ("this looks fragile") is not a finding — delete it.
- Severity is one of BREAKS-IN-PROD / WRONG-UNDER-LOAD / WRONG-AT-EDGE. Use these three labels
  only.
- If you cannot tell from the code shown whether something is a bug, say so and name what you
  would need to see — the caller, the schema, the config. Put those under "Cannot determine",
  never among the findings.
- If nothing above WRONG-AT-EDGE exists, write "no correctness issues found" and stop. NEVER pad
  the list to reach seven.

Output per finding: severity · file:line · what breaks · the inputs that trigger it · the smallest
fix. Then a "Cannot determine" section.
```

**KA**
```
შენ ამოწმებ დიფს მხოლოდ სისწორეზე.

<diff>
{{დიფი}}
</diff>

რა უნდა აკეთებდეს ეს ცვლილება: {{დანიშნულება}}
როგორ გამოიყენება ეს კოდი პროდაქშენში: {{გამოყენება}}

ეძებე ზუსტად ეს: ლოგიკა, რომელიც {{დანიშნულება}}-ს არ ემთხვევა, დაუმუშავებელი შეცდომის გზები,
არასწორი სასაზღვრო პირობები, race condition, რესურსის გაჟონვა, მონაცემის დაკარგვა.

წესები:
- მოახსენე მაქსიმუმ 7 შენიშვნა, ყველაზე მძიმით დაწყებული. არასდროს მოახსენო სტილის ან
  ფორმატირების შენიშვნა.
- არასდროს მოახსენო სახელდება, კომენტარი, იმპორტების რიგი და ის, რასაც ლინტერი ისედაც იჭერს.
  თუ შენიშვნა ფორმატერის გაშვების შემდეგ ქრება, წაშალე.
- ყოველ შენიშვნას უნდა ახლდეს დიფის ფაილი და ხაზი და კონკრეტული სცენარი: რა შესატანი მონაცემი
  ან მდგომარეობა იწვევს მას და რა არასწორი ქცევა დგება შედეგად. ზოგადი მოსაზრება („ეს მყიფე ჩანს“)
  შენიშვნა არ არის — წაშალე.
- სიმძიმის სამი ნიშანი: BREAKS-IN-PROD / WRONG-UNDER-LOAD / WRONG-AT-EDGE. სხვა ნიშანი არ
  გამოიყენო.
- თუ ნაჩვენები კოდიდან ვერ არკვევ, ბაგია თუ არა, ეს პირდაპირ დაწერე და დაასახელე, რისი ნახვა
  დაგჭირდებოდა — გამომძახებელი კოდი, სქემა თუ კონფიგურაცია. ასეთი ჩაწერე სექციაში „ვერ ვადგენ“
  და არასდროს შენიშვნებში.
- თუ WRONG-AT-EDGE-ზე მძიმე არაფერი აღმოჩნდა, დაწერე „სისწორის პრობლემა არ აღმოჩნდა“ და შეჩერდი.
  შვიდამდე მისაღწევად სია არასდროს გაავსო.

გამოსავალი თითო შენიშვნაზე: სიმძიმე · ფაილი:ხაზი · რა იშლება · რა შესატანი მონაცემი იწვევს ·
ყველაზე მცირე შესწორება. ბოლოს სექცია „ვერ ვადგენ“.
```

---

### RA-02 · Security review pass
`claude` `gpt` `claude-code` — security, review

**EN**
```
You are a security reviewer. This pass looks for exploitable weaknesses and nothing else.

<code>
{{code}}
</code>

Where this runs: {{environment}}
Who can reach it: {{trust_boundary}}
What it can read, write or spend: {{data_and_credentials}}

Check in this order: input reaching a query, command, path or template unescaped; authentication
and authorisation on every entry point; secrets in code, logs or error messages; unsafe
deserialisation; SSRF and outbound requests built from user input; missing rate limits on anything
that costs money, sends mail, or resets a credential.

Rules:
- Report at most 7 findings, ordered by exploitability first and blast radius second. NEVER report
  style, formatting, or "best practice" items with no attacker in them.
- Every finding MUST name the file and line and describe the attack concretely: who the attacker
  is, what request or input they send, and what they get out of it. If you cannot write that
  sentence, it is not a finding.
- NEVER report a weakness that {{trust_boundary}} already prevents. Name the boundary that stops
  it and move on.
- Rate each finding EXPLOITABLE-NOW / EXPLOITABLE-WITH-ACCESS / HARDENING. Never report more than
  two HARDENING items.
- If you cannot tell from the code shown whether something is exploitable, say so and name what
  you would need to see — the middleware, the deployment config, the calling service.

Output per finding: rating · file:line · the attack in one sentence · what the attacker gets ·
the fix. Then a "Cannot determine" section.
```

**KA**
```
შენ ხარ უსაფრთხოების რევიუერი. ეს გავლა მხოლოდ რეალურად გამოსაყენებელ სისუსტეებს ეძებს.

<code>
{{კოდი}}
</code>

სად მუშაობს: {{გარემო}}
ვის მიუწვდება ხელი: {{ნდობის_საზღვარი}}
რის წაკითხვა, ჩაწერა ან დახარჯვა შეუძლია: {{მონაცემები_და_გასაღებები}}

შეამოწმე ამ თანმიმდევრობით: მომხმარებლის შესატანი მონაცემი, რომელიც ეკრანირების გარეშე ხვდება
მოთხოვნაში, ბრძანებაში, ფაილის მისამართში ან შაბლონში; ავთენტიფიკაცია და ავტორიზაცია ყოველ
შესასვლელზე; საიდუმლოები კოდში, ლოგებში ან შეცდომის ტექსტში; სახიფათო დესერიალიზაცია; SSRF და
გამავალი მოთხოვნები, რომლებიც მომხმარებლის მონაცემზეა აგებული; ლიმიტის არარსებობა იქ, სადაც
მოთხოვნა ფულს ხარჯავს, წერილს აგზავნის ან პაროლს აღადგენს.

წესები:
- მოახსენე მაქსიმუმ 7 შენიშვნა, დალაგებული ჯერ გამოყენებადობით, მერე ზიანის მასშტაბით. არასდროს
  მოახსენო სტილი, ფორმატირება ან „კარგი პრაქტიკა“, რომელშიც შემტევი არ ფიგურირებს.
- ყოველ შენიშვნას უნდა ახლდეს ფაილი და ხაზი და შეტევის კონკრეტული აღწერა: ვინ არის შემტევი, რა
  მოთხოვნას ან მონაცემს აგზავნის და რას იღებს შედეგად. თუ ამ წინადადებას ვერ წერ, ეს შენიშვნა
  არ არის.
- არასდროს მოახსენო სისუსტე, რომელსაც {{ნდობის_საზღვარი}} ისედაც კეტავს. დაასახელე, რომელი
  საზღვარი აჩერებს მას, და გადადი შემდეგზე.
- თითოეულს მიაწერე ნიშანი: EXPLOITABLE-NOW / EXPLOITABLE-WITH-ACCESS / HARDENING. HARDENING-ის
  ორზე მეტი პუნქტი არასდროს დაწერო.
- თუ ნაჩვენები კოდიდან ვერ არკვევ, გამოსაყენებელია თუ არა სისუსტე, ეს პირდაპირ დაწერე და
  დაასახელე, რისი ნახვა დაგჭირდებოდა — middleware, დეპლოის კონფიგურაცია თუ გამომძახებელი სერვისი.

გამოსავალი თითო შენიშვნაზე: ნიშანი · ფაილი:ხაზი · შეტევა ერთი წინადადებით · რას იღებს შემტევი ·
გამოსწორება. ბოლოს სექცია „ვერ ვადგენ“.
```

---

### RA-03 · Review for this stack's failure modes
`claude` `gpt` `gemini` — review, stack-specific

**EN**
```
Review this code for the failure modes this specific stack produces. Generic advice is not wanted.

Stack: {{stack}}
Versions and runtime: {{versions}}
Deployment shape: {{deployment}}

<code>
{{code}}
</code>

First list the 5 failure modes this stack is actually known for in this deployment shape — the
ones that bite in production, not the ones in the getting-started guide. Then check the code
against those 5 and nothing else.

Rules:
- Report at most 6 findings, ordered most severe first. NEVER report style or formatting issues.
- Every finding MUST name the file and line, which of your 5 failure modes it is, and a concrete
  scenario: the load, input or sequence that triggers it, and what the user sees when it does.
- NEVER report a problem that belongs to a stack other than {{stack}}, however familiar it is.
- If the code is clean against one of the 5, write one line saying so. NEVER invent a finding to
  fill the slot.
- If a failure mode cannot be checked from the code shown, say so and name what you would need to
  see — the connection pool config, the worker settings, the container memory limit.

Output: The 5 failure modes (one line each) · Findings · Cannot determine.
```

**KA**
```
გაუკეთე რევიუ ამ კოდს იმ ჩავარდნებზე, რომლებსაც სწორედ ეს სტეკი აწარმოებს. ზოგადი რჩევა არ მჭირდება.

სტეკი: {{სტეკი}}
ვერსიები და გარემო: {{ვერსიები}}
როგორ არის გაშვებული: {{დეპლოი}}

<code>
{{კოდი}}
</code>

ჯერ ჩამოწერე 5 ჩავარდნის სცენარი, რომლითაც ეს სტეკი სწორედ ასეთ გაშვებაში ცნობილია — ის, რაც
პროდაქშენში იჩენს თავს და არა ის, რაც დოკუმენტაციის შესავალშია. მერე შეამოწმე კოდი მხოლოდ ამ
ხუთის მიმართ.

წესები:
- მოახსენე მაქსიმუმ 6 შენიშვნა, ყველაზე მძიმით დაწყებული. არასდროს მოახსენო სტილის ან
  ფორმატირების შენიშვნა.
- ყოველ შენიშვნას უნდა ახლდეს ფაილი და ხაზი, შენი ხუთეულიდან რომელ სცენარს ეკუთვნის, და კონკრეტული
  სიტუაცია: რა დატვირთვა, შესატანი მონაცემი ან თანმიმდევრობა იწვევს მას და რას ხედავს ამ დროს
  მომხმარებელი.
- არასდროს მოახსენო პრობლემა, რომელიც {{სტეკი}}-ს არ ეხება, რაც უნდა ნაცნობი იყოს.
- თუ კოდი ხუთეულის რომელიმე პუნქტის მიმართ სუფთაა, ეს ერთ ხაზში დაწერე. სლოტის შესავსებად
  შენიშვნა არასდროს გამოიგონო.
- თუ რომელიმე სცენარს ნაჩვენები კოდიდან ვერ ამოწმებ, ეს პირდაპირ დაწერე და დაასახელე, რისი ნახვა
  დაგჭირდებოდა — კავშირების პულის კონფიგურაცია, worker-ების პარამეტრები თუ კონტეინერის მეხსიერების
  ლიმიტი.

გამოსავალი: 5 ჩავარდნის სცენარი (თითო ერთ ხაზში) · შენიშვნები · ვერ ვადგენ.
```

---

### RA-04 · Refactor plan as independent PRs
`claude` `gpt` `claude-code` — refactoring, planning

**EN**
```
Turn this refactor into a sequence of pull requests that can each ship on their own.

What is wrong today: {{problem}}
Target shape: {{target}}
Constraints that cannot be broken: {{constraints}}
Test coverage on the affected code today: {{coverage}}

<code_map>
{{files_and_responsibilities}}
</code_map>

Rules:
- Every PR MUST be independently shippable: once it merges, main is green and the product behaves
  exactly as it did before. A PR that only makes sense after the next one lands is not a PR —
  merge the two and say so.
- Every PR MUST fit under 400 changed lines. If a step cannot, split it and state what the split
  costs.
- Maximum 8 PRs. If the refactor needs more, cut the target and say exactly what you cut.
- For each PR: the files it touches, the behaviour it must NOT change, the command that proves it,
  and how to revert it on its own.
- MUST name every PR that cannot be reverted independently, and why.
- MUST name the single PR that carries the real risk. The rest are preparation.
- If {{coverage}} is not enough to prove a step preserves behaviour, make writing that test its own
  PR at the front of the sequence.
- NEVER put a behaviour change and a move-or-rename in the same PR.

Output: numbered PR list with the fields above · Riskiest PR and why · What I would not refactor
and why not.
```

**KA**
```
დაშალე ეს რეფაქტორინგი PR-ების თანმიმდევრობად, სადაც თითოეული ცალკე იდება.

რა არის დღეს არასწორად: {{პრობლემა}}
სამიზნე მდგომარეობა: {{სამიზნე}}
შეზღუდვები, რომელთა დარღვევაც არ შეიძლება: {{შეზღუდვები}}
დღევანდელი ტესტების დაფარვა შესაცვლელ კოდზე: {{დაფარვა}}

<code_map>
{{ფაილები_და_პასუხისმგებლობები}}
</code_map>

წესები:
- ყოველი PR ცალკე უნდა იდგმებოდეს: მისი შერწყმის შემდეგ main მწვანეა და პროდუქტი ზუსტად ისე იქცევა,
  როგორც მანამდე. PR, რომელსაც აზრი მხოლოდ მომდევნოს მერე აქვს, PR არ არის — გააერთიანე ორივე და
  ეს დაწერე.
- ყოველი PR უნდა ეტეოდეს 400 შეცვლილ ხაზში. თუ ეტაპი ვერ ეტევა, გაყავი და დაწერე, რა ფასი აქვს
  ამ გაყოფას.
- მაქსიმუმ 8 PR. თუ რეფაქტორინგს მეტი სჭირდება, შეამცირე სამიზნე და ზუსტად დაასახელე, რა ამოაგდე.
- თითო PR-ზე: რომელ ფაილებს ეხება, რომელი ქცევა არ უნდა შეიცვალოს, რომელი ბრძანება ამოწმებს ამას
  და როგორ ბრუნდება ეს PR ცალკე უკან.
- დაასახელე ყოველი PR, რომელიც ცალკე უკან ვერ ბრუნდება, და მიზეზი.
- დაასახელე ერთი PR, რომელზეც რეალური რისკი მოდის. დანარჩენი მომზადებაა.
- თუ {{დაფარვა}} არ ყოფნის იმის დასამტკიცებლად, რომ ეტაპი ქცევას არ ცვლის, ამ ტესტის დაწერა ცალკე
  PR-ად აქციე და თანმიმდევრობის დასაწყისში დადე.
- არასდროს მოაქციო ერთ PR-ში ქცევის ცვლილება და ფაილის გადატანა ან სახელის შეცვლა.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: დანომრილი PR-ების სია ზემოთ ჩამოთვლილი ველებით · ყველაზე სარისკო PR და რატომ ·
რას არ შევეხებოდი და რატომ.
```

---

### RA-05 · Does this abstraction earn its cost
`claude` `gpt` — design, abstraction

**EN**
```
Judge whether this abstraction is worth introducing. The default answer is no — argue me out of it.

Proposed abstraction: {{abstraction}}
The duplication or problem it removes: {{problem}}
Call sites today: {{call_sites}}
Call sites expected in six months, and what that number rests on: {{projection}}

Rules:
- First line is the verdict: INTRODUCE IT / NOT YET / NO. Everything after it is justification.
- MUST count the cost concretely: how many files a reader opens to follow one request end to end,
  before and after. Give both numbers.
- MUST name one change that would be harder after this abstraction exists than it is today.
- MUST state the number of call sites at which the verdict flips, and what would have to happen
  for that number to be reached.
- NEVER accept "we will need it later" unless {{projection}} names a specific dated thing that
  needs it. If it does not, say the projection is unsupported.
- If the duplicated blocks change for different reasons, say so — that is not duplication worth
  removing, and the abstraction will fight every future change.
- If you cannot tell from what you were given whether the call sites share a reason to change,
  say so and name what you would need to see.

Output: Verdict · What it costs a reader · What it makes harder · The flip point · The cheaper
thing to do instead, if there is one.
```

**KA**
```
შეაფასე, ღირს თუ არა ამ აბსტრაქციის შემოტანა. ნაგულისხმევი პასუხია „არა“ — დამარწმუნე საწინააღმდეგოში.

შემოთავაზებული აბსტრაქცია: {{აბსტრაქცია}}
რომელ გამეორებას ან პრობლემას ხსნის: {{პრობლემა}}
გამოძახების ადგილები დღეს: {{გამოძახებები}}
რამდენი იქნება ნახევარ წელიწადში და რას ეყრდნობა ეს ციფრი: {{პროგნოზი}}

წესები:
- პირველივე ხაზი დასკვნაა: შემოიტანე / ჯერ არა / არა. დანარჩენი დასაბუთებაა.
- ღირებულება კონკრეტულად დათვალე: რამდენ ფაილს ხსნის მკითხველი ერთი მოთხოვნის თავიდან ბოლომდე
  გასაყოლად ცვლილებამდე და რამდენს — მის შემდეგ. ორივე ციფრი დაწერე.
- დაასახელე ერთი ცვლილება, რომელიც ამ აბსტრაქციის შემდეგ უფრო რთული იქნება, ვიდრე დღეს არის.
- დაწერე, გამოძახების რამდენ ადგილზე იცვლება დასკვნა და რა უნდა მოხდეს, რომ ეს ციფრი დადგეს.
- არასდროს მიიღო არგუმენტად „მერე დაგვჭირდება“, თუ {{პროგნოზი}} კონკრეტულ, ვადიან საქმეს არ
  ასახელებს. თუ არ ასახელებს, დაწერე, რომ პროგნოზი დაუსაბუთებელია.
- თუ გამეორებული ბლოკები სხვადასხვა მიზეზით იცვლება, ეს დაწერე — ასეთი გამეორება მოსაშორებელი არ
  არის და აბსტრაქცია ყოველ მომავალ ცვლილებას შეეწინააღმდეგება.
- თუ მოცემული მასალიდან ვერ არკვევ, აქვთ თუ არა ამ გამოძახებებს შეცვლის საერთო მიზეზი, ეს პირდაპირ
  დაწერე და დაასახელე, რისი ნახვა დაგჭირდებოდა.

გამოსავალი: დასკვნა · რა უჯდება მკითხველს · რას ართულებს · სად იცვლება დასკვნა · რა იქნებოდა
უფრო იაფი გამოსავალი, თუ არსებობს.
```

---

### RA-06 · Two designs against named criteria
`claude` `gpt` `gemini` — design, decision

**EN**
```
Compare two designs and tell me which assumption decides between them.

Design A: {{design_a}}
Design B: {{design_b}}
The decision this comparison must inform: {{decision}}

Criteria, in priority order. Use these and no others:
1. {{criterion_1}}
2. {{criterion_2}}
3. {{criterion_3}}
Anything outside this list is out of scope for this comparison, however interesting it is.

Rules:
- Score each design against each criterion with a concrete consequence, never an adjective:
  "one extra network hop per request, about 15ms" — not "slightly slower".
- MUST state in one sentence the single assumption that decides the outcome: the fact which, if it
  turned out to be false, would flip the recommendation.
- MUST state how to test that assumption before committing, and what testing it costs.
- MUST name what each design makes permanently hard, not only what it makes slow.
- NEVER answer "it depends". Pick one and say what would change your mind.
- If the material given does not settle a criterion for one design, write "not determinable from
  what I have" in that cell and name what you would need to see.

Output: a table (criterion | A | B | which wins), then: The deciding assumption · How to test it ·
Recommendation · What would reverse it.
```

**KA**
```
შეადარე ორი დიზაინი და დაასახელე დაშვება, რომელიც მათ შორის არჩევანს წყვეტს.

დიზაინი A: {{დიზაინი_a}}
დიზაინი B: {{დიზაინი_b}}
გადაწყვეტილება, რომელსაც ეს შედარება უნდა დაეხმაროს: {{გადაწყვეტილება}}

კრიტერიუმები, პრიორიტეტის მიხედვით. იმუშავე მხოლოდ ამ სამით:
1. {{კრიტერიუმი_1}}
2. {{კრიტერიუმი_2}}
3. {{კრიტერიუმი_3}}
ყველაფერი ამ სიის გარეთ ამ შედარების არეალს სცდება, რაც უნდა საინტერესო იყოს.

წესები:
- თითო კრიტერიუმზე თითოეული დიზაინი შეაფასე კონკრეტული შედეგით და არა ზედსართავით:
  „ერთი დამატებითი ქსელური გადასვლა თითო მოთხოვნაზე, დაახლოებით 15 მწმ“ და არა „ოდნავ ნელია“.
- ერთ წინადადებაში დაასახელე ერთადერთი დაშვება, რომელიც შედეგს წყვეტს: ფაქტი, რომლის გაბათილებაც
  რეკომენდაციას საპირისპიროდ შეატრიალებდა.
- დაწერე, როგორ შემოწმდება ეს დაშვება გადაწყვეტილებამდე და რა დაჯდება მისი შემოწმება.
- დაასახელე, რას ხდის თითოეული დიზაინი სამუდამოდ რთულს — და არა მხოლოდ რას ანელებს.
- არასდროს უპასუხო „დამოკიდებულია“. აირჩიე ერთი და დაწერე, რა შეგაცვლევინებდა აზრს.
- თუ მოცემული მასალა რომელიმე კრიტერიუმზე პასუხს არ იძლევა, იმ უჯრაში დაწერე „მოცემული მასალით
  ვერ ვადგენ“ და დაასახელე, რისი ნახვა დაგჭირდებოდა.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ცხრილი (კრიტერიუმი | A | B | რომელი იგებს), შემდეგ: გადამწყვეტი დაშვება · როგორ
შემოწმდება · რეკომენდაცია · რა შეცვლიდა მას.
```

---

### RA-07 · Architecture decision record with the rejected options
`claude` `gpt` `claude-code` — documentation, adr

**EN**
```
Write an architecture decision record for a decision that has already been made.

Decision: {{decision}}
Context and the forces behind it: {{context}}
Options that were considered: {{options}}
Constraints that were real, not aspirational: {{constraints}}
Date and who decided: {{decider}}

Rules:
- MUST document every option in {{options}}, the rejected ones included, each with the reason it
  lost. An ADR that records only the winner is worthless in six months — the rejected options are
  the document.
- Each rejection reason MUST be a specific consequence under {{constraints}}, not a generic
  weakness of the technology. "Needs a second Postgres instance we have no budget for" — not
  "harder to scale".
- MUST state what this decision makes hard or impossible later, and what undoing it would take.
- MUST state the assumption the decision rests on and the observable event that would mean it was
  wrong.
- NEVER rewrite history to make the choice look inevitable. If it was close, say so and say what
  made it close.
- If {{context}} does not contain what a section needs, write "not recorded". NEVER fill the gap.

Output sections: Title · Status and date · Context · Decision · Options considered (each with why
it lost) · Consequences, good and bad · What would reverse this · Not recorded.
```

**KA**
```
დაწერე არქიტექტურული გადაწყვეტილების ჩანაწერი (ADR) გადაწყვეტილებაზე, რომელიც უკვე მიღებულია.

გადაწყვეტილება: {{გადაწყვეტილება}}
კონტექსტი და რა კარნახობდა მას: {{კონტექსტი}}
განხილული ვარიანტები: {{ვარიანტები}}
შეზღუდვები, რომლებიც რეალური იყო და არა სასურველი: {{შეზღუდვები}}
თარიღი და ვინ გადაწყვიტა: {{გადაწყვეტილების_მიმღები}}

წესები:
- ჩაწერე {{ვარიანტები}}-ს ყოველი პუნქტი, უარყოფილების ჩათვლით, და თითოეულს მიაწერე, რატომ წააგო.
  ADR, რომელშიც მხოლოდ გამარჯვებული წერია, ნახევარ წელიწადში უსარგებლოა — უარყოფილი ვარიანტებია
  თვითონ დოკუმენტი.
- უარის ყოველი მიზეზი კონკრეტული შედეგი უნდა იყოს {{შეზღუდვები}}-ს პირობებში და არა ტექნოლოგიის
  ზოგადი სისუსტე. „სჭირდება მეორე Postgres, რომლისთვისაც ბიუჯეტი არ გვაქვს“ და არა „ცუდად სკალირდება“.
- დაწერე, რას ხდის ეს გადაწყვეტილება მომავალში რთულს ან შეუძლებელს და რა დასჭირდება მის უკან დაბრუნებას.
- დაასახელე დაშვება, რომელზეც გადაწყვეტილება დგას, და ის დაკვირვებადი მოვლენა, რომელიც ამ დაშვების
  მცდარობას დაადასტურებდა.
- არასდროს გადაწერო ისტორია ისე, თითქოს არჩევანი გარდაუვალი იყო. თუ გადაწყვეტილება ძნელი იყო, ეს
  დაწერე და დაასახელე, რა ხდიდა მას ძნელს.
- თუ {{კონტექსტი}}-ში სექციისთვის საჭირო ინფორმაცია არ არის, დაწერე „არ არის დაფიქსირებული“.
  ხარვეზი არასდროს შეავსო.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი, სექციებად: სათაური · სტატუსი და თარიღი · კონტექსტი · გადაწყვეტილება · განხილული
ვარიანტები (თითოეულს — რატომ წააგო) · შედეგები, დადებითი და უარყოფითი · რა დააბრუნებდა ამას უკან ·
არ არის დაფიქსირებული.
```

---

### RA-08 · Riskiest part of a change, and the first test to write
`claude` `gpt` `claude-code` — risk, testing

**EN**
```
Find the part of this change most likely to be wrong, and tell me what to test before anything else.

<diff>
{{diff}}
</diff>

What it changes for users: {{user_impact}}
What is already covered by tests: {{existing_tests}}
How it will be released: {{rollout}}

Rules:
- Name at most 3 risky areas, ordered by probability of being wrong multiplied by cost of being
  wrong. NEVER list style or formatting concerns — they are not risk.
- For each: the file and line, why THIS code is likely to be wrong (new logic, changed invariant,
  untested branch, concurrency, data migration), and the concrete scenario in which it produces a
  wrong result — the inputs and the wrong output.
- For each, give exactly ONE test to write first: the input, the expected output, and what its
  failure would tell you. A test plan is not an answer; one test is.
- MUST say which of the risky areas {{existing_tests}} already covers, and stop calling those
  risky.
- MUST name the signal to watch after release and the threshold at which to roll back. A signal
  with no threshold is not a signal.
- If you cannot tell from the diff whether a path is reached in production, say so and name what
  you would need to see — traffic data, feature flags, the caller.

Output: Risk 1–3 in the shape above · The first test to write · Rollback signal and threshold.
```

**KA**
```
იპოვე ამ ცვლილების ის ნაწილი, რომელიც ყველაზე დიდი ალბათობით არასწორია, და დამისახელე, რა უნდა
შემოწმდეს ყველაფერზე ადრე.

<diff>
{{დიფი}}
</diff>

რას ცვლის მომხმარებლისთვის: {{გავლენა}}
რა არის უკვე ტესტებით დაფარული: {{არსებული_ტესტები}}
როგორ გავა ეს ცვლილება პროდაქშენში: {{გამოშვება}}

წესები:
- დაასახელე მაქსიმუმ 3 სარისკო ადგილი, დალაგებული შეცდომის ალბათობისა და შეცდომის ფასის ნამრავლით.
  არასდროს ჩამოწერო სტილის ან ფორმატირების საკითხი — ის რისკი არ არის.
- თითოეულზე: ფაილი და ხაზი, რატომ არის სწორედ ეს კოდი სავარაუდოდ არასწორი (ახალი ლოგიკა, შეცვლილი
  ინვარიანტი, დაუტესტავი განშტოება, პარალელურობა, მონაცემების მიგრაცია) და კონკრეტული სცენარი,
  რომელშიც ის არასწორ შედეგს აბრუნებს — რა შედის და რა გამოდის.
- თითოეულზე დაასახელე ზუსტად ერთი ტესტი, რომელიც პირველი უნდა დაიწეროს: შესატანი მონაცემი,
  მოსალოდნელი შედეგი და რას გეტყოდა მისი ჩავარდნა. ტესტების გეგმა პასუხი არ არის; ერთი ტესტია პასუხი.
- დაწერე, სარისკო ადგილებიდან რომელს ფარავს უკვე {{არსებული_ტესტები}}, და ის სარისკოდ აღარ ჩათვალო.
- დაასახელე სიგნალი, რომელსაც გამოშვების შემდეგ უნდა ვუყუროთ, და ზღვარი, რომელზეც rollback კეთდება.
  სიგნალი ზღვრის გარეშე სიგნალი არ არის.
- თუ დიფიდან ვერ არკვევ, მიუწვდება თუ არა პროდაქშენს ხელი რომელიმე გზამდე, ეს პირდაპირ დაწერე და
  დაასახელე, რისი ნახვა დაგჭირდებოდა — ტრაფიკის მონაცემები, feature flag-ები თუ გამომძახებელი კოდი.

გამოსავალი: რისკი 1–3 ზემოთ აღწერილი ფორმით · პირველი დასაწერი ტესტი · rollback-ის სიგნალი და ზღვარი.
```

---

### RA-09 · Blast radius of a change
`claude-code` `cursor` `claude` — impact, repo-wide

**EN**
```
Map what this change can break across the codebase. This task is read-only — change nothing.

The change: {{change}}
The symbol, endpoint or table it touches: {{surface}}

Find the callers yourself before reasoning about them:
  `rg -n "{{surface}}" --type {{lang}}`
  `rg -n "{{surface}}" -g '!*test*'`
Print the match count before the analysis.

Rules:
- Group affected places into DIRECT (calls it), INDIRECT (calls something that calls it), and
  CROSSES-A-BOUNDARY (another service, a queue consumer, a scheduled job, a client app, a stored
  SQL view, a dashboard query).
- Report at most 8 impacted places, ordered by how badly each breaks. NEVER list a caller that is
  affected only cosmetically.
- Every entry MUST name the file and line and the concrete failure: what input reaches it and what
  it does wrong once {{change}} lands.
- MUST list separately what this change touches that is NOT in this repo — other services, jobs,
  shipped client versions, saved queries — and how you would confirm each one.
- If you cannot tell whether a caller is live or dead code, say so and name what you would need to
  see: traffic, feature flags, deploy history.
- NEVER edit, create or delete a file. `git status --porcelain` must stay empty.

Output: Match count · Direct · Indirect · Crosses a boundary · Outside this repo · Cannot determine.
```

**KA**
```
დაადგინე, რისი გატეხვა შეუძლია ამ ცვლილებას მთელ კოდის ბაზაში. ეს ამოცანა მხოლოდ კითხვისაა —
არაფერი შეცვალო.

ცვლილება: {{ცვლილება}}
სიმბოლო, ენდპოინტი ან ცხრილი, რომელსაც ეხება: {{სამიზნე}}

გამომძახებლები ჯერ თვითონ იპოვე და მერე იმსჯელე მათზე:
  `rg -n "{{სამიზნე}}" --type {{ენა}}`
  `rg -n "{{სამიზნე}}" -g '!*test*'`
ანალიზამდე დაბეჭდე დამთხვევების რაოდენობა.

წესები:
- დააჯგუფე ადგილები სამად: DIRECT (პირდაპირ იძახებს), INDIRECT (იძახებს იმას, რაც მას იძახებს) და
  CROSSES-A-BOUNDARY (სხვა სერვისი, რიგის მომხმარებელი, დაგეგმილი job, კლიენტის აპლიკაცია,
  შენახული SQL-ხედი, დაშბორდის მოთხოვნა).
- მოახსენე მაქსიმუმ 8 დაზარალებული ადგილი, დალაგებული იმის მიხედვით, რამდენად მძიმედ იშლება
  თითოეული. არასდროს ჩამოწერო გამომძახებელი, რომელზეც გავლენა მხოლოდ კოსმეტიკურია.
- ყოველ ჩანაწერს უნდა ახლდეს ფაილი და ხაზი და კონკრეტული ჩავარდნა: რა შესატანი მონაცემი აღწევს
  იქამდე და რას აკეთებს არასწორად მას შემდეგ, რაც {{ცვლილება}} დაიდება.
- ცალკე ჩამოწერე, რას ეხება ეს ცვლილება ამ რეპოს გარეთ — სხვა სერვისები, job-ები, უკვე გაშვებული
  კლიენტის ვერსიები, შენახული მოთხოვნები — და როგორ გადაამოწმებდი თითოეულს.
- თუ ვერ არკვევ, ცოცხალია თუ მკვდარი კოდი გამომძახებელი, ეს პირდაპირ დაწერე და დაასახელე, რისი
  ნახვა დაგჭირდებოდა: ტრაფიკი, feature flag-ები, დეპლოის ისტორია.
- არასდროს შეასწორო, შექმნა ან წაშალო ფაილი. `git status --porcelain` ცარიელი უნდა დარჩეს.

გამოსავალი: დამთხვევების რაოდენობა · DIRECT · INDIRECT · CROSSES-A-BOUNDARY · რეპოს გარეთ ·
ვერ ვადგენ.
```

---

### RA-10 · What will break for existing users
`claude` `gpt` `claude-code` — compatibility, api

**EN**
```
Review this change for what it breaks for people already on the current version.

<diff>
{{diff}}
</diff>

What consumes this and how it is versioned: {{consumers}}
The compatibility promise we made: {{promise}}
How consumers upgrade and how long old versions stay live: {{upgrade_path}}

Check all of these, not just the function signature: request and response shapes; default values;
error codes and messages consumers match on; ordering and pagination; new enum values arriving at
a consumer that switches on them; data written by the old version and read by the new one, and the
reverse; config keys; timeouts and rate limits.

Rules:
- Report at most 7 breaks, ordered by how many consumers hit each one. NEVER report a change that
  is internal to this repo and reaches no consumer.
- Every break MUST name the file and line and a concrete scenario: a consumer on version X sends
  this request, or holds this stored row, and gets this wrong result. Name the version.
- Label each SILENT (keeps working, returns a wrong answer) or LOUD (visible error). SILENT goes
  first, always — a loud break is found in an hour, a silent one in a quarter.
- For each, say whether a deprecation window, a version header, or dual-writing would avoid it,
  and what that costs us.
- If you cannot tell from the diff whether a consumer depends on a behaviour, say so and name what
  you would need to see — client code, request logs, the shape of stored rows.

Output per break: SILENT/LOUD · file:line · the consumer scenario · the wrong result · the
mitigation. Then: Cannot determine · Safe to ship as is.
```

**KA**
```
გაუკეთე რევიუ ამ ცვლილებას იმაზე, რა ეტეხებათ მათ, ვინც უკვე მიმდინარე ვერსიაზე ზის.

<diff>
{{დიფი}}
</diff>

ვინ იყენებს ამას და როგორ არის დაყოფილი ვერსიებად: {{კლიენტები}}
თავსებადობის დაპირება, რომელიც მივეცით: {{დაპირება}}
როგორ ახლდებიან კლიენტები და რამდენ ხანს ცოცხლობს ძველი ვერსია: {{განახლების_გზა}}

შეამოწმე ყველა ეს პუნქტი და არა მხოლოდ ფუნქციის ხელმოწერა: მოთხოვნისა და პასუხის სტრუქტურა;
ნაგულისხმევი მნიშვნელობები; შეცდომის კოდები და ტექსტები, რომლებსაც კლიენტი ამოწმებს; დალაგება და
გვერდებად დაყოფა; ახალი enum-მნიშვნელობა, რომელიც კლიენტამდე მიდის და რომელზეც ის switch-ს აკეთებს;
მონაცემი, რომელიც ძველმა ვერსიამ ჩაწერა და ახალი კითხულობს, და პირიქით; კონფიგურაციის გასაღებები;
ტაიმაუტები და ლიმიტები.

წესები:
- მოახსენე მაქსიმუმ 7 გატეხვა, დალაგებული იმის მიხედვით, რამდენ კლიენტს ხვდება თითოეული. არასდროს
  მოახსენო ცვლილება, რომელიც ამ რეპოს შიგნით რჩება და კლიენტამდე არ აღწევს.
- ყოველ გატეხვას უნდა ახლდეს ფაილი და ხაზი და კონკრეტული სცენარი: X ვერსიაზე მყოფი კლიენტი აგზავნის
  ამ მოთხოვნას ან ინახავს ამ ჩანაწერს და იღებს ამ არასწორ შედეგს. ვერსია დაასახელე.
- თითოეულს მიაწერე ნიშანი: SILENT (მუშაობს, მაგრამ არასწორ პასუხს აბრუნებს) ან LOUD (ხილული
  შეცდომა). SILENT ყოველთვის წინ დადე — ხმაურიან გატეხვას ერთ საათში პოულობენ, ჩუმს კი კვარტალში.
- თითოეულზე დაწერე, აგვარიდებდა თუ არა თავიდან deprecation-ის პერიოდი, ვერსიის ჰედერი ან ორმაგი
  ჩაწერა, და რა დაგვიჯდება ეს.
- თუ დიფიდან ვერ არკვევ, ეყრდნობა თუ არა კლიენტი რომელიმე ქცევას, ეს პირდაპირ დაწერე და დაასახელე,
  რისი ნახვა დაგჭირდებოდა — კლიენტის კოდი, მოთხოვნების ლოგები თუ შენახული ჩანაწერების სტრუქტურა.

გამოსავალი თითო გატეხვაზე: SILENT/LOUD · ფაილი:ხაზი · კლიენტის სცენარი · არასწორი შედეგი ·
როგორ ავირიდოთ. შემდეგ: ვერ ვადგენ · უსაფრთხოდ იდება ასე, როგორც არის.
```

---

### RA-11 · Tech debt ranked by cost of delay
`claude` `gpt` `gemini` — tech-debt, prioritisation

**EN**
```
Turn this pile of complaints into a ranked list. The ranking is the deliverable, not the list.

<complaints>
{{complaints}}
</complaints>

Team size and how much time per sprint goes to debt: {{capacity}}
What the team ships in the next two quarters: {{roadmap}}
Incidents in the last six months: {{incidents}}

Rank by cost of delay: what each item costs per month if nobody touches it, and how fast that cost
is growing. Cheap-and-annoying loses to expensive-and-quiet.

Rules:
- Rank every item against every other. NEVER output an unranked list, a 2x2 grid, or high/medium/low
  buckets — those are ways of avoiding the decision.
- Each item MUST carry: the monthly cost today (engineer-hours, incidents, or lari), whether that
  cost is flat or compounding, the fix size in engineer-days, and which item in {{roadmap}} it slows
  down.
- Merge complaints that are the same underlying problem, and list which ones you merged.
- MUST mark every cost you estimated rather than took from {{incidents}} or {{complaints}}, and say
  what the estimate is based on.
- MUST name the items NOT to fix, each with the reason: the code is being deleted, the cost is flat
  and small, or the fix costs more than the debt does.
- If an item's cost cannot be estimated from what you were given, put it under "Needs measurement"
  and name the one measurement that would place it in the ranking.
- NEVER rank an item by how unpleasant the code is to read.

Output: ranked table (rank | item | monthly cost | flat or compounding | fix size | what it blocks)
· Merged · Do not fix · Needs measurement.
```

**KA**
```
გადააქციე ეს საჩივრების გროვა რანჟირებულ სიად. შედეგი რანჟირებაა და არა თვითონ სია.

<complaints>
{{საჩივრები}}
</complaints>

გუნდის ზომა და რამდენი დრო ეთმობა ტექნიკურ ვალს თითო სპრინტში: {{რესურსი}}
რას უშვებს გუნდი მომდევნო ორ კვარტალში: {{გეგმა}}
ინციდენტები ბოლო ნახევარი წლის განმავლობაში: {{ინციდენტები}}

დაალაგე გადავადების ფასის მიხედვით: რა უჯდება თითოეული პუნქტი თვეში, თუ მას არავინ შეეხო, და
რამდენად სწრაფად იზრდება ეს ფასი. იაფი და მოსაბეზრებელი აგებს ძვირსა და ჩუმს.

წესები:
- დაარანჟირე ყოველი პუნქტი ყოველი სხვის მიმართ. არასდროს დააბრუნო დაულაგებელი სია, 2x2 მატრიცა ან
  „მაღალი / საშუალო / დაბალი“ ჯგუფები — ეს გადაწყვეტილების არიდების ხერხებია.
- ყოველ პუნქტს უნდა ახლდეს: დღევანდელი თვიური ფასი (ინჟინრის საათი, ინციდენტი ან ლარი), ეს ფასი
  ფიქსირებულია თუ მზარდი, გამოსწორების მოცულობა ინჟინერ-დღეებში და {{გეგმა}}-ს რომელ პუნქტს აფერხებს.
- გააერთიანე საჩივრები, რომლებიც ერთსა და იმავე პრობლემას აღწერს, და ჩამოწერე, რომლები გააერთიანე.
- მონიშნე ყოველი ფასი, რომელიც შენ შეაფასე და არა {{ინციდენტები}}-დან ან {{საჩივრები}}-დან აიღე,
  და დაწერე, რას ეყრდნობა შეფასება.
- დაასახელე პუნქტები, რომლებიც არ უნდა გასწორდეს, და თითოეულზე მიზეზი: კოდი ისედაც იშლება, ფასი
  ფიქსირებული და მცირეა, ან გამოსწორება უფრო ძვირია, ვიდრე თვითონ ვალი.
- თუ პუნქტის ფასს მოცემული მასალით ვერ აფასებ, ჩაწერე სექციაში „საზომია“ და დაასახელე ერთი გაზომვა,
  რომელიც მას რანჟირებაში ჩასვამდა.
- არასდროს დაარანჟირო პუნქტი იმის მიხედვით, რამდენად უსიამოვნოა კოდის კითხვა.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: რანჟირებული ცხრილი (ადგილი | პუნქტი | თვიური ფასი | ფიქსირებული თუ მზარდი |
გამოსწორების მოცულობა | რას აფერხებს) · გაერთიანებული · არ გასწორდეს · საზომია.
```
