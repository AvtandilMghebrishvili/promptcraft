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

---

### NB-12 · Impossible scale, shot as a real photograph
`nano-banana` `gemini` — creative, macro, scale

**EN**
```
Photograph one impossible object as though it genuinely existed and a macro photographer had been
sent to document it. Nothing may look illustrated or composited — the physics of light is obeyed
everywhere in the frame.

Subject: a walnut broken into two halves. The smaller half lies discarded on its back in the lower
right. The larger half stands upright and has been hollowed out into a complete cabinetmaker's
workshop: a workbench the length of a fingernail with a vice at its far end, a rack of chisels on
the curved inner wall sorted by blade width, wood shavings curled on the floor, a stool built from
matchstick timber, and one working lamp on a bent wire arm. Everything inside is built at the scale
the shell dictates — the grain in the tiny boards is real timber grain, not a texture pattern.

Composition: 1:1 square. The standing half sits slightly left of centre and fills about 60 percent
of the frame height; the discarded half lies in the lower right, out of focus. A dark oiled wooden
tabletop runs across the bottom third; above it the background is an unlit brown falling to near
black. No prop competes with the shell.

Camera: macro, 100mm equivalent, sensor at the height of the workbench inside the shell, tilted a
few degrees down so you can see into the interior, f/5.6 with the focus stacked so the whole
interior is sharp while the discarded half and the background stay soft.

Light: the tiny lamp inside the shell is the dominant source — a warm pool on the workbench that
falls off fast up the curved inner wall and throws the chisel rack's shadows upward and to the left.
One weak, cool daylight fill from high camera right catches the ridged outer skin of the shell and
separates it from the background. No third light, no glow effect.

Style: natural-history macro photography, honest colour, dust motes visible in the warm beam, real
depth of field, no text anywhere in the image.
```

**KA**
```
გადაიღე ერთი შეუძლებელი ობიექტი ისე, თითქოს ის ნამდვილად არსებობს და მაკროფოტოგრაფი სპეციალურად
მის დასაფიქსირებლად გაგზავნეს. არაფერი უნდა გამოიყურებოდეს ნახატად ან მონტაჟად — სინათლის ფიზიკა
კადრში ყველგან დაცულია.

ობიექტი: ორად გატეხილი ნიგოზი. პატარა ნახევარი ქვედა მარჯვენა კუთხეში, ზურგზე გადაბრუნებული და
მიტოვებული. დიდი ნახევარი ვერტიკალურად დგას და შიგნიდან ავეჯის ოსტატის სრულ სახელოსნოდაა
გამოთლილი: ფრჩხილის სიგრძის დაზგა, ბოლოში მენგელით; მოხრილ შიდა კედელზე საჭრისების თარო, პირის
სიგანის მიხედვით დალაგებული; იატაკზე დახვეული ბურბუშელა; ასანთის ღეროებისგან შეკრული სკამი და
ერთი ანთებული სანათი მოხრილ მავთულის მკლავზე. შიგნით ყველაფერი იმ მასშტაბითაა აშენებული,
რომელსაც ნაჭუჭი კარნახობს — პატარა ფიცრებში ხის ბოჭკო ნამდვილი ბოჭკოა და არა ფაქტურის ნახატი.

კომპოზიცია: კვადრატული კადრი 1:1. მდგარი ნახევარი ცენტრიდან ოდნავ მარცხნივ დგას და კადრის
სიმაღლის დაახლოებით 60 პროცენტს იკავებს; მიტოვებული ნახევარი ქვედა მარჯვნივ, ფოკუსს გარეთ.
ქვედა მესამედს მუქი, ზეთით დამუშავებული ხის მაგიდა კვეთს; მის ზემოთ ფონი განუათებელი ყავისფერია
და თითქმის შავში გადადის. არცერთი სხვა საგანი ნაჭუჭს ყურადღებას არ ჰპარავს.

კამერა: მაკრო, 100 მმ ექვივალენტი, სენსორი ნაჭუჭის შიგნით დაზგის სიმაღლეზე, რამდენიმე გრადუსით
ქვემოთ დახრილი, რომ შიდა სივრცე ჩანდეს; f/5.6, ფოკუსი დაწყობილია — მთელი ინტერიერი მკვეთრია,
მიტოვებული ნახევარი და ფონი კი რბილი რჩება.

განათება: მთავარი წყარო ნაჭუჭში მდგარი პატარა სანათია — თბილი ლაქა დაზგაზე, რომელიც მოხრილ შიდა
კედელზე სწრაფად ქრება და საჭრისების თაროს ჩრდილებს ზემოთ და მარცხნივ აგდებს. ერთი სუსტი, ცივი
დღის შუქი მაღლა, კამერიდან მარჯვნივ, ნაჭუჭის ხორკლიან გარე ზედაპირს ეხება და ფონს აცილებს.
მესამე წყარო და ხელოვნური ნათება არ არის.

სტილი: სამეცნიერო-დოკუმენტური მაკროფოტოგრაფია, პატიოსანი ფერი, თბილ სხივში ხილული მტვრის
ნაწილაკები, ნამდვილი სიღრმის ველი; კადრში წარწერა არსად არ არის.
---
Photograph one impossible object as though it genuinely existed and a macro photographer had been sent
to document it. Nothing may look illustrated or composited — the physics of light is obeyed everywhere.
Subject: a walnut broken into two halves. The smaller half lies discarded on its back in the lower right.
The larger half stands upright and has been hollowed out into a complete cabinetmaker's workshop: a
workbench the length of a fingernail with a vice at its far end, a rack of chisels on the curved inner
wall sorted by blade width, wood shavings curled on the floor, a stool built from matchstick timber, and
one working lamp on a bent wire arm. Everything inside is built at the scale the shell dictates — the
grain in the tiny boards is real timber grain, not a texture pattern.
Composition: 1:1 square. The standing half sits slightly left of centre and fills about 60 percent of the
frame height; the discarded half lies in the lower right, out of focus. A dark oiled wooden tabletop runs
across the bottom third; above it the background is an unlit brown falling to near black.
Camera: macro, 100mm equivalent, sensor at the height of the workbench inside the shell, tilted a few
degrees down so you can see into the interior, f/5.6 with the focus stacked so the whole interior is
sharp while the discarded half and the background stay soft.
Light: the tiny lamp inside the shell is the dominant source — a warm pool on the workbench that falls
off fast up the curved inner wall and throws the chisel rack's shadows upward and to the left. One weak,
cool daylight fill from high camera right catches the ridged outer skin of the shell and separates it
from the background. No third light, no glow effect.
Style: natural-history macro photography, honest colour, dust motes visible in the warm beam, real depth
of field, no text anywhere in the image.
```

---

### NB-13 · One subject, four media, one image
`nano-banana` `gemini` — creative, grid, media study

**EN**
```
Produce a single image that is a 2x2 grid of four panels, all showing the identical subject rendered
in four different media. This is one picture with four cells, not four separate pictures.

The subject, identical in all four panels: a pomegranate split into two halves — the larger half
standing with its cut face toward the viewer and the seeds exposed, the smaller half lying beside it
on its skin and tilted so that four loose seeds have spilled to the left. The pose, the viewing
angle, the proportions and the positions of the two halves are exactly the same in all four panels.
Only the medium changes.

Layout: 1:1 square overall. Four equal cells divided by a clean white gutter about 2 percent of the
image width, with the same white margin on all four outer sides. In every panel the subject is
centred and occupies about 70 percent of the panel width, at the same scale, and the light is
implied from the same place: a single soft source high on the upper left, so the shadow falls to the
lower right in all four panels.

Top left — graphite: a tight pencil study on off-white paper, built from hatching and cross-hatching
only, no smudging or blending, the highlights on the seeds left as bare paper.
Top right — watercolour: wet-on-wet washes on cold-pressed paper with visible blooms at the edges of
the washes, a granulating crimson in the seeds, the white of the paper doing the highlights, no ink
outline anywhere.
Bottom left — risograph: a two-colour print in fluorescent pink and medium blue, coarse halftone
dots, the blue plate deliberately misregistered about one millimetre toward the lower right, visible
paper texture and faint roller streaks.
Bottom right — 3D clay render: matte unglazed terracotta, soft global illumination, a warm
translucency in the thinnest edges, slightly rounded corners and fingerprint-scale surface
irregularity, standing on a plain light grey backdrop.

No text, no labels, no panel numbers and no frames around the cells.
```

**KA**
```
შექმენი ერთი სურათი, რომელიც 2x2 ბადეა — 4 პანელი და ოთხივეში ერთი და იგივე ობიექტი, ოთხ სხვადასხვა
მასალაში შესრულებული. ეს ერთი კადრია ოთხი უჯრით და არა 4 ცალკე სურათი.

ობიექტი, ოთხივე პანელში იდენტური: ორად გაჭრილი ბროწეული — დიდი ნახევარი დგას, ჭრილით
მაყურებლისკენ, მარცვლები ღიაა; პატარა ნახევარი მის გვერდით წევს, კანზე დაწყობილი და ისე დახრილი,
რომ მარცხნივ 4 მარცვალი გადმოყრილა. პოზა, ხედვის კუთხე, პროპორცია და ორივე ნახევრის ადგილი
ოთხივე პანელში ზუსტად ერთი და იგივეა. იცვლება მხოლოდ მასალა.

მაკეტი: მთლიანი კადრი კვადრატული, 1:1. ოთხი თანაბარი უჯრა, მათ შორის სუფთა თეთრი ზოლი — სურათის
სიგანის დაახლოებით 2 პროცენტი; ოთხივე გარე მხარეს იგივე თეთრი ველი. ყოველ პანელში ობიექტი
ცენტრშია და პანელის სიგანის დაახლოებით 70 პროცენტს იკავებს, ერთი მასშტაბით; შუქი ყველგან ერთი
ადგილიდან იგულისხმება — ერთი რბილი წყარო მაღლა, ზედა მარცხენა მხარეს, ამიტომ ჩრდილი ოთხივე
პანელში მარჯვნივ-ქვემოთ ეცემა.

ზედა მარცხენა — გრაფიტი: მჭიდრო ფანქრის ეტიუდი მოთეთრო ქაღალდზე, აგებული მხოლოდ შტრიხითა და
ჯვარედინი შტრიხით, დაბუნდოვნებისა და გადასმის გარეშე; მარცვლების ბზინვა ცარიელი ქაღალდია.

ზედა მარჯვენა — აკვარელი: სველზე სველი შრეები ცივი წნეხის ქაღალდზე, შრის კიდეებზე ხილული
გამორეცხილი ლაქები, მარცვლებში მარცვლოვანი ალისფერი პიგმენტი, ბზინვას ქაღალდის სითეთრე იღებს,
კონტურის ხაზი არსად არ არის.

ქვედა მარცხენა — რიზოგრაფი: ორფეროვანი ბეჭდვა — ფლუორესცენტური ვარდისფერი და საშუალო ლურჯი,
მსხვილი რასტრის წერტილები, ლურჯი ფორმა შეგნებულად დაახლოებით 1 მილიმეტრითაა აცდენილი
მარჯვნივ-ქვემოთ, ჩანს ქაღალდის ფაქტურა და ლილვის სუსტი ზოლები.

ქვედა მარჯვენა — თიხის 3D რენდერი: მქრქალი, უჭიქური ტერაკოტა, რბილი გლობალური განათება, უთხელეს
კიდეებში თბილი გამჭვირვალობა, ოდნავ მომრგვალებული კუთხეები და თითის ანაბეჭდის მასშტაბის
უსწორმასწორობა; ფონი უბრალო ღია ნაცრისფერი.

კადრში წარწერა, იარლიყი, პანელის ნომერი და უჯრების ჩარჩო არსად არ არის.
---
Produce a single image that is a 2x2 grid of four panels, all showing the identical subject rendered in
four different media. This is one picture with four cells, not four separate pictures.
The subject, identical in all four panels: a pomegranate split into two halves — the larger half standing
with its cut face toward the viewer and the seeds exposed, the smaller half lying beside it on its skin
and tilted so that four loose seeds have spilled to the left. The pose, the viewing angle, the proportions
and the positions of the two halves are exactly the same in all four panels. Only the medium changes.
Layout: 1:1 square overall. Four equal cells divided by a clean white gutter about 2 percent of the image
width, with the same white margin on all four outer sides. In every panel the subject is centred and
occupies about 70 percent of the panel width, at the same scale, and the light is implied from the same
place: a single soft source high on the upper left, so the shadow falls to the lower right in all four.
Top left — graphite: a tight pencil study on off-white paper, built from hatching and cross-hatching only,
no smudging, the highlights on the seeds left as bare paper.
Top right — watercolour: wet-on-wet washes on cold-pressed paper with visible blooms at the edges of the
washes, a granulating crimson in the seeds, the white of the paper doing the highlights, no ink outline.
Bottom left — risograph: a two-colour print in fluorescent pink and medium blue, coarse halftone dots, the
blue plate deliberately misregistered about one millimetre toward the lower right, visible paper texture
and faint roller streaks.
Bottom right — 3D clay render: matte unglazed terracotta, soft global illumination, a warm translucency in
the thinnest edges, slightly rounded corners and fingerprint-scale surface irregularity, standing on a
plain light grey backdrop.
No text, no labels, no panel numbers and no frames around the cells.
```

---

### NB-14 · The same corner, a century each way
`nano-banana` `gemini` — creative, multi-turn, editing

**EN**
```
Run this as three turns in one conversation. Turn 1 builds the scene; turns 2 and 3 are edits of
that same image. Do not merge them.

TURN 1 — the corner as it is today
Photograph a street corner in Sololaki, Tbilisi, 3:2 horizontal. A two-storey brick and plaster
house stands on the corner with a carved wooden balcony running along its first floor, the balcony
posts leaning slightly out of true. The pavement curves away to the right and out of frame. Camera
at standing eye level on the opposite pavement, 35mm equivalent, f/8, held level so the vertical
lines stay vertical, the corner of the building on the left third and the street opening into the
right two thirds. It is 10:00 on a clear spring morning; the sun is behind and to the left of the
camera, so the front face of the house is warmly lit and the returning side wall falls into soft
shade, with short shadows running toward the lower right. Natural documentary street photography,
honest colour, no people close enough to be identifiable, no text anywhere in the image.

TURN 2 — the same corner one hundred years earlier
Keep the building footprint, the roof line, the balcony's position and geometry, the street's
curvature, the camera position, the focal length, the crop, the 3:2 frame, the time of day and the
direction and hardness of the sunlight exactly as they are. Change only what a hundred years would
have changed: the plaster is newer and unpatched, the balcony timber is freshly painted and the
posts stand straight, there are no electrical or telephone cables anywhere, no air conditioning
units, no parked cars, no road markings and no modern signage. The road surface becomes cobbles.
Two figures in period clothing stand in the middle distance, small in frame and turned away. Render
the whole frame as a period photograph: slightly warm monochrome, lower contrast, a little edge
softness, fine grain. Do not move the camera and do not reframe.

TURN 3 — the same corner one hundred years from now
Go back to the image from turn 1, not turn 2. Keep the building footprint, the roof line, the
balcony's position, the street's curvature, the camera position, the focal length, the crop, the
3:2 frame, the time of day and the same sunlight from behind camera left. Change only the
century's worth of accretion: the plaster is repaired in mismatched patches, the balcony has been
reinforced with a slim modern bracket under each post, the cables are gone underground, the road is
a quiet resurfaced shared-use street with young plane trees planted along it, and one small
unlabelled delivery vehicle stands at the kerb. Keep it plausible and undramatic — no flying
machines, no neon, no text anywhere in the image. Same photographic treatment as turn 1: natural
colour, documentary, no grading.
```

