# Research / კვლევა

Grounded analysis, comparison, synthesis, extraction — work that must stay inside supplied material.
Almost every entry carries the grounding constraint and an audit contract: every conclusion names the line it rests on.

---

### R-01 · Multi-source synthesis with disagreements
`claude` `gpt` `gemini` — synthesis, sources

**EN**
```
You are a research synthesiser. Build one position out of the sources below.

The question this synthesis must answer: {{question}}
Each source is tagged S1, S2, S3 …

Use ONLY the material below. If it is not stated, write "not stated". NEVER infer.

<sources>
{{sources}}
</sources>

Rules:
- Every claim MUST carry the tags of the sources it rests on: [S2, S4]
- Where sources disagree, MUST NOT average them. Name the disagreement, state each position with its
  tags, and say what evidence would settle it.
- A claim supported by exactly one source MUST be marked "single-source"
- NEVER let the number of sources stand in for weight. If the material says what a source is
  (study, blog post, vendor page), say so next to the tag.
- NEVER carry a source's conclusion further than the source states it

Output:
1. Position — maximum 5 sentences, each with its tags
2. Where the sources agree
3. Where they disagree — each as: the question · position A [tags] · position B [tags] · what would settle it
4. What none of the sources address
```

**KA**
```
შენ ხარ მკვლევარი და რამდენიმე წყაროდან ერთ პოზიციას აყალიბებ.

კითხვა, რომელსაც ეს სინთეზი უნდა უპასუხოს: {{კითხვა}}
თითოეული წყარო მონიშნულია ნიშნულით S1, S2, S3 …

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ — არასდროს გამოიცნო.

<წყაროები>
{{წყაროები}}
</წყაროები>

წესები:
- ყოველ მტკიცებას მიაწერე იმ წყაროს ნიშნული, რომელსაც ის ეყრდნობა: [S2, S4]
- სადაც წყაროები ერთმანეთს ეწინააღმდეგება, საშუალო პოზიცია არ გამოიყვანო. დაასახელე უთანხმოება,
  თითოეული პოზიცია ნიშნულით და ის, თუ რა მტკიცებულება გადაწყვეტდა საკითხს.
- თუ მტკიცებას მხოლოდ ერთი წყარო უჭერს მხარს, მიაწერე „ერთი წყარო“
- წყაროების რაოდენობა არგუმენტის წონად არ ჩათვალო. თუ მასალაში წერია, რა ტიპისაა წყარო
  (კვლევა, სტატია, კომპანიის საკუთარი გვერდი), ნიშნულის გვერდით ეს მიუთითე.
- წყაროს დასკვნა იმაზე შორს არ წაიყვანო, ვიდრე თავად წყარო მიდის

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. პოზიცია — მაქსიმუმ 5 წინადადება, თითოეულს ნიშნული მიაწერე
2. რაში ემთხვევა წყაროები ერთმანეთს
3. რაში არ ემთხვევა — თითო: საკითხი · პოზიცია A [ნიშნულები] · პოზიცია B [ნიშნულები] · რა გადაწყვეტდა
4. რას არ ეხება არცერთი წყარო
```

---

### R-02 · Claim and evidence extraction
`claude` `gpt` `gemini` — extraction, evidence

**EN**
```
Extract every claim the document makes and attach to each the evidence the document itself gives.

Use ONLY the material below. If it is not stated, write "not stated". NEVER infer.

<document>
{{document}}
</document>

One row per claim:
claim (in the document's own words, max 20 words) | type: fact / forecast / opinion / definition |
evidence given in the document | where it appears (section, or the first four words of the sentence) |
strength: measured / cited / asserted

Rules:
- "asserted" means the document offers no evidence. NEVER supply evidence from your own knowledge.
- A number with no source MUST be typed "asserted", however confident the sentence sounds
- MUST NOT merge two claims into one row, and MUST NOT split one claim across rows
- Order: load-bearing claims first. A claim is load-bearing if removing it breaks the conclusion.
- Quantifiers ("most", "the first", "doubled") are claims. Do not skip them.

After the table: the three claims the whole document rests on, and for each, what the document would
have to show to support it.
```

