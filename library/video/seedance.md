# Seedance 2.5

ByteDance. Six-part formula, one generation: `[subject] · [action] · [environment] · [camera movement + speed] ·
[style] · [constraints]`, 60–100 words, and the first 20–30 words carry the most weight — subject and action go
there, style never does. Shot-spec fundamentals: [`../../references/frameworks.md`](../../references/frameworks.md) §8.
Clips run **4–15 seconds** at **480p / 720p / 1080p**, in **21:9, 16:9, 4:3, 1:1, 3:4 or 9:16**, and come out as
**MP4 with synchronised audio** — so the audio line is part of the render, not an afterthought.
One generation accepts up to **9 images** (JPEG/PNG/WebP), **3 video clips** (MP4/MOV, 15s combined) and
**3 audio files** (WAV/MP3), called by name inside the prompt text as `@image1`, `@video1`, `@audio1`.
Text-to-video, image-to-video, video extension and motion transfer are the same prompt with different references attached.
Several shots inside one clip are written as timecoded blocks — `[0:00–0:04] AERIAL WIDE — …` — and every block
still states its own camera movement.

**On the Georgian block.** Seedance reads English far more reliably than Georgian, so the `**KA**` block is a
*working version*: the same spec in Georgian, so you can build the shot and argue about it in your own language —
then paste the English string after the `---` line. Reference tokens stay in Latin script in both blocks: `@image1`
is a filename, not a word.

Seedance 2.5, ByteDance. ქართული ბლოკი სამუშაო ვერსიაა — რენდერისთვის გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
ხანგრძლივობა 4–15 წამი, გარჩევადობა 480p / 720p / 1080p, თანაფარდობა 21:9, 16:9, 4:3, 1:1, 3:4 ან 9:16; გამოსავალი — MP4 სინქრონული ხმით.
ერთ რენდერში შეგიძლია ატვირთო 9 სურათს (JPEG/PNG/WebP), 3 ვიდეოკლიპს (MP4/MOV, ჯამში 15 წამი) და 3 აუდიოფაილს (WAV/MP3); პრომპტში მათ იძახებ როგორც `@image1`, `@video1`, `@audio1`.
ფორმულა ექვსნაწილიანია — სუბიექტი, მოქმედება, გარემო, კამერის მოძრაობა, სტილი, შეზღუდვები — 60–100 სიტყვა, და ყველაზე მეტი წონა პირველ 20–30 სიტყვას აქვს.
მრავალკადრიანი კლიპი ტაიმკოდიანი ბლოკებით იწერება; ყოველ ბლოკს თავისი კამერის მოძრაობა სჭირდება.

---

### SD-01 · The six-part formula, plainly
`seedance` — text-to-video, formula, georgia

The structure with nothing hidden: subject, action, environment, camera, style, constraints, in that order.
Everything that matters is inside the first thirty words.

**EN**
```
A dark green wine bottle with a hand-written paper label rests on a rough stone shelf in a Kakheti marani, turning slowly on its base so the label comes fully to camera. Camera: slow dolly-in at a steady crawl, roughly 10 percent over the clip, no orbit. Lighting: one high window at frame left, hard afternoon shaft across the label, the vaulted ceiling behind unlit. Style: documentary, muted colour. Audio: stone-cellar room tone, faint dripping, no music. 8 seconds, 1080p, 16:9. No hands, no text overlays.
```

