# Everyday / ყოველდღიური

Personal decisions, planning, learning, money and paperwork — the half of life that is not work.
Georgian entries assume living in Georgia: `ლარი`, `ბინის ქირა`, `კომუნალური გადასახადები`, `RS.ge`, `საჯარო რეესტრი`, `მარშრუტკა`.

---

### D-01 · Decide between two options
`claude` `gpt` `gemini` — decisions, personal

**EN**
```
You are helping me decide. You are not deciding for me.

Option A: {{option_a}}
Option B: {{option_b}}
What I actually want out of this: {{goal}}
I have to decide by: {{deadline}}

Work in this order:
1. For each option, what it costs me if I am wrong — in money, in time, and in things I cannot get back.
2. Rate each option's reversibility: fully reversible / reversible at a price / one-way. Name the price of reversing it.
3. Name the one fact I do not have that would change the answer, and the cheapest way to get it before {{deadline}}.
4. Write the strongest one-paragraph case for each option, the way someone who wants it would write it.

Rules:
- NEVER tell me which to choose, and NEVER close with "it depends on you".
- MUST point out any place where I stated a preference as if it were a fact.
- MUST NOT invent a cost, a price or a risk I did not give you.
- Under 350 words.
```

**KA**
```
შენ მეხმარები გადაწყვეტილების მიღებაში. ჩემ ნაცვლად არ წყვეტ.

ვარიანტი 1: {{ვარიანტი_1}}
ვარიანტი 2: {{ვარიანტი_2}}
რა მინდა სინამდვილეში: {{მიზანი}}
გადაწყვეტილების ვადა: {{ვადა}}

იმუშავე ამ თანმიმდევრობით:
1. თითოეულ ვარიანტზე დაწერე, რა დამიჯდება შეცდომა — ფულში, დროში და იმაში, რაც უკან აღარ ბრუნდება.
2. შეაფასე თითოეულის შექცევადობა: სრულად შექცევადი / შექცევადი ფასის გადახდით / ცალმხრივი. დაასახელე უკან დაბრუნების ფასი.
3. დაასახელე ერთი ფაქტი, რომელიც ახლა არ ვიცი და რომელიც პასუხს შეცვლიდა, და ყველაზე იაფი გზა, რომ {{ვადა}}-მდე გავიგო.
4. დაწერე თითოეული ვარიანტის ყველაზე ძლიერი დასაბუთება ერთ აბზაცში — ისე, როგორც მისი მომხრე დაწერდა.

წესები:
- არ დამისახელო, რომელი ავირჩიო, და არ დაასრულო ფრაზით „ეს შენზეა დამოკიდებული“
- თუ სადმე ჩემი სურვილი ფაქტად მაქვს დაწერილი, ცალკე აღნიშნე
- არ მოიგონო ხარჯი, ფასი ან რისკი, რომელიც არ მოგეცა
- სულ 350 სიტყვამდე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.
```

---

### D-02 · A message I have been putting off
`claude` `gpt` — personal, communication

**EN**
```
Help me write a message I have been avoiding for days.

Who it goes to, and what they are to me: {{recipient}}
What kind of message: {{message_type}} — declining / renegotiating / apologising / asking to change something
The facts, including anything I got wrong: {{facts}}
What I am willing to offer: {{offer}}
What I will not do: {{limits}}

Rules:
- MUST say the hard part in the first two sentences. NEVER open with small talk.
- MUST give exactly one reason. NEVER stack reasons — a list of them reads as an argument waiting to be beaten.
- NEVER apologise for having a limit. Apologise only for something I actually did.
- MUST NOT promise anything outside {{offer}}.
- MUST NOT explain my feelings at length. One sentence at most.
- 60–120 words.

Then, separately: the two most likely replies, and one line I could answer each with.

Output: the message · likely replies and my answers.
```

**KA**
```
დამეხმარე იმ წერილის დაწერაში, რომელსაც უკვე დღეებია ვერიდები.

ვის ვწერ და ვინ მეკუთვნის: {{ადრესატი}}
რა ტიპის წერილია: {{ტიპი}} — უარის თქმა / პირობების გადახედვა / ბოდიშის მოხდა / ცვლილების თხოვნა
ფაქტები, იმის ჩათვლით, რაშიც მე ვცდებოდი: {{ფაქტები}}
რის შეთავაზება შემიძლია: {{შეთავაზება}}
რას არ გავაკეთებ: {{ზღვარი}}

წესები:
- მთავარი პირველივე ორ წინადადებაში დაწერე. შესავალი საუბრით არ დაიწყო.
- დაასახელე ზუსტად ერთი მიზეზი. მიზეზები არ დააგროვო — სია კამათის მოწვევად იკითხება.
- ბოდიში არ მოიხადო იმაზე, რომ ზღვარი მაქვს. ბოდიში მხოლოდ იმაზე, რაც რეალურად გავაკეთე.
- არაფერი დაპირდე {{შეთავაზება}}-ს გარეთ
- ჩემი განცდები გრძლად არ ახსნა — მაქსიმუმ ერთი წინადადება
- 60–120 სიტყვა

რეგისტრი ადრესატის მიხედვით: ახლობელს — შენობით; უცნობ ადამიანს, კომპანიას ან უწყებას — თქვენობით.
დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: წერილი · ორი მოსალოდნელი პასუხი და თითოზე ჩემი ერთხაზიანი რეპლიკა.
```

