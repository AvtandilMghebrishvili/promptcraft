# Runway, Kling, Pika & Luma

Image-to-video. Every entry here starts from a still you already have, so the prompt carries the
**motion and the camera** — never the scene. The Shot spec framework applies minus everything the
source image has already decided: see [`../../references/frameworks.md`](../../references/frameworks.md) §8
and [`../../references/tool-routing.md`](../../references/tool-routing.md) §Video.

Tool shapes: **Runway** — strongest image-to-video; prompt the motion and let the source image hold
the composition. **Kling** — human motion and faces, start-frame / end-frame control.
**Pika** — fast iteration, effects and transformations. **Luma** — camera moves, named in
camera-operator vocabulary.

**On the Georgian block.** None of these four take Georgian input reliably, so the `**KA**` block is a
*working version*: the same motion brief in Georgian, so you can compose, edit and argue about the shot
in your own language — then, after the `---` line, the English string you actually paste.

**Prompt the motion, not the scene.** The source image has already fixed the subject, the framing and
the light. Re-describing them fights the image and invites the model to redraw it.

**One motion per shot.** A second action in the same shot produces morphing — the face drifts, the label
re-letters, the hand grows a finger. Split it into two shots instead.

ქართული ბლოკი სამუშაო ვერსიაა — Runway-ში, Kling-ში, Pika-სა და Luma-ში ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
აღწერე მოძრაობა და არა სცენა — საწყის სურათს კადრი, კომპოზიცია და განათება უკვე გადაწყვეტილი აქვს; მათი ხელახლა აღწერა მოდელს სურათის გადახატვისკენ უბიძგებს.
ერთ კადრში ერთი მოძრაობა. მეორე მოქმედების დამატება მორფინგს იწვევს — სახე „ცურავს“, ეტიკეტზე ასოები იცვლება, ხელს თითი ემატება. ასეთ დროს კადრი ორად გაყავი.

---

### RK-01 · Still product shot, barely brought to life
`runway` — product, subtle

**EN**
```
Source image: a bottle of amber qvevri wine standing on a stone shelf in a marani, label facing camera, a clay qvevri lid out of focus behind it.
Motion: light only — a slow brightening across the label and the glass, as if a door had opened off frame left. Nothing else in the frame changes.
Camera: slow push-in, 8% tighter over the shot, dead level, no tilt.
The bottle, the label and the shelf must not move, warp or change shape; the label text stays legible and unaltered to the last frame. No hands and no people enter the frame.
Duration: 4s
```

**KA**
```
საწყისი სურათი: ქარვისფერი ქვევრის ღვინის ბოთლი მარნის ქვის თაროზე, ეტიკეტი კამერისკენ, უკან ფოკუსს მიღმა ქვევრის თიხის სარქველი.
მოძრაობა: მხოლოდ შუქი — ეტიკეტსა და შუშაზე განათება ნელა ძლიერდება, თითქოს კადრს გარეთ, მარცხნივ, კარი გაიღო. კადრში სხვა არაფერი იცვლება.
კამერა: ნელი მიახლოება — კადრი მთელ ხანგრძლივობაზე 8%-ით ვიწროვდება, მკაცრად ჰორიზონტალურად, დახრის გარეშე.
ბოთლი, ეტიკეტი და თარო არ მოძრაობს და ფორმას არ იცვლის; ეტიკეტის ტექსტი ბოლო კადრამდე უცვლელი და წასაკითხი რჩება. კადრში ხელი ან ადამიანი არ შემოდის.
ხანგრძლივობა: 4 წამი
---
Source image: a bottle of amber qvevri wine standing on a stone shelf in a marani, label facing camera, a clay qvevri lid out of focus behind it.
Motion: light only — a slow brightening across the label and the glass, as if a door had opened off frame left. Nothing else in the frame changes.
Camera: slow push-in, 8% tighter over the shot, dead level, no tilt.
The bottle, the label and the shelf must not move, warp or change shape; the label text stays legible and unaltered to the last frame. No hands and no people enter the frame.
Duration: 4s
```

---

### RK-02 · Portrait that does not drift
`kling` — portrait, face

**EN**
```
Source image: head-and-shoulders portrait of a cloisonné enamel master in his sixties in his Tbilisi workshop, looking straight into the lens, a board of hanging tools behind him.
Motion: one slow blink and the small settle of a single breath in the shoulders. Nothing else. The head holds its position, the mouth stays closed, the gaze stays on the lens.
Camera: locked off — no push, no drift, no handheld shake.
Keep the identity, the beard line, the wrinkles and the skin texture exactly as in the source: do not re-age, smooth, restyle or re-light the face. The tools on the board behind him stay static.
Duration: 3s
```