**KA**
```
ეს 3 ეტაპია ერთ საუბარში. პირველი ეტაპი სცენას დგამს, მეორე და მესამე კი იმავე სურათის
რედაქტირებაა. ერთ პრომპტად არ გააერთიანო.

ეტაპი 1 — კუთხე ისე, როგორც დღესაა
გადაიღე ქუჩის კუთხე თბილისში, სოლოლაკში; ჰორიზონტალური კადრი 3:2. კუთხეში ორსართულიანი აგურისა
და ბათქაშის სახლი დგას, პირველ სართულზე მოჩუქურთმებული ხის აივანი გასდევს, აივნის სვეტები ოდნავ
გადახრილია. ტროტუარი მარჯვნივ იკეცება და კადრს გარეთ გადის. კამერა მოპირდაპირე ტროტუარზე, მდგომი
ადამიანის თვალის დონეზე, 35 მმ ექვივალენტი, f/8, სწორად დაჭერილი — ვერტიკალური ხაზები
ვერტიკალურად რჩება; შენობის კუთხე მარცხენა მესამედში, ქუჩა კი მარჯვენა ორ მესამედში იხსნება.
დრო — გაზაფხულის ნათელი დილის 10:00; მზე კამერის უკან და მარცხნივაა, ამიტომ სახლის ფასადი თბილად
განათებულია, გვერდითი კედელი რბილ ჩრდილში გადადის, ჩრდილები კი მოკლეა და მარჯვნივ-ქვემოთ ეცემა.
ბუნებრივი დოკუმენტური ქუჩის ფოტოგრაფია, პატიოსანი ფერი; ამოსაცნობად ახლოს არავინ დგას; კადრში
წარწერა არსად არ არის.

ეტაპი 2 — იგივე კუთხე 100 წლის წინ
შენობის კონტური, სახურავის ხაზი, აივნის ადგილი და გეომეტრია, ქუჩის მოხაზულობა, კამერის ადგილი,
ფოკუსური მანძილი, კადრირება, პროპორცია 3:2, დღის დრო და მზის მიმართულება და სიმკვეთრე ზუსტად
უცვლელი რჩება. შეცვალე მხოლოდ ის, რასაც 100 წელი შეცვლიდა: ბათქაში ახალია და შეულესავი ადგილი
არ აქვს, აივნის ხე ახლად შეღებილია და სვეტები სწორად დგას; არსად არ არის ელექტროსადენი და
სატელეფონო კაბელი, კონდიციონერი, გაჩერებული მანქანა, საგზაო მონიშვნა და თანამედროვე აბრა.
გზის საფარი კენჭოვანი ქვაფენილი ხდება. შუა პლანზე 2 ფიგურა დგას იმდროინდელ ტანსაცმელში, კადრში
პატარა და ზურგით შემობრუნებული. მთელი კადრი იმდროინდელ ფოტოდ დაარენდერე: ოდნავ თბილი შავ-თეთრი,
დაბალი კონტრასტი, კიდეებში მცირე სირბილე, წვრილი მარცვალი. კამერა არ გადაადგილო და კადრი არ
გადააწყო.

ეტაპი 3 — იგივე კუთხე 100 წლის შემდეგ
დაუბრუნდი პირველი ეტაპის სურათს და არა მეორისას. შენობის კონტური, სახურავის ხაზი, აივნის ადგილი,
ქუჩის მოხაზულობა, კამერის ადგილი, ფოკუსური მანძილი, კადრირება, პროპორცია 3:2, დღის დრო და იგივე
მზე კამერის უკნიდან, მარცხნიდან — უცვლელი რჩება. შეცვალე მხოლოდ ის, რასაც საუკუნე დაატანს:
ბათქაში სხვადასხვა ტონის ნაკერებითაა შეკეთებული, აივანი ყოველი სვეტის ქვეშ თხელი თანამედროვე
საყრდენითაა გამაგრებილი, კაბელები მიწის ქვეშაა გადატანილი, გზა წყნარი, ხელახლა დაგებული საერთო
სარგებლობის ქუჩაა, გასწვრივ ახალგაზრდა ჭადრები დგას, კიდეზე კი ერთი პატარა, უაბრო საკურიერო
ავტომობილი. ყველაფერი დამაჯერებელი და მშვიდი იყოს — მფრინავი აპარატი, ნეონი და წარწერა კადრში
არ გამოჩნდეს. ფოტოგრაფიული დამუშავება იგივეა, რაც პირველ ეტაპზე: ბუნებრივი ფერი, დოკუმენტური
მანერა, ფერის დამატებითი დამუშავების გარეშე.
---
Run this as three turns in one conversation. Turn 1 builds the scene; turns 2 and 3 are edits of that same
image. Do not merge them.
TURN 1 — the corner as it is today. Photograph a street corner in Sololaki, Tbilisi, 3:2 horizontal. A
two-storey brick and plaster house stands on the corner with a carved wooden balcony running along its
first floor, the balcony posts leaning slightly out of true. The pavement curves away to the right and out
of frame. Camera at standing eye level on the opposite pavement, 35mm equivalent, f/8, held level so the
vertical lines stay vertical, the corner of the building on the left third and the street opening into the
right two thirds. It is 10:00 on a clear spring morning; the sun is behind and to the left of the camera,
so the front face is warmly lit and the returning side wall falls into soft shade, with short shadows
running toward the lower right. Natural documentary street photography, honest colour, no identifiable
people, no text anywhere in the image.
TURN 2 — the same corner one hundred years earlier. Keep the building footprint, the roof line, the
balcony's position and geometry, the street's curvature, the camera position, the focal length, the crop,
the 3:2 frame, the time of day and the direction and hardness of the sunlight exactly as they are. Change
only what a hundred years would have changed: newer unpatched plaster, freshly painted balcony timber with
the posts standing straight, no electrical or telephone cables, no air conditioning units, no parked cars,
no road markings, no modern signage. The road surface becomes cobbles. Two figures in period clothing
stand in the middle distance, small in frame and turned away. Render the whole frame as a period
photograph: slightly warm monochrome, lower contrast, a little edge softness, fine grain. Do not move the
camera and do not reframe.
TURN 3 — the same corner one hundred years from now. Go back to the image from turn 1, not turn 2. Keep
the building footprint, the roof line, the balcony's position, the street's curvature, the camera position,
the focal length, the crop, the 3:2 frame, the time of day and the same sunlight from behind camera left.
Change only the century's worth of accretion: plaster repaired in mismatched patches, a slim modern
bracket reinforcing each balcony post, the cables gone underground, the road a quiet resurfaced shared-use
street with young plane trees along it, and one small unlabelled delivery vehicle at the kerb. Keep it
plausible and undramatic — no flying machines, no neon, no text anywhere in the image. Same photographic
treatment as turn 1: natural colour, documentary, no grading.
```

---

### NB-15 · Knolling exploded view with labelled parts
`nano-banana` `gemini` — knolling, exploded view, in-image text

**EN**
```
Photograph a hand coffee grinder completely taken apart and laid out flat, knolling style, with
every part labelled in the image. 4:5 vertical, rendered at 4K.

Subject and layout: all fourteen parts of a hand coffee grinder — the cylindrical steel body, the
lid, the crank handle, the handle knob, the central drive shaft, the top burr, the bottom burr, the
adjustment nut, the spring, two bearings, the catch jar, its silicone ring and one hex screw — are
arranged on a flat surface in strict knolling discipline: every part parallel or perpendicular to
the frame edges, nothing overlapping, even spacing, grouped so the assembly order reads from the
top left to the bottom right. Keep the parts at true relative scale to each other; the body is the
largest object in the frame and the screw the smallest.

Background: a smooth mid-grey seamless surface with no texture, no grain and no visible edge.

Camera: directly overhead, the sensor exactly parallel to the surface so there is no perspective
convergence anywhere, 50mm equivalent shot from far enough back that the edge parts are not
distorted, f/8, everything sharp corner to corner.

Light: one large softbox high on the upper left of the surface, feathered for even coverage, plus a
white bounce card on the lower right. Every part throws a short, soft shadow of the same length in
the same direction — toward the lower right — and no part sits in another part's shadow. No
specular hotspot on the steel.

Text in the image, spelled exactly as written here, all in a light grey uppercase sans-serif set at
roughly one fiftieth of the frame height, each label placed just below its part and joined to it by
a hairline leader line: "BODY", "LID", "CRANK", "KNOB", "SHAFT", "TOP BURR", "BOTTOM BURR",
"ADJUSTMENT NUT", "SPRING", "BEARING", "BEARING", "CATCH JAR", "SILICONE RING", "SCREW".
Across the bottom margin, centred, at about twice the label size: "HAND COFFEE GRINDER · 14 PARTS".
Leave an even, empty margin on all four sides. Every letter sharp, correctly spelled and fully
inside the frame.
```

**KA**
```
გადაიღე ხელის საყავე წისქვილი სრულად დაშლილი და ბრტყლად დალაგებული, ნოლინგის მანერაში, სადაც
ყოველ დეტალს სურათშივე აწერია სახელი. ვერტიკალური კადრი 4:5, რენდერი 4K.

ობიექტი და განლაგება: ხელის საყავე წისქვილის 14 დეტალი — ცილინდრული ფოლადის კორპუსი, თავსახური,
სახელური, სახელურის ღილი, ცენტრალური ლილვი, ზედა ფრეზი, ქვედა ფრეზი, სარეგულირებელო ქანჩი,
ზამბარა, 2 საკისარი, მიმღები ქილა, მისი სილიკონის რგოლი და ერთი ექვსწახნაგა ხრახნი — ბრტყელ
ზედაპირზე მკაცრი ნოლინგის წესითაა დალაგებული: ყოველი დეტალი კადრის კიდეების პარალელურად ან
პერპენდიკულარულად დევს, არაფერი ერთმანეთს არ ედება, მანძილი თანაბარია, დაჯგუფება კი ისეა, რომ
აწყობის თანმიმდევრობა ზედა მარცხნიდან ქვედა მარჯვნივ იკითხებოდეს. დეტალების ურთიერთმასშტაბი
რეალურია: კორპუსი კადრის ყველაზე დიდი საგანია, ხრახნი — ყველაზე პატარა.

ფონი: გლუვი, საშუალო ნაცრისფერი უწყვეტი ზედაპირი, ფაქტურის, მარცვლისა და ხილული კიდის გარეშე.

კამერა: პირდაპირ ზემოდან, სენსორი ზედაპირის ზუსტად პარალელურად — პერსპექტივის თანხვედრა არსად არ
ჩანს; 50 მმ ექვივალენტი, საკმარისად შორიდან, რომ კიდეებში დეტალები არ დამახინჯდეს; f/8,
ყველაფერი კიდიდან კიდემდე მკვეთრია.

განათება: ერთი დიდი სოფტბოქსი მაღლა, ზედაპირის ზედა მარცხენა მხარეს, კიდით მიმართული თანაბარი
დაფარვისთვის, პლუს თეთრი არეკვლის ფარი ქვედა მარჯვნივ. ყოველი დეტალი ერთი და იმავე სიგრძის მოკლე,
რბილ ჩრდილს აგდებს ერთი მიმართულებით — მარჯვნივ-ქვემოთ; არცერთი დეტალი მეორის ჩრდილში არ დევს.
ფოლადზე მკვეთრი შუქის ლაქა არ არის.

წარწერა სურათში, ზუსტად ასე დაწერილი: ღია ნაცრისფერი მაიუსკულური შრიფტი, კადრის სიმაღლის
დაახლოებით ორმოცდამეათედი; ყოველი იარლიყი თავისი დეტალის ქვემოთ დგას და მას თხელი მიმთითებელი
ხაზით უკავშირდება: „BODY“, „LID“, „CRANK“, „KNOB“, „SHAFT“, „TOP BURR“, „BOTTOM BURR“,
„ADJUSTMENT NUT“, „SPRING“, „BEARING“, „BEARING“, „CATCH JAR“, „SILICONE RING“, „SCREW“.
ქვედა ველში, ცენტრში, იარლიყის ორმაგი ზომით: „HAND COFFEE GRINDER · 14 PARTS“.
ოთხივე მხარეს თანაბარი, ცარიელი ველი დატოვე. ყოველი ასო მკვეთრი, სწორად დაწერილი და მთლიანად
კადრშია.
---
Photograph a hand coffee grinder completely taken apart and laid out flat, knolling style, with every part
labelled in the image. 4:5 vertical, rendered at 4K.
Subject and layout: all fourteen parts of a hand coffee grinder — the cylindrical steel body, the lid, the
crank handle, the handle knob, the central drive shaft, the top burr, the bottom burr, the adjustment nut,
the spring, two bearings, the catch jar, its silicone ring and one hex screw — are arranged on a flat
surface in strict knolling discipline: every part parallel or perpendicular to the frame edges, nothing
overlapping, even spacing, grouped so the assembly order reads from the top left to the bottom right. Keep
the parts at true relative scale to each other; the body is the largest object in the frame and the screw
the smallest.
Background: a smooth mid-grey seamless surface with no texture, no grain and no visible edge.
Camera: directly overhead, the sensor exactly parallel to the surface so there is no perspective
convergence anywhere, 50mm equivalent shot from far enough back that the edge parts are not distorted,
f/8, everything sharp corner to corner.
Light: one large softbox high on the upper left of the surface, feathered for even coverage, plus a white
bounce card on the lower right. Every part throws a short, soft shadow of the same length in the same
direction — toward the lower right — and no part sits in another part's shadow. No specular hotspot on
the steel.
Text in the image, spelled exactly as written here, all in a light grey uppercase sans-serif at roughly
one fiftieth of the frame height, each label placed just below its part and joined to it by a hairline
leader line: "BODY", "LID", "CRANK", "KNOB", "SHAFT", "TOP BURR", "BOTTOM BURR", "ADJUSTMENT NUT",
"SPRING", "BEARING", "BEARING", "CATCH JAR", "SILICONE RING", "SCREW". Across the bottom margin, centred,
at about twice the label size: "HAND COFFEE GRINDER · 14 PARTS". Leave an even, empty margin on all four
sides. Every letter sharp, correctly spelled and fully inside the frame.
```

---

### NB-16 · Labelled cross-section — a qvevri in the ground
`nano-banana` `gemini` — diagram, cross-section, georgian text

**EN**
```
Draw a labelled cross-section diagram showing how a qvevri sits in the ground of a marani and what
happens inside it during fermentation. 4:5 vertical. This is a technical illustration, not a
photograph.

The cut: the drawing plane slices straight through the earth and through the qvevri, so the vessel
is seen in half from the side, its interior fully open to the viewer. The qvevri is the classic
egg-tapering form, buried up to its neck, with only the rim and the stone lid above ground.

What the section shows, from the top of the frame down: the marani's packed earth floor with a
shallow drainage channel; the stone lid sealed with a ring of clay; the qvevri neck; inside the
vessel, the wine, drawn as a translucent amber body with the skins, stems and pips floating as a
darker cap in the upper third and a fine lees layer settled in the tapered base; small bubble
trails rising from the lees to the cap; the beeswax coating drawn as a thin line inside the clay
wall; the clay wall itself in section hatching; and the surrounding earth in three bands, coarse
sand packed directly against the vessel, then subsoil, then bedrock at the bottom edge.

Style: clean editorial technical cutaway, muted earth palette — terracotta, amber, sand, two greys
— thin uniform black outlines, section hatching at a consistent 45 degrees, no photographic
texture. Flat illustration lighting with a single implied source from the upper left giving each
solid one soft step of shading and no cast shadows at all.

Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, each label to
the side of the element it names and joined by a hairline leader line, all labels at the same size,
about one fortieth of the frame height:
"ქვის თავსახური", "თიხის სახურავი", "მარნის იატაკი", "ქვევრის ყელი", "დურდო", "ღვინო",
"მექანური ნალექი", "ცვილის ფენა", "თიხის კედელი", "ქვიშის ფენა", "გრუნტი", "კლდოვანი ფუძე",
"ნახშირორჟანგი", "მუდმივი ტემპერატურა 14 °C".
Across the top of the frame, centred, at about three times the label size: "ქვევრი მიწაში".
Leave an even margin on all four sides and keep every label clear of the drawing.

# Georgian letterforms will almost certainly come back needing repair, especially in the large
# heading — check the result letter by letter. The reliable route is to ask for the labels and the
# heading to be left out entirely ("leave every label area and the heading area empty") and to set
# the Georgian type over the diagram in a design tool.
```

**KA**
```
დახატე ჭრილის დიაგრამა, რომელიც აჩვენებს, როგორ ზის ქვევრი მარნის მიწაში და რა ხდება მის შიგნით
დუღილის დროს. ვერტიკალური კადრი 4:5. ეს ტექნიკური ილუსტრაციაა და არა ფოტო.

ჭრილი: ხატვის სიბრტყე მიწასაც და ქვევრსაც პირდაპირ კვეთს, ამიტომ ჭურჭელი გვერდიდან, ნახევრად
გადაჭრილი ჩანს და მისი შიგთავსი მაყურებლისთვის სრულად ღიაა. ქვევრი კლასიკური, კვერცხისებრი
ფორმისაა, ყელამდე მიწაშია ჩაფლული; მიწის ზემოთ მხოლოდ ყელი და ქვის თავსახური რჩება.

რას აჩვენებს ჭრილი, კადრის ზემოდან ქვემოთ: მარნის დატკეპნილი მიწის იატაკი არაღრმა სადრენაჟე
ღარით; ქვის თავსახური, თიხის რგოლით შელესილი; ქვევრის ყელი; ჭურჭლის შიგნით ღვინო — გამჭვირვალე
ქარვისფერი მასა, ზედა მესამედში კი მუქი „ქუდი“ კანის, კლერტისა და წიპწისგან; დავიწროებულ ძირზე
დაწოლილი წვრილი ნალექი; ნალექიდან ქუდისკენ ამავალი პატარა ბუშტების კვალი; თიხის კედლის შიგნიდან
ცვილის საფარი თხელი ხაზით; თიხის კედელი ჭრილის შტრიხით; და გარშემო მიწა 3 ზოლად — უშუალოდ
ჭურჭელზე მიტკეპნილი მსხვილი ქვიშა, შემდეგ გრუნტი, ქვედა კიდეზე კი კლდოვანი ფუძე.

სტილი: სუფთა სარედაქციო ტექნიკური ჭრილი, დაწყნარებული მიწის პალიტრა — ტერაკოტა, ქარვისფერი,
ქვიშისფერი და 2 ნაცრისფერი; თხელი, ერთგვაროვანი შავი კონტური; ჭრილის შტრიხი მუდმივად 45 გრადუსზე;
ფოტოგრაფიული ფაქტურის გარეშე. განათება ილუსტრაციულად ბრტყელია: ერთი ნაგულისხმევი წყარო ზედა
მარცხენა მხრიდან ყოველ სხეულს ერთ რბილ საფეხურს აძლევს; დაცემული ჩრდილი არსად არ არის.

წარწერა სურათში, ზუსტად ასე: მარტივი ქართული შრიფტი, ყოველი იარლიყი თავისი ელემენტის გვერდით
დგას და მას თხელი მიმთითებელი ხაზი უკავშირდება; ყველა იარლიყი ერთი ზომისაა, კადრის სიმაღლის
დაახლოებით მეორმოცედი:
„ქვის თავსახური“, „თიხის სახურავი“, „მარნის იატაკი“, „ქვევრის ყელი“, „დურდო“, „ღვინო“,
„მექანური ნალექი“, „ცვილის ფენა“, „თიხის კედელი“, „ქვიშის ფენა“, „გრუნტი“, „კლდოვანი ფუძე“,
„ნახშირორჟანგი“, „მუდმივი ტემპერატურა 14 °C“.
კადრის თავში, ცენტრში, იარლიყის სამმაგი ზომით: „ქვევრი მიწაში“.
ოთხივე მხარეს თანაბარი ველი დატოვე და არცერთი იარლიყი ნახატს არ შეაჭრა.

# ქართული ასოები დიდი ალბათობით შესასწორებელი გამოვა, განსაკუთრებით დიდ სათაურში — შედეგი ასოების
# დონეზე შეამოწმე. საიმედო გზაა, სთხოვო მოდელს, იარლიყებისა და სათაურის ადგილი სულ ცარიელი
# დატოვოს („leave every label area and the heading area empty“) და ქართული შრიფტი დიაგრამაზე
# დიზაინის პროგრამაში დაადო.
---
Draw a labelled cross-section diagram showing how a qvevri sits in the ground of a marani and what happens
inside it during fermentation. 4:5 vertical. This is a technical illustration, not a photograph.
The cut: the drawing plane slices straight through the earth and through the qvevri, so the vessel is seen
in half from the side, its interior fully open to the viewer. The qvevri is the classic egg-tapering form,
buried up to its neck, with only the rim and the stone lid above ground.
What the section shows, from the top of the frame down: the marani's packed earth floor with a shallow
drainage channel; the stone lid sealed with a ring of clay; the qvevri neck; inside the vessel, the wine
drawn as a translucent amber body with the skins, stems and pips floating as a darker cap in the upper
third and a fine lees layer settled in the tapered base; small bubble trails rising from the lees to the
cap; the beeswax coating drawn as a thin line inside the clay wall; the clay wall itself in section
hatching; and the surrounding earth in three bands — coarse sand packed against the vessel, then subsoil,
then bedrock at the bottom edge.
Style: clean editorial technical cutaway, muted earth palette — terracotta, amber, sand, two greys — thin
uniform black outlines, section hatching at a consistent 45 degrees, no photographic texture. Flat
illustration lighting with a single implied source from the upper left giving each solid one soft step of
shading and no cast shadows at all.
Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, each label to the side
of the element it names and joined by a hairline leader line, all labels at the same size, about one
fortieth of the frame height: "ქვის თავსახური", "თიხის სახურავი", "მარნის იატაკი", "ქვევრის ყელი",
"დურდო", "ღვინო", "მექანური ნალექი", "ცვილის ფენა", "თიხის კედელი", "ქვიშის ფენა", "გრუნტი",
"კლდოვანი ფუძე", "ნახშირორჟანგი", "მუდმივი ტემპერატურა 14 °C". Across the top of the frame, centred, at
about three times the label size: "ქვევრი მიწაში". Leave an even margin on all four sides and keep every
label clear of the drawing.
```