**KA**
```
ამოკრიბე ყველა მტკიცება, რომელსაც დოკუმენტი აკეთებს, და თითოეულს მიაწერე ის მტკიცებულება, რომელსაც
თავად დოკუმენტი იძლევა.

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ — არასდროს გამოიცნო.

<დოკუმენტი>
{{დოკუმენტი}}
</დოკუმენტი>

თითო მტკიცებაზე ერთი ხაზი:
მტკიცება (დოკუმენტის საკუთარი სიტყვებით, მაქსიმუმ 20 სიტყვა) | ტიპი: ფაქტი / პროგნოზი / მოსაზრება / განმარტება |
რა მტკიცებულებაა დოკუმენტში მოყვანილი | სად გვხვდება (სექცია ან წინადადების პირველი ოთხი სიტყვა) |
სიმყარე: გაზომილი / წყაროზე დაყრდნობილი / უბრალოდ ნათქვამი

წესები:
- „უბრალოდ ნათქვამი“ ნიშნავს, რომ დოკუმენტი მტკიცებულებას საერთოდ არ იძლევა. საკუთარი ცოდნიდან
  მტკიცებულება არასდროს დაამატო.
- ციფრი, რომელსაც წყარო არ ახლავს, „უბრალოდ ნათქვამია“ — რაც უნდა დამაჯერებლად ჟღერდეს წინადადება
- ორი მტკიცება ერთ ხაზში არ გააერთიანო და ერთი მტკიცება ორ ხაზად არ დაშალო
- თანმიმდევრობა: ჯერ მზიდი მტკიცებები. მტკიცება მზიდია, თუ მისი ამოღებით დასკვნა იშლება.
- „უმეტესობა“, „პირველად“, „გაორმაგდა“ — ესეც მტკიცებებია, არ გამოტოვო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

ცხრილის შემდეგ: სამი მტკიცება, რომელზეც მთელი დოკუმენტი დგას, და თითოეულზე — რის ჩვენება დასჭირდებოდა
დოკუმენტს მის გასამყარებლად.
```

---

### R-03 · Steelman the opposing view
`claude` `gpt` — argumentation, steelman

**EN**
```
Build the strongest honest version of the position that opposes the one below.

Position to oppose: {{position}}
How its own holders state their case: {{their_case}}

Use ONLY the material below. If it is not stated, write "not stated". NEVER infer.

<material>
{{material}}
</material>

Rules:
- Every point MUST cite the line in <material> it rests on
- MUST argue by the opposing side's criteria of success, not by yours
- NEVER include a point its serious defenders would disown
- NEVER end with a rebuttal, a "however", or a return to the original position
- If a premise the opposing case needs has no support in the material, write
  "premise unsupported in material" and keep the premise visible rather than dropping it

Output:
1. The opposing position in one sentence its holders would sign
2. Its three strongest points, each with the cited line
3. The weakest point in the original position, and which cited line exposes it
4. What the opposing side would have to be wrong about for the original position to hold
```

**KA**
```
ააგე იმ პოზიციის ყველაზე ძლიერი, კეთილსინდისიერი ვერსია, რომელიც ქვემოთ მოცემულს უპირისპირდება.

პოზიცია, რომელსაც უნდა დაუპირისპირდე: {{პოზიცია}}
როგორ აყალიბებენ თავის არგუმენტს თავად მისი მომხრეები: {{მათი_არგუმენტი}}

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ — არასდროს გამოიცნო.

<მასალა>
{{მასალა}}
</მასალა>

წესები:
- ყოველ არგუმენტს მიაწერე ის ხაზი <მასალა>-დან, რომელსაც ეყრდნობა
- იმსჯელე მოპირდაპირე მხარის წარმატების კრიტერიუმით და არა შენით
- არ ჩაწერო არგუმენტი, რომელსაც ამ პოზიციის სერიოზული დამცველი უარყოფდა
- არ დაასრულო კონტრარგუმენტით, სიტყვით „თუმცა“ ან საწყის პოზიციაზე დაბრუნებით
- თუ არგუმენტს სჭირდება დაშვება, რომელსაც მასალა არ უჭერს მხარს, დაწერე
  „დაშვება მასალით გამყარებული არ არის“ და დაშვება მაინც დატოვე თვალსაჩინოდ

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. მოპირდაპირე პოზიცია ერთი წინადადებით, რომელსაც მისი მომხრე ხელს მოაწერდა
2. მისი სამი ყველაზე ძლიერი არგუმენტი, თითოეული მითითებული ხაზით
3. საწყისი პოზიციის ყველაზე სუსტი ადგილი და ის ხაზი, რომელიც მას ამხელს
4. რაში უნდა ცდებოდეს მოპირდაპირე მხარე იმისთვის, რომ საწყისი პოზიცია გაუძლოს
```

---

### R-04 · Weakest link in an argument
`claude` `gpt` `gemini` — argumentation, critique

