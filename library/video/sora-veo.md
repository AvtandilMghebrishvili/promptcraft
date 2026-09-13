# Sora & Veo

Shot spec, one shot at a time: `[shot size]. [subject + one action]. Camera: [movement + speed].
Lighting: [source, quality, direction]. Mood: [x]. Audio: [x]. Duration: [n]s.`
Structure and per-tool notes: [`../../references/frameworks.md`](../../references/frameworks.md) §8,
[`../../references/tool-routing.md`](../../references/tool-routing.md) §Video.

**On the Georgian block.** Both tools take English far more reliably than Georgian, so the `**KA**`
block here is a *working version*: the same shot spec in Georgian, so you can build the shot, cut it
and argue about it in your own language — then paste the English string after the `---` line.
One prompt is one shot and one action inside it — no cuts, no second thing happening.
Always write the audio line, `no music` included — leave it off and you get a generic stock score under everything.

ქართული ბლოკი სამუშაო ვერსიაა — Sora-სა და Veo-ში ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
ერთი პრომპტი — ერთი კადრი და მასში ერთი მოქმედება; მონტაჟური გადასვლის გარეშე.
აუდიო ყოველთვის დაწერე, მათ შორის „მუსიკის გარეშე“ — თუ არ დაწერე, ქვეშ საერთო, სტოკური მუსიკა დაგიდგება.

---

### SV-01 · Product hero on a sweep
`sora` — product, studio

**EN**
```
Medium shot. A matte white ceramic kettle stands on a seamless mid-grey sweep and a thin ribbon of steam lifts from the spout. Camera: slow orbit right, 30 degrees across the whole shot, constant speed, no acceleration. Lighting: one large softbox from camera right just above the kettle, thin white rim light down the left edge, no fill from below. Mood: calm, precise. Audio: faint room tone and the low hiss of steam, no music. Duration: 6s.
```

**KA**
```
საშუალო პლანი. მქრქალი თეთრი კერამიკული ჩაიდანი დგას ერთიან საშუალო ნაცრისფერ ფონზე და ყუნწიდან თხელი ორთქლის ზოლი ადის. კამერა: ნელი ორბიტა მარჯვნივ, 30 გრადუსი მთელ კადრზე, მუდმივი სიჩქარით, აჩქარების გარეშე. განათება: ერთი დიდი სოფტბოქსი კამერიდან მარჯვნივ, ჩაიდნის ოდნავ ზემოთ; თხელი თეთრი კონტურული შუქი მარცხენა კიდეზე; ქვემოდან შემავსებელი შუქი არ არის. განწყობა: მშვიდი, ზუსტი. აუდიო: ოთახის სუსტი ტონი და ორთქლის დაბალი შიშინი, მუსიკის გარეშე. ხანგრძლივობა: 6 წამი.
---
Medium shot. A matte white ceramic kettle stands on a seamless mid-grey sweep and a thin ribbon of steam lifts from the spout. Camera: slow orbit right, 30 degrees across the whole shot, constant speed, no acceleration. Lighting: one large softbox from camera right just above the kettle, thin white rim light down the left edge, no fill from below. Mood: calm, precise. Audio: faint room tone and the low hiss of steam, no music. Duration: 6s.
```

---

### SV-02 · Khinkali, steam as the plate lands
`sora` `veo` — food, georgia
Sora holds the steam physics; Veo if you want the kitchen behind the shot to sound real.

**EN**
```
Close-up. Two hands set a plate of khinkali down on a bare wooden table and steam lifts off the pleated tops as it lands; the hands stay fully inside the frame the whole time and are never cropped. Camera: slow push-in, about 8 percent over the shot. Lighting: single window from frame left, soft late-morning daylight, the right half of the table falling into shadow. Mood: appetite, unhurried. Audio: the plate meeting wood, faint kitchen clatter two rooms away, no music. Duration: 5s.
```

