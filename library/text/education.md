# Education / განათლება

Lesson planning, explanation, assessment, grading, feedback, study habits.
Georgian entries use local referents: `ეროვნული გამოცდები`, `სკოლის ატესტატი`, `საბაზო/საშუალო საფეხური`, `სემესტრი`, `მაგისტრატურა`.

---

### E-01 · Lesson plan from one objective
`claude` `gpt` `gemini` — teaching, planning

**EN**
```
You are a teacher planning a single lesson built around one objective.

Learning objective: {{objective}}
Level and grade: {{level}}
Lesson length: {{minutes}} minutes
Class size and constraints: {{constraints}}
What students already know: {{prior_knowledge}}

Rules:
- MUST plan exactly {{minutes}} minutes. Put a duration on every segment and make the durations sum to {{minutes}}.
- MUST place one check for understanding before the halfway point, and write out the exact question you will ask
- MUST state what you do next if that check shows most of the class is lost
- NEVER list an activity without naming what the student produces during it
- NEVER introduce an objective other than {{objective}}
- Materials: only what a teacher already has in the room or can print

Output: Objective in student words · Segments (time | teacher does | student does | evidence of learning) · Mid-lesson check + recovery plan · Closing question (1) · Materials
```

**KA**
```
შენ ხარ მასწავლებელი და გეგმავ ერთ გაკვეთილს, რომელიც ერთ მიზანზეა აგებული.

სასწავლო მიზანი: {{მიზანი}}
საფეხური და კლასი: {{კლასი}}
გაკვეთილის ხანგრძლივობა: {{წუთი}} წუთი
მოსწავლეთა რაოდენობა და შეზღუდვები: {{შეზღუდვები}}
რა იციან მოსწავლეებმა უკვე: {{წინარე_ცოდნა}}

წესები:
- გაკვეთილი ზუსტად {{წუთი}} წუთზე გაწერე. ყოველ ეტაპს მიაწერე ხანგრძლივობა და ჯამი {{წუთი}} წუთს უნდა დაემთხვეს.
- გაკვეთილის შუამდე ჩადე ცოდნის შემოწმების ერთი წერტილი და სრულად ჩაწერე ის კითხვა, რომელსაც დასვამ
- დაწერე, რას გააკეთებ, თუ ეს შემოწმება აჩვენებს, რომ კლასის უმეტესობას თემა არ გაუგია
- არ ჩაწერო აქტივობა, რომლის ბოლოსაც მოსწავლე კონკრეტულ შედეგს არ აწარმოებს
- {{მიზანი}}-ს გარდა სხვა მიზანი არ შემოიტანო
- მასალებში მხოლოდ ის ჩაწერე, რაც მასწავლებელს უკვე აქვს ან ამობეჭდვა შეუძლია

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: მიზანი მოსწავლის ენაზე · ეტაპები (დრო | რას აკეთებს მასწავლებელი | რას აკეთებს მოსწავლე | რით დასტურდება) · შუალედური შემოწმება და სარეზერვო გეგმა · დასკვნითი კითხვა (1) · მასალები
```

---

### E-02 · One concept, three difficulty levels
`claude` `gpt` `gemini` — explanation, tutoring

**EN**
```
Explain {{concept}} three times, for three different levels.

Subject: {{subject}}
Why the learner is asking: {{context}}

Levels:
1. A 10-year-old — max 80 words, one everyday analogy, zero technical terms
2. A student meeting it for the first time in class — max 150 words, define every term at first mention
3. Someone who already knows the basics — max 150 words, focus on the part people get wrong and why

Rules:
- The analogy in level 1 MUST break somewhere. State where it breaks, in one line under it.
- NEVER repeat the same sentence across two levels
- NEVER use "simply", "just", "obviously", "of course"
- If {{concept}} is routinely confused with something else, name that other thing in level 3

Output: three blocks, labelled 1, 2, 3. Nothing else.
```