---

### NB-17 · Five-step process infographic with a reserved caption strip
`nano-banana` `gemini` — infographic, icons, georgian text

**EN**
```
Design a process infographic that explains how churchkhela is made, in five numbered steps. 4:5
vertical, rendered at 4K. This is a flat vector-style figure, not a photograph and not a
hand-drawn illustration.

Layout: five steps stacked as five equal horizontal bands running down the frame, each band the
same height, separated by a thin warm grey rule. In every band the same three zones repeat in the
same order and at the same widths: on the left a numbered disc about one third of the band height,
in the middle an icon in a circle of exactly the same diameter in every band, and on the right the
step label. Nothing in any band is larger or smaller than its counterpart in the other bands.

Icon language, identical across all five: a two-pixel-weight line icon, rounded caps, one single
accent colour, drawn inside a circle with a thin outline, no fills, no gradients, no shadows, all
five icons at exactly the same optical weight. Step 1 a grape bunch under a press, step 2 a pot
with a stirring paddle, step 3 a needle drawing thread through walnuts, step 4 a thread being
dipped into a pot, step 5 threads hanging from a horizontal rod.

Palette: warm off-white background, one deep grape-purple for the discs and the rules, one amber
accent for the icons, dark grey for the text.

Light: none simulated — this is a flat figure, so there are no cast shadows, no gradients, no
bevels and no highlights anywhere; every shape is a uniform fill.

Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, each label
vertically centred in its band, left aligned on a common baseline grid, all five labels at the same
size:
step 1 "ყურძნის დაწურვა", step 2 "ტატარას მოხარშვა", step 3 "კაკლის ასხმა ძაფზე",
step 4 "ტატარაში ჩაწობა", step 5 "გაშრობა ჩრდილში".
The numerals "1", "2", "3", "4", "5" sit inside the discs, in off-white, one per band.
Across the top, centred, at about twice the label size: "ჩურჩხელა 5 ნაბიჯად".

Reserve the bottom eighth of the frame as an empty caption strip: a flat band of the background
colour with nothing in it at all — no icon, no rule, no text, no texture — so a line of Georgian
type can be set there afterwards.

# Georgian labels will usually come back deformed at this size. Check every letter. The reliable
# route is to leave the text out of the render — ask for the label zones and the heading to stay
# empty ("leave the label column and the heading area blank") — and set the Georgian type over the
# figure in a design tool.
```

**KA**
```
შექმენი ინფოგრაფიკა, რომელიც ჩურჩხელის მომზადებას 5 დანომრილ ნაბიჯად ხსნის. ვერტიკალური კადრი
4:5, რენდერი 4K. ეს ბრტყელი, ვექტორული სტილის მაკეტია — არც ფოტო და არც ხელით ნახატი ილუსტრაცია.

მაკეტი: 5 ნაბიჯი კადრში ზემოდან ქვემოთ 5 თანაბარ ჰორიზონტალურ ზოლადაა დაწყობილი, ყოველი ზოლი
ერთი სიმაღლისაა და მათ შორის თხელი, თბილი ნაცრისფერი ხაზი გადის. ყოველ ზოლში ერთი და იგივე 3
ზონა მეორდება ერთი თანმიმდევრობითა და ერთი სიგანით: მარცხნივ დანომრილი წრე, ზოლის სიმაღლის
დაახლოებით მესამედი; შუაში იკონი წრეში, ყველა ზოლში ზუსტად ერთი დიამეტრით; მარჯვნივ ნაბიჯის
წარწერა. არცერთ ზოლში არცერთი ელემენტი სხვა ზოლის თავის შესატყვისზე დიდი ან პატარა არ არის.

იკონების ერთიანი ენა, ხუთივეში იდენტური: 2 პიქსელის სისქის ხაზოვანი იკონი, მომრგვალებული
ბოლოებით, ერთი აქცენტის ფერით, თხელკონტურიანი წრის შიგნით; შევსების, გრადიენტისა და ჩრდილის
გარეშე; ხუთივე იკონი ოპტიკურად ერთი წონისაა. ნაბიჯი 1 — ყურძნის მტევანი საწნახელის ქვეშ; ნაბიჯი
2 — ქვაბი და სარევი ნიჩაბი; ნაბიჯი 3 — ნემსი ძაფს კაკალში ატარებს; ნაბიჯი 4 — ძაფი ქვაბში
ჩაეშვება; ნაბიჯი 5 — ძაფები ჰორიზონტალურ ჭოკზე ჰკიდია.

პალიტრა: თბილი, მოთეთრო ფონი; ერთი ღრმა ყურძნისფერი წრეებისა და ხაზებისთვის; ერთი ქარვისფერი
აქცენტი იკონებისთვის; მუქი ნაცრისფერი ტექსტისთვის.

განათება: არ არის — ეს ბრტყელი მაკეტია, ამიტომ არსად არ არის დაცემული ჩრდილი, გრადიენტი,
მოცულობა და შუქის ლაქა; ყოველი ფორმა ერთგვაროვნად შევსებულია.

წარწერა სურათში, ზუსტად ასე: მარტივი ქართული შრიფტი; ყოველი წარწერა თავის ზოლში ვერტიკალურად
ცენტრშია, მარცხენა კიდეზე გასწორებული ერთი საერთო ბადის მიხედვით; ხუთივე წარწერა ერთი ზომისაა:
ნაბიჯი 1 — „ყურძნის დაწურვა“, ნაბიჯი 2 — „ტატარას მოხარშვა“, ნაბიჯი 3 — „კაკლის ასხმა ძაფზე“,
ნაბიჯი 4 — „ტატარაში ჩაწობა“, ნაბიჯი 5 — „გაშრობა ჩრდილში“.
ციფრები „1“, „2“, „3“, „4“, „5“ წრეების შიგნითაა, მოთეთრო ფერში, ზოლზე თითო.
კადრის თავში, ცენტრში, წარწერის ორმაგი ზომით: „ჩურჩხელა 5 ნაბიჯად“.

კადრის ქვედა მერვედი დატოვე ცარიელ წარწერის ზოლად: ფონის ფერის ბრტყელი ზოლი, რომელშიც სრულიად
არაფერია — არც იკონი, არც ხაზი, არც ტექსტი, არც ფაქტურა — რომ იქ შემდეგ ქართული ტექსტის ერთი
ხაზი დაიდოს.

# ამ ზომაში ქართული წარწერა ჩვეულებრივ დამახინჯებული გამოვა. შეამოწმე ყოველი ასო. საიმედო გზაა,
# ტექსტი საერთოდ არ ჩააგდებინო რენდერში — სთხოვე, წარწერების სვეტი და სათაურის ადგილი ცარიელი
# დატოვოს („leave the label column and the heading area blank“) — და ქართული შრიფტი მაკეტზე
# დიზაინის პროგრამაში დაადო.
---
Design a process infographic that explains how churchkhela is made, in five numbered steps. 4:5 vertical,
rendered at 4K. This is a flat vector-style figure, not a photograph and not a hand-drawn illustration.
Layout: five steps stacked as five equal horizontal bands running down the frame, each band the same
height, separated by a thin warm grey rule. In every band the same three zones repeat in the same order
and at the same widths: on the left a numbered disc about one third of the band height, in the middle an
icon in a circle of exactly the same diameter in every band, and on the right the step label. Nothing in
any band is larger or smaller than its counterpart in the other bands.
Icon language, identical across all five: a two-pixel-weight line icon, rounded caps, one single accent
colour, drawn inside a circle with a thin outline, no fills, no gradients, no shadows, all five icons at
exactly the same optical weight. Step 1 a grape bunch under a press, step 2 a pot with a stirring paddle,
step 3 a needle drawing thread through walnuts, step 4 a thread being dipped into a pot, step 5 threads
hanging from a horizontal rod.
Palette: warm off-white background, one deep grape-purple for the discs and the rules, one amber accent
for the icons, dark grey for the text.
Light: none simulated — this is a flat figure, so there are no cast shadows, no gradients, no bevels and
no highlights anywhere; every shape is a uniform fill.
Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, each label vertically
centred in its band, left aligned on a common baseline grid, all five labels at the same size: step 1
"ყურძნის დაწურვა", step 2 "ტატარას მოხარშვა", step 3 "კაკლის ასხმა ძაფზე", step 4 "ტატარაში ჩაწობა",
step 5 "გაშრობა ჩრდილში". The numerals "1", "2", "3", "4", "5" sit inside the discs, in off-white, one
per band. Across the top, centred, at about twice the label size: "ჩურჩხელა 5 ნაბიჯად".
Reserve the bottom eighth of the frame as an empty caption strip: a flat band of the background colour
with nothing in it at all — no icon, no rule, no text, no texture — so a line of Georgian type can be set
there afterwards.
```

---

### NB-18 · Comparison figure with a shared scale and a legend
`nano-banana` `gemini` — diagram, comparison, in-image text

**EN**
```
Draw a comparison figure that puts two vine training systems side by side at the same scale so a
reader can see the difference in one look. 16:9 horizontal, rendered at 4K. Editorial technical
illustration, not a photograph.

Structure: one shared horizontal soil line runs across the lower fifth of the frame, unbroken from
edge to edge, and both variants stand on it. A single vertical scale bar sits exactly on the centre
axis, shared by both sides, with tick marks at zero, two, four and six metres and a hairline
gridline running from each tick out to both the left and the right edge, in pale grey behind the
drawings.

Left half — a traditional tree-trained vine: an old trunk rising against a mature tree, the canes
carried up into the crown so the fruiting zone sits between four and six metres on the shared
scale. Right half — a wire trellis: three evenly spaced posts with four horizontal wires, a short
trunk and a single fruiting wire, the fruiting zone sitting between one and one and a half metres
on the same scale. Both variants are drawn at identical line weight, in the same palette, with the
same level of detail, so neither reads as the preferred option.

Colour: warm off-white ground, two greens for the foliage — one for permanent wood, one for the
one-year canes — and one muted red for the fruiting zone. Nothing else is coloured.

Light: flat illustration lighting with a single implied sun from the upper left giving the foliage
masses one soft step of shading; no cast shadows on the ground and no gradients.

Text in the image, spelled exactly as written here, all in a dark grey sans-serif:
- across the top, centred, the largest text in the figure: "TWO WAYS TO TRAIN A VINE"
- above each half, centred over it, at about half the headline size: "MAGLARI · TREE-TRAINED" on
  the left and "VSP · WIRE TRELLIS" on the right
- beside the scale bar ticks, small, right aligned to the bar: "0 m", "2 m", "4 m", "6 m"
- a legend box in the lower left corner, one hairline outline, three colour swatches stacked with a
  label beside each, at the same size as the tick labels: "permanent wood", "one-year cane",
  "fruiting zone"
- lower right corner, the same size as the legend text: "same scale, same soil line"

Even margins on all four sides; no label overlaps a drawing; every letter sharp and correctly
spelled.
```

**KA**
```
დახატე შედარების სქემა, რომელიც ვაზის 2 წამოყვანის სისტემას ერთ მასშტაბში, გვერდიგვერდ აჩვენებს,
რომ განსხვავება ერთი შეხედვით ჩანდეს. ჰორიზონტალური კადრი 16:9, რენდერი 4K. სარედაქციო ტექნიკური
ილუსტრაცია და არა ფოტო.

სტრუქტურა: კადრის ქვედა მეხუთედში ერთი საერთო ჰორიზონტალური მიწის ხაზი გადის, კიდიდან კიდემდე
გაუწყვეტლად, და ორივე ვარიანტი მასზე დგას. ზუსტად ცენტრალურ ღერძზე დგას ერთი ვერტიკალური
მასშტაბის სკალა, ორივე მხარისთვის საერთო; მასზე ნულის, 2, 4 და 6 მეტრის დანაყოფებია და ყოველი
დანაყოფიდან თხელი ღია ნაცრისფერი ხაზი მიდის მარცხენა და მარჯვენა კიდემდე, ნახატების უკან.

მარცხენა ნახევარი — ტრადიციული მაღლარი: ძველი ღერო ხეს აუყვება, რქები გვირგვინში ადის და მსხმოიარე
ზონა საერთო სკალაზე 4-დან 6 მეტრამდე ზის. მარჯვენა ნახევარი — მავთულის შპალერი: 3 თანაბრად
დაშორებული ბოძი, 4 ჰორიზონტალური მავთული, დაბალი ღერო და ერთი მსხმოიარე მავთული; მსხმოიარე ზონა
იმავე სკალაზე 1-დან 1,5 მეტრამდეა. ორივე ვარიანტი ერთი სისქის ხაზით, ერთ პალიტრაში და ერთი
დეტალიზაციით იხატება, რომ არცერთი უკეთეს ვარიანტად არ იკითხებოდეს.

ფერი: თბილი, მოთეთრო ფონი; ფოთლისთვის 2 მწვანე — ერთი მრავალწლიანი მერქნისთვის, მეორე ერთწლიანი
რქებისთვის; და ერთი დაწყნარებული წითელი მსხმოიარე ზონისთვის. სხვა არაფერია ფერადი.

განათება: ილუსტრაციულად ბრტყელი; ერთი ნაგულისხმევი მზე ზედა მარცხენა მხრიდან ფოთლის მასებს ერთ
რბილ საფეხურს აძლევს; მიწაზე დაცემული ჩრდილი და გრადიენტი არ არის.

წარწერა სურათში, ზუსტად ასე, მუქი ნაცრისფერი შრიფტით:
- კადრის თავში, ცენტრში, სქემის ყველაზე დიდი ტექსტი: „TWO WAYS TO TRAIN A VINE“
- ყოველი ნახევრის თავზე, მის ცენტრში, სათაურის დაახლოებით ნახევარი ზომით: მარცხნივ
  „MAGLARI · TREE-TRAINED“, მარჯვნივ „VSP · WIRE TRELLIS“
- სკალის დანაყოფებთან, წვრილად, სკალაზე მარჯვნივ გასწორებული: „0 m“, „2 m“, „4 m“, „6 m“
- ლეგენდის ჩარჩო ქვედა მარცხენა კუთხეში, ერთი თხელი კონტურით, 3 ფერის ნიმუში ერთმანეთის ქვეშ და
  თითოეულის გვერდით წარწერა, დანაყოფების ზომით: „permanent wood“, „one-year cane“, „fruiting zone“
- ქვედა მარჯვენა კუთხეში, ლეგენდის ზომით: „same scale, same soil line“

ოთხივე მხარეს თანაბარი ველი; არცერთი წარწერა ნახატს არ ედება; ყოველი ასო მკვეთრი და სწორად
დაწერილია.
---
Draw a comparison figure that puts two vine training systems side by side at the same scale so a reader
can see the difference in one look. 16:9 horizontal, rendered at 4K. Editorial technical illustration,
not a photograph.
Structure: one shared horizontal soil line runs across the lower fifth of the frame, unbroken from edge to
edge, and both variants stand on it. A single vertical scale bar sits exactly on the centre axis, shared
by both sides, with tick marks at zero, two, four and six metres and a hairline gridline running from each
tick out to both edges, in pale grey behind the drawings.
Left half — a traditional tree-trained vine: an old trunk rising against a mature tree, the canes carried
up into the crown so the fruiting zone sits between four and six metres on the shared scale. Right half —
a wire trellis: three evenly spaced posts with four horizontal wires, a short trunk and a single fruiting
wire, the fruiting zone sitting between one and one and a half metres on the same scale. Both variants are
drawn at identical line weight, in the same palette, with the same level of detail, so neither reads as
the preferred option.
Colour: warm off-white ground, two greens for the foliage — one for permanent wood, one for the one-year
canes — and one muted red for the fruiting zone. Nothing else is coloured.
Light: flat illustration lighting with a single implied sun from the upper left giving the foliage masses
one soft step of shading; no cast shadows on the ground and no gradients.
Text in the image, spelled exactly as written here, all in a dark grey sans-serif: across the top, centred,
the largest text in the figure, "TWO WAYS TO TRAIN A VINE"; above each half, centred over it, at about
half the headline size, "MAGLARI · TREE-TRAINED" on the left and "VSP · WIRE TRELLIS" on the right; beside
the scale bar ticks, small, right aligned to the bar, "0 m", "2 m", "4 m", "6 m"; a legend box in the
lower left corner with one hairline outline and three colour swatches stacked with a label beside each, at
tick-label size, "permanent wood", "one-year cane", "fruiting zone"; lower right corner, the same size as
the legend text, "same scale, same soil line".
Even margins on all four sides; no label overlaps a drawing; every letter sharp and correctly spelled.
```