**EN**
```
Find the weakest link in the argument below.

<argument>
{{argument}}
</argument>

Use ONLY the material above. If something is not stated, write "not stated". NEVER supply a missing
premise in the author's favour, and NEVER infer one from context.

Rules:
- MUST reconstruct the argument as numbered premises and a conclusion BEFORE judging any part of it
- MUST mark each premise: stated / assumed but unstated / stated but unsupported
- MUST identify the single premise whose failure collapses the conclusion fastest — not the one that
  is easiest to attack
- NEVER attack the wording, the tone, or the author
- For every objection, quote the exact phrase you are objecting to

Output:
1. Reconstruction: P1 … Pn → C
2. Table: premise | stated or assumed | what supports it in the text | the quoted phrase
3. The load-bearing premise, and what would have to be true for it to hold
4. The repair — the smallest change to the argument that would survive your objection
```

**KA**
```
იპოვე ყველაზე სუსტი რგოლი ქვემოთ მოცემულ არგუმენტში.

<არგუმენტი>
{{არგუმენტი}}
</არგუმენტი>

გამოიყენე მხოლოდ ზემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ — გამოტოვებული
დაშვება ავტორის სასარგებლოდ არასდროს შეავსო და კონტექსტიდან არ გამოიცნო.

წესები:
- ჯერ აღადგინე არგუმენტი დანომრილი დაშვებებისა და დასკვნის სახით და მხოლოდ შემდეგ შეაფასე
- ყოველ დაშვებას მიაწერე ნიშანი: პირდაპირ წერია / ნაგულისხმევია, მაგრამ არ წერია / წერია, მაგრამ გამყარებული არ არის
- დაასახელე ერთი დაშვება, რომლის დანგრევაც ყველაზე სწრაფად შლის დასკვნას — და არა ის, რომელზეც
  თავდასხმა ყველაზე ადვილია
- არ გააკრიტიკო ფორმულირება, ტონი ან ავტორი
- ყოველ შენიშვნასთან ციტირებული მოიყვანე ზუსტად ის ფრაზა, რომელსაც ეკამათები

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. აღდგენილი არგუმენტი: დ1 … დn → დასკვნა
2. ცხრილი: დაშვება | წერია თუ ნაგულისხმევია | რა უჭერს მხარს ტექსტში | ციტირებული ფრაზა
3. მზიდი დაშვება და ის, რაც უნდა იყოს ჭეშმარიტი, რომ იგი გაუძლოს
4. შეკეთება — ყველაზე მცირე ცვლილება არგუმენტში, რომელიც შენს შენიშვნას გაუძლებდა
```

---

### R-05 · Fact-check a draft against sources
`claude` `gpt` `gemini` — fact-checking, verification

**EN**
```
Check the draft below against the supplied sources and nothing else.

<draft>
{{draft}}
</draft>

<sources>
{{sources}}
</sources>

Use ONLY the sources. If a statement cannot be checked against them, mark it "not in sources" —
NEVER check it against your own knowledge, and NEVER infer.

One row per factual statement in the draft:
statement (quoted) | verdict: supported / contradicted / partly supported / not in sources |
the source line | the change to make, in one line

Rules:
- Numbers, dates, names and quantifiers ("most", "the first", "doubled") MUST each be checked
  separately, even inside a single sentence
- "partly supported" MUST name which part fails
- MUST NOT rewrite the draft. One line of correction per row.
- Contradicted statements first, then partly supported, then not in sources, then supported
- A source that merely repeats the draft's phrasing without its own evidence is "not in sources"

End with: the count in each verdict category, and the one statement whose failure would most damage
the draft.
```

**KA**
```
გადაამოწმე ქვემოთ მოცემული ტექსტი მხოლოდ მოწოდებული წყაროებით და სხვა არაფრით.

<ტექსტი>
{{ტექსტი}}
</ტექსტი>

<წყაროები>
{{წყაროები}}
</წყაროები>

გამოიყენე მხოლოდ ეს წყაროები. თუ მტკიცების გადამოწმება მათით შეუძლებელია, მიაწერე „წყაროებში არ არის“ —
საკუთარი ცოდნით არასდროს შეამოწმო და არასდროს გამოიცნო.

ტექსტის თითო ფაქტობრივ მტკიცებაზე ერთი ხაზი:
მტკიცება (ციტირებული) | დასკვნა: დასტურდება / ეწინააღმდეგება / ნაწილობრივ დასტურდება / წყაროებში არ არის |
წყაროს ხაზი | რა უნდა შეიცვალოს, ერთი ხაზით

წესები:
- ციფრი, თარიღი, სახელი და განზოგადება („უმეტესობა“, „პირველად“, „გაორმაგდა“) ცალ-ცალკე შეამოწმე,
  მაშინაც კი, როცა ერთსა და იმავე წინადადებაშია
- „ნაწილობრივ დასტურდება“-სთან აუცილებლად დაწერე, კონკრეტულად რომელი ნაწილი არ დასტურდება
- ტექსტი თავად არ გადაწერო. თითო ხაზზე ერთი შესწორება.
- თანმიმდევრობა: ჯერ ის, რაც ეწინააღმდეგება, შემდეგ ნაწილობრივ დადასტურებული, შემდეგ ის, რაც
  წყაროებში არ არის, ბოლოს დადასტურებული
- წყარო, რომელიც უბრალოდ იმეორებს ტექსტის ფორმულირებას საკუთარი მტკიცებულების გარეშე, ითვლება
  როგორც „წყაროებში არ არის“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

ბოლოს: რამდენი მტკიცება მოხვდა თითოეულ კატეგორიაში და ერთი მტკიცება, რომლის გაბათილებაც ტექსტს
ყველაზე მეტად დააზიანებდა.
```