**KA**
```
ახსენი {{თემა}} სამჯერ, სამი სხვადასხვა დონისთვის.

საგანი: {{საგანი}}
რატომ ეკითხება ადამიანი: {{კონტექსტი}}

დონეები:
1. 10 წლის ბავშვისთვის — მაქსიმუმ 80 სიტყვა, ერთი ყოფითი ანალოგია, ტერმინების გარეშე
2. მოსწავლისთვის, რომელიც ამ თემას გაკვეთილზე პირველად ხვდება — მაქსიმუმ 150 სიტყვა, ყოველი ტერმინი პირველივე ხსენებისას ახსენი
3. ადამიანისთვის, რომელმაც საფუძვლები უკვე იცის — მაქსიმუმ 150 სიტყვა, ყურადღება იმ ადგილს დაუთმე, სადაც ყველაზე ხშირად ცდებიან, და ახსენი რატომ

წესები:
- პირველი დონის ანალოგია სადღაც აუცილებლად ირღვევა — ქვემოთ ერთი ხაზით დაწერე, სად
- ერთი და იგივე წინადადება ორ დონეზე არ გაიმეორო
- აკრძალულია: „უბრალოდ“, „ცხადია“, „რა თქმა უნდა“, „მარტივად რომ ვთქვათ“
- თუ {{თემა}} ხშირად ერევათ სხვა ცნებაში, მესამე დონეზე ეს ცნება დაასახელე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სამი ბლოკი, დანომრილი 1, 2, 3. სხვა არაფერი.
```

---

### E-03 · Quiz with answer key and distractor rationale
`claude` `gpt` `gemini` — assessment, testing

**EN**
```
You are an assessment writer. Build a quiz on {{topic}}.

Level: {{level}}
Number of questions: {{n}}
Material the students studied:
<source>
{{source}}
</source>

Rules:
- MUST build every question from <source> only. NEVER test something the source does not cover.
- Mix: 60% recall and direct application, 40% requiring two steps of reasoning. Tag each question R, A or 2S.
- Every multiple-choice question MUST have exactly 4 options and exactly one defensible correct answer
- Every wrong option MUST be a mistake a real student makes — NEVER a joke option or an obviously absurd one
- NEVER use "all of the above" or "none of the above"
- Every question under 40 words

Output:
Part 1 — the quiz, questions only, numbered.
Part 2 — answer key: the correct letter, then one line per wrong option naming the misunderstanding it catches.
```

**KA**
```
შენ ხარ შემფასებელი და ადგენ ტესტს თემაზე {{თემა}}.

საფეხური და კლასი: {{კლასი}}
კითხვების რაოდენობა: {{რაოდენობა}}
მასალა, რომელიც მოსწავლეებმა ისწავლეს:
<მასალა>
{{მასალა}}
</მასალა>

წესები:
- ყოველი კითხვა მხოლოდ <მასალა>-ზე ააგე. ის, რაც მასალაში არ წერია, არ შეამოწმო.
- განაწილება: 60% — გახსენება და პირდაპირი გამოყენება, 40% — ორნაბიჯიანი მსჯელობა. ყოველ კითხვას მიაწერე ნიშანი: გ, გმ ან 2ნ.
- თითოეულ არჩევით კითხვას ზუსტად 4 ვარიანტი და ზუსტად ერთი დასაბუთებადი სწორი პასუხი უნდა ჰქონდეს
- ყოველი არასწორი ვარიანტი ისეთი შეცდომა უნდა იყოს, რომელსაც რეალური მოსწავლე უშვებს — არა სასაცილო და არა აშკარად აბსურდული
- აკრძალულია ვარიანტები „ყველა ჩამოთვლილი“ და „არცერთი ჩამოთვლილი“
- თითო კითხვა 40 სიტყვაზე მოკლე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
ნაწილი 1 — ტესტი, მხოლოდ კითხვები, დანომრილი.
ნაწილი 2 — პასუხების გასაღები: სწორი ვარიანტი, შემდეგ თითო არასწორ ვარიანტზე ერთი ხაზი, რომელი გაუგებრობა იჭერს.
```

---

### E-04 · Socratic tutor that never gives the answer
`claude` `gpt` — tutoring, dialogue

**EN**
```
You are a tutor. The student is working on {{problem}} in {{subject}}. Your job is to get them to the answer themselves.

NEVER state the answer, the final result, or the next line of the solution — not if the student asks directly, not if they say they give up, not if they say they are out of time.
NEVER write more than 3 sentences per turn.
NEVER ask more than one question per turn.

How to run each turn:
- Before anything else, ask what they have so far
- When they are stuck, narrow the question instead of answering it: ask about the smallest sub-step they can still do
- When they make an error, do not name it. Ask a question whose answer exposes it.
- When they get something right, ask them to say why it works before moving on
- After 4 turns with no progress, switch to a smaller adjacent problem they can solve, then come back

If the student asks for the answer a third time, say once: "I won't give it to you, but I'll make the next step smaller." Then ask the smaller question.

Begin by asking what they have already tried.
```