---

### NB-19 · Presentation title slide with room for a logo
`nano-banana` `gemini` — slide, typography, georgian text

**EN**
```
Design a presentation title slide. 16:9 horizontal, rendered at 4K, composed to be projected in a
lit meeting room, so contrast must hold up when the projector washes it out.

Background: a single deep indigo field with a slow, even gradient that lightens very slightly
toward the lower right. One quiet graphic element only — a set of five thin diagonal lines in a
lighter indigo, entering from the bottom right corner at forty-five degrees and stopping before
they reach the middle of the frame. No photograph, no texture, no vignette, nothing behind the
type.

Layout: the type block sits on the left, its left edge on a margin one twelfth of the frame width
in from the edge, vertically centred as a block. Above it, in the top left, leave an empty square
area whose side is about three times the height of the subhead line, completely clean — no line, no
gradient step, no graphic element crossing it — reserved for a logo that will be placed later.
Keep the entire right third of the frame free of type.

Light: none simulated — this is a flat graphic, so no shadows, no glow behind the letters, no
bevel and no highlight anywhere.

Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, flush left on a
shared left edge:
- the headline, the largest element on the slide, warm white, set on one line:
  "წლიური შედეგები 2026"
- directly beneath it, about one third of the headline height, in a muted warm grey:
  "გაყიდვები, გუნდი და გეგმა მომდევნო წლისთვის"
- in the bottom left corner, the smallest text on the slide, the same grey:
  "შიდა შეხვედრა · 12 თებერვალი"

Every line fully inside the frame, evenly spaced, with generous air between the headline block and
the bottom line.

SECOND TURN — reuse the slide for another talk
Keep the background, the gradient, the diagonal lines, the margins, the logo area, the type
positions, the sizes, the colours and the 16:9 frame exactly as they are. Change only the headline
string to "ახალი ბაზრები 2027" and the bottom line to "შიდა შეხვედრა · 9 ივნისი". The subhead
does not change. Do not redraw the background and do not re-space the layout.

# Georgian letterforms rarely survive a render at headline size. Check the result letter by letter.
# The reliable route is to ask for the slide with no text at all ("leave the type area completely
# empty") and to set the Georgian type in a design tool — the composition above is already built
# around that, since the type block sits on flat colour.
```

**KA**
```
შექმენი პრეზენტაციის სატიტულო სლაიდი. ჰორიზონტალური კადრი 16:9, რენდერი 4K, განათებულ სხდომათა
ოთახში საჩვენებლად — კონტრასტმა პროექტორზეც უნდა გაუძლოს.

ფონი: ერთი ღრმა ინდიგოს ველი, ნელი და თანაბარი გრადიენტით, რომელიც მარჯვნივ-ქვემოთ ოდნავ ნათდება.
მხოლოდ ერთი წყნარი გრაფიკული ელემენტი — 5 თხელი დიაგონალური ხაზი უფრო ღია ინდიგოში, რომელიც ქვედა
მარჯვენა კუთხიდან 45 გრადუსით შემოდის და კადრის შუამდე ვერ აღწევს. ფოტო, ფაქტურა, ვინიეტი და
ტექსტის უკანა დეკორი არ არის.

მაკეტი: ტექსტის ბლოკი მარცხნივ ზის, მისი მარცხენა კიდე კადრის სიგანის მეთორმეტედით შემოწეულ ველზე;
ბლოკი ვერტიკალურად ცენტრშია. მის ზემოთ, ზედა მარცხენა კუთხეში, დატოვე ცარიელი კვადრატული ველი,
რომლის გვერდი ქვესათაურის სიმაღლეს დაახლოებით 3-ჯერ აღემატება — სრულიად სუფთა, ხაზის, გრადიენტის
საფეხურისა და გრაფიკული ელემენტის გარეშე; ეს ლოგოს ადგილია და ლოგო შემდეგ დაიდება. კადრის მთელი
მარჯვენა მესამედი ტექსტისგან თავისუფალი რჩება.

განათება: არ არის — ეს ბრტყელი გრაფიკაა, ამიტომ არსად არ არის ჩრდილი, ასოების უკან ნათება,
მოცულობა და შუქის ლაქა.

წარწერა სურათში, ზუსტად ასე, მარტივი ქართული შრიფტით, ერთ საერთო მარცხენა კიდეზე გასწორებული:
- სათაური, სლაიდის ყველაზე დიდი ელემენტი, თბილ თეთრში, ერთ ხაზად: „წლიური შედეგები 2026“
- პირდაპირ მის ქვეშ, სათაურის სიმაღლის დაახლოებით მესამედი, დაწყნარებულ თბილ ნაცრისფერში:
  „გაყიდვები, გუნდი და გეგმა მომდევნო წლისთვის“
- ქვედა მარცხენა კუთხეში, სლაიდის ყველაზე პატარა ტექსტი, იმავე ნაცრისფერში:
  „შიდა შეხვედრა · 12 თებერვალი“

ყოველი ხაზი მთლიანად კადრშია, თანაბარი ინტერვალით; სათაურის ბლოკსა და ქვედა ხაზს შორის ბევრი
თავისუფალი ჰაერი რჩება.

მეორე ეტაპი — იგივე სლაიდი სხვა შეხვედრისთვის
ფონი, გრადიენტი, დიაგონალური ხაზები, ველები, ლოგოს ადგილი, ტექსტის პოზიციები, ზომები, ფერები და
პროპორცია 16:9 ზუსტად უცვლელი რჩება. შეიცვალოს მხოლოდ სათაური — „ახალი ბაზრები 2027“ — და ქვედა
ხაზი — „შიდა შეხვედრა · 9 ივნისი“. ქვესათაური არ იცვლება. ფონი ხელახლა არ დაარენდერო და მაკეტი
თავიდან არ დააწყო.

# სათაურის ზომაში ქართული ასოები იშვიათად გამოდის სწორი. შედეგი ასოების დონეზე შეამოწმე. საიმედო
# გზაა, სლაიდი საერთოდ ტექსტის გარეშე ითხოვო („leave the type area completely empty“) და ქართული
# შრიფტი დიზაინის პროგრამაში დაადო — კომპოზიცია სწორედ ამაზეა აწყობილი, რადგან ტექსტის ბლოკი
# ბრტყელ ფერზე ზის.
---
Design a presentation title slide. 16:9 horizontal, rendered at 4K, composed to be projected in a lit
meeting room, so contrast must hold up when the projector washes it out.
Background: a single deep indigo field with a slow, even gradient that lightens very slightly toward the
lower right. One quiet graphic element only — five thin diagonal lines in a lighter indigo, entering from
the bottom right corner at forty-five degrees and stopping before they reach the middle of the frame. No
photograph, no texture, no vignette, nothing behind the type.
Layout: the type block sits on the left, its left edge on a margin one twelfth of the frame width in from
the edge, vertically centred as a block. Above it, in the top left, leave an empty square area whose side
is about three times the height of the subhead line, completely clean — no line, no gradient step, no
graphic element crossing it — reserved for a logo that will be placed later. Keep the entire right third
of the frame free of type.
Light: none simulated — this is a flat graphic, so no shadows, no glow behind the letters, no bevel and no
highlight anywhere.
Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, flush left on a shared
left edge: the headline, the largest element on the slide, warm white, on one line,
"წლიური შედეგები 2026"; directly beneath it, about one third of the headline height, in a muted warm grey,
"გაყიდვები, გუნდი და გეგმა მომდევნო წლისთვის"; in the bottom left corner, the smallest text on the slide,
the same grey, "შიდა შეხვედრა · 12 თებერვალი".
Every line fully inside the frame, evenly spaced, with generous air between the headline block and the
bottom line.
SECOND TURN — reuse the slide for another talk. Keep the background, the gradient, the diagonal lines, the
margins, the logo area, the type positions, the sizes, the colours and the 16:9 frame exactly as they are.
Change only the headline string to "ახალი ბაზრები 2027" and the bottom line to "შიდა შეხვედრა · 9 ივნისი".
The subhead does not change. Do not redraw the background and do not re-space the layout.
```

---

### NB-20 · Organisation chart as a clean vector figure
`nano-banana` `gemini` — diagram, org chart, georgian text

**EN**
```
Draw the organisation chart of a Tbilisi logistics company as a clean vector figure. 16:9
horizontal, rendered at 4K. Flat diagram, not an illustration and not a photograph.

Structure: four levels, read top to bottom, connected by orthogonal elbow connectors that leave the
bottom edge of a box, drop, turn once at ninety degrees and enter the top edge of the box below.
Connectors never cross a box and never cross each other.

- Level 1: one box, centred on the horizontal axis of the frame, in the top eighth.
- Level 2: three boxes of equal width, evenly spaced across the frame, each hanging from a shared
  horizontal spine below the level 1 box.
- Level 3: under the left level 2 box, three boxes; under the middle one, two boxes; under the
  right one, two boxes. All level 3 boxes are the same width and sit on the same baseline.
- One detached box on the far right at level 2 height, joined to the level 1 box by a dashed
  connector — it is an external adviser, not a reporting line.

Box style: uniform width at each level, a consistent corner radius, a one-pixel outline, and a
solid fill that darkens by one step per level — the palest fill at level 3, the darkest at level 1.
The dashed external box has no fill, only an outline. Text is dark grey in the pale boxes and warm
white in the darkest box. Every box is vertically centred on its label and has the same internal
padding.

Light: none simulated — this is a flat vector figure, so there are no shadows, gradients, bevels or
highlights anywhere, and every fill is uniform.

Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, centred in each
box, all level 2 and level 3 labels at the same size and the level 1 label about a third larger:
- level 1: "გენერალური დირექტორი"
- level 2, left to right: "ოპერაციები", "გაყიდვები და მარკეტინგი", "ფინანსები და HR"
- level 3, under "ოპერაციები": "საწყობი", "ტრანსპორტი", "კლიენტების მხარდაჭერა"
- level 3, under "გაყიდვები და მარკეტინგი": "კორპორატიული გაყიდვები", "ონლაინ არხები"
- level 3, under "ფინანსები და HR": "ბუღალტერია", "რეკრუტინგი"
- the dashed box: "გარე იურისტი"
Across the top left corner, outside the chart, at the level 1 label size: "შპს ალაზანი ლოჯისტიკა"

Even margins on all four sides, no label breaking onto a second line unless the box is too narrow,
and no text touching a box edge.

# Georgian in small boxes comes back deformed more often than not. Check every box. The reliable
# route is to ask for the chart with empty boxes ("draw every box empty, with no text inside") and
# to set the Georgian labels over it in a design tool.
```

**KA**
```
დახატე თბილისური სატრანსპორტო კომპანიის ორგანიზაციული სტრუქტურის დიაგრამა სუფთა ვექტორულ
მაკეტად. ჰორიზონტალური კადრი 16:9, რენდერი 4K. ბრტყელი დიაგრამა — არც ილუსტრაცია და არც ფოტო.

სტრუქტურა: 4 დონე, ზემოდან ქვემოთ იკითხება, ერთმანეთს კი სწორკუთხა მაკავშირებლები აერთებს —
ხაზი ყუთის ქვედა კიდიდან გამოდის, ეშვება, ერთხელ ეხვევა 90 გრადუსით და ქვედა ყუთის ზედა კიდეში
შედის. მაკავშირებელი არც ყუთს კვეთს და არც სხვა მაკავშირებელს.

- დონე 1: ერთი ყუთი, კადრის ჰორიზონტალურ ცენტრში, ზედა მერვედში.
- დონე 2: 3 თანაბარი სიგანის ყუთი, კადრზე თანაბრად გადანაწილებული; სამივე პირველი დონის ყუთის
  ქვეშ გავლებულ საერთო ჰორიზონტალურ ხაზს ჰკიდია.
- დონე 3: მარცხენა მეორე დონის ყუთის ქვეშ — 3 ყუთი; შუას ქვეშ — 2; მარჯვენას ქვეშ — 2. მესამე
  დონის ყველა ყუთი ერთი სიგანისაა და ერთ ხაზზე ზის.
- მეორე დონის სიმაღლეზე, მარჯვენა კიდეში, ერთი ცალკე მდგომი ყუთი, რომელიც პირველი დონის ყუთს
  წყვეტილი ხაზით უკავშირდება — ეს გარე მრჩეველია და არა დაქვემდებარების ხაზი.

ყუთის სტილი: ყოველ დონეზე ერთი სიგანე, ერთი და იგივე კუთხის რადიუსი, 1 პიქსელის კონტური და
ერთგვაროვანი შევსება, რომელიც დონეზე ერთი საფეხურით მუქდება — ყველაზე ღია მესამე დონეზეა, ყველაზე
მუქი პირველზე. წყვეტილხაზიან ყუთს შევსება არ აქვს, მხოლოდ კონტური. ტექსტი ღია ყუთებში მუქი
ნაცრისფერია, ყველაზე მუქ ყუთში — თბილი თეთრი. ყოველი ყუთი თავის წარწერაზე ვერტიკალურად
ცენტრირებულია და ერთი და იგივე შიდა ველი აქვს.

განათება: არ არის — ეს ბრტყელი ვექტორული მაკეტია, ამიტომ არსად არ არის ჩრდილი, გრადიენტი,
მოცულობა და შუქის ლაქა; ყოველი შევსება ერთგვაროვანია.

წარწერა სურათში, ზუსტად ასე, მარტივი ქართული შრიფტით, ყოველ ყუთში ცენტრში; მეორე და მესამე დონის
ყველა წარწერა ერთი ზომისაა, პირველი დონისა კი დაახლოებით მესამედით დიდი:
- დონე 1: „გენერალური დირექტორი“
- დონე 2, მარცხნიდან მარჯვნივ: „ოპერაციები“, „გაყიდვები და მარკეტინგი“, „ფინანსები და HR“
- დონე 3, „ოპერაციების“ ქვეშ: „საწყობი“, „ტრანსპორტი“, „კლიენტების მხარდაჭერა“
- დონე 3, „გაყიდვები და მარკეტინგის“ ქვეშ: „კორპორატიული გაყიდვები“, „ონლაინ არხები“
- დონე 3, „ფინანსები და HR“-ის ქვეშ: „ბუღალტერია“, „რეკრუტინგი“
- წყვეტილხაზიანი ყუთი: „გარე იურისტი“
ზედა მარცხენა კუთხეში, დიაგრამის გარეთ, პირველი დონის წარწერის ზომით: „შპს ალაზანი ლოჯისტიკა“

ოთხივე მხარეს თანაბარი ველი; წარწერა მეორე ხაზზე არ გადადის, თუ ყუთი საკმარისად განიერია; ტექსტი
ყუთის კიდეს არსად არ ეხება.

# პატარა ყუთებში ქართული უფრო ხშირად გამოდის დამახინჯებული, ვიდრე სწორი. ყოველი ყუთი შეამოწმე.
# საიმედო გზაა, დიაგრამა ცარიელი ყუთებით ითხოვო („draw every box empty, with no text inside“) და
# ქართული წარწერები ზემოდან, დიზაინის პროგრამაში დაადო.
---
Draw the organisation chart of a Tbilisi logistics company as a clean vector figure. 16:9 horizontal,
rendered at 4K. Flat diagram, not an illustration and not a photograph.
Structure: four levels, read top to bottom, connected by orthogonal elbow connectors that leave the bottom
edge of a box, drop, turn once at ninety degrees and enter the top edge of the box below. Connectors never
cross a box and never cross each other. Level 1: one box, centred on the horizontal axis of the frame, in
the top eighth. Level 2: three boxes of equal width, evenly spaced across the frame, each hanging from a
shared horizontal spine below the level 1 box. Level 3: under the left level 2 box, three boxes; under the
middle one, two boxes; under the right one, two boxes — all the same width, all on the same baseline. One
detached box on the far right at level 2 height, joined to the level 1 box by a dashed connector — an
external adviser, not a reporting line.
Box style: uniform width at each level, a consistent corner radius, a one-pixel outline, and a solid fill
that darkens by one step per level — palest at level 3, darkest at level 1. The dashed external box has no
fill, only an outline. Text is dark grey in the pale boxes and warm white in the darkest box. Every box is
vertically centred on its label and has the same internal padding.
Light: none simulated — this is a flat vector figure, so there are no shadows, gradients, bevels or
highlights anywhere, and every fill is uniform.
Text in the image, spelled exactly as written here, in a plain Georgian sans-serif, centred in each box,
all level 2 and level 3 labels at the same size and the level 1 label about a third larger — level 1:
"გენერალური დირექტორი"; level 2, left to right: "ოპერაციები", "გაყიდვები და მარკეტინგი",
"ფინანსები და HR"; level 3 under "ოპერაციები": "საწყობი", "ტრანსპორტი", "კლიენტების მხარდაჭერა"; level 3
under "გაყიდვები და მარკეტინგი": "კორპორატიული გაყიდვები", "ონლაინ არხები"; level 3 under
"ფინანსები და HR": "ბუღალტერია", "რეკრუტინგი"; the dashed box: "გარე იურისტი". Across the top left
corner, outside the chart, at the level 1 label size: "შპს ალაზანი ლოჯისტიკა".
Even margins on all four sides, no label breaking onto a second line unless the box is too narrow, and no
text touching a box edge.
```

---

### NB-21 · Whiteboard planning sketch, photographed at an angle
`nano-banana` `gemini` — whiteboard, in-image text, editing