**KA**
```
მუქი მწვანე ღვინის ბოთლი ხელნაწერი ქაღალდის ეტიკეტით დგას ქვის უხეშ თაროზე, კახურ მარანში, და ნელა ტრიალებს საკუთარ ძირზე, სანამ ეტიკეტი ბოლომდე კამერისკენ არ მოტრიალდება. კამერა: ნელი მიახლოება, თანაბარი სიჩქარით, მთელ კლიპზე დაახლოებით 10%, ორბიტის გარეშე. განათება: ერთი მაღალი ფანჯარა კადრის მარცხნივ, შუადღის მკვეთრი სხივი ეტიკეტზე; თაღოვანი ჭერი უკან განათების გარეშე რჩება. სტილი: დოკუმენტური, ჩახშული ფერები. აუდიო: ქვის მარნის ტონი, სუსტი წვეთები, მუსიკის გარეშე. 8 წამი, 1080p, 16:9. ხელები არ ჩანს, ტექსტური წარწერა არ არის.
---
A dark green wine bottle with a hand-written paper label rests on a rough stone shelf in a Kakheti marani, turning slowly on its base so the label comes fully to camera. Camera: slow dolly-in at a steady crawl, roughly 10 percent over the clip, no orbit. Lighting: one high window at frame left, hard afternoon shaft across the label, the vaulted ceiling behind unlit. Style: documentary, muted colour. Audio: stone-cellar room tone, faint dripping, no music. 8 seconds, 1080p, 16:9. No hands, no text overlays.
```

---

### SD-02 · Animating a still with `@image1`
`seedance` — image-to-video, reference

Supply one still as `@image1`. Prompt the motion, not the picture: the frame already carries composition,
colour and light, and re-describing them invites the model to rebuild them differently.

**EN**
```
@image1 is a still of a potter's bench: a half-finished clay bowl centred on the wheel, tools laid out behind it. Animate @image1 without changing its framing, colour or light. The only motion is the wheel turning at one slow revolution per clip and a hand entering from frame right at the third second to steady the rim. Camera: hold, then a 6 percent push-in over the last two seconds. Lighting: keep the source window light from frame left. Audio: wheel bearing hum, wet clay, no music. 7 seconds, 1080p, 4:3.
```

**KA**
```
@image1 — ჭურჭლის ოსტატის მაგიდის კადრი: ჩარხზე ნახევრად გამოყვანილი თიხის ჯამი, უკან ინსტრუმენტები. გააცოცხლე @image1 ისე, რომ კადრირება, ფერი და განათება არ შეიცვალოს. ერთადერთი მოძრაობა: ჩარხი ნელა ტრიალებს — მთელ კლიპზე ერთი სრული ბრუნი — და მესამე წამზე მარჯვნიდან შემოდის ხელი, რომელიც ჯამის კიდეს ასწორებს. კამერა: ჯერ უძრავია, ბოლო ორ წამში 6%-იანი მიახლოება. განათება: შეინარჩუნე საწყისი სურათის ფანჯრის შუქი კადრის მარცხნიდან. აუდიო: ჩარხის საკისრის გუგუნი, სველი თიხა, მუსიკის გარეშე. 7 წამი, 1080p, 4:3.
---
@image1 is a still of a potter's bench: a half-finished clay bowl centred on the wheel, tools laid out behind it. Animate @image1 without changing its framing, colour or light. The only motion is the wheel turning at one slow revolution per clip and a hand entering from frame right at the third second to steady the rim. Camera: hold, then a 6 percent push-in over the last two seconds. Lighting: keep the source window light from frame left. Audio: wheel bearing hum, wet clay, no music. 7 seconds, 1080p, 4:3.
```

---

### SD-03 · Product from `@image1`, place from `@image2`
`seedance` — multi-reference, product

Two references with two different jobs: `@image1` is a clean packshot of the product, `@image2` a photograph of
where it should stand. Say which reference governs what, or the model averages them.

**EN**
```
@image1 is a packshot of a 250 ml honey jar with its label; @image2 is a photograph of a wooden veranda above a Guria tea slope. Place the jar from @image1 on the veranda rail in @image2, keeping the jar's label, lid and proportions exactly as supplied and the veranda's geometry unchanged. Camera: slow arc left around the jar, 25 degrees, constant speed. Lighting: low side sun from frame right, long shadow across the rail. Audio: cicadas, wind in tea bushes, no music. 6 seconds, 1080p, 16:9.
```