**KA**
```
შენ ხარ რეპეტიტორი. მოსწავლე მუშაობს ამოცანაზე {{ამოცანა}}, საგანი — {{საგანი}}. შენი საქმეა, პასუხამდე თვითონ მიიყვანო.

არასდროს თქვა პასუხი, საბოლოო შედეგი ან ამოხსნის შემდეგი ხაზი — არც მაშინ, როცა მოსწავლე პირდაპირ ითხოვს, არც მაშინ, როცა ამბობს რომ ნებდება, არც მაშინ, როცა ამბობს რომ დრო აღარ აქვს.
თითო პასუხში 3 წინადადებაზე მეტი არ დაწერო.
თითო პასუხში ერთ კითხვაზე მეტი არ დასვა.

როგორ წარმართო თითოეული ნაბიჯი:
- პირველ რიგში ჰკითხე, სადამდე მივიდა
- როცა ჩიხშია, კითხვა დაავიწროვე და არ უპასუხო: ჰკითხე ყველაზე პატარა ნაბიჯზე, რომლის გაკეთებაც ჯერ კიდევ შეუძლია
- როცა შეცდომას უშვებს, შეცდომა არ დაასახელო. დასვი კითხვა, რომლის პასუხიც თვითონ გამოააშკარავებს მას.
- როცა სწორად პასუხობს, გადასვლამდე ჰკითხე, რატომ მუშაობს ეს
- თუ 4 ნაბიჯის შემდეგ წინსვლა არ არის, გადადი უფრო პატარა, მონათესავე ამოცანაზე, რომელსაც ამოხსნის, მერე დაუბრუნდი ძირითადს

თუ მოსწავლე მესამედ ითხოვს პასუხს, ერთხელ უთხარი: „პასუხს არ გეტყვი, სამაგიეროდ შემდეგ ნაბიჯს პატარას გავხდი“. შემდეგ დასვი უფრო მცირე კითხვა.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: სასაუბრო, შენობით.

დაიწყე კითხვით, უკვე რა სცადა.
```

---

### E-05 · Grade an essay against a rubric
`claude` `gpt` `gemini` — assessment, grading

**EN**
```
Grade the student essay below against the rubric below. Grade the essay that was written, not the essay you would have written.

<rubric>
{{rubric}}
</rubric>

<essay>
{{essay}}
</essay>

Rules:
- MUST score every criterion in <rubric> and no criterion outside it
- Every score MUST be justified by an exact quotation from <essay>, max 20 words
- If the essay does not attempt a criterion, give the lowest score and write "not attempted" — NEVER guess at intent
- NEVER lower a score for spelling or style unless <rubric> has a criterion for it
- NEVER rewrite the student's sentences inside your comments
- Comments to the student: exactly 3, each naming one change that would raise one named criterion

Output: table (criterion | score | quotation) · total · the 3 comments · the one thing to fix first.
```

**KA**
```
შეაფასე ქვემოთ მოცემული მოსწავლის ესე მოცემული რუბრიკით. შეაფასე ის ესე, რომელიც დაიწერა და არა ის, რომელსაც შენ დაწერდი.

<რუბრიკა>
{{რუბრიკა}}
</რუბრიკა>

<ესე>
{{ესე}}
</ესე>

წესები:
- ქულა დაუწერე რუბრიკის ყოველ კრიტერიუმს და მხოლოდ მათ
- ყოველი ქულა დაასაბუთე ესედან ზუსტი ციტატით, მაქსიმუმ 20 სიტყვა
- თუ ესეში კრიტერიუმზე მუშაობა საერთოდ არ ჩანს, დაწერე ყველაზე დაბალი ქულა და მიაწერე „არ არის შესრულებული“ — ავტორის განზრახვა არ გამოიცნო
- ორთოგრაფიისა და სტილის გამო ქულა არ ჩამოაკლო, თუ რუბრიკაში ამის კრიტერიუმი არ არის
- კომენტარებში მოსწავლის წინადადებები არ გადაწერო
- კომენტარი მოსწავლისთვის: ზუსტად 3, თითოეულში ერთი ცვლილება, რომელიც ერთ კონკრეტულ კრიტერიუმზე ქულას აწევს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ცხრილი (კრიტერიუმი | ქულა | ციტატა) · ჯამური ქულა · 3 კომენტარი · ერთი, რაც პირველ რიგში უნდა გამოსწორდეს.
```

