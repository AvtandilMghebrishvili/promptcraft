# Flux & Stable Diffusion

Two engines, two prompt shapes. **Flux** takes long fluent sentences and follows them closely —
write prose, not the comma-separated descriptor list Midjourney wants. **Stable Diffusion** takes
weighted tokens (`(sharp focus:1.3)`) plus a *separate negative prompt field*, and on SD the
checkpoint decides the style before your prompt gets a vote — an anime checkpoint returns anime
however carefully you word it. Descriptor logic otherwise follows
[`../../references/tool-routing.md`](../../references/tool-routing.md) §Image.

**On the Georgian block.** Neither engine reads Georgian reliably, so the `**KA**` block here is a
*working version*: the same prompt, negative prompt and settings in Georgian, so you can compose and
argue about the shot in your own language — then, after the `---` line, the English string you paste.

ქართული ბლოკი სამუშაო ვერსიაა — ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
SD-ზე სტილს პრომპტზე მეტად მოდელი (checkpoint) წყვეტს: ანიმეს მოდელი ანიმეს დააბრუნებს, როგორც არ უნდა დაწერო.

---

### FX-01 · Flux prose — chacha still in a village kitchen
`flux` — portrait, photography

**EN**
```
A copper still for distilling chacha stands on a low brick hearth in a village kitchen in Kakheti, its coiled condenser pipe running down into a scratched enamel bucket while the first of the distillate drips clear into a glass jar. An old man in a cardigan crouches beside it with one hand on the firebox door, watching the drip rather than the camera. Steam and woodsmoke hang in the air and catch the hard morning light coming through the single east window at frame left, which rakes across the copper and leaves the far corner of the room in unlit shadow. Shot from waist level on a 50mm lens at f/2, Kodak Portra 400, focus held on the mouth of the jar.
Settings: 28 steps, guidance 3.5, Flux.1 dev, 1152x1440
```

**KA**
```
ჩაჩის გამოსახდელი სპილენძის ქვაბი დგას დაბალ აგურის კერაზე, კახურ სოფლის სამზარეულოში; სპირალური გამაგრილებელი მილი გახეხილ მინანქრის ვედროში ჩადის, პირველი ნაწური კი გამჭვირვალედ წვეთავს შუშის ქილაში. გვერდით მოხუცი კაცი ჩაცუცქულია ჟაკეტში, ერთი ხელი საცეცხლის კარზე უდევს და კამერას კი არა, წვეთს უყურებს. ორთქლი და შეშის კვამლი ჰაერში დგას და იჭერს მკვეთრ დილის შუქს, რომელიც კადრის მარცხნიდან, ერთადერთი აღმოსავლეთის ფანჯრიდან შემოდის, ირიბად გადაუყვება სპილენძს და ოთახის შორეულ კუთხეს სრულ ჩრდილში ტოვებს. გადაღებულია წელის სიმაღლიდან, 50 მმ ობიექტივი, f/2, Kodak Portra 400, ფოკუსი ქილის ყელზე.
პარამეტრები: 28 ნაბიჯი, guidance 3.5, Flux.1 dev, 1152x1440
---
A copper still for distilling chacha stands on a low brick hearth in a village kitchen in Kakheti, its coiled condenser pipe running down into a scratched enamel bucket while the first of the distillate drips clear into a glass jar. An old man in a cardigan crouches beside it with one hand on the firebox door, watching the drip rather than the camera. Steam and woodsmoke hang in the air and catch the hard morning light coming through the single east window at frame left, which rakes across the copper and leaves the far corner of the room in unlit shadow. Shot from waist level on a 50mm lens at f/2, Kodak Portra 400, focus held on the mouth of the jar.
Settings: 28 steps, guidance 3.5, Flux.1 dev, 1152x1440
```

---

### FX-02 · SD photoreal portrait — weighted tokens
`stable-diffusion` — portrait, photography

**EN**
```
portrait of a woman in her fifties in a wool headscarf, three-quarter view, standing in the doorway of a stone house, (skin texture with visible pores:1.2), (sharp focus on the near eye:1.3), soft overcast light from open sky camera left, the hallway behind her falling into deep shade, 85mm, f/1.8, Kodak Portra 400, natural colour
Negative prompt: (blurry:1.4), (smooth plastic skin:1.3), (makeup:1.2), studio backdrop, direct flash, oversaturated
Checkpoint: photoreal family (Juggernaut / RealVis-class SDXL). On an anime checkpoint this same text returns a cartoon — change the checkpoint, not the prompt.
Settings: 30 steps, CFG 5, DPM++ 2M Karras, 896x1152
```