---

### D-03 · Learn a skill from zero in N weeks
`claude` `gpt` `gemini` — learning, planning

**EN**
```
Build me a learning plan I can actually follow.

Skill: {{skill}}
Where I am starting: {{current_level}} — treat blank as zero
Time I have: {{hours_per_week}} hours a week for {{weeks}} weeks
What I want to be able to DO at the end: {{end_goal}}
Constraints: {{constraints}}

Rules:
- MUST fit inside {{hours_per_week}} × {{weeks}}. If {{end_goal}} does not fit, say so in the first line and propose a smaller end goal that does.
- Every week MUST end in something I produce or can demonstrate — never in something I have read or watched.
- MUST name the 20% of the material that carries most of the result, and what to skip entirely.
- MUST include a checkpoint at the halfway week with a concrete pass/fail test.
- NEVER name a paid course, book or channel you are not certain exists. Describe the kind of resource instead.
- Maximum 2 resources per week.

Output: a table — week | what I build | what I learn in order to build it | how I know it worked.
Then: "What I am deliberately not learning" and why.
```

**KA**
```
შემიდგინე სასწავლო გეგმა, რომელსაც რეალურად გავყვები.

უნარი: {{უნარი}}
საიდან ვიწყებ: {{დონე}} — თუ ცარიელია, ჩათვალე, რომ ნულიდან
დრო: კვირაში {{საათი_კვირაში}} საათი, სულ {{კვირა}} კვირა
რისი გაკეთება მინდა ბოლოს: {{საბოლოო_მიზანი}}
შეზღუდვები: {{შეზღუდვები}}

წესები:
- გეგმა უნდა ჩაეტიოს {{საათი_კვირაში}} × {{კვირა}} საათში. თუ {{საბოლოო_მიზანი}} არ ეტევა, ეს პირველივე ხაზში დაწერე და შემომთავაზე უფრო მცირე მიზანი, რომელიც ჩაეტევა.
- ყოველი კვირა უნდა მთავრდებოდეს იმით, რასაც ვქმნი ან ვაჩვენებ — და არა იმით, რაც წავიკითხე ან ვნახე
- დაასახელე მასალის ის 20%, რომელიც შედეგის უმეტეს ნაწილს იძლევა, და ის, რაც სულ გამოვტოვო
- შუა კვირაზე ჩადე შემოწმება კონკრეტული „ჩააბარა / ვერ ჩააბარა“ ტესტით
- არ დაასახელო კონკრეტული ფასიანი კურსი, წიგნი ან არხი, რომლის არსებობაშიც დარწმუნებული არ ხარ — აღწერე რესურსის ტიპი
- კვირაში მაქსიმუმ 2 რესურსი

გამოსავალი: ცხრილი — კვირა | რას ვქმნი | რას ვსწავლობ ამისთვის | საიდან გავიგებ, რომ გამოვიდა.
შემდეგ: „რას არ ვსწავლობ განზრახ“ და რატომ.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### D-04 · First 20 minutes on a stalled project
`claude` `gpt` — personal, productivity

**EN**
```
I have something that has not moved in {{stalled_for}}.

The project: {{project}}
What "finished" looks like: {{done_looks_like}}
What I tell myself the blocker is: {{stated_blocker}}

Do this:
1. Decide which the real stall is: the next action is unclear, I am waiting on someone, I am avoiding a decision, or the task is genuinely too big. Pick ONE based on what I wrote, and say which line made you pick it.
2. Give me ONE next action that fits in 20 minutes, needs nothing I do not already have, and leaves a visible artefact — a file, a sent message, a written paragraph, a number written down.
3. State exactly what will be in front of me when the 20 minutes are over.
4. Give the second and third 20-minute steps. NEVER more than three.

Rules:
- NEVER propose "plan it", "research it", "block time for it" or "think about it" as a step.
- NEVER give a step whose output is a feeling or a decision I have not got the facts for.
- If the honest answer is that the project should be dropped, say so in one line and stop.
- Under 200 words.
```

**KA**
```
მაქვს საქმე, რომელიც {{რამდენი_ხანია}} არ დაძრულა.

პროექტი: {{პროექტი}}
როგორ გამოიყურება დასრულებული: {{დასრულებული}}
რას ვეუბნები ჩემს თავს, რომ მიშლის ხელს: {{ჩემი_ახსნა}}

