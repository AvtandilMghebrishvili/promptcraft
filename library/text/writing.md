# Writing / წერა

Drafting, editing, rewriting, tone, structure — long-form and short-form craft.
Each entry names one operation, states the output format and a number, and puts its constraints up front.

---

### W-01 · Line edit for clarity
`claude` `gpt` `gemini` — editing, clarity

**EN**
```
You are a line editor. Edit the text below sentence by sentence.

<text>
{{text}}
</text>

Who reads it: {{audience}}

Rules:
- MUST preserve the author's meaning, the order of the argument, and the author's voice
- NEVER add a claim that is not already in the text
- MUST NOT change the total word count by more than 10% in either direction
- MUST split every sentence over 30 words
- NEVER use: "in order to", "it should be noted that", "the fact that", "utilise", "leverage" as a verb
- Leave technical terms alone, unless the same term is used two different ways — then flag it instead of fixing it

Output: first the edited text, then a list of every change longer than five words, each with a three-word reason ("ambiguous referent", "buried verb", "double negative"). Maximum 12 entries; if there were more, list the 12 that cost the reader most.
```

**KA**
```
შენ ხარ რედაქტორი და ასწორებ ტექსტს წინადადება-წინადადება.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

ვინ კითხულობს: {{აუდიტორია}}

წესები:
- ავტორის აზრი, არგუმენტების თანმიმდევრობა და ხმა უცვლელი უნდა დარჩეს
- ახალი მტკიცება არ დაამატო — ტექსტში რაც არ წერია, არ გაჩნდეს
- სიტყვების საერთო რაოდენობა 10%-ზე მეტად არც გაზარდო და არც შეამცირო
- 30 სიტყვაზე გრძელი წინადადება გაყავი
- აკრძალულია: „უნდა აღინიშნოს, რომ“, „ის ფაქტი, რომ“, „მოცემულ შემთხვევაში“, „იმ თვალსაზრისით, რომ“
- ტერმინებს ხელი არ ახლო; თუ ერთი ტერმინი ორი სხვადასხვა მნიშვნელობით გხვდება, გაასწორების ნაცვლად მონიშნე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ჯერ გასწორებული ტექსტი, შემდეგ სია — ყოველი ცვლილება, რომელიც ხუთ სიტყვას აღემატება, სამსიტყვიანი მიზეზით („ბუნდოვანი მიმართება“, „დაკარგული ზმნა“, „ორმაგი უარყოფა“). სიაში მაქსიმუმ 12 პუნქტი; თუ მეტი იყო, დატოვე ის 12, რომელიც მკითხველს ყველაზე ძვირი უჯდება.
```

---

### W-02 · Cut by 40%
`claude` `gpt` `gemini` — editing, compression

**EN**
```
Cut the text below by 40% of its word count.

<text>
{{text}}
</text>

Must survive the cut: {{must_keep}}

Rules:
- MUST hit 40% within ±3%. State the before and after word counts on the first line.
- MUST cut whole sentences and whole clauses before cutting words inside a sentence
- NEVER cut a number, a date, a name, or a caveat that limits a claim
- NEVER replace a concrete example with a summary of it — delete the weaker example instead
- If two paragraphs make the same point, delete the second one entirely rather than merging them

Output: word count before → after, then the cut version, then the three cuts you were least sure about and why you made them anyway.
```

**KA**
```
შეამოკლე ქვემოთ მოცემული ტექსტი 40%-ით.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

რა უნდა გადარჩეს აუცილებლად: {{სავალდებულო}}

წესები:
- დასაშვები ცდომილება 3%-ია. პირველ ხაზზე მიუთითე სიტყვების რაოდენობა შემოკლებამდე და შემდეგ.
- ჯერ მთელი წინადადება ან მთელი ქვეწყობილი ნაწილი ამოაგდე და მხოლოდ მერე შეეხე ცალკეულ სიტყვას
- არასდროს ამოაგდო ციფრი, თარიღი, სახელი ან დათქმა, რომელიც მტკიცებას ზღუდავს
- კონკრეტული მაგალითი მის შეჯამებად არ აქციო — სჯობს სუსტი მაგალითი მთლიანად ამოაგდო
- თუ ორი აბზაცი ერთსა და იმავეს ამბობს, მეორე მთლიანად წაშალე და არ გააერთიანო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სიტყვების რაოდენობა ადრე → ახლა, შემოკლებული ტექსტი, ბოლოს სამი ამოღება, რომელშიც ყველაზე ნაკლებად იყავი დარწმუნებული, და რატომ მაინც ამოაგდე.
```