---

### E-06 · Write the rubric itself
`claude` `gpt` — assessment, rubric

**EN**
```
Build a grading rubric for {{assignment}}.

Subject and level: {{level}}
What the assignment must prove the student can do: {{objective}}
Total points: {{points}}

Rules:
- MUST have 4 to 6 criteria, each traceable directly to {{objective}}
- MUST use 4 performance levels described by what is observable in the work — NEVER by adverbs like "excellent", "good", "weak"
- Every level description MUST contain something countable or checkable: how many sources, whether a counter-argument appears, whether every claim carries evidence
- Points MUST sum to exactly {{points}}, with the most weight on the criterion closest to {{objective}}
- NEVER include effort, neatness, or participation as a criterion
- Add one student-facing line per criterion: "you have done this well if…"

Output: the rubric table · the student-facing lines · one sentence on which criterion two graders will disagree about most, and the rule that settles it.
```

**KA**
```
შეადგინე შეფასების რუბრიკა დავალებისთვის {{დავალება}}.

საგანი და საფეხური: {{კლასი}}
რა უნდა დაამტკიცოს ამ დავალებამ მოსწავლეზე: {{მიზანი}}
ჯამური ქულა: {{ქულა}}

წესები:
- 4-დან 6-მდე კრიტერიუმი, თითოეული პირდაპირ {{მიზანი}}-დან გამომდინარე
- 4 დონე, აღწერილი იმით, რაც ნაშრომში თვალით ჩანს — და არა ზედსართავებით „შესანიშნავი“, „კარგი“, „სუსტი“
- ყოველი დონის აღწერაში ჩადე რაღაც დათვლადი ან შესამოწმებელი: რამდენი წყაროა, არის თუ არა საპირისპირო არგუმენტი, ახლავს თუ არა ყოველ მტკიცებას მტკიცებულება
- ქულების ჯამი ზუსტად {{ქულა}} უნდა იყოს; ყველაზე დიდი წონა იმ კრიტერიუმს მიეცი, რომელიც {{მიზანი}}-სთან ყველაზე ახლოსაა
- კრიტერიუმად არ ჩასვა ძალისხმევა, მოწესრიგებულობა ან გაკვეთილზე აქტიურობა
- თითო კრიტერიუმს მიაწერე ერთი ხაზი მოსწავლისთვის: „ეს კარგად გაქვს გაკეთებული, თუ…“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: რუბრიკის ცხრილი · მოსწავლისთვის განკუთვნილი ხაზები · ერთი წინადადება იმაზე, რომელ კრიტერიუმზე შეიძლება ორმა შემფასებელმა ყველაზე მეტად ვერ შეთანხმდეს და რა წესით გადაწყდება ეს.
```

---

### E-07 · Misconception diagnosis from a wrong answer
`claude` `gpt` `gemini` — diagnosis, teaching

**EN**
```
A student gave a wrong answer. Work out what they were thinking.

Subject: {{subject}} · Level: {{level}}
The question: {{question}}
Correct answer: {{correct}}
Student's answer: {{student_answer}}
Their working, if any: {{working}}

Rules:
- MUST give the 3 most likely misconceptions that produce exactly this answer, ranked by likelihood
- For each: state the rule the student is applying, then show that rule producing this exact wrong answer
- MUST give one diagnostic question per misconception whose answer separates it from the other two
- NEVER call it a careless mistake unless you can show that no consistent rule produces this answer
- NEVER recommend re-teaching the whole topic

Output: ranked list of 3 (misconception · the rule they are using · how it produces this answer · the question that confirms it) · then the first sentence to say to the student.
```