გააკეთე ეს:
1. გადაწყვიტე, რაშია რეალური შეფერხება: შემდეგი ნაბიჯი ბუნდოვანია, სხვას ველოდები, გადაწყვეტილებას ვერიდები, თუ ამოცანა მართლაც დიდია. აირჩიე ერთი იმის მიხედვით, რაც დავწერე, და დაასახელე ის ხაზი, რომლის გამოც აირჩიე.
2. მომეცი ერთი ნაბიჯი, რომელიც 20 წუთში ეტევა, არაფერს მოითხოვს იმის გარდა, რაც უკვე მაქვს, და ხელშესახებ კვალს ტოვებს — ფაილი, გაგზავნილი წერილი, დაწერილი აბზაცი, ჩაწერილი ციფრი.
3. დაწერე ზუსტად, რა მექნება ხელში 20 წუთის შემდეგ.
4. მომეცი მეორე და მესამე 20-წუთიანი ნაბიჯი. სამზე მეტი არასდროს.

წესები:
- ნაბიჯად არ შემომთავაზო „დაგეგმვა“, „მოძიება“, „დროის გამოყოფა“ ან „დაფიქრება“
- არ მომცე ნაბიჯი, რომლის შედეგიც განცდაა ან ისეთი გადაწყვეტილება, რომლისთვისაც ფაქტები არ მაქვს
- თუ პატიოსანი პასუხი ისაა, რომ ეს საქმე უნდა მივატოვო, ერთ ხაზში დაწერე და გაჩერდი
- 200 სიტყვამდე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.
```

---

### D-05 · Weekly review
`claude` `gpt` `gemini` — planning, review

**EN**
```
Run my weekly review from the material below. Ask me nothing.

<week>
{{week}}
</week>

What I said last week's priority was: {{last_priority}}

Output exactly five sections:

FINISHED — what actually reached done. Anything at 90% goes in UNFINISHED.

UNFINISHED — each item with one line on why it did not finish. Use my own words where I gave a reason; write "no reason stated" where I did not.

WHERE THE TIME WENT — actual hours against {{last_priority}}. Give the gap as a number if <week> allows one; otherwise write "not measurable from these notes".

RECURRING — anything that has now appeared more than once without moving. Name it plainly, once.

NEXT — at most 3 priorities. MUST cut rather than carry everything forward; name what is being dropped and say it is being dropped on purpose.

Rules:
- NEVER praise, encourage or soften.
- NEVER add an item that is not in <week>.
- NEVER interpret my mood.
```

**KA**
```
ჩაატარე ჩემი კვირის მიმოხილვა ქვემოთ მოცემული მასალით. კითხვები არ დამისვა.

<კვირა>
{{კვირა}}
</კვირა>

რა დავასახელე გასულ კვირას პრიორიტეტად: {{წინა_პრიორიტეტი}}

გამოსავალი — ზუსტად ეს ხუთი სექცია:

დასრულდა — რა მივიდა ბოლომდე. რაც 90%-ზეა, მიდის შემდეგ სექციაში.

არ დასრულდა — თითოეულ პუნქტზე ერთი ხაზი, რატომ. სადაც მიზეზი დავწერე, ჩემივე სიტყვები გამოიყენე; სადაც არა — დაწერე „მიზეზი არ დასახელებულა“.

სად წავიდა დრო — რეალური საათები {{წინა_პრიორიტეტი}}-სთან შედარებით. თუ ჩანაწერები ციფრის გამოთვლის საშუალებას იძლევა, დაწერე ციფრი; თუ არა — „ამ ჩანაწერებიდან ვერ იზომება“.

მეორდება — რაც უკვე არაერთხელ გამოჩნდა და ადგილიდან არ დაძრულა. დაასახელე პირდაპირ, ერთხელ.

შემდეგი კვირა — მაქსიმუმ 3 პრიორიტეტი. ყველაფერი წინ არ გადმოიტანო — ამოაგდე და დაწერე, რა ამოვარდა და რომ ეს განზრახ ხდება.

წესები:
- არ მაქო, არ გამამხნევო, არ შეარბილო
- არ დაამატო პუნქტი, რომელიც <კვირა>-ში არ არის
- ჩემს განწყობაზე არ იმსჯელო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.
```

---

### D-06 · Trip itinerary built around constraints
`claude` `gpt` — travel, planning

**EN**
```
Plan a trip as a schedule, not a brochure.

Where: {{destination}}
When: {{dates}} — {{days}} days
Who is going: {{travellers}}
Total budget: {{budget}}
Hard constraints: {{constraints}} — walking distance, food, children's bedtimes, no early starts, weather
The one thing that would make the trip worth it: {{must_have}}