**KA**
```
ორმოცდაათს გადაცილებული ქალის პორტრეტი შალის თავსაფრით, სამმეოთხედი რაკურსი, ქვის სახლის კარებში დგას, (კანის ფაქტურა, ხილული ფორები:1.2), (მკვეთრი ფოკუსი ახლო თვალზე:1.3), რბილი ღრუბლიანი შუქი ღია ცის მხრიდან, კამერიდან მარცხნივ, მის უკან დერეფანი ღრმა ჩრდილში ეცემა, 85 მმ ობიექტივი, f/1.8, Kodak Portra 400, ბუნებრივი ფერები
ნეგატიური პრომპტი: (გადაბუნდოვნებული:1.4), (გლუვი, პლასტმასისებრი კანი:1.3), (მაკიაჟი:1.2), სტუდიური ფონი, პირდაპირი ფლეში, გადაჯერებული ფერები
მოდელი (checkpoint): ფოტორეალისტური ოჯახი (Juggernaut / RealVis კლასის SDXL). ანიმეს მოდელზე იგივე ტექსტი მულტიპლიკაციას დააბრუნებს — შეცვალე მოდელი და არა პრომპტი.
პარამეტრები: 30 ნაბიჯი, CFG 5, სემპლერი DPM++ 2M Karras, 896x1152
---
portrait of a woman in her fifties in a wool headscarf, three-quarter view, standing in the doorway of a stone house, (skin texture with visible pores:1.2), (sharp focus on the near eye:1.3), soft overcast light from open sky camera left, the hallway behind her falling into deep shade, 85mm, f/1.8, Kodak Portra 400, natural colour
Negative prompt: (blurry:1.4), (smooth plastic skin:1.3), (makeup:1.2), studio backdrop, direct flash, oversaturated
Checkpoint: photoreal family (Juggernaut / RealVis-class SDXL). On an anime checkpoint this same text returns a cartoon — change the checkpoint, not the prompt.
Settings: 30 steps, CFG 5, DPM++ 2M Karras, 896x1152
```

---

### FX-03 · Hands and fine detail — the classic failure case
`stable-diffusion` — macro, hands

**EN**
```
close-up of two hands winding a gut string onto the tuning peg of a panduri, (five fingers on each hand:1.3), (anatomically correct hands:1.2), (fingernails and knuckle creases in focus:1.2), the instrument's neck crossing the frame diagonally, bare workbench wood below, one warm lamp low from camera right raking along the fingers, 100mm macro, f/5.6, focus stacked
Negative prompt: (extra fingers:1.5), (fused fingers:1.4), (deformed hands:1.4), (six fingers:1.4), (blurry:1.3), mitten hands
Settings: 34 steps, CFG 6, DPM++ 2M Karras, 1024x1024, hires fix 1.5x at denoise 0.35
```

**KA**
```
ახლო პლანი: ორი ხელი პანდურის საჭიმ კოჭზე ძარღვის სიმს ახვევს, (თითო ხელზე ხუთი თითი:1.3), (ანატომიურად სწორი ხელები:1.2), (ფრჩხილები და სახსრების ნაკეცები ფოკუსში:1.2), ინსტრუმენტის ტარი კადრს ირიბად კვეთს, ქვემოთ სახელოსნო მაგიდის შიშველი ხე, ერთი თბილი ნათურა დაბლა, კამერიდან მარჯვნივ, ირიბად უყვება თითებს, 100 მმ მაკრო ობიექტივი, f/5.6, დაწყობილი ფოკუსი
ნეგატიური პრომპტი: (ზედმეტი თითები:1.5), (შეზრდილი თითები:1.4), (დეფორმირებული ხელები:1.4), (ექვსი თითი:1.4), (გადაბუნდოვნებული:1.3), ხელთათმანივით შერწყმული თითები
პარამეტრები: 34 ნაბიჯი, CFG 6, სემპლერი DPM++ 2M Karras, 1024x1024, hires fix 1.5x, დენოისი 0.35
---
close-up of two hands winding a gut string onto the tuning peg of a panduri, (five fingers on each hand:1.3), (anatomically correct hands:1.2), (fingernails and knuckle creases in focus:1.2), the instrument's neck crossing the frame diagonally, bare workbench wood below, one warm lamp low from camera right raking along the fingers, 100mm macro, f/5.6, focus stacked
Negative prompt: (extra fingers:1.5), (fused fingers:1.4), (deformed hands:1.4), (six fingers:1.4), (blurry:1.3), mitten hands
Settings: 34 steps, CFG 6, DPM++ 2M Karras, 1024x1024, hires fix 1.5x at denoise 0.35
```