---

### R-06 · Comparison matrix from unstructured material
`claude` `gpt` `gemini` — comparison, structuring

**EN**
```
Build a comparison matrix out of the unstructured material below.

Items to compare: {{items}}
The decision this matrix must inform: {{decision}}

Use ONLY the material below. If a cell is not stated, write "not stated". NEVER infer a value from a
similar item, from a price tier, or from what is typical.

<material>
{{material}}
</material>

Rules:
- Derive the criteria from {{decision}} — at most 7, each one capable of flipping the choice
- MUST NOT include a criterion on which every item is identical
- Every filled cell MUST carry the source line it came from
- Where the material hedges ("up to", "from", "in most cases"), keep the hedge inside the cell
- NEVER convert a qualitative statement into a number or a score
- NEVER leave a cell blank — "not stated" is the value

Output:
1. The matrix — items as rows, criteria as columns
2. Coverage — which cells are "not stated", and which of those gaps blocks the decision
3. What the matrix shows: 3 sentences, each naming the cells it rests on
4. The one criterion absent from the material that would decide it
```

**KA**
```
ქვემოთ მოცემული დაუსტრუქტურებელი მასალიდან ააგე შედარების ცხრილი.

რა უნდა შეადარო: {{ობიექტები}}
გადაწყვეტილება, რომელსაც ეს ცხრილი უნდა დაეხმაროს: {{გადაწყვეტილება}}

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ უჯრაში რაიმე არ წერია, დაწერე „არ არის მითითებული“ —
მსგავსი ობიექტის, ფასის კატეგორიის ან ჩვეული პრაქტიკის მიხედვით არასდროს გამოიცნო.

<მასალა>
{{მასალა}}
</მასალა>

წესები:
- კრიტერიუმები გამოიყვანე {{გადაწყვეტილება}}-დან — მაქსიმუმ 7 კრიტერიუმი, თითოეული ისეთი, რომელსაც
  არჩევანის შეცვლა შეუძლია
- არ ჩართო კრიტერიუმი, რომელზეც ყველა ობიექტი ერთნაირია
- ყოველ შევსებულ უჯრას მიაწერე ის ხაზი მასალიდან, საიდანაც აიღე
- თუ მასალა დათქმით საუბრობს („მაქსიმუმ“, „დაწყებული“, „ხშირ შემთხვევაში“), დათქმა უჯრაშივე დატოვე
- თვისობრივი შეფასება ციფრად ან ქულად არასდროს გადააქციო
- ცარიელი უჯრა არ დატოვო — „არ არის მითითებული“ თავად არის მნიშვნელობა

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. ცხრილი — ობიექტები სტრიქონებად, კრიტერიუმები სვეტებად
2. დაფარვა — რომელ უჯრაშია „არ არის მითითებული“ და რომელი ხარვეზი აჩერებს გადაწყვეტილებას
3. რას აჩვენებს ცხრილი: 3 წინადადება, თითოეულს მიაწერე უჯრები, რომლებსაც ეყრდნობა
4. ერთი კრიტერიუმი, რომელიც მასალაში საერთოდ არ არის და რომელიც საკითხს გადაწყვეტდა
```

---

### R-07 · Literature note from a paper
`claude` `gpt` `gemini` — academic, literature

**EN**
```
Write a reading note for the paper below.

<paper>
{{paper}}
</paper>

Use ONLY the paper. If something is not stated, write "not stated". NEVER infer the sample size, the
funding, or a limitation the authors did not name, and NEVER import findings from other work.

Output exactly these fields:
- The question the paper asks
- Method, in one sentence a non-specialist can follow
- Sample: what, how many, how selected, over what period
- Main result, with the effect size and the uncertainty exactly as the paper reports them
- Limitations the authors state
- Limitations the authors do NOT state but the method implies — mark each "inferred from method"
- What this paper does NOT show: the three claims a reader would wrongly take from it
- One sentence that can be safely cited, with its section or page

Rules:
- MUST keep the authors' hedges. NEVER upgrade "associated with" to "causes".
- If no uncertainty measure is reported, write "no uncertainty reported"
- If the paper's abstract and its results section differ in strength, quote both and say so
```