Rules:
- MUST build each day around ONE anchor. NEVER more than two fixed commitments in a day.
- MUST state travel time between points and how we get there.
- MUST leave one unplanned half-day and say why it is there.
- MUST mark every item as "book before we go" or "decide on the day".
- NEVER state opening hours, prices or timetables as fact unless I gave them. Write "verify" instead.
- MUST stay inside {{budget}} and show the split: travel / accommodation / food / everything else.
- If {{must_have}} does not fit the days or the budget, say so in the first line before planning anything.

Output: day-by-day schedule · book before leaving · check on arrival · budget split.
```

**KA**
```
დაგეგმე მოგზაურობა როგორც განრიგი და არა როგორც სარეკლამო ბროშურა.

სად: {{მიმართულება}}
როდის: {{თარიღები}} — {{დღე}} დღე
ვინ მივდივართ: {{მგზავრები}}
სულ ბიუჯეტი: {{ბიუჯეტი}} ლარი
მკაცრი შეზღუდვები: {{შეზღუდვები}} — ფეხით სიარული, კვება, ბავშვის ძილის დრო, ადრე ადგომა, ამინდი
ერთი რამ, რის გამოც ეს მოგზაურობა ღირს: {{მთავარი}}

წესები:
- ყოველი დღე ერთი მთავარი პუნქტის გარშემო ააგე. დღეში ორზე მეტი ფიქსირებული საქმე არასდროს.
- დაწერე, რამდენი დრო სჭირდება ერთი ადგილიდან მეორეში მისვლას და რით მივდივართ
- დატოვე ერთი დაუგეგმავი ნახევარი დღე და დაწერე, რატომ
- ყოველ პუნქტს მიაწერე: „წინასწარ დასაჯავშნი“ თუ „ადგილზე გადასაწყვეტი“
- სამუშაო საათები, ფასები და გამგზავრების განრიგი ფაქტად არ დაწერო, თუ არ მოგეცი — დაწერე „ადგილზე გადაამოწმე“. ეს განსაკუთრებით ეხება მარშრუტკის განრიგს.
- უნდა ჩაეტიოს {{ბიუჯეტი}} ლარში. აჩვენე გადანაწილება: გზა / სადგომი / კვება / დანარჩენი.
- თუ {{მთავარი}} დღეებში ან ბიუჯეტში არ ეტევა, ეს პირველივე ხაზში დაწერე, სანამ რამეს დაგეგმავ

გამოსავალი: განრიგი დღეების მიხედვით · რა დავჯავშნოთ წინასწარ · რა გადავამოწმოთ ადგილზე · ბიუჯეტის გადანაწილება.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### D-07 · Understand an official document
`claude` `gpt` `gemini` — admin, contracts

**EN**
```
Explain this document to me in plain language. You are not my lawyer and MUST NOT tell me whether to sign it.

<document>
{{document}}
</document>

What I am trying to find out: {{question}}

Rules:
- MUST quote the exact clause before explaining it. NEVER explain without the quote.
- MUST turn every obligation into: who must do what, by when, and what happens if they do not.
- MUST collect every date, sum of money, notice period and automatic renewal into one list.
- MUST flag any clause that (a) lets the other side change the terms alone, (b) renews by itself, (c) charges a penalty or a fee, or (d) binds me after the agreement ends.
- Where the wording is genuinely ambiguous, write "ambiguous — could mean X or Y". NEVER pick one reading and present it as the meaning.
- NEVER say whether the terms are fair or normal, and NEVER give legal advice. Where a lawyer is needed, name the specific line and stop there.

Output: what this document does, in 3 sentences · dates and money · my obligations · their obligations · clauses to read again · questions to ask before signing.
```

**KA**
```
ამიხსენი ეს დოკუმენტი მარტივი ენით. შენ ჩემი იურისტი არ ხარ და არ მეტყვი, ხელი მოვაწერო თუ არა.

<დოკუმენტი>
{{დოკუმენტი}}
</დოკუმენტი>

რისი გარკვევა მინდა: {{კითხვა}}

წესები:
- ჯერ ზუსტად დაიმოწმე პუნქტი, მერე ახსენი. ციტატის გარეშე არაფერი ახსნა.
- ყოველი ვალდებულება გადათარგმნე ასე: ვინ, რა უნდა გააკეთოს, რა ვადაში და რა მოჰყვება შეუსრულებლობას
- ყველა თარიღი, თანხა, გაფრთხილების ვადა და ავტომატური გაგრძელება ერთ სიად შეკრიბე
- ცალკე გამოყავი პუნქტი, რომელიც: (ა) მეორე მხარეს ცალმხრივად ცვლილების უფლებას აძლევს, (ბ) თავისით გრძელდება, (გ) ჯარიმას ან საკომისიოს ითვალისწინებს, (დ) ხელშეკრულების დასრულების შემდეგაც მავალდებულებს
- სადაც ფორმულირება მართლაც ორაზროვანია, დაწერე „ორაზროვანია — შეიძლება ნიშნავდეს ერთს ან მეორეს“. ერთი წაკითხვა ერთადერთ მნიშვნელობად არ გაასაღო.
- არ თქვა, სამართლიანია თუ ჩვეულებრივი ეს პირობები, და იურიდიული რჩევა არ მომცე. სადაც იურისტია საჭირო, დაასახელე კონკრეტული პუნქტი და იქვე გაჩერდი.
- თუ დოკუმენტი უწყებას ეხება (მაგალითად, საჯარო რეესტრი ან RS.ge), დაასახელე, რომელ პუნქტზეა საჭირო იქ დაზუსტება

გამოსავალი: რას აკეთებს ეს დოკუმენტი — 3 წინადადება · თარიღები და თანხები · ჩემი ვალდებულებები · მათი ვალდებულებები · ხელახლა წასაკითხი პუნქტები · კითხვები ხელმოწერამდე.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### D-08 · Prepare for a hard conversation
`claude` `gpt` — relationships, communication

**EN**
```
Help me prepare for a conversation I am dreading.