**KA**
```
საწყისი სურათი: სამოცს გადაცილებული მინანქრის ოსტატის პორტრეტი წელზევით, თბილისურ სახელოსნოში, პირდაპირ ობიექტივში იყურება, უკან დაფაზე ჩამოკიდებული ხელსაწყოები.
მოძრაობა: ერთი ნელი დახამხამება და ერთი ამოსუნთქვის მსუბუქი მოძრაობა მხრებში. სხვა არაფერი. თავი ადგილიდან არ იძვრის, პირი დახურული რჩება, მზერა ობიექტივზეა.
კამერა: სრულიად უძრავი — მიახლოების, გადაცურებისა და ხელის კანკალის გარეშე.
სახე ზუსტად ისეთი უნდა დარჩეს, როგორიც საწყის სურათზეა: წვერის ხაზი, ნაოჭები და კანის ფაქტურა უცვლელი. სახე არ გაახალგაზრდავო, არ დააგლუვო და ხელახლა არ გადაანათო. უკან, დაფაზე, ხელსაწყოები უძრავია.
ხანგრძლივობა: 3 წამი
---
Source image: head-and-shoulders portrait of a cloisonné enamel master in his sixties in his Tbilisi workshop, looking straight into the lens, a board of hanging tools behind him.
Motion: one slow blink and the small settle of a single breath in the shoulders. Nothing else. The head holds its position, the mouth stays closed, the gaze stays on the lens.
Camera: locked off — no push, no drift, no handheld shake.
Keep the identity, the beard line, the wrinkles and the skin texture exactly as in the source: do not re-age, smooth, restyle or re-light the face. The tools on the board behind him stay static.
Duration: 3s
```

---

### RK-03 · Start frame to end frame
`kling` — transition, keyframe

**EN**
```
Source images: start frame — a closed tin of tea dead centre on a bare oak counter, lid on, shot front-on at counter height. End frame — the identical counter, identical camera position and identical light, the tin now open with its lid resting flat beside it and the leaves visible inside.
Motion: one continuous move between the two frames — the lid lifts, travels right and settles. No hand enters the frame, no cut, no second pass.
Camera: identical framing in both keyframes, locked off throughout. Interpolate the object, not the camera.
The counter, the light, the tin's body and its printed label stay identical from first frame to last.
Duration: 5s
```

**KA**
```
საწყისი სურათები: საწყისი კადრი — ჩაის დახურული ქილა მუხის ცარიელი მაგიდის შუაში, სახურავი დახურული, გადაღებული პირდაპირ, მაგიდის სიმაღლიდან. საბოლოო კადრი — იგივე მაგიდა, კამერის იგივე წერტილი და იგივე განათება, ქილა უკვე ღიაა, სახურავი გვერდით ბრტყლად დევს, შიგნით ჩაის ფოთოლი ჩანს.
მოძრაობა: ერთი უწყვეტი გადასვლა ორ კადრს შორის — სახურავი ასწევს, მარჯვნივ გადაინაცვლებს და დაწვება. ხელი კადრში არ შემოდის, მონტაჟური გადაჭრა და გამეორება არ არის.
კამერა: ორივე საკვანძო კადრში ერთი და იგივე კომპოზიცია, კამერა ბოლომდე უძრავია — ანიმაცია საგანს ეხება და არა კამერას.
მაგიდა, განათება, ქილის კორპუსი და მასზე დაბეჭდილი ეტიკეტი პირველიდან ბოლო კადრამდე უცვლელია.
ხანგრძლივობა: 5 წამი
---
Source images: start frame — a closed tin of tea dead centre on a bare oak counter, lid on, shot front-on at counter height. End frame — the identical counter, identical camera position and identical light, the tin now open with its lid resting flat beside it and the leaves visible inside.
Motion: one continuous move between the two frames — the lid lifts, travels right and settles. No hand enters the frame, no cut, no second pass.
Camera: identical framing in both keyframes, locked off throughout. Interpolate the object, not the camera.
The counter, the light, the tin's body and its printed label stay identical from first frame to last.
Duration: 5s
```

---

### RK-04 · Parallax push into a landscape still
`luma` — landscape, parallax

