# Brand & Product / ბრენდი და პროდუქტი

Commercial work: pack shots, lifestyle, mockups, shelf renders, ad creative. Every entry names an
aspect ratio for a real placement, and wherever type will sit over the image the prompt reserves the
space and says which part of the frame it holds clear.

**On the Georgian block.** As everywhere in this library the `**KA**` block is a *working version* —
the same shot described in Georgian so you can compose, edit and argue about it in your own language —
and after the `---` line comes the English string you actually paste. This holds for all three tools
here; none of them takes Georgian input reliably.

**On consistency.** A catalogue, a team page or a campaign is not a set of good images, it is one
image made several times. Repeat the lighting clause, the lens and the colour language word for word
across the set and change only the subject clause; in Midjourney add a fixed `--seed` and the same
`--sref`. BP-01, BP-07 and BP-11 are built around this.

ქართული ბლოკი სამუშაო ვერსიაა — ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
სერიაში (კატალოგი, გუნდი, კამპანია) განათების წინადადება, ობიექტივი და ფერის ენა სიტყვასიტყვით
გაიმეორე და მხოლოდ პროდუქტის აღწერა შეცვალე; Midjourney-ში დაამატე ფიქსირებული `--seed` და იგივე `--sref`.

`→` ნიშნით დაწყებული ხაზი შენთვისაა და ჩასასმელ სტრიქონში არ შედის.
Lines starting with `→` are notes to you, not part of the string you paste.

---

### BP-01 · Cutout-ready pack shot on a seamless sweep
`flux` — product, e-commerce, holds an exact background value across a whole catalogue

**EN**
```
A 50ml amber glass cosmetics jar with a brushed aluminium lid, label panel square to the camera, standing dead centre on a seamless light grey sweep at RGB 235,235,235 with no visible horizon line and nothing else in frame. A large softbox forty-five degrees from camera left and slightly above the lid is the key; a white bounce card at camera right opens the shadow side to a two-stop ratio; one narrow strip box behind camera right draws a single thin highlight down the right edge of the glass. The jar sits directly on the sweep with a short contact shadow beneath it and clean falloff within two centimetres, so the product cuts out without fringing. Square 1:1 frame with even margins, the jar filling the middle seventy percent of the height. Studio product photography, 100mm macro, f/11, focus stacked front to back, neutral white balance, colour-accurate.
→ consistency: for every other SKU in the catalogue change only the first sentence. The sweep value, the key-fill-strip sentence, the 100mm f/11 and the white balance stay byte-for-byte identical, and the seed stays fixed, or the grey behind each product will drift and the row will not line up.
```

**KA**
```
50 მლ ყავისფერი შუშის კოსმეტიკური ქილა გახეხილი ალუმინის სახურავით, ეტიკეტი კამერის პირდაპირ, ზუსტად ცენტრში, ერთიან ღია ნაცრისფერ ფონზე RGB 235,235,235, ჰორიზონტის ხაზისა და სხვა საგნის გარეშე. მთავარი შუქი — დიდი სოფტბოქსი კამერიდან მარცხნივ, 45 გრადუსზე, სახურავზე ოდნავ მაღლა; თეთრი ამრეკლი კამერიდან მარჯვნივ ჩრდილოვან მხარეს 2 საფეხურით ავსებს; ვიწრო სტრიპ-სოფტბოქსი კამერის უკან, მარჯვნივ, შუშის მარჯვენა კიდეზე ერთ თხელ ბზინვარებას ხატავს. ქილა უშუალოდ ფონზე დგას, ქვეშ მოკლე კონტაქტური ჩრდილი, რომელიც 2 სანტიმეტრში ქრება — რომ პროდუქტი კონტურის ნაფლეთების გარეშე ამოიჭრას. კვადრატული 1:1 კადრი თანაბარი მინდვრებით, ქილა სიმაღლის შუა 70 პროცენტს იკავებს. სტუდიური საგნობრივი ფოტოგრაფია, 100 მმ მაკრო ობიექტივი, f/11, დაწყობილი ფოკუსი, ნეიტრალური თეთრის ბალანსი, ზუსტი ფერები.
→ სერიისთვის: კატალოგის ყოველ სხვა პროდუქტზე მხოლოდ პირველი წინადადება შეცვალე. ფონის მნიშვნელობა, განათების წინადადება, 100 მმ f/11 და თეთრის ბალანსი უცვლელი რჩება, seed კი ფიქსირებული — თორემ ფონის ნაცრისფერი თითოეულ კადრში სხვაგვარი გამოვა და რიგი არ აეწყობა.
---
A 50ml amber glass cosmetics jar with a brushed aluminium lid, label panel square to the camera, standing dead centre on a seamless light grey sweep at RGB 235,235,235 with no visible horizon line and nothing else in frame. A large softbox forty-five degrees from camera left and slightly above the lid is the key; a white bounce card at camera right opens the shadow side to a two-stop ratio; one narrow strip box behind camera right draws a single thin highlight down the right edge of the glass. The jar sits directly on the sweep with a short contact shadow beneath it and clean falloff within two centimetres, so the product cuts out without fringing. Square 1:1 frame with even margins, the jar filling the middle seventy percent of the height. Studio product photography, 100mm macro, f/11, focus stacked front to back, neutral white balance, colour-accurate.
```