**KA**
```
მოსწავლემ არასწორი პასუხი გასცა. გაარკვიე, როგორ ფიქრობდა.

საგანი: {{საგანი}} · საფეხური და კლასი: {{კლასი}}
კითხვა: {{კითხვა}}
სწორი პასუხი: {{სწორი_პასუხი}}
მოსწავლის პასუხი: {{მოსწავლის_პასუხი}}
მისი ამონახსნი, თუ არსებობს: {{ამონახსნი}}

წესები:
- დაასახელე 3 ყველაზე სავარაუდო მცდარი წარმოდგენა, რომელიც ზუსტად ამ პასუხს იძლევა, და დაალაგე ალბათობის მიხედვით
- თითოეულზე: დაწერე, რომელ წესს იყენებს მოსწავლე, და აჩვენე, როგორ გამოაქვს ამ წესს სწორედ ეს არასწორი პასუხი
- თითო მცდარ წარმოდგენაზე დასვი ერთი შემამოწმებელი კითხვა, რომლის პასუხიც მას დანარჩენი ორისგან გამოარჩევს
- „უყურადღებობით დაშვებული შეცდომა“ არ დაწერო, თუ ვერ აჩვენებ, რომ ამ პასუხს ვერცერთი თანმიმდევრული წესი ვერ ხსნის
- მთელი თემის თავიდან ახსნა არ შემოგთავაზო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: 3 პუნქტი თანმიმდევრობით (მცდარი წარმოდგენა · რომელ წესს იყენებს · როგორ იძლევა ამ პასუხს · რომელი კითხვა დაადასტურებს) · შემდეგ პირველი წინადადება, რომელსაც მოსწავლეს ეტყვი.
```

---

### E-08 · Worked example plus faded practice
`claude` `gpt` — instruction design, practice

**EN**
```
Build a worked example and a faded practice set for {{skill}}.

Level: {{level}}
Practice items: 5

Rules:
- Start with one fully worked example: every step shown, and next to each step a short reason saying why that step was chosen — not what it does
- Then 5 items that fade the support: item 1 shows all steps but the last, item 2 shows the first half, item 3 shows only the first step, items 4 and 5 show the problem alone
- All 5 items MUST exercise the same skill. NEVER make the content harder while you are removing the support.
- MUST include one item where the obvious first move is wrong, and explain in the key why it is wrong
- NEVER place an answer next to its item — all answers go at the end

Output: Worked example · Items 1–5 · Answer key with one line per item on what the teacher should check.
```

**KA**
```
შეადგინე ამოხსნილი ნიმუში და თანდათან გამარტივებული სავარჯიშოების ნაკრები უნარისთვის {{უნარი}}.

საფეხური და კლასი: {{კლასი}}
სავარჯიშოების რაოდენობა: 5

წესები:
- დაიწყე ერთი სრულად ამოხსნილი ნიმუშით: ყველა ნაბიჯი ჩანს და თითოეულს გვერდით მიწერილი აქვს მოკლე მიზეზი, რატომ აირჩია სწორედ ეს ნაბიჯი — და არა რას აკეთებს ეს ნაბიჯი
- შემდეგ 5 სავარჯიშო, სადაც დახმარება თანდათან იკლებს: პირველში ყველა ნაბიჯია ბოლოს გარდა, მეორეში — პირველი ნახევარი, მესამეში — მხოლოდ პირველი ნაბიჯი, მეოთხესა და მეხუთეში მხოლოდ პირობაა
- ხუთივე სავარჯიშო ერთსა და იმავე უნარს უნდა ავარჯიშებდეს. დახმარების მოხსნისას შინაარსი არ გაართულო.
- ჩადე ერთი სავარჯიშო, რომელშიც აშკარა პირველი ნაბიჯი არასწორია, და გასაღებში ახსენი რატომ
- პასუხი სავარჯიშოს გვერდით არ დადო — ყველა პასუხი ბოლოში

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ამოხსნილი ნიმუში · სავარჯიშოები 1–5 · პასუხების გასაღები, თითო სავარჯიშოზე ერთი ხაზი იმაზე, რას უნდა მიაქციოს მასწავლებელმა ყურადღება.
```

---

### E-09 · Study plan from a syllabus and an exam date
`claude` `gpt` `gemini` — study planning, exams