**KA**
```
ახლო პლანი. ორი ხელი ხის შიშველ მაგიდაზე დებს ხინკლის თეფშს და დაკეცილ კუდებზე ორთქლი ადის; ხელები ბოლომდე კადრშია და არსად არ იჭრება. კამერა: ნელი მიახლოება (push-in), მთელ კადრზე დაახლოებით 8%. განათება: ერთი ფანჯარა კადრის მარცხნიდან, გვიანი დილის რბილი შუქი; მაგიდის მარჯვენა ნახევარი ჩრდილში რჩება. განწყობა: მადისაღმძვრელი, აუჩქარებელი. აუდიო: თეფშის შეხება ხეზე, ორი ოთახის იქით სამზარეულოს სუსტი ხმაური, მუსიკის გარეშე. ხანგრძლივობა: 5 წამი.
---
Close-up. Two hands set a plate of khinkali down on a bare wooden table and steam lifts off the pleated tops as it lands; the hands stay fully inside the frame the whole time and are never cropped. Camera: slow push-in, about 8 percent over the shot. Lighting: single window from frame left, soft late-morning daylight, the right half of the table falling into shadow. Mood: appetite, unhurried. Audio: the plate meeting wood, faint kitchen clatter two rooms away, no music. Duration: 5s.
```

---

### SV-03 · Fog through the Svan towers
`sora` — landscape, establishing, georgia
Sora: the longest coherent take, which is what a ten-second atmospheric hold needs.

**EN**
```
Wide establishing shot. Low fog drifts left to right through a cluster of stone Svan defensive towers, covering and then uncovering the tallest one. Camera: very slow push-in, almost imperceptible, under 10 percent across the whole shot, no pan and no tilt. Lighting: flat overcast dawn, cold and shadowless, the snow ridge behind sitting one stop brighter than the towers. Mood: still, remote. Audio: wind moving across stone, one dog barking far off, a cowbell somewhere below, no music. Duration: 10s.
```

**KA**
```
ზოგადი პლანი. დაბალი ნისლი მარცხნიდან მარჯვნივ მიიწევს სვანური ქვის კოშკების ჯგუფში, ჯერ ფარავს ყველაზე მაღალ კოშკს, მერე ისევ ხსნის. კამერა: ძალიან ნელი მიახლოება, თითქმის შეუმჩნეველი, მთელ კადრზე 10%-ზე ნაკლები; პანორამისა და ტილტის გარეშე. განათება: ღრუბლიანი გამთენიის თანაბარი შუქი, ცივი, ჩრდილების გარეშე; უკან თოვლიანი ქედი ერთი საფეხურით უფრო ნათელია. განწყობა: უძრავი, შორეული. აუდიო: ქარი ქვაზე, შორს ერთი ძაღლის ყეფა, ქვემოთ სადღაც ზანზალაკი, მუსიკის გარეშე. ხანგრძლივობა: 10 წამი.
---
Wide establishing shot. Low fog drifts left to right through a cluster of stone Svan defensive towers, covering and then uncovering the tallest one. Camera: very slow push-in, almost imperceptible, under 10 percent across the whole shot, no pan and no tilt. Lighting: flat overcast dawn, cold and shadowless, the snow ridge behind sitting one stop brighter than the towers. Mood: still, remote. Audio: wind moving across stone, one dog barking far off, a cowbell somewhere below, no music. Duration: 10s.
```

---

### SV-04 · Talking-head plate with nobody talking
`veo` — portrait, no-dialogue
Veo for the room tone. The shot is built so no mouth moves — lip-sync is the failure you avoid by not asking for it.

**EN**
```
Medium close-up. A woman in her forties sits at a desk and listens, holding her look just off-lens to camera left; her mouth stays closed and she does not speak at any point. Camera: static on a long lens, locked off, no push and no drift. Lighting: large window from camera left, soft, one bounce card filling the shadow side at a third of the key, background two stops down. Mood: attentive, composed. Audio: small-office room tone, a laptop fan, one page turning off-screen, no music, no dialogue. Duration: 6s.
```