---

### BP-02 · Product in a lifestyle context
`midjourney` — lifestyle, product, best texture and window light of the three

**EN**
```
an open 250g jar of chestnut honey on a worn oak kitchen counter, a wooden dipper resting across the rim with one thread of honey running off it, a torn piece of bread and a chipped enamel mug just behind, a linen curtain and a blown-out window far back and fully defocused, three-quarter view from just above the rim, jar in the left third with the label panel unobstructed and clear counter space to the right, low morning sun from camera right raking along the grain of the oak and laying a long soft shadow to the left, warm 4800K daylight with no artificial fill, lifestyle product photography, 50mm, f/2.8, label plane held sharp, background falling off fast --ar 4:5 --style raw --stylize 100 --no clutter, text, plastic
```

**KA**
```
გახსნილი 250 გრამიანი წაბლის თაფლის ქილა გაცვეთილ მუხის სამზარეულოს მაგიდაზე, ხის ჩხირი კიდეზე გადებული, მისგან თაფლის ერთი ძაფი ჩამოდის, უკან მოტეხილი პური და ჩამოცვენილი ემალის ჭიქა, კიდევ უფრო შორს თეთრეულის ფარდა და გადანათებული ფანჯარა სრულად დაბუნდოვნებული, სამმეოთხედი რაკურსი, კამერა ქილის კიდეზე ოდნავ მაღლა, ქილა კადრის მარცხენა მესამედში, ეტიკეტი გადაუფარავი, მარჯვნივ თავისუფალი მაგიდა, დილის დაბალი მზე კამერიდან მარჯვნივ, ირიბად მუხის ბოჭკოზე, გრძელი რბილი ჩრდილი მარცხნივ, თბილი 4800K დღის შუქი, ხელოვნური შუქის დამატების გარეშე, ლაიფსტაილ საგნობრივი ფოტოგრაფია, 50 მმ ობიექტივი, f/2.8, ეტიკეტის სიბრტყე მკვეთრი, ფონი სწრაფად ეცემა --ar 4:5 --style raw --stylize 100 --no clutter, text, plastic
---
an open 250g jar of chestnut honey on a worn oak kitchen counter, a wooden dipper resting across the rim with one thread of honey running off it, a torn piece of bread and a chipped enamel mug just behind, a linen curtain and a blown-out window far back and fully defocused, three-quarter view from just above the rim, jar in the left third with the label panel unobstructed and clear counter space to the right, low morning sun from camera right raking along the grain of the oak and laying a long soft shadow to the left, warm 4800K daylight with no artificial fill, lifestyle product photography, 50mm, f/2.8, label plane held sharp, background falling off fast --ar 4:5 --style raw --stylize 100 --no clutter, text, plastic
```

---

### BP-03 · Flat-lay of a product set
`midjourney` — flat-lay, range shot, one square for the Instagram grid

**EN**
```
six items of a Georgian pantry range laid out in a loose two by three grid — a jar of svanuri marili, a pouch of blue fenugreek, a jar of ajika, a bottle of tkemali, a pouch of walnut spice mix and a jar of dried marigold — all lids square to the camera, on a grey-green limewashed plaster board, a folded linen cloth in the bottom right corner and three walnuts as the only props, seen straight down from directly above with the plaster filling the frame, even spacing between items and a clear margin of one eighth of the frame on all four sides, large diffused overhead source from the top of the frame with a black flag along the bottom keeping every shadow short and falling the same way, flat-lay product photography, 50mm, f/8, evenly lit corner to corner --ar 1:1 --style raw --stylize 75 --no hands, text, perspective distortion
```