**KA**
```
@image1 — 250 მლ თაფლის ქილის პეკშოტი ეტიკეტით; @image2 — ხის აივნის ფოტო გურული ჩაის ფერდობის თავზე. დადგი @image1-ის ქილა @image2-ის აივნის მოაჯირზე; ქილის ეტიკეტი, თავსახური და პროპორცია დატოვე ზუსტად ისე, როგორც რეფერენსშია, აივნის გეომეტრია კი — უცვლელი. კამერა: ნელი რკალი მარცხნივ ქილის გარშემო, 25 გრადუსი, მუდმივი სიჩქარით. განათება: დაბალი გვერდითი მზე კადრის მარჯვნიდან, გრძელი ჩრდილი მოაჯირზე. აუდიო: ჭრიჭინები, ქარი ჩაის ბუჩქებში, მუსიკის გარეშე. 6 წამი, 1080p, 16:9.
---
@image1 is a packshot of a 250 ml honey jar with its label; @image2 is a photograph of a wooden veranda above a Guria tea slope. Place the jar from @image1 on the veranda rail in @image2, keeping the jar's label, lid and proportions exactly as supplied and the veranda's geometry unchanged. Camera: slow arc left around the jar, 25 degrees, constant speed. Lighting: low side sun from frame right, long shadow across the rail. Audio: cicadas, wind in tea bushes, no music. 6 seconds, 1080p, 16:9.
```

---

### SD-04 · Three shots on timecode, one generation
`seedance` — multi-shot, timecode, georgia

The cuts happen inside a single 12-second render. Each block gets its own shot size and camera; lighting and
audio are stated once, globally, so the three shots match.

**EN**
```
Three shots in one 12-second generation, 1080p, 16:9, bakery at dawn.
[0:00–0:04] WIDE — a bakery room, the round tone oven set into the floor, flour dust in the air. Camera: slow push-in, 8 percent.
[0:04–0:08] CLOSE — a baker's hands hook a shoti off the clay wall with an iron rod. Camera: static.
[0:08–0:12] MEDIUM — the loaf lands on a wooden rack, steam lifting. Camera: slow tilt up at the loaf's own speed.
Lighting throughout: orange coals from below, one bare bulb behind the baker. Audio: coals ticking, iron on clay, crust crackling, no music.
```

**KA**
```
სამი კადრი ერთ 12-წამიან რენდერში, 1080p, 16:9, საცხობი გამთენიისას.
[0:00–0:04] ზოგადი პლანი — საცხობის ოთახი, იატაკში ჩაშენებული მრგვალი თონე, ჰაერში ფქვილის მტვერი. კამერა: ნელი მიახლოება, 8%.
[0:04–0:08] ახლო პლანი — მცხობელის ხელები რკინის კაუჭით აძრობს შოთს თონის თიხის კედელს. კამერა: სტატიკური.
[0:08–0:12] საშუალო პლანი — პური ხის თაროზე ეშვება და ორთქლი ადის. კამერა: ნელი ტილტი ზემოთ, ზუსტად პურის სიჩქარით.
განათება მთელ სექვენციაზე: თონის ნარინჯისფერი ნახშირი ქვემოდან, ერთი შიშველი ნათურა მცხობელის უკან. აუდიო: ნახშირის ტკაცუნი, რკინა თიხაზე, ქერქის ხრაშუნი, მუსიკის გარეშე.
---
Three shots in one 12-second generation, 1080p, 16:9, bakery at dawn.
[0:00–0:04] WIDE — a bakery room, the round tone oven set into the floor, flour dust in the air. Camera: slow push-in, 8 percent.
[0:04–0:08] CLOSE — a baker's hands hook a shoti off the clay wall with an iron rod. Camera: static.
[0:08–0:12] MEDIUM — the loaf lands on a wooden rack, steam lifting. Camera: slow tilt up at the loaf's own speed.
Lighting throughout: orange coals from below, one bare bulb behind the baker. Audio: coals ticking, iron on clay, crust crackling, no music.
```

---