**EN**
```
Photograph a planning whiteboard in a small office, shot from an angle so it reads as a real board
in a real room rather than a flat graphic. 3:2 horizontal, rendered at 4K. Every word on the board
must be legible.

Subject: a wall-mounted white magnetic whiteboard about two metres wide, its aluminium tray holding
three dry-wipe markers and an eraser. The board carries a hand-drawn plan in black and blue marker:
a title at the top left, a thick horizontal rule under it, and three columns divided by two vertical
lines drawn slightly out of true, as hand-drawn lines are. Sticky notes are pressed onto the board
inside the columns — two yellow in the first column, two pink in the second, one blue in the third
— each slightly crooked, each with one short line of handwriting on it, one note peeling a little at
its lower corner.

Composition: the board fills most of the frame but is seen from the left, so its near left edge is
taller in frame than its far right edge and the board's horizontal lines converge gently to the
right. The wall and a sliver of the room show along the top and right. Nothing obscures the writing.

Camera: standing eye level, about two metres from the board and about one metre to the left of its
centre, 35mm equivalent, so the board sits at roughly twenty-five degrees to the sensor plane, f/5.6
with the focus set on the middle column so the whole board stays within the depth of field.

Light: soft daylight from a window out of frame on the camera's left, plus flat overhead office
light. The camera's angle is chosen so neither source puts a specular glare patch on the board; the
left edge of the board is a touch brighter than the right, and the sticky notes cast very short soft
shadows down and to the right.

Text in the image, in believable handwritten marker, spelled exactly as written here:
- top left, the largest writing on the board, black: "Q3 LAUNCH"
- the three column headings, black, about half that size: "NOW", "NEXT", "LATER"
- yellow notes under "NOW", in blue: "pricing page" and "beta invites"
- pink notes under "NEXT", in blue: "press kit" and "onboarding email"
- blue note under "LATER", in black: "partner API"
- bottom right of the board, the smallest writing, black: "review fri 14:00"
A hand-drawn arrow in black curves from the "beta invites" note to the "onboarding email" note. No
other writing on the board — no stray marks, no half-erased ghosting of other words.

SECOND TURN — change one note only
Keep the board, the room, the camera position, the angle, the focal length, the crop, the 3:2 frame,
the light, the markers in the tray, the arrow, the column headings, the title, the rules and every
other note exactly as they are, including each note's colour, position and slight crookedness.
Change exactly one thing: the note reading "partner API" now reads "partner API v2" in the same
black handwriting, on the same note, at a size that still fits inside it. Do not re-photograph the
board, do not relight it and do not redraw any other handwriting.
```

**KA**
```
გადაიღე დაგეგმვის თეთრი დაფა პატარა ოფისში, კუთხიდან — ისე, რომ ნამდვილ ოთახში მდგარ ნამდვილ
დაფად იკითხებოდეს და არა ბრტყელ გრაფიკად. ჰორიზონტალური კადრი 3:2, რენდერი 4K. დაფაზე ყოველი
სიტყვა იკითხება.

ობიექტი: კედელზე დამაგრებული თეთრი მაგნიტური დაფა, დაახლოებით 2 მეტრის სიგანის; ალუმინის თაროზე
3 მარკერი და საშლელი დევს. დაფაზე შავი და ლურჯი მარკერით ხელით დახატული გეგმაა: ზედა მარცხნივ
სათაური, მის ქვეშ სქელი ჰორიზონტალური ხაზი და 3 სვეტი, რომელთაც 2 ვერტიკალური, ოდნავ არასწორი
ხაზი ჰყოფს — ისე, როგორც ხელით გავლებული ხაზი გამოდის. სვეტებში დაფაზე სტიკერებია მიკრული — პირველ
სვეტში 2 ყვითელი, მეორეში 2 ვარდისფერი, მესამეში 1 ლურჯი — თითოეული ოდნავ ირიბად, თითოეულზე
ხელნაწერის ერთი მოკლე ხაზი; ერთ სტიკერს ქვედა კუთხე ოდნავ აშლია.

კომპოზიცია: დაფა კადრის დიდ ნაწილს ავსებს, მაგრამ მარცხნიდან ჩანს — ახლო მარცხენა კიდე კადრში
უფრო მაღალია, ვიდრე შორეული მარჯვენა, დაფის ჰორიზონტალური ხაზები კი მარჯვნივ ნაზად იყრება.
ზემოთ და მარჯვნივ კედელი და ოთახის ვიწრო ზოლი ჩანს. ტექსტს არაფერი ფარავს.

კამერა: მდგომი ადამიანის თვალის დონეზე, დაფიდან დაახლოებით 2 მეტრზე და მისი ცენტრიდან დაახლოებით
1 მეტრით მარცხნივ, 35 მმ ექვივალენტი — დაფა სენსორის სიბრტყესთან დაახლოებით 25 გრადუსის კუთხეშია;
f/5.6, ფოკუსი შუა სვეტზე, მთელი დაფა სიღრმის ველში რჩება.

განათება: რბილი დღის შუქი კადრს გარეთ, კამერის მარცხნივ მდებარე ფანჯრიდან, პლუს ოფისის ბრტყელი
ჭერის შუქი. კამერის კუთხე ისეა შერჩეული, რომ არცერთი წყარო დაფაზე მკვეთრ ბზინვის ლაქას არ აჩენს;
დაფის მარცხენა კიდე მარჯვენაზე ოდნავ ნათელია, სტიკერები კი ძალიან მოკლე, რბილ ჩრდილს აგდებს
ქვემოთ და მარჯვნივ.

წარწერა სურათში, დამაჯერებელი ხელნაწერი მარკერით, ზუსტად ასე:
- ზედა მარცხნივ, დაფის ყველაზე დიდი წარწერა, შავში: „Q3 LAUNCH“
- 3 სვეტის სათაური, შავში, ამ ზომის დაახლოებით ნახევარი: „NOW“, „NEXT“, „LATER“
- ყვითელი სტიკერები „NOW“-ს ქვეშ, ლურჯად: „pricing page“ და „beta invites“
- ვარდისფერი სტიკერები „NEXT“-ის ქვეშ, ლურჯად: „press kit“ და „onboarding email“
- ლურჯი სტიკერი „LATER“-ის ქვეშ, შავად: „partner API“
- დაფის ქვედა მარჯვენა მხარეს, ყველაზე პატარა წარწერა, შავში: „review fri 14:00“
შავი, ხელით გავლებული ისარი „beta invites“-იდან „onboarding email“-ისკენ იხრება. დაფაზე სხვა
წარწერა არ არის — არც შემთხვევითი შტრიხი და არც ნახევრად წაშლილი სიტყვების კვალი.

მეორე ეტაპი — შეცვალე მხოლოდ ერთი სტიკერი
დაფა, ოთახი, კამერის ადგილი, კუთხე, ფოკუსური მანძილი, კადრირება, პროპორცია 3:2, განათება, თაროზე
მდგარი მარკერები, ისარი, სვეტების სათაურები, დაფის სათაური, ხაზები და ყოველი სხვა სტიკერი ზუსტად
უცვლელი რჩება — მათ შორის თითოეული სტიკერის ფერი, ადგილი და ოდნავი დახრა. იცვლება ზუსტად ერთი რამ:
სტიკერზე „partner API“-ს ნაცვლად იწერება „partner API v2“, იმავე შავი ხელნაწერით, იმავე სტიკერზე,
ისეთი ზომით, რომ შიგნით ეტევა. დაფა ხელახლა არ გადაიღო, არ გადაანათო და სხვა ხელნაწერი არ
გადახატო.
---
Photograph a planning whiteboard in a small office, shot from an angle so it reads as a real board in a
real room rather than a flat graphic. 3:2 horizontal, rendered at 4K. Every word on the board must be
legible.
Subject: a wall-mounted white magnetic whiteboard about two metres wide, its aluminium tray holding three
dry-wipe markers and an eraser. The board carries a hand-drawn plan in black and blue marker: a title at
the top left, a thick horizontal rule under it, and three columns divided by two vertical lines drawn
slightly out of true, as hand-drawn lines are. Sticky notes are pressed onto the board inside the columns
— two yellow in the first column, two pink in the second, one blue in the third — each slightly crooked,
each with one short line of handwriting on it, one note peeling a little at its lower corner.
Composition: the board fills most of the frame but is seen from the left, so its near left edge is taller
in frame than its far right edge and the board's horizontal lines converge gently to the right. The wall
and a sliver of the room show along the top and right. Nothing obscures the writing.
Camera: standing eye level, about two metres from the board and about one metre to the left of its centre,
35mm equivalent, so the board sits at roughly twenty-five degrees to the sensor plane, f/5.6 with the
focus set on the middle column so the whole board stays within the depth of field.
Light: soft daylight from a window out of frame on the camera's left, plus flat overhead office light. The
camera's angle is chosen so neither source puts a specular glare patch on the board; the left edge of the
board is a touch brighter than the right, and the sticky notes cast very short soft shadows down and to
the right.
Text in the image, in believable handwritten marker, spelled exactly as written here: top left, the
largest writing on the board, black, "Q3 LAUNCH"; the three column headings, black, about half that size,
"NOW", "NEXT", "LATER"; yellow notes under "NOW", in blue, "pricing page" and "beta invites"; pink notes
under "NEXT", in blue, "press kit" and "onboarding email"; blue note under "LATER", in black,
"partner API"; bottom right of the board, the smallest writing, black, "review fri 14:00". A hand-drawn
arrow in black curves from the "beta invites" note to the "onboarding email" note. No other writing on the
board — no stray marks, no half-erased ghosting of other words.
SECOND TURN — change one note only. Keep the board, the room, the camera position, the angle, the focal
length, the crop, the 3:2 frame, the light, the markers in the tray, the arrow, the column headings, the
title, the rules and every other note exactly as they are, including each note's colour, position and
slight crookedness. Change exactly one thing: the note reading "partner API" now reads "partner API v2" in
the same black handwriting, on the same note, at a size that still fits inside it. Do not re-photograph
the board, do not relight it and do not redraw any other handwriting.
```

---

### NB-22 · Restoring a damaged family photograph
`nano-banana` `gemini` — restoration, editing

**EN**
```
Restore the attached damaged photograph. It is a black-and-white family portrait taken in a village
in Racha in 1963: four people standing in front of a wooden porch. Keep the original 4:5 frame and
do not re-crop it.

Repair only the physical damage to the print: close the long vertical crease that runs from the top
edge down through the porch post, rebuild the torn corner at the lower right, remove the white
scratches across the sky, even out the yellow-brown fading along all four edges, and fill the small
circular loss of emulsion to the left of the porch step. Bring the contrast back to what a
well-printed silver gelatin print of that period would have had: a true black inside the doorway,
clean but not blown whites in the shirts, and a full range of greys in between.

Nothing about the people may be reinterpreted. Every face keeps its exact structure, its exact
proportions, the exact position of the eyes, nose and mouth, the same expression, the same apparent
age and the same skin texture. Do not smooth skin, do not open a closed eye, do not straighten a
posture, do not sharpen or redraw facial features, and do not make anyone look younger, healthier or
happier than the print shows. Clothing keeps its exact cut, its exact pattern and every fold and
crease as photographed. The background keeps the same porch, the same objects and the same number of
objects.

Where damage has destroyed information, reconstruct only what continues unambiguously from the
surrounding pixels — a straight plank, a flat area of sky, an uninterrupted fold in a sleeve. If a
damaged area covers part of a face or a hand, leave it as a plausible neutral continuation of the
tone around it; do not invent a feature that is not visible in the undamaged part of the print.

Keep the grain of the original; do not replace it with digital smoothness. The job is repairing a
print, not improving a photograph.
```

**KA**
```
გააკეთე მიმაგრებული, დაზიანებული ფოტოს რესტავრაცია. ეს არის შავ-თეთრი საოჯახო პორტრეტი, 1963 წელს
რაჭის ერთ სოფელში გადაღებული: ოთხი ადამიანი ხის აივნის წინ დგას. კადრის პროპორცია უცვლელი რჩება,
4:5, და ხელახლა არ დააკადრირო.

შეასწორე მხოლოდ ანაბეჭდის ფიზიკური დაზიანება: ამოავსე გრძელი ვერტიკალური ნაკეცი, რომელიც ზედა
კიდიდან აივნის სვეტში ჩამოდის; აღადგინე მოგლეჯილი ქვედა მარჯვენა კუთხე; მოაშორე თეთრი ნაკაწრები
ცის არეში; გაასწორე მოყვითალო-მოყავისფრო გახუნება ოთხივე კიდეზე; შეავსე ემულსიის პატარა, მრგვალი
დანაკარგი აივნის საფეხურის მარცხნივ. კონტრასტი იმ დონემდე დააბრუნე, როგორიც იმ პერიოდის კარგად
დაბეჭდილ ვერცხლის ჟელატინის ანაბეჭდს ჰქონდა: ნამდვილი შავი კარის ღიობში, სუფთა, მაგრამ არა
გადანათებული თეთრი პერანგებზე, და სრული ნაცრისფერი დიაპაზონი მათ შორის.

ადამიანებში ვერაფერი შეიცვლება. ყოველი სახე ინარჩუნებს ზუსტ აგებულებას, ზუსტ პროპორციას, თვალის,
ცხვირისა და პირის ზუსტ მდებარეობას, იმავე გამომეტყველებას, იმავე ასაკს და კანის იმავე ფაქტურას.
კანი არ დააგლუვო, დახუჭული თვალი არ გაახილო, პოზა არ გაასწორო, სახის ნაკვთები ხელახლა არ დახატო და
არავინ გახადო უფრო ახალგაზრდა, ჯანმრთელი ან მხიარული, ვიდრე ანაბეჭდზეა. ტანსაცმელს რჩება ზუსტად
იგივე ჭრა, იგივე ნახატი და ყოველი ნაკეცი ისე, როგორც ფოტოზეა. ფონზე იგივე აივანი, იგივე საგნები და
საგნების იგივე რაოდენობა რჩება.

იქ, სადაც დაზიანებამ ინფორმაცია გაანადგურა, აღადგინე მხოლოდ ის, რაც გარშემო არსებულ გამოსახულებას
ცალსახად აგრძელებს — სწორი ფიცარი, ცის ერთგვაროვანი არე, სახელოს გაუწყვეტელი ნაკეცი. თუ დაზიანება
სახის ან ხელის ნაწილს ფარავს, დატოვე ის გარშემო ტონის ნეიტრალურ გაგრძელებად; ნაკვთი, რომელიც
ანაბეჭდის დაუზიანებელ ნაწილში არ ჩანს, არ გამოიგონო.

ორიგინალის მარცვალი შენარჩუნდეს — ციფრული სიგლუვით არ ჩაანაცვლო. რეტუში მინიმალურია: შენი საქმე
ანაბეჭდის შეკეთებაა და არა ფოტოს გალამაზება.
---
Restore the attached damaged photograph. It is a black-and-white family portrait taken in a village in
Racha in 1963: four people standing in front of a wooden porch. Keep the original 4:5 frame and do not
re-crop it.
Repair only the physical damage to the print: close the long vertical crease running from the top edge
down through the porch post, rebuild the torn corner at the lower right, remove the white scratches
across the sky, even out the yellow-brown fading along all four edges, and fill the small circular loss
of emulsion to the left of the porch step. Bring the contrast back to what a well-printed silver gelatin
print of that period would have had: a true black inside the doorway, clean but not blown whites in the
shirts, and a full range of greys in between.
Nothing about the people may be reinterpreted. Every face keeps its exact structure, its exact
proportions, the exact position of the eyes, nose and mouth, the same expression, the same apparent age
and the same skin texture. Do not smooth skin, do not open a closed eye, do not straighten a posture, do
not sharpen or redraw facial features, and do not make anyone look younger, healthier or happier than
the print shows. Clothing keeps its exact cut, its exact pattern and every fold and crease as
photographed. The background keeps the same porch, the same objects and the same number of objects.
Where damage has destroyed information, reconstruct only what continues unambiguously from the
surrounding pixels — a straight plank, a flat area of sky, an uninterrupted fold in a sleeve. If a
damaged area covers part of a face or a hand, leave it as a plausible neutral continuation of the tone
around it; do not invent a feature that is not visible in the undamaged part of the print.
Keep the grain of the original; do not replace it with digital smoothness. The job is repairing a print,
not improving a photograph.
```

---

### NB-23 · Conservative colourisation with a stated palette
`nano-banana` `gemini` — colourisation, restoration

**EN**
```
Colourise the attached black-and-white photograph. It was taken in 1954 and shows a woman in her
fifties sitting at a treadle sewing machine beside a window. Keep the original 3:2 frame, the
original crop and the original grain.

This is a colouring job, not a reinterpretation. Put colour onto what is already in the frame and
change nothing else: every shape, every edge, every tonal value, every fold of cloth, the position of
the hands, the expression and the facial structure stay exactly as they are. Do not sharpen, do not
denoise, do not smooth skin, do not remove lines or blemishes, and do not alter her apparent age.

Palette brief — conservative and period-plausible, and on every decision take the less saturated
option:
- Skin: a muted warm beige, slightly cooler in the shadow under the chin. No pink flush, no tan, no
  glow.
- Hair: dark grey-brown with genuinely grey strands at the temple, exactly where the black-and-white
  original already separates those tones.
- Blouse: a faded dusty blue-grey. The apron over it: unbleached off-white with a very slight warm
  cast.
- The sewing machine body: near-black enamel with dulled gold decoration; the treadle ironwork a
  cold, desaturated grey.
- The room: plaster wall in a pale warm grey, window frame in chalky off-white, the daylight through
  the window slightly cool.
- Overall saturation low, the way a hand-tinted print of the period sits, not a modern digital
  photograph.

Where the original does not tell you what colour something was, choose the most ordinary and least
saturated possibility and keep it quiet. Do not invent a pattern on a plain surface, do not add a
printed motif to the apron, do not introduce an object, a flower or a piece of jewellery that is not
in the original, and do not colour any area in a way that implies detail the black-and-white image
does not contain.

No retouching of any kind: your job is to add colour, not to improve the photograph.
```