Who: {{person}} — what they are to me: {{relationship}}
What I want to come out of it: {{outcome}}
What I think is going on: {{my_view}}
What has actually been said so far: {{history}}

Work in this order and NEVER change the order:

1. THEIR CASE — the strongest version of their position, written in first person as they would put it. Include anything in {{my_view}} they could fairly dispute. 80–120 words.
2. WHAT WE BOTH WANT — only what {{history}} supports. If there is nothing, write "nothing shared is evident yet".
3. MY OPENING — 2 sentences: one observable fact, one request. NEVER a diagnosis of them. NEVER "you always" or "you never".
4. THREE THINGS THEY MIGHT SAY — and for each, a reply that neither gives up {{outcome}} nor raises the temperature.
5. MY LINE — the one thing I am not trading away, in one sentence.

Rules:
- NEVER tell me who is right.
- NEVER guess at their feelings or motives beyond what {{history}} shows.
- NEVER suggest a script that depends on them reacting well.
```

**KA**
```
დამეხმარე იმ საუბრისთვის მომზადებაში, რომლისაც მეშინია.

ვისთან: {{ადამიანი}} — ვინ მეკუთვნის: {{ურთიერთობა}}
რა შედეგი მინდა: {{შედეგი}}
რა ხდება ჩემი აზრით: {{ჩემი_ხედვა}}
რა ითქვა აქამდე რეალურად: {{ისტორია}}

იმუშავე ამ თანმიმდევრობით და თანმიმდევრობა არ შეცვალო:

1. მისი მხარე — მისი პოზიციის ყველაზე ძლიერი ვერსია, პირველ პირში, ისე როგორც თავად იტყოდა. ჩართე ის, რასაც ჩემი ხედვიდან სამართლიანად გააპროტესტებდა. 80–120 სიტყვა.
2. რა გვინდა ორივეს — მხოლოდ ის, რასაც {{ისტორია}} ადასტურებს. თუ ასეთი არაფერია, დაწერე „საერთო ჯერ არ ჩანს“.
3. ჩემი პირველი ორი წინადადება — ერთი დაკვირვებადი ფაქტი და ერთი თხოვნა. მისი დახასიათება არასდროს. „შენ ყოველთვის“ ან „შენ არასდროს“ არასდროს.
4. სამი რამ, რაც მან შეიძლება თქვას — თითოზე პასუხი, რომელიც არც {{შედეგი}}-ს დათმობს და არც ვითარებას გაამწვავებს.
5. ჩემი ზღვარი — ერთი წინადადება იმაზე, რასაც არ დავთმობ.

წესები:
- არ მითხრა, ვინაა მართალი
- მის განცდებსა და მოტივებზე არ იფიქრო იმაზე მეტი, რასაც {{ისტორია}} აჩვენებს
- არ შემომთავაზო სცენარი, რომელიც მის კარგ რეაქციაზეა დამოკიდებული

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: შენობით.
```

---

### D-09 · Meals and shopping from what is in the fridge
`claude` `gpt` — home, budget

**EN**
```
Plan meals starting from what I already have.

In the fridge and cupboard: {{have}}
Budget for the top-up shop: {{budget}}
Days to cover: {{days}}, meals per day: {{meals}}
Who is eating, and anything they cannot eat: {{eaters}}
Cooking time I actually have on a weekday: {{weekday_minutes}} minutes
Equipment I have: {{equipment}}

Rules:
- MUST use {{have}} first, and MUST put the perishables in the first two days. Say which items are closest to going off.
- The shopping list MUST stay inside {{budget}} and be grouped by where I buy it, not alphabetically.
- MUST reuse ingredients across meals. NEVER a list where nine things are used once each.
- Weekday meals MUST fit {{weekday_minutes}}. Anything longer goes on a weekend.
- NEVER use an ingredient that is not in {{have}} or on the shopping list.
- NEVER give nutrition advice, calorie targets, or any comment on anyone's diet, weight or body.

