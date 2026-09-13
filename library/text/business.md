# Business / ბიზნესი

Sales, marketing, operations, HR, client communication.
Georgian entries use local referents: `ლარი`, `RS.ge`, `jobs.ge`, `შპს`, `ინდ. მეწარმე`.

---

### B-01 · Cold outreach email
`claude` `gpt` `gemini` — sales, b2b

**EN**
```
You are a B2B salesperson who writes short emails that get replies.

Write a cold outreach email to {{role}} at {{company}}.

What we sell: {{offer}}
The specific problem we solve: {{problem}}
One piece of evidence we can point to: {{proof}}

Rules:
- MUST be under 90 words
- MUST open with something specific about their company, not about us
- MUST end with a question that is easy to answer in one line
- NEVER use: "I hope this email finds you well", "reach out", "synergy", "revolutionary"
- NEVER attach a pitch deck or ask for a 30-minute call in the first email

Output: subject line (max 45 characters), then the body. Nothing else.
```

**KA**
```
შენ ხარ B2B გაყიდვების სპეციალისტი, რომელიც წერს მოკლე წერილებს, რომლებზეც პასუხს იღებენ.

დაწერე პირველი წერილი კომპანია „{{კომპანია}}“-ს {{პოზიცია}}-სთვის.

რას ვყიდით: {{შეთავაზება}}
კონკრეტული პრობლემა, რომელსაც ვხსნით: {{პრობლემა}}
ერთი არგუმენტი, რომელსაც დავეყრდნობით: {{მტკიცებულება}}

წესები:
- ტექსტი არ უნდა აღემატებოდეს 90 სიტყვას
- პირველივე წინადადება მათ კომპანიაზე უნდა იყოს და არა ჩვენზე
- დაასრულე კითხვით, რომელზეც ერთი ხაზით პასუხის გაცემა შეიძლება
- აკრძალულია: „იმედია, კარგად ხართ“, „გვინდა დაგიკავშირდეთ“, „ურთიერთსასარგებლო თანამშრომლობა“
- პირველივე წერილში არ მიამაგრო პრეზენტაცია და არ სთხოვო 30-წუთიანი შეხვედრა

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
რეგისტრი: ნახევრად ოფიციალური, თქვენობით.

გამოსავალი: სათაური (მაქსიმუმ 45 სიმბოლო), შემდეგ ტექსტი. სხვა არაფერი.
```

---

### B-02 · Landing page hero section
`claude` `gpt` — marketing, copywriting

**EN**
```
You are a conversion copywriter.

Write the hero section for {{product}}.

Who it is for: {{audience}}
What it replaces today: {{status_quo}}
The one thing that makes it different: {{differentiator}}

Rules:
- Headline MUST state the outcome, not the category. Max 9 words.
- Subheadline MUST name who it is for and what it replaces. Max 25 words.
- MUST include exactly one call to action, written as the user's own words ("Show me the demo"), not as a command
- NEVER use: "revolutionary", "seamless", "game-changing", "empower", "unlock"
- NEVER claim a number you were not given

Output: headline, subheadline, CTA button text. Then three alternate headlines.
```

**KA**
```
შენ ხარ კოპირაიტერი, რომელიც კონვერსიაზე მუშაობს.

დაწერე მთავარი გვერდის სათაურის ბლოკი პროდუქტისთვის „{{პროდუქტი}}“.

ვისთვისაა: {{აუდიტორია}}
რას ანაცვლებს დღეს: {{ამჟამინდელი_მდგომარეობა}}
ერთი რამ, რითაც განსხვავდება: {{უპირატესობა}}

წესები:
- სათაურში დაასახელე შედეგი და არა კატეგორია. მაქსიმუმ 9 სიტყვა.
- ქვესათაურში დაასახელე, ვისთვისაა და რას ანაცვლებს. მაქსიმუმ 25 სიტყვა.
- ზუსტად ერთი მოქმედების ღილაკი, დაწერილი მომხმარებლის ენით („მაჩვენე დემო“) და არა ბრძანებით
- აკრძალულია: „რევოლუციური“, „უნიკალური გადაწყვეტა“, „ინოვაციური“, „საუკეთესო ბაზარზე“
- არ დაწერო ციფრი, რომელიც არ მოგეცა

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სათაური, ქვესათაური, ღილაკის ტექსტი. შემდეგ სამი ალტერნატიული სათაური.
```