**KA**
```
საშუალო ახლო პლანი. ორმოცს გადაცილებული ქალი მაგიდასთან ზის და უსმენს; მზერა ობიექტივიდან ოდნავ მარცხნივ უჭირავს, პირი დახურული აქვს და არსად არ ლაპარაკობს. კამერა: სტატიკური, გრძელ ობიექტივზე, ფიქსირებული; არც მიახლოება, არც წანაცვლება. განათება: დიდი ფანჯარა კამერიდან მარცხნივ, რბილი; ერთი ამრეკლი ჩრდილიან მხარეს ავსებს ძირითადი შუქის მესამედით; ფონი ორი საფეხურით ბნელია. განწყობა: ყურადღებიანი, აწონილი. აუდიო: პატარა ოფისის ტონი, ლეპტოპის ქულერი, კადრს გარეთ გადაფურცლული ერთი ფურცელი; მუსიკის გარეშე, დიალოგის გარეშე. ხანგრძლივობა: 6 წამი.
---
Medium close-up. A woman in her forties sits at a desk and listens, holding her look just off-lens to camera left; her mouth stays closed and she does not speak at any point. Camera: static on a long lens, locked off, no push and no drift. Lighting: large window from camera left, soft, one bounce card filling the shadow side at a third of the key, background two stops down. Mood: attentive, composed. Audio: small-office room tone, a laptop fan, one page turning off-screen, no music, no dialogue. Duration: 6s.
```

---

### SV-05 · Hands at the tone oven
`sora` — hands, craft, georgia
Hands are a known weak point, so they are held fully in frame at a size the model can resolve.

**EN**
```
Close-up on the hands. A baker's hands, fully in frame and never cropped, hook a shoti loaf off the clay wall of a tone oven with an iron rod and lift it up out of the pit. Camera: slow tilt up following the loaf at exactly its own speed, settling when the loaf clears the rim. Lighting: the oven's own coals from directly below, hard and orange, the only other source a dim bulb behind the baker's shoulder. Mood: heat, practised ease. Audio: coals ticking, the iron scraping clay, the crust crackling as it hits cooler air, no music. Duration: 7s.
```

**KA**
```
ახლო პლანი ხელებზე. მცხობელის ხელები — ბოლომდე კადრში, არსად მოჭრილი — რკინის კაუჭით აძრობს შოთს თონის თიხის კედელს და ორმოდან ზემოთ ამოაქვს. კამერა: ნელი ტილტი ზემოთ, ზუსტად პურის სიჩქარით, და ჩერდება, როცა პური თონის კიდეს გასცდება. განათება: თონის ნახშირი პირდაპირ ქვემოდან, მკვეთრი და ნარინჯისფერი; ერთადერთი სხვა წყარო სუსტი ნათურაა მცხობელის მხრის უკან. განწყობა: სიცხე, ნავარჯიშები სიმსუბუქე. აუდიო: ნახშირის ტკაცუნი, რკინის ხახუნი თიხაზე, ქერქის ხრაშუნი გრილ ჰაერზე, მუსიკის გარეშე. ხანგრძლივობა: 7 წამი.
---
Close-up on the hands. A baker's hands, fully in frame and never cropped, hook a shoti loaf off the clay wall of a tone oven with an iron rod and lift it up out of the pit. Camera: slow tilt up following the loaf at exactly its own speed, settling when the loaf clears the rim. Lighting: the oven's own coals from directly below, hard and orange, the only other source a dim bulb behind the baker's shoulder. Mood: heat, practised ease. Audio: coals ticking, the iron scraping clay, the crust crackling as it hits cooler air, no music. Duration: 7s.
```

---

### SV-06 · Walking the length of a glasshouse
`sora` — camera-move, interior
Sora holds a long forward track without the geometry sliding; the only moving subject is the fan.