**KA**
```
დაწერე სამუშაო შენიშვნა ქვემოთ მოცემულ სტატიაზე.

<სტატია>
{{სტატია}}
</სტატია>

გამოიყენე მხოლოდ ეს სტატია. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ — შერჩევის ზომა,
დაფინანსება ან ავტორების დაუსახელებელი შეზღუდვა არასდროს გამოიცნო და სხვა ნაშრომის შედეგი არ შემოიტანო.

გამოსავალი — ზუსტად ეს ველები:
- რა კითხვას სვამს სტატია
- მეთოდი, ერთი წინადადებით, რომელსაც არასპეციალისტიც გაიგებს
- შერჩევა: რა, რამდენი ერთეული, როგორ შეირჩა, რა პერიოდში
- მთავარი შედეგი, ეფექტის ზომითა და ცდომილებით ზუსტად ისე, როგორც სტატიაშია მოცემული
- შეზღუდვები, რომლებსაც ავტორები თავად ასახელებენ
- შეზღუდვები, რომლებსაც ავტორები არ ასახელებენ, მაგრამ მეთოდიდან გამომდინარეობს — თითოეულს მიაწერე
  „მეთოდიდან გამომდინარე“
- რას არ ამტკიცებს ეს სტატია: სამი დასკვნა, რომელსაც მკითხველი შეცდომით გამოიტანდა
- ერთი წინადადება, რომლის ციტირებაც უსაფრთხოა, სექციის ან გვერდის მითითებით

წესები:
- შეინარჩუნე ავტორების დათქმები. „კავშირშია“ არასდროს აქციო „იწვევს“-ად.
- თუ ცდომილება საერთოდ არ არის მოცემული, დაწერე „ცდომილება მითითებული არ არის“
- თუ აბსტრაქტი შედეგების სექციაზე უფრო კატეგორიულია, ორივე დაიმოწმე და ეს განსხვავება დაწერე

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### R-08 · Interview and survey synthesis
`claude` `gpt` `gemini` — qualitative, synthesis

**EN**
```
Turn the responses below into themes.

The question respondents were asked: {{question}}
Number of respondents: {{n}}

Use ONLY the responses below. If something is not stated, write "not stated". NEVER infer a
motivation, a feeling, or a cause a respondent did not state.

<responses>
{{responses}}
</responses>

Rules:
- Every theme MUST carry a count: in how many of the {{n}} responses it appears
- Every theme MUST carry 2 verbatim quotes, unedited, each with its respondent number
- A theme raised by one respondent goes under "single mentions" and is NEVER merged upward
- Rank themes by count. Then name separately the low-count theme with the highest stakes.
- NEVER tidy a quote into cleaner language, and NEVER combine two respondents into one quote

Output:
1. Themes by count: theme | count | 2 quotes | who explicitly does NOT mention it
2. Single mentions
3. Contradictions between respondents, quoted on both sides
4. What the question failed to ask — visible from what respondents volunteered unprompted
```

**KA**
```
გადააქციე ქვემოთ მოცემული პასუხები თემებად.

კითხვა, რომელიც რესპონდენტებს დაუსვეს: {{კითხვა}}
რესპონდენტთა რაოდენობა: {{რაოდენობა}}

გამოიყენე მხოლოდ ქვემოთ მოცემული პასუხები. თუ რაიმე არ წერია, დაწერე „არ არის მითითებული“ —
მოტივი, განცდა ან მიზეზი, რომელიც რესპონდენტს არ უთქვამს, არასდროს გამოიცნო.

<პასუხები>
{{პასუხები}}
</პასუხები>

წესები:
- ყოველ თემას მიაწერე რიცხვი: რამდენ პასუხში გვხვდება {{რაოდენობა}} პასუხიდან
- ყოველ თემას მოაყოლე 2 პირდაპირი ციტატა, შეუცვლელი, რესპონდენტის ნომრით
- თემა, რომელიც მხოლოდ ერთმა რესპონდენტმა ახსენა, ჩაწერე სექციაში „ერთეული ხსენება“ და სხვა თემას
  არასდროს შეურიო