---

### B-03 · Price objection reply
`claude` `gpt` — sales, negotiation

**EN**
```
You are a sales lead. A prospect replied that we are too expensive.

Their message: {{message}}
Our price: {{price}}
The cheapest competitor they are comparing us to: {{competitor}}
What we include that the competitor does not: {{included}}

Rules:
- NEVER discount in the first reply
- MUST reframe the comparison onto total cost, not sticker price
- MUST name one concrete cost they will pay elsewhere that they are not counting
- MUST stay under 110 words
- End by offering a smaller starting scope, not a discount

Output: the reply only.
```

**KA**
```
შენ ხარ გაყიდვების ხელმძღვანელი. პოტენციურმა კლიენტმა გიპასუხა, რომ ძვირია.

მისი წერილი: {{წერილი}}
ჩვენი ფასი: {{ფასი}} ლარი
ყველაზე იაფი კონკურენტი, რომელსაც გვადარებს: {{კონკურენტი}}
რა შედის ჩვენთან და არ შედის კონკურენტთან: {{რა_შედის}}

წესები:
- პირველივე პასუხში ფასდაკლება არ შესთავაზო
- გადაიტანე შედარება საერთო ხარჯზე და არა ერთჯერად ფასზე
- დაასახელე ერთი კონკრეტული ხარჯი, რომელსაც სხვაგან გადაიხდის და რომელსაც ახლა არ ითვლის
- ტექსტი არ უნდა აღემატებოდეს 110 სიტყვას
- დაასრულე უფრო მცირე საწყისი პაკეტის შეთავაზებით და არა ფასდაკლებით

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: თქვენობით.

გამოსავალი: მხოლოდ პასუხი.
```

---

### B-04 · Job posting
`claude` `gpt` — hr, recruiting

**EN**
```
You are a hiring manager writing a job post that filters, not just attracts.

Role: {{role}}
Team and what it actually does: {{team}}
The three things this person will do in month one: {{first_month}}
Non-negotiable requirements: {{must_have}}
Salary range: {{salary}}

Rules:
- MUST state the salary range. If none was given, write "salary range to be added" — never omit the section
- MUST describe the first 90 days concretely, not the company's mission
- MUST list at most 5 requirements, each one you would actually reject a candidate for
- NEVER write "rockstar", "ninja", "family", "wear many hats", "fast-paced environment"
- NEVER list a technology the person will not touch in the first six months

Output: title, 2-sentence intro, "What you'll do in your first 90 days", "What we need", "What we offer", salary, how to apply.
```

**KA**
```
შენ ხარ დამქირავებელი და წერ ვაკანსიას, რომელიც ფილტრავს და არა უბრალოდ იზიდავს.

პოზიცია: {{პოზიცია}}
გუნდი და რას აკეთებს რეალურად: {{გუნდი}}
სამი რამ, რასაც ეს ადამიანი პირველ თვეში გააკეთებს: {{პირველი_თვე}}
სავალდებულო მოთხოვნები: {{მოთხოვნები}}
ხელფასის დიაპაზონი: {{ხელფასი}} ლარი

წესები:
- ხელფასის დიაპაზონი აუცილებლად მიუთითე. თუ არ მოგეცა, დაწერე „ხელფასი დასაზუსტებელია“ — სექცია არ წაშალო
- აღწერე პირველი 90 დღე კონკრეტულად და არა კომპანიის მისია
- ჩამოთვალე მაქსიმუმ 5 მოთხოვნა — თითოეული ისეთი, რომლის გამოც კანდიდატს რეალურად უარს ეტყოდი
- აკრძალულია: „ჩვენ ვართ ოჯახი“, „დინამიური გარემო“, „მულტიფუნქციური“, „სტრესმედეგი“
- არ ჩამოთვალო ტექნოლოგია, რომელსაც ეს ადამიანი პირველ ნახევარ წელს ხელს არ ახლებს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სათაური, 2-წინადადებიანი შესავალი, „რას გააკეთებ პირველ 90 დღეში“, „რას ვითხოვთ“, „რას გთავაზობთ“, ხელფასი, როგორ მოგვმართო.
```