**KA**
```
ქართული სამზარეულოს ექვსი პროდუქტი ორ რიგად, სამ-სამი — სვანური მარილის ქილა, ულუმბოს პაკეტი, აჯიკის ქილა, ტყემლის ბოთლი, ნიგვზის სანელებლის პაკეტი და ხმელი ყვითელი ყვავილის ქილა — ყველა სახურავი კამერისკენ, მოყვითალო-მომწვანო კირით შელესილ ფიცარზე, მარჯვენა ქვედა კუთხეში დაკეცილი თეთრეულის ტილო, სხვა რეკვიზიტი მხოლოდ 3 ნიგოზი, ხედი ზემოდან, მკაცრად ვერტიკალური კუთხით, ლესილი ზედაპირი მთელ კადრს ავსებს, თანაბარი მანძილი საგნებს შორის და კადრის მერვედის ტოლი თავისუფალი მინდორი ოთხივე მხრიდან, დიდი გაბნეული შუქი ზემოდან, კადრის ზედა კიდიდან, ქვემოთ შავი ფარი ჩრდილებს მოკლედ და ერთი მიმართულებით ტოვებს, ზემოდან გადაღებული საგნობრივი ფოტოგრაფია, 50 მმ ობიექტივი, f/8, თანაბარი განათება კუთხიდან კუთხემდე --ar 1:1 --style raw --stylize 75 --no hands, text, perspective distortion
---
six items of a Georgian pantry range laid out in a loose two by three grid — a jar of svanuri marili, a pouch of blue fenugreek, a jar of ajika, a bottle of tkemali, a pouch of walnut spice mix and a jar of dried marigold — all lids square to the camera, on a grey-green limewashed plaster board, a folded linen cloth in the bottom right corner and three walnuts as the only props, seen straight down from directly above with the plaster filling the frame, even spacing between items and a clear margin of one eighth of the frame on all four sides, large diffused overhead source from the top of the frame with a black flag along the bottom keeping every shadow short and falling the same way, flat-lay product photography, 50mm, f/8, evenly lit corner to corner --ar 1:1 --style raw --stylize 75 --no hands, text, perspective distortion
```

---

### BP-04 · Packaging mockup on a shop shelf
`gpt-image` — packaging, mockup, the only one of the three that renders label text you can read

**EN**
```
A retail shelf in a Tbilisi supermarket with three cartons of a mountain herbal tea brand standing at eye level on the middle pine shelf. The front carton faces the camera square on and the two behind it are turned a few degrees away; each is matte uncoated board in deep forest green with a cream panel across the lower half, and the panel carries the words "MTIS CHAI" in a narrow serif with "50g" beneath it in small caps. Rows of softly out-of-focus boxes in muted colours continue to the left and right and on the shelves above and below, with a white price rail along the front edge of each shelf. Cool overhead fluorescent strip lighting from directly above plus a soft frontal fill keeps the uncoated board matte and the carton edges crisp. Horizontal 3:2 frame with the three cartons held in the centre, one shelf visible above and one below. Packaging mockup rendered as commercial retail photography, 50mm, f/4, the shelf plane sharp and the background rows falling gently out of focus.
→ keep the panel text in Latin. Set the Georgian wordmark over the render afterwards; every image model still garbles Georgian script.
```

**KA**
```
თბილისური სუპერმარკეტის თარო, შუა ფიჩვის თაროზე, თვალის დონეზე, მთის მცენარეული ჩაის ბრენდის 3 კოლოფი დგას. წინა კოლოფი პირდაპირ კამერისკენაა მიმართული, უკანა ორი რამდენიმე გრადუსით არის შემობრუნებული; თითოეული მქრქალი, დაუფარავი მუყაოსია, მუქი მწვანე, ქვედა ნახევარზე კრემისფერი ველით, ველზე ვიწრო სერიფული ასოებით ეწერა „MTIS CHAI“, ქვემოთ კი პატარა ასოებით „50g“. მარცხნივ, მარჯვნივ და ზედა და ქვედა თაროებზე დაწყნარებული ფერების კოლოფების რიგები გრძელდება, ოდნავ დაბუნდოვნებული, თითოეული თაროს წინა კიდეზე თეთრი ფასის ლენტია. ცივი დღის ნათურები პირდაპირ ზემოდან და რბილი შუქი წინიდან — მუყაო მქრქალი რჩება, კოლოფის წიბოები კი მკვეთრი. ჰორიზონტალური 3:2 კადრი, სამი კოლოფი ცენტრშია, ზემოთ ერთი თარო ჩანს და ქვემოთ ერთი. შეფუთვის მაკეტი, გადაღებული როგორც კომერციული სავაჭრო ფოტოგრაფია, 50 მმ ობიექტივი, f/4, თაროს სიბრტყე მკვეთრი, უკანა რიგები ნაზად გასული ფოკუსიდან.
→ ეტიკეტის ტექსტი ლათინურად დატოვე. ქართული ლოგოტიპი მაკეტზე შემდეგ დაადე — ქართულ დამწერლობას ჯერჯერობით ვერცერთი მოდელი ვერ ხატავს.
---
A retail shelf in a Tbilisi supermarket with three cartons of a mountain herbal tea brand standing at eye level on the middle pine shelf. The front carton faces the camera square on and the two behind it are turned a few degrees away; each is matte uncoated board in deep forest green with a cream panel across the lower half, and the panel carries the words "MTIS CHAI" in a narrow serif with "50g" beneath it in small caps. Rows of softly out-of-focus boxes in muted colours continue to the left and right and on the shelves above and below, with a white price rail along the front edge of each shelf. Cool overhead fluorescent strip lighting from directly above plus a soft frontal fill keeps the uncoated board matte and the carton edges crisp. Horizontal 3:2 frame with the three cartons held in the centre, one shelf visible above and one below. Packaging mockup rendered as commercial retail photography, 50mm, f/4, the shelf plane sharp and the background rows falling gently out of focus.
```