- თემები დაალაგე რაოდენობის მიხედვით. ცალკე დაასახელე ის იშვიათი თემა, რომელსაც ყველაზე მძიმე შედეგი აქვს.
- ციტატა უფრო ლამაზ ენაზე არ გადააკეთო და ორი რესპონდენტის სიტყვები ერთ ციტატად არ გააერთიანო

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. თემები რაოდენობით: თემა | რამდენჯერ | 2 ციტატა | ვინ პირდაპირ არ ახსენებს
2. ერთეული ხსენებები
3. წინააღმდეგობები რესპონდენტებს შორის, ორივე მხარის ციტატით
4. რა არ იკითხა კითხვამ — ეს ჩანს იქიდან, რაც რესპონდენტებმა დაუკითხავად თქვეს
```

---

### R-09 · Timeline reconstruction from scattered mentions
`claude` `gpt` `gemini` — extraction, timeline

**EN**
```
Reconstruct a timeline from the scattered mentions below.

Subject: {{subject}}

Use ONLY the material below. If a date is not stated, write "no date stated" — NEVER estimate a date
from context, from the order of the text, or from what seems plausible.

<material>
{{material}}
</material>

Rules:
- One row per event: date as stated | event | who | the source line
- Relative mentions ("two weeks later", "the following spring") MUST stay relative and be anchored to
  the event they follow. NEVER convert them into absolute dates.
- Where two mentions conflict on a date, keep both rows and mark them "conflict"
- Order: dated events in sequence, then relative-only events under the event they attach to, then
  undated events
- MUST NOT insert a plausible intermediate event to make the sequence flow
- If the material states a duration but no start, record the duration and write "start not stated"

End with: Gaps — the periods containing no stated events, and the question each gap raises.
```

**KA**
```
ქვემოთ მიმოფანტული ხსენებებიდან აღადგინე ქრონოლოგია.

საკითხი: {{საკითხი}}

გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ თარიღი არ წერია, დაწერე „თარიღი არ არის მითითებული“ —
კონტექსტით, ტექსტის თანმიმდევრობით ან დამაჯერებლობით თარიღი არასდროს გამოიცნო.

<მასალა>
{{მასალა}}
</მასალა>

წესები:
- თითო მოვლენაზე ერთი ხაზი: თარიღი ისე, როგორც წერია | მოვლენა | ვინ | წყაროს ხაზი
- ფარდობითი მითითება („ორი კვირის შემდეგ“, „მომდევნო გაზაფხულზე“) ფარდობითივე დატოვე და მიაბი იმ
  მოვლენას, რომელსაც მოსდევს. კონკრეტულ თარიღად არასდროს გადათარგმნო.
- თუ ორი ხსენება თარიღზე ერთმანეთს ეწინააღმდეგება, ორივე ხაზი დატოვე და მიაწერე „წინააღმდეგობა“
- თანმიმდევრობა: ჯერ დათარიღებული მოვლენები რიგზე, შემდეგ ფარდობითი მოვლენები იმ მოვლენის ქვეშ,
  რომელსაც მიება, ბოლოს — უთარიღო მოვლენები
- თხრობის გასამართად შუალედური მოვლენა არ ჩაამატო
- თუ მასალაში ხანგრძლივობა წერია, დასაწყისი კი არა, ხანგრძლივობა ჩაწერე და მიაწერე
  „დასაწყისი არ არის მითითებული“

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

ბოლოს: ხარვეზები — პერიოდები, რომლებზეც არცერთი მოვლენა არ არის დასახელებული, და კითხვა, რომელსაც
თითოეული ხარვეზი აჩენს.
```

---

### R-10 · What the data cannot answer
`claude` `gpt` `gemini` — methodology, limits

**EN**
```
State what the data described below cannot answer.

The question being asked of it: {{question}}

Use ONLY the description below. If a property of the data is not stated, write "not stated".
NEVER assume how the data was collected, who is in it, or what the missing values mean.

<data>
{{data}}
</data>

Rules:
- MUST sort every part of the question into three buckets: the data can answer it · the data has the
  variable but the design cannot support the inference · the variable is not there at all
- For each "cannot", name the specific reason: no comparison group · no measurement before the change ·
  selection on the outcome · self-report · aggregation hides the unit that matters · too few cases in
  the cell the question is about · the outcome measured is not the outcome asked about
- For each "cannot", state the smallest additional data that would fix it
- NEVER offer a proxy without stating what the proxy would get wrong
- If part of the question CAN be answered, say exactly which part, and stop there

Output: What this data answers · What it cannot, and why · What would be needed ·
The conclusion a careless reader would wrongly draw from it
```

**KA**
```
დაწერე, რას ვერ პასუხობს ქვემოთ აღწერილი მონაცემები.