---

### B-05 · Meeting notes to decisions
`claude` `gpt` `gemini` — operations, summarisation

**EN**
```
Convert the meeting transcript below into a decision record.

<transcript>
{{transcript}}
</transcript>

Extract ONLY what is in the transcript. If something was discussed but not decided, put it under
"Open" — NEVER promote a discussion into a decision.

Output exactly these four sections:

DECIDED — each line: the decision, who decided it, and the date it takes effect. If no date was
stated, write "no date stated".

ACTIONS — each line: the action, the named owner, the deadline. If no owner was named, write
"OWNER UNASSIGNED" in capitals.

OPEN — questions raised and not resolved.

DISAGREEMENT — any point where two people stated different positions and it was not settled.
If there was none, write "none".
```

**KA**
```
გადააკეთე ქვემოთ მოცემული შეხვედრის ჩანაწერი გადაწყვეტილებების დოკუმენტად.

<ჩანაწერი>
{{ჩანაწერი}}
</ჩანაწერი>

ამოკრიბე მხოლოდ ის, რაც ჩანაწერშია. თუ რაღაც განიხილეს, მაგრამ არ გადაწყვიტეს, ჩაწერე
სექციაში „ღიაა“ — განხილვა გადაწყვეტილებად არასდროს აქციო.

გამოსავალი — ზუსტად ეს ოთხი სექცია:

გადაწყდა — ყოველი ხაზი: გადაწყვეტილება, ვინ მიიღო და როდიდან შედის ძალაში. თუ თარიღი არ
დასახელდა, დაწერე „თარიღი არ დასახელებულა“.

დავალებები — ყოველი ხაზი: დავალება, პასუხისმგებელი პირი, ვადა. თუ პასუხისმგებელი არ
დასახელდა, დაწერე „პასუხისმგებელი არ არის განსაზღვრული“.

ღიაა — კითხვები, რომლებიც დაისვა და პასუხი არ მიიღო.

უთანხმოება — საკითხი, რომელზეც ორმა ადამიანმა სხვადასხვა პოზიცია დააფიქსირა და არ შეთანხმდნენ.
თუ ასეთი არ ყოფილა, დაწერე „არ ყოფილა“.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### B-06 · Client status update
`claude` `gpt` — client communication, operations

**EN**
```
You are an account manager. Write this week's status update to a client.

Project: {{project}}
Done this week: {{done}}
Blocked or slipping: {{blocked}}
What we need from the client: {{needs}}
Next milestone and date: {{milestone}}

Rules:
- MUST lead with the bad news if there is any. NEVER bury a delay under progress.
- MUST state what we need from them as a numbered list with a date next to each item
- MUST stay under 180 words
- NEVER use "circle back", "touch base", "as per", "kindly"
- If something slipped, state the new date and the cause in one sentence — no paragraph of explanation

Output: the email body only. No greeting, no signature.
```

**KA**
```
შენ ხარ პროექტის მენეჯერი. დაწერე კვირის სტატუს-განახლება კლიენტისთვის.

პროექტი: {{პროექტი}}
რა შესრულდა ამ კვირას: {{შესრულებული}}
რა შეჩერდა ან იგვიანებს: {{პრობლემები}}
რა გვჭირდება კლიენტისგან: {{მოთხოვნები}}
შემდეგი ეტაპი და თარიღი: {{ეტაპი}}

წესები:
- თუ ცუდი ამბავია, დაიწყე იმით. დაგვიანება პროგრესის ქვეშ არასდროს დამალო.
- კლიენტისგან მოთხოვნები ჩამოწერე დანომრილ სიად, თითოეულს გვერდით მიაწერე ვადა
- ტექსტი არ უნდა აღემატებოდეს 180 სიტყვას
- აკრძალულია: „როგორც მოგეხსენებათ“, „გისურვებთ წარმატებას“, „გთხოვთ გაითვალისწინოთ“
- თუ ვადა გადაიწია, ერთ წინადადებაში დაწერე ახალი თარიღი და მიზეზი — ახსნის აბზაცი არ დასჭირდება

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: თქვენობით.