**EN**
```
Build a study plan from a syllabus and a fixed exam date.

<syllabus>
{{syllabus}}
</syllabus>

Exam date: {{exam_date}} · Today: {{today}}
Hours available per week: {{hours}}
Topics the student already finds hard: {{weak_topics}}

Rules:
- MUST fit inside {{hours}} per week, and MUST leave the final 20% of the calendar for review only — no new material there
- MUST schedule every topic in <syllabus> at least twice, with at least 7 days between the two passes
- MUST give every topic in {{weak_topics}} three passes instead of two, with the first one early
- Every session MUST end with a self-test, never with reading
- NEVER put more than 2 hours on one topic in one session
- If the material does not fit the time available, say so in the first line and name which topics drop to one pass

Output: week-by-week table (week | topics | session tasks | self-test) · what was cut and what it costs · the checkpoint date by which the student must know whether they are behind.
```

**KA**
```
შეადგინე მომზადების გეგმა პროგრამისა და გამოცდის ფიქსირებული თარიღის მიხედვით.

<პროგრამა>
{{პროგრამა}}
</პროგრამა>

გამოცდა (ეროვნული გამოცდები, სემესტრული ან საკლასო): {{გამოცდა}}
გამოცდის თარიღი: {{გამოცდის_თარიღი}} · დღევანდელი თარიღი: {{დღეს}}
კვირაში ხელმისაწვდომი საათი: {{საათი}}
თემები, რომლებიც მოსწავლეს უჭირს: {{სუსტი_თემები}}

წესები:
- გეგმა კვირაში {{საათი}} საათში უნდა ჩაეტიოს, ბოლო 20% კი მხოლოდ გამეორებას დაუტოვე — იქ ახალი მასალა არ შემოიტანო
- პროგრამის ყოველი თემა სულ მცირე ორჯერ დაგეგმე, ორ გავლას შორის მინიმუმ 7 დღე
- {{სუსტი_თემები}}-ს ორის ნაცვლად სამი გავლა დაუთმე და პირველი ადრე ჩადე
- ყოველი სესია თვითშემოწმებით უნდა მთავრდებოდეს და არა კითხვით
- ერთ სესიაზე ერთ თემას 2 საათზე მეტი არ დაუთმო
- თუ მასალა არსებულ დროში არ ეტევა, პირველივე ხაზში ეს დაწერე და დაასახელე, რომელი თემა რჩება ერთი გავლით

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ცხრილი კვირების მიხედვით (კვირა | თემები | სესიის დავალებები | თვითშემოწმება) · რა ამოვარდა და რა ფასი აქვს ამას · საკონტროლო თარიღი, რომლამდეც მოსწავლემ უნდა გაიგოს, ჩამორჩება თუ არა.
```

---

### E-10 · Lecture transcript to student notes
`claude` `gpt` `gemini` — notes, summarisation

**EN**
```
Turn the lecture transcript below into notes a student who missed the class can study from.

<transcript>
{{transcript}}
</transcript>

Rules:
- Use ONLY what is in <transcript>. If the lecturer left something incomplete, keep it incomplete and mark it "[unclear in the lecture]" — NEVER fill the gap from your own knowledge.
- MUST separate four things: what was defined, what was claimed, what was an example, what was an aside
- MUST keep every number, date, name and formula exactly as spoken
- MUST mark anything the lecturer flagged as exam-relevant with "EXAM"
- NEVER keep filler, repetition, or digressions
- Max 600 words

Output: Topic · Definitions · Main points in the order taught · Examples · Marked EXAM · Questions to ask the lecturer.
```

**KA**
```
გადააკეთე ქვემოთ მოცემული ლექციის ჩანაწერი ისეთ ჩანაწერებად, რომლითაც გაცდენილი სტუდენტი მოემზადება.

<ჩანაწერი>
{{ჩანაწერი}}
</ჩანაწერი>

წესები:
- გამოიყენე მხოლოდ ის, რაც ჩანაწერშია. თუ ლექტორმა რამე ბოლომდე არ თქვა, დაუმთავრებლადვე დატოვე და მიაწერე „ლექციაზე ბოლომდე არ ითქვა“ — შენი ცოდნით ხარვეზი არ შეავსო.
- ერთმანეთისგან გამიჯნე ოთხი რამ: რა განისაზღვრა, რა მტკიცება გაკეთდა, რა იყო მაგალითი და რა — გვერდითი შენიშვნა
- ყოველი ციფრი, თარიღი, სახელი და ფორმულა ზუსტად ისე დატოვე, როგორც ითქვა
- ის, რაც ლექტორმა გამოცდისთვის მნიშვნელოვნად დაასახელა, მონიშნე სიტყვით „გამოცდა“
- სიტყვა-პარაზიტები, გამეორებები და თემიდან გადახვევები ამოაგდე
- მაქსიმუმ 600 სიტყვა

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: თემა · განმარტებები · ძირითადი დებულებები სწავლების თანმიმდევრობით · მაგალითები · მონიშნული „გამოცდა“ · კითხვები ლექტორისთვის.
```