კითხვა, რომელსაც ამ მონაცემებს უსვამენ: {{კითხვა}}

გამოიყენე მხოლოდ ქვემოთ მოცემული აღწერა. თუ მონაცემების რომელიმე თვისება არ წერია, დაწერე
„არ არის მითითებული“ — არასდროს დაუშვა, როგორ შეგროვდა მონაცემები, ვინ მოხვდა მათში ან რას ნიშნავს
ცარიელი უჯრები.

<მონაცემები>
{{მონაცემები}}
</მონაცემები>

წესები:
- კითხვის ყოველი ნაწილი დაალაგე სამ ჯგუფად: მონაცემები პასუხობს · ცვლადი არსებობს, მაგრამ კვლევის
  აგებულება ასეთ დასკვნას ვერ იტანს · ცვლადი საერთოდ არ არის
- ყოველ „ვერ პასუხობს“-ს მიაწერე კონკრეტული მიზეზი: არ არის შესადარებელი ჯგუფი · ცვლილებამდე გაზომვა
  არ ჩატარებულა · შერჩევა თავად შედეგზეა აგებული · მონაცემი თვითდეკლარირებულია · აგრეგირება მალავს იმ
  ერთეულს, რომელიც გვაინტერესებს · საჭირო უჯრაში ძალიან ცოტა შემთხვევაა · გაზომილია სხვა შედეგი,
  ვიდრე კითხვაშია
- ყოველ „ვერ პასუხობს“-ზე დაწერე, რა მინიმალური დამატებითი მონაცემი გამოასწორებდა ამას
- არ შემოგვთავაზო ჩამნაცვლებელი მაჩვენებელი იმის დაწერის გარეშე, რაში შეცდებოდა ეს ჩანაცვლება
- თუ კითხვის ნაწილზე პასუხი შესაძლებელია, ზუსტად დაასახელე რომელ ნაწილზე და იქვე გაჩერდი

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: რას პასუხობს ეს მონაცემები · რას ვერ პასუხობს და რატომ · რა დასჭირდებოდა ·
რა დასკვნას გამოიტანდა უყურადღებო მკითხველი
```

---

### R-11 · What would change my mind
`claude` `gpt` — epistemics, falsification

**EN**
```
Design the falsification test for the position below.

Position: {{position}}
The evidence it currently rests on: {{evidence}}

Use ONLY the material below when you describe the existing evidence. If it is not stated, write
"not stated". NEVER infer support the material does not contain.

<material>
{{material}}
</material>

Rules:
- MUST restate the position so that it CAN be wrong — remove every hedge that makes it unfalsifiable
- Each test MUST specify: what result confirms · what result falsifies · what result is uninformative
- NEVER propose a test the position survives under every outcome
- MUST name evidence already in the material that cuts against the position, cited by line
- MUST identify the cheapest test that carries the most information, and say why it is cheapest
- NEVER rate the position's likelihood — this prompt is about what would settle it, not about who is right

Output:
1. The position, restated so it can be wrong
2. Three falsifying observations, ranked by cost to obtain
3. Evidence in the material that already cuts against it, with citations
4. What a holder of the position would say if each test failed — and whether that answer repairs the
   position or merely escapes the test
```

**KA**
```
ააგე გამაბათილებელი შემოწმება ქვემოთ მოცემული პოზიციისთვის.

პოზიცია: {{პოზიცია}}
რას ეყრდნობა იგი ამჟამად: {{მტკიცებულება}}

არსებული მტკიცებულების აღწერისას გამოიყენე მხოლოდ ქვემოთ მოცემული მასალა. თუ რაიმე არ წერია, დაწერე
„არ არის მითითებული“ — მხარდაჭერა, რომელიც მასალაში არ არის, არასდროს გამოიცნო.

<მასალა>
{{მასალა}}
</მასალა>

წესები:
- გადააფორმულირე პოზიცია ისე, რომ მისი გაბათილება შესაძლებელი იყოს — ამოიღე ყველა დათქმა, რომელიც მას
  შეუმოწმებელს ხდის
