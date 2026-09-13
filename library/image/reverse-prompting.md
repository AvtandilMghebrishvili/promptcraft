# Reverse prompting / უკუპრომპტინგი

These are not generator prompts. They are instructions for a vision-capable text model — Claude, GPT or Gemini — and you send them together with a picture.
Input is an image; output is a prompt you then paste into Midjourney, Nano Banana, GPT-Image, Veo or Sora.
Observation only: every entry holds the model to what is visibly in the frame. Camera metadata is what models invent most confidently, so where a lens, focal length or film stock cannot be seen, the answer is "uncertain" — never a plausible-sounding value.
No real people, no imitation: describe a person by generic visible attributes instead of naming them or naming who they resemble, and describe a style in generic terms instead of naming a living artist, studio or brand to copy.

ეს ბლოკი დანარჩენი `image/` სექციისგან განსხვავდება — აქ პრომპტს გენერატორს კი არ აძლევ, არამედ მხედველობის მქონე ტექსტურ მოდელს: Claude, GPT ან Gemini.
შესატანი მასალა სურათია, გამოსავალი — მზა პრომპტი, რომელსაც შემდეგ Midjourney-ში, Nano Banana-ში, GPT-Image-ში, Veo-ში ან Sora-ში ჩასვამ.
მხოლოდ დაკვირვება: ყოველი პრომპტი მოდელს კადრში ხილულით ზღუდავს. ობიექტივს, ფოკუსურ მანძილსა და ფირს მოდელი ყველაზე თავდაჯერებულად იგონებს — თუ ეს ვერ დგინდება, პასუხი უნდა იყოს „ვერ დგინდება“ და არა დამაჯერებელი ციფრი.
რეალურ ადამიანს სახელით არ ვასახელებთ და ნიმუშს არ ვაკოპირებთ: ადამიანი ხილული ნიშნებით აღიწერება, სტილი კი ზოგადი ენით და არა ცოცხალი მხატვრის, სტუდიის ან ბრენდის სახელით.

---

### RP-01 · Reference image → Midjourney descriptor string
`claude` `gpt` `gemini` — reverse, midjourney

**EN**
```
You are given one reference image. Return a Midjourney prompt — a comma-separated descriptor
string — that would produce a picture like it.

<image>{{image}}</image>

Describe ONLY what is visible. If you cannot tell the lens, focal length, aperture or film
stock, write "uncertain" in that slot rather than guessing a plausible value.

Do not name anyone in the image and do not state who they resemble — describe people only by
visible generic attributes: approximate age range, build, clothing, pose. Do not name a living
artist, photographer or brand to imitate; describe the visual treatment in generic terms.

Build the string in this order, comma-separated, no sentences:
subject → action → setting → composition and camera position → lighting → style/medium →
technical → parameters

Rules:
- Composition MUST state shot size, where the subject sits in the frame, and camera height
- Lighting MUST state source, direction relative to camera, and quality (hard or soft)
- Technical: only what the image supports. Shallow depth of field is visible; a specific lens
  usually is not.
- Parameters: --ar matching the visible aspect ratio, plus --style raw for photographic
  references. Add --no only for something visibly absent that the generator tends to add anyway.
- Return the string on one line. No explanation, no bullets, no commentary.

On a second line, list every slot where you wrote "uncertain".
```

**KA**
```
გაქვს ერთი რეფერენსი. დააბრუნე Midjourney-ის პრომპტი — დესკრიპტორების მძიმეებით გამოყოფილი
სტრიქონი, რომელიც მსგავს სურათს დააგენერირებს.

<სურათი>{{სურათი}}</სურათი>

აღწერე მხოლოდ ის, რაც კადრში რეალურად ჩანს. თუ ობიექტივს, ფოკუსურ მანძილს, დიაფრაგმას ან
ფირის ტიპს ვერ არჩევ, იმ ადგილას დაწერე „ვერ დგინდება“ და დამაჯერებელი მნიშვნელობა არ მოიგონო.

სურათზე გამოსახული ადამიანი სახელით არ დაასახელო და არ მიუთითო, ვის ჰგავს — აღწერე მხოლოდ
ხილული ნიშნებით: სავარაუდო ასაკი, აღნაგობა, ჩაცმულობა, პოზა. მისაბაძად არ დაასახელო ცოცხალი
მხატვარი, ფოტოგრაფი ან ბრენდი — სტილი ზოგადი ენით აღწერე.

ააგე სტრიქონი ამ თანმიმდევრობით, წინადადებების გარეშე:
ობიექტი → მოქმედება → გარემო → კომპოზიცია და კამერის მდებარეობა → განათება → სტილი/მედიუმი →
ტექნიკა → პარამეტრები

წესები:
- კომპოზიციაში დაასახელე პლანის სიმსხო, ობიექტის ადგილი კადრში და კამერის სიმაღლე
- განათებაში დაასახელე წყარო, მიმართულება კამერასთან მიმართებით და ხასიათი (მკვეთრი თუ რბილი)
- ტექნიკაში მხოლოდ ის, რასაც სურათი ადასტურებს. მცირე სიღრმის ველი ჩანს; კონკრეტული ობიექტივი
  — როგორც წესი, არა.
- პარამეტრები: --ar კადრის ხილული პროპორციით, ფოტოგრაფიულ რეფერენსზე დამატებით --style raw.
  --no დაამატე მხოლოდ იმაზე, რაც კადრში არ არის, გენერატორი კი თავისით ამატებს ხოლმე.
- სტრიქონი ერთ ხაზზე დააბრუნე: ახსნის, ბულეტებისა და კომენტარის გარეშე.

მეორე ხაზზე ჩამოთვალე ყველა ველი, სადაც „ვერ დგინდება“ დაწერე.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-02 · Reference image → natural-language brief
`claude` `gpt` `gemini` — reverse, nano-banana, gpt-image

**EN**
```
You are given one reference image. Return a natural-language prompt for a conversational image
generator (Nano Banana or GPT-Image) that would produce a picture like it.