---

### FX-04 · Text in image — Tbilisi metro platform
`flux` — signage, photography

**EN**
```
An empty Tbilisi metro platform late at night, the tunnel mouth black at the far end and the tiled vault curving overhead. On the wall behind the bench a large enamel sign reads "RUSTAVELI" in clean white capitals on a deep red panel, and a smaller white plate beneath it reads "EXIT" beside an arrow. One passenger sits at the far end of the bench looking down the tunnel. Cold fluorescent strips run the length of the vault and reflect in the polished granite floor, and there is no other light source in the frame. Wide shot from platform level, 24mm, f/4, Cinestill 800T, the sign fully legible and in focus.
Settings: 30 steps, guidance 3.5, Flux.1 dev, 1536x864 — spell sign text in Latin capitals; Flux garbles Georgian mkhedruli at any size.
```

**KA**
```
თბილისის მეტროს ცარიელი პლატფორმა გვიან ღამით, გვირაბის პირი შორს შავად ჩანს, ფილებით მოპირკეთებული თაღი თავზე გადაშლილი. სკამის უკან კედელზე დიდი მინანქრის აბრა წერს „RUSTAVELI“ თეთრი ლათინური მაიუსკულით მუქ წითელ ველზე, ქვემოთ კი პატარა თეთრ ფირფიტაზე ისრის გვერდით ეწერა „EXIT“. სკამის შორეულ ბოლოში ერთი მგზავრი ზის და გვირაბისკენ იყურება. ცივი დღის ნათურების ზოლები თაღის მთელ სიგრძეზე მიუყვება და გაპრიალებულ გრანიტის იატაკზე აირეკლება; კადრში სხვა შუქის წყარო არ არის. ფართო პლანი პლატფორმის დონიდან, 24 მმ ობიექტივი, f/4, Cinestill 800T, აბრის წარწერა სრულად იკითხება და ფოკუსშია.
პარამეტრები: 30 ნაბიჯი, guidance 3.5, Flux.1 dev, 1536x864 — აბრის ტექსტი ლათინური მაიუსკულით ჩაწერე; მხედრულს Flux ნებისმიერ ზომაზე ამახინჯებს.
---
An empty Tbilisi metro platform late at night, the tunnel mouth black at the far end and the tiled vault curving overhead. On the wall behind the bench a large enamel sign reads "RUSTAVELI" in clean white capitals on a deep red panel, and a smaller white plate beneath it reads "EXIT" beside an arrow. One passenger sits at the far end of the bench looking down the tunnel. Cold fluorescent strips run the length of the vault and reflect in the polished granite floor, and there is no other light source in the frame. Wide shot from platform level, 24mm, f/4, Cinestill 800T, the sign fully legible and in focus.
Settings: 30 steps, guidance 3.5, Flux.1 dev, 1536x864 — spell sign text in Latin capitals; Flux garbles Georgian mkhedruli at any size.
```

---

### FX-05 · Product render on a seamless sweep
`flux` — product, studio

**EN**
```
A squat amber glass bottle of cold-pressed sunflower oil stands three-quarter on a slab of grey basalt, its matte paper label blank and unbranded, the oil reading gold where the light passes through it. Behind the bottle the background falls away to an even warm grey with no visible horizon line. A large softbox sits high and camera right, just behind the shoulder of the bottle, so the glass carries one long soft highlight down its right edge; a white card at camera left returns a thin cool rim on the opposite side, and a single small hard specular lands on the cap. Nothing else is in frame. Shot on a 100mm macro at f/11, focus stacked front to back, studio product photography, clean and unstyled.
Settings: 30 steps, guidance 3.5, Flux.1 dev, 1152x1440
```