---

### W-03 · Rewrite for a different reader
`claude` `gpt` — rewriting, accessibility

**EN**
```
Rewrite the text below for a different reader.

<text>
{{text}}
</text>

Written for: {{current_reader}}
Must now work for: {{new_reader}}
What the new reader must be able to do after reading: {{task}}

Rules:
- MUST keep every factual claim. If a claim cannot survive simplification, keep it and explain it — NEVER drop it.
- MUST replace each specialist term with a plain equivalent, or keep the term and add a gloss of 7 words or fewer on first use
- Average sentence length MUST stay under 18 words; no sentence over 28
- NEVER use an analogy that introduces a fact the source does not contain
- NEVER write "simply", "just", "obviously", "of course"

Output: the rewritten text, then a two-column table of every term you replaced or glossed. Maximum 15 rows.
```

**KA**
```
გადაწერე ქვემოთ მოცემული ტექსტი სხვა მკითხველისთვის.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

ვისთვის იყო დაწერილი: {{ამჟამინდელი_მკითხველი}}
ვისთვის უნდა იმუშაოს ახლა: {{ახალი_მკითხველი}}
რა უნდა შეძლოს ახალმა მკითხველმა წაკითხვის შემდეგ: {{ამოცანა}}

წესები:
- ყველა ფაქტობრივი მტკიცება უნდა დარჩეს. თუ მტკიცება გამარტივებას ვერ უძლებს, დატოვე და ახსენი — არ ამოაგდო.
- ყოველი პროფესიული ტერმინი ან მარტივი შესატყვისით ჩაანაცვლე, ან დატოვე და პირველ ხსენებაზე 7 სიტყვამდე ახსნა მიაწერე
- წინადადების საშუალო სიგრძე 18 სიტყვაზე ნაკლები იყოს, ყველაზე გრძელი — 28 სიტყვამდე
- შედარება არ მოიგონო, თუ ის ახალ ფაქტს შემოიტანს — წყაროში რაც არ წერია, ტექსტში არ გაჩნდეს
- აკრძალულია: „უბრალოდ“, „ცხადია“, „რა თქმა უნდა“, „ყველამ იცის“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: გადაწერილი ტექსტი, შემდეგ ორსვეტიანი ცხრილი — ყოველი ჩანაცვლებული ან ახსნილი ტერმინი. მაქსიმუმ 15 სტრიქონი.
```

---

### W-04 · Tone shift
`claude` `gpt` — tone, register

**EN**
```
Shift the register of the text below without touching its content.

<text>
{{text}}
</text>

From: {{from_tone}}
To: {{to_tone}}
Where it will be read: {{channel}}

Rules:
- MUST keep the same information in the same order. NEVER reorder anything to make the new tone easier.
- MUST change register through verbs and sentence length first; adjectives last
- NEVER add humour, exclamation marks or emoji unless {{to_tone}} names them
- NEVER soften a refusal, a deadline or a number while making the text friendlier
- If a sentence carries legal or contractual weight, leave it word for word and mark it [unchanged: binding]

Output: the shifted text, then a note of 40 words or fewer on what could not be shifted without changing the meaning.
```

**KA**
```
შეუცვალე ქვემოთ მოცემულ ტექსტს რეგისტრი ისე, რომ შინაარსს არ შეეხო.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

საიდან: {{ამჟამინდელი_ტონი}}
საით: {{სასურველი_ტონი}}
სად წაიკითხავენ: {{არხი}}

წესები:
- ინფორმაცია და მისი თანმიმდევრობა უცვლელი უნდა დარჩეს. ტონის გამო აზრებს ადგილი არ გაუცვალო.
- რეგისტრი ჯერ ზმნებითა და წინადადების სიგრძით შეცვალე, ზედსართავებით — ბოლოს
- ხუმრობა, ძახილის ნიშანი და ემოჯი არ დაამატო, თუ {{სასურველი_ტონი}}-ში პირდაპირ არ წერია
- უარი, ვადა და ციფრი არ დაარბილო მაშინაც, როცა ტექსტს უფრო თბილს ხდი
- თუ წინადადებას იურიდიული ან სახელშეკრულებო წონა აქვს, დატოვე სიტყვასიტყვით და მიაწერე [უცვლელი: სავალდებულო]

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: გარდაქმნილი ტექსტი, შემდეგ 40 სიტყვამდე კომენტარი იმაზე, რისი შეცვლაც აზრის დაზიანების გარეშე ვერ მოხერხდა.
```