<image>{{image}}</image>

These generators read sentences, not descriptor lists. Write prose — but prose where every
sentence carries one decision, not atmosphere.

Describe ONLY what is visible. If you cannot tell the lens, focal length, aperture or film
stock, say "uncertain" rather than guessing a plausible value — and if you are uncertain about
all of it, simply leave camera language out instead of padding the brief with it.

Do not name anyone in the image or say who they resemble; use generic visible attributes only.
Do not name a living artist or a brand as a style shorthand.

Structure the brief in this order, one short paragraph each:
1. What the picture is — subject, what they are doing, where
2. How it is framed — shot size, subject placement, camera height and distance, aspect ratio
3. How it is lit — source, direction, quality, colour
4. How it is made — medium, treatment, palette, texture
5. What must NOT be in it — 3–5 items, each visibly absent from the reference

Rules:
- 120–200 words total
- Every adjective must be traceable to something in the frame. Cut "beautiful", "stunning",
  "epic", "masterpiece" — they steer nothing.
- Name colours as colours, not as moods
- End with the exclusion paragraph; do not bury it mid-brief

Then list every attribute you marked "uncertain".
```

**KA**
```
გაქვს ერთი რეფერენსი. დააბრუნე პრომპტი სასაუბრო გენერატორისთვის (Nano Banana ან GPT-Image) —
ისეთი, რომ მსგავსი სურათი გამოვიდეს.

<სურათი>{{სურათი}}</სურათი>

ეს გენერატორები წინადადებებს კითხულობენ და არა დესკრიპტორების სიას. დაწერე ტექსტად, ოღონდ ისე,
რომ ყოველი წინადადება ერთ კონკრეტულ გადაწყვეტილებას შეიცავდეს და არა განწყობას.

აღწერე მხოლოდ ის, რაც ჩანს. თუ ობიექტივს, ფოკუსურ მანძილს, დიაფრაგმას ან ფირს ვერ არჩევ,
დაწერე „ვერ დგინდება“ და ციფრი არ მოიგონო. თუ ტექნიკიდან არაფერი დგინდება, საერთოდ ამოაგდე
ეს ნაწილი და ტექსტი ცარიელი ტერმინებით არ გაავსო.

ადამიანი სახელით არ დაასახელო და არ მიუთითო, ვის ჰგავს — მხოლოდ ხილული ნიშნები. სტილის
აღსანიშნავად ცოცხალი მხატვრის ან ბრენდის სახელი არ გამოიყენო.

ააგე ბრიფი ამ თანმიმდევრობით, თითო მოკლე აბზაცად:
1. რა არის სურათზე — ობიექტი, მოქმედება, გარემო
2. როგორია კადრი — პლანის სიმსხო, ობიექტის ადგილი, კამერის სიმაღლე და მანძილი, პროპორცია
3. როგორია განათება — წყარო, მიმართულება, ხასიათი, ფერი
4. როგორია შესრულება — მედიუმი, დამუშავება, პალიტრა, ფაქტურა
5. რა არ უნდა იყოს — 3–5 პუნქტი, თითოეული ისეთი, რაც რეფერენსზე თვალსაჩინოდ არ არის

წესები:
- სულ 120–200 სიტყვა
- ყოველი ზედსართავი კადრში დანახულს უნდა ეყრდნობოდეს. ამოაგდე „მშვენიერი“, „განსაცვიფრებელი“,
  „ეპიკური“, „შედევრი“ — ისინი შედეგზე არ მოქმედებს.
- ფერი ფერად დაასახელე და არა განწყობად
- დაასრულე გამორიცხვების აბზაცით; შუაში არ ჩამარხო