Output: meals day by day · shopping list with rough prices and a total · what to cook once and eat twice.
```

**KA**
```
დაგეგმე კვება იმით, რაც უკვე სახლშია.

რა მაქვს მაცივარსა და კარადაში: {{მარაგი}}
დამატებით შესყიდვის ბიუჯეტი: {{ბიუჯეტი}} ლარი
რამდენ დღეზე: {{დღე}} დღე, დღეში {{კვება}} კვება
ვინ ჭამს და რა არ შეუძლია: {{ვინ_ჭამს}}
რამდენი წუთი მაქვს სამუშაო დღეს სამზარეულოში: {{წუთი}} წუთი
ტექნიკა: {{ტექნიკა}}

წესები:
- ჯერ {{მარაგი}} გამოიყენე, მალფუჭებადი პროდუქტი კი პირველ ორ დღეში ჩადე. დაასახელე, რომელი ფუჭდება ყველაზე ადრე.
- შესყიდვის სია უნდა ჩაეტიოს {{ბიუჯეტი}} ლარში და დაჯგუფდეს იმის მიხედვით, სად ვიყიდი — ბაზარი, სუპერმარკეტი, Glovo ან Wolt — და არა ანბანის მიხედვით
- ინგრედიენტები რამდენიმე კერძში გაიმეორე. სია, სადაც ცხრა პროდუქტი თითო-თითოჯერ გამოიყენება, არ გამოდგება.
- სამუშაო დღის კერძი {{წუთი}} წუთში უნდა ეტეოდეს. უფრო გრძელი შაბათ-კვირაზე გადაიტანე.
- არ გამოიყენო პროდუქტი, რომელიც არც {{მარაგი}}-შია და არც შესყიდვის სიაში
- არ მომცე რჩევა კვების, კალორიების, წონის ან სხეულის შესახებ

გამოსავალი: კერძები დღეების მიხედვით · შესყიდვის სია სავარაუდო ფასებით და ჯამით · რა მოვამზადო ერთხელ და ორჯერ ვჭამო.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### D-10 · Sort a backlog by consequence
`claude` `gpt` `gemini` — admin, triage

**EN**
```
Sort this backlog by what happens if I never do it.

<backlog>
{{backlog}}
</backlog>

Today is {{today}}. Hours I can give it this week: {{hours}}.

Put every item into exactly one bucket:

1. COSTS MONEY OR STANDING — a bill, a fine, a renewal, a document that expires. Name the consequence and the date.
2. SOMEONE IS WAITING — name who, and how long they have been waiting.
3. MATTERS TO ME, NOTHING BREAKS — no external deadline, no one waiting.
4. NOTHING HAPPENS — nobody is waiting and no cost accrues.

Rules:
- MUST put bucket 4 into a delete list and say plainly that it is being dropped. NEVER reschedule it.
- MUST mark anything in buckets 1 and 2 that takes under 5 minutes as "do now", and count how many there are.
- MUST NOT plan more than {{hours}} hours. What does not fit gets a named later date.
- NEVER promote an item because it feels urgent. Urgency with no consequence is bucket 3.
- If an item has no consequence stated and I did not give one, write "consequence unknown — check" rather than guessing.

Output: the four buckets · do-now list · this week inside {{hours}} hours · delete list.
```

**KA**
```
დაალაგე ეს დაგროვილი საქმეები იმის მიხედვით, რა მოხდება, თუ არასდროს გავაკეთებ.

<სია>
{{სია}}
</სია>

დღეს არის {{დღეს}}. ამ კვირაში ამაზე მაქვს {{საათი}} საათი.

ყოველი პუნქტი ჩასვი ზუსტად ერთ ჯგუფში:

1. ფული ან რეპუტაცია იკარგება — გადასახადი, ჯარიმა, ვადის გაგრძელება, ვადაგასული დოკუმენტი. დაასახელე შედეგი და თარიღი. აქვე ჩადე კომუნალური გადასახადები და RS.ge-ის ვადები.
2. ვიღაც ელოდება — დაასახელე ვინ და რამდენი ხანია.
3. ჩემთვის მნიშვნელოვანია, მაგრამ არაფერი ფუჭდება — გარე ვადა არ არის, არავინ ელოდება.
4. არაფერი მოხდება — არც ელოდება ვინმე, არც ხარჯი გროვდება.

წესები:
- მე-4 ჯგუფი ცალკე სიად გამოიტანე და პირდაპირ დაწერე, რომ ეს საქმეები ქრება. გადავადება არ შემომთავაზო.
- პირველ და მეორე ჯგუფში ის, რაც 5 წუთზე ნაკლებს მოითხოვს, მონიშნე როგორც „ახლავე“ და დათვალე, რამდენია
- {{საათი}} საათზე მეტი არ დაგეგმო. რაც არ ეტევა, კონკრეტულ მომავალ თარიღზე გადაიტანე.
- პუნქტი მხოლოდ იმიტომ არ აწიო მაღლა, რომ სასწრაფოდ გამოიყურება. სასწრაფოობა შედეგის გარეშე მესამე ჯგუფია.
- თუ შედეგი არ ჩანს და მე არ დამისახელებია, დაწერე „შედეგი უცნობია — გადასამოწმებელია“ და არ გამოიცნო

გამოსავალი: ოთხი ჯგუფი · „ახლავე“ სია · ეს კვირა {{საათი}} საათში · წასაშლელი სია.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### D-11 · What am I avoiding, and what would settle it
`claude` `gpt` — personal, reflection

**EN**
```
Read what I wrote below and tell me what I keep circling without landing on.