**EN**
```
Wide shot. The camera travels down the centre aisle of a long glasshouse between benches of seedlings while a single overhead fan turns at the far end. Camera: steadicam tracking forward at a slow walk, roughly one metre per second, constant, no stops and no turns. Lighting: diffuse midday sun through dirty glass overhead, soft and falling straight down, the aisle brighter than the benches either side. Mood: green, humid, empty. Audio: the fan motor, water dripping onto gravel, muffled rain on the glass, no music, no voices. Duration: 8s.
```

**KA**
```
ფართო პლანი. კამერა მიიწევს გრძელი სათბურის ცენტრალურ დერეფანში, ორივე მხარეს ნერგების თაროებია, შორეულ ბოლოში კი ერთადერთი ჭერის ვენტილატორი ტრიალებს. კამერა: სტედიკამით ტრეკინგი წინ, ნელი ნაბიჯის სიჩქარით, დაახლოებით წამში ერთი მეტრი, მუდმივად, გაჩერებისა და მოხვევის გარეშე. განათება: შუადღის გაბნეული მზე ჭუჭყიან შუშაში, ზემოდან ვერტიკალურად; დერეფანი გვერდითა თაროებზე ნათელია. განწყობა: მწვანე, ნოტიო, ცარიელი. აუდიო: ვენტილატორის ძრავა, წვეთები ხრეშზე, შუშაზე მიყრუებული წვიმა; მუსიკის გარეშე, ადამიანის ხმის გარეშე. ხანგრძლივობა: 8 წამი.
---
Wide shot. The camera travels down the centre aisle of a long glasshouse between benches of seedlings while a single overhead fan turns at the far end. Camera: steadicam tracking forward at a slow walk, roughly one metre per second, constant, no stops and no turns. Lighting: diffuse midday sun through dirty glass overhead, soft and falling straight down, the aisle brighter than the benches either side. Mood: green, humid, empty. Audio: the fan motor, water dripping onto gravel, muffled rain on the glass, no music, no voices. Duration: 8s.
```

---

### SV-07 · Wind ahead of the storm
`sora` `veo` — weather, atmosphere
Sora for the wave of wind through the crop; Veo when you want the thunder and first rain delivered with the picture.

**EN**
```
Wide shot. Wind flattens a wheat field in one travelling wave that runs from the far edge toward camera. Camera: static, locked off on a tripod at chest height, no pan and no push at any point. Lighting: hard low sun from camera right under a blue-black cloud base, the field lit and the sky unlit. Mood: charged, about to break. Audio: wind rising through the heads of the wheat, the first heavy drops on dry ground, thunder a long way off, no music. Duration: 8s.
```

**KA**
```
ფართო პლანი. ქარი ხორბლის ყანას ერთი გადამავალი ტალღით ხრის — შორეული კიდიდან კამერისკენ. კამერა: სტატიკური, შტატივზე ფიქსირებული, გულმკერდის სიმაღლეზე; არც პანორამა, არც მიახლოება. განათება: დაბალი მკვეთრი მზე კამერიდან მარჯვნივ, ლურჯ-შავი ღრუბლის ქვეშ; ყანა განათებულია, ცა — არა. განწყობა: დაძაბული, წამოსვლის წინ. აუდიო: ქარი თავთავებში თანდათან ძლიერდება, პირველი მძიმე წვეთები მშრალ მიწაზე, შორეული ჭექა; მუსიკის გარეშე. ხანგრძლივობა: 8 წამი.
---
Wide shot. Wind flattens a wheat field in one travelling wave that runs from the far edge toward camera. Camera: static, locked off on a tripod at chest height, no pan and no push at any point. Lighting: hard low sun from camera right under a blue-black cloud base, the field lit and the sky unlit. Mood: charged, about to break. Audio: wind rising through the heads of the wheat, the first heavy drops on dry ground, thunder a long way off, no music. Duration: 8s.
```

---