**KA**
```
ქარვისფერი შუშის დაბალი ბოთლი ცივად დაწურული მზესუმზირის ზეთით დგას რუხი ბაზალტის ფილაზე, სამმეოთხედი რაკურსით; ქაღალდის მქრქალი ეტიკეტი ცარიელია, წარწერის გარეშე, ზეთი კი შუქზე ოქროსფრად ანათებს. ბოთლის უკან ფონი თანაბარ თბილ ნაცრისფერში გადადის, ჰორიზონტის ხაზის გარეშე. დიდი სოფტბოქსი მაღლა, კამერიდან მარჯვნივ, ბოთლის მხრის ოდნავ უკან დგას, ასე რომ მინის მარჯვენა კიდეზე ერთი გრძელი რბილი ელვარება ჩნდება; მარცხნიდან თეთრი ეკრანი თხელ ცივ კონტურს აბრუნებს, თავსახურზე კი ერთი პატარა მკვეთრი ბზინვარება ჯდება. კადრში სხვა არაფერია. 100 მმ მაკრო ობიექტივი, f/11, ფოკუსი წინიდან უკან დაწყობილი, სტუდიური საგნობრივი ფოტოგრაფია, სუფთა, ზედმეტი გაწყობის გარეშე.
პარამეტრები: 30 ნაბიჯი, guidance 3.5, Flux.1 dev, 1152x1440
---
A squat amber glass bottle of cold-pressed sunflower oil stands three-quarter on a slab of grey basalt, its matte paper label blank and unbranded, the oil reading gold where the light passes through it. Behind the bottle the background falls away to an even warm grey with no visible horizon line. A large softbox sits high and camera right, just behind the shoulder of the bottle, so the glass carries one long soft highlight down its right edge; a white card at camera left returns a thin cool rim on the opposite side, and a single small hard specular lands on the cap. Nothing else is in frame. Shot on a 100mm macro at f/11, focus stacked front to back, studio product photography, clean and unstyled.
Settings: 30 steps, guidance 3.5, Flux.1 dev, 1152x1440
```

---

### FX-06 · Architectural exterior — Saburtalo hillside block
`flux` — architecture, photography

**EN**
```
A 1970s concrete residential block steps down a steep Saburtalo hillside in Tbilisi, eight storeys of repeated balcony bays, half of them glazed in by their owners with mismatched frames, satellite dishes and drying laundry breaking the grid. Bare plane trees stand along the road in front of it. Low winter sun comes from the left at a shallow angle, throwing the balcony slabs into long horizontal shadows across the façade and leaving the recessed stairwells almost black. The camera is across the street at street level with the verticals kept parallel, the building filling the frame edge to edge and a narrow band of pale sky left above it. 24mm tilt-shift, f/8, Kodak Ektar 100, architectural exterior photography.
Settings: 28 steps, guidance 3.0, Flux.1 dev, 1536x1024
```

**KA**
```
70-იანი წლების ბეტონის საცხოვრებელი კორპუსი საბურთალოს ციცაბო ფერდობზე საფეხურებად ჩამოდის, რვა სართული ერთნაირი აივნის უჯრებით, ნახევარი მათგანი მესაკუთრეებს სხვადასხვა ჩარჩოთი აქვთ შეშუშული, თანამგზავრული თეფშები და გაფენილი სარეცხი ბადეს არღვევს. წინ, გზის გასწვრივ, შიშველი ჭადრები დგას. დაბალი ზამთრის მზე მარცხნიდან, ბლაგვი კუთხით ეცემა, აივნის ფილებს გრძელ ჰორიზონტალურ ჩრდილებად აგდებს ფასადზე და ჩაღრმავებულ სადარბაზოებს თითქმის შავად ტოვებს. კამერა ქუჩის მეორე მხარეს, მიწის დონეზეა, ვერტიკალები პარალელურად შენარჩუნებული, შენობა კადრს კიდიდან კიდემდე ავსებს, ზემოთ კი ღია ცის ვიწრო ზოლი რჩება. 24 მმ tilt-shift ობიექტივი, f/8, Kodak Ektar 100, არქიტექტურული ექსტერიერის ფოტოგრაფია.
პარამეტრები: 28 ნაბიჯი, guidance 3.0, Flux.1 dev, 1536x1024
---
A 1970s concrete residential block steps down a steep Saburtalo hillside in Tbilisi, eight storeys of repeated balcony bays, half of them glazed in by their owners with mismatched frames, satellite dishes and drying laundry breaking the grid. Bare plane trees stand along the road in front of it. Low winter sun comes from the left at a shallow angle, throwing the balcony slabs into long horizontal shadows across the façade and leaving the recessed stairwells almost black. The camera is across the street at street level with the verticals kept parallel, the building filling the frame edge to edge and a narrow band of pale sky left above it. 24mm tilt-shift, f/8, Kodak Ektar 100, architectural exterior photography.
Settings: 28 steps, guidance 3.0, Flux.1 dev, 1536x1024
```

---