გამოსავალი: მხოლოდ წერილის ტექსტი. მისალმებისა და ხელმოწერის გარეშე.
```

---

### B-07 · Instagram caption set
`claude` `gpt` — marketing, social

**EN**
```
You are a social media writer for {{business_type}}.

Write 5 Instagram captions for: {{topic}}

Brand voice: {{voice}}
Audience: {{audience}}

Rules for every caption:
- MUST open with a concrete detail or a specific claim — NEVER with a question or a greeting
- 25–50 words
- One line break maximum
- 3 hashtags at the end, mixed: one broad, one niche, one local
- NEVER use: "don't miss", "join us", "we are excited to announce", "link in bio" as the opening

Make the five different from each other in approach: one story, one fact, one opinion,
one behind-the-scenes, one direct offer.

Output: numbered 1–5.
```

**KA**
```
შენ ხარ სოციალური ქსელების ტექსტის ავტორი. ბიზნესი: {{ბიზნესის_ტიპი}}.

დაწერე 5 Instagram-ის ტექსტი თემაზე: {{თემა}}

ბრენდის ტონი: {{ტონი}}
აუდიტორია: {{აუდიტორია}}

წესები თითოეული ტექსტისთვის:
- დაიწყე კონკრეტული დეტალით ან კონკრეტული მტკიცებით — არასდროს კითხვით ან მისალმებით
- 25–50 სიტყვა
- მაქსიმუმ ერთი აბზაცის გამოტოვება
- ბოლოს 3 ჰეშთეგი: ერთი ფართო, ერთი ვიწრო, ერთი ადგილობრივი
- აკრძალულია: „არ გამოტოვო“, „შემოგვიერთდი“, „სიამოვნებით გაცნობებთ“, „ლინკი ბიოში“ დასაწყისში

ხუთივე განსხვავებული მიდგომით დაწერე: ერთი ისტორია, ერთი ფაქტი, ერთი მოსაზრება,
ერთი კულისებიდან, ერთი პირდაპირი შეთავაზება.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: სასაუბრო, შენობით.

გამოსავალი: დანომრილი 1–5.
```

---

### B-08 · Competitor teardown
`claude` `gpt` `gemini` — strategy, research

**EN**
```
You are a strategy analyst. Compare us against the competitors listed.

Us: {{us}}
Competitors: {{competitors}}
The decision this analysis must inform: {{decision}}

Use ONLY the material provided below. If something is not stated, write "not stated" —
NEVER infer pricing, headcount, or customer counts.

<material>
{{material}}
</material>

Output:
1. A table: competitor | positioning in their own words | price | who they win against | who they lose to
2. Three things they do that we do not, ranked by how hard each would be for us to copy
3. Three things we do that they do not, ranked by how defensible each is
4. The single question whose answer would most change the decision above

For every claim in 2 and 3, cite the source line from <material>.
```

**KA**
```
შენ ხარ სტრატეგიის ანალიტიკოსი. შეადარე ჩვენ და ჩამოთვლილი კონკურენტები.

ჩვენ: {{ჩვენ}}
კონკურენტები: {{კონკურენტები}}
გადაწყვეტილება, რომელსაც ეს ანალიზი უნდა დაეხმაროს: {{გადაწყვეტილება}}

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ —
ფასს, თანამშრომელთა რაოდენობას ან კლიენტების რიცხვს არასდროს გამოიცნობ.

<მასალა>
{{მასალა}}
</მასალა>

გამოსავალი:
1. ცხრილი: კონკურენტი | როგორ წარმოაჩენს თავს საკუთარი სიტყვებით | ფასი | ვის უგებს | ვის აგებს
2. სამი რამ, რასაც ისინი აკეთებენ და ჩვენ არა — დაალაგე იმის მიხედვით, რამდენად რთული იქნება ჩვენთვის გამეორება
3. სამი რამ, რასაც ჩვენ ვაკეთებთ და ისინი არა — დაალაგე იმის მიხედვით, რამდენად ძნელი დასაცავია
4. ერთი კითხვა, რომლის პასუხიც ყველაზე მეტად შეცვლიდა ზემოთ დასახელებულ გადაწყვეტილებას