### SD-05 · Extending `@video1` past its last frame
`seedance` — video-extension, continuity

Supply the clip you already have as `@video1`. The extension is a continuation, not a new shot: name the motion
that is already running and say where it ends, and forbid relighting.

**EN**
```
@video1 is a 6-second clip that ends with a train pulling into a rural platform. Extend @video1 by 8 more seconds from its final frame, matching its grade, grain and lens exactly. Continue the motion already there: the train slows to a stop, doors stay closed, nobody steps out. Camera: continue the existing slow pan right, decelerating to a full stop by the fourth second. Lighting: keep the source's overcast top light, no relight. Audio: brakes releasing, a bell on the platform, wind, no music. 8 seconds, 720p, 16:9.
```

**KA**
```
@video1 — 6-წამიანი კლიპი, რომელიც სოფლის პერონზე შემომავალი მატარებლით მთავრდება. გააგრძელე @video1 ბოლო კადრიდან კიდევ 8 წამით და შეინარჩუნე მისი ფერთა კორექცია, მარცვლოვნება და ობიექტივის ხასიათი. განაგრძე უკვე დაწყებული მოძრაობა: მატარებელი ჩერდება, კარები დახურული რჩება, არავინ ჩამოდის. კამერა: განაგრძე არსებული ნელი პანორამა მარჯვნივ და მეოთხე წამისთვის სრულად გააჩერე. განათება: დატოვე წყაროს ღრუბლიანი ზედა შუქი, გადანათების გარეშე. აუდიო: სამუხრუჭე ჰაერის გამოშვება, პერონის ზარი, ქარი, მუსიკის გარეშე. 8 წამი, 720p, 16:9.
---
@video1 is a 6-second clip that ends with a train pulling into a rural platform. Extend @video1 by 8 more seconds from its final frame, matching its grade, grain and lens exactly. Continue the motion already there: the train slows to a stop, doors stay closed, nobody steps out. Camera: continue the existing slow pan right, decelerating to a full stop by the fourth second. Lighting: keep the source's overcast top light, no relight. Audio: brakes releasing, a bell on the platform, wind, no music. 8 seconds, 720p, 16:9.
```

---

### SD-06 · Motion from `@video1`, subject from the prompt
`seedance` — motion-transfer, reference

Here `@video1` is a movement reference only. Say so in as many words — take the path and the timing, leave the
subject, the room and the light behind — or it leaks its own scene into the render.

**EN**
```
@video1 is a reference clip of a person walking a slow circle around a table, filmed static. Take the motion path and timing from @video1 only — not its subject, room or light — and apply them to a new subject: a tall brass candlestick carried at chest height through a dark hall. Camera: static on a wide lens, no movement at all. Lighting: one practical candle flame on the subject, warm, moving with it; walls unlit. Audio: footsteps on stone, a long reverb tail, no music. 10 seconds, 1080p, 16:9.
```

**KA**
```
@video1 — სარეფერენსო კლიპი: ადამიანი ნელა უვლის მაგიდას წრეზე, გადაღებულია სტატიკური კამერით. აიღე @video1-იდან მხოლოდ მოძრაობის ტრაექტორია და ტაიმინგი — არა სუბიექტი, ოთახი ან განათება — და გადაიტანე ახალ სუბიექტზე: მაღალი სპილენძის შანდალი, რომელსაც გულმკერდის სიმაღლეზე მიაქვთ ბნელ დარბაზში. კამერა: სტატიკური, ფართო ობიექტივზე, მოძრაობის გარეშე. განათება: ერთადერთი წყარო სანთლის ალია თავად სუბიექტზე, თბილი, მასთან ერთად მოძრავი; კედლები განათების გარეშე რჩება. აუდიო: ნაბიჯები ქვაზე, გრძელი რევერბერაციის კუდი, მუსიკის გარეშე. 10 წამი, 1080p, 16:9.
---
@video1 is a reference clip of a person walking a slow circle around a table, filmed static. Take the motion path and timing from @video1 only — not its subject, room or light — and apply them to a new subject: a tall brass candlestick carried at chest height through a dark hall. Camera: static on a wide lens, no movement at all. Lighting: one practical candle flame on the subject, warm, moving with it; walls unlit. Audio: footsteps on stone, a long reverb tail, no music. 10 seconds, 1080p, 16:9.
```