---

### W-05 · Structure from messy notes
`claude` `gpt` `gemini` — structure, outlining

**EN**
```
Build a structure out of the notes below.

<notes>
{{notes}}
</notes>

Final piece: {{format}}, target length {{length}} words
The one thing the reader must take away: {{takeaway}}

Rules:
- MUST use only what is in the notes. Where the structure needs something the notes do not contain, write "GAP: <what>".
- MUST give every section a word budget, and the budgets MUST sum to {{length}}
- Every heading MUST be a claim or a question — NEVER a label like "Background" or "Context"
- For each section, MUST name the one sentence that would survive if the section were cut to a single line
- NEVER produce more than 6 top-level sections
- Any note that does not fit anywhere goes under "Did not fit" — NEVER force it into a section

Output: Spine (one sentence) · Sections with word budgets · Did not fit · Gaps
```

**KA**
```
ქვემოთ მოცემული ჩანაწერებიდან ააგე ტექსტის სტრუქტურა.

<ჩანაწერები>
{{ჩანაწერები}}
</ჩანაწერები>

საბოლოო ტექსტი: {{ფორმატი}}, სასურველი მოცულობა — {{მოცულობა}} სიტყვა
ერთი აზრი, რომელიც მკითხველს უნდა დარჩეს: {{მთავარი_აზრი}}

წესები:
- გამოიყენე მხოლოდ ის, რაც ჩანაწერებშია. თუ სტრუქტურას რამე სჭირდება და ჩანაწერებში არ არის, დაწერე „აკლია: <რა>“.
- ყოველ სექციას მიაწერე სიტყვების ლიმიტი; ჯამში ზუსტად {{მოცულობა}} სიტყვა უნდა გამოვიდეს
- სექციის სათაური მტკიცება ან კითხვა უნდა იყოს და არა იარლიყი „შესავალი“ ან „კონტექსტი“
- თითო სექციაზე დაასახელე ერთი წინადადება, რომელიც გადარჩებოდა, ეს სექცია ერთ ხაზამდე რომ შემცირდეს
- მთავარი დონის სექცია 6-ზე მეტი არ იყოს
- ჩანაწერი, რომელიც ვერსად ჩაჯდა, ცალკე ჩამოწერე სექციაში „ვერ ჩაჯდა“ — ძალით არსად ჩასვა

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ხერხემალი (ერთი წინადადება) · სექციები სიტყვების ლიმიტით · ვერ ჩაჯდა · აკლია
```

---

### W-06 · Strengthen a weak opening
`claude` `gpt` — drafting, openings

**EN**
```
Rewrite the opening of the piece below.

<opening>
{{opening}}
</opening>

What the piece is about: {{subject}}
Where the reader is coming from: {{context}}
The promise the piece must keep: {{promise}}

Rules:
- MUST write 5 alternative openings, each under 45 words, each using a different move: a concrete scene, a number that surprises, a claim the reader will resist, a question the reader has already asked themselves, a flat statement of the problem
- Each opening MUST hand off into the existing second paragraph without that paragraph being rewritten
- NEVER open with a dictionary definition, a historical wind-up, a rhetorical "have you ever", or the words "In today's world"
- NEVER promise something the piece does not deliver

Output: 5 numbered openings, each labelled with the move it uses. Then one line naming the one you would ship and the single reason.
```