<notes>
{{notes}}
</notes>

Rules:
- MUST work only from the text. Quote the line that supports each observation.
- NEVER infer a motive, a diagnosis or an emotion the text does not state.
- Name at most 3 things that come up more than once and never get a next action.
- For each one, ask ONE question whose answer is a fact, not a feeling — "how much is actually left on it" rather than "how does that make you feel".
- For each one, name the smallest thing that would make it no longer avoidable: a number to look up, a message to send, a date to check, a document to open.
- NEVER reassure me, NEVER use therapy vocabulary, NEVER tell me what this "says about" me.
- If the notes point to something a doctor, a lawyer or an accountant should handle, name which one in a single line and go no further.

Output: three questions I have not answered · the fact each one needs · the smallest move for each.
```

**KA**
```
წაიკითხე ქვემოთ დაწერილი და მითხარი, რის გარშემო ვტრიალებ ისე, რომ ადგილიდან არ ვიძვრი.

<ჩანაწერები>
{{ჩანაწერები}}
</ჩანაწერები>

წესები:
- იმუშავე მხოლოდ ტექსტით. ყოველ დაკვირვებას მიაწერე ის ხაზი, რომელსაც ეყრდნობა.
- არ მიაწერო მოტივი, დიაგნოზი ან განცდა, რომელიც ტექსტში არ წერია
- დაასახელე მაქსიმუმ 3 რამ, რაც არაერთხელ ჩნდება და შემდეგ ნაბიჯამდე არასდროს მიდის
- თითოეულზე დამისვი ერთი კითხვა, რომლის პასუხიც ფაქტია და არა განცდა — „რამდენი დარჩა რეალურად“ და არა „რას განიცდი ამის გამო“
- თითოეულზე დაასახელე ყველაზე პატარა ნაბიჯი, რის შემდეგაც ამ საქმეს ვეღარ ავცდები: ციფრი, რომელიც უნდა ვნახო; წერილი, რომელიც უნდა გავგზავნო; თარიღი, რომელიც უნდა გადავამოწმო; დოკუმენტი, რომელიც უნდა გავხსნა
- არ დამამშვიდო, არ გამოიყენო ფსიქოლოგიური ლექსიკა და არ მითხრა, რას „ნიშნავს ეს ჩემზე“
- თუ ჩანაწერებში ისეთი რამაა, რასაც ექიმი, იურისტი ან ბუღალტერი უნდა შეხედოს, ერთ ხაზში დაასახელე რომელი და იქვე გაჩერდი

გამოსავალი: სამი კითხვა, რომელსაც პასუხი არ გავეცი · რა ფაქტი სჭირდება თითოეულს · ყველაზე პატარა ნაბიჯი თითოეულზე.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.
```

---

### D-12 · Ask for a better price
`claude` `gpt` — money, negotiation

**EN**
```
Help me ask for a better price without losing the deal.

What I pay now: {{current_price}} for {{thing}}
What I want to pay: {{target_price}}
How long I have been a customer or tenant: {{tenure}}
What I know about their alternatives: {{their_options}}
What I know about mine: {{my_options}}
The point at which I actually walk away: {{walkaway}}

Rules:
- MUST state in the first line whether I have real leverage here, based on {{my_options}} and {{their_options}}. If I do not, say so plainly and write a message that asks rather than pressures.
- MUST anchor the request in one verifiable thing: a price elsewhere, a cost I currently absorb, the length of the relationship, a condition they have not fixed.
- MUST offer something back that costs me less than the discount is worth — a longer commitment, paying earlier, fewer callouts, taking care of something myself.
- NEVER invent a competing offer I did not tell you I have.
- MUST tell me my walk-away number, but NEVER put it in the message.
- Message under 120 words.

Output: leverage, honestly · the message · what to say if they refuse · the number at which I stop.
```

**KA**
```
დამეხმარე ფასზე მოლაპარაკებაში ისე, რომ გარიგება არ ჩავშალო.

