# Nano Banana 2

Nano Banana 2 (Google's Gemini image model) reads a **creative director's brief**, not a tag list.
Write full sentences in this order: subject, composition, action, location, style, editing instruction.
Midjourney-style comma strings of descriptors underperform here — they give the model nothing to reason about.
Text rendering is a strength: it spells reliably and can translate text that already sits inside a picture.
Native 512px to 4K, 14 aspect ratios including 21:9, 9:16, 1:8 and 8:1.
**Consistency** holds for about 5 characters and 14 objects in one workflow, with up to 14 reference images —
and it comes from two things: a reference sheet, and the *identical physical description repeated verbatim*
in every prompt that uses that character, plus one sentence saying how the new light falls on them.
**Editing** works by semantic masking (name what changes, name what must stay exactly the same) and by
short successive turns — not one enormous prompt. The model is fast and cheap, so three turns are the
intended workflow, not a fallback.

Nano Banana 2 კრეატიული დირექტორის ბრიფს კითხულობს და არა თეგების სიას: დაწერე სრული წინადადებები —
ობიექტი, კომპოზიცია, მოქმედება, ადგილი, სტილი და, თუ არედაქტირებ, ზუსტად რა იცვლება.
Midjourney-ს მძიმეებიანი სტრიქონი აქ სუსტ შედეგს იძლევა.
ქართული ბლოკი სამუშაო ვერსიაა — ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული ინგლისური სტრიქონი.
პერსონაჟის იგივეობა ერთ სამუშაოში 5 პერსონაჟსა და 14 ობიექტს უძლებს; მექანიზმი ასეთია — ჯერ რეფერენსული
ფურცელი, მერე კი ერთი და იმავე გარეგნობის აღწერა სიტყვასიტყვით გადატანილი ყოველ შემდეგ პრომპტში,
პლუს ერთი წინადადება იმაზე, როგორ ეცემა ახალ სცენაში სინათლე.
რედაქტირება სემანტიკური მასკით მუშაობს: დაასახელე ის, რაც იცვლება, და ცალკე დაასახელე ის, რაც უცვლელი
რჩება; ერთი გიგანტური პრომპტის ნაცვლად იმუშავე რამდენიმე მოკლე ეტაპად — მოდელი სწრაფი და იაფია.
ქართული დამწერლობა: გენერირებულ სურათში ქართული ასოები თითქმის ყოველთვის შესასწორებელი გამოვა.
საიმედო გზაა, სთხოვო მოდელს, წარწერის ადგილი ცარიელი დატოვოს და ქართული შრიფტი შენ დაადო.

---

### NB-01 · Creative-director brief — winemaker portrait
`nano-banana` `gemini` — portrait, brief

**EN**
```
Photograph a winemaker in his sixties inside his own marani in Kakheti, and treat this brief the
way a creative director would hand it to a photographer.

Subject: the man stands behind the clay lip of a buried qvevri, both palms resting flat on the stone
slab that covers it. He has a short grey beard, deep vertical lines between the eyebrows, wind-burnt
skin and heavy hands with dirt still in the knuckle creases. He wears a faded navy work shirt with
the sleeves rolled above the elbow.

Composition: 4:5 vertical, waist-up, the figure slightly right of centre, the qvevri mouth cutting
across the bottom edge of the frame. Camera at chest height, straight on, 85mm equivalent, shallow
depth of field so the vaulted stone ceiling behind him falls soft.

Action: he has just looked up from the qvevri — chin lifted, eyes to camera, mouth closed, no smile.

Location: a whitewashed vaulted cellar, one small window high on the left wall, clay dust in the air.

Light: a single hard shaft of daylight enters from camera left and rakes across his left cheek and
the back of his hands; the right side of his face falls two stops darker; the far wall is unlit and
sinks toward black.

Style: editorial documentary portrait, natural colour, warm ochre and grey palette, fine film grain,
no retouching of skin texture.
```

**KA**
```
გადაიღე სამოცს გადაცილებული მეღვინის პორტრეტი კახეთში, საკუთარ მარანში. ეს ბრიფია — ისე დაწერილი,
როგორც კრეატიული დირექტორი გადასცემდა ფოტოგრაფს.

ობიექტი: კაცი მიწაში ჩაფლული ქვევრის უკან დგას, ორივე ხელისგული ქვევრის თავზე დადებულ ქვის ფილაზე
აქვს დადებული. მოკლე ჭაღარა წვერი, წარბებს შორის ღრმა ვერტიკალური ნაოჭები, ქარისგან დაზიანებული
კანი და მძიმე ხელები, რომელთა თითების ნაკეცებში მიწა შერჩენილია. აცვია გახუნებული მუქი ლურჯი
სამუშაო პერანგი, სახელოები იდაყვზე მაღლა აწეული.

კომპოზიცია: ვერტიკალური კადრი 4:5, პორტრეტი წელზევით, ფიგურა ცენტრიდან ოდნავ მარჯვნივ, ქვევრის
ყელი კადრის ქვედა კიდეს კვეთს. კამერა მკერდის სიმაღლეზე, პირდაპირ, 85 მმ ექვივალენტი, მცირე
სიღრმის ველი — უკან ქვის თაღოვანი ჭერი რბილად იბუნდოვნება.

მოქმედება: ახლახან ქვევრიდან აიხედა — ნიკაპი ოდნავ აწეული, მზერა კამერაში, პირი დახურული, ღიმილის
გარეშე.

ადგილი: მოთეთრებული, თაღოვანი მარანი, მარცხენა კედელზე მაღლა ერთი პატარა ფანჯარა, ჰაერში თიხის მტვერი.

განათება: ერთი მკვეთრი დღის სხივი შემოდის კამერიდან მარცხნივ და ირიბად ეცემა მარცხენა ლოყასა და
ხელის ზურგს; სახის მარჯვენა მხარე ორი საფეხურით მუქია; შორეული კედელი განათების გარეშე რჩება და
შავში გადადის.

სტილი: სარედაქციო დოკუმენტური პორტრეტი, ბუნებრივი ფერი, თბილი ოხრისა და ნაცრისფერის პალიტრა,
წვრილი ფოტოფირის მარცვალი, კანის ფაქტურა შეუსწორებელი.
---
Photograph a winemaker in his sixties inside his own marani in Kakheti, and treat this brief the way
a creative director would hand it to a photographer.
Subject: the man stands behind the clay lip of a buried qvevri, both palms resting flat on the stone
slab that covers it. Short grey beard, deep vertical lines between the eyebrows, wind-burnt skin,
heavy hands with dirt still in the knuckle creases, a faded navy work shirt with sleeves rolled above
the elbow.
Composition: 4:5 vertical, waist-up, the figure slightly right of centre, the qvevri mouth cutting
across the bottom edge. Camera at chest height, straight on, 85mm equivalent, shallow depth of field
so the vaulted stone ceiling behind him falls soft.
Action: he has just looked up from the qvevri — chin lifted, eyes to camera, mouth closed, no smile.
Location: a whitewashed vaulted cellar, one small window high on the left wall, clay dust in the air.
Light: a single hard shaft of daylight from camera left rakes across his left cheek and the back of
his hands; the right side of his face falls two stops darker; the far wall is unlit and sinks to black.
Style: editorial documentary portrait, natural colour, warm ochre and grey palette, fine film grain,
no retouching of skin texture.
```

---

### NB-02 · Character reference sheet built for reuse
`nano-banana` `gemini` — consistency, reference sheet

**EN**
```
Build a character reference sheet I will reuse across later prompts. 16:9, one sheet, flat even
studio light with no dramatic shadows, plain light grey seamless background, no props, no text.

The character, described exactly as follows — treat every detail as binding:
"Nino, a woman in her early thirties, 172 cm, slim build; straight dark brown hair cut just above
the shoulders with a centre parting; dark brown eyes, thick unshaped eyebrows, a small mole below
the left cheekbone; olive skin; a heavy indigo denim apron worn over a plain white cotton t-shirt
with the sleeves rolled to the elbow; a thin silver ring on the right index finger."

Lay the sheet out as five figures on one horizontal baseline, evenly spaced, all at the same scale
and the same height in frame, all lit identically:
1. full-length front view, arms relaxed at her sides
2. full-length three-quarter view turned to her left
3. full-length profile, facing right
4. full-length back view, showing the apron ties
5. head and shoulders only, front on, neutral expression

Camera at chest height for the full-length figures, eye level for the head-and-shoulders crop.
Keep the face, the hair length, the apron colour and the ring identical in all five figures. Neutral
expression throughout, no stylisation, photographic realism, natural skin texture.
```

**KA**
```
შექმენი პერსონაჟის რეფერენსული ფურცელი, რომელსაც შემდეგ პრომპტებში გამოვიყენებ. 16:9, ერთი
ფურცელი, თანაბარი სტუდიური განათება მკვეთრი ჩრდილების გარეშე, ღია ნაცრისფერი უწყვეტი ფონი,
რეკვიზიტისა და წარწერის გარეშე.

პერსონაჟი, ზუსტად ასე აღწერილი — ყოველი დეტალი სავალდებულოა:
„ნინო, ოცდაათს ახლად გადაცილებული ქალი, სიმაღლე 172 სმ, გამხდარი აღნაგობა; სწორი მუქი წაბლისფერი
თმა, მხრებზე ოდნავ მაღლა შეჭრილი, შუაზე გაყოფილი; მუქი ყავისფერი თვალები, სქელი, დაუმუშავებელი
წარბები, მარცხენა ლოყის ძვლის ქვემოთ პატარა ხალი; ზეთისხილისფერი კანი; ინდიგოსფერი მკვრივი ჯინსის წინსაფარი
უბრალო თეთრ ბამბის მაისურზე, სახელოები იდაყვამდე აწეული; მარჯვენა საჩვენებელ თითზე თხელი
ვერცხლის ბეჭედი.“

ფურცელი ასე დაალაგე — ერთ ჰორიზონტალურ ხაზზე 5 ფიგურა, თანაბარი მანძილით, ერთი მასშტაბით, კადრში
ერთსა და იმავე სიმაღლეზე, ერთნაირად განათებული:
1. სრული ტანი, წინხედი, ხელები თავისუფლად ჩამოშვებული
2. სრული ტანი, სამი მეოთხედი, მარცხნივ შემობრუნებული
3. სრული ტანი, პროფილი, სახით მარჯვნივ
4. სრული ტანი, ზურგიდან — ჩანს წინსაფრის ზონრები
5. მხოლოდ თავი და მხრები, წინხედი, ნეიტრალური გამომეტყველება

კამერა სრული ტანის ფიგურებისთვის მკერდის სიმაღლეზეა, თავისა და მხრების კადრისთვის — თვალის დონეზე.
სახე, თმის სიგრძე, წინსაფრის ფერი და ბეჭედი ხუთივე ფიგურაზე იდენტური რჩება. ნეიტრალური
გამომეტყველება, სტილიზაციის გარეშე, ფოტოგრაფიული რეალიზმი, კანის ბუნებრივი ფაქტურა.
---
Build a character reference sheet I will reuse across later prompts. 16:9, one sheet, flat even studio
light with no dramatic shadows, plain light grey seamless background, no props, no text.
The character, described exactly as follows — treat every detail as binding:
"Nino, a woman in her early thirties, 172 cm, slim build; straight dark brown hair cut just above the
shoulders with a centre parting; dark brown eyes, thick unshaped eyebrows, a small mole below the left
cheekbone; olive skin; a heavy indigo denim apron worn over a plain white cotton t-shirt with the
sleeves rolled to the elbow; a thin silver ring on the right index finger."
Lay the sheet out as five figures on one horizontal baseline, evenly spaced, all at the same scale and
the same height in frame, all lit identically: 1. full-length front view, arms relaxed at her sides;
2. full-length three-quarter view turned to her left; 3. full-length profile, facing right; 4.
full-length back view, showing the apron ties; 5. head and shoulders only, front on, neutral expression.
Camera at chest height for the full-length figures, eye level for the head-and-shoulders crop. Keep the
face, the hair length, the apron colour and the ring identical in all five figures. Neutral expression
throughout, no stylisation, photographic realism, natural skin texture.
```

---

### NB-03 · The same character in a second scene — verbatim carry-over
`nano-banana` `gemini` — consistency, scene

**EN**
```
Use the attached reference sheet as the binding likeness for the character in this scene.

The character, described exactly as in the reference sheet — this description is repeated word for
word on purpose and must not be paraphrased:
"Nino, a woman in her early thirties, 172 cm, slim build; straight dark brown hair cut just above
the shoulders with a centre parting; dark brown eyes, thick unshaped eyebrows, a small mole below
the left cheekbone; olive skin; a heavy indigo denim apron worn over a plain white cotton t-shirt
with the sleeves rolled to the elbow; a thin silver ring on the right index finger."

Scene: she is behind the counter of a small specialty coffee bar in Vera, Tbilisi, tamping a dose
of coffee into a portafilter, head slightly down, eyes on her hands, weight on her left foot.

Composition: 3:2 horizontal, medium shot cut at the hips, Nino on the left third, the espresso
machine's chrome flank filling the right third, the counter edge running along the bottom of the
frame. Camera at counter height, 50mm equivalent, f/2.8 so the room behind her softens.

How the new light changes her, relative to the flat studio light of the reference sheet: a single
large window is out of frame to camera right, so the light now comes from her left side — a soft
highlight along her left cheekbone and the left edge of the apron, the right side of her face one
stop down, warm bounce from the wooden counter under her chin, and a cool reflection of the window
sliding down the chrome behind her. The hair, the mole, the apron and the ring stay exactly as
described.

Style: natural-light documentary photography, muted warm palette, no colour grading tricks.
```

**KA**
```
მიმაგრებული რეფერენსული ფურცელი ამ სცენაში პერსონაჟის სავალდებულო გარეგნობაა.

პერსონაჟი, ზუსტად ისე აღწერილი, როგორც რეფერენსზე — აღწერა შეგნებულად სიტყვასიტყვით მეორდება და
გადაკეთებას არ ექვემდებარება:
„ნინო, ოცდაათს ახლად გადაცილებული ქალი, სიმაღლე 172 სმ, გამხდარი აღნაგობა; სწორი მუქი წაბლისფერი
თმა, მხრებზე ოდნავ მაღლა შეჭრილი, შუაზე გაყოფილი; მუქი ყავისფერი თვალები, სქელი, დაუმუშავებელი
წარბები, მარცხენა ლოყის ძვლის ქვემოთ პატარა ხალი; ზეთისხილისფერი კანი; ინდიგოსფერი მკვრივი ჯინსის წინსაფარი
უბრალო თეთრ ბამბის მაისურზე, სახელოები იდაყვამდე აწეული; მარჯვენა საჩვენებელ თითზე თხელი
ვერცხლის ბეჭედი.“

სცენა: ნინო თბილისში, ვერაზე, პატარა სპეშელთი ყავის ბარის დახლს უკან დგას და პორტაფილტრში ყავას
ტკეპნის; თავი ოდნავ დახრილი, მზერა ხელებზე, წონა მარცხენა ფეხზე.

კომპოზიცია: ჰორიზონტალური კადრი 3:2, საშუალო ხედი თეძოებამდე, ნინო მარცხენა მესამედში, ყავის
აპარატის ქრომირებული გვერდი მარჯვენა მესამედს ავსებს, დახლის კიდე კადრის ქვედა ხაზზე გადის.
კამერა დახლის სიმაღლეზე, 50 მმ ექვივალენტი, f/2.8 — უკანა სივრცე რბილდება.

როგორ იცვლება მისი განათება რეფერენსის თანაბარ სტუდიურ შუქთან შედარებით: კადრს გარეთ, კამერიდან
მარჯვნივ, ერთი დიდი ფანჯარაა, ამიტომ შუქი ახლა მისი მარცხენა მხრიდან მოდის — რბილი ბზინვა მარცხენა
ლოყის ძვალსა და წინსაფრის მარცხენა კიდეზე, სახის მარჯვენა მხარე ერთი საფეხურით მუქი, ხის დახლიდან
თბილი არეკვლა ნიკაპის ქვეშ და ფანჯრის ცივი ანარეკლი უკან, ქრომზე ჩამოცურებული. თმა, ხალი,
წინსაფარი და ბეჭედი ზუსტად ისე რჩება, როგორც აღწერილია.

სტილი: ბუნებრივ შუქზე გადაღებული დოკუმენტური ფოტო, დაწყნარებული თბილი პალიტრა, ფერის ხელოვნური
დამუშავების გარეშე.
---
Use the attached reference sheet as the binding likeness for the character in this scene.
The character, described exactly as in the reference sheet — this description is repeated word for word
on purpose and must not be paraphrased:
"Nino, a woman in her early thirties, 172 cm, slim build; straight dark brown hair cut just above the
shoulders with a centre parting; dark brown eyes, thick unshaped eyebrows, a small mole below the left
cheekbone; olive skin; a heavy indigo denim apron worn over a plain white cotton t-shirt with the
sleeves rolled to the elbow; a thin silver ring on the right index finger."
Scene: she is behind the counter of a small specialty coffee bar in Vera, Tbilisi, tamping a dose of
coffee into a portafilter, head slightly down, eyes on her hands, weight on her left foot.
Composition: 3:2 horizontal, medium shot cut at the hips, Nino on the left third, the espresso machine's
chrome flank filling the right third, the counter edge running along the bottom of the frame. Camera at
counter height, 50mm equivalent, f/2.8 so the room behind her softens.
How the new light changes her, relative to the flat studio light of the reference sheet: a single large
window is out of frame to camera right, so the light now comes from her left side — a soft highlight
along her left cheekbone and the left edge of the apron, the right side of her face one stop down, warm
bounce from the wooden counter under her chin, and a cool reflection of the window sliding down the
chrome behind her. The hair, the mole, the apron and the ring stay exactly as described.
Style: natural-light documentary photography, muted warm palette, no colour grading tricks.
```

---

### NB-04 · Multi-reference composite — product, model, location
`nano-banana` `gemini` — composite, references

**EN**
```
You have three reference images. Use each one for one thing only, and say nothing of your own into
the others.

Reference 1 — the product: a Saperavi wine bottle with a cream uncoated paper label. Take the bottle
shape, the glass colour, the label artwork and every character printed on it exactly as they are.
Do not redraw, re-letter, re-space or re-colour the label. Its proportions relative to a human hand
must stay believable.

Reference 2 — the model: take the woman's face, hair, build and hands from this image only. Her
clothing changes to a plain charcoal linen shirt with the sleeves rolled to the elbow.

Reference 3 — the location: take the room from this image only — the dark oiled wood counter, the
white plaster wall, the row of small windows on the left.

Composite: 4:5 vertical, the model standing behind the counter on the right third of the frame,
turned three-quarters toward camera, holding the bottle upright at chest height with her right hand
around its shoulder and the label facing camera, unobstructed by her fingers. The counter runs
across the lower quarter of the frame. Camera at chest height, 50mm equivalent, f/4 so both the
label and her face stay sharp.

Light: the windows on the left are the only source — soft directional daylight across the label from
camera left, a gentle falloff into the right side of the room, one soft specular band down the left
shoulder of the glass, and a short soft contact shadow to the right of the bottle's base.

Style: commercial lifestyle photography, natural colour, nothing overlit.
```

**KA**
```
გაქვს 3 რეფერენსი. თითოეული მხოლოდ ერთი რამისთვის გამოიყენე და ერთმანეთში არაფერი აურიო.

რეფერენსი 1 — პროდუქტი: საფერავის ბოთლი კრემისფერი, დაუფარავი ქაღალდის ეტიკეტით. აიღე ბოთლის
ფორმა, მინის ფერი, ეტიკეტის გრაფიკა და მასზე დაბეჭდილი ყოველი სიმბოლო ზუსტად ისე, როგორც არის.
ეტიკეტი ხელახლა არ დახატო, ასოები არ გადააწერო, ინტერვალი და ფერი არ შეცვალო. ბოთლის პროპორცია
ადამიანის ხელთან შედარებით დამაჯერებელი უნდა დარჩეს.

რეფერენსი 2 — მოდელი: ქალის სახე, თმა, აღნაგობა და ხელები მხოლოდ ამ სურათიდან აიღე. ტანსაცმელი
იცვლება — მუქი ნაცრისფერი, უბრალო სელის პერანგი, სახელოები იდაყვამდე აწეული.

რეფერენსი 3 — ადგილი: ინტერიერი მხოლოდ ამ სურათიდან აიღე — მუქი, ზეთით დამუშავებული ხის დახლი,
თეთრი ბათქაშის კედელი, მარცხნივ პატარა ფანჯრების რიგი.

მონტაჟი: ვერტიკალური კადრი 4:5, მოდელი დახლს უკან დგას, კადრის მარჯვენა მესამედში, სამი მეოთხედით
კამერისკენ შებრუნებული; ბოთლს მკერდის სიმაღლეზე, ვერტიკალურად უჭირავს მარჯვენა ხელით, თითები
ბოთლის მხარზეა და ეტიკეტს არ ფარავს — ეტიკეტი კამერისკენ იყურება. დახლი კადრის ქვედა მეოთხედს
კვეთს. კამერა მკერდის სიმაღლეზე, 50 მმ ექვივალენტი, f/4 — ეტიკეტიც და სახეც მკვეთრი რჩება.

განათება: ერთადერთი წყარო მარცხენა ფანჯრებია — რბილი, მიმართული დღის შუქი ეტიკეტზე კამერიდან
მარცხნივ, ოთახის მარჯვენა მხარეს ნელი ჩაბნელება, მინის მარცხენა მხარზე ერთი რბილი შუქის ზოლი და
ბოთლის ძირიდან მარჯვნივ მოკლე, რბილი ჩრდილი.

სტილი: კომერციული ლაიფსტაილ ფოტოგრაფია, ბუნებრივი ფერი, გადანათების გარეშე.
---
You have three reference images. Use each one for one thing only, and say nothing of your own into the
others.
Reference 1 — the product: a Saperavi wine bottle with a cream uncoated paper label. Take the bottle
shape, the glass colour, the label artwork and every character printed on it exactly as they are. Do not
redraw, re-letter, re-space or re-colour the label. Its proportions relative to a human hand must stay
believable.
Reference 2 — the model: take the woman's face, hair, build and hands from this image only. Her clothing
changes to a plain charcoal linen shirt with the sleeves rolled to the elbow.
Reference 3 — the location: take the room from this image only — the dark oiled wood counter, the white
plaster wall, the row of small windows on the left.
Composite: 4:5 vertical, the model standing behind the counter on the right third of the frame, turned
three-quarters toward camera, holding the bottle upright at chest height with her right hand around its
shoulder and the label facing camera, unobstructed by her fingers. The counter runs across the lower
quarter of the frame. Camera at chest height, 50mm equivalent, f/4 so both the label and her face stay
sharp.
Light: the windows on the left are the only source — soft directional daylight across the label from
camera left, a gentle falloff into the right side of the room, one soft specular band down the left
shoulder of the glass, and a short soft contact shadow to the right of the bottle's base.
Style: commercial lifestyle photography, natural colour, nothing overlit.
```

---

### NB-05 · Semantic mask — change one element, freeze the rest
`nano-banana` `gemini` — editing, semantic mask

**EN**
```
Edit the attached photograph of the Tbilisi café interior. Keep the same 3:2 frame.

Change exactly one element: the four bentwood chairs around the window table become simple square
oak stools with no backrest, the same seat height, standing in the same four positions on the floor,
casting shadows that fall in the same direction and at the same length as the shadows the chairs
cast now.

Everything else stays identical and must not be regenerated: the marble table top and its position,
the white plaster wall and its hairline cracks, the row of windows and the view through them, the
brass pendant lamp, the terrazzo floor pattern, the two plants on the sill, the counter in the
background, the camera position, the focal length, the depth of field, the crop, the grain and the
colour temperature. The light still comes from the windows on the left at the same angle and the
same softness.

Do not relight the room, do not tidy it, do not add or remove any other object. If a part of the
floor was hidden behind a chair, fill it with the same terrazzo pattern that surrounds it.
```

**KA**
```
შეასწორე მიმაგრებული ფოტო — თბილისური კაფეს ინტერიერი. კადრის პროპორცია იგივე რჩება, 3:2.

შეცვალე ზუსტად ერთი ელემენტი: ფანჯარასთან მდგარი მაგიდის გარშემო ოთხი მოხრილი ხის სკამი გადაიქცევა
მუხის მარტივ, კვადრატულ, ზურგსაყრდენის გარეშე სკამად — იმავე სიმაღლის ჯდომის ზედაპირით, იატაკზე
იმავე ოთხ ადგილას; ჩრდილები იმავე მიმართულებით და იმავე სიგრძით ეცემა, როგორც ახლა ეცემა სკამებს.

დანარჩენი ყველაფერი უცვლელი რჩება და ხელახლა არ გენერირდება: მარმარილოს მაგიდის ზედაპირი და მისი
ადგილი, თეთრი ბათქაშის კედელი თავისი თხელი ბზარებით, ფანჯრების რიგი და მათში გამოსახული ხედი,
სპილენძის ჭერის სანათი, ტერაცოს იატაკის ნახატი, რაფაზე მდგარი 2 მცენარე, ფონზე დახლი, კამერის
ადგილი, ფოკუსური მანძილი, სიღრმის ველი, კადრირება, ფაქტურა და ფერის ტემპერატურა. შუქი ისევ
მარცხენა ფანჯრებიდან მოდის, იმავე კუთხით და იმავე სირბილით.

ოთახი ხელახლა არ გაანათო, არ მოალამაზო, სხვა არცერთი საგანი არ დაამატო და არ ამოიღო. თუ იატაკის
რომელიმე ნაწილი სკამს ჰქონდა ამოფარებული, შეავსე იმავე ტერაცოს ნახატით, რომელიც მის გარშემოა.
---
Edit the attached photograph of the Tbilisi café interior. Keep the same 3:2 frame.
Change exactly one element: the four bentwood chairs around the window table become simple square oak
stools with no backrest, the same seat height, standing in the same four positions on the floor, casting
shadows that fall in the same direction and at the same length as the shadows the chairs cast now.
Everything else stays identical and must not be regenerated: the marble table top and its position, the
white plaster wall and its hairline cracks, the row of windows and the view through them, the brass
pendant lamp, the terrazzo floor pattern, the two plants on the sill, the counter in the background, the
camera position, the focal length, the depth of field, the crop, the grain and the colour temperature.
The light still comes from the windows on the left at the same angle and the same softness.
Do not relight the room, do not tidy it, do not add or remove any other object. If a part of the floor
was hidden behind a chair, fill it with the same terrazzo pattern that surrounds it.
```

---

### NB-06 · Three-turn refinement chain
`nano-banana` `gemini` — multi-turn, workflow

**EN**
```
Run this as three separate turns in one conversation. Send turn 1, look at the result, then send
turn 2 against that image, then turn 3. Do not merge them into one prompt.

TURN 1 — establish the scene
Photograph the interior of a small café on a corner in Sololaki, Tbilisi, 3:2 horizontal, late
afternoon. A dark oiled wood counter runs from the lower left corner diagonally into the middle
right of the frame. Behind it a white plaster wall with visible hairline cracks and one arched
doorway. Three tall windows fill the left wall. Camera at standing eye level, 35mm equivalent, f/4,
one point of view, no people. Warm natural light from the left, soft, no hard shadows. Natural
colour, documentary interior photography.

TURN 2 — fix the light and the depth
Keep the room, the camera position, the focal length, the crop and every object exactly as they are.
Change only the light: push the time to the last half hour before sunset, so a low warm beam enters
through the left windows, lands across the counter top and throws three long window-shaped patches
onto the floor, angled toward the lower right. Deepen the shadow in the arched doorway. Everything
else stays identical.

TURN 3 — add one element and nothing more
Keep everything from the previous image unchanged — the same light, the same beams on the floor, the
same counter, wall, doorway, windows, camera and crop. Add one thing only: a single brass pendant
lamp hanging above the middle of the counter, its shade about the width of two hands, switched on,
casting a small warm pool on the counter top directly below it and a soft round shadow beside it.
The lamp must not change the daylight already in the room.
```

**KA**
```
ეს 3 ცალკე ეტაპია ერთ საუბარში. გაგზავნე პირველი, ნახე შედეგი, მერე მიაყოლე მეორე იმავე სურათზე,
შემდეგ მესამე. ერთ პრომპტად არ გააერთიანო.

ეტაპი 1 — სცენის დადგმა
გადაიღე პატარა კაფეს ინტერიერი თბილისში, სოლოლაკის კუთხეში; ჰორიზონტალური კადრი 3:2, შუადღის
მიწურული. მუქი, ზეთით დამუშავებული ხის დახლი ქვედა მარცხენა კუთხიდან დიაგონალზე მიდის კადრის
მარჯვენა შუამდე. მის უკან თეთრი ბათქაშის კედელი, თხელი ბზარებით, და ერთი თაღოვანი კარი. მარცხენა
კედელს 3 მაღალი ფანჯარა ავსებს. კამერა მდგომი ადამიანის თვალის დონეზე, 35 მმ ექვივალენტი, f/4,
ერთი ხედი, ადამიანების გარეშე. თბილი ბუნებრივი შუქი მარცხნიდან, რბილი, მკვეთრი ჩრდილების გარეშე.
ბუნებრივი ფერი, დოკუმენტური ინტერიერის ფოტოგრაფია.

ეტაპი 2 — შუქისა და სიღრმის გასწორება
ოთახი, კამერის ადგილი, ფოკუსური მანძილი, კადრირება და ყოველი საგანი უცვლელი დატოვე. შეცვალე
მხოლოდ განათება: დროს გადაიტანე მზის ჩასვლამდე ბოლო ნახევარ საათზე — დაბალი, თბილი სხივი შემოდის
მარცხენა ფანჯრებიდან, ეცემა დახლის ზედაპირს და იატაკზე აგდებს 3 გრძელ, ფანჯრის ფორმის ლაქას,
მარჯვნივ-ქვემოთ დახრილს. თაღოვან კარში ჩრდილი უფრო ღრმა გახადე. დანარჩენი ყველაფერი იდენტური რჩება.

ეტაპი 3 — დაამატე ერთი ელემენტი და მეტი არაფერი
წინა სურათიდან ყველაფერი უცვლელი რჩება — იგივე შუქი, იგივე ლაქები იატაკზე, იგივე დახლი, კედელი,
კარი, ფანჯრები, კამერა და კადრირება. დაამატე მხოლოდ ერთი რამ: სპილენძის ერთი ჭერის სანათი დახლის
შუა ნაწილის თავზე, აბაჟურის სიგანე დაახლოებით ორი ხელისგულის ტოლი, ჩართული — პირდაპირ მის ქვეშ
დახლზე პატარა თბილი შუქის ლაქა და გვერდით რბილი, მრგვალი ჩრდილი. სანათი ოთახში უკვე არსებულ დღის
შუქს არ ცვლის.
---
Run this as three separate turns in one conversation. Send turn 1, look at the result, then send turn 2
against that image, then turn 3. Do not merge them into one prompt.
TURN 1 — establish the scene. Photograph the interior of a small café on a corner in Sololaki, Tbilisi,
3:2 horizontal, late afternoon. A dark oiled wood counter runs from the lower left corner diagonally into
the middle right of the frame. Behind it a white plaster wall with visible hairline cracks and one arched
doorway. Three tall windows fill the left wall. Camera at standing eye level, 35mm equivalent, f/4, one
point of view, no people. Warm natural light from the left, soft, no hard shadows. Natural colour,
documentary interior photography.
TURN 2 — fix the light and the depth. Keep the room, the camera position, the focal length, the crop and
every object exactly as they are. Change only the light: push the time to the last half hour before
sunset, so a low warm beam enters through the left windows, lands across the counter top and throws three
long window-shaped patches onto the floor, angled toward the lower right. Deepen the shadow in the arched
doorway. Everything else stays identical.
TURN 3 — add one element and nothing more. Keep everything from the previous image unchanged — the same
light, the same beams on the floor, the same counter, wall, doorway, windows, camera and crop. Add one
thing only: a single brass pendant lamp hanging above the middle of the counter, its shade about the
width of two hands, switched on, casting a small warm pool on the counter top directly below it and a
soft round shadow beside it. The lamp must not change the daylight already in the room.
```

---

### NB-07 · Poster with exact typography
`nano-banana` `gemini` — poster, typography

**EN**
```
Design a concert poster, 2:3 vertical, printed as a three-colour screen print on uncoated stock with
a visible paper tooth. Palette: deep plum ground, warm cream type, one burnt-orange accent.

Image: a double bass photographed from a low angle against the plum ground, occupying the lower
right third of the frame and cropped by the right edge, lit by one hard light from the upper left so
the strings catch a thin cream highlight and a long shadow falls to the lower left. The upper half
of the poster stays an even flat plum field with nothing in it, so the type sits cleanly.

Text in the image, spelled exactly as written here:
- Across the top third, the largest element on the poster, a heavy condensed sans-serif in warm
  cream, set in two lines flush left with the lines optically the same width:
  "TBILISI / JAZZ NIGHTS"
- Directly beneath it, about one fifth of the headline height, widely letterspaced, burnt orange:
  "12–14 OCTOBER · MTATSMINDA HALL"
- Bottom left corner, the smallest text on the poster, cream: "doors 19:30 · tickets on the door"
- Bottom right corner, the same size as the line above it, cream: "three nights, nine sets"

Generous even margins on all four sides, the headline block clear of the double bass, every letter
sharp, correctly spelled, evenly spaced and fully inside the frame.
```

**KA**
```
შექმენი საკონცერტო აფიშა, ვერტიკალური კადრი 2:3, სამფეროვანი სატრაფარეტო ბეჭდვა დაუფარავ ქაღალდზე,
ქაღალდის ხილული ფაქტურით. პალიტრა: ღრმა ქლიავისფერი ფონი, თბილი კრემისფერი ასოები, ერთი დამწვარი
ნარინჯისფერი აქცენტი.

გამოსახულება: კონტრაბასი დაბალი რაკურსით, ქლიავისფერ ფონზე; იკავებს კადრის ქვედა მარჯვენა მესამედს
და მარჯვენა კიდე მას კვეთს. ერთი მკვეთრი შუქი ზედა მარცხენა მხრიდან — სიმებზე თხელი კრემისფერი
ბზინვა და გრძელი ჩრდილი მარცხნივ-ქვემოთ. აფიშის ზედა ნახევარი ერთგვაროვან ქლიავისფერად რჩება,
სრულიად ცარიელი, რომ წარწერა სუფთად დაჯდეს.

წარწერა სურათში, ზუსტად ასე:
- ზედა მესამედში, აფიშის ყველაზე დიდი ელემენტი, მძიმე შევიწროებული შრიფტი თბილ კრემისფერში, ორ
  ხაზად, მარცხენა კიდეზე გასწორებული, ორივე ხაზი ოპტიკურად ერთი სიგანის:
  „TBILISI / JAZZ NIGHTS“
- პირდაპირ მის ქვეშ, სათაურის სიმაღლის დაახლოებით მეხუთედი, გაფართოებული ასოთაშორისი მანძილით,
  ნარინჯისფერში: „12–14 OCTOBER · MTATSMINDA HALL“
- ქვედა მარცხენა კუთხეში, აფიშის ყველაზე პატარა ტექსტი, კრემისფერში:
  „doors 19:30 · tickets on the door“
- ქვედა მარჯვენა კუთხეში, იმავე ზომით: „three nights, nine sets“

თანაბარი, თავისუფალი ველი ოთხივე მხრიდან, სათაურის ბლოკი კონტრაბასს არ ეხება, ყოველი ასო მკვეთრი,
სწორად დაწერილი, თანაბარი ინტერვალით და მთლიანად კადრშია.
---
Design a concert poster, 2:3 vertical, printed as a three-colour screen print on uncoated stock with a
visible paper tooth. Palette: deep plum ground, warm cream type, one burnt-orange accent.
Image: a double bass photographed from a low angle against the plum ground, occupying the lower right
third of the frame and cropped by the right edge, lit by one hard light from the upper left so the
strings catch a thin cream highlight and a long shadow falls to the lower left. The upper half of the
poster stays an even flat plum field with nothing in it.
Text in the image, spelled exactly as written here: across the top third, the largest element on the
poster, a heavy condensed sans-serif in warm cream, set in two lines flush left with the lines optically
the same width: "TBILISI / JAZZ NIGHTS". Directly beneath it, about one fifth of the headline height,
widely letterspaced, burnt orange: "12–14 OCTOBER · MTATSMINDA HALL". Bottom left corner, the smallest
text on the poster, cream: "doors 19:30 · tickets on the door". Bottom right corner, the same size,
cream: "three nights, nine sets".
Generous even margins on all four sides, the headline block clear of the double bass, every letter sharp,
correctly spelled, evenly spaced and fully inside the frame.
```

---

### NB-08 · Translate the text inside the picture
`nano-banana` `gemini` — translation, in-image text

**EN**
```
Edit the attached poster. Keep the 2:3 frame.

Translate every piece of text in the image from English into Georgian and reset it in place. The
translated lines are exactly these, and no other wording is acceptable:
- the headline becomes: "თბილისის ჯაზის ღამეები"
- the line beneath it becomes: "12–14 ოქტომბერი · მთაწმინდის დარბაზი"
- the bottom left line becomes: "კარი იღება 19:30 · ბილეთი ადგილზე"
- the bottom right line becomes: "სამი ღამე, ცხრა კონცერტი"

Keep every line in the same position, at the same size relative to the poster, in the same colour,
with the same alignment and the same letterspacing as the English text it replaces. The headline
stays two lines, flush left, optically the same width.

Nothing else changes: the same plum ground, the same double bass in the same position with the same
crop, the same hard light from the upper left, the same shadow, the same paper texture, the same
margins. Do not re-render the photograph.

Georgian is longer than English — if a line will not fit at the original size, reduce that line's
size by up to fifteen percent rather than breaking it onto a new line or crowding the margins.
```

**KA**
```
შეასწორე მიმაგრებული აფიშა. კადრის პროპორცია იგივე რჩება, 2:3.

თარგმნე სურათში არსებული ყოველი წარწერა ინგლისურიდან ქართულად და იმავე ადგილას დააწყვე. ნათარგმნი
ხაზები ზუსტად ესაა და სხვა ფორმულირება არ მიიღება:
- სათაური: „თბილისის ჯაზის ღამეები“
- მის ქვეშ მდგომი ხაზი: „12–14 ოქტომბერი · მთაწმინდის დარბაზი“
- ქვედა მარცხენა ხაზი: „კარი იღება 19:30 · ბილეთი ადგილზე“
- ქვედა მარჯვენა ხაზი: „სამი ღამე, ცხრა კონცერტი“

ყოველი ხაზი იმავე ადგილას რჩება, აფიშასთან იმავე თანაფარდობის ზომით, იმავე ფერში, იმავე
გასწორებით და იმავე ასოთაშორისი მანძილით, როგორიც ჩანაცვლებულ ინგლისურ ტექსტს ჰქონდა. სათაური
ორ ხაზად რჩება, მარცხენა კიდეზე გასწორებული, ოპტიკურად ერთი სიგანის.

სხვა არაფერი იცვლება: იგივე ქლიავისფერი ფონი, იგივე კონტრაბასი იმავე ადგილას და იმავე კადრირებით,
იგივე მკვეთრი შუქი ზედა მარცხენა მხრიდან, იგივე ჩრდილი, იგივე ქაღალდის ფაქტურა, იგივე ველები.
ფოტო ხელახლა არ დაარენდერო.

ქართული ინგლისურზე გრძელია — თუ ხაზი თავდაპირველ ზომაში არ ეტევა, შეამცირე ამ ხაზის ზომა მაქსიმუმ
თხუთმეტი პროცენტით, ახალ ხაზზე გადატანისა და ველების შევიწროების ნაცვლად.

# ქართული ასოები დიდი ალბათობით შესასწორებელი გამოვა, განსაკუთრებით დიდ სათაურში — შედეგი ასოების
# დონეზე შეამოწმე და საჭიროებისას შრიფტი დიზაინის პროგრამაში თავიდან დააწერე. საიმედო ვარიანტი:
# სთხოვე მოდელს, წარწერების ადგილი ცარიელი დატოვოს („remove all text and leave those areas as
# clean flat plum“) და ქართული შრიფტი შენ დაადო.
---
Edit the attached poster. Keep the 2:3 frame.
Translate every piece of text in the image from English into Georgian and reset it in place. The
translated lines are exactly these, and no other wording is acceptable: the headline becomes
"თბილისის ჯაზის ღამეები"; the line beneath it becomes "12–14 ოქტომბერი · მთაწმინდის დარბაზი"; the
bottom left line becomes "კარი იღება 19:30 · ბილეთი ადგილზე"; the bottom right line becomes
"სამი ღამე, ცხრა კონცერტი".
Keep every line in the same position, at the same size relative to the poster, in the same colour, with
the same alignment and the same letterspacing as the English text it replaces. The headline stays two
lines, flush left, optically the same width.
Nothing else changes: the same plum ground, the same double bass in the same position with the same crop,
the same hard light from the upper left, the same shadow, the same paper texture, the same margins. Do
not re-render the photograph.
Georgian is longer than English — if a line will not fit at the original size, reduce that line's size by
up to fifteen percent rather than breaking it onto a new line or crowding the margins. Every Georgian
letter must be correctly formed, level and fully legible.
```

---

### NB-09 · Ultra-wide 21:9 site banner
`nano-banana` `gemini` — banner, ultra-wide

**EN**
```
Photograph a vineyard banner for the top of a wine estate's website. 21:9 ultra-wide, rendered at
4K, composed specifically for this extreme width — not a wide crop of a normal photograph.

Location: a Kakheti vineyard in late September, rows of vines running away from camera toward the
Caucasus foothills, the Alazani valley haze behind them.

Composition, read left to right across the full width: the left third is open vine rows with the
horizon low, at about one third of the frame height; the middle third holds two pickers bent over
the vines, small in frame, roughly a tenth of the frame height, giving scale; the right third is
deliberately quiet — vines and haze only, no incident — because the estate's logo and one line of
type will be placed there. Keep that right third free of any bright highlight, strong line or high
contrast shape.

Camera: chest height, 50mm equivalent so the perspective stays honest, f/8, everything from the
first vine row to the foothills acceptably sharp.

Light: the sun is low behind and to the left of the camera, so the vine leaves are front-lit and
warm, the rows cast long shadows running toward the lower right, and the foothills sit in cool blue
haze. No lens flare.

Style: natural documentary landscape photography, warm greens and dusty gold, no heavy grading, no
text anywhere in the image.
```

**KA**
```
გადაიღე ვენახის ბანერი ღვინის მარნის საიტის თავისთვის. ულტრა განიერი კადრი 21:9, 4K რენდერით,
სპეციალურად ამ განიერი ფორმატისთვის აწყობილი — და არა ჩვეულებრივი ფოტოს განიერი ამონაჭერი.

ადგილი: კახეთის ვენახი სექტემბრის ბოლოს, ვაზის რიგები კამერიდან კავკასიონის მთისწინეთისკენ მიდის,
უკან ალაზნის ველის ნისლი.

კომპოზიცია, მარცხნიდან მარჯვნივ, მთელ სიგანეზე: მარცხენა მესამედი — ღია ვაზის რიგები, ჰორიზონტი
დაბლა, კადრის სიმაღლის დაახლოებით მესამედზე; შუა მესამედი — ვაზზე დახრილი 2 მკრეფავი, კადრში
პატარა, სიმაღლის დაახლოებით მეათედი, რაც მასშტაბს იძლევა; მარჯვენა მესამედი შეგნებულად წყნარია —
მხოლოდ ვაზი და ნისლი, ყოველგვარი მოვლენის გარეშე — რადგან იქ მარნის ლოგო და ერთი ხაზი წარწერა
დაიდება. მარჯვენა მესამედში არ დატოვო არც ერთი კაშკაშა ლაქა, მკვეთრი ხაზი ან მაღალი კონტრასტის ფორმა.

კამერა: მკერდის სიმაღლეზე, 50 მმ ექვივალენტი — პერსპექტივა პატიოსანი რჩება, f/8, პირველი ვაზის
რიგიდან მთისწინეთამდე ყველაფერი საკმარისად მკვეთრია.

განათება: მზე დაბალია, კამერის უკან და მარცხნივ — ვაზის ფოთოლი წინიდან განათებული და თბილია,
რიგები გრძელ ჩრდილებს აგდებს მარჯვნივ-ქვემოთ, მთისწინეთი ცივ ლურჯ ნისლშია. ობიექტივის ბრჭყვიალის
გარეშე.

სტილი: ბუნებრივი დოკუმენტური პეიზაჟის ფოტოგრაფია, თბილი მწვანე და მტვრიანი ოქროსფერი, ფერის მძიმე
დამუშავების გარეშე; კადრში წარწერა არსად არ არის.
---
Photograph a vineyard banner for the top of a wine estate's website. 21:9 ultra-wide, rendered at 4K,
composed specifically for this extreme width — not a wide crop of a normal photograph.
Location: a Kakheti vineyard in late September, rows of vines running away from camera toward the
Caucasus foothills, the Alazani valley haze behind them.
Composition, read left to right across the full width: the left third is open vine rows with the horizon
low, at about one third of the frame height; the middle third holds two pickers bent over the vines,
small in frame, roughly a tenth of the frame height, giving scale; the right third is deliberately quiet
— vines and haze only, no incident — because the estate's logo and one line of type will be placed there.
Keep that right third free of any bright highlight, strong line or high contrast shape.
Camera: chest height, 50mm equivalent so the perspective stays honest, f/8, everything from the first
vine row to the foothills acceptably sharp.
Light: the sun is low behind and to the left of the camera, so the vine leaves are front-lit and warm,
the rows cast long shadows running toward the lower right, and the foothills sit in cool blue haze. No
lens flare.
Style: natural documentary landscape photography, warm greens and dusty gold, no heavy grading, no text
anywhere in the image.
```

---

### NB-10 · Guesthouse listing set — four frames, one shoot
`nano-banana` `gemini` — consistency, real estate

**EN**
```
Produce four photographs of the same guesthouse in Sighnaghi for one booking listing. They must
read as four frames from a single shoot on a single afternoon, by one photographer with one camera.

Hold these constant across all four images, word for word:
"A stone guesthouse with lime-plastered white walls, a dark stained timber ceiling, wide-plank oak
floors, deep-set windows with plain white linen curtains, and a carved wooden balcony rail painted
dusty blue. It is 16:30 in early autumn; the sun is low and to the west, entering every room from
the same side; the light is warm, soft and unbroken, with no lamp switched on anywhere."

Every frame: 4:5 vertical, 24mm equivalent with the camera held level so the vertical lines stay
vertical, f/5.6, camera at 140cm, no people, no wide-angle distortion at the edges, identical white
balance and identical mild contrast across all four.

Frame 1 — the double bedroom, shot from the doorway: the bed centred on the far wall, the window on
the left, the light falling across the bedspread from left to right.
Frame 2 — the kitchen, shot from the corner opposite the window: the wooden table on the right third,
the window on the left, the same warm beam crossing the table top.
Frame 3 — the balcony, shot from inside looking out through the open door: the dusty blue rail across
the lower third, the roofs of Sighnaghi and the Alazani valley beyond, the low sun out of frame to
the left.
Frame 4 — the bathroom, shot from the doorway: white tile, a small deep-set window high on the left
wall, the same warm light pooling on the floor.

If a wall, a floorboard tone or a curtain appears in more than one frame, it must be the same colour,
the same texture and the same brightness in every frame it appears in.
```

**KA**
```
გადაიღე ერთი და იმავე სასტუმრო სახლის 4 ფოტო სიღნაღში, ერთი განცხადებისთვის. ოთხივე კადრი ისე
უნდა იკითხებოდეს, თითქოს ერთ შუადღეს, ერთმა ფოტოგრაფმა, ერთი კამერით გადაიღო.

ეს აღწერა ოთხივე კადრში სიტყვასიტყვით უცვლელი რჩება:
„ქვის სასტუმრო სახლი: კირის ბათქაშით შეთეთრებული კედლები, მუქად მორილული ხის ჭერი, განიერფიცრიანი
მუხის იატაკი, ღრმად ჩამჯდარი ფანჯრები უბრალო თეთრი სელის ფარდებით და მოჩუქურთმებული ხის აივნის
მოაჯირი, მტვრისფერ ცისფრად შეღებილი. დრო შემოდგომის დასაწყისის 16:30-ია; მზე დაბალია, დასავლეთით
და ყოველ ოთახში ერთი და იმავე მხრიდან შემოდის; შუქი თბილი, რბილი და უწყვეტია; არსად არცერთი
ნათურა არ ანთია.“

ყოველი კადრი: ვერტიკალური 4:5, 24 მმ ექვივალენტი, კამერა სწორად დაჭერილი — ვერტიკალური ხაზები
ვერტიკალურად რჩება, f/5.6, კამერა 140 სმ სიმაღლეზე, ადამიანების გარეშე, კიდეებში განიერი
ობიექტივის დამახინჯების გარეშე; ოთხივე კადრში ერთი და იგივე თეთრის ბალანსი და ერთი და იგივე,
სუსტი კონტრასტი.

კადრი 1 — ორადგილიანი საძინებელი, კარიდან: საწოლი შორეული კედლის ცენტრში, ფანჯარა მარცხნივ, შუქი
საბანზე მარცხნიდან მარჯვნივ ეცემა.
კადრი 2 — სამზარეულო, ფანჯრის მოპირდაპირე კუთხიდან: ხის მაგიდა მარჯვენა მესამედში, ფანჯარა
მარცხნივ, იგივე თბილი სხივი მაგიდის ზედაპირს კვეთს.
კადრი 3 — აივანი, შიგნიდან, ღია კარიდან გადაღებული: მტვრისფერ-ცისფერი მოაჯირი ქვედა მესამედში,
უკან სიღნაღის სახურავები და ალაზნის ველი, დაბალი მზე კადრს გარეთ, მარცხნივ.
კადრი 4 — სააბაზანო, კარიდან: თეთრი კაფელი, პატარა, ღრმად ჩამჯდარი ფანჯარა მარცხენა კედელზე
მაღლა, იგივე თბილი შუქი იატაკზე ლაქად.

თუ რომელიმე კედელი, იატაკის ტონი ან ფარდა ერთზე მეტ კადრში ჩანს, ყველგან ერთი და იმავე ფერის,
ფაქტურისა და სიკაშკაშის უნდა იყოს.
---
Produce four photographs of the same guesthouse in Sighnaghi for one booking listing. They must read as
four frames from a single shoot on a single afternoon, by one photographer with one camera.
Hold these constant across all four images, word for word:
"A stone guesthouse with lime-plastered white walls, a dark stained timber ceiling, wide-plank oak floors,
deep-set windows with plain white linen curtains, and a carved wooden balcony rail painted dusty blue. It
is 16:30 in early autumn; the sun is low and to the west, entering every room from the same side; the
light is warm, soft and unbroken, with no lamp switched on anywhere."
Every frame: 4:5 vertical, 24mm equivalent with the camera held level so the vertical lines stay vertical,
f/5.6, camera at 140cm, no people, no wide-angle distortion at the edges, identical white balance and
identical mild contrast across all four.
Frame 1 — the double bedroom, shot from the doorway: the bed centred on the far wall, the window on the
left, the light falling across the bedspread from left to right.
Frame 2 — the kitchen, shot from the corner opposite the window: the wooden table on the right third, the
window on the left, the same warm beam crossing the table top.
Frame 3 — the balcony, shot from inside looking out through the open door: the dusty blue rail across the
lower third, the roofs of Sighnaghi and the Alazani valley beyond, the low sun out of frame to the left.
Frame 4 — the bathroom, shot from the doorway: white tile, a small deep-set window high on the left wall,
the same warm light pooling on the floor.
If a wall, a floorboard tone or a curtain appears in more than one frame, it must be the same colour, the
same texture and the same brightness in every frame it appears in.
```

---

### NB-11 · Vertical product frame with reserved negative space
`nano-banana` `gemini` — product, negative space

**EN**
```
Photograph a wine bottle for a 9:16 vertical story frame, composed so that a designer can drop
Georgian type into the top of the image afterwards. Render at 4K.

Subject: a single Saperavi bottle in near-black glass with a cream uncoated paper label, standing
upright on a rough limestone slab. Shown straight on, label facing camera, fully unobstructed.

Composition: the bottle occupies the lower 45 percent of the frame, its base sitting about one tenth
of the frame height above the bottom edge, centred horizontally. The upper 45 percent of the frame
is deliberately empty: an even, unbroken warm grey gradient with no object, no texture detail, no
bright highlight and no strong edge anywhere in it — this is reserved negative space for a headline
and one line of small type, so nothing may intrude into it, not even the neck of the bottle or a
lens flare. The remaining strip between them is the soft transition.

Camera: 100mm equivalent at label height, f/8, the whole label sharp corner to corner.

Light: one large softbox high on the right, feathered so the top of the frame stays evenly lit and
one stop darker than the label; a white bounce card on the left lifting the shadow side of the glass;
one clean specular band down the left shoulder; a short soft contact shadow falling to the lower left
of the base and staying well clear of the empty upper half.

No text anywhere in the image — leave the label blank cream paper as well, so the label artwork can
be placed on it in the layout stage.
```

**KA**
```
გადაიღე ღვინის ბოთლი ვერტიკალური სთორის კადრისთვის, 9:16, ისე აწყობილი, რომ დიზაინერმა შემდეგ
კადრის ზედა ნაწილში ქართული შრიფტი დაადოს. რენდერი 4K.

ობიექტი: ერთი საფერავის ბოთლი თითქმის შავი მინისა, კრემისფერი, დაუფარავი ქაღალდის ეტიკეტით,
უხეში კირქვის ფილაზე ვერტიკალურად დგას. პირდაპირი ხედი, ეტიკეტი კამერისკენ, სრულიად ღია.

კომპოზიცია: ბოთლი კადრის ქვედა 45 პროცენტს იკავებს, ძირი ქვედა კიდიდან კადრის სიმაღლის დაახლოებით
მეათედით მაღლაა, ჰორიზონტალურად ცენტრში. კადრის ზედა 45 პროცენტი შეგნებულად ცარიელია: თანაბარი,
უწყვეტი თბილი ნაცრისფერი გრადიენტი — არც ერთი საგანი, არც ერთი ფაქტურის დეტალი, არც ერთი კაშკაშა
ლაქა და არც ერთი მკვეთრი კიდე. ეს არის სათაურისა და ერთი პატარა ხაზისთვის დატოვებული თავისუფალი
ველი, ამიტომ იქ ვერაფერი შეიჭრება — ვერც ბოთლის ყელი და ვერც ობიექტივის ბრჭყვიალი. დანარჩენი
ზოლი მათ შორის რბილი გადასვლაა.

კამერა: 100 მმ ექვივალენტი, ეტიკეტის სიმაღლეზე, f/8 — ეტიკეტი კიდიდან კიდემდე მკვეთრია.

განათება: ერთი დიდი სოფტბოქსი მაღლა, მარჯვნივ, კიდით მიმართული ისე, რომ კადრის ზედა ნაწილი
თანაბრად განათებული და ეტიკეტზე ერთი საფეხურით მუქი დარჩეს; თეთრი არეკვლის ფარი მარცხნივ ავსებს
მინის ჩრდილიან მხარეს; ერთი სუფთა შუქის ზოლი მარცხენა მხარზე; მოკლე, რბილი ჩრდილი ძირიდან
მარცხნივ-ქვემოთ, რომელიც ცარიელ ზედა ნახევარს არ უახლოვდება.

კადრში წარწერა არსად არ არის — ეტიკეტიც ცარიელი, კრემისფერი ქაღალდი დატოვე, რომ მაკეტი შემდეგ
ზემოდან დაიდოს.

# ქართული ტექსტი შეგნებულად არ ვთხოვეთ მოდელს: ეტიკეტიც და ზედა ველიც ცარიელი რჩება, შრიფტი კი
# დიზაინის პროგრამაში დაიდება — ეს ქართული წარწერისთვის ერთადერთი საიმედო გზაა.
---
Photograph a wine bottle for a 9:16 vertical story frame, composed so that a designer can drop Georgian
type into the top of the image afterwards. Render at 4K.
Subject: a single Saperavi bottle in near-black glass with a cream uncoated paper label, standing upright
on a rough limestone slab. Shown straight on, label facing camera, fully unobstructed.
Composition: the bottle occupies the lower 45 percent of the frame, its base sitting about one tenth of
the frame height above the bottom edge, centred horizontally. The upper 45 percent of the frame is
deliberately empty: an even, unbroken warm grey gradient with no object, no texture detail, no bright
highlight and no strong edge anywhere in it — this is reserved negative space for a headline and one line
of small type, so nothing may intrude into it, not even the neck of the bottle or a lens flare. The
remaining strip between them is the soft transition.
Camera: 100mm equivalent at label height, f/8, the whole label sharp corner to corner.
Light: one large softbox high on the right, feathered so the top of the frame stays evenly lit and one
stop darker than the label; a white bounce card on the left lifting the shadow side of the glass; one
clean specular band down the left shoulder; a short soft contact shadow falling to the lower left of the
base and staying well clear of the empty upper half.
No text anywhere in the image — leave the label blank cream paper as well, so the label artwork can be
placed on it in the layout stage.
```