---

### E-11 · One task, three ability levels
`claude` `gpt` — differentiation, classroom

**EN**
```
Take one classroom task and produce three versions of it.

The task: {{task}}
Subject and level: {{level}}
The objective all three versions must still meet: {{objective}}

Versions:
- Support: for students who cannot start without help
- Core: the task as written
- Extension: for students who will finish early

Rules:
- All three MUST assess {{objective}}. NEVER give the support version a smaller objective — change the scaffolding, not the goal.
- The support version MUST add structure: a partly completed table, a sentence starter, a first item done for them. NEVER just fewer questions of the same kind.
- The extension MUST demand a different kind of thinking — justify, compare, find the flaw. NEVER more items of the same type.
- All three MUST take the same amount of class time
- NEVER name the versions in a way students can rank; name them by what they contain

Output: the three versions in full, ready to hand out, plus one line each on what you will look at to know it worked.
```

**KA**
```
აიღე ერთი საკლასო დავალება და გააკეთე მისი სამი ვარიანტი.

დავალება: {{დავალება}}
საგანი და საფეხური: {{კლასი}}
მიზანი, რომელსაც სამივე ვარიანტი უნდა პასუხობდეს: {{მიზანი}}

ვარიანტები:
- დამხმარე: მოსწავლისთვის, რომელიც დახმარების გარეშე ვერ იწყებს
- ძირითადი: დავალება ისე, როგორც არის
- გაფართოებული: მოსწავლისთვის, რომელიც ადრე დაასრულებს

წესები:
- სამივე ვარიანტი {{მიზანი}}-ს უნდა ამოწმებდეს. დამხმარე ვარიანტს მიზანი არ შეუმცირო — შეცვალე დასაყრდენი და არა მიზანი.
- დამხმარე ვარიანტში სტრუქტურა დაამატე: ნაწილობრივ შევსებული ცხრილი, წინადადების დასაწყისი, პირველი პუნქტი უკვე გაკეთებული. იმავე ტიპის კითხვების უბრალოდ შემცირება არ გამოდგება.
- გაფართოებული ვარიანტი სხვა ტიპის აზროვნებას უნდა ითხოვდეს — დაასაბუთე, შეადარე, იპოვე ხარვეზი. იმავე ტიპის დამატებითი პუნქტები არ ივარგებს.
- სამივე ვარიანტს გაკვეთილის ერთნაირი დრო უნდა სჭირდებოდეს
- ვარიანტებს ისეთი სახელი არ დაარქვა, რომლითაც მოსწავლეები ერთმანეთს დაახარისხებენ; დაასახელე შინაარსის მიხედვით

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სამივე ვარიანტი სრულად, დასარიგებლად მზად, და თითოეულზე ერთი ხაზი იმაზე, რას დააკვირდები, რომ გაიგო — გამოვიდა თუ არა.
```

---

### E-12 · Specific, actionable feedback on student work
`claude` `gpt` `gemini` — feedback, teaching

**EN**
```
Write feedback on a piece of student work.

Subject and level: {{level}}
What the task asked for: {{task}}
The work:
<work>
{{work}}
</work>

Rules:
- MUST name exactly 2 things that work and exactly 2 to change — no more, no fewer
- Every point MUST point at a specific place in <work>, by quotation or by line. NEVER a general judgement about the student.
- Every "change" point MUST say what to do, not what is wrong — an instruction the student can carry out in one sitting
- NEVER comment on ability, effort, or neatness
- NEVER rewrite the work for them. At most, show the change on one sentence as a demonstration.
- Under 200 words, addressed to the student

Output: What works · What to change · The one thing to do before the next submission.
```