### FX-07 · Painterly illustration — checkpoint decides this one
`stable-diffusion` — illustration, painterly

**EN**
```
a fox curled asleep among the roots of a beech tree, autumn leaf litter, (painterly brushwork with visible strokes:1.3), (soft edges:1.2), low warm sun filtering through the canopy from behind the tree, muted ochre and olive palette, storybook illustration
Negative prompt: (photorealistic:1.4), (3d render:1.3), (harsh black outlines:1.2), text, signature
Checkpoint: illustration / painterly family (Dreamshaper- or Pony-class). On a photoreal checkpoint these same tokens give you a slightly soft photograph of a fox — (painterly:1.3) cannot outvote the model.
Settings: 28 steps, CFG 7, Euler a, 1216x832
```

**KA**
```
მელას წიფლის ფესვებში დახვეულს სძინავს, შემოდგომის ფოთოლცვენა, (ხილული ფუნჯის მონასმები:1.3), (რბილი კიდეები:1.2), დაბალი თბილი მზე ხის უკნიდან ვარჯში იფილტრება, დაწყნარებული ოხრისა და ზეთისხილისფერი პალიტრა, საბავშვო წიგნის ილუსტრაცია
ნეგატიური პრომპტი: (ფოტორეალიზმი:1.4), (3D რენდერი:1.3), (მკვეთრი შავი კონტური:1.2), ტექსტი, ხელმოწერა
მოდელი (checkpoint): ილუსტრაციის/მხატვრული ოჯახი (Dreamshaper ან Pony კლასი). ფოტორეალისტურ მოდელზე იგივე ტოკენები ოდნავ რბილ ფოტოს მოგცემს — (painterly:1.3) მოდელს ვერ გადაწონის.
პარამეტრები: 28 ნაბიჯი, CFG 7, სემპლერი Euler a, 1216x832
---
a fox curled asleep among the roots of a beech tree, autumn leaf litter, (painterly brushwork with visible strokes:1.3), (soft edges:1.2), low warm sun filtering through the canopy from behind the tree, muted ochre and olive palette, storybook illustration
Negative prompt: (photorealistic:1.4), (3d render:1.3), (harsh black outlines:1.2), text, signature
Checkpoint: illustration / painterly family (Dreamshaper- or Pony-class). On a photoreal checkpoint these same tokens give you a slightly soft photograph of a fox — (painterly:1.3) cannot outvote the model.
Settings: 28 steps, CFG 7, Euler a, 1216x832
```

---

### FX-08 · Same character across generations — seed + fixed identity block
`stable-diffusion` — character, consistency

**EN**
```
[identity block — reuse word for word in every generation] a 30-year-old woman, square jaw, wide-set grey eyes, a scar through the left eyebrow, black hair cut blunt at the chin, one silver stud in the right ear, (consistent facial features:1.2)
[scene block — the only part you change] standing at a bus stop in the rain, hood down, three-quarter view, cold evening light from a shop window camera right, 50mm, f/2, Kodak Portra 400
Negative prompt: (changing face:1.3), (blurry:1.3), heavy makeup, beauty filter
Checkpoint: one photoreal checkpoint locked for the whole set — swapping checkpoints mid-set changes the face more than rewriting the description does.
Settings: 30 steps, CFG 5, DPM++ 2M Karras, 832x1216, seed 774213 fixed. Change only the scene block between runs.
```