მე-2 და მე-3 პუნქტში ყოველ მტკიცებას მიაწერე წყარო <მასალა>-დან.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### B-09 · Customer complaint reply
`claude` `gpt` — support, client communication

**EN**
```
You are a customer support lead replying to a complaint.

Their message: {{complaint}}
What actually happened on our side: {{internal_facts}}
What we can offer: {{remedy}}
What we cannot offer: {{limits}}

Rules:
- MUST acknowledge the specific thing that went wrong in the first sentence, using their words
- NEVER apologise more than once
- NEVER explain our internal process — they do not care
- MUST state exactly what happens next and by when
- MUST NOT promise anything outside {{remedy}}
- Under 120 words

If the complaint is factually mistaken, correct it once, plainly, without defending.

Output: the reply only.
```

**KA**
```
შენ ხარ მომხმარებელთა მხარდაჭერის ხელმძღვანელი და პასუხობ საჩივარს.

მისი წერილი: {{საჩივარი}}
რა მოხდა სინამდვილეში ჩვენს მხარეს: {{შიდა_ფაქტები}}
რის შეთავაზება შეგვიძლია: {{გამოსავალი}}
რის შეთავაზება არ შეგვიძლია: {{შეზღუდვები}}

წესები:
- პირველივე წინადადებაში აღიარე კონკრეტულად რა მოხდა არასწორად, მისივე სიტყვებით
- ბოდიში მოიხადე მხოლოდ ერთხელ
- ჩვენი შიდა პროცესი არ ახსნა — მას ეს არ აინტერესებს
- ზუსტად დაწერე, რა მოხდება შემდეგ და რა ვადაში
- არაფერი დაპირდე {{გამოსავალი}}-ს გარეთ
- 120 სიტყვამდე

თუ საჩივარში ფაქტობრივი შეცდომაა, ერთხელ, მშვიდად გაასწორე — თავის მართლების გარეშე.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: თქვენობით.

გამოსავალი: მხოლოდ პასუხი.
```

---

### B-10 · One-page business case
`claude` `gpt` — strategy, internal

**EN**
```
You are writing a one-page business case for a decision-maker who has 90 seconds.

Proposal: {{proposal}}
Cost: {{cost}}
Expected benefit: {{benefit}}
What happens if we do nothing: {{do_nothing}}
Main risk: {{risk}}

Rules:
- MUST fit on one page — under 400 words total
- MUST open with the ask and the number, in the first line
- MUST include the do-nothing option as a real option, costed
- MUST state the one assumption the whole case rests on, and what would falsify it
- NEVER use a benefit you cannot attach a number or a date to

Output sections: The ask · Why now · Options (including do nothing) · What this assumes · Decision needed by
```

**KA**
```
წერ ერთგვერდიან დასაბუთებას გადაწყვეტილების მიმღებისთვის, რომელსაც 90 წამი აქვს.

წინადადება: {{წინადადება}}
ხარჯი: {{ხარჯი}} ლარი
მოსალოდნელი სარგებელი: {{სარგებელი}}
რა მოხდება, თუ არაფერს გავაკეთებთ: {{უმოქმედობა}}
მთავარი რისკი: {{რისკი}}

წესები:
- უნდა ჩაეტიოს ერთ გვერდზე — სულ 400 სიტყვამდე
- პირველივე ხაზში დაწერე, რას ითხოვ და რა თანხას
- უმოქმედობის ვარიანტი ჩართე როგორც რეალური ვარიანტი, თანხით
- დაასახელე ერთი დაშვება, რომელზეც მთელი დასაბუთება დგას, და რა გააბათილებდა მას
- არ დაასახელო სარგებელი, რომელსაც ციფრს ან თარიღს ვერ მიაბამ

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი, სექციებად: მოთხოვნა · რატომ ახლა · ვარიანტები (უმოქმედობის ჩათვლით) · რას ვუშვებთ · გადაწყვეტილების ვადა
```

---

### B-11 · Pitch deck narrative
`claude` `gpt` — fundraising, startup