**KA**
```
გადაწერე ქვემოთ მოცემული ტექსტის დასაწყისი.

<დასაწყისი>
{{დასაწყისი}}
</დასაწყისი>

რაზეა ტექსტი: {{თემა}}
რა მდგომარეობაში მოდის მკითხველი: {{კონტექსტი}}
დაპირება, რომელიც ტექსტმა უნდა შეასრულოს: {{დაპირება}}

წესები:
- დაწერე 5 ვარიანტი, თითოეული 45 სიტყვამდე, თითოეული სხვა ხერხით: კონკრეტული სცენა, მოულოდნელი ციფრი, მტკიცება, რომელსაც მკითხველი წინააღმდეგობას გაუწევს, კითხვა, რომელიც მკითხველს საკუთარი თავისთვის უკვე დაუსვამს, პრობლემის პირდაპირი ფორმულირება
- ყოველი ვარიანტი არსებულ მეორე აბზაცს ისე უნდა დაუკავშირდეს, რომ ის აბზაცი გადასაწერი არ გახდეს
- აკრძალულია: ლექსიკონური განმარტებით დაწყება, ისტორიული შესავალი, „ოდესმე თუ დაფიქრებულხართ“ ტიპის კითხვა, „დღევანდელ სამყაროში“
- არ დაპირდე იმას, რასაც ტექსტი არ ასრულებს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: 5 დანომრილი ვარიანტი, თითოეულს გვერდით მიაწერე გამოყენებული ხერხი. ბოლოს ერთი ხაზი: რომელს გამოვაქვეყნებდი და ერთი მიზეზი.
```

---

### W-07 · Kill the passive and the nominalisation
`claude` `gpt` `gemini` — editing, style

**EN**
```
Strip the passive constructions and nominalisations out of the text below.

<text>
{{text}}
</text>

Rules:
- MUST convert every passive to active, UNLESS the actor is genuinely unknown or deliberately withheld — in those cases keep it and mark it [passive kept: actor unknown] or [passive kept: deliberate]
- MUST turn every nominalisation back into a verb: "made a decision" → "decided", "provides support for" → "supports"
- MUST name the actor in every sentence where the original hid one. If the source does not say who acted, write [WHO?].
- NEVER lengthen the text — the output MUST be shorter than the input
- NEVER touch a quoted sentence

Output: the rewritten text, then a count: passives found, passives kept and why, nominalisations converted, [WHO?] markers left standing.
```

**KA**
```
გაასუფთავე ქვემოთ მოცემული ტექსტი ვნებითი კონსტრუქციებისა და ზმნური არსებითებისგან.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

წესები:
- ყოველი ვნებითი კონსტრუქცია მოქმედ ზმნად აქციე, თუ მოქმედი პირი ნამდვილად უცნობი ან განზრახ დამალული არ არის — ასეთ შემთხვევაში დატოვე და მიაწერე [ვნებითი დარჩა: პირი უცნობია] ან [ვნებითი დარჩა: განზრახ]
- ზმნური არსებითი ზმნად დააბრუნე: „გადაწყვეტილების მიღება მოხდა“ → „გადაწყვიტეს“; „მხარდაჭერის გაწევას ახორციელებს“ → „მხარს უჭერს“
- ყოველ წინადადებაში დაასახელე მოქმედი პირი, თუ ორიგინალი მას მალავს. თუ ტექსტიდან არ ჩანს, ვინ იმოქმედა, დაწერე [ვინ?].
- ტექსტი არ გააგრძელო — გამოსავალი ორიგინალზე მოკლე უნდა იყოს
- ციტატას ხელი არ ახლო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: გადაწერილი ტექსტი, შემდეგ ანგარიში: რამდენი ვნებითი იპოვე, რამდენი დატოვე და რატომ, რამდენი ზმნური არსებითი გადააკეთე, რამდენი [ვინ?] დარჩა.
```

---

### W-08 · Counter-argument to your own draft
`claude` `gpt` — argument, critique

**EN**
```
Argue against the draft below as its strongest opponent would.

<draft>
{{draft}}
</draft>

Who the real opponent is: {{opponent}}
What they lose if the draft is right: {{stakes}}

Rules:
- MUST attack the load-bearing claim, NEVER the weakest sentence
- MUST produce exactly 4 objections, ranked by how much damage each does if it lands
- Each objection: the claim it attacks, quoted; the objection in under 40 words; the evidence that would settle it
- MUST include at least one objection about something the draft does not mention at all
- NEVER attack tone, length or style — only the argument
- NEVER invent a statistic to make an objection land

Then, for each objection, one line: does the draft survive it as written — yes / only with a caveat / no.

Output: the 4 objections, then the 4 verdicts. Do NOT defend the draft.
```