---

### BP-05 · Chilled bottle, condensation and controlled reflections
`flux` — beverage, reflection control, follows a named two-strip lighting plan literally

**EN**
```
A chilled 750ml bottle of Kakhetian rkatsiteli in dark olive glass, label square to the camera, standing on a wet slab of grey basalt against a deep charcoal background that falls to near black at the edges of the frame. A tall vertical strip box behind and to camera left renders one continuous soft white highlight down the left shoulder and body of the bottle; a second, narrower strip behind camera right renders a brighter thin line down the right edge; a black flag between the two keeps the centre of the glass dark so the label stays legible against it. Fine condensation beads cover the upper two thirds of the glass and three heavier drops have run down, leaving clear tracks through the mist; a shallow ring of meltwater on the basalt catches one soft reflection of the bottle and nothing else. Vertical 4:5 frame with the bottle slightly right of centre and the upper left corner left dark and empty for a headline. Studio beverage photography, 100mm macro, f/13, focus stacked from the neck to the base, cool neutral grade with a single warm note in the wet stone.
```

**KA**
```
გაცივებული 750 მლ კახური რქაწითელის ბოთლი მუქ ზეთისხილისფერ შუშაში, ეტიკეტი კამერის პირდაპირ, სველ ნაცრისფერ ბაზალტის ფილაზე დგას, ფონი ღრმა ნახშირისფერია და კადრის კიდეებში თითქმის შავში გადადის. მაღალი ვერტიკალური სტრიპ-სოფტბოქსი ბოთლის უკან, კამერიდან მარცხნივ, ერთ უწყვეტ რბილ თეთრ ბზინვარებას ხატავს ბოთლის მარცხენა მხარზე და ტანზე; მეორე, უფრო ვიწრო სტრიპი კამერის უკან, მარჯვნივ, მარჯვენა კიდეზე უფრო კაშკაშა თხელ ხაზს ავლებს; ორს შორის შავი ფარი შუშის შუა ნაწილს ბნელად ტოვებს, რომ ეტიკეტი მკაფიოდ იკითხებოდეს. წვრილი ნამი შუშის ზედა ორ მესამედს ფარავს, 3 მსხვილი წვეთი ჩამოსულია და ნისლში გამჭვირვალე კვალი დაუტოვებია; ბაზალტზე გამდნარი წყლის თხელი რგოლი ბოთლის ერთადერთ რბილ რეფლექსს იჭერს. ვერტიკალური 4:5 კადრი, ბოთლი ცენტრიდან ოდნავ მარჯვნივ, ზედა მარცხენა კუთხე ბნელი და ცარიელი რჩება სათაურისთვის. სტუდიური სასმელის ფოტოგრაფია, 100 მმ მაკრო ობიექტივი, f/13, დაწყობილი ფოკუსი ყელიდან ძირამდე, ცივი ნეიტრალური ფერის დამუშავება, ერთადერთი თბილი ნოტა სველ ქვაზე.
---
A chilled 750ml bottle of Kakhetian rkatsiteli in dark olive glass, label square to the camera, standing on a wet slab of grey basalt against a deep charcoal background that falls to near black at the edges of the frame. A tall vertical strip box behind and to camera left renders one continuous soft white highlight down the left shoulder and body of the bottle; a second, narrower strip behind camera right renders a brighter thin line down the right edge; a black flag between the two keeps the centre of the glass dark so the label stays legible against it. Fine condensation beads cover the upper two thirds of the glass and three heavier drops have run down, leaving clear tracks through the mist; a shallow ring of meltwater on the basalt catches one soft reflection of the bottle and nothing else. Vertical 4:5 frame with the bottle slightly right of centre and the upper left corner left dark and empty for a headline. Studio beverage photography, 100mm macro, f/13, focus stacked from the neck to the base, cool neutral grade with a single warm note in the wet stone.
```

---

### BP-06 · Dish styled for a menu
`midjourney` — food, menu card, handles steam and glaze better than the others

**EN**
```
an adjarian khachapuri straight out of the oven on the pass of a Batumi restaurant, the yolk whole and glossy in the middle of the cheese, a knob of butter half melted beside it, on a matte black ceramic plate on a dark walnut table, a linen napkin and the tip of a fork entering the bottom right corner, three-quarter view from thirty degrees above the plate with the boat shape running diagonally from lower left to upper right, hard backlight from camera left behind the plate catching the steam and the blistered glaze on the crust, a large white bounce card at the front lifting the shadows just enough to read the cheese, restaurant menu photography, 90mm macro, f/5.6, focus on the yolk, natural colour with no cast, deep shadows held open --ar 4:5 --style raw --stylize 100 --no hands, text, garnish sprigs
```