**KA**
```
[იდენტობის ბლოკი — ყოველ გენერაციაში სიტყვასიტყვით იმეორებ] ოცდაათი წლის ქალი, კუთხოვანი ყბა, ფართოდ დაშორებული რუხი თვალები, მარცხენა წარბზე გამჭოლი ნაწიბური, შავი თმა ნიკაპის სიმაღლეზე სწორად შეჭრილი, მარჯვენა ყურში ერთი ვერცხლის საყურე, (მუდმივი სახის ნაკვთები:1.2)
[სცენის ბლოკი — მხოლოდ ეს იცვლება] ავტობუსის გაჩერებაზე დგას წვიმაში, კაპიუშონი ჩამოხდილი, სამმეოთხედი რაკურსი, ცივი საღამოს შუქი მაღაზიის ვიტრინიდან, კამერიდან მარჯვნივ, 50 მმ ობიექტივი, f/2, Kodak Portra 400
ნეგატიური პრომპტი: (სახის ცვლილება:1.3), (გადაბუნდოვნებული:1.3), მძიმე მაკიაჟი, სილამაზის ფილტრი
მოდელი (checkpoint): ერთი ფოტორეალისტური მოდელი მთელი სერიისთვის, დაფიქსირებული — სერიის შუაში მოდელის შეცვლა სახეს უფრო მეტად ცვლის, ვიდრე აღწერის გადაწერა.
პარამეტრები: 30 ნაბიჯი, CFG 5, სემპლერი DPM++ 2M Karras, 832x1216, ფიქსირებული seed 774213. გაშვებებს შორის მხოლოდ სცენის ბლოკს ცვლი.
---
[identity block — reuse word for word in every generation] a 30-year-old woman, square jaw, wide-set grey eyes, a scar through the left eyebrow, black hair cut blunt at the chin, one silver stud in the right ear, (consistent facial features:1.2)
[scene block — the only part you change] standing at a bus stop in the rain, hood down, three-quarter view, cold evening light from a shop window camera right, 50mm, f/2, Kodak Portra 400
Negative prompt: (changing face:1.3), (blurry:1.3), heavy makeup, beauty filter
Checkpoint: one photoreal checkpoint locked for the whole set — swapping checkpoints mid-set changes the face more than rewriting the description does.
Settings: 30 steps, CFG 5, DPM++ 2M Karras, 832x1216, seed 774213 fixed. Change only the scene block between runs.
```

---

### FX-09 · img2img and the upscale-refine pass — Kazbegi road in fog
`stable-diffusion` `flux` — img2img, upscale

**EN**
```
a flatbed truck crawling uphill on the wet Georgian Military Highway near Kazbegi, headlights on, the road disappearing into thick fog twenty metres ahead, a guardrail and one snow pole at the right edge, dark firs barely readable as shapes behind it, flat diffuse grey light with no visible sun, (fog density:1.2), (wet asphalt reflections:1.2), 135mm, f/4, Kodak Portra 400
Negative prompt: (clear sky:1.4), (blurry:1.3), (oversharpened halos:1.3), lens flare, hdr
Settings: pass 1 — img2img over your own photo at denoise 0.45, high enough to restyle the light, low enough to keep the road geometry and the truck. Pass 2 — upscale 2x, run img2img again at denoise 0.2, 20 steps, CFG 4, same seed. Above 0.3 on the second pass the model reinvents the guardrail.
```

**KA**
```
ბაქნიანი სატვირთო ნელა ადის სველ საქართველოს სამხედრო გზაზე ყაზბეგთან, ფარები ანთებული, გზა ოცი მეტრის იქით სქელ ნისლში იკარგება, მარჯვენა კიდეზე მოაჯირი და ერთი თოვლის ბოძი, უკან მუქი ნაძვები ნისლში მხოლოდ ფორმებად იკითხება, ბრტყელი გაბნეული ნაცრისფერი შუქი, მზე არ ჩანს, (ნისლის სიმკვრივე:1.2), (სველი ასფალტის ანარეკლი:1.2), 135 მმ ობიექტივი, f/4, Kodak Portra 400
ნეგატიური პრომპტი: (უღრუბლო ცა:1.4), (გადაბუნდოვნებული:1.3), (გადამკვეთრებული კონტურები:1.3), ბლიკი, hdr
პარამეტრები: პირველი გავლა — img2img შენსავე ფოტოზე, დენოისი 0.45: საკმარისი შუქის გადასაწერად და საკმარისად დაბალი, რომ გზის გეომეტრია და სატვირთო შენარჩუნდეს. მეორე გავლა — 2x გადიდება, ისევ img2img, დენოისი 0.2, 20 ნაბიჯი, CFG 4, იგივე seed. მეორე გავლაზე 0.3-ზე მაღლა მოდელი მოაჯირს თავიდან იგონებს.
---
a flatbed truck crawling uphill on the wet Georgian Military Highway near Kazbegi, headlights on, the road disappearing into thick fog twenty metres ahead, a guardrail and one snow pole at the right edge, dark firs barely readable as shapes behind it, flat diffuse grey light with no visible sun, (fog density:1.2), (wet asphalt reflections:1.2), 135mm, f/4, Kodak Portra 400
Negative prompt: (clear sky:1.4), (blurry:1.3), (oversharpened halos:1.3), lens flare, hdr
Settings: pass 1 — img2img over your own photo at denoise 0.45, high enough to restyle the light, low enough to keep the road geometry and the truck. Pass 2 — upscale 2x, run img2img again at denoise 0.2, 20 steps, CFG 4, same seed. Above 0.3 on the second pass the model reinvents the guardrail.
```