**EN**
```
Source image: Gergeti Trinity church on its ridge, the snow face of Kazbegi behind it, one deep bank of cloud crossing the mountain, long lens, horizon level.
Motion: parallax only — the cloud bank slides right to left across the peak, separating from the foreground ridge and opening the depth between the church and the mountain.
Camera: slow dolly in, 12% over the shot, dead level, no tilt, no roll, no handheld float.
The church must not bend, stretch, gain windows or change the shape of its cross; the ridge line and the horizon stay fixed. No birds, no people, no vehicles.
Duration: 6s
```

**KA**
```
საწყისი სურათი: გერგეტის სამება ქედზე, უკან ყაზბეგის თოვლიანი კალთა, მთას ერთი სქელი ღრუბლის ზოლი კვეთს, გრძელი ობიექტივი, ჰორიზონტი სწორი.
მოძრაობა: მხოლოდ პარალაქსი — ღრუბლის ზოლი მარჯვნიდან მარცხნივ მიცურავს მწვერვალზე, წინა პლანის ქედს შორდება და ეკლესიასა და მთას შორის სიღრმეს ხსნის.
კამერა: ნელი მიახლოება — კადრი მთელ ხანგრძლივობაზე 12%-ით ვიწროვდება, მკაცრად ჰორიზონტალურად, დახრისა და გადაბრუნების გარეშე, ხელის კანკალის იმიტაციის გარეშე.
ეკლესია არ უნდა მოიხაროს, გაიწელოს, ფანჯრები შეიძინოს ან ჯვრის ფორმა შეიცვალოს; ქედის ხაზი და ჰორიზონტი უძრავია. კადრში ფრინველი, ადამიანი და ტრანსპორტი არ ჩნდება.
ხანგრძლივობა: 6 წამი
---
Source image: Gergeti Trinity church on its ridge, the snow face of Kazbegi behind it, one deep bank of cloud crossing the mountain, long lens, horizon level.
Motion: parallax only — the cloud bank slides right to left across the peak, separating from the foreground ridge and opening the depth between the church and the mountain.
Camera: slow dolly in, 12% over the shot, dead level, no tilt, no roll, no handheld float.
The church must not bend, stretch, gain windows or change the shape of its cross; the ridge line and the horizon stay fixed. No birds, no people, no vehicles.
Duration: 6s
```

---

### RK-05 · One gust in a curtain
`runway` — cloth, physics

**EN**
```
Source image: a half-open kitchen window with a thin linen curtain hanging beside it, morning light on the sill, the edge of a table below.
Motion: the curtain only — it lifts once on a single gust, billows into the room and settles back against the frame. One gust, not a repeating rhythm.
Camera: locked off, no movement.
The window frame, the sill and the table edge must not move, and the light must not change level or colour temperature. The curtain keeps its weave and its hem — it must not turn to smoke or melt into the wall.
Duration: 4s
```

**KA**
```
საწყისი სურათი: ნახევრად ღია სამზარეულოს ფანჯარა, გვერდით თხელი სელის ფარდა, დილის შუქი რაფაზე, ქვემოთ მაგიდის კიდე.
მოძრაობა: მხოლოდ ფარდა — ერთ დაბერვაზე ასწევს, ოთახში შემოიბერება და ისევ ჩამოწვება ჩარჩოზე. ერთი დაბერვა და არა განმეორებადი რიტმი.
კამერა: სრულიად უძრავი.
ფანჯრის ჩარჩო, რაფა და მაგიდის კიდე არ მოძრაობს; შუქის სიძლიერე და ტემპერატურა უცვლელია. ფარდას ქსოვილის ფაქტურა და ნაკერი უნარჩუნდება — კვამლად არ უნდა გადაიქცეს და კედელში არ უნდა ჩაიწრიტოს.
ხანგრძლივობა: 4 წამი
---
Source image: a half-open kitchen window with a thin linen curtain hanging beside it, morning light on the sill, the edge of a table below.
Motion: the curtain only — it lifts once on a single gust, billows into the room and settles back against the frame. One gust, not a repeating rhythm.
Camera: locked off, no movement.
The window frame, the sill and the table edge must not move, and the light must not change level or colour temperature. The curtain keeps its weave and its hem — it must not turn to smoke or melt into the wall.
Duration: 4s
```

---

### RK-06 · Logo reveal that leaves the letterforms alone
`pika` — logo, brand