ბოლოს ჩამოთვალე ყველა მახასიათებელი, რომელზეც „ვერ დგინდება“ დაწერე.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-03 · Style only, subject discarded
`claude` `gpt` `gemini` — style-transfer, reverse

**EN**
```
You are given one reference image. Extract its STYLE and discard its subject entirely, so the
style can be applied to something completely different.

<image>{{image}}</image>

Describe ONLY what is visible. If you cannot tell the medium, film stock, lens or rendering
method, write "uncertain" rather than guessing a plausible value.

Do not name a living artist, illustrator, studio or brand as shorthand for the style, and do not
identify anyone in the image. Describe the treatment in generic, observable terms.

Discard: who or what is depicted, the location, the action, the props. If a style term only makes
sense because of the subject — "wedding photography", "food styling" — replace it with what is
actually visible in the treatment.

Report these six, one line each:
1. MEDIUM — photograph, 3D render, watercolour, vector, print process, and what in the image shows it
2. PALETTE — 3–6 colours by plain name, each with its role: dominant, ground, accent
3. CONTRAST AND TONE — where the blacks sit, whether midtones are compressed, any colour cast
4. EDGE AND TEXTURE — line weight, grain, halftone, brush or paper texture, softness of edges
5. DETAIL — what is rendered in full and what is simplified or left out
6. FINISH — anything applied afterwards: vignette, misregistration, bloom, chromatic aberration

Then output one STYLE CLAUSE: a single comma-separated line, under 40 words, containing no
subject noun, ready to append to a prompt about an unrelated subject.
```

**KA**
```
გაქვს ერთი რეფერენსი. ამოკრიბე მისი სტილი და სრულად ჩამოაშორე ობიექტი, რომ ეს სტილი სულ სხვა
თემას მოარგო.

<სურათი>{{სურათი}}</სურათი>

აღწერე მხოლოდ ის, რაც ჩანს. თუ მედიუმს, ფირს, ობიექტივს ან რენდერის ხერხს ვერ არჩევ, დაწერე
„ვერ დგინდება“ და დამაჯერებელი ვარიანტი არ მოიგონო.

სტილის აღსანიშნავად არ დაასახელო ცოცხალი მხატვარი, ილუსტრატორი, სტუდია ან ბრენდი; სურათზე
გამოსახული ადამიანიც სახელით არ დაასახელო. დამუშავება ზოგადი, დაკვირვებადი ენით აღწერე.

ჩამოაშორე: ვინ ან რა არის გამოსახული, ადგილი, მოქმედება, საგნები. თუ სტილის ტერმინს აზრი
მხოლოდ ობიექტის გამო აქვს — „საქორწილო ფოტო“, „კვების ფოტოგრაფია“ — ჩაანაცვლე იმით, რაც
დამუშავებაში რეალურად ჩანს.

დააბრუნე ეს ექვსი, თითო ხაზად:
1. მედიუმი — ფოტო, 3D რენდერი, აკვარელი, ვექტორი, ბეჭდვის ხერხი; და რა მიანიშნებს ამაზე
2. პალიტრა — 3–6 ფერი მარტივი სახელით, თითოეულს მიაწერე როლი: მთავარი, ფონი, აქცენტი
3. კონტრასტი და ტონი — სად დგას შავი, შეკუმშულია თუ არა შუატონები, აქვს თუ არა ფერის გადახრა
4. კიდე და ფაქტურა — ხაზის სისქე, მარცვლოვნება, ჰალფტონი, ფუნჯის ან ქაღალდის ფაქტურა, კიდეების სირბილე
5. დეტალი — რა არის ბოლომდე დამუშავებული და რა — გამარტივებული ან საერთოდ გამოტოვებული
6. დასრულება — რაც შემდეგ დაედო: ვინიეტი, ფენების აცდენა, შუქის გადაღვრა, ქრომატული აბერაცია

ბოლოს დააბრუნე ერთი სტილის კლაუზა: ერთი სტრიქონი, 40 სიტყვამდე, ობიექტის სახელის გარეშე —
ისეთი, რომ ნებისმიერ სხვა პრომპტს ბოლოში მიაწერო.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-04 · Lighting setup as a reusable clause
`claude` `gpt` `gemini` — lighting, reverse

**EN**
```
You are given one reference image. Extract only its lighting setup.

<image>{{image}}</image>

Read the light from the evidence in the frame: shadow direction, shadow edge hardness,
catchlights, falloff across the subject, reflections, the colour of the shadows. Describe ONLY
what that evidence supports. If a source is not readable from it, write "uncertain" — never name
a plausible fixture, modifier or time of day you cannot actually see.

Do not identify anyone in the image.

Report:
- KEY — direction as a clock position relative to camera, plus height (above / eye level / below),
  and the evidence you read it from