**KA**
```
დაწერე უკუკავშირი მოსწავლის ნაშრომზე.

საგანი და საფეხური: {{კლასი}}
რას ითხოვდა დავალება: {{დავალება}}
ნაშრომი:
<ნაშრომი>
{{ნაშრომი}}
</ნაშრომი>

წესები:
- დაასახელე ზუსტად 2 რამ, რაც გამოვიდა, და ზუსტად 2, რაც უნდა შეიცვალოს — არც მეტი, არც ნაკლები
- ყოველი შენიშვნა ნაშრომის კონკრეტულ ადგილს უნდა უთითებდეს — ციტატით ან ხაზის მითითებით. ზოგადი შეფასება მოსწავლეზე არ დაწერო.
- ყოველ შესაცვლელ პუნქტში დაწერე, რა გააკეთოს და არა რა არის ცუდად — მითითება, რომელსაც ერთ ჯდომაზე შეასრულებს
- არ იმსჯელო ნიჭზე, ძალისხმევაზე ან მოწესრიგებულობაზე
- ნაშრომი მის ნაცვლად არ გადაწერო. მაქსიმუმ ერთ წინადადებაზე აჩვენე, როგორ გამოიყურება ცვლილება.
- 200 სიტყვამდე, პირდაპირ მოსწავლისადმი მიმართვით

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: სასაუბრო, შენობით.

გამოსავალი: რა გამოვიდა · რა უნდა შეიცვალოს · ერთი, რაც შემდეგ ჩაბარებამდე უნდა გააკეთოს.
```

---

### E-13 · Spaced-repetition cards from source material
`claude` `gpt` `gemini` — memorisation, revision

**EN**
```
Turn the source below into spaced-repetition cards.

<source>
{{source}}
</source>

Subject: {{subject}} · Number of cards: {{n}}

Rules:
- One fact per card. If a card needs the word "and", split it.
- The front MUST be answerable without seeing any other card. NEVER write "this term", "the above", "as mentioned".
- The back MUST be under 15 words
- NEVER make a card out of something the learner only has to recognise; make it out of what they must produce from memory
- Where a card has a direction (term → meaning), MUST also give the reverse card when the reverse is genuinely worth knowing, and MUST skip it when it is not — list what you skipped and why
- MUST include 3 cards that test application, phrased as a small problem rather than a lookup
- Every card MUST come from <source> only

Output: numbered cards as FRONT / BACK, then 2 lines on which parts of <source> you deliberately did not turn into cards.
```

**KA**
```
გადააკეთე ქვემოთ მოცემული მასალა გამეორების ბარათებად.

<მასალა>
{{მასალა}}
</მასალა>

საგანი: {{საგანი}} · ბარათების რაოდენობა: {{რაოდენობა}}

წესები:
- თითო ბარათზე ერთი ფაქტი. თუ ბარათს „და“ სჭირდება, ორად გაყავი.
- წინა მხარეს პასუხის გაცემა სხვა ბარათის ნახვის გარეშე უნდა შეიძლებოდეს. არასდროს დაწერო „ეს ტერმინი“, „ზემოთ მოცემული“, „უკვე ნახსენები“.
- უკანა მხარე 15 სიტყვაზე მოკლე
- ბარათი არ გააკეთო იმაზე, რაც მოსწავლეს მხოლოდ უნდა ამოიცნოს; გააკეთე იმაზე, რაც მეხსიერებიდან უნდა აღადგინოს
- როცა ბარათს მიმართულება აქვს (ტერმინი → მნიშვნელობა), გააკეთე შებრუნებული ბარათიც იქ, სადაც შებრუნებული მართლა სასარგებლოა, და არ გააკეთო იქ, სადაც არა — ჩამოწერე, რომელი გამოტოვე და რატომ
- ჩადე 3 ბარათი, რომელიც ცოდნის გამოყენებას ამოწმებს და პატარა ამოცანადაა ჩამოყალიბებული და არა ცნობარის კითხვად
- ყოველი ბარათი მხოლოდ <მასალა>-ზე უნდა დგებოდეს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: დანომრილი ბარათები ფორმატით წინა მხარე / უკანა მხარე, შემდეგ 2 ხაზი იმაზე, მასალის რომელი ნაწილი განზრახ არ აქციე ბარათად.
```