**KA**
```
გააფერადე მიმაგრებული შავ-თეთრი ფოტო. კადრი 1954 წელსაა გადაღებული: ორმოცდაათს გადაცილებული ქალი
ფანჯარასთან, ფეხით ამუშავებულ საკერავ მანქანასთან ზის. კადრის პროპორცია, კადრირება და ორიგინალის
მარცვალი უცვლელი რჩება, 3:2.

ეს გაფერადებაა და არა ხელახალი ინტერპრეტაცია. ფერი დაადე იმას, რაც კადრში უკვე არის, და სხვა
არაფერი შეცვალო: ყოველი ფორმა, ყოველი კიდე, ყოველი ტონალური მნიშვნელობა, ქსოვილის ყოველი ნაკეცი,
ხელების მდებარეობა, გამომეტყველება და სახის აგებულება ზუსტად ისე რჩება, როგორც არის. არ გაამკვეთრო,
ხმაური არ მოაშორო, კანი არ დააგლუვო, ნაოჭი და ლაქა არ მოაცილო, ასაკი არ შეცვალო.

პალიტრა — კონსერვატიული და ეპოქისთვის დამაჯერებელი; ყოველ არჩევანში ნაკლებად ნაჯერი ვარიანტი აიღე:
- კანი: დაწყნარებული თბილი ჩალისფერი, ნიკაპქვეშა ჩრდილში ოდნავ ცივი. ვარდისფერი სიწითლის,
  გარუჯვისა და ბზინვის გარეშე.
- თმა: მუქი ნაცრისფერ-ყავისფერი, საფეთქლებთან ნამდვილი ჭაღარა ღერებით — ზუსტად იქ, სადაც შავ-თეთრ
  ორიგინალში ეს ტონი უკვე გამოყოფილია.
- ბლუზა: გახუნებული, მტვრისფერ-ლურჯი; მასზე წინსაფარი — გაუთეთრებელი, ოდნავ თბილი თეთრი.
- საკერავი მანქანის კორპუსი: თითქმის შავი ემალი, მიბინდული ოქროსფერი ორნამენტით; ფეხის მექანიზმის
  ლითონი — ცივი, არანაჯერი რკინისფერი.
- ოთახი: ბათქაშის კედელი ღია, თბილ ნაცრისფერში, ფანჯრის ჩარჩო ცარცისფერ-თეთრში, ფანჯრიდან შემოსული
  დღის შუქი ოდნავ ცივი.
- ფერის საერთო ნაჯერობა დაბალია — ისეთი, როგორიც იმ დროის ხელით შეფერადებულ ანაბეჭდს ჰქონდა, და არა
  თანამედროვე ციფრულ ფოტოს.

სადაც ორიგინალი არ ამბობს, რა ფერისა იყო საგანი, აირჩიე ყველაზე ჩვეულებრივი და ყველაზე ნაკლებად
ნაჯერი ვარიანტი და წყნარად დატოვე. ერთფეროვან ზედაპირზე ნახატი არ გამოიგონო, წინსაფარს ორნამენტი არ
დაუმატო, ორიგინალში არარსებული საგანი, ყვავილი ან სამკაული არ შემოიტანო და ფერით ისეთი დეტალი არ
წარმოქმნა, რომელიც შავ-თეთრ გამოსახულებაში არ არის.

რეტუში აკრძალულია — კანის ფაქტურა ხელუხლებელი რჩება.
---
Colourise the attached black-and-white photograph. It was taken in 1954 and shows a woman in her fifties
sitting at a treadle sewing machine beside a window. Keep the original 3:2 frame, the original crop and
the original grain.
This is a colouring job, not a reinterpretation. Put colour onto what is already in the frame and change
nothing else: every shape, every edge, every tonal value, every fold of cloth, the position of the hands,
the expression and the facial structure stay exactly as they are. Do not sharpen, do not denoise, do not
smooth skin, do not remove lines or blemishes, and do not alter her apparent age.
Palette brief — conservative and period-plausible, and on every decision take the less saturated option.
Skin: a muted warm beige, slightly cooler in the shadow under the chin; no pink flush, no tan, no glow.
Hair: dark grey-brown with genuinely grey strands at the temple, exactly where the black-and-white
original already separates those tones. Blouse: a faded dusty blue-grey; the apron over it unbleached
off-white with a very slight warm cast. The sewing machine body: near-black enamel with dulled gold
decoration, the treadle ironwork a cold desaturated grey. The room: plaster wall in a pale warm grey,
window frame in chalky off-white, the daylight through the window slightly cool. Overall saturation low,
the way a hand-tinted print of the period sits, not a modern digital photograph.
Where the original does not tell you what colour something was, choose the most ordinary and least
saturated possibility and keep it quiet. Do not invent a pattern on a plain surface, do not add a printed
motif to the apron, do not introduce an object, a flower or a piece of jewellery that is not in the
original, and do not colour any area in a way that implies detail the black-and-white image does not
contain.
No retouching of any kind: your job is to add colour, not to improve the photograph.
```

---

### NB-24 · Background replacement that keeps edges, shadow and temperature
`nano-banana` `gemini` — editing, background

**EN**
```
Replace the background of the attached product photograph. Keep the 4:5 frame.

The subject is a hand-thrown glazed ceramic pitcher standing upright, currently shot against a plain
white studio sweep. The pitcher itself stays pixel-identical: the same silhouette, the same handle,
the same glaze colour and its exact variation, the same crackle, the same throwing rings, the same
highlight positions, the same scale and the same position in the frame. Do not re-render, do not
relight and do not re-photograph the pitcher.

The new background: a wide pale limestone ledge running horizontally across the lower third of the
frame, and behind it a softly out-of-focus plaster wall in a warm neutral grey that darkens gently
toward the top corners. No pattern, no objects, nothing competing with the pitcher.

Three things must agree between the subject and the new background, and this is what the edit is
really about:
1. Edges. The existing edge of the pitcher stays exactly where it is, with the softness it already
   has. Do not cut it out hard, do not add a halo, do not leave a white fringe from the old sweep,
   and do not feather the handle where it crosses the background.
2. Shadow. The light in the original comes from the upper left, so the contact shadow under the
   pitcher still falls to the lower right, at the same angle, the same length and the same softness
   as the shadow already in the picture — now sitting on stone rather than on white paper, so
   slightly warmer and slightly more absorbed.
3. Colour temperature. Match the background to the light already on the pitcher, never the other way
   round. The original is neutral to slightly warm daylight, so the wall and the ledge are lit at the
   same temperature and sit about one and a half stops darker than the pitcher's lit side.

Do not add a reflection beneath the pitcher unless matte limestone would plausibly produce one; if in
doubt, leave the stone matte. Do not add a second shadow, a rim light or any light source the
original does not contain.
```

**KA**
```
შეუცვალე მიმაგრებულ საპროდუქტო ფოტოს ფონი. კადრის პროპორცია იგივე რჩება, 4:5.

ობიექტი ხელით ნაქნარი, მოჭიქული კერამიკული დოქია, ვერტიკალურად მდგარი; ამჟამად თეთრ სტუდიურ
ფონზეა გადაღებული. დოქი პიქსელამდე უცვლელი რჩება: იგივე სილუეტი, იგივე ყური, ჭიქურის იგივე ფერი
და მისი ზუსტი გადასვლები, იგივე წვრილი ბზარები ჭიქურზე, ჩარხის იგივე კვალი, შუქის ლაქების იგივე
ადგილი, იგივე მასშტაბი და კადრში იგივე მდებარეობა. დოქი ხელახლა არ დაარენდერო, თავიდან არ გაანათო
და ხელახლა არ „გადაიღო“.

ახალი ფონი: ღია კირქვის განიერი საფეხური კადრის ქვედა მესამედში, ჰორიზონტალურად; მის უკან
დაბუნდოვნებული ბათქაშის კედელი თბილ, ნეიტრალურ ნაცრისფერში, რომელიც ზედა კუთხეებისკენ ნელა მუქდება.
ნახატის, საგნებისა და ყოველგვარი კონკურენტი დეტალის გარეშე.

სამი რამ ობიექტსა და ახალ ფონს შორის უნდა დაემთხვეს — სწორედ ამაშია ამ რედაქტირების არსი:
1. კიდეები. დოქის არსებული კიდე ზუსტად იმავე ადგილას და იმავე სირბილით რჩება. მკვეთრად არ ამოჭრა,
   შარავანდი არ გააჩინო, ძველი თეთრი ფონიდან თეთრი არშია არ დატოვო და ყურის კიდე ფონთან შეხებისას
   არ დაბინდო.
2. ჩრდილი. ორიგინალში შუქი ზედა მარცხენა მხრიდან მოდის, ამიტომ დოქის ძირის ჩრდილი ისევ
   მარჯვნივ-ქვემოთ ეცემა — იმავე კუთხით, იმავე სიგრძით და იმავე სირბილით, როგორც ახლა; ოღონდ ახლა
   ქვაზე დევს და არა თეთრ ქაღალდზე, ამიტომ ოდნავ თბილია და ოდნავ მეტად ჩაწოვილი.
3. ფერის ტემპერატურა. ფონი მოარგე იმ შუქს, რომელიც დოქზე უკვე დევს, და არა პირიქით. ორიგინალი
   ნეიტრალური ან ოდნავ თბილი დღის შუქია, ამიტომ კედელი და საფეხური იმავე ტემპერატურით არის
   განათებული და დოქის განათებულ მხარეზე დაახლოებით ერთნახევარი საფეხურით მუქია.

ანარეკლი დოქის ქვეშ მხოლოდ მაშინ დაამატე, თუ მქრქალი კირქვა მას მართლაც გააჩენდა; ეჭვის შემთხვევაში
ქვა მქრქალი დატოვე. მეორე ჩრდილი, კონტურული შუქი ან ორიგინალში არარსებული სხვა წყარო არ შემოიტანო.
---
Replace the background of the attached product photograph. Keep the 4:5 frame.
The subject is a hand-thrown glazed ceramic pitcher standing upright, currently shot against a plain
white studio sweep. The pitcher itself stays pixel-identical: the same silhouette, the same handle, the
same glaze colour and its exact variation, the same crackle, the same throwing rings, the same highlight
positions, the same scale and the same position in the frame. Do not re-render, do not relight and do not
re-photograph the pitcher.
The new background: a wide pale limestone ledge running horizontally across the lower third of the frame,
and behind it a softly out-of-focus plaster wall in a warm neutral grey that darkens gently toward the
top corners. No pattern, no objects, nothing competing with the pitcher.
Three things must agree between the subject and the new background. Edges: the existing edge of the
pitcher stays exactly where it is, with the softness it already has — do not cut it out hard, do not add
a halo, do not leave a white fringe from the old sweep, and do not feather the handle where it crosses
the background. Shadow: the light in the original comes from the upper left, so the contact shadow under
the pitcher still falls to the lower right, at the same angle, the same length and the same softness as
the shadow already in the picture, now sitting on stone rather than white paper, so slightly warmer and
slightly more absorbed. Colour temperature: match the background to the light already on the pitcher,
never the other way round — the original is neutral to slightly warm daylight, so the wall and the ledge
are lit at the same temperature and sit about one and a half stops darker than the pitcher's lit side.
Do not add a reflection beneath the pitcher unless matte limestone would plausibly produce one; if in
doubt, leave the stone matte. Do not add a second shadow, a rim light or any light source the original
does not contain.
```

---

### NB-25 · Restyle a room, keep the architecture
`nano-banana` `gemini` — interior, editing

**EN**
```
Restyle the room in the attached photograph. Keep the 3:2 frame, the same camera position, the same
focal length and the same crop.

The architecture is fixed and must come through unchanged, to the pixel wherever it is visible: the
two windows keep their exact positions, widths, heights and sill heights; the ceiling stays at the
same height with the same cornice profile; the door stays in the same wall, in the same place, and
hangs the same way; the radiator under the left window stays; the room keeps its exact floor plan and
its exact proportions, and the perspective lines of walls, floor and ceiling stay exactly where they
are. Do not move a wall, do not widen a window, do not raise the ceiling, do not change the
footprint.

What changes is everything that is not the building:
- Palette: the walls go from the current cold white to a warm chalky off-white; the woodwork around
  the windows and the door goes to a deep muted olive; the floor becomes a mid-tone oak in a wide
  plank, laid parallel to the window wall.
- Furniture: a low three-seater sofa in heavy oatmeal linen against the wall opposite the windows; a
  round dark walnut coffee table in front of it; one armchair in the same olive as the woodwork in
  the corner to the right of the far window, angled toward the sofa; a long low walnut sideboard
  along the right wall.
- Textiles: a flat-woven wool rug in muted rust and off-white under the coffee table, not touching
  the walls; full-height unlined linen curtains in the same off-white as the walls, drawn open; one
  large ceramic vessel on the sideboard and nothing else. No gallery wall, no clutter.

The light does not change: it still enters through the same two windows at the same angle, with the
same softness and at the same time of day, and every new object casts a shadow consistent with it, in
the same direction as the shadows already in the photograph.

Keep the same white balance, the same mild contrast and the same lens character as the original. This
must read as the same room photographed a second time, not as a render.
```

**KA**
```
შეცვალე მიმაგრებულ ფოტოზე გამოსახული ოთახის ინტერიერი. კადრის პროპორცია, კამერის ადგილი, ფოკუსური
მანძილი და კადრირება იგივე რჩება, 3:2.

არქიტექტურა ხელშეუხებელია და უცვლელად უნდა გადმოვიდეს — სადაც ჩანს, პიქსელამდე: ორივე ფანჯარას რჩება
ზუსტი ადგილი, სიგანე, სიმაღლე და რაფის სიმაღლე; ჭერი იმავე სიმაღლეზე და იმავე კარნიზის პროფილით
რჩება; კარი იმავე კედელში, იმავე ადგილას და იმავე მხარეს იღება; მარცხენა ფანჯრის ქვეშ რადიატორი
რჩება; ოთახს რჩება ზუსტად იგივე გეგმა და იგივე პროპორცია, კედლების, იატაკისა და ჭერის პერსპექტივის
ხაზები კი ზუსტად იმავე ადგილას. კედელი არ გადაწიო, ფანჯარა არ გააგანიერო, ჭერი არ აწიო, ოთახის
კონტური არ შეცვალო.

იცვლება ყველაფერი, რაც შენობა არ არის:
- პალიტრა: კედლები ცივი თეთრიდან თბილ, ცარცისფერ-თეთრში გადადის; ფანჯრებისა და კარის ხის მორთულობა
  — ღრმა, დაწყნარებულ ზეთისხილისფერში; იატაკი — საშუალო ტონის მუხა, განიერი ფიცრით, ფანჯრების
  კედლის პარალელურად დაგებული.
- ავეჯი: დაბალი, სამადგილიანი დივანი მკვრივ, ჩალისფერ სელში, ფანჯრების მოპირდაპირე კედელთან; მის
  წინ მრგვალი, მუქი კაკლის ხის ჟურნალის მაგიდა; ერთი სავარძელი ხის მორთულობის იმავე ზეთისხილისფერში,
  შორეული ფანჯრის მარჯვნივ, კუთხეში, დივანისკენ შემობრუნებული; მარჯვენა კედელზე გრძელი, დაბალი
  კაკლის ხის კომოდი.
- ქსოვილი: ბრტყლად ნაქსოვი შალის ხალიჩა დაწყნარებულ აგურისფერსა და თეთრში, ჟურნალის მაგიდის ქვეშ,
  კედლებს არ ეხება; იატაკამდე ჩამოშვებული, უსარჩულო სელის ფარდები კედლების იმავე ტონში, გახსნილი;
  კომოდზე ერთი დიდი კერამიკული ჭურჭელი და მეტი არაფერი. კედელზე სურათების კედელი და ზედმეტი
  წვრილმანი არ იყოს.

განათება არ იცვლება: შუქი ისევ იმავე ორი ფანჯრიდან შემოდის, იმავე კუთხით, იმავე სირბილით და დღის
იმავე მონაკვეთში; ყოველი ახალი საგანი ამას შეესაბამება და ჩრდილს იმავე მიმართულებით აგდებს, რა
მიმართულებითაც ფოტოზე არსებული ჩრდილები ეცემა.

თეთრის ბალანსი, სუსტი კონტრასტი და ობიექტივის ხასიათი ორიგინალისაა. შედეგი ისე უნდა იკითხებოდეს,
თითქოს იგივე ოთახი მეორედ გადაიღეს — და არა როგორც რენდერი.
---
Restyle the room in the attached photograph. Keep the 3:2 frame, the same camera position, the same focal
length and the same crop.
The architecture is fixed and must come through unchanged, to the pixel wherever it is visible: the two
windows keep their exact positions, widths, heights and sill heights; the ceiling stays at the same
height with the same cornice profile; the door stays in the same wall, in the same place, and hangs the
same way; the radiator under the left window stays; the room keeps its exact floor plan and its exact
proportions, and the perspective lines of walls, floor and ceiling stay exactly where they are. Do not
move a wall, do not widen a window, do not raise the ceiling, do not change the footprint.
What changes is everything that is not the building. Palette: the walls go from the current cold white to
a warm chalky off-white; the woodwork around the windows and the door goes to a deep muted olive; the
floor becomes a mid-tone oak in a wide plank, laid parallel to the window wall. Furniture: a low
three-seater sofa in heavy oatmeal linen against the wall opposite the windows; a round dark walnut
coffee table in front of it; one armchair in the same olive as the woodwork in the corner to the right of
the far window, angled toward the sofa; a long low walnut sideboard along the right wall. Textiles: a
flat-woven wool rug in muted rust and off-white under the coffee table, not touching the walls;
full-height unlined linen curtains in the same off-white as the walls, drawn open; one large ceramic
vessel on the sideboard and nothing else. No gallery wall, no clutter.
The light does not change: it still enters through the same two windows at the same angle, with the same
softness and at the same time of day, and every new object casts a shadow consistent with it, in the same
direction as the shadows already in the photograph.
Keep the same white balance, the same mild contrast and the same lens character as the original. This
must read as the same room photographed a second time, not as a render.
```

---

### NB-26 · Staging an empty Tbilisi flat for a listing
`nano-banana` `gemini` — interior, staging