**EN**
```
Source image: a flat logo lockup — mark above a wordmark — centred on an even deep-blue field with wide margins, no texture, no gradient.
Motion: one reveal — the lockup resolves from a soft defocus into full sharpness over the first second, then holds absolutely still for the rest of the shot.
Camera: static. No zoom, no drift, no rotation.
The letterforms must not deform, reflow, wobble, or gain or lose strokes; the mark keeps its exact geometry and spacing; the background stays one flat colour. No particles, no light sweep, no glow, no second animation of any kind.
Duration: 3s
```

**KA**
```
საწყისი სურათი: ბრტყელი ლოგოს ბლოკი — ნიშანი და ქვემოთ ტექსტური ლოგო — ცენტრში, ერთიან მუქ ლურჯ ფონზე, ფართო მინდვრებით, ფაქტურისა და გრადიენტის გარეშე.
მოძრაობა: ერთი გამოჩენა — ლოგო პირველ წამში რბილი დაბინდვიდან სრულ სიმკვეთრეში გადადის, შემდეგ კადრის ბოლომდე სრულიად უძრავად რჩება.
კამერა: სტატიკური. ზუმის, გადაცურებისა და ბრუნვის გარეშე.
ასოების ფორმა არ უნდა დამახინჯდეს, არ უნდა გადაეწყოს, შტრიხები არ უნდა დაემატოს ან დააკლდეს; ნიშნის გეომეტრია და შორისები უცვლელია; ფონი ერთიან, ბრტყელ ფერად რჩება. ნაწილაკები, შუქის გავლა, ნათება ან სხვა ეფექტი არ ემატება.
ხანგრძლივობა: 3 წამი
---
Source image: a flat logo lockup — mark above a wordmark — centred on an even deep-blue field with wide margins, no texture, no gradient.
Motion: one reveal — the lockup resolves from a soft defocus into full sharpness over the first second, then holds absolutely still for the rest of the shot.
Camera: static. No zoom, no drift, no rotation.
The letterforms must not deform, reflow, wobble, or gain or lose strokes; the mark keeps its exact geometry and spacing; the background stays one flat colour. No particles, no light sweep, no glow, no second animation of any kind.
Duration: 3s
```

---

### RK-07 · Orbit around a static subject
`luma` — camera move, product

**EN**
```
Source image: a matte black ceramic vase, three-quarter view, on a seamless mid-grey sweep with no horizon line, one large softbox from camera right.
Motion: none in the subject. The only movement is the camera.
Camera: slow orbit to the right, 25 degrees over the shot, constant height, constant distance, the vase held centred from first frame to last. Ease in and ease out, no whip, no acceleration through the middle.
The key light stays fixed to the room, not to the camera, so the highlight travels across the glaze as the camera moves. The vase must not rotate on its own axis, wobble or change silhouette, and no horizon line may appear in the sweep.
Duration: 5s
```

**KA**
```
საწყისი სურათი: მქრქალი შავი კერამიკული ვაზა, სამმეოთხედი რაკურსი, ერთიან საშუალო ნაცრისფერ ფონზე, ჰორიზონტის ხაზის გარეშე, ერთი დიდი სოფტბოქსი კამერიდან მარჯვნივ.
მოძრაობა: საგანი უძრავია. მოძრაობს მხოლოდ კამერა.
კამერა: ნელი ორბიტა მარჯვნივ, 25 გრადუსი მთელ კადრზე, მუდმივი სიმაღლე და მუდმივი მანძილი, ვაზა პირველიდან ბოლო კადრამდე ცენტრში რჩება. დაწყება და დასრულება რბილი, შუაში აჩქარებისა და მკვეთრი მოსმის გარეშე.
მთავარი შუქი ოთახზეა მიბმული და არა კამერაზე — ბზინვარება ჭიქურზე კამერის მოძრაობისას გადაინაცვლებს. ვაზა საკუთარ ღერძზე არ ბრუნავს, არ ირყევა და სილუეტს არ იცვლის; ფონზე ჰორიზონტის ხაზი არ უნდა გამოჩნდეს.
ხანგრძლივობა: 5 წამი
---
Source image: a matte black ceramic vase, three-quarter view, on a seamless mid-grey sweep with no horizon line, one large softbox from camera right.
Motion: none in the subject. The only movement is the camera.
Camera: slow orbit to the right, 25 degrees over the shot, constant height, constant distance, the vase held centred from first frame to last. Ease in and ease out, no whip, no acceleration through the middle.
The key light stays fixed to the room, not to the camera, so the highlight travels across the glaze as the camera moves. The vase must not rotate on its own axis, wobble or change silhouette, and no horizon line may appear in the sweep.
Duration: 5s
```

---