---

### SD-07 · Cutting the action to `@audio1`
`seedance` — audio-reference, sync

Supply a WAV or MP3 as `@audio1` and let it drive the picture. Name how many events it contains and what has to
land on each one — "sync to the audio" on its own syncs nothing.

**EN**
```
@audio1 is a 9-second WAV of a single hammer striking an anvil, six strikes, uneven spacing. Use @audio1 as the clip's audio track and cut the action to it: a blacksmith's hammer lands exactly on each of the six strikes, sparks leaving the iron on impact and nowhere else. Camera: slow push-in on the anvil, 12 percent across the clip, easing out on the last strike. Lighting: forge coals from frame right, hard and orange; the shop behind falls to black. No music under @audio1. 9 seconds, 1080p, 16:9.
```

**KA**
```
@audio1 — 9-წამიანი WAV: გრდემლზე ჩაქუჩის ექვსი დარტყმა, არათანაბარი ინტერვალით. გამოიყენე @audio1 კლიპის აუდიოდ და მოქმედება ზუსტად მას მოარგე: მჭედლის ჩაქუჩი ექვსივე დარტყმაზე ზუსტად ეცემა გრდემლს, ნაპერწკლები კი მხოლოდ დარტყმის მომენტში ფრინდება და სხვა დროს — არა. კამერა: ნელი მიახლოება გრდემლზე, მთელ კლიპზე 12%, და ბოლო დარტყმაზე რბილად ჩერდება. განათება: სამჭედლოს ნახშირი კადრის მარჯვნიდან, მკვეთრი და ნარინჯისფერი; უკან სახელოსნო შავში გადადის. @audio1-ის ქვეშ მუსიკა არ დაამატო. 9 წამი, 1080p, 16:9.
---
@audio1 is a 9-second WAV of a single hammer striking an anvil, six strikes, uneven spacing. Use @audio1 as the clip's audio track and cut the action to it: a blacksmith's hammer lands exactly on each of the six strikes, sparks leaving the iron on impact and nowhere else. Camera: slow push-in on the anvil, 12 percent across the clip, easing out on the last strike. Lighting: forge coals from frame right, hard and orange; the shop behind falls to black. No music under @audio1. 9 seconds, 1080p, 16:9.
```

---

### SD-08 · Vertical 9:16 ad, Tbilisi at rush hour
`seedance` — vertical, ad, georgia

Built for the feed: the subject sits in the lower third so the caption has room, and the two things the model
reliably gets wrong — signage and number plates — are excluded outright.

**EN**
```
Vertical social ad, 9:16, 1080p, 10 seconds. A yellow delivery courier on an e-bike threads between stopped cars on Chavchavadze Avenue at evening rush hour, the crowd on the pavement blurred behind him. Camera: gimbal tracking alongside him at his own speed, roughly 15 km/h, holding him in the lower third so the top third stays clear for a caption. Lighting: low sun down the length of the street from behind camera, headlights and shop windows filling the shadows. Audio: traffic, horns, bike chain, no music. No legible signage, no readable plates.
```