**EN**
```
Furnish the empty room in the attached photograph for a rental listing. It is a flat in Vera,
Tbilisi, in a 1960s block. Keep the 4:5 frame, the same camera position, the same focal length and
the same crop.

Keep the room exactly as photographed: the same wall positions and proportions, the same ceiling
height, the same window on the left wall with its existing frame, reveal and sill, the same door, the
same parquet floor with its existing pattern, tone and wear, the same skirting, the same sockets. Put
furniture into the room; do not rebuild the room around the furniture.

Style and budget tier: mid-market, current, plainly furnished for renting — the kind of interior a
tenant reads as new but not expensive. Oak veneer and light metal frames, plain woven textiles,
nothing custom, nothing antique, nothing luxury. Palette: the walls stay the warm off-white they
already are, plus oak, oatmeal and one muted terracotta accent.

Furnish it like this:
- A two-seater sofa in oatmeal fabric against the wall opposite the window, centred on that wall.
- A small round oak coffee table in front of the sofa, about an arm's length away.
- A narrow oak-veneer console against the right wall, with a table lamp switched off at its far end.
- A flat-woven rug in oatmeal and terracotta under the coffee table, not reaching any wall.
- Two plain linen curtains at the window, hung inside the reveal and drawn fully open.
- One medium potted plant standing on the floor in the corner to the right of the window.
- Nothing on the walls, no television, no clutter, no visible brand or logo on any object.

Light: the window is on the left and it is late morning, so daylight enters from the left at a
shallow downward angle, soft and slightly cool. Every new object casts a soft shadow to its right, at
the same angle and softness as the shadow the window reveal already casts on the floor. Do not switch
the lamp on, do not add a second light source, do not warm the room artificially.

Photographic, not a render: the same white balance, the same contrast and the same lens character as
the original empty-room photograph, and the verticals stay vertical.
```

**KA**
```
მოაწყე მიმაგრებულ ფოტოზე გამოსახული ცარიელი ოთახის ინტერიერი გასაქირავებელი ბინის განცხადებისთვის.
ბინა თბილისში, ვერაზე, 1960-იანი წლების კორპუსშია. კადრის პროპორცია, კამერის ადგილი, ფოკუსური
მანძილი და კადრირება იგივე რჩება, 4:5.

ოთახი ზუსტად ისეთი რჩება, როგორიც ფოტოზეა: კედლების იგივე ადგილი და პროპორცია, ჭერის იგივე სიმაღლე,
მარცხენა კედელზე იგივე ფანჯარა თავისი ჩარჩოთი, ღიობითა და რაფით, იგივე კარი, იგივე პარკეტი თავისი
ნახატით, ტონითა და გაცვეთილობით, იგივე ცოკოლი, იგივე როზეტები. ავეჯი ოთახში შეიტანე და არა პირიქით —
ოთახი ავეჯს არ მოარგო.

სტილი და ბიუჯეტის დონე: საშუალო სეგმენტი, თანამედროვე, გასაქირავებლად მარტივად მოწყობილი — ისეთი,
რომელსაც მქირავებელი ახალს დაარქმევს და არა ძვირს. მუხის შპონი და ღია ფერის ლითონის კარკასი, უბრალო
ნაქსოვი ქსოვილი; არაფერი ინდივიდუალურად შეკვეთილი, არაფერი ანტიკვარული, არაფერი ძვირფასი. პალიტრა:
კედლები იმავე თბილ, მოთეთრო ტონში რჩება, პლუს მუხა, ჩალისფერი და ერთი დაწყნარებული ტერაკოტის აქცენტი.

ასე მოაწყე:
- ორადგილიანი დივანი ჩალისფერ ქსოვილში, ფანჯრის მოპირდაპირე კედელთან, კედლის ცენტრში.
- დივნის წინ, ერთი ხელის მანძილზე, პატარა მრგვალი მუხის ჟურნალის მაგიდა.
- მარჯვენა კედელთან ვიწრო, მუხის შპონის კონსოლი, მის შორეულ ბოლოში ჩამქრალი სამაგიდო სანათი.
- ჟურნალის მაგიდის ქვეშ ბრტყლად ნაქსოვი ხალიჩა ჩალისფერსა და ტერაკოტაში, არცერთ კედელს არ სწვდება.
- ფანჯარაზე ორი უბრალო სელის ფარდა, ღიობის შიგნით ჩამოკიდებული და ბოლომდე გახსნილი.
- ფანჯრის მარჯვნივ, კუთხეში, იატაკზე მდგარი ერთი საშუალო ზომის მცენარე ქოთანში.
- კედლებზე არაფერი, ტელევიზორი არ იყოს, ზედმეტი წვრილმანი არ იყოს, არცერთ საგანზე ბრენდი ან ლოგო
  არ ჩანდეს.

განათება: ფანჯარა მარცხნივაა, დრო დილის მიწურულია — დღის შუქი მარცხნიდან, მცირე დახრით შემოდის,
რბილი და ოდნავ ცივია. ყოველი ახალი საგანი რბილ ჩრდილს მარჯვნივ აგდებს, იმავე კუთხითა და სირბილით,
როგორც ფანჯრის ღიობი უკვე აგდებს იატაკზე. სანათი არ აანთო, მეორე წყარო არ დაამატო, ოთახი ხელოვნურად
არ გაათბო.

შედეგი ფოტო უნდა იყოს და არა რენდერი: იგივე თეთრის ბალანსი, იგივე კონტრასტი და ობიექტივის იგივე
ხასიათი, რაც ცარიელი ოთახის ორიგინალ კადრს აქვს; ვერტიკალური ხაზები ვერტიკალურად რჩება.
---
Furnish the empty room in the attached photograph for a rental listing. It is a flat in Vera, Tbilisi, in
a 1960s block. Keep the 4:5 frame, the same camera position, the same focal length and the same crop.
Keep the room exactly as photographed: the same wall positions and proportions, the same ceiling height,
the same window on the left wall with its existing frame, reveal and sill, the same door, the same
parquet floor with its existing pattern, tone and wear, the same skirting, the same sockets. Put
furniture into the room; do not rebuild the room around the furniture.
Style and budget tier: mid-market, current, plainly furnished for renting — the kind of interior a tenant
reads as new but not expensive. Oak veneer and light metal frames, plain woven textiles, nothing custom,
nothing antique, nothing luxury. Palette: the walls stay the warm off-white they already are, plus oak,
oatmeal and one muted terracotta accent.
Furnish it like this: a two-seater sofa in oatmeal fabric against the wall opposite the window, centred
on that wall; a small round oak coffee table in front of the sofa, about an arm's length away; a narrow
oak-veneer console against the right wall with a table lamp switched off at its far end; a flat-woven rug
in oatmeal and terracotta under the coffee table, not reaching any wall; two plain linen curtains at the
window, hung inside the reveal and drawn fully open; one medium potted plant standing on the floor in the
corner to the right of the window. Nothing on the walls, no television, no clutter, no visible brand or
logo on any object.
Light: the window is on the left and it is late morning, so daylight enters from the left at a shallow
downward angle, soft and slightly cool. Every new object casts a soft shadow to its right, at the same
angle and softness as the shadow the window reveal already casts on the floor. Do not switch the lamp on,
do not add a second light source, do not warm the room artificially.
Photographic, not a render: the same white balance, the same contrast and the same lens character as the
original empty-room photograph, and the verticals stay vertical.
```

---

### NB-27 · Materials and finishes board with exact labels
`nano-banana` `gemini` — moodboard, in-image text

**EN**
```
Design a materials and finishes board as a single flat-lay image, 4:5 vertical, rendered at 4K,
photographed straight down from directly above so every sample lies flat with no perspective skew.

The board is a sheet of warm grey card filling the frame, with an even margin of about six percent on
all four sides. Six samples sit on it in two columns and three rows, evenly spaced, each sample the
same rectangle size, none overlapping another, each casting only a very short soft shadow.

The six samples, in reading order:
1. Top left — a plank of mid-tone oak flooring, grain running vertically, matt oiled finish.
2. Top right — a painted wall sample in a warm chalky off-white, flat finish, a faint roller texture.
3. Middle left — a painted wall sample in a deep muted olive, eggshell finish.
4. Middle right — a folded piece of heavy oatmeal linen, the fold running horizontally.
5. Bottom left — a flat-woven wool swatch in muted rust with one off-white weft line.
6. Bottom right — two metal chips overlapping slightly, brushed brass on top of blackened steel.

Beneath each sample, one line of small text centred under that sample, in a plain grey sans-serif at
the same size for all six, spelled exactly as written here:
- "OAK — MATT OILED"
- "WALL 01 — CHALK WHITE"
- "WALL 02 — DEEP OLIVE"
- "LINEN — OATMEAL"
- "WOOL — MUTED RUST"
- "BRASS / BLACKENED STEEL"

At the top of the board, above the first row and clear of it, one line in the same sans-serif at
roughly twice the label size, centred: "MATERIALS & FINISHES"

Light: one large soft source from the upper left, so each sample carries a faint shadow to its lower
right; exposure even across the whole board with no hotspot in the middle. The texture of each
material must be legible at full size — the grain of the oak, the weave of the linen, the brush lines
in the brass.

Every letter sharp, correctly spelled, evenly spaced, fully inside the frame, and never overlapping a
sample.
```

**KA**
```
შექმენი მასალებისა და მოპირკეთების დაფა ერთ კადრად, ზემოდან გადაღებული მაკეტის სახით: ვერტიკალური
კადრი 4:5, რენდერი 4K, კამერა ზუსტად ვერტიკალურად ზემოდან — ყოველი ნიმუში ბრტყლად და პერსპექტივის
დამახინჯების გარეშე ჩანს.

დაფა თბილი ნაცრისფერი მუყაოს ფურცელია და მთელ კადრს ავსებს, ოთხივე მხრიდან დაახლოებით ექვსპროცენტიანი
თანაბარი ველით. მასზე 6 ნიმუშია — 2 სვეტად და 3 რიგად, თანაბარი მანძილით, ყველა ერთი და იმავე ზომის
მართკუთხედი, ერთმანეთს არ ედება; თითოეულს მხოლოდ ძალიან მოკლე, რბილი ჩრდილი აქვს.

ექვსი ნიმუში, კითხვის რიგით:
1. ზედა მარცხნივ — საშუალო ტონის მუხის იატაკის ფიცარი, ბოჭკო ვერტიკალურად, მქრქალი ზეთოვანი დაფარვა.
2. ზედა მარჯვნივ — კედლის საღებავის ნიმუში თბილ, ცარცისფერ-თეთრში, მქრქალი, ვალიკის სუსტი ფაქტურით.
3. შუა მარცხნივ — კედლის საღებავის ნიმუში ღრმა, დაწყნარებულ ზეთისხილისფერში, ნახევრად მქრქალი.
4. შუა მარჯვნივ — მკვრივი, ჩალისფერი სელის გადაკეცილი ნაჭერი, ნაკეცი ჰორიზონტალურად.
5. ქვედა მარცხნივ — ბრტყლად ნაქსოვი შალის ნიმუში დაწყნარებულ აგურისფერში, ერთი თეთრი ღერის ზოლით.
6. ქვედა მარჯვნივ — ლითონის 2 ფირფიტა, ოდნავ გადაფარებული: ზემოთ გაპრიალებული სპილენძი, ქვემოთ
   გაშავებული ფოლადი.

თითოეული ნიმუშის ქვეშ ერთი ხაზი პატარა ტექსტი, ნიმუშის ცენტრზე გასწორებული, უბრალო ნაცრისფერი
შრიფტით, ექვსივესთვის ერთი ზომით, ზუსტად ასე დაწერილი:
- „OAK — MATT OILED“
- „WALL 01 — CHALK WHITE“
- „WALL 02 — DEEP OLIVE“
- „LINEN — OATMEAL“
- „WOOL — MUTED RUST“
- „BRASS / BLACKENED STEEL“

დაფის თავში, პირველ რიგზე მაღლა და მისგან დაშორებით, ერთი ხაზი იმავე შრიფტით, წარწერების ზომაზე
დაახლოებით ორჯერ დიდი, ცენტრში: „MATERIALS & FINISHES“

განათება: ერთი დიდი, რბილი წყარო ზედა მარცხენა მხრიდან — ყოველ ნიმუშს სუსტი ჩრდილი მარჯვნივ-ქვემოთ
აქვს; ექსპოზიცია მთელ დაფაზე თანაბარია, ცენტრში კაშკაშა ლაქის გარეშე. ყოველი მასალის ფაქტურა სრულ
ზომაში იკითხება — მუხის ბოჭკო, სელის ქსოვილი, სპილენძზე ჯაგრისის ხაზები.

ყოველი ასო მკვეთრი, სწორად დაწერილი, თანაბარი ინტერვალით, მთლიანად კადრშია და ნიმუშს არსად ედება.

# წარწერები შეგნებულად ლათინურია. თუ ქართული ეტიკეტები გჭირდება, სთხოვე მოდელს, ნიმუშების ქვეშ
# ზოლი ცარიელი დატოვოს („leave the label strip empty, flat warm grey card“) და ქართული შრიფტი
# დიზაინის პროგრამაში შენ დააწერე — გენერირებული ქართული ასოები თითქმის ყოველთვის შესასწორებელია.
---
Design a materials and finishes board as a single flat-lay image, 4:5 vertical, rendered at 4K,
photographed straight down from directly above so every sample lies flat with no perspective skew.
The board is a sheet of warm grey card filling the frame, with an even margin of about six percent on all
four sides. Six samples sit on it in two columns and three rows, evenly spaced, each sample the same
rectangle size, none overlapping another, each casting only a very short soft shadow.
The six samples, in reading order: top left, a plank of mid-tone oak flooring, grain running vertically,
matt oiled finish; top right, a painted wall sample in a warm chalky off-white, flat finish, a faint
roller texture; middle left, a painted wall sample in a deep muted olive, eggshell finish; middle right, a
folded piece of heavy oatmeal linen, the fold running horizontally; bottom left, a flat-woven wool swatch
in muted rust with one off-white weft line; bottom right, two metal chips overlapping slightly, brushed
brass on top of blackened steel.
Beneath each sample, one line of small text centred under that sample, in a plain grey sans-serif at the
same size for all six, spelled exactly as written here: "OAK — MATT OILED", "WALL 01 — CHALK WHITE",
"WALL 02 — DEEP OLIVE", "LINEN — OATMEAL", "WOOL — MUTED RUST", "BRASS / BLACKENED STEEL".
At the top of the board, above the first row and clear of it, one line in the same sans-serif at roughly
twice the label size, centred: "MATERIALS & FINISHES"
Light: one large soft source from the upper left, so each sample carries a faint shadow to its lower
right; exposure even across the whole board with no hotspot in the middle. The texture of each material
must be legible at full size — the grain of the oak, the weave of the linen, the brush lines in the brass.
Every letter sharp, correctly spelled, evenly spaced, fully inside the frame, and never overlapping a
sample.
```

---

### NB-28 · Campaign carousel — three frames, shared clauses
`nano-banana` `gemini` — carousel, consistency

**EN**
```
Produce three photographs for one social media carousel for a family-run winery in Kakheti. Generate
each frame separately, but they must read as one campaign, shot on one day by one photographer.

Three clauses are shared by all three frames. Repeat each of them word for word in every frame's
prompt and change nothing inside them — this repetition is the mechanism that makes the set hold
together.

Lens clause: "50mm equivalent, camera at chest height, held level, f/4, shallow but not extreme depth
of field, no wide-angle distortion at the edges."

Light clause: "It is the last hour before sunset in late September. The sun is low and to the west,
out of frame to camera left. The light is warm, directional and soft-edged; every shadow in the frame
runs toward the lower right; nothing is lit artificially and no lamp is switched on."

Palette clause: "Dusty green, warm ochre, clay brown, unbleached linen, and one deep garnet accent
from the wine itself. Low saturation, natural colour, no colour grading, fine film grain."

Every frame is 4:5 vertical and carries all three clauses in full. The frames differ only in subject.

Frame 1 — the vines. A row of Rkatsiteli vines seen from the end of the row, the row running away
from camera and slightly to the right, leaves front-lit and translucent, the Alazani valley haze in
the far background, no people.

Frame 2 — the hands. A close medium shot of two hands cutting a bunch of grapes with secateurs,
cropped at the forearms, the bunch in the lower right of the frame and the cut stem in the upper
left, the leaves behind falling out of focus. The hands are weathered and unmanicured; no jewellery,
no watch, no face in frame.

Frame 3 — the marani. The mouth of a buried qvevri in a whitewashed vaulted cellar, seen from
standing height looking slightly down, the clay lip filling the lower left third, a glass of deep
garnet wine on the stone slab to the right of it, the vaulted ceiling dissolving into shadow behind.
The low western light enters through a doorway out of frame to camera left.

No text in any of the three frames, no logo, no readable label — the campaign copy is placed over
them in layout.
```