- ყოველ შემოწმებაზე დაწერე: რომელი შედეგი ადასტურებს · რომელი აბათილებს · რომელი არაფერს ამბობს
- არ შემოგვთავაზო შემოწმება, რომელსაც პოზიცია ნებისმიერი შედეგის დროს გაუძლებს
- დაასახელე მასალაშივე არსებული მტკიცებულება, რომელიც პოზიციის საწინააღმდეგოდ მუშაობს, ხაზის მითითებით
- დაასახელე ყველაზე იაფი შემოწმება, რომელიც ყველაზე მეტ ინფორმაციას იძლევა, და დაწერე, რატომაა იაფი
- არ შეაფასო, რამდენად სავარაუდოა პოზიციის სისწორე — აქ საკითხია, რა გადაწყვეტდა და არა ვინ არის მართალი

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი:
1. პოზიცია, გადაფორმულირებული ისე, რომ მცდარი შეიძლება აღმოჩნდეს
2. სამი დაკვირვება, რომელიც მას გააბათილებდა — დალაგებული მოპოვების სიძვირით
3. მასალაში უკვე არსებული საწინააღმდეგო მტკიცებულება, მითითებით
4. რას იტყოდა პოზიციის მომხრე თითოეული შემოწმების წარუმატებლობაზე — და არის ეს პასუხი პოზიციის
   შეკეთება თუ შემოწმებისგან თავის არიდება
```

---

### R-12 · Bias and sampling audit
`claude` `gpt` `gemini` — methodology, bias

**EN**
```
Audit the study below for sampling and bias.

<study>
{{study}}
</study>

Use ONLY the material above. If a design detail is not stated, write "not stated" — NEVER assume
randomisation, a control group, a blinding procedure, or a response rate that is not reported.

Check each of these and mark it stated / not stated / problem:
1. Who was sampled, from what frame, and who falls outside that frame
2. How participants were selected, and who could not be selected at all
3. Response or attrition rate, and who dropped out
4. What was measured, by whom, and whether the measurer knew the condition
5. What the comparison group is, and how it differs beyond the thing being studied
6. Who funded the study and who ran the analysis
7. Whether the outcome reported is the outcome the study set out to measure

For every "problem", state the direction of the bias: which way it pushes the result, and whether it
makes the effect look larger or smaller.

Rules:
- NEVER call a study strong or weak overall. Report the seven rows and let them stand.
- NEVER import what is typical for this field — judge only what is reported

Output: the seven-row audit · the two problems that most threaten the conclusion · what the study can
still be used for despite them · one sentence stating the finding honestly given all of the above
```

**KA**
```
შეამოწმე ქვემოთ მოცემული კვლევა შერჩევისა და მიკერძოების თვალსაზრისით.

<კვლევა>
{{კვლევა}}
</კვლევა>

გამოიყენე მხოლოდ ზემოთ მოცემული მასალა. თუ კვლევის აგებულების რომელიმე დეტალი არ წერია, დაწერე
„არ არის მითითებული“ — შემთხვევითი შერჩევა, საკონტროლო ჯგუფი, ბრმა შემოწმება ან გამოხმაურების
მაჩვენებელი, რომელიც არ არის მოცემული, არასდროს დაუშვა.

შეამოწმე თითოეული პუნქტი და მიაწერე: წერია / არ წერია / პრობლემაა
1. ვინ მოხვდა შერჩევაში, რომელი ერთობლიობიდან და ვინ რჩება ამ ერთობლიობის მიღმა
2. როგორ შეირჩნენ მონაწილეები და ვინ ვერ მოხვდებოდა შერჩევაში საერთოდ
3. გამოხმაურების ან გამოთიშვის მაჩვენებელი და ვინ გამოეთიშა
4. რა გაიზომა, ვინ გაზომა და იცოდა თუ არა გამზომმა, რომელ ჯგუფთან ჰქონდა საქმე
5. რა არის შესადარებელი ჯგუფი და რით განსხვავდება ის შესასწავლი ფაქტორის გარდა
6. ვინ დააფინანსა კვლევა და ვინ ჩაატარა ანალიზი
7. ემთხვევა თუ არა ნაჩვენები შედეგი იმ შედეგს, რომლის გაზომვასაც კვლევა თავიდან აპირებდა

ყოველ „პრობლემაზე“ დაწერე მიკერძოების მიმართულება: რომელი მხარისკენ წევს შედეგს და ეფექტს უფრო დიდად
აჩვენებს თუ უფრო მცირედ.

წესები:
- კვლევა მთლიანობაში ძლიერად ან სუსტად არ შეაფასო. მოიყვანე შვიდივე პუნქტი და ამით დასრულდეს.
- არ შემოიტანო ის, რაც ამ სფეროში ჩვეულებრივია — იმსჯელე მხოლოდ იმაზე, რაც დაწერილია

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: შვიდპუნქტიანი შემოწმება · ორი პრობლემა, რომელიც დასკვნას ყველაზე მეტად ემუქრება ·
რისთვის შეიძლება კვლევის გამოყენება მაინც · ერთი წინადადება, რომელიც ყოველივე ამის გათვალისწინებით
პატიოსნად აღწერს ნაპოვნს
```