**KA**
```
აჭარული ხაჭაპური ღუმელიდან ახლად გამოღებული, ბათუმური რესტორნის სამზარეულოს დახლზე, ყვითელი მთლიანი და მბზინავი ყველის შუაგულში, გვერდით ნახევრად გამდნარი კარაქის ნაჭერი, მქრქალ შავ კერამიკულ თეფშზე, მუქი კაკლის მაგიდაზე, მარჯვენა ქვედა კუთხეში თეთრეულის ხელსახოცი და ჩანგლის წვერი შემოდის, სამმეოთხედი რაკურსი, კამერა თეფშზე 30 გრადუსით მაღლა, ნავის ფორმა დიაგონალზე მიდის ქვედა მარცხნიდან ზედა მარჯვნივ, მკვეთრი უკანა შუქი კამერიდან მარცხნივ, თეფშის უკნიდან, ორთქლსა და ქერქის ბზინვარე ქერქს გამოკვეთს, დიდი თეთრი ამრეკლი წინიდან ჩრდილებს იმდენად ხსნის, რომ ყველი იკითხებოდეს, რესტორნის მენიუს ფოტოგრაფია, 90 მმ მაკრო ობიექტივი, f/5.6, ფოკუსი ყვითელზე, ბუნებრივი ფერები ელფერის გარეშე, ღრმა ჩრდილები გახსნილი --ar 4:5 --style raw --stylize 100 --no hands, text, garnish sprigs
---
an adjarian khachapuri straight out of the oven on the pass of a Batumi restaurant, the yolk whole and glossy in the middle of the cheese, a knob of butter half melted beside it, on a matte black ceramic plate on a dark walnut table, a linen napkin and the tip of a fork entering the bottom right corner, three-quarter view from thirty degrees above the plate with the boat shape running diagonally from lower left to upper right, hard backlight from camera left behind the plate catching the steam and the blistered glaze on the crust, a large white bounce card at the front lifting the shadows just enough to read the cheese, restaurant menu photography, 90mm macro, f/5.6, focus on the yolk, natural colour with no cast, deep shadows held open --ar 4:5 --style raw --stylize 100 --no hands, text, garnish sprigs
```

---

### BP-07 · Founder and team portraits in one brand style
`midjourney` — portrait, about page, `--sref` plus a fixed seed is what holds a team page together

**EN**
```
the founder of a small ceramics studio, a woman in her forties in a plain indigo apron over a grey shirt, head and shoulders, turned three quarters to camera with her eyes on the lens, a pale plastered brick workshop wall two metres behind her and softly out of focus, large softbox forty-five degrees from camera left at head height as the key, silver reflector at camera right lifting the shadow side by two stops, one bare hair light behind camera right separating her shoulder from the wall, brand portrait photography, 85mm, f/2.8, camera at eye level, warm neutral grade, skin kept matte --ar 4:5 --style raw --stylize 100 --seed 1471 --sref https://your-approved-first-portrait.jpg --no hard shadows, busy background, corporate blue
→ consistency: shoot the founder first, approve one frame, upload it and use its URL as --sref for everyone else. Then for each colleague change only the first clause — "the ceramicist, a man in his twenties in the same indigo apron" — and leave the wall, the key-reflector-hair-light sentence, the 85mm f/2.8, the eye-level camera, the warm neutral grade, the seed and the --sref exactly as they are. Different lens or different key position and the team page reads as stock images from three different sources.
```

**KA**
```
პატარა კერამიკის სახელოსნოს დამფუძნებელი, ორმოცს გადაცილებული ქალი, უბრალო ინდიგოსფერ წინსაფარში ნაცრისფერ პერანგზე, პორტრეტი მხრებით, სამმეოთხედით კამერისკენ შემობრუნებული, მზერა ობიექტივში, ორ მეტრში უკან სახელოსნოს ღია ფერის შელესილი აგურის კედელი, რბილად გასული ფოკუსიდან, მთავარი შუქი — დიდი სოფტბოქსი კამერიდან მარცხნივ, 45 გრადუსზე, თავის სიმაღლეზე, ვერცხლისფერი ამრეკლი კამერიდან მარჯვნივ ჩრდილოვან მხარეს 2 საფეხურით ხსნის, ერთი შიშველი შუქი კამერის უკან, მარჯვნივ, მხარს კედლისგან აშორებს, ბრენდის პორტრეტული ფოტოგრაფია, 85 მმ ობიექტივი, f/2.8, კამერა თვალის დონეზე, თბილი ნეიტრალური ფერის დამუშავება, კანი მქრქალი --ar 4:5 --style raw --stylize 100 --seed 1471 --sref https://your-approved-first-portrait.jpg --no hard shadows, busy background, corporate blue
→ სერიისთვის: ჯერ დამფუძნებელი გადაიღე, აირჩიე ერთი კადრი, ატვირთე და მისი ბმული ყველა დანარჩენს --sref-ად მიეცი. შემდეგ თითოეულ კოლეგაზე მხოლოდ პირველი ფრაზა შეცვალე — „ოცდაათამდე კერამიკოსი კაცი იმავე ინდიგოსფერ წინსაფარში“ — კედელი, განათების წინადადება, 85 მმ f/2.8, კამერის სიმაღლე, ფერის დამუშავება, seed და --sref კი ხელუხლებელი დატოვე. სხვა ობიექტივი ან სხვა კუთხით დადგმული მთავარი შუქი და გუნდის გვერდი სამი სხვადასხვა წყაროდან აღებულ სტოკის სურათებად წაიკითხება.
---
the founder of a small ceramics studio, a woman in her forties in a plain indigo apron over a grey shirt, head and shoulders, turned three quarters to camera with her eyes on the lens, a pale plastered brick workshop wall two metres behind her and softly out of focus, large softbox forty-five degrees from camera left at head height as the key, silver reflector at camera right lifting the shadow side by two stops, one bare hair light behind camera right separating her shoulder from the wall, brand portrait photography, 85mm, f/2.8, camera at eye level, warm neutral grade, skin kept matte --ar 4:5 --style raw --stylize 100 --seed 1471 --sref https://your-approved-first-portrait.jpg --no hard shadows, busy background, corporate blue
```