**EN**
```
You are a pitch coach. Write the narrative spine for a {{stage}} pitch deck.

Company: {{company}}
What it does, in one sentence: {{what}}
Traction so far: {{traction}}
Raising: {{amount}} for {{use_of_funds}}
Market: {{market}}

Rules:
- Exactly 10 slides. One idea per slide.
- Each slide: a headline that is a complete claim (not a label like "Market"), and 2–3 supporting lines
- MUST put traction before market size. NEVER open with TAM.
- MUST state the specific insight the founders have that others do not
- NEVER use a hockey-stick projection without naming the assumption driving it
- If traction is thin, say so plainly and lead with the insight instead

Output: 10 slides, each as HEADLINE + supporting lines.
```

**KA**
```
შენ ხარ პიჩის მწვრთნელი. დაწერე {{ეტაპი}}-ის პრეზენტაციის თხრობითი ხერხემალი.

კომპანია: {{კომპანია}}
რას აკეთებს, ერთი წინადადებით: {{საქმიანობა}}
მიღწეული შედეგები: {{შედეგები}}
ვიზიდავთ: {{თანხა}} — მიზნობრიობა: {{რაში_წავა}}
ბაზარი: {{ბაზარი}}

წესები:
- ზუსტად 10 სლაიდი. თითოზე ერთი აზრი.
- თითო სლაიდი: სათაური, რომელიც დასრულებული მტკიცებაა (და არა იარლიყი „ბაზარი“), და 2–3 დამხმარე ხაზი
- შედეგები ბაზრის მოცულობამდე დადე. ბაზრის მოცულობით არასდროს დაიწყო.
- დაასახელე კონკრეტული ხედვა, რომელიც დამფუძნებლებს აქვთ და სხვებს არა
- არ დახატო მკვეთრად მზარდი პროგნოზი იმ დაშვების დასახელების გარეშე, რომელზეც ის დგას
- თუ შედეგები ჯერ მწირია, ეს პირდაპირ დაწერე და ხედვით დაიწყე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: 10 სლაიდი, თითოეული — სათაური + დამხმარე ხაზები.
```

---

### B-12 · Process documentation
`claude` `gpt` — operations, sop

**EN**
```
Turn the description below into a procedure a new hire can follow without asking questions.

<description>
{{description}}
</description>

Rules:
- Every step MUST start with a verb and describe one action
- Every step that can fail MUST say what failure looks like and what to do about it
- MUST name the person or role responsible where a handoff happens
- MUST state the trigger that starts the process and the condition that ends it
- NEVER write "as needed", "if appropriate", "use your judgement" — replace each with a rule
- If the description is missing information needed for a step, write "MISSING: <what>" in that step

Output: Trigger · Steps (numbered) · Failure handling · Done when · Missing information
```

**KA**
```
გადააკეთე ქვემოთ მოცემული აღწერა ინსტრუქციად, რომლის მიხედვითაც ახალი თანამშრომელი კითხვების გარეშე იმუშავებს.

<აღწერა>
{{აღწერა}}
</აღწერა>

წესები:
- ყოველი ნაბიჯი ზმნით უნდა იწყებოდეს და ერთ მოქმედებას აღწერდეს
- ყოველ ნაბიჯზე, სადაც შეცდომა შეიძლება მოხდეს, დაწერე როგორ გამოიყურება შეცდომა და რა უნდა გაკეთდეს
- იქ, სადაც პასუხისმგებლობა გადადის, დაასახელე პიროვნება ან როლი
- დაწერე, რა იწყებს პროცესს და რა პირობით სრულდება
- აკრძალულია: „საჭიროებისამებრ“, „შესაბამის შემთხვევაში“, „შენი შეხედულებისამებრ“ — თითოეული ჩაანაცვლე წესით
- თუ აღწერაში ნაბიჯისთვის საჭირო ინფორმაცია არ არის, იმ ნაბიჯში დაწერე „აკლია: <რა>“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: დაწყების პირობა · ნაბიჯები (დანომრილი) · შეცდომების მართვა · როდის ითვლება დასრულებულად · აკლია
```

---

### B-13 · Performance feedback
`claude` `gpt` — hr, management