- QUALITY — hard or soft, and how you can tell (shadow edge width)
- RATIO — approximate key-to-fill difference in stops, or "uncertain"
- FILL — present or absent; if present, its source (bounce, ambient, second light) and direction
- SEPARATION — rim, kicker, hair or background light, with direction. If none, write "none".
- PRACTICALS — any light source visible inside the frame
- COLOUR — key versus fill or background as warm / neutral / cool, plus any deliberate gel colour
- SOURCE AND TIME — daylight, window, overcast, artificial, mixed, or "uncertain"

Then output one LIGHTING CLAUSE: a single comma-separated line under 30 words describing the
light only — no subject, no setting — reusable in a prompt about anything.
```

**KA**
```
გაქვს ერთი რეფერენსი. ამოკრიბე მხოლოდ განათების სქემა.

<სურათი>{{სურათი}}</სურათი>

განათება კადრში არსებული ნიშნებით წაიკითხე: ჩრდილის მიმართულება, ჩრდილის კიდის სიმკვეთრე,
ბზინვარება თვალებში, შუქის დაცემა ობიექტზე, ანარეკლები, ჩრდილის ფერი. აღწერე მხოლოდ ის, რასაც
ეს ნიშნები ადასტურებს. თუ წყარო აქედან არ იკითხება, დაწერე „ვერ დგინდება“ — არ დაასახელო
ხელსაწყო, მოდიფიკატორი ან დღის მონაკვეთი, რომელსაც რეალურად ვერ ხედავ.

სურათზე გამოსახული ადამიანი სახელით არ დაასახელო.

დააბრუნე:
- მთავარი შუქი — მიმართულება საათის ციფერბლატის მიხედვით, კამერასთან მიმართებით, პლუს სიმაღლე
  (ზემოდან / თვალის დონეზე / ქვემოდან) და რა ნიშნით დაადგინე
- ხასიათი — მკვეთრი თუ რბილი და საიდან ჩანს (ჩრდილის კიდის სიგანე)
- თანაფარდობა — მთავარსა და შემავსებელ შუქს შორის სხვაობა საფეხურებში, ან „ვერ დგინდება“
- შემავსებელი — არის თუ არა; თუ არის, წყარო (ამრეკლი, გარემოს შუქი, მეორე ხელსაწყო) და მიმართულება
- გამოყოფა — კონტურული, გვერდითი, თმის ან ფონის შუქი, მიმართულებით. თუ არ არის, დაწერე „არ არის“.
- კადრში ხილული წყაროები — ნათურა, ფანჯარა, ეკრანი, ცეცხლი
- ფერი — მთავარი შუქი შემავსებელთან და ფონთან შედარებით: თბილი / ნეიტრალური / ცივი, პლუს
  შეგნებულად დადებული ფერადი ფილტრი
- წყარო და დრო — დღის შუქი, ფანჯარა, ღრუბლიანი ამინდი, ხელოვნური, შერეული ან „ვერ დგინდება“

ბოლოს დააბრუნე ერთი განათების კლაუზა: ერთი სტრიქონი, 30 სიტყვამდე, მხოლოდ შუქზე — ობიექტისა და
გარემოს გარეშე, ისე, რომ ნებისმიერ პრომპტში ჩაჯდეს.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-05 · Character reference sheet from one photo
`claude` `gpt` `gemini` — character, consistency

**EN**
```
You are given one photograph of a person. Return a character description that lets an image
generator regenerate the SAME character consistently across new images.

<image>{{image}}</image>

Hard limits:
- Do not name the person, do not guess their name, nationality or profession, and never state
  that they resemble any real or public figure.
- Treat the result as an original fictional character assembled from visible attributes only.
- Nothing in the output may function as a likeness of a real identifiable individual.

Describe ONLY what is visible. If hair colour under a hat, eye colour, or height cannot be seen,
write "uncertain" — never fill the gap with a plausible value, because a guessed constant is
exactly what breaks consistency in the next twenty images.

Output:

IDENTITY LOCK — 8–12 fixed attributes that must appear in every future prompt: approximate age
range, build, face shape, hair (length, texture, colour, how it is worn), eyebrows, eye shape and
colour, nose, jaw, skin tone, facial hair, distinguishing marks. One short phrase each.

WARDROBE — the outfit item by item, with colour and material. Mark each item as SIGNATURE (part
of the character) or INCIDENTAL (true only of this one photo).

DEFAULT EXPRESSION AND POSTURE — resting expression, how the head sits, the shoulder line.

NOT DETERMINABLE — every attribute you could not see. These stay out of future prompts until you
decide them deliberately and then fix them.

CHARACTER STRING — one comma-separated line under 60 words containing the IDENTITY LOCK only:
no setting, no lighting, no pose.
```