---

### BP-08 · Social ad creative with the headline area reserved
`gpt-image` — social ad, respects a stated empty region instead of filling it

**EN**
```
A stack of three warm shotis puri loaves fresh out of the tone in a small Tbilisi bakery, lying low in the frame on a floured steel table, the blistered crust and the long split down the top loaf clearly visible. Behind them the mouth of the clay tone glows amber and the rest of the bakery falls into soft brown shadow. Warm low light at 3200K from camera right skims across the crust and picks out the flour dust, while a weak cool fill from a window at camera left keeps the shadows open. Vertical 4:5 frame for an Instagram feed post: the bread and the table occupy the bottom forty-five percent, and the top fifty-five percent is an even, unbroken field of dark out-of-focus bakery wall with no detail, no highlight and no texture, so a white headline and a price can be set over it and stay readable. Commercial food advertising photography, 50mm, f/2.8, the top loaf sharp, warm grade, deep shadows held open.
→ 4:5 is the feed. If the same creative also runs as a story, re-render at 9:16 and move the reserved field to the top sixty percent — cropping this one will cut the bread in half.
```

**KA**
```
3 თბილი შოთი თონიდან ახლად ამოღებული, პატარა თბილისურ საცხობში, ერთმანეთზე დაწყობილი კადრის ქვედა ნაწილში, ფქვილიან ლითონის მაგიდაზე, ქერქის ბუშტუკები და ზედა შოთის გრძელი ჭრილი კარგად ჩანს. მათ უკან თონის პირი ქარვისფრად ანათებს, დანარჩენი საცხობი რბილ მოყავისფრო ჩრდილშია. თბილი დაბალი შუქი 3200K კამერიდან მარჯვნივ ირიბად გადაუყვება ქერქს და ფქვილის მტვერს გამოკვეთს, სუსტი ცივი შუქი კი მარცხენა ფანჯრიდან ჩრდილებს ხსნის. ვერტიკალური 4:5 კადრი ინსტაგრამის ფიდისთვის: პური და მაგიდა ქვედა 45 პროცენტს იკავებს, ზედა 55 პროცენტი კი საცხობის ბნელი, ფოკუსგარეშე კედლის თანაბარი, უწყვეტი ველია — დეტალის, ბზინვარებისა და ფაქტურის გარეშე, რომ თეთრი სათაური და ფასი მასზე დაიდოს და იკითხებოდეს. კომერციული სარეკლამო კვების ფოტოგრაფია, 50 მმ ობიექტივი, f/2.8, ზედა შოთი მკვეთრი, თბილი ფერის დამუშავება, ღრმა ჩრდილები გახსნილი.
→ 4:5 ფიდისთვისაა. თუ იგივე კრეატივი სთორისაც გჭირდება, თავიდან გაარენდერე 9:16-ში და თავისუფალი ველი ზედა 60 პროცენტზე გადაიტანე — ამ კადრის ჩამოჭრა პურს შუაზე გაჭრის.
---
A stack of three warm shotis puri loaves fresh out of the tone in a small Tbilisi bakery, lying low in the frame on a floured steel table, the blistered crust and the long split down the top loaf clearly visible. Behind them the mouth of the clay tone glows amber and the rest of the bakery falls into soft brown shadow. Warm low light at 3200K from camera right skims across the crust and picks out the flour dust, while a weak cool fill from a window at camera left keeps the shadows open. Vertical 4:5 frame for an Instagram feed post: the bread and the table occupy the bottom forty-five percent, and the top fifty-five percent is an even, unbroken field of dark out-of-focus bakery wall with no detail, no highlight and no texture, so a white headline and a price can be set over it and stay readable. Commercial food advertising photography, 50mm, f/2.8, the top loaf sharp, warm grade, deep shadows held open.
```

---

### BP-09 · Website hero background
`flux` — web hero, keeps a clean left third and survives the responsive crop