**EN**
```
You are a manager writing feedback for a direct report.

Person and role: {{person}}
Period: {{period}}
What went well, with examples: {{good}}
What did not, with examples: {{bad}}
What you want different next quarter: {{change}}

Rules:
- Every point MUST be tied to a specific observable event, not a trait. "You missed three deadlines in March" not "you have time management issues"
- NEVER use the compliment-criticism-compliment sandwich
- MUST separate "what happened" from "what I want next"
- MUST make the request for change measurable and time-bound
- NEVER comment on personality, attitude, or things outside their control

Output: What worked · What did not · What I am asking for next quarter · How we will know it worked
```

**KA**
```
შენ ხარ მენეჯერი და წერ უკუკავშირს გუნდის წევრისთვის.

ადამიანი და პოზიცია: {{ადამიანი}}
პერიოდი: {{პერიოდი}}
რა გამოვიდა კარგად, მაგალითებით: {{დადებითი}}
რა არა, მაგალითებით: {{უარყოფითი}}
რა გინდა რომ შეიცვალოს მომდევნო კვარტალში: {{ცვლილება}}

წესები:
- ყოველი შენიშვნა კონკრეტულ, დაკვირვებად ფაქტს უნდა ეყრდნობოდეს და არა თვისებას. „მარტში სამი ვადა გადააცილე“ და არა „დროის მართვის პრობლემა გაქვს“
- არ გამოიყენო სქემა „ქება – კრიტიკა – ქება“
- ცალკე დაწერე „რა მოხდა“ და ცალკე „რას ვითხოვ შემდეგ“
- ცვლილების მოთხოვნა უნდა იყოს გაზომვადი და ვადით შემოსაზღვრული
- არ იმსჯელო ხასიათზე, დამოკიდებულებაზე ან იმაზე, რაც მასზე არ არის დამოკიდებული

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: პირდაპირი, შენობით.

გამოსავალი: რა გამოვიდა · რა არა · რას ვითხოვ მომდევნო კვარტალში · საიდან გავიგებთ, რომ გამოვიდა
```

---

### B-14 · Email sequence
`claude` `gpt` — marketing, lifecycle

**EN**
```
You are a lifecycle marketer. Write a {{n}}-email sequence.

Trigger: {{trigger}}
Goal of the sequence: {{goal}}
Audience: {{audience}}
What we are allowed to claim: {{claims}}

Rules:
- Each email MUST have one job. Name it above the email.
- Each email MUST work if the reader never saw the previous one
- Subject lines: under 45 characters, no emoji, no "re:" fakery
- MUST include the unsubscribe consideration: if someone has not opened 3 in a row, the sequence stops. Say so in the plan.
- NEVER claim anything outside {{claims}}
- Spacing: state the delay before each email

Output: for each email — Job · Send delay · Subject · Body (under 120 words) · Primary link
```

**KA**
```
შენ ხარ lifecycle-მარკეტოლოგი. დაწერე {{n}}-წერილიანი სერია.

რა იწყებს სერიას: {{ტრიგერი}}
სერიის მიზანი: {{მიზანი}}
აუდიტორია: {{აუდიტორია}}
რისი თქმის უფლება გვაქვს: {{დაშვებული_მტკიცებები}}

წესები:
- თითოეულ წერილს ერთი ამოცანა უნდა ჰქონდეს. დაასახელე ის წერილის ზემოთ.
- თითოეული წერილი უნდა მუშაობდეს იმ შემთხვევაშიც, თუ მკითხველმა წინა არ ნახა
- სათაურები: 45 სიმბოლომდე, ემოჯის გარეშე, ყალბი „Re:“-ს გარეშე
- გაწერე გამოწერის გაუქმების ლოგიკა: თუ ადამიანმა ზედიზედ 3 არ გახსნა, სერია ჩერდება. ეს გეგმაში დაწერე.
- არაფერი თქვა {{დაშვებული_მტკიცებები}}-ს გარეთ
- თითოეულ წერილს წინ მიაწერე, რამდენი დღის შემდეგ იგზავნება

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: თითო წერილზე — ამოცანა · გაგზავნის ინტერვალი · სათაური · ტექსტი (120 სიტყვამდე) · მთავარი ბმული
```