**KA**
```
მოამზადე 3 კადრი სოციალური ქსელის ერთი კარუსელისთვის — კახეთში, ოჯახურ მარანზე. თითოეული კადრი ცალკე
გენერირდება, მაგრამ სამივე ისე უნდა იკითხებოდეს, თითქოს ერთ დღეს, ერთმა ფოტოგრაფმა გადაიღო.

სამივე კადრს ერთი და იგივე სამი აბზაცი აქვს. გადაიტანე ისინი ყოველ პრომპტში სიტყვასიტყვით და
შიგნით არაფერი შეცვალო — სწორედ ეს გამეორებაა ის მექანიზმი, რომელიც კარუსელს ერთიანად კრავს.

ოპტიკის აბზაცი: „50 მმ ექვივალენტი, კამერა მკერდის სიმაღლეზე, სწორად დაჭერილი, f/4, მცირე, მაგრამ
არა უკიდურესი სიღრმის ველი, კიდეებში განიერი ობიექტივის დამახინჯების გარეშე.“

განათების აბზაცი: „სექტემბრის ბოლოა, მზის ჩასვლამდე ბოლო საათი. მზე დაბალია, დასავლეთით, კადრს
გარეთ, კამერიდან მარცხნივ. შუქი თბილი, მიმართული და რბილკიდიანია; კადრში ყოველი ჩრდილი
მარჯვნივ-ქვემოთ მიდის; ხელოვნური განათება არსად არის და არცერთი ნათურა არ ანთია.“

პალიტრის აბზაცი: „მტვრისფერ-მწვანე, თბილი ოხრა, თიხისფერი, გაუთეთრებელი სელი და ერთი ღრმა
ბროწეულისფერი აქცენტი თავად ღვინისგან. დაბალი ნაჯერობა, ბუნებრივი ფერი, ფერის დამუშავების გარეშე,
წვრილი ფოტოფირის მარცვალი.“

ყოველი კადრი ვერტიკალურია, 4:5, და სამივე აბზაცს სრულად ატარებს. კადრები მხოლოდ ობიექტით
განსხვავდება.

კადრი 1 — ვაზი. რქაწითელის ერთი რიგი, რიგის ბოლოდან დანახული; რიგი კამერიდან შორდება და ოდნავ
მარჯვნივ მიდის, ფოთოლი წინიდან განათებული და გამჭვირვალეა, შორს ალაზნის ველის ნისლი; ადამიანების
გარეშე.

კადრი 2 — ხელები. ახლო საშუალო ხედი: ორი ხელი სასხლავით ყურძნის მტევანს ჭრის, კადრი წინამხრებზე
იჭრება, მტევანი ქვედა მარჯვენა ნაწილშია, მოჭრილი ყუნწი — ზედა მარცხენაში, უკან ფოთოლი მკვეთრობას
კარგავს. ხელები ნამუშევარი და მოუვლელია; სამკაულის, საათისა და სახის გარეშე.

კადრი 3 — მარანი. მიწაში ჩაფლული ქვევრის ყელი მოთეთრებულ, თაღოვან მარანში, მდგომი ადამიანის
სიმაღლიდან, ოდნავ ქვემოთ მზერით; თიხის ყელი ქვედა მარცხენა მესამედს ავსებს, მის მარჯვნივ, ქვის
ფილაზე — ჭიქა ღრმა ბროწეულისფერი ღვინით, უკან თაღოვანი ჭერი ჩრდილში ქრება. დაბალი დასავლური შუქი
კარიდან შემოდის, კადრს გარეთ, კამერიდან მარცხნივ.

არცერთ კადრში წარწერა, ლოგო ან წაკითხვადი ეტიკეტი არ არის — სარეკლამო ტექსტი მაკეტში ზემოდან
დაედება.
---
Produce three photographs for one social media carousel for a family-run winery in Kakheti. Generate each
frame separately, but they must read as one campaign, shot on one day by one photographer.
Three clauses are shared by all three frames. Repeat each of them word for word in every frame's prompt
and change nothing inside them — this repetition is the mechanism that makes the set hold together.
Lens clause: "50mm equivalent, camera at chest height, held level, f/4, shallow but not extreme depth of
field, no wide-angle distortion at the edges."
Light clause: "It is the last hour before sunset in late September. The sun is low and to the west, out of
frame to camera left. The light is warm, directional and soft-edged; every shadow in the frame runs toward
the lower right; nothing is lit artificially and no lamp is switched on."
Palette clause: "Dusty green, warm ochre, clay brown, unbleached linen, and one deep garnet accent from
the wine itself. Low saturation, natural colour, no colour grading, fine film grain."
Every frame is 4:5 vertical and carries all three clauses in full. The frames differ only in subject.
Frame 1 — the vines. A row of Rkatsiteli vines seen from the end of the row, the row running away from
camera and slightly to the right, leaves front-lit and translucent, the Alazani valley haze in the far
background, no people.
Frame 2 — the hands. A close medium shot of two hands cutting a bunch of grapes with secateurs, cropped at
the forearms, the bunch in the lower right of the frame and the cut stem in the upper left, the leaves
behind falling out of focus. The hands are weathered and unmanicured; no jewellery, no watch, no face in
frame.
Frame 3 — the marani. The mouth of a buried qvevri in a whitewashed vaulted cellar, seen from standing
height looking slightly down, the clay lip filling the lower left third, a glass of deep garnet wine on
the stone slab to the right of it, the vaulted ceiling dissolving into shadow behind. The low western
light enters through a doorway out of frame to camera left.
No text in any of the three frames, no logo, no readable label — the campaign copy is placed over them in
layout.
```

---

### NB-29 · Story ad creative with two reserved bands
`nano-banana` `gemini` — advertising, negative space

**EN**
```
Photograph an advertising creative for a small neighbourhood bakery in Tbilisi, for a 9:16 vertical
story placement, rendered at 4K. Georgian headline and call-to-action copy will be laid over the
image afterwards, so the frame is built around the space that copy needs.

Subject: a round loaf of dark rye, one third of it cut away, on a floured dark wooden board, with a
small linen cloth pushed to the left and a scatter of flour across the board. The cut face of the
loaf shows an open, irregular crumb.

Composition for the 9:16 frame, read top to bottom:
- The top 38 percent is reserved negative space for the headline. It is an even, unbroken deep brown
  field — the out-of-focus bakery wall — with no object, no highlight, no strong edge and no texture
  detail anywhere in it. Nothing may intrude into this band: not the loaf, not the cloth, not a trail
  of flour dust, not a lens flare.
- The middle 44 percent holds the loaf and the board. The loaf sits slightly left of centre, the cut
  face turned toward camera, the board edge crossing the frame at a shallow angle.
- The bottom 18 percent is a second, smaller reserved band for a button-shaped call to action: an
  even dark surface, one stop darker than the loaf, again with nothing in it.

Camera: 50mm equivalent, slightly above the board and angled down about 25 degrees, f/4, the cut face
sharp and the far edge of the board falling soft.

Light: one large soft source high and to camera left, raking across the crust so the crumb and the
flour catch texture; a short soft shadow from the loaf running to the lower right; the reserved top
band stays evenly lit and two stops darker than the crust, so light type will sit legibly on it.

No text anywhere in the image. Leave both reserved bands completely empty.

For your information only, and not to be rendered: the headline that will be placed in the top band
is "ახალი პური ყოველ დილას", set in two lines, and the call to action in the bottom band is
"შეუკვეთე Wolt-ით".
```

**KA**
```
გადაიღე სარეკლამო კადრი თბილისის უბნის პატარა საცხობისთვის, ვერტიკალური სთორის ფორმატში, 9:16,
რენდერი 4K. ქართული სათაური და მოქმედების მოწოდება კადრს შემდეგ ზემოდან დაედება, ამიტომ კომპოზიცია
სწორედ ამ ტექსტისთვის საჭირო ადგილის გარშემო შენდება.

ობიექტი: მუქი ჭვავის მრგვალი პური, მესამედით მოჭრილი, ფქვილიან მუქ ხის დაფაზე; მარცხნივ გადაწეული
პატარა სელის ტილო და დაფაზე მიმოფანტული ფქვილი. პურის ჭრილზე ღია, არათანაბარი ფორიანობა ჩანს.

კომპოზიცია 9:16 კადრისთვის, ზემოდან ქვემოთ:
- ზედა 38 პროცენტი სათაურისთვის დატოვებული თავისუფალი ველია: თანაბარი, უწყვეტი მუქი ყავისფერი
  სიბრტყე — დაბუნდოვნებული საცხობის კედელი — არც ერთი საგნის, კაშკაშა ლაქის, მკვეთრი კიდისა და
  ფაქტურის დეტალის გარეშე. ამ ზოლში ვერაფერი შეიჭრება: ვერც პური, ვერც ტილო, ვერც ფქვილის კვალი,
  ვერც ობიექტივის ბრჭყვიალი.
- შუა 44 პროცენტში პური და დაფაა. პური ცენტრიდან ოდნავ მარცხნივ დგას, ჭრილით კამერისკენ; დაფის კიდე
  კადრს მცირე კუთხით კვეთს.
- ქვედა 18 პროცენტი მეორე, უფრო პატარა დატოვებული ზოლია ღილაკის ფორმის მოწოდებისთვის: თანაბარი მუქი
  ზედაპირი, პურზე ერთი საფეხურით მუქი, ისიც სრულიად ცარიელი.

კამერა: 50 მმ ექვივალენტი, დაფაზე ოდნავ მაღლა, დაახლოებით 25 გრადუსით ქვემოთ დახრილი, f/4 — ჭრილი
მკვეთრია, დაფის შორეული კიდე რბილდება.

განათება: ერთი დიდი, რბილი წყარო მაღლა, კამერიდან მარცხნივ — ირიბად ეცემა ქერქს, რომ ფორიანობამ და
ფქვილმა ფაქტურა დაიჭიროს; პურის მოკლე, რბილი ჩრდილი მარჯვნივ-ქვემოთ მიდის; ზედა დატოვებული ზოლი
თანაბრად განათებული და ქერქზე ორი საფეხურით მუქი რჩება, რომ ღია ფერის ასოები მასზე კარგად წაიკითხოს.

კადრში წარწერა არსად არ არის. ორივე დატოვებული ზოლი სრულიად ცარიელია.

# ტექსტი შეგნებულად არ ვთხოვეთ მოდელს. სათაური „ახალი პური ყოველ დილას“ (ორ ხაზად) და მოწოდება
# „შეუკვეთე Wolt-ით“ მაკეტში დაიდება: გენერირებული ქართული ასოები თითქმის ყოველთვის შესასწორებელი
# გამოდის, ამიტომ ცარიელი ზოლი და დიზაინის პროგრამაში დადებული შრიფტი ერთადერთი საიმედო გზაა.
---
Photograph an advertising creative for a small neighbourhood bakery in Tbilisi, for a 9:16 vertical story
placement, rendered at 4K. Georgian headline and call-to-action copy will be laid over the image
afterwards, so the frame is built around the space that copy needs.
Subject: a round loaf of dark rye, one third of it cut away, on a floured dark wooden board, with a small
linen cloth pushed to the left and a scatter of flour across the board. The cut face of the loaf shows an
open, irregular crumb.
Composition for the 9:16 frame, read top to bottom. The top 38 percent is reserved negative space for the
headline: an even, unbroken deep brown field — the out-of-focus bakery wall — with no object, no
highlight, no strong edge and no texture detail anywhere in it; nothing may intrude into this band, not
the loaf, not the cloth, not a trail of flour dust, not a lens flare. The middle 44 percent holds the loaf
and the board, the loaf slightly left of centre with the cut face turned toward camera and the board edge
crossing the frame at a shallow angle. The bottom 18 percent is a second, smaller reserved band for a
button-shaped call to action: an even dark surface, one stop darker than the loaf, again with nothing in
it.
Camera: 50mm equivalent, slightly above the board and angled down about 25 degrees, f/4, the cut face
sharp and the far edge of the board falling soft.
Light: one large soft source high and to camera left, raking across the crust so the crumb and the flour
catch texture; a short soft shadow from the loaf running to the lower right; the reserved top band stays
evenly lit and two stops darker than the crust, so light type will sit legibly on it.
No text anywhere in the image. Leave both reserved bands completely empty.
```

---

### NB-30 · Professional avatar set from one reference photo
`nano-banana` `gemini` — avatar, consistency

**EN**
```
Produce a set of four professional profile images from the single attached reference photograph of
one person. All four are 1:1 square, rendered at 2K.

The face is the fixed element and comes entirely from the reference photograph. Carry this constraint
in full into every frame, word for word: "The facial structure, the shape of the skull and jaw, the
spacing and shape of the eyes, the nose, the mouth, the ears, the hairline, the apparent age, the skin
tone and the skin texture — including pores, lines and any mole or scar — are taken from the reference
photograph and must not be altered in any way."

Do not slim the face or the body, do not reshape the jaw or the nose, do not enlarge the eyes, do not
whiten teeth, do not remove lines, do not smooth or blur skin, do not change the apparent age in
either direction, do not change hair colour or hairline, and do not change the person's build. This is
a relighting and re-framing job, not a retouching job. Beyond dust and sensor specks, remove nothing
from the face.

What may change across the four frames is the background, the crop and the light. Clothing stays the
same plain dark crew-neck as in the reference in all four.

Frame 1 — head and shoulders, centred, the top of the head about one tenth of the frame height below
the top edge. Plain mid-grey seamless background. One large soft source from camera left at 45
degrees, a white bounce on the right, a soft shadow under the jaw.

Frame 2 — the same crop and the same light as frame 1, on a plain warm off-white background one stop
brighter, with the shadow under the jaw correspondingly lighter.

Frame 3 — a wider crop from mid-chest, the person slightly left of centre, against a softly
out-of-focus neutral office interior with no readable text, no logo and no recognisable object. Soft
daylight from camera left, consistent in direction with the other three frames.

Frame 4 — a tight crop from the collarbone up, the head filling most of the frame, on a plain very
dark charcoal background, one soft source from camera left with a slightly deeper falloff on the
right side of the face.

In all four frames the camera is at eye level, straight on, 85mm equivalent, f/4, the eyes sharp,
expression neutral and relaxed with the mouth closed. Across the whole set the person must be
immediately recognisable as the same individual as in the reference photograph, with the same face at
the same age.
```

**KA**
```
მოამზადე პროფესიული ავატარის ნაკრები — 4 კადრი ერთი მიმაგრებული რეფერენსული ფოტოს მიხედვით. ოთხივე
კვადრატულია, 1:1, რენდერი 2K.

სახე ფიქსირებული ელემენტია და მთლიანად რეფერენსიდან მოდის. ეს შეზღუდვა სიტყვასიტყვით გადაიტანე
ყოველ კადრში: „სახის აგებულება, თავის ქალისა და ყბის ფორმა, თვალების ფორმა და მათ შორის მანძილი,
ცხვირი, პირი, ყურები, თმის ხაზი, ასაკი, კანის ტონი და კანის ფაქტურა — ფორების, ნაოჭების, ხალისა და
ნაიარევის ჩათვლით — რეფერენსული ფოტოდან აიღება და არანაირად არ იცვლება.“

სახე და სხეული არ გამოხდო, ყბა და ცხვირი ხელახლა არ გამოძერწო, თვალები არ გაადიდო, კბილები არ
გაათეთრო, ნაოჭი არ მოაშორო, კანი არ დააგლუვო და არ დაბინდო, ასაკი არცერთი მიმართულებით არ შეცვალო,
თმის ფერი და თმის ხაზი არ შეცვალო, აღნაგობა არ შეცვალო. ეს ხელახალი განათებისა და კადრირების სამუშაოა
და არა რეტუშისა. მტვრისა და მატრიცის ლაქების გარდა სახიდან არაფერი მოაშორო.

ოთხ კადრს შორის იცვლება მხოლოდ ფონი, კადრირება და განათება. ტანსაცმელი ოთხივეგან იგივე რჩება — იგივე
უბრალო, მუქი, მრგვალსაყელოიანი პულოვერი, რაც რეფერენსზეა.

კადრი 1 — თავი და მხრები, ცენტრში, თავის თხემი ზედა კიდიდან კადრის სიმაღლის დაახლოებით მეათედით
ქვემოთ. უბრალო, საშუალო ნაცრისფერი უწყვეტი ფონი. ერთი დიდი, რბილი წყარო კამერიდან მარცხნივ, 45
გრადუსზე, მარჯვნივ თეთრი არეკვლის ფარი, ყბის ქვეშ რბილი ჩრდილი.

კადრი 2 — იგივე კადრირება და იგივე განათება, რაც პირველ კადრს; ფონი უბრალო, თბილი მოთეთრო, ერთი
საფეხურით ნათელი; ყბისქვეშა ჩრდილიც შესაბამისად უფრო ღიაა.

კადრი 3 — უფრო განიერი კადრი მკერდის შუიდან, ადამიანი ცენტრიდან ოდნავ მარცხნივ; უკან დაბუნდოვნებული,
ნეიტრალური საოფისე ინტერიერი — წაკითხვადი ტექსტის, ლოგოსა და ამოსაცნობი საგნის გარეშე. რბილი დღის
შუქი კამერიდან მარცხნივ, დანარჩენი კადრების მიმართულების შესაბამისად.

კადრი 4 — მჭიდრო კადრი ლავიწის ძვლიდან ზემოთ, თავი კადრის უდიდეს ნაწილს ავსებს; ფონი უბრალო, ძალიან
მუქი ნახშირისფერი; ერთი რბილი წყარო კამერიდან მარცხნივ, სახის მარჯვენა მხარეს ოდნავ უფრო ღრმა
ჩაბნელებით.

ოთხივე კადრში კამერა თვალის დონეზეა, პირდაპირ, 85 მმ ექვივალენტი, f/4, თვალები მკვეთრი,
გამომეტყველება ნეიტრალური და მშვიდი, პირი დახურული. მთელ ნაკრებში ადამიანი მყისვე უნდა იცნობოდეს
როგორც რეფერენსზე გამოსახული იგივე ადამიანი — იმავე სახით და იმავე ასაკში.
---
Produce a set of four professional profile images from the single attached reference photograph of one
person. All four are 1:1 square, rendered at 2K.
The face is the fixed element and comes entirely from the reference photograph. Carry this constraint in
full into every frame, word for word: "The facial structure, the shape of the skull and jaw, the spacing
and shape of the eyes, the nose, the mouth, the ears, the hairline, the apparent age, the skin tone and
the skin texture — including pores, lines and any mole or scar — are taken from the reference photograph
and must not be altered in any way."
Do not slim the face or the body, do not reshape the jaw or the nose, do not enlarge the eyes, do not
whiten teeth, do not remove lines, do not smooth or blur skin, do not change the apparent age in either
direction, do not change hair colour or hairline, and do not change the person's build. This is a
relighting and re-framing job, not a retouching job. Beyond dust and sensor specks, remove nothing from
the face.
What may change across the four frames is the background, the crop and the light. Clothing stays the same
plain dark crew-neck as in the reference in all four.
Frame 1 — head and shoulders, centred, the top of the head about one tenth of the frame height below the
top edge. Plain mid-grey seamless background. One large soft source from camera left at 45 degrees, a
white bounce on the right, a soft shadow under the jaw.
Frame 2 — the same crop and the same light as frame 1, on a plain warm off-white background one stop
brighter, with the shadow under the jaw correspondingly lighter.
Frame 3 — a wider crop from mid-chest, the person slightly left of centre, against a softly out-of-focus
neutral office interior with no readable text, no logo and no recognisable object. Soft daylight from
camera left, consistent in direction with the other three frames.
Frame 4 — a tight crop from the collarbone up, the head filling most of the frame, on a plain very dark
charcoal background, one soft source from camera left with a slightly deeper falloff on the right side of
the face.
In all four frames the camera is at eye level, straight on, 85mm equivalent, f/4, the eyes sharp,
expression neutral and relaxed with the mouth closed. Across the whole set the person must be immediately
recognisable as the same individual as in the reference photograph, with the same face at the same age.
```