### SV-08 · Eight mugs, two wobbles, no fall
`sora` — physics, comedy
Sora only. This is the multi-beat physics it is best at: one event, three phases, no cut.

**EN**
```
Medium shot. A stack of eight enamel mugs on a tin tray teeters after the tray is set down, rocks twice, and settles upright without falling. Camera: slow push-in, 15 percent over the shot, easing to a stop as the stack settles. Lighting: one hard bare bulb directly above the tray, fast falloff, background going black. Mood: comic tension. Audio: enamel knocking against enamel, the tray ringing on wood, then silence, no music. Duration: 5s.
```

**KA**
```
საშუალო პლანი. თუნუქის ლანგარზე დაწყობილი რვა მინანქრის ჭიქა ლანგრის დადებისთანავე ირხევა, ორჯერ გადაიხრება და სწორად ჩერდება — არ ეცემა. კამერა: ნელი მიახლოება, მთელ კადრზე 15%, და რბილად ჩერდება მაშინ, როცა ჭიქები დამშვიდდება. განათება: ერთი მკვეთრი შიშველი ნათურა პირდაპირ ლანგრის თავზე, სწრაფი ჩავარდნით; ფონი შავში გადადის. განწყობა: კომიკური დაძაბულობა. აუდიო: მინანქარი მინანქარს ეხება, ლანგარი ხეზე წკრიალებს, შემდეგ სიჩუმე; მუსიკის გარეშე. ხანგრძლივობა: 5 წამი.
---
Medium shot. A stack of eight enamel mugs on a tin tray teeters after the tray is set down, rocks twice, and settles upright without falling. Camera: slow push-in, 15 percent over the shot, easing to a stop as the stack settles. Lighting: one hard bare bulb directly above the tray, fast falloff, background going black. Mood: comic tension. Audio: enamel knocking against enamel, the tray ringing on wood, then silence, no music. Duration: 5s.
```

---

### SV-09 · Wine from the jug — the soundscape is the shot
`veo` — audio, georgia
Veo, and only Veo: the picture is simple on purpose so the whole prompt budget goes to the sound.

**EN**
```
Medium close-up. A man tilts a clay jug and pours amber wine into a glass until it is half full. Camera: very slow push-in, 10 percent over the shot. Lighting: one hard-edged shaft of daylight from a high opening at frame left, landing on the wine only, the vaulted stone marani behind it unlit. Mood: cool, unhurried. Audio, built in layers and the point of this shot: wine striking glass and the pitch rising as the glass fills; the clay base of the jug grating on the stone lip of a qvevri as it is set down; a stone-cellar reverb tail of roughly 1.2 seconds on everything; slow drips somewhere behind camera; no music, no voices. Duration: 7s.
```

**KA**
```
საშუალო ახლო პლანი. მამაკაცი თიხის ქოთანს ხრის და ჭიქაში ქარვისფერ ღვინოს ნახევრამდე ასხამს. კამერა: ძალიან ნელი მიახლოება, მთელ კადრზე 10%. განათება: ერთი მკვეთრკიდეებიანი დღის სხივი მაღალი ღიობიდან კადრის მარცხნივ, მხოლოდ ღვინოზე ეცემა; თაღოვანი ქვის მარანი უკან განათების გარეშე რჩება. განწყობა: გრილი, აუჩქარებელი. აუდიო — ეს კადრის მთავარი ნაწილია, ააწყვე ფენებად: ღვინის ჩხრიალი ჭიქაში, ტონი ავსებასთან ერთად მაღლდება; ქოთნის თიხის ძირი ქვევრის ქვის კიდეზე ხახუნით დგება; ყველაფერზე ქვის მარნის რევერბერაცია, დაახლოებით 1,2 წამის კუდით; კადრს მიღმა ნელი წვეთები; მუსიკის გარეშე, ადამიანის ხმის გარეშე. ხანგრძლივობა: 7 წამი.
---
Medium close-up. A man tilts a clay jug and pours amber wine into a glass until it is half full. Camera: very slow push-in, 10 percent over the shot. Lighting: one hard-edged shaft of daylight from a high opening at frame left, landing on the wine only, the vaulted stone marani behind it unlit. Mood: cool, unhurried. Audio, built in layers and the point of this shot: wine striking glass and the pitch rising as the glass fills; the clay base of the jug grating on the stone lip of a qvevri as it is set down; a stone-cellar reverb tail of roughly 1.2 seconds on everything; slow drips somewhere behind camera; no music, no voices. Duration: 7s.
```