**KA**
```
იკამათე ქვემოთ მოცემული ტექსტის წინააღმდეგ ისე, როგორც მისი ყველაზე ძლიერი ოპონენტი იკამათებდა.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

ვინ არის რეალური ოპონენტი: {{ოპონენტი}}
რას კარგავს ის, თუ ტექსტი მართალია: {{ფსონი}}

წესები:
- დაესხი თავს მთავარ, მზიდ მტკიცებას და არა ყველაზე სუსტ წინადადებას
- დაწერე ზუსტად 4 შენიშვნა და დაალაგე იმის მიხედვით, რომელი აზიანებს ტექსტს ყველაზე მძიმედ
- თითო შენიშვნაზე: რომელ მტკიცებას ეხება (ციტატით), თავად შენიშვნა 40 სიტყვამდე და რა მტკიცებულება გადაწყვეტდა დავას
- ერთი შენიშვნა მაინც იმაზე უნდა იყოს, რაზეც ტექსტი საერთოდ არაფერს ამბობს
- ტონზე, სიგრძესა და სტილზე არ ისაუბრო — მხოლოდ არგუმენტზე
- სტატისტიკა არ მოიგონო შენიშვნის გასამყარებლად

შემდეგ თითო შენიშვნაზე ერთი ხაზი: უძლებს თუ არა ტექსტი ამ დარტყმას არსებული სახით — დიახ / მხოლოდ დათქმით / არა.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: 4 შენიშვნა, შემდეგ 4 დასკვნა. ტექსტს ნუ დაიცავ.
```

---

### W-09 · Title variants
`claude` `gpt` — headlines, copywriting

**EN**
```
Write title options for the piece below.

<piece>
{{piece}}
</piece>

Where it publishes: {{channel}}
Who scrolls past it: {{audience}}
The promise the piece actually keeps: {{promise}}

Rules:
- MUST write 12 titles, each under 65 characters
- MUST cover four approaches, 3 titles each: the specific result, the named tension, what the reader is getting wrong, the plain description
- Every title MUST be true of the piece as written. NEVER promise 7 items if the piece has 5.
- NEVER use: "the ultimate guide", "everything you need to know", "X things that will change your Y", or a colon followed by a vague abstraction
- MUST mark any title that only works if the reader already holds {{audience}}-specific context

Output: 12 titles grouped by approach, each with its character count. Then the two you would A/B test and what each one is actually testing.
```

**KA**
```
დაწერე სათაურის ვარიანტები ქვემოთ მოცემული ტექსტისთვის.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

სად გამოქვეყნდება: {{არხი}}
ვინ გაუსრიალებს გვერდს: {{აუდიტორია}}
დაპირება, რომელსაც ტექსტი ნამდვილად ასრულებს: {{დაპირება}}

წესები:
- დაწერე 12 სათაური, თითოეული 65 სიმბოლომდე
- ოთხი მიდგომა, თითოზე 3 სათაური: კონკრეტული შედეგი, დასახელებული დაპირისპირება, რას აკეთებს მკითხველი არასწორად, უბრალო აღწერა
- ყოველი სათაური ტექსტის რეალურ შიგთავსს უნდა შეესაბამებოდეს. თუ ტექსტში 5 პუნქტია, 7 არ დაპირდე.
- აკრძალულია: „სრული გზამკვლევი“, „ყველაფერი, რაც უნდა იცოდეთ“, „5 რამ, რაც შენს ცხოვრებას შეცვლის“, ორწერტილი და მის შემდეგ ბუნდოვანი განზოგადება
- მონიშნე სათაური, რომელიც მხოლოდ მაშინ მუშაობს, თუ მკითხველმა {{აუდიტორია}}-სთვის ნაცნობი კონტექსტი უკვე იცის

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: 12 სათაური მიდგომების მიხედვით დაჯგუფებული, თითოეულს გვერდით სიმბოლოების რაოდენობა. ბოლოს ორი, რომელსაც A/B ტესტში გავუშვებდი, და რას ამოწმებს თითოეული.
```