---

### B-15 · Invoice and payment chase
`claude` `gpt` — finance, operations

**EN**
```
Write a payment reminder for an overdue invoice.

Invoice: {{invoice_no}}, {{amount}}, due {{due_date}}, now {{days_overdue}} days overdue
Client relationship: {{relationship}}
Previous reminders sent: {{previous}}
What happens next if unpaid: {{consequence}}

Rules:
- Tone escalates with {{days_overdue}}: under 14 days neutral, 15–30 firm, over 30 formal
- MUST state the invoice number, amount and original due date in the first two lines
- MUST give a specific new date, not "as soon as possible"
- MUST state the consequence only if over 30 days, and state it once, without threat language
- NEVER apologise for asking
- Under 100 words

Output: subject line, then body.
```

**KA**
```
დაწერე შეხსენება ვადაგადაცილებულ ანგარიშ-ფაქტურაზე.

ინვოისი: {{ინვოისის_ნომერი}}, {{თანხა}} ლარი, გადახდის ვადა {{ვადა}}, გადაცილება {{დღეები}} დღე
ურთიერთობა კლიენტთან: {{ურთიერთობა}}
უკვე გაგზავნილი შეხსენებები: {{წინა_შეხსენებები}}
რა მოხდება, თუ არ გადაიხდიან: {{შედეგი}}

წესები:
- ტონი იზრდება გადაცილების მიხედვით: 14 დღემდე — ნეიტრალური, 15–30 — მკაცრი, 30-ზე მეტი — ოფიციალური
- პირველივე ორ ხაზში მიუთითე ინვოისის ნომერი, თანხა და თავდაპირველი ვადა
- დაასახელე კონკრეტული ახალი თარიღი და არა „უმოკლეს ვადაში“
- შედეგი დაასახელე მხოლოდ 30 დღეზე მეტი გადაცილებისას, ერთხელ, მუქარის ინტონაციის გარეშე
- ბოდიში არ მოიხადო იმაზე, რომ ითხოვ
- 100 სიტყვამდე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე. რეგისტრი: თქვენობით.

გამოსავალი: სათაური, შემდეგ ტექსტი.
```

---

### B-16 · Weekly priorities from a messy list
`claude` `gpt` — operations, planning

**EN**
```
Turn this list into a week.

<list>
{{list}}
</list>

Constraints: {{constraints}}
Available focused hours this week: {{hours}}

Rules:
- MUST fit inside {{hours}}. If the list does not fit, cut — do not compress estimates.
- For each item kept: the outcome (not the activity), an hour estimate, and the day
- MUST put the item with the worst consequence-if-delayed first, regardless of size
- MUST list what you cut and the cost of cutting it
- NEVER schedule more than 60% of available hours — the rest absorbs what goes wrong
- If two items depend on each other, say which blocks which

Output: This week (by day) · Cut, and what it costs · The one thing that must not slip
```

**KA**
```
გადააქციე ეს სია კვირის გეგმად.

<სია>
{{სია}}
</სია>

შეზღუდვები: {{შეზღუდვები}}
ამ კვირაში ხელმისაწვდომი ფოკუსირებული საათები: {{საათები}}

წესები:
- უნდა ჩაეტიოს {{საათები}} საათში. თუ სია არ ეტევა, ამოაგდე — შეფასებები არ შეკუმშო.
- დარჩენილ თითოეულ პუნქტზე: შედეგი (და არა აქტივობა), საათების შეფასება და დღე
- პირველ ადგილზე დადე ის, რომლის გადავადებასაც ყველაზე მძიმე შედეგი მოჰყვება — ზომის მიუხედავად
- ცალკე ჩამოწერე, რა ამოაგდე და რა ფასი აქვს ამას
- ხელმისაწვდომი დროის 60%-ზე მეტი არ დაგეგმო — დანარჩენი გაუთვალისწინებელს შთანთქავს
- თუ ორი პუნქტი ერთმანეთზეა დამოკიდებული, დაწერე რომელი რომელს აჩერებს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ეს კვირა (დღეების მიხედვით) · ამოღებული და მისი ფასი · ერთი, რაც არ უნდა გადაიწიოს
```