**KA**
```
გაქვს ერთი ფოტო, რომელზეც ადამიანია. დააბრუნე პერსონაჟის აღწერა, რომლითაც გენერატორი იმავე
პერსონაჟს ახალ სურათებში სტაბილურად გაიმეორებს.

<სურათი>{{სურათი}}</სურათი>

მკაცრი შეზღუდვები:
- ადამიანი სახელით არ დაასახელო, არ გამოიცნო მისი სახელი, ეროვნება ან პროფესია და არასდროს
  დაწერო, ვის ჰგავს რეალური ან ცნობილი ადამიანებიდან.
- შედეგი განიხილე როგორც ორიგინალური გამოგონილი პერსონაჟი, მხოლოდ ხილული ნიშნებისგან აწყობილი.
- გამოსავალი არ უნდა მუშაობდეს რეალური, ამოსაცნობი ადამიანის პორტრეტულ აღწერად.

აღწერე მხოლოდ ის, რაც ჩანს. თუ ქუდის ქვეშ თმის ფერი, თვალის ფერი ან სიმაღლე არ ჩანს, დაწერე
„ვერ დგინდება“ და ხვრელი დამაჯერებელი ვარიანტით არ ამოავსო — სწორედ გამოცნობილი მუდმივა შლის
სტაბილურობას მომდევნო ოც სურათში.

გამოსავალი:

ფიქსირებული ნიშნები — 8–12 მახასიათებელი, რომლებიც ყოველ მომავალ პრომპტში უნდა გაიმეოროს:
სავარაუდო ასაკი, აღნაგობა, სახის ფორმა, თმა (სიგრძე, ტექსტურა, ფერი, როგორ არის დავარცხნილი),
წარბები, თვალის ფორმა და ფერი, ცხვირი, ყბა, კანის ტონი, სახის ბალანი, გამორჩეული ნიშნები.
თითოეული — ერთი მოკლე ფრაზა.

ჩაცმულობა — ტანსაცმელი ცალ-ცალკე, ფერითა და მასალით. თითოეულს მიაწერე: მუდმივი (პერსონაჟის
ნაწილია) თუ შემთხვევითი (მხოლოდ ამ ფოტოს ეხება).

ნაგულისხმევი გამომეტყველება და პოზა — მშვიდი სახის გამომეტყველება, თავის მდებარეობა, მხრების ხაზი.

ვერ დგინდება — ყველა ნიშანი, რომელიც ვერ დაინახე. ისინი მომავალ პრომპტებში არ ჩაწერო, სანამ
შეგნებულად არ გადაწყვეტ და არ დააფიქსირებ.

პერსონაჟის სტრიქონი — ერთი ხაზი, 60 სიტყვამდე, მხოლოდ ფიქსირებული ნიშნებით: გარემოს, განათებისა
და პოზის გარეშე.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-06 · Video still → shot spec
`claude` `gpt` `gemini` — video, veo, sora

**EN**
```
You are given one still frame from a video, or one image to be treated as a frame. Return a shot
spec for a video generator (Veo, Sora, Runway).

<image>{{image}}</image>

Describe ONLY what is visible in the frame. Camera movement is not visible in a still — do not
invent a dolly or a pan. If motion cannot be inferred from motion blur, streaking or a tilted
horizon, write "no motion evidence" and put any movement under MOVEMENT (PROPOSED), labelled as
your proposal rather than as something you observed. If the lens or format cannot be read, write
"uncertain".

Do not identify anyone in the frame, and do not name a film, director or cinematographer as a
style shorthand.

Output these fields, one line each:
SHOT SIZE — wide / medium / close, and what the frame edge cuts off
CAMERA — height, angle, approximate distance, aspect ratio, depth of field as visible
SUBJECT AND ACTION — what is in frame, and the single action it performs across the shot
SETTING — the location and the three details that carry it
LIGHTING — source, direction, quality, colour
MOOD — two adjectives, each tied to something visible
MOVEMENT (PROPOSED) — one camera move, or "static", with the reason
AUDIO — ambient bed, one or two specific diegetic sounds, and whether anyone speaks; write
"no dialogue" if not
DURATION — a length that fits one action, 5–8 seconds

Then output the spec as a single-paragraph prompt: present tense, one action, no shot list, no
cuts.
```

**KA**
```
გაქვს ვიდეოს ერთი კადრი (ან სურათი, რომელსაც კადრად განვიხილავთ). დააბრუნე კადრის სპეციფიკაცია
ვიდეოგენერატორისთვის — Veo, Sora, Runway.

<სურათი>{{სურათი}}</სურათი>