**EN**
```
The stone and timber terrace of a small guesthouse above Stepantsminda at first light, two empty chairs and a low wooden table with a steaming cup at the right-hand edge of the terrace, the Sno valley and the snow face of Kazbegi filling the distance. The camera stands on the terrace at standing height looking out, the horizon on the lower third and the peak on the right. Cold blue shadow sits in the foreground timber while the first warm sun strikes only the snow and the top of the far ridge. The left forty percent of the frame is open sky and soft valley haze with no detail, held clear so a headline, a line of body text and a booking button can sit over it at any screen width. Wide 16:9 frame composed so that a centre 3:2 crop and a 1:1 crop both still hold the terrace and the peak. Travel and hospitality photography, 35mm, f/8, deep focus from the table to the ridge, natural colour with a cool to warm gradient running left to right across the frame.
```

**KA**
```
პატარა საოჯახო სასტუმროს ქვისა და ხის ტერასა სტეფანწმინდის ზემოთ, გათენებისას, ტერასის მარჯვენა კიდეზე 2 ცარიელი სკამი და დაბალი ხის მაგიდა, მაგიდაზე ორთქლიანი ჭიქა, სიღრმეში სნოს ხეობა და ყაზბეგის თოვლიანი კალთა. კამერა ტერასაზე დგას, ადამიანის სიმაღლეზე, გარეთ იყურება, ჰორიზონტი ქვედა მესამედზეა, მწვერვალი მარჯვნივ. წინა პლანის ხე ცივ ლურჯ ჩრდილშია, პირველი თბილი მზე მხოლოდ თოვლსა და შორეული ქედის თხემს ეხება. კადრის მარცხენა 40 პროცენტი ღია ცა და ხეობის ნაზი ნისლია, დეტალის გარეშე — თავისუფალი რჩება, რომ სათაური, ერთი წინადადება ტექსტი და ჯავშნის ღილაკი ეკრანის ნებისმიერ სიგანეზე დაიდოს. ფართო 16:9 კადრი ისეა აწყობილი, რომ ცენტრალური 3:2 და 1:1 ჩამოჭრაც ინარჩუნებს ტერასასაც და მწვერვალსაც. ტურიზმისა და სტუმართმასპინძლობის ფოტოგრაფია, 35 მმ ობიექტივი, f/8, ღრმა სიმკვეთრე მაგიდიდან ქედამდე, ბუნებრივი ფერები, ცივიდან თბილში გადასვლა მარცხნიდან მარჯვნივ.
---
The stone and timber terrace of a small guesthouse above Stepantsminda at first light, two empty chairs and a low wooden table with a steaming cup at the right-hand edge of the terrace, the Sno valley and the snow face of Kazbegi filling the distance. The camera stands on the terrace at standing height looking out, the horizon on the lower third and the peak on the right. Cold blue shadow sits in the foreground timber while the first warm sun strikes only the snow and the top of the far ridge. The left forty percent of the frame is open sky and soft valley haze with no detail, held clear so a headline, a line of body text and a booking button can sit over it at any screen width. Wide 16:9 frame composed so that a centre 3:2 crop and a 1:1 crop both still hold the terrace and the peak. Travel and hospitality photography, 35mm, f/8, deep focus from the table to the ridge, natural colour with a cool to warm gradient running left to right across the frame.
```

---

### BP-10 · Seamless brand pattern tile
`flux` — pattern, tileable, edge matching is a literal instruction it actually follows

**EN**
```
A seamless repeating tile for wrapping paper and packaging liners: a sparse scatter of hand-drawn grapevine tendrils, single vine leaves and small three-berry clusters, every motif drawn in one consistent thin ink line with no fill and no shading, set at two sizes on a forty-five degree offset repeat so that no motif touches or overlaps another. Deep aubergine line on a warm oatmeal ground, two flat colours only. The motifs run off all four edges and continue exactly where the opposite edge begins, so the tile repeats without a visible seam. Square 1:1 tile with the motifs covering roughly a fifth of the area, so the pattern still reads as light texture when it is scaled down to a 40mm label. Flat vector pattern design, even line weight throughout, drawn straight on with no perspective.
```