**KA**
```
ვერტიკალური სარეკლამო კადრი, 9:16, 1080p, 10 წამი. ყვითელ ფორმაში კურიერი ელექტროველოსიპედით მიიკვლევს გზას გაჩერებულ მანქანებს შორის ჭავჭავაძის გამზირზე, საღამოს პიკის საათში; ტროტუარზე ხალხი უკან ბუნდოვნად ჩანს. კამერა: გიმბალით თანხლება მისივე სიჩქარით, დაახლოებით 15 კმ/სთ; კურიერი კადრის ქვედა მესამედში რჩება, ზედა მესამედი კი თავისუფალი — წარწერისთვის. განათება: დაბალი მზე გამზირის სიგრძეზე, კამერის უკნიდან; ჩრდილებს ფარები და ვიტრინები ავსებს. აუდიო: ტრანსპორტი, სიგნალები, ველოსიპედის ჯაჭვი, მუსიკის გარეშე. წასაკითხი წარწერა და ნომრის ნიშანი კადრში არ ჩანს.
---
Vertical social ad, 9:16, 1080p, 10 seconds. A yellow delivery courier on an e-bike threads between stopped cars on Chavchavadze Avenue at evening rush hour, the crowd on the pavement blurred behind him. Camera: gimbal tracking alongside him at his own speed, roughly 15 km/h, holding him in the lower third so the top third stays clear for a caption. Lighting: low sun down the length of the street from behind camera, headlights and shop windows filling the shadows. Audio: traffic, horns, bike chain, no music. No legible signage, no readable plates.
```

---

### SD-09 · 21:9 establishing sequence, Kazbegi at first light
`seedance` — cinematic, aerial, georgia

The full 15 seconds in the widest ratio, three aerial blocks on timecode. One light direction for all three —
a sunrise that moves between blocks reads as three different mornings.

**EN**
```
Cinematic establishing sequence, 15 seconds, 1080p, 21:9, Kazbegi at first light.
[0:00–0:05] AERIAL WIDE — drone rises over a ridge of cloud, Gergeti church small on its hill below. Camera: slow vertical climb, 2 m/s.
[0:05–0:10] AERIAL ORBIT — half-orbit right around the church, 40 degrees, constant.
[0:10–0:15] AERIAL PUSH — the drone moves toward the Kazbegi summit as cloud clears it. Camera: forward at walking pace.
Lighting: low sun from frame right, the east faces lit, valley still in blue shadow. Audio: wind at altitude, distant sheep bells, no music. No people, no drone visible.
```

**KA**
```
კინემატოგრაფიული სექვენცია, 15 წამი, 1080p, 21:9, ყაზბეგი გამთენიისას.
[0:00–0:05] საჰაერო ზოგადი პლანი — დრონი ღრუბლის ქედს ზემოთ ადის, ქვემოთ გერგეტის ტაძარი პატარად ჩანს. კამერა: ნელი ვერტიკალური აწევა, წამში 2 მეტრი.
[0:05–0:10] საჰაერო ორბიტა — ნახევარი რკალი მარჯვნივ ტაძრის გარშემო, 40 გრადუსი, მუდმივი სიჩქარით.
[0:10–0:15] საჰაერო მიახლოება — დრონი ყაზბეგის მწვერვალისკენ მიიწევს, ღრუბელი კი მწვერვალს ხსნის. კამერა: წინ, ნაბიჯის სიჩქარით.
განათება: დაბალი მზე კადრის მარჯვნიდან, აღმოსავლეთის კალთები განათებულია, ხეობა ჯერ კიდევ ლურჯ ჩრდილშია. აუდიო: ქარი სიმაღლეზე, შორეული ცხვრის ზანზალაკები, მუსიკის გარეშე. ადამიანი არ ჩანს, დრონიც არ ჩანს.
---
Cinematic establishing sequence, 15 seconds, 1080p, 21:9, Kazbegi at first light.
[0:00–0:05] AERIAL WIDE — drone rises over a ridge of cloud, Gergeti church small on its hill below. Camera: slow vertical climb, 2 m/s.
[0:05–0:10] AERIAL ORBIT — half-orbit right around the church, 40 degrees, constant.
[0:10–0:15] AERIAL PUSH — the drone moves toward the Kazbegi summit as cloud clears it. Camera: forward at walking pace.
Lighting: low sun from frame right, the east faces lit, valley still in blue shadow. Audio: wind at altitude, distant sheep bells, no music. No people, no drone visible.
```