აღწერე მხოლოდ ის, რაც კადრში ჩანს. კამერის მოძრაობა სტატიკურ კადრში არ ჩანს — არ მოიგონო
ნაოსნობა ან პანორამა. თუ მოძრაობაზე არც გადაბუნდოვნება, არც ჰორიზონტის დახრა არ მიანიშნებს,
დაწერე „მოძრაობის კვალი არ ჩანს“ და შენი ვარიანტი ცალკე, „შემოთავაზებულ მოძრაობაში“ ჩაწერე.
თუ ობიექტივი ან ფორმატი არ იკითხება, დაწერე „ვერ დგინდება“.

კადრში გამოსახული ადამიანი სახელით არ დაასახელო; სტილის აღსანიშნავად ფილმის, რეჟისორის ან
ოპერატორის სახელი არ გამოიყენო.

დააბრუნე ეს ველები, თითო ხაზად:
პლანის სიმსხო — ზოგადი / საშუალო / ახლო; და რას ჭრის კადრის კიდე
კამერა — სიმაღლე, კუთხე, სავარაუდო მანძილი, პროპორცია, სიღრმის ველი როგორც ჩანს
ობიექტი და მოქმედება — რა არის კადრში და ერთი მოქმედება, რომელსაც კადრის მანძილზე ასრულებს
გარემო — ადგილი და სამი დეტალი, რომელიც ამ ადგილს ატარებს
განათება — წყარო, მიმართულება, ხასიათი, ფერი
განწყობა — ორი ზედსართავი, თითოეული კადრში დანახულს მიბმული
შემოთავაზებული მოძრაობა — ერთი მოძრაობა ან „სტატიკა“, მიზეზის მითითებით
ხმა — გარემოს ფონი, ერთი ან ორი კონკრეტული ხმა კადრიდან და ლაპარაკობს თუ არა ვინმე; თუ არა,
დაწერე „დიალოგის გარეშე“
ხანგრძლივობა — 5–8 წამი, ერთ მოქმედებაზე მორგებული

ბოლოს ეს სპეციფიკაცია ერთ აბზაცად გადააკეთე: აწმყო დროში, ერთი მოქმედებით, კადრების სიისა და
მონტაჟის გარეშე.

შედეგად დააბრუნე ინგლისური პრომპტი — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-07 · Diff two images into a prompt change
`claude` `gpt` `gemini` — comparison, iteration

**EN**
```
You are given two images. A is what you have; B is what you want.

<image_a>{{image_a}}</image_a>
<image_b>{{image_b}}</image_b>
The prompt that produced A: {{prompt}}

Compare ONLY what is visible. If a difference could be explained by the generator's randomness
rather than by the prompt — a hand position, a fold of cloth, one strand of hair — say so instead
of inventing a prompt clause for it. Where you cannot tell whether a difference comes from lens,
lighting or post-processing, write "uncertain".

Do not identify anyone in either image, and do not name an artist or brand.

Output a table, one row per real difference:
DIMENSION | A | B | prompt-controllable? (yes / no / partly)

Cover, in this order: subject, action and pose, setting, composition and crop, camera height and
distance, depth of field, lighting, colour and contrast, medium and finish.

Then: THE BIGGEST GAP — the single change that accounts for most of the distance between A and B,
in one sentence.

Then: CORRECTED PROMPT — the prompt for A rewritten so it lands closer to B. Change only the
clauses the table marked controllable. Do not rebuild the description from scratch.

Then: CHANGES — each edited clause as old → new, one line each. Nothing else.
```

**KA**
```
გაქვს ორი სურათი. A — რაც გაქვს; B — რაც გინდა.

<სურათი_a>{{სურათი_a}}</სურათი_a>
<სურათი_b>{{სურათი_b}}</სურათი_b>
პრომპტი, რომელმაც A დააგენერირა: {{პრომპტი}}

შეადარე მხოლოდ ის, რაც ჩანს. თუ სხვაობა გენერატორის შემთხვევითობით აიხსნება და არა პრომპტით —
ხელის მდებარეობა, ქსოვილის ნაკეცი, თმის ღერი — ეს პირდაპირ დაწერე და ამის გამო პრომპტში ახალი
პუნქტი არ მოიგონო. სადაც ვერ არჩევ, სხვაობა ობიექტივიდან მოდის, განათებიდან თუ დამუშავებიდან,
დაწერე „ვერ დგინდება“.

ვერცერთ სურათზე ადამიანი სახელით არ დაასახელო; მხატვრისა და ბრენდის სახელი არ გამოიყენო.

დააბრუნე ცხრილი, თითო რეალურ სხვაობაზე ერთი სტრიქონი:
პარამეტრი | A | B | იმართება პრომპტით? (კი / არა / ნაწილობრივ)

მოიცავი ამ თანმიმდევრობით: ობიექტი, მოქმედება და პოზა, გარემო, კომპოზიცია და კადრირება, კამერის
სიმაღლე და მანძილი, სიღრმის ველი, განათება, ფერი და კონტრასტი, მედიუმი და დამუშავება.

შემდეგ: მთავარი სხვაობა — ერთი ცვლილება, რომელზეც A-სა და B-ს შორის მანძილის უდიდესი ნაწილი
მოდის. ერთი წინადადება.

შემდეგ: გასწორებული პრომპტი — A-ს პრომპტი გადაწერილი ისე, რომ B-სთან ახლოს მოვიდეს. შეცვალე
მხოლოდ ის, რაც ცხრილში პრომპტით მართვადად მონიშნე. აღწერა თავიდან არ ააგო.

შემდეგ: ცვლილებები — ყოველი შეცვლილი ადგილი როგორც ძველი → ახალი, თითო ხაზად. სხვა არაფერი.

ცხრილი და შენიშვნები დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
გასწორებული პრომპტი კი ინგლისურად დააბრუნე — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-08 · Prompt repair from prompt + result
`claude` `gpt` `gemini` — debugging, iteration

**EN**
```
You are given a prompt and the image it produced. The image missed. Find the clause responsible.