**KA**
```
უნაკერო, გამეორებადი ორნამენტის ფილა შესაფუთი ქაღალდისა და კოლოფის სარჩულისთვის: ხელით დახატული ვაზის ულვაშები, ცალკეული ვაზის ფოთლები და სამმარცვლიანი პატარა მტევნები, იშვიათად მიმოფანტული; ყველა მოტივი ერთი და იმავე სისქის თხელი ხაზითაა გავლებული, შევსებისა და ჩრდილის გარეშე, 2 ზომაში, 45 გრადუსით აცდენილ განმეორებაზე ისე, რომ არცერთი მოტივი მეორეს არ ეხება. მუქი ბადრიჯნისფერი ხაზი თბილ შვრიისფერ ფონზე, მხოლოდ 2 ბრტყელი ფერი. მოტივები ოთხივე კიდიდან გადადის და მოპირდაპირე კიდეზე ზუსტად იქიდან აგრძელებს, რომ ფილა ხილული ნაკერის გარეშე გამეორდეს. კვადრატული 1:1 ფილა, მოტივები ფართობის დაახლოებით მეხუთედს იკავებს — რომ ორნამენტი 40 მმ ეტიკეტზე შემცირებულიც მსუბუქ ფაქტურად იკითხებოდეს. ბრტყელი ვექტორული ორნამენტის დიზაინი, თანაბარი სისქის ხაზი, პირდაპირი ხედი, პერსპექტივის გარეშე.
---
A seamless repeating tile for wrapping paper and packaging liners: a sparse scatter of hand-drawn grapevine tendrils, single vine leaves and small three-berry clusters, every motif drawn in one consistent thin ink line with no fill and no shading, set at two sizes on a forty-five degree offset repeat so that no motif touches or overlaps another. Deep aubergine line on a warm oatmeal ground, two flat colours only. The motifs run off all four edges and continue exactly where the opposite edge begins, so the tile repeats without a visible seam. Square 1:1 tile with the motifs covering roughly a fifth of the area, so the pattern still reads as light texture when it is scaled down to a 40mm label. Flat vector pattern design, even line weight throughout, drawn straight on with no perspective.
```

---

### BP-11 · Three images that must read as one campaign
`midjourney` — campaign set, the shared block plus `--sref` and a fixed seed is the whole trick

**EN**
```
→ shared and identical in all three: late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg
→ render image 1 first, approve one frame, upload it, and use its URL as --sref in all three. Only the opening clause changes between them.

1) a bottle of amber qvevri wine standing on an unpainted plaster ledge beside a half-full stemless glass, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

2) a winemaker's hands lifting the clay lid off a qvevri, forearms and the lid only, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

3) amber wine falling from a clay jug into a stemless glass on an unpainted plaster ledge, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props
```

**KA**
```
→ სამივესთვის საერთო და უცვლელი: გვიანი შუადღის გვერდითი შუქი კამერიდან მარცხნივ, მტვრიანი ფანჯრიდან, ერთი თეთრი ამრეკლი კამერიდან მარჯვნივ, თბილი ქარვისფერი და ზეთისხილისფერი შეულესავ ბათქაშზე, 85 მმ ობიექტივი, f/2.8, თბილი ნეიტრალური ფერის დამუშავება --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg
→ ჯერ პირველი კადრი გაარენდერე, აირჩიე ერთი, ატვირთე და მისი ბმული სამივეს --sref-ად მიეცი. ერთმანეთისგან მხოლოდ პირველი ფრაზით განსხვავდებიან.

1) ქარვისფერი ქვევრის ღვინის ბოთლი შეულესავი ბათქაშის თაროზე, გვერდით ნახევრად სავსე ფეხის გარეშე ჭიქა, გვიანი შუადღის გვერდითი შუქი კამერიდან მარცხნივ, მტვრიანი ფანჯრიდან, ერთი თეთრი ამრეკლი კამერიდან მარჯვნივ, თბილი ქარვისფერი და ზეთისხილისფერი შეულესავ ბათქაშზე, 85 მმ ობიექტივი, f/2.8, თბილი ნეიტრალური ფერის დამუშავება --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

2) მეღვინის ხელები ქვევრს თიხის სარქველს ხდის, კადრში მხოლოდ წინამხრები და სარქველი, გვიანი შუადღის გვერდითი შუქი კამერიდან მარცხნივ, მტვრიანი ფანჯრიდან, ერთი თეთრი ამრეკლი კამერიდან მარჯვნივ, თბილი ქარვისფერი და ზეთისხილისფერი შეულესავ ბათქაშზე, 85 მმ ობიექტივი, f/2.8, თბილი ნეიტრალური ფერის დამუშავება --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

3) ქარვისფერი ღვინო თიხის დოქიდან ფეხის გარეშე ჭიქაში ჩამოდის, შეულესავი ბათქაშის თაროზე, გვიანი შუადღის გვერდითი შუქი კამერიდან მარცხნივ, მტვრიანი ფანჯრიდან, ერთი თეთრი ამრეკლი კამერიდან მარჯვნივ, თბილი ქარვისფერი და ზეთისხილისფერი შეულესავ ბათქაშზე, 85 მმ ობიექტივი, f/2.8, თბილი ნეიტრალური ფერის დამუშავება --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props
---
1) a bottle of amber qvevri wine standing on an unpainted plaster ledge beside a half-full stemless glass, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

2) a winemaker's hands lifting the clay lid off a qvevri, forearms and the lid only, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props

3) amber wine falling from a clay jug into a stemless glass on an unpainted plaster ledge, late afternoon side light from camera left through a dusty window, one white bounce at camera right, warm amber and olive green against unpainted plaster, 85mm, f/2.8, warm neutral grade --ar 4:5 --style raw --stylize 100 --seed 2204 --sref https://your-approved-key-image.jpg --no text, props
```