---

### W-10 · Transitions between sections
`claude` `gpt` — structure, flow

**EN**
```
Fix the joins between the sections below.

<text>
{{text}}
</text>

Rules:
- For every section boundary, MUST name the logical relation that actually holds: consequence, contrast, example, escalation, change of scale, or none
- Where the relation is "none", MUST say so and propose either a reorder or a cut — NEVER paper over a missing link with a transition sentence
- Each transition MUST be one sentence, under 22 words, and MUST carry a word or an idea from the section above into the one below
- NEVER use: "Moreover", "Furthermore", "That being said", "With that in mind", "Now let's turn to"
- NEVER start more than one transition in the whole piece with "But"

Output: a table — boundary | relation | proposed transition | flag where the relation is "none". Then, in one line, the reordering you recommend, if any.
```

**KA**
```
გაასწორე გადასვლები ქვემოთ მოცემული ტექსტის სექციებს შორის.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

წესები:
- ყოველ საზღვარზე დაასახელე, რა კავშირი აქვს რეალურად ორ სექციას: შედეგი, დაპირისპირება, მაგალითი, გამძაფრება, მასშტაბის შეცვლა თუ არანაირი
- სადაც კავშირი არ არსებობს, ეს პირდაპირ დაწერე და შემოგვთავაზე ან თანმიმდევრობის შეცვლა, ან ამოღება — არარსებული კავშირი გადამაბმელი წინადადებით არ დამალო
- თითო გადასვლა ერთი წინადადებაა, 22 სიტყვამდე, და წინა სექციიდან ერთი სიტყვა ან აზრი მომდევნოში უნდა გადმოიტანოს
- აკრძალულია: „გარდა ამისა“, „ამასთანავე“, „ზემოაღნიშნულიდან გამომდინარე“, „ახლა კი გადავიდეთ“
- მთელ ტექსტში მხოლოდ ერთი გადასვლა შეიძლება იწყებოდეს სიტყვით „მაგრამ“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ცხრილი — საზღვარი | კავშირი | შემოთავაზებული გადასვლა | ნიშანი, სადაც კავშირი არ არსებობს. ბოლოს ერთი ხაზი: რა თანმიმდევრობას გირჩევ, თუ საჭიროა.
```

---

### W-11 · Dialogue that sounds spoken
`claude` `gpt` — fiction, dialogue

**EN**
```
Rewrite the dialogue below so it sounds spoken.

<dialogue>
{{dialogue}}
</dialogue>

Who is speaking and what each one wants from the other: {{speakers}}
What neither of them will say out loud: {{unsaid}}

Rules:
- MUST keep every fact the scene delivers
- NEVER let a character explain something both characters already know
- MUST make at least three lines answer a different question than the one asked
- Average line MUST be under 14 words; at least two lines under 4
- NEVER spell out an accent phonetically, and NEVER give more than one speaker a verbal tic
- Speech tags: "said" and "asked" only. Delete every adverb attached to a tag.
- MUST leave {{unsaid}} unsaid — it may show only in what the characters step around

Output: the rewritten scene, then two lines naming where the scene still explains instead of showing.
```

**KA**
```
გადაწერე ქვემოთ მოცემული დიალოგი ისე, რომ ცოცხალ მეტყველებას ჰგავდეს.

<დიალოგი>
{{დიალოგი}}
</დიალოგი>

ვინ საუბრობს და რა უნდა თითოეულს მეორისგან: {{პერსონაჟები}}
რას არ იტყვის ხმამაღლა არც ერთი: {{უთქმელი}}

წესები:
- სცენაში არსებული ყველა ფაქტი უნდა შენარჩუნდეს
- პერსონაჟმა არ ახსნას ის, რაც ორივემ ისედაც იცის
- სულ მცირე სამი რეპლიკა სხვა კითხვას უნდა პასუხობდეს, ვიდრე დაისვა
- რეპლიკის საშუალო სიგრძე 14 სიტყვაზე ნაკლები იყოს, ორი მაინც — 4 სიტყვამდე
- კილოკავი ფონეტიკურად არ ჩაწერო; სიტყვიერი ჩვევა („გესმის?“, „აი, ასე“) მხოლოდ ერთ პერსონაჟს დაუტოვე
- ავტორის რემარკაში მხოლოდ „თქვა“ და „ჰკითხა“. რემარკას მიწერილი ზმნიზედა ამოაგდე: „წარმოთქვა გულისწყვეტით“ → „თქვა“.
- {{უთქმელი}} უთქმელი უნდა დარჩეს — ის მხოლოდ იმაში უნდა ჩანდეს, რასაც პერსონაჟები გვერდს აუვლიან

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: გადაწერილი სცენა, შემდეგ ორი ხაზი იმაზე, სად ხსნის სცენა ჯერ კიდევ იმის ნაცვლად, რომ აჩვენოს.
```