<prompt>{{prompt}}</prompt>
<image>{{image}}</image>
Generator: {{generator}}
What I wanted instead: {{intent}}

Judge ONLY what is visible in the image against what the prompt actually says, word for word. If
the image is a fair rendering of the prompt and the prompt simply never asked for what I wanted,
say so plainly — that is the most common cause and the easiest one to talk yourself out of. Where
you cannot tell from the image whether a clause took effect, write "uncertain".

Do not identify anyone in the image, and do not put an artist's or brand's name into the repair.

Output:
1. WHAT THE PROMPT ASKED FOR — one sentence, strictly as written
2. WHAT THE IMAGE SHOWS — one sentence, observation only
3. THE MISS — the gap between them, one sentence
4. CAUSE — exactly one of: clause missing / clause too vague / two clauses in conflict / clause
   placed too late to carry weight / parameter wrong / the generator cannot do this. Quote the
   clause at fault, or write "not present in the prompt".
5. WHY — one sentence. No general prompting advice.
6. CORRECTED PROMPT — the full prompt with the smallest edit that fixes it. Change nothing that
   was already working.
7. WHAT TO CHECK IN THE NEXT RENDER — one thing.

If the cause is that the generator cannot do this, stop after step 5 and name the one thing to
do instead — a different generator, an edit pass, or a different composition.
```

**KA**
```
გაქვს პრომპტი და სურათი, რომელიც მან დააგენერირა. შედეგი ამცდა. იპოვე, რომელმა ადგილმა გამოიწვია.

<პრომპტი>{{პრომპტი}}</პრომპტი>
<სურათი>{{სურათი}}</სურათი>
გენერატორი: {{გენერატორი}}
რა მინდოდა სინამდვილეში: {{განზრახვა}}

შეაფასე მხოლოდ ის, რაც სურათზე ჩანს, და შეადარე იმას, რაც პრომპტში სიტყვასიტყვით წერია. თუ
სურათი პრომპტის სამართლიანი შესრულებაა და პრომპტს უბრალოდ არასდროს უთხოვია ის, რაც მე მინდოდა,
ეს პირდაპირ დაწერე — ეს ყველაზე ხშირი მიზეზია და ყველაზე ადვილი უგულებელსაყოფი. სადაც სურათიდან
ვერ დგინდება, იმუშავა თუ არა კონკრეტულმა პუნქტმა, დაწერე „ვერ დგინდება“.

სურათზე გამოსახული ადამიანი სახელით არ დაასახელო; გასწორებულ პრომპტში მხატვრის ან ბრენდის
სახელი არ ჩადო.

გამოსავალი:
1. რას ითხოვდა პრომპტი — ერთი წინადადება, მკაცრად ისე, როგორც წერია
2. რა ჩანს სურათზე — ერთი წინადადება, მხოლოდ დაკვირვება
3. სხვაობა — ერთი წინადადება
4. მიზეზი — ზუსტად ერთი: პუნქტი აკლია / პუნქტი ბუნდოვანია / ორი პუნქტი ერთმანეთს ეწინააღმდეგება /
   პუნქტი ძალიან ბოლოში დგას და წონას კარგავს / პარამეტრი არასწორია / გენერატორი ამას ვერ აკეთებს.
   დაასახელე პრობლემური ადგილი ციტატით ან დაწერე „პრომპტში არ არის“.
5. რატომ — ერთი წინადადება. ზოგადი რჩევები პრომპტინგზე არ დაწერო.
6. გასწორებული პრომპტი — სრული პრომპტი მინიმალური ჩასწორებით. ის, რაც უკვე მუშაობდა, არ შეცვალო.
7. რას დავაკვირდე შემდეგ რენდერში — ერთი რამ.