---

### SV-10 · Loopable winter sea, Batumi
`sora` `veo` — loop, background, georgia
Either tool. Static frame and constant audio level are what make the loop point invisible on a website header.

**EN**
```
Wide shot. Winter swell rolls in against the Batumi breakwater, one wave every few seconds, no boats and no people anywhere in frame. Camera: static, locked off, no movement of any kind so the clip loops cleanly. Lighting: flat grey overcast, shadowless, even top light, the sea a stop darker than the sky. Mood: cold, empty. Audio: sea and wind only, no gulls, no music, and hold the level constant end to end so the loop point is inaudible. Nothing enters or leaves the frame; the first and last frames must match. Duration: 10s.
```

**KA**
```
ფართო პლანი. ზამთრის ტალღა ბათუმის ბურუნზე მოდის — რამდენიმე წამში ერთი ტალღა; კადრში არც გემია, არც ადამიანი. კამერა: სტატიკური, ფიქსირებული; მოძრაობა საერთოდ არ არის, რომ კადრი ციკლში სუფთად ჩაიკეტოს. განათება: თანაბარი ნაცრისფერი ღრუბლიანობა, ჩრდილების გარეშე, ზემოდან; ზღვა ცაზე ერთი საფეხურით მუქია. განწყობა: ცივი, ცარიელი. აუდიო: მხოლოდ ზღვა და ქარი — თოლიის ხმის გარეშე, მუსიკის გარეშე; დონე ბოლომდე ერთნაირი, რომ ციკლის შეერთება არ ისმოდეს. კადრში არაფერი შემოდის და არაფერი გადის; პირველი და ბოლო კადრი უნდა ემთხვეოდეს. ხანგრძლივობა: 10 წამი.
---
Wide shot. Winter swell rolls in against the Batumi breakwater, one wave every few seconds, no boats and no people anywhere in frame. Camera: static, locked off, no movement of any kind so the clip loops cleanly. Lighting: flat grey overcast, shadowless, even top light, the sea a stop darker than the sky. Mood: cold, empty. Audio: sea and wind only, no gulls, no music, and hold the level constant end to end so the loop point is inaudible. Nothing enters or leaves the frame; the first and last frames must match. Duration: 10s.
```

---

### SV-11 · Image-to-video continuation from a still
`sora` — image-to-video, motion-only
Prompt the motion, not the picture — the source frame already carries composition and light. Sora holds the continuation longest before the frame starts to drift.

**EN**
```
Continue the attached still and keep its framing exactly. Close-up: a cast-iron pan on a stove with a steak resting in it. The only change in the whole clip is steam lifting off the pan and drifting toward frame right. Camera: hold the source composition, then a 5 percent push-in across the last two seconds, nothing else. Lighting: do not relight — keep the source image's single hard lamp from camera left and its unlit background exactly as they are. Mood: quiet, finished. Audio: a low sizzle falling in intensity, an extractor fan, no music. Nothing enters the frame, no hands appear, no cut. Duration: 4s.
```