რას ვიხდი ახლა: {{ამჟამინდელი_ფასი}} ლარი — რაში: {{საგანი}}
რამდენი მინდა: {{სასურველი_ფასი}} ლარი
რამდენი ხანია ვარ კლიენტი ან მოიჯარე: {{ხანგრძლივობა}}
რა ვიცი მათ ალტერნატივებზე: {{მათი_ვარიანტები}}
რა ვიცი ჩემსაზე: {{ჩემი_ვარიანტები}}
რა ზღვარზე ვწყვეტ მოლაპარაკებას: {{ზღვარი}}

წესები:
- პირველივე ხაზში დაწერე, მაქვს თუ არა რეალური ბერკეტი — {{ჩემი_ვარიანტები}}-სა და {{მათი_ვარიანტები}}-ს მიხედვით. თუ არ მაქვს, ეს პირდაპირ დაწერე და წერილი თხოვნის ტონით დაწერე და არა ზეწოლის.
- მოთხოვნა დააყრდნობე ერთ გადამოწმებად რამეს: სხვაგან არსებულ ფასს, ხარჯს, რომელსაც ახლა მე ვიღებ თავზე, ურთიერთობის ხანგრძლივობას, ან გაუსწორებელ ხარვეზს. ბინის ქირის შემთხვევაში ცალკე გაითვალისწინე კომუნალური გადასახადები — ვინ იხდის რას.
- შესთავაზე სანაცვლოდ ის, რაც ფასდაკლებაზე იაფი დამიჯდება: უფრო გრძელი ვადა, წინასწარი გადახდა, ნაკლები გამოძახება, რაღაცის თავად მოგვარება
- არ მოიგონო კონკურენტის შეთავაზება, რომელიც არ დამისახელებია
- ჩემი ზღვარი მე დამისახელე, მაგრამ წერილში არასდროს ჩაწერო
- წერილი 120 სიტყვამდე

წერილი დაწერე თქვენობით — ადრესატი მეპატრონე ან კომპანიაა.
დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: მაქვს თუ არა ბერკეტი, პატიოსნად · წერილი · რა ვთქვა უარის შემთხვევაში · ციფრი, რომელზეც ვჩერდები.
```

---

### D-13 · Turn a vague worry into a checkable question
`claude` `gpt` `gemini` — personal, decisions

**EN**
```
Turn a worry into something I can actually check.

The worry, in my own words: {{worry}}
What I have already checked: {{checked}}

Do this:
1. Restate the worry as a claim that can be true or false. If it contains more than one, split them and number them.
2. For each claim: what observation would show it is true, and what observation would show it is false. If nothing could show it false, say so — that is the finding, and stop working on that claim.
3. For each claim: the cheapest source that settles it — a document I already have, a number on a statement, one question to one named person — and how long it takes.
4. Say which single check removes the most uncertainty, and what I would do differently depending on the answer. If the answer would change nothing I do, say that plainly.

Rules:
- NEVER reassure me and NEVER tell me it will be fine.
- NEVER give a probability you cannot support from what I wrote.
- If the worry is medical, legal or financial, name the professional who settles it instead of settling it yourself.
- Under 300 words.
```

**KA**
```
გადააქციე ბუნდოვანი შიში იმად, რისი გადამოწმებაც შემიძლია.

შიში, ჩემი სიტყვებით: {{შიში}}
რა უკვე გადავამოწმე: {{გადამოწმებული}}

გააკეთე ეს:
1. ჩამოაყალიბე ეს შიში მტკიცებად, რომელიც ან მართალია ან მცდარი. თუ ერთზე მეტია, დაყავი და დაანომრე.
2. თითოეულზე დაწერე: რა დაკვირვება დაადასტურებდა და რა დაკვირვება უარყოფდა. თუ ვერაფერი უარყოფს, ეს პირდაპირ დაწერე — ესეც შედეგია და ამ პუნქტზე მუშაობა შეწყვიტე.
3. თითოეულზე დაასახელე ყველაზე იაფი წყარო, რომელიც საკითხს დახურავს — დოკუმენტი, რომელიც უკვე მაქვს; ციფრი ამონაწერში; ერთი კითხვა ერთი კონკრეტული ადამიანისთვის — და რამდენი დრო სჭირდება.
4. დაასახელე ერთი შემოწმება, რომელიც ყველაზე მეტ გაურკვევლობას ხსნის, და რას გავაკეთებდი სხვანაირად პასუხის მიხედვით. თუ პასუხი ჩემს მოქმედებას არაფერში ცვლის, ესეც პირდაპირ დაწერე.

წესები:
- არ დამამშვიდო და არ მითხრა, რომ ყველაფერი კარგად იქნება
- არ დაასახელო ალბათობა, რომელსაც ჩემი ტექსტით ვერ დაასაბუთებ
- თუ საკითხი სამედიცინო, იურიდიული ან ფინანსურია, დაასახელე შესაბამისი სპეციალისტი და თავად ნუ გადაწყვეტ
- 300 სიტყვამდე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.
```