---

### W-12 · Description without the adjective pile-up
`claude` `gpt` — description, craft

**EN**
```
Rewrite the description below so detail does the work adjectives are doing now.

<description>
{{description}}
</description>

What the reader should feel or conclude afterwards: {{effect}}

Rules:
- MUST cut the adjective count by at least half. State the before and after counts on the first line.
- MUST replace each removed adjective with a noun, a verb, or a measurable detail: "old chair" → "the chair's left arm was wrapped in tape"
- MUST keep at most one adjective per sentence, and NEVER two before the same noun
- NEVER use: "beautiful", "stunning", "vibrant", "atmospheric", "bustling", "nestled"
- MUST include at least two things the reader can hear, smell or touch — not only what they can see
- NEVER state {{effect}} directly; the detail has to produce it

Output: adjective count before/after, the rewritten description, then the three details doing the most work.
```

**KA**
```
გადაწერე ქვემოთ მოცემული აღწერა ისე, რომ ზედსართავების ნაცვლად დეტალი მუშაობდეს.

<აღწერა>
{{აღწერა}}
</აღწერა>

რა უნდა იგრძნოს ან დაასკვნას მკითხველმა: {{შთაბეჭდილება}}

წესები:
- ზედსართავების რაოდენობა სულ მცირე ორჯერ შეამცირე. პირველ ხაზზე მიუთითე რიცხვი ადრე და შემდეგ.
- ყოველი ამოღებული ზედსართავი ჩაანაცვლე არსებითით, ზმნით ან გაზომვადი დეტალით: „ძველი სკამი“ → „სკამის მარცხენა სახელური იზოლენტით იყო შემოხვეული“
- ერთ წინადადებაში მაქსიმუმ ერთი ზედსართავი; ერთსა და იმავე არსებითს ორი ზედსართავი არასდროს
- აკრძალულია: „მშვენიერი“, „თვალწარმტაცი“, „ულამაზესი“, „განუმეორებელი“, „მყუდრო“, „ხმაურიანი ქუჩა“
- დაასახელე მინიმუმ ორი რამ, რაც ისმის, სუნით ან შეხებით აღიქმება და არა მხოლოდ თვალით
- {{შთაბეჭდილება}} პირდაპირ არ დაწერო — ის დეტალიდან უნდა დაიბადოს

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: ზედსართავების რაოდენობა ადრე/შემდეგ, გადაწერილი აღწერა, ბოლოს სამი დეტალი, რომელიც ყველაზე მეტს აკეთებს.
```

---

### W-13 · One text, three formats
`claude` `gpt` `gemini` — repurposing, formats

**EN**
```
Adapt the source below into three formats without repeating yourself.

<source>
{{source}}
</source>

Formats: {{format_a}}, {{format_b}}, {{format_c}}
Audience for each, where they differ: {{audiences}}

Rules:
- Each version MUST lead with a different fact from the source. NEVER open all three the same way.
- Each version MUST stand alone — a reader who sees only one MUST still get the point
- For the shortest format, MUST cut rather than compress, and MUST state what the short version loses
- NEVER copy a sentence word for word from one version into another
- NEVER add a claim that is not in the source
- State a word target for each version before writing it, and land within 10% of it

Output: three versions, each preceded by its word target and its lead fact. Then one line: what the source contains that none of the three could carry.
```