**KA**
```
გააგრძელე მიბმული სურათი და შეინარჩუნე მისი კადრირება ზუსტად. ახლო პლანი: თუჯის ტაფა ქურაზე, შიგნით ხორცის ნაჭერი ისვენებს. მთელ კლიპში ერთადერთი ცვლილება ისაა, რომ ტაფიდან ორთქლი ადის და კადრის მარჯვენა მხარეს მიიწევს. კამერა: ჯერ ინარჩუნებს საწყისი სურათის კომპოზიციას, ბოლო ორ წამში კი — 5%-იანი მიახლოება; სხვა არაფერი. განათება: ნუ გადაანათებ — დატოვე საწყისი სურათის ერთი მკვეთრი ნათურა კამერიდან მარცხნივ და განათების გარეშე დარჩენილი ფონი, უცვლელად. განწყობა: წყნარი, დასრულებული. აუდიო: დაბალი შიშინი, რომელიც თანდათან სუსტდება, გამწოვის ხმა, მუსიკის გარეშე. კადრში არაფერი შემოდის, ხელები არ ჩნდება, მონტაჟური გადასვლა არ არის. ხანგრძლივობა: 4 წამი.
---
Continue the attached still and keep its framing exactly. Close-up: a cast-iron pan on a stove with a steak resting in it. The only change in the whole clip is steam lifting off the pan and drifting toward frame right. Camera: hold the source composition, then a 5 percent push-in across the last two seconds, nothing else. Lighting: do not relight — keep the source image's single hard lamp from camera left and its unlit background exactly as they are. Mood: quiet, finished. Audio: a low sizzle falling in intensity, an extractor fan, no music. Nothing enters the frame, no hands appear, no cut. Duration: 4s.
```

---

### SV-12 · Funicular at dusk, built around the weak points
`sora` `veo` — cityscape, georgia, failure-proofing
Either tool. The shot is designed against what both still get wrong: no crowd, no legible signage, no hands.

**EN**
```
Wide shot. One empty funicular carriage climbs the track through bare trees above Tbilisi at dusk. Camera: slow pan right following the carriage at exactly its own speed, never running ahead of it. Lighting: last blue daylight from behind the ridge plus the carriage's own warm interior lamps, the only warm source in frame. Mood: end of day, quiet. Audio: cable hum, wheels on rail, wind in bare branches, one car horn from the city below, no music, no voices. Framed around the known failure points: no passengers and no crowd anywhere in shot, station signage and destination boards kept outside the frame, no hands visible at all. Duration: 8s.
```

**KA**
```
ფართო პლანი. ერთი ცარიელი ფუნიკულიორის ვაგონი ბინდში, მოშიშვლებულ ხეებში, თბილისის თავზე ზემოთ მიიწევს. კამერა: ნელი პანორამა მარჯვნივ, ზუსტად ვაგონის სიჩქარით, არასდროს უსწრებს. განათება: ქედის უკან დარჩენილი ლურჯი დღის შუქი და ვაგონის საკუთარი თბილი სალონის ნათურები — ერთადერთი თბილი წყარო კადრში. განწყობა: დღის დასასრული, წყნარი. აუდიო: ბაგირის გუგუნი, ბორბლები ლიანდაგზე, ქარი შიშველ ტოტებში, ქვემოთ ქალაქიდან ერთი მანქანის სიგნალი; მუსიკის გარეშე, ადამიანის ხმის გარეშე. კადრი შედგენილია ცნობილი სუსტი წერტილების გვერდის ავლით: არც ბრბო ჩანს და არც ერთი მგზავრი, სადგურის წარწერა და მიმართულების დაფა კადრს გარეთ რჩება, ხელები საერთოდ არ ჩანს. ხანგრძლივობა: 8 წამი.
---
Wide shot. One empty funicular carriage climbs the track through bare trees above Tbilisi at dusk. Camera: slow pan right following the carriage at exactly its own speed, never running ahead of it. Lighting: last blue daylight from behind the ridge plus the carriage's own warm interior lamps, the only warm source in frame. Mood: end of day, quiet. Audio: cable hum, wheels on rail, wind in bare branches, one car horn from the city below, no music, no voices. Framed around the known failure points: no passengers and no crowd anywhere in shot, station signage and destination boards kept outside the frame, no hands visible at all. Duration: 8s.
```