თუ მიზეზი ის არის, რომ გენერატორი ამას ვერ აკეთებს, გაჩერდი მე-5 პუნქტზე და დაასახელე ერთი
ალტერნატივა: სხვა გენერატორი, ცალკე სარედაქციო გავლა ან სხვა კომპოზიცია.

პუნქტები 1–5 და 7 დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
გასწორებული პრომპტი ინგლისურად დააბრუნე — გენერატორი ქართულს საიმედოდ არ იღებს.
```

---

### RP-09 · Brand visual language from a set of images
`claude` `gpt` `gemini` — brand, style-guide

**EN**
```
You are given 3–5 images from one brand's own existing visual output. Return the style rules they
share, as a clause you can reuse.

Brand: {{brand}}
<images>{{images}}</images>

Use this only for a brand you are authorised to produce work for. Describe the treatment in
generic, observable terms — never name a living photographer, illustrator or agency, and never
name another brand whose look should be copied. Do not identify anyone appearing in the images.

Describe ONLY what is visible across the set. A trait counts as a rule only if it appears in at
least three of the images; anything appearing once goes under VARIES, not under the rules. If you
cannot tell whether something is a deliberate rule or an accident of one shoot, write "uncertain"
rather than promoting it.

Output:

CONSISTENT ACROSS THE SET — 6–10 rules, one line each, covering: palette with rough proportions,
lighting, composition and crop, camera distance to subject, depth of field, colour and contrast
treatment, texture and finish, how people are framed and posed, how product is placed, use of
negative space.

VARIES — traits present in only one or two images.

NOT VISIBLE FROM THESE IMAGES — things a brand usually specifies that this set does not show:
typography, motion, formats other than the ones supplied.

STYLE CLAUSE — one comma-separated line under 45 words, subject-free, ready to append to any prompt.

DO-NOT LIST — 5–8 items, each one visibly absent from every image in the set and something a
generator would otherwise add by default.
```

**KA**
```
გაქვს ერთი ბრენდის 3–5 სურათი მისივე არსებული მასალიდან. ამოკრიბე საერთო სტილის წესები და
დააბრუნე მრავალჯერ გამოსაყენებელი კლაუზის სახით.

ბრენდი: {{ბრენდი}}
<სურათები>{{სურათები}}</სურათები>

ეს პრომპტი მხოლოდ იმ ბრენდზე გამოიყენე, რომლისთვისაც მუშაობის უფლება გაქვს. დამუშავება ზოგადი,
დაკვირვებადი ენით აღწერე — არ დაასახელო ცოცხალი ფოტოგრაფი, ილუსტრატორი ან სააგენტო და არ
დაასახელო სხვა ბრენდი, რომლის იერსახეც უნდა გამეორდეს. სურათებზე გამოსახული ადამიანები სახელით
არ დაასახელო.

აღწერე მხოლოდ ის, რაც მთელ ნაკრებში ჩანს. ნიშანი წესად მაშინ ჩაითვლება, თუ სულ მცირე სამ სურათზე
მეორდება; ერთხელ გამოჩენილი მიდის სექციაში „იცვლება“ და არა წესებში. თუ ვერ არჩევ, ეს შეგნებული
წესია თუ ერთი გადაღების შემთხვევითობა, დაწერე „ვერ დგინდება“ და წესებში არ გადაიტანო.

გამოსავალი:

მუდმივი მთელ ნაკრებში — 6–10 წესი, თითო ხაზად: პალიტრა მიახლოებითი პროპორციებით, განათება,
კომპოზიცია და კადრირება, კამერის მანძილი ობიექტამდე, სიღრმის ველი, ფერისა და კონტრასტის
დამუშავება, ფაქტურა და დასრულება, როგორ არის ადამიანი აყვანილი კადრში და როგორ პოზაშია,
სად დევს პროდუქტი, როგორ გამოიყენება თავისუფალი სივრცე.

იცვლება — ნიშნები, რომლებიც მხოლოდ ერთ ან ორ სურათზეა.

ამ სურათებიდან არ ჩანს — ის, რასაც ბრენდი ჩვეულებრივ აწესებს, ამ ნაკრები კი არ აჩვენებს:
ტიპოგრაფია, მოძრაობა, სხვა ფორმატები.

სტილის კლაუზა — ერთი სტრიქონი, 45 სიტყვამდე, ობიექტის სახელის გარეშე, ნებისმიერ პრომპტზე
მისაწერად.

აკრძალულების სია — 5–8 პუნქტი; თითოეული ისეთი, რაც ნაკრების არცერთ სურათზე არ არის, გენერატორი
კი ჩვეულებრივ თავისით ამატებს.

შედეგად სტილის კლაუზა და აკრძალულების სია ინგლისურად დააბრუნე — გენერატორი ქართულს საიმედოდ
არ იღებს. დანარჩენი სექციები დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```