**KA**
```
ერთი და იგივე მასალა სამ ფორმატში გადაიტანე ისე, რომ თავი არ გაიმეორო.

<მასალა>
{{მასალა}}
</მასალა>

ფორმატები: {{ფორმატი_1}}, {{ფორმატი_2}}, {{ფორმატი_3}}
აუდიტორია თითოეულისთვის, თუ განსხვავდება: {{აუდიტორიები}}

წესები:
- თითოეული ვერსია სხვა ფაქტით დაიწყე — სამივე ერთნაირად არ გახსნა
- თითოეული ვერსია დამოუკიდებლად უნდა მუშაობდეს: ვინც მხოლოდ ერთს ნახავს, მთავარი აზრი მაინც უნდა მიიღოს
- ყველაზე მოკლე ფორმატისთვის ამოაგდე და არ შეკუმშო; ცალკე დაწერე, რას კარგავს მოკლე ვერსია
- ერთი ვერსიიდან მეორეში წინადადება სიტყვასიტყვით არ გადაიტანო
- მასალაში რაც არ წერია, არ დაამატო
- ყოველი ვერსიის წინ დაწერე სამიზნე მოცულობა სიტყვებში და 10%-ის ფარგლებში მოერგე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სამი ვერსია, თითოეულის წინ — სამიზნე მოცულობა და საწყისი ფაქტი. ბოლოს ერთი ხაზი: რა რჩება მასალაში, რაც სამივემ ვერ ატარა.
```

---

### W-14 · Read it back as a hostile reader
`claude` `gpt` `gemini` — critique, review

**EN**
```
Read the text below as a reader who wants it to fail.

<text>
{{text}}
</text>

Who this reader is: {{reader}}
Why they are hostile: {{motive}}
What they will do with a weakness once they find one: {{consequence}}

Rules:
- MUST quote the exact sentence behind every objection. NEVER paraphrase what you are attacking.
- MUST identify the first sentence at which this reader stops reading, and say why
- MUST sort problems into three kinds: factually attackable, unsupported, and phrased so badly it reads weaker than it is
- MUST name the one sentence that could be screenshotted out of context and used against the author
- NEVER suggest fixes — this pass only finds problems
- If a passage holds up, say so plainly instead of inventing an objection

Output: Stopped reading at · Factually attackable · Unsupported · Reads weaker than it is · Screenshot risk · Verdict: would this reader change their mind? yes / no / partly, in one sentence.
```

**KA**
```
წაიკითხე ქვემოთ მოცემული ტექსტი ისე, როგორც მკითხველი, რომელსაც ამ ტექსტის ჩავარდნა უნდა.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

ვინ არის ეს მკითხველი: {{მკითხველი}}
რატომ არის წინააღმდეგ განწყობილი: {{მიზეზი}}
რას იზამს, თუ სუსტ ადგილს იპოვის: {{შედეგი}}

წესები:
- ყოველ შენიშვნას თან უნდა ახლდეს ზუსტი ციტატა; ნათქვამი საკუთარი სიტყვებით არ გადმოთქვა
- იპოვე პირველი წინადადება, რომელზეც ეს მკითხველი კითხვას წყვეტს, და დაწერე რატომ
- პრობლემები სამ ჯგუფად დაალაგე: ფაქტობრივად სადავო, დაუსაბუთებელი და ცუდად ფორმულირებული — ისეთი, რომელიც სინამდვილეზე სუსტად ჟღერს
- დაასახელე ერთი წინადადება, რომელიც კონტექსტიდან ამოგლეჯილი, სქრინშოტის სახით ავტორის წინააღმდეგ წავა
- გამოსწორება არ შემოგვთავაზო — ამ ეტაპზე მხოლოდ პრობლემებს პოულობ
- თუ რომელიმე მონაკვეთი დარტყმას უძლებს, ეს პირდაპირ დაწერე და შენიშვნა ნუ მოიგონებ

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სად შეწყვიტა კითხვა · ფაქტობრივად სადავო · დაუსაბუთებელი · სინამდვილეზე სუსტად ჟღერს · სქრინშოტის რისკი · დასკვნა: შეიცვლის თუ არა ეს მკითხველი აზრს — დიახ / არა / ნაწილობრივ, ერთი წინადადებით.
```