### RK-08 · Seamless loop for a website hero
`runway` — loop, web

**EN**
```
Source image: an overhead still of a walnut desk shot straight down — an open laptop, a full cup of coffee, a closed notebook, an even pool of daylight.
Motion: one element only — steam rising from the cup in a slow, continuous, unhurried ribbon. The laptop screen, the notebook and the desk stay completely still.
Camera: locked off, absolutely static, so the last frame matches the first exactly.
Build it as a seamless loop: the steam must sit at the same density and the same position in the final frame as in the opening frame, with no fade at either end and no visible seam on the repeat.
Duration: 6s, loopable
```

**KA**
```
საწყისი სურათი: კაკლის ხის მაგიდა, გადაღებული მკაცრად ზემოდან — ღია ლეპტოპი, სავსე ყავის ჭიქა, დახურული რვეული, თანაბარი დღის შუქი.
მოძრაობა: მხოლოდ ერთი ელემენტი — ჭიქიდან ნელი, უწყვეტი ორთქლის ზოლი ადის. ლეპტოპის ეკრანი, რვეული და მაგიდა სრულიად უძრავია.
კამერა: სრულიად სტატიკური, რომ ბოლო კადრი პირველს ზუსტად დაემთხვეს.
გააკეთე უწყვეტი ლუპი: ორთქლი ბოლო კადრში იმავე სიმკვრივითა და იმავე ადგილას უნდა იყოს, რაც პირველში; არც დასაწყისში და არც ბოლოში ჩაქრობა არ გინდა და ლუპის ნაკერი არ უნდა ჩანდეს.
ხანგრძლივობა: 6 წამი, ლუპისთვის
---
Source image: an overhead still of a walnut desk shot straight down — an open laptop, a full cup of coffee, a closed notebook, an even pool of daylight.
Motion: one element only — steam rising from the cup in a slow, continuous, unhurried ribbon. The laptop screen, the notebook and the desk stay completely still.
Camera: locked off, absolutely static, so the last frame matches the first exactly.
Build it as a seamless loop: the steam must sit at the same density and the same position in the final frame as in the opening frame, with no fade at either end and no visible seam on the repeat.
Duration: 6s, loopable
```

---

### RK-09 · Single-pass colour transformation
`pika` — effects, transformation

**EN**
```
Source image: a plain white canvas sneaker, side-on, on a light grey sweep, laces tied, even studio light.
Motion: one transformation — the canvas changes from white to deep indigo, the change travelling once from the heel to the toe and stopping there. No second pass, no pulse, no return.
Camera: static, no push, no drift.
The silhouette, the stitching, the eyelets, the laces and the rubber sole must stay exactly as in the source — only the colour of the canvas changes. The shoe must not deform, inflate or grow extra eyelets, and the background stays flat light grey throughout.
Duration: 4s
```

**KA**
```
საწყისი სურათი: სადა თეთრი ტილოს კედი, გვერდითი ხედი, ღია ნაცრისფერ ერთიან ფონზე, თასმები შეკრული, თანაბარი სტუდიური განათება.
მოძრაობა: ერთი გარდაქმნა — ტილო თეთრიდან მუქ ინდიგოში გადადის, ფერის ტალღა ერთხელ გაივლის ქუსლიდან წვერამდე და იქვე ჩერდება. მეორე გავლა, პულსაცია და უკან დაბრუნება არ არის.
კამერა: სტატიკური, მიახლოებისა და გადაცურების გარეშე.
სილუეტი, ნაკერები, თასმის ხვრელები, თასმები და რეზინის ძირი ზუსტად ისეთი რჩება, როგორიც საწყის სურათზეა — იცვლება მხოლოდ ტილოს ფერი. ფეხსაცმელი არ უნდა დამახინჯდეს, არ უნდა გაიბეროს და ხვრელები არ უნდა დაემატოს; ფონი ბოლომდე ბრტყელი, ღია ნაცრისფერი რჩება.
ხანგრძლივობა: 4 წამი
---
Source image: a plain white canvas sneaker, side-on, on a light grey sweep, laces tied, even studio light.
Motion: one transformation — the canvas changes from white to deep indigo, the change travelling once from the heel to the toe and stopping there. No second pass, no pulse, no return.
Camera: static, no push, no drift.
The silhouette, the stitching, the eyelets, the laces and the rubber sole must stay exactly as in the source — only the colour of the canvas changes. The shoe must not deform, inflate or grow extra eyelets, and the background stays flat light grey throughout.
Duration: 4s
```
