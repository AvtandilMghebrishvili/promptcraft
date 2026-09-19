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

---

### NB-31 · Compact digital camera, mid-2000s
`nano-banana` `gemini` — retro, consumer camera

**EN**
```
Make a photograph that looks as though it was taken on a cheap pocket digital camera around 2005,
at a family dinner in a Tbilisi flat. The subject of this brief is the camera, not the styling —
reproduce the way that class of machine actually behaved.

Subject: three generations crowded around a laid table. The grandmother is caught mid-sentence with
one hand lifted; a man in his forties leans in from the left with his elbow on the cloth; a boy sits
on a stool at the near corner, half cut off by the bottom edge. Nobody is posed. Two of them are
looking at the lens, one is not, and one blinked.

Composition: 4:3 horizontal — the native shape of that sensor, not a widescreen crop. The camera is
held at chest height by someone standing at the end of the table, tilted about three degrees to the
left so the wall line behind runs slightly downhill. The zoom sits at its widest, roughly 35mm
equivalent, so the near edge of the table bows outward along the bottom of the frame: mild barrel
distortion, invisible at the centre and strongest in the corners.

Light: the built-in flash is the only real source. It fires straight down the lens axis from about
two metres, flattens every face, removes all modelling from the noses and cheeks, and falls off
fast. The nearest wine glass and the grandmother's forehead are burnt to flat white with no detail
left inside them; the far end of the table sits two stops darker; the corner of the room behind
goes almost black. The ceiling fixture is switched on but contributes almost nothing, so the shadow
of each head lands hard, doubled and low on the wall behind.

Sensor character: small-sensor CCD colour. Thin neutrals leaning slightly cyan, reds that slide
toward orange and clip early, skin that turns waxy where the flash hits hardest, chroma noise
speckling the dark corners, fine detail smeared into mush, a thin white halo of in-camera
sharpening along every high-contrast edge, and blocky JPEG compression breaking up the shadows.

Text in the image: a date stamp in the lower right corner, small, orange-yellow, in a seven-segment
digital face, reading exactly "2005 11 23" and nothing else. Keep it clear of the frame edge by
about two percent of the frame width.

Interior: a Tbilisi flat — a glass-fronted cabinet against the back wall, a bowl of pomegranates
and a half-eaten cake on the table, mismatched chairs, a radiator under the window, curtains drawn.

Nothing modern in frame: no smartphone, no flat screen, no logo, no brand name, no wordmark.
```

**KA**
```
გადაიღე ფოტო ისე, თითქოს 2005 წელს, იაფი ჯიბის ციფრული კამერით გადაუღიათ თბილისურ ბინაში, ოჯახურ
სუფრაზე. ამ ბრიფის მთავარი საგანი კამერაა და არა სტილიზაცია — ზუსტად გაიმეორე, როგორ იქცეოდა ამ
კლასის ტექნიკა.

ობიექტი: სამი თაობა გაშლილ მაგიდას შემოსხდომია. ბებია სიტყვის შუაშია გაჩერებული, ერთი ხელი აწეული
აქვს; ორმოცდაათამდე კაცი მარცხნიდან იდაყვით სუფრაზე გადმოხრილია; ბიჭი ახლო კუთხეში სკამზე ზის და
კადრის ქვედა კიდე მას ნახევრად კვეთს. არავინ პოზირებს: ორი ადამიანი ობიექტივში იყურება, ერთი — არა,
ერთმა კი დაახამხამა.

კომპოზიცია: ჰორიზონტალური კადრი 4:3 — ამ მატრიცის საკუთარი პროპორცია და არა განიერეკრანიანი კროპი.
კამერა მაგიდის ბოლოში მდგომ ადამიანს მკერდის სიმაღლეზე უჭირავს, სამი გრადუსით მარცხნივ გადახრით,
ისე რომ უკანა კედლის ხაზი ოდნავ ქვევით მიდის. ზუმი ყველაზე განიერ მდგომარეობაშია, დაახლოებით 35 მმ
ექვივალენტი — კადრის ქვედა კიდესთან მაგიდის ნაპირი გარეთ იბერება: სუსტი კასრისებრი დამახინჯება,
ცენტრში შეუმჩნეველი და კუთხეებში ყველაზე ძლიერი.

განათება: ერთადერთი რეალური წყარო ჩაშენებული ფლეშია. ის ობიექტივის ღერძიდან, ორი მეტრიდან
პირდაპირ ესროლა სუფრას: ყველა სახეს აბრტყელებს, ცხვირსა და ლოყას მოცულობას აცლის და სწრაფად ეცემა.
უახლოესი ჭიქა და ბებიის შუბლი სუფთა თეთრამდეა გადანათებული — იქ დეტალი აღარ არსებობს; მაგიდის
შორეული ბოლო ორი საფეხურით მუქია; უკანა კუთხე თითქმის შავია. ჭერის ნათურა ანთია, მაგრამ თითქმის
არაფერს მატებს, ამიტომ თითოეული თავის ჩრდილი კედელზე მკვეთრი, გაორებული და დაბლა დაცემულია.

მატრიცის ხასიათი: პატარა CCD მატრიცის ფერი — თხელი, ციანისკენ გადახრილი ნეიტრალები; წითელი
ნარინჯისფერში ცურავს და ადრე იჭრება; კანი იქ, სადაც ფლეში ყველაზე ძლიერ ეცემა, ცვილისებრი ხდება;
მუქ კუთხეებში ფერადი ხმაური აშკარად ჩანს; წვრილი დეტალი აბურდულია; ყოველ კონტრასტულ კიდეზე კამერის
შიდა გამკვეთრების თხელი თეთრი კონტურია; JPEG-შეკუმშვა ჩრდილებს კვადრატებად შლის.

წარწერა სურათში: ქვედა მარჯვენა კუთხეში თარიღის შტამპი — პატარა, ნარინჯისფერ-ყვითელი, სეგმენტური
ციფრული შრიფტით, ზუსტად ასე: „2005 11 23“ და სხვა არაფერი. კადრის კიდიდან დაშორება კადრის სიგანის
დაახლოებით ორი პროცენტი.

ინტერიერი: თბილისური ბინა — შუშისკარიანი სერვანტი უკანა კედელთან, მაგიდაზე ბროწეულის ლანგარი და
ნახევრად შეჭმული ტორტი, სხვადასხვა სკამი, ფანჯრის ქვეშ რადიატორი, ფარდები ჩამოშვებული.

კადრში თანამედროვე არაფერი: არც სმარტფონი, არც ბრტყელი ეკრანი, არც ლოგო, არც ბრენდის სახელი.
---
Make a photograph that looks as though it was taken on a cheap pocket digital camera around 2005, at a
family dinner in a Tbilisi flat. The subject of this brief is the camera, not the styling — reproduce the
way that class of machine actually behaved.
Subject: three generations crowded around a laid table. The grandmother is caught mid-sentence with one
hand lifted; a man in his forties leans in from the left with his elbow on the cloth; a boy sits on a
stool at the near corner, half cut off by the bottom edge. Nobody is posed; two are looking at the lens,
one is not, and one blinked.
Composition: 4:3 horizontal, the native shape of that sensor. The camera is held at chest height by
someone standing at the end of the table, tilted about three degrees to the left. The zoom sits at its
widest, roughly 35mm equivalent, so the near edge of the table bows outward along the bottom of the
frame: mild barrel distortion, invisible at the centre and strongest in the corners.
Light: the built-in flash is the only real source. It fires straight down the lens axis from about two
metres, flattens every face, removes all modelling from noses and cheeks, and falls off fast. The nearest
wine glass and the grandmother's forehead are burnt to flat white with no detail left inside them; the far
end of the table sits two stops darker; the corner of the room behind goes almost black. The ceiling
fixture is on but contributes almost nothing, so the shadow of each head lands hard, doubled and low on
the wall behind.
Sensor character: small-sensor CCD colour — thin neutrals leaning slightly cyan, reds that slide toward
orange and clip early, skin that turns waxy where the flash hits hardest, chroma noise in the dark
corners, fine detail smeared into mush, a thin white halo of in-camera sharpening along every
high-contrast edge, and blocky JPEG compression breaking up the shadows.
Text in the image: a date stamp in the lower right corner, small, orange-yellow, in a seven-segment
digital face, reading exactly "2005 11 23" and nothing else, clear of the frame edge by about two percent
of the frame width.
Interior: a Tbilisi flat — a glass-fronted cabinet against the back wall, a bowl of pomegranates and a
half-eaten cake on the table, mismatched chairs, a radiator under the window, curtains drawn.
Nothing modern in frame: no smartphone, no flat screen, no logo, no brand name, no wordmark.
```

---

### NB-32 · Disposable film camera at night
`nano-banana` `gemini` — retro, flash

**EN**
```
Photograph four friends on the steps of a block courtyard in Tbilisi at night, as a single-use film
camera would record them. Everything in this brief describes the camera's limitations; honour them
rather than improving on them.

Composition: 3:2 horizontal, snapshot framing — the camera is held at the photographer's chest,
about a metre and a half from the nearest person, tilted five degrees, the horizon not level and
the top edge cutting arbitrarily through the doorway arch behind them. One person is slightly out
of frame at the right. Fixed lens, roughly 30mm equivalent, everything from a metre to infinity
nominally in focus and nothing actually crisp.

Light: one tiny flash tube, on the lens axis, with no power to spare. The nearest face is about a
stop and a half over-lit with the shine on the forehead gone to blank white; the person half a
metre further back is correctly exposed; anything past three metres receives nothing at all and
sinks into a muddy green-black. The lit stairwell doorway behind them registers only as a dull
yellow rectangle. Shadows from the flash fall directly behind each person, hard-edged, stacked one
on the next against the wall.

Film and lens character: fast consumer colour negative, developed carelessly. Coarse, clearly
visible grain across the whole frame, heaviest in the dark areas. A green-cyan cast through the
shadows and the mid-tones; whites that never come back to neutral. Heavy mechanical vignetting
from the cheap plastic lens — the corners are a stop and a half down and visibly softer than the
centre. Faint magenta-green colour fringing along the brightest edges.

Motion: the ambient exposure continues after the flash has fired, so a figure walking behind the
group renders as a soft translucent ghost trailing to the right, with the wall visible through it,
while the four flash-lit faces stay frozen and sharp. The same continuation leaves a short warm
streak where a car passed in the far background.

Damp asphalt in the foreground picks up a few specular points from the flash. No legible signage,
no logo, no brand name anywhere in frame.
```

**KA**
```
გადაიღე ოთხი მეგობარი თბილისური ეზოს კიბეზე, ღამით — ისე, როგორც ერთჯერადი ფოტოაპარატი ჩაწერდა.
ამ ბრიფში ყველაფერი კამერის შეზღუდვებს აღწერს; შეასრულე ისინი და არ გააუმჯობესო.

კომპოზიცია: ჰორიზონტალური კადრი 3:2, შემთხვევითი კადრირებით — კამერა ფოტოგრაფს მკერდთან უჭირავს,
უახლოეს ადამიანამდე დაახლოებით მეტრნახევარია, კადრი ხუთი გრადუსითაა გადახრილი, ჰორიზონტი სწორი არ
არის და ზედა კიდე უკან მდებარე თაღოვან კარს თვითნებურად კვეთს. ერთი ადამიანი მარჯვნივ კადრიდან
ნაწილობრივ გასულია. ობიექტივი ფიქსირებული, დაახლოებით 30 მმ ექვივალენტი: ერთი მეტრიდან უსასრულობამდე
ფორმალურად ყველაფერი მკვეთრია და სინამდვილეში არაფერია მკვეთრი.

განათება: ერთი პატარა ფლეში ობიექტივის ღერძზე, მარაგის გარეშე. უახლოესი სახე საფეხურნახევრით
გადანათებულია — შუბლზე ბზინვა სუფთა თეთრად გადავიდა; ნახევარი მეტრით უკან მდგომი ადამიანი სწორადაა
ექსპონირებული; სამ მეტრზე იქით ფლეში ვეღარაფერს აღწევს და იქაურობა მღვრიე მწვანე-შავში იძირება.
უკან განათებული სადარბაზოს კარი მხოლოდ მკრთალ ყვითელ მართკუთხედად აღიბეჭდება. ფლეშის ჩრდილები
პირდაპირ თითოეული ადამიანის უკან ეცემა — მკვეთრი კიდეებით, კედელზე ერთმანეთზე დაწყობილი.

ფირისა და ობიექტივის ხასიათი: მაღალმგრძნობიარე სამოყვარულო ფერადი ნეგატივი, უყურადღებოდ გამჟღავნებული.
მსხვილი, აშკარად ხილული მარცვლოვნება მთელ კადრში, ყველაზე ძლიერი მუქ უბნებში. მწვანე-ციანისკენ
გადახრილი ჩრდილები და შუატონები; თეთრი ნეიტრალურობას ვეღარ უბრუნდება. იაფი პლასტმასის ობიექტივის
ძლიერი ვინიეტი — კუთხეები საფეხურნახევრით მუქია და ცენტრზე შესამჩნევად რბილი. ყველაზე კაშკაშა
კიდეებზე სუსტი მაჯენტა-მწვანე ფერადი კონტური.

მოძრაობა: ფლეშის გასროლის შემდეგ გარემოს ექსპოზიცია გრძელდება, ამიტომ ჯგუფის უკან მოსიარულე ფიგურა
რბილ, გამჭვირვალე აჩრდილად იშლება მარჯვნივ — კედელი მასში გამოსჭვივის — მაშინ როცა ფლეშით
განათებული ოთხი სახე გაყინული და მკვეთრი რჩება. იმავე მიზეზით, შორეულ ფონზე გავლილ მანქანას მოკლე
თბილი ზოლი დარჩა.

წინა პლანზე სველი ასფალტი ფლეშის რამდენიმე ბრჭყვიალა წერტილს იჭერს. კადრში არც წაკითხვადი წარწერა,
არც ლოგო, არც ბრენდის სახელი.
---
Photograph four friends on the steps of a block courtyard in Tbilisi at night, as a single-use film camera
would record them. Everything in this brief describes the camera's limitations; honour them rather than
improving on them.
Composition: 3:2 horizontal, snapshot framing — the camera is held at the photographer's chest, about a
metre and a half from the nearest person, tilted five degrees, the horizon not level and the top edge
cutting arbitrarily through the doorway arch behind them. One person is slightly out of frame at the
right. Fixed lens, roughly 30mm equivalent, everything from a metre to infinity nominally in focus and
nothing actually crisp.
Light: one tiny flash tube on the lens axis with no power to spare. The nearest face is about a stop and
a half over-lit with the shine on the forehead gone to blank white; the person half a metre further back
is correctly exposed; anything past three metres receives nothing and sinks into a muddy green-black. The
lit stairwell doorway behind registers only as a dull yellow rectangle. Flash shadows fall directly behind
each person, hard-edged, stacked one on the next against the wall.
Film and lens character: fast consumer colour negative, carelessly developed. Coarse visible grain across
the whole frame, heaviest in the dark areas. A green-cyan cast through the shadows and mid-tones; whites
that never return to neutral. Heavy mechanical vignetting from the cheap plastic lens — corners a stop and
a half down and visibly softer than the centre. Faint magenta-green fringing along the brightest edges.
Motion: the ambient exposure continues after the flash has fired, so a figure walking behind the group
renders as a soft translucent ghost trailing to the right with the wall visible through it, while the four
flash-lit faces stay frozen and sharp; the same continuation leaves a short warm streak where a car passed
in the far background.
Damp asphalt in the foreground picks up a few specular points from the flash. No legible signage, no logo,
no brand name anywhere in frame.
```

---

### NB-33 · 35mm colour negative in daylight
`nano-banana` `gemini` — film, daylight

**EN**
```
Photograph a woman hanging washing on a balcony at noon, and render it the way colour negative film
renders daylight. Describe nothing by brand — describe the behaviour.

Subject: a woman in her thirties, a dark green cotton dress, bare arms, hair tied back, reaching up
with a wooden peg in her mouth and both hands on a white sheet that is lifting slightly in the
breeze. Two sheets are already up; one has blown across itself.

Composition: 3:2 horizontal, camera at the photographer's eye level about three metres away and
slightly to the left, 50mm equivalent, f/5.6. She stands on the right third, facing left; the line
of washing crosses the top half of the frame; a shaded plastered wall fills the left of the picture
with an open doorway into the dark interior of the flat.

Light: high sun through thin cloud, from camera right and above. The sheets are the brightest thing
in the frame by a wide margin; the shaded wall is four stops below them.

Film behaviour, which is the point of this image:
- Highlight roll-off is long and gradual. The white sheets keep texture and weave all the way up
  into the brightest part of the picture instead of clipping to a flat white; the transition from
  lit cloth to shadowed fold is smooth with no hard edge where the tone gives out.
- Mid-tones run warm. Skin sits slightly toward yellow-red, the plaster reads cream rather than
  grey, and the green dress is a little muted and dusty rather than saturated.
- Shadows hold colour but lose separation, and they are where the grain lives: clearly visible
  grain in the doorway and under the balcony rail, almost none in the bright cloth.
- Gentle halation: where the brilliant sheet edge meets the dark doorway behind it, a soft warm
  glow bleeds a few pixels into the dark side, rounding the edge. It appears only against the
  brightest edges and never around mid-tones.
- Overall contrast is moderate, the blacks are not truly black but a dense warm grey, and a
  faint bloom sits over the whole frame.

Natural, unposed, no retouching of skin, no digital sharpening, no clipped whites anywhere.
```

**KA**
```
გადაიღე ქალი, რომელიც შუადღისას აივანზე თეთრეულს ფენს, და გამოსახულება ისე ააგე, როგორც ფერადი
ნეგატივი დღის შუქს ხედავს. ბრენდი არსად დაასახელო — დაასახელე ქცევა.

ობიექტი: ოცდაათს გადაცილებული ქალი, მუქი მწვანე ბამბის კაბით, შიშველი მკლავებით, უკან შეკრული
თმით; ხელები ზემოთ აქვს აწეული, პირში ხის სამაგრი უჭირავს, ორივე ხელით თეთრ ზეწარს იჭერს, რომელსაც
ნიავი ოდნავ წევს. ორი ზეწარი უკვე გაფენილია; ერთი თავის თავზე გადაკეცილა.

კომპოზიცია: ჰორიზონტალური კადრი 3:2, კამერა ფოტოგრაფის თვალის დონეზე, სამი მეტრის მოშორებით და
ოდნავ მარცხნივ, 50 მმ ექვივალენტი, დიაფრაგმა f/5.6. ქალი მარჯვენა მესამედში დგას, მარცხნივ
მიბრუნებული; თოკი თეთრეულით კადრის ზედა ნახევარს კვეთს; მარცხენა ნაწილს ბათქაშიანი, ჩრდილში მყოფი
კედელი ავსებს, რომელშიც ღია კარი ბინის ბნელ სიღრმეში გადის.

განათება: მაღალი მზე თხელ ღრუბელში, კამერიდან მარჯვნივ და ზემოდან. ზეწრები კადრის ყველაზე კაშკაშა
ნაწილია დიდი სხვაობით; ჩრდილში მყოფი კედელი მათზე ოთხი საფეხურით დაბლაა.

ფირის ქცევა — სწორედ ეს არის ამ კადრის აზრი:
- ნათელი უბნების გადასვლა გრძელი და თანდათანობითია. თეთრი ზეწრები ქსოვილის ფაქტურას ყველაზე
  კაშკაშა ადგილშიც ინარჩუნებენ და ბრტყელ თეთრში არ იჭრებიან; განათებული ქსოვილიდან ჩრდილიან
  ნაკეცამდე გადასვლა რბილია, მკვეთრი საზღვრის გარეშე.
- შუატონები თბილია. კანი ყვითელ-წითელისკენაა გადახრილი, ბათქაში ნაცრისფერზე მეტად კრემისფრად
  იკითხება, მწვანე კაბა კი ნაჯერზე მეტად ოდნავ მიბინდულია, მტვრიანი.
- ჩრდილები ფერს ინარჩუნებენ, მაგრამ დეტალს კარგავენ — და სწორედ იქ ცხოვრობს მარცვლოვნება: კარის
  ღიობსა და აივნის მოაჯირის ქვეშ აშკარად ხილული მარცვალი, ნათელ ქსოვილში კი თითქმის არცერთი.
- რბილი ჰალაცია: იქ, სადაც ზეწრის კაშკაშა კიდე უკან მდებარე ბნელ ღიობს ხვდება, თბილი ნათება რამდენიმე
  პიქსელით შედის მუქ მხარეს და კიდეს ამრგვალებს. ეს მხოლოდ ყველაზე კაშკაშა კიდეებზე ჩნდება და
  შუატონების გარშემო არასდროს.
- საერთო კონტრასტი ზომიერია, შავი ნამდვილი შავი არ არის — მკვრივი თბილი ნაცრისფერია — და მთელ კადრს
  სუსტი ნათების ფარდა ადევს.

ბუნებრივი, არაპოზირებული კადრი: კანის რეტუშის, ციფრული გამკვეთრებისა და გადანათებული თეთრის გარეშე.
---
Photograph a woman hanging washing on a balcony at noon, and render it the way colour negative film
renders daylight. Describe nothing by brand — describe the behaviour.
Subject: a woman in her thirties, a dark green cotton dress, bare arms, hair tied back, reaching up with
a wooden peg in her mouth and both hands on a white sheet lifting slightly in the breeze. Two sheets are
already up; one has blown across itself.
Composition: 3:2 horizontal, camera at eye level about three metres away and slightly to the left, 50mm
equivalent, f/5.6. She stands on the right third facing left; the line of washing crosses the top half of
the frame; a shaded plastered wall fills the left of the picture with an open doorway into the dark
interior of the flat.
Light: high sun through thin cloud, from camera right and above. The sheets are the brightest thing in
the frame by a wide margin; the shaded wall is four stops below them.
Film behaviour, which is the point of this image: highlight roll-off is long and gradual — the white
sheets keep texture and weave all the way up into the brightest part of the picture instead of clipping
to flat white, and the transition from lit cloth to shadowed fold is smooth with no hard edge. Mid-tones
run warm: skin sits slightly toward yellow-red, the plaster reads cream rather than grey, the green dress
is muted and dusty rather than saturated. Shadows hold colour but lose separation, and they are where the
grain lives — clearly visible grain in the doorway and under the balcony rail, almost none in the bright
cloth. Gentle halation: where the brilliant sheet edge meets the dark doorway behind it, a soft warm glow
bleeds a few pixels into the dark side and rounds the edge; it appears only against the brightest edges
and never around mid-tones. Overall contrast is moderate, the blacks are a dense warm grey rather than
true black, and a faint bloom sits over the whole frame.
Natural, unposed, no retouching of skin, no digital sharpening, no clipped whites anywhere.
```

---

### NB-34 · Fisheye, close and wide
`nano-banana` `gemini` — lens, distortion

**EN**
```
Photograph a hand holding a green apple out toward the camera on a flat city rooftop, with a
full-frame fisheye lens. The distortion rules below are what make this read as a real fisheye
rather than a warped photograph — apply all of them together.

Subject and distance: an outstretched right hand, palm up, a small green apple resting on it, the
apple about fifteen centimetres from the front element. Behind the hand, a young man in a grey
t-shirt leans back at arm's length, laughing, his face about seventy centimetres away. Beyond them,
the rooftop: a tar-paper surface, a low parapet, satellite dishes, laundry lines, a city of
mid-rise blocks and, on the horizon, hills.

Composition: 1:1 square, full-frame fisheye — the image fills the whole square, the corners are
filled with picture and there is no black circle and no dark ring. The camera is held low, at
about waist height, tilted slightly upward, roughly thirty centimetres from the hand.

Distortion rules:
- Straight lines that pass exactly through the centre of the frame stay straight. Every other
  straight line bows outward, and the further it sits from the centre the more it bows.
- The parapet and the roof line therefore curve strongly; verticals near the left and right edges
  lean inward toward the top of the frame.
- The horizon is a curve: it bows upward because the camera is tilted up, and it would flatten
  only if it ran exactly through the centre of the frame.
- Scale falls away extremely fast with distance. The apple is enormous — it occupies a fifth of
  the frame — the man's head is a fraction of it, and the buildings behind are small.
- Objects near the frame edge are compressed into narrow slivers, stretched along the edge and
  squeezed across it, while objects near the centre are enlarged and comparatively undistorted.
- The environment wraps all the way round to the edges: the parapet appears on the left, behind
  and on the right, and the photographer's own shoes and shadow enter at the bottom edge.
- Depth of field is enormous: the apple at fifteen centimetres and the hills at the horizon are
  both acceptably sharp. Only the extreme corners soften slightly.
- Light: open sky overhead as the main source, late afternoon sun from camera right putting a
  hard edge on the top of the apple and a long shadow across the roof to the left.

Bright natural colour, moderate contrast, no vignette beyond a slight corner falloff.
```

**KA**
```
გადაიღე ხელი, რომელიც კამერისკენ მწვანე ვაშლს იწვდის, ქალაქის ბრტყელ სახურავზე, სრულკადრიანი
ფიშაი-ობიექტივით. ქვემოთ მოცემული დამახინჯების წესები სწორედ ის არის, რაც კადრს ნამდვილ ფიშაიდ
აქცევს და არა უბრალოდ გადაგრეხილ ფოტოდ — გამოიყენე ისინი ერთად.

ობიექტი და მანძილი: წინ გაწვდილი მარჯვენა ხელი, გულაღმა, ზედ პატარა მწვანე ვაშლი; ვაშლი ობიექტივის
წინა ლინზიდან დაახლოებით თხუთმეტ სანტიმეტრშია. ხელის უკან ნაცრისფერმაისკიანი ახალგაზრდა კაცი
მკლავის სიგრძეზე უკან გადახრილა და იცინის — მისი სახე სამოცდაათ სანტიმეტრზეა. მათ მიღმა სახურავია:
რუბეროიდი, დაბალი პარაპეტი, თეფშისებრი ანტენები, სარეცხის თოკები, საშუალო სართულიანობის ქალაქი და
ჰორიზონტზე მთები.

კომპოზიცია: კვადრატული კადრი 1:1, სრულკადრიანი ფიშაი — გამოსახულება მთელ კვადრატს ავსებს, კუთხეებში
სურათია და არც შავი წრეა, არც მუქი რგოლი. კამერა დაბლაა, წელის სიმაღლეზე, ოდნავ ზემოთ მიმართული,
ხელიდან ოცდაათ სანტიმეტრში.

დამახინჯების წესები:
- სწორი ხაზი, რომელიც ზუსტად კადრის ცენტრზე გადის, სწორად რჩება. ყველა სხვა სწორი ხაზი გარეთ იღუნება
  და რაც უფრო შორსაა ცენტრიდან, მით უფრო ძლიერად.
- ამიტომ პარაპეტი და სახურავის ხაზი ძლიერ იმრუდება; მარცხენა და მარჯვენა კიდესთან ვერტიკალები
  ზემოთკენ შიგნით იხრება.
- ჰორიზონტი მრუდია: ზემოთ იბერება, რადგან კამერა ზემოთაა გადახრილი, და მხოლოდ მაშინ გასწორდებოდა,
  ზუსტად ცენტრზე რომ გადიოდეს.
- მასშტაბი მანძილთან ერთად ძალიან სწრაფად ეცემა. ვაშლი უზარმაზარია — კადრის მეხუთედს იკავებს — კაცის
  თავი მის ნაწილია, უკანა შენობები კი პატარა.
- კადრის კიდესთან მყოფი საგნები ვიწრო ნაფლეთებად იკუმშება — კიდის გასწვრივ იჭიმება და განივად ზნექავს —
  ცენტრთან მყოფი კი გადიდებული და შედარებით დაუმახინჯებელია.
- გარემო კიდეებამდე ეხვევა: პარაპეტი მარცხნივაც ჩანს, უკანაც და მარჯვნივაც, ქვედა კიდიდან კი
  ფოტოგრაფის საკუთარი ფეხსაცმელი და ჩრდილი შემოდის.
- სიღრმის ველი უზარმაზარია: თხუთმეტ სანტიმეტრზე მყოფი ვაშლიც და ჰორიზონტზე მდგარი მთებიც საკმარისად
  მკვეთრია. მხოლოდ უკიდურესი კუთხეები რბილდება ოდნავ.
- განათება: მთავარი წყარო ღია ცაა თავზე; შუადღის შემდგომი მზე კამერიდან მარჯვნივ ვაშლის თავზე მკვეთრ
  კიდეს დებს და სახურავზე გრძელ ჩრდილს მარცხნივ აგდებს.

ნათელი ბუნებრივი ფერი, ზომიერი კონტრასტი, ვინიეტის გარეშე — მხოლოდ კუთხეებში სუსტი დაბნელებით.
---
Photograph a hand holding a green apple out toward the camera on a flat city rooftop, with a full-frame
fisheye lens. The distortion rules below are what make this read as a real fisheye rather than a warped
photograph — apply all of them together.
Subject and distance: an outstretched right hand, palm up, a small green apple resting on it, the apple
about fifteen centimetres from the front element. Behind the hand, a young man in a grey t-shirt leans
back at arm's length, laughing, his face about seventy centimetres away. Beyond them the rooftop: tar
paper, a low parapet, satellite dishes, laundry lines, a city of mid-rise blocks, and hills on the horizon.
Composition: 1:1 square, full-frame fisheye — the image fills the whole square, the corners are filled
with picture, and there is no black circle and no dark ring. The camera is held low at about waist height,
tilted slightly upward, roughly thirty centimetres from the hand.
Distortion rules: straight lines that pass exactly through the centre of the frame stay straight, and
every other straight line bows outward, more the further it sits from the centre. The parapet and roof
line therefore curve strongly; verticals near the left and right edges lean inward toward the top. The
horizon is a curve, bowing upward because the camera is tilted up, and would flatten only if it ran
exactly through the centre. Scale falls away extremely fast with distance: the apple is enormous and
occupies a fifth of the frame, the man's head is a fraction of it, the buildings behind are small. Objects
near the frame edge are compressed into narrow slivers, stretched along the edge and squeezed across it,
while objects near the centre are enlarged and comparatively undistorted. The environment wraps all the
way round: the parapet appears left, behind and right, and the photographer's own shoes and shadow enter
at the bottom edge. Depth of field is enormous — the apple at fifteen centimetres and the hills at the
horizon are both acceptably sharp, with only the extreme corners softening.
Light: open sky overhead as the main source, late afternoon sun from camera right putting a hard edge on
the top of the apple and a long shadow across the roof to the left.
Bright natural colour, moderate contrast, no vignette beyond a slight corner falloff.
```

---

### NB-35 · The photograph on the camera screen
`nano-banana` `gemini` — frame within frame, screen

**EN**
```
Photograph a small camera's rear screen being held up in one hand, with a picture on it. The
finished image is a photograph of a screen — the frame within the frame is the whole idea, so the
inner picture must obey the screen and not the room.

Outer frame: 4:5 vertical. The camera is a plain black compact body with no lettering, no logo and
no wordmark anywhere on it, held in a woman's right hand at chest height — a thin silver ring on
the index finger, short unpolished nails, the thumb resting on the bottom edge of the body. Our
camera is at eye level, about sixty centimetres away, 50mm equivalent, f/4, focused precisely on
the screen surface so that the hand and everything behind it fall soft.

The screen occupies roughly half the frame and is not parallel to our sensor: it is tilted back so
the top edge sits a little further away and the rectangle reads as a slight trapezoid, and turned a
few degrees to the left. Its bezel is a deep matte black, deeper than anything in the picture on it.

The picture on the screen: a wide view of a wooden pier running out into flat grey water at dusk,
a single figure at the far end, a low band of cloud. It is coarser than a real photograph would be —
a faint pixel grid is visible if you look closely, the contrast is pushed and the colours are more
saturated than the scene itself, and the whole inner image glows slightly because it is backlit.

Reflections on the glass: a soft reflection of the overcast sky and the faint silhouette of the
photographer's shoulder lie across the upper left third of the screen and lift the blacks there, so
that part of the inner picture loses contrast. Near the lower right corner, finger smudges catch
the light in a dull smear.

Interface overlay, sitting on the screen surface and not floating in space, in thin white type,
small and slightly aliased:
- along the top, a playback bar with a small solid triangle at the left and, at the right,
  "128/364"
- along the bottom, a strip of shooting data reading "1/60  f/2.8  ISO 800"
- a small battery pictogram in the top right corner, two thirds filled
- a thin white rectangle in the centre left of the screen marking the focus point

Behind the hand, thrown well out of focus: a wet car park under flat overcast light, one distant
parked car, no readable text anywhere.
```

**KA**
```
გადაიღე პატარა კამერის უკანა ეკრანი, რომელიც ერთ ხელში უჭირავთ და რომელზეც სურათია. საბოლოო
გამოსახულება ეკრანის ფოტოა — კადრი კადრში მთელი აზრია, ამიტომ შიდა სურათი ეკრანს უნდა დაემორჩილოს
და არა ოთახს.

გარე კადრი: ვერტიკალური 4:5. კამერა უბრალო შავი კომპაქტური კორპუსია, ზედ არც ერთი ასო, ლოგო ან
ბრენდის ნიშანი; ქალს მარჯვენა ხელში, მკერდის სიმაღლეზე უჭირავს — საჩვენებელ თითზე თხელი ვერცხლის
ბეჭედი, მოკლე, უმანიკურო ფრჩხილები, ცერა თითი კორპუსის ქვედა კიდეზე. ჩვენი კამერა თვალის დონეზეა,
სამოცი სანტიმეტრის მოშორებით, 50 მმ ექვივალენტი, დიაფრაგმა f/4, ფოკუსი ზუსტად ეკრანის ზედაპირზე —
ხელი და ყველაფერი მის უკან რბილად იბუნდოვნება.

ეკრანი კადრის დაახლოებით ნახევარს იკავებს და ჩვენი მატრიცის პარალელური არ არის: უკან არის გადახრილი,
ამიტომ ზედა კიდე ოდნავ შორსაა და მართკუთხედი მსუბუქ ტრაპეციად იკითხება; გარდა ამისა, რამდენიმე
გრადუსით მარცხნივაა შემობრუნებული. ჩარჩო ღრმა მქრქალი შავია — იმაზე მუქი, ვიდრე მასზე გამოსახულ
სურათში რამე.

სურათი ეკრანზე: განიერი ხედი — ხის ბოგირი ბინდში, ბრტყელ ნაცრისფერ წყალში გასული, ბოლოში ერთი
ფიგურა, დაბალი ღრუბლის ზოლი. ის ნამდვილ ფოტოზე უხეშია: ახლოს დაკვირვებისას პიქსელების ბადე ჩანს,
კონტრასტი აწეულია, ფერები თავად სცენაზე უფრო ნაჯერია და მთელი შიდა გამოსახულება ოდნავ ნათობს,
რადგან უკნიდან არის განათებული.

არეკვლა შუშაზე: მოღრუბლული ცისა და ფოტოგრაფის მხრის ბუნდოვანი სილუეტის რბილი არეკვლა ეკრანის ზედა
მარცხენა მესამედზე დევს და იქაურ შავს წევს — შიდა სურათის ეს ნაწილი კონტრასტს კარგავს. ქვედა
მარჯვენა კუთხესთან თითების ნაკვალევი შუქს მქრქალ ლაქად იჭერს.

ინტერფეისი, რომელიც ეკრანის ზედაპირზე ზის და არა ჰაერში — თხელი თეთრი შრიფტი, წვრილი და ოდნავ
დაკბილული:
- ზემოთ დათვალიერების ზოლი: მარცხნივ პატარა სავსე სამკუთხედი, მარჯვნივ „128/364“
- ქვემოთ გადაღების პარამეტრების ზოლი: „1/60  f/2.8  ISO 800“
- ზედა მარჯვენა კუთხეში პატარა ბატარეის პიქტოგრამა, ორ მესამედამდე შევსებული
- ეკრანის მარცხენა შუაში თხელი თეთრი მართკუთხედი — ფოკუსის წერტილი

ხელის უკან, ღრმად დაბუნდოვნებული: სველი ავტოსადგომი ბრტყელ, მოღრუბლულ შუქზე, შორს ერთი გაჩერებული
მანქანა, არსად წაკითხვადი ტექსტი.
---
Photograph a small camera's rear screen being held up in one hand, with a picture on it. The finished
image is a photograph of a screen — the frame within the frame is the whole idea, so the inner picture
must obey the screen and not the room.
Outer frame: 4:5 vertical. The camera is a plain black compact body with no lettering, no logo and no
wordmark anywhere on it, held in a woman's right hand at chest height — a thin silver ring on the index
finger, short unpolished nails, the thumb resting on the bottom edge of the body. Our camera is at eye
level, about sixty centimetres away, 50mm equivalent, f/4, focused precisely on the screen surface so the
hand and everything behind it fall soft.
The screen occupies roughly half the frame and is not parallel to our sensor: it is tilted back so the top
edge sits a little further away and the rectangle reads as a slight trapezoid, and turned a few degrees to
the left. Its bezel is a deep matte black, deeper than anything in the picture on it.
The picture on the screen: a wide view of a wooden pier running out into flat grey water at dusk, a single
figure at the far end, a low band of cloud. It is coarser than a real photograph would be — a faint pixel
grid is visible up close, the contrast is pushed, the colours are more saturated than the scene itself,
and the whole inner image glows slightly because it is backlit.
Reflections on the glass: a soft reflection of the overcast sky and the faint silhouette of the
photographer's shoulder lie across the upper left third of the screen and lift the blacks there, so that
part of the inner picture loses contrast; near the lower right corner, finger smudges catch the light in a
dull smear.
Interface overlay, sitting on the screen surface and not floating in space, in thin white type, small and
slightly aliased: along the top a playback bar with a small solid triangle at the left and, at the right,
"128/364"; along the bottom a strip of shooting data reading "1/60  f/2.8  ISO 800"; a small battery
pictogram in the top right corner, two thirds filled; a thin white rectangle in the centre left of the
screen marking the focus point.
Behind the hand, thrown well out of focus: a wet car park under flat overcast light, one distant parked
car, no readable text anywhere.
```

---

### NB-36 · Magazine cover with exact cover lines
`nano-banana` `gemini` — cover, typography

**EN**
```
Design the front cover of a Georgian culture magazine: a full-bleed studio portrait with a masthead,
three cover lines and a barcode panel. 4:5 vertical, treated as a trimmed cover.

Photograph: a ceramicist in her forties, shot from mid-chest up, standing slightly right of centre
against a flat warm ochre studio ground that runs to all four edges of the cover. She has grey
threading through dark hair pinned up loosely, no make-up beyond a little colour on the mouth, dry
hands with clay dust in the creases, and she wears a heavy oatmeal linen shirt, sleeves pushed up.
She holds an unglazed clay bowl at chest height in both hands and looks straight into the lens with
her chin slightly down and her mouth closed.

Camera and light: 85mm equivalent, f/5.6, camera at her eye level, straight on. One large softbox
from camera left at forty-five degrees and slightly above the eyeline; a white bounce at camera
right returning about one stop, so the shadow side stays open; a second small light on the
background from the right making the ochre a quarter-stop brighter behind her left shoulder to
separate her from the ground. The top left of the cover stays an empty ochre field for the masthead.

Safe margins: every piece of type sits at least six percent of the cover width in from all four
trim edges. Nothing but the photograph reaches the edge; no letter is cropped, touched or crowded.

Text in the image, spelled exactly as written here:
- Masthead across the top, the largest element on the cover, heavy Georgian sans-serif in warm
  off-white, letterspaced slightly, centred: „კონტური“. The top of her hair overlaps the lower
  third of the final letter so she stands in front of the masthead.
- Directly under the masthead, flush right, about one eighth of the masthead height, widely
  letterspaced, off-white: „#47 · ოქტომბერი“
- Down the left edge, a stack of three cover lines, flush left, ragged right, generous line spacing,
  the first in off-white and larger, the other two smaller and in a pale clay pink:
  „თიხა, რომელსაც ხელი ახსოვს“
  „ახალი მარანი გურჯაანში“
  „ინტერვიუ: რატომ ვბრუნდებით სოფელში“
- Bottom right, a plain flat white rectangle about eighteen percent of the cover width and ten
  percent of its height, containing a generic barcode of black vertical bars of varying width with
  a row of small digits beneath reading "9 771234 567890"
- Bottom left, the smallest text on the cover, off-white: „ფასი 9,90 ₾“

No real publication name, no logo, no brand mark, no wordmark on the clothing or the bowl.

# ქართული ასოები დიდი ალბათობით შესასწორებელი გამოვა — განსაკუთრებით დიდ სათაურში და
# „ვბრუნდებით“-ის მსგავს გრძელ სიტყვაში. შედეგი ასოების დონეზე შეამოწმე და საჭიროებისას
# წარწერა დიზაინის პროგრამაში თავიდან დააწყვე. საიმედო ვარიანტი: სთხოვე მოდელს, ტექსტის
# ადგილები ცარიელი დატოვოს („leave the masthead area and the left column as clean flat ochre“)
# და ქართული შრიფტი შენ დაადო.
```

**KA**
```
დააპროექტე ქართული კულტურული ჟურნალის ყდა: სტუდიური პორტრეტი კიდიდან კიდემდე, ზემოდან სათაური,
სამი საყდო ხაზი და შტრიხკოდის ველი. ვერტიკალური კადრი 4:5, მოჭრილი ყდის სახით.

ფოტო: ორმოცს გადაცილებული კერამიკოსი ქალი, მკერდის შუიდან ზევით; ცენტრიდან ოდნავ მარჯვნივ დგას
ერთგვაროვან, თბილ ოხრისფერ სტუდიურ ფონზე, რომელიც ყდის ოთხივე კიდემდე აღწევს. მუქ თმაში ჭაღარა
უვლის, თმა ზემოთ თავისუფლად აქვს აკრეფილი, მაკიაჟი მხოლოდ ტუჩებზეა, ხელები მშრალი და თითების
ნაკეცებში თიხის მტვერი შერჩენილი. აცვია მძიმე, შვრიისფერი სელის პერანგი, სახელოები აწეული. ორივე
ხელით მკერდის სიმაღლეზე უჭირავს მოუჭიქავი თიხის თასი და პირდაპირ ობიექტივში იყურება, ნიკაპი ოდნავ
დახრილი, პირი დახურული.

კამერა და განათება: 85 მმ ექვივალენტი, დიაფრაგმა f/5.6, კამერა მის თვალის დონეზე, პირდაპირ. ერთი
დიდი რბილი წყარო კამერიდან მარცხნივ, ორმოცდახუთ გრადუსზე და თვალის ხაზზე ოდნავ მაღლა; მარჯვნივ
თეთრი ამრეკლი ერთი საფეხურით აბრუნებს შუქს, ამიტომ ჩრდილიანი მხარე ღია რჩება; მეორე, პატარა წყარო
მარჯვნიდან ფონს ანათებს და მარცხენა მხრის უკან ოხრისფერს მეოთხედი საფეხურით ანათლებს, რომ ფიგურა
ფონს მოსწყდეს. ყდის ზედა მარცხენა ნაწილი ცარიელ ოხრისფერ ველად რჩება სათაურისთვის.

უსაფრთხო ველი: ყოველი წარწერა ოთხივე კიდიდან ყდის სიგანის მინიმუმ ექვსი პროცენტითაა შიგნით.
კიდემდე მხოლოდ ფოტო აღწევს; არცერთი ასო არ იჭრება, კიდეს არ ეხება და არ იჭყლიტება.

წარწერა სურათში, ზუსტად ასე:
- სათაური ზემოთ, ყდის ყველაზე დიდი ელემენტი, მძიმე ქართული უსერიფო შრიფტი თბილ მოთეთრო ფერში,
  ოდნავ გაფართოებული ასოთაშორისი მანძილით, ცენტრში: „კონტური“. თმის თხემი ბოლო ასოს ქვედა მესამედს
  გადაფარავს, ასე რომ ქალი სათაურის წინ დგას.
- პირდაპირ სათაურის ქვეშ, მარჯვენა კიდეზე გასწორებული, სათაურის სიმაღლის დაახლოებით მერვედი,
  გაფართოებული ასოთაშორისი მანძილით, მოთეთროში: „#47 · ოქტომბერი“
- მარცხენა კიდეზე სამი საყდო ხაზი სვეტად, მარცხნივ გასწორებული, მარჯვნივ თავისუფალი, დიდი
  სტრიქონთაშორისი მანძილით; პირველი უფრო დიდი და მოთეთრო, დანარჩენი ორი უფრო პატარა და ღია
  თიხისფერ-ვარდისფერი:
  „თიხა, რომელსაც ხელი ახსოვს“
  „ახალი მარანი გურჯაანში“
  „ინტერვიუ: რატომ ვბრუნდებით სოფელში“
- ქვედა მარჯვენა კუთხეში ერთგვაროვანი თეთრი მართკუთხედი — ყდის სიგანის დაახლოებით თვრამეტი და
  სიმაღლის ათი პროცენტი — რომელშიც სხვადასხვა სისქის შავვერტიკალზოლებიანი ზოგადი შტრიხკოდია და
  ქვეშ წვრილი ციფრების რიგი: „9 771234 567890“
- ქვედა მარცხენა კუთხეში, ყდის ყველაზე პატარა ტექსტი, მოთეთროში: „ფასი 9,90 ₾“

არცერთი არსებული გამოცემის სახელი, არც ლოგო, არც სავაჭრო ნიშანი; ტანსაცმელსა და თასზე წარწერა არ იყოს.

# ქართული ასოები დიდი ალბათობით შესასწორებელი გამოვა — განსაკუთრებით დიდ სათაურში და „ვბრუნდებით“-ის
# მსგავს გრძელ სიტყვაში. შედეგი ასოების დონეზე შეამოწმე და საჭიროებისას წარწერა დიზაინის პროგრამაში
# თავიდან დააწყვე. საიმედო ვარიანტი: სთხოვე მოდელს, ტექსტის ადგილები ცარიელი დატოვოს („leave the
# masthead area and the left column as clean flat ochre“) და ქართული შრიფტი შენ დაადო.
---
Design the front cover of a Georgian culture magazine: a full-bleed studio portrait with a masthead, three
cover lines and a barcode panel. 4:5 vertical, treated as a trimmed cover.
Photograph: a ceramicist in her forties, shot from mid-chest up, standing slightly right of centre against
a flat warm ochre studio ground that runs to all four edges. Grey threading through dark hair pinned up
loosely, no make-up beyond a little colour on the mouth, dry hands with clay dust in the creases, a heavy
oatmeal linen shirt with the sleeves pushed up. She holds an unglazed clay bowl at chest height in both
hands and looks straight into the lens, chin slightly down, mouth closed.
Camera and light: 85mm equivalent, f/5.6, camera at her eye level, straight on. One large softbox from
camera left at forty-five degrees and slightly above the eyeline; a white bounce at camera right returning
about one stop so the shadow side stays open; a second small light on the background from the right making
the ochre a quarter-stop brighter behind her left shoulder. The top left of the cover stays an empty ochre
field for the masthead.
Safe margins: every piece of type sits at least six percent of the cover width in from all four trim edges.
Nothing but the photograph reaches the edge; no letter is cropped, touched or crowded.
Text in the image, spelled exactly as written here: masthead across the top, the largest element on the
cover, heavy Georgian sans-serif in warm off-white, slightly letterspaced, centred: "კონტური", with the top
of her hair overlapping the lower third of the final letter so she stands in front of it. Directly under
the masthead, flush right, about one eighth of the masthead height, widely letterspaced, off-white:
"#47 · ოქტომბერი". Down the left edge, a stack of three cover lines, flush left, ragged right, generous
line spacing, the first in off-white and larger, the other two smaller and in a pale clay pink:
"თიხა, რომელსაც ხელი ახსოვს" / "ახალი მარანი გურჯაანში" / "ინტერვიუ: რატომ ვბრუნდებით სოფელში". Bottom
right, a plain flat white rectangle about eighteen percent of the cover width and ten percent of its
height, containing a generic barcode of black vertical bars of varying width with a row of small digits
beneath reading "9 771234 567890". Bottom left, the smallest text on the cover, off-white: "ფასი 9,90 ₾".
Every Georgian letter must be correctly formed, level and fully legible. No real publication name, no logo,
no brand mark, no wordmark on the clothing or the bowl.
```

---

### NB-37 · One face, three lighting schemes
`nano-banana` `gemini` — headshot, lighting

**EN**
```
Produce three professional headshots of the same man under three named lighting schemes. Run them
as three separate generations from the identical description block below — do not lay them out as
one sheet and do not build a grid.

The person, carried word for word into all three prompts:
"A man in his late thirties, close-cropped dark hair receding a little at the temples, a trimmed
black beard with a few grey hairs at the chin, brown eyes, a straight nose broken once and set
very slightly off-centre, a small pale scar through the outer half of the left eyebrow, olive skin
with open pores and visible texture, wearing a plain charcoal merino crew-neck."

Held constant in all three: 4:5 vertical, head and shoulders, the top of the head about one tenth
of the frame height below the top edge, the person centred, camera at his eye level and straight
on, 85mm equivalent, f/4, the near eye critically sharp, mouth closed, expression neutral and
relaxed, a plain mid-grey seamless background, the same camera distance and the same white balance
in every frame. Skin texture is not smoothed and nothing is retouched away.

Scheme 1 — Rembrandt. One medium softbox at camera left, forty-five degrees round from the lens
axis and forty-five degrees above the eyeline. The shadow cast by the nose runs down and meets the
shadow rising from the right cheek, leaving one small lit triangle on the right cheek no wider than
his eye and no longer than his nose. No fill of any kind: the shadow side sits three stops under
the lit side, and the background falls off to the right.

Scheme 2 — clamshell. One large source directly in front of him and above, tipped down at about
thirty degrees, and a white reflector directly below at chest height tipped up. Shadows almost
disappear; only a small shadow sits directly under the nose and under the lower lip. Two
catchlights in each eye, one at the top of the iris and one at the bottom. The face is evenly lit
across its whole width, falling off about one stop at the ears, and the background is a full stop
brighter than in scheme 1.

Scheme 3 — split with a rim. The key is at ninety degrees to camera left, at eye level, close in
and undiffused, so the lit half and the dark half divide down the ridge of the nose. No fill at
all: the shadow half sits four stops under and loses all detail. Behind him and to camera right, a
narrow hard rim light skims the edge of the right jaw and the top of the right shoulder, a stop
brighter than the key and spilling onto nothing else. The background goes nearly black.

In all three the man must read as the same individual at the same age: only the light changes.
```

**KA**
```
გააკეთე ერთი და იმავე კაცის 3 პროფესიული პორტრეტი განათების 3 დასახელებული სქემით. ეს სამი ცალკე
გენერაციაა ქვემოთ მოცემული ერთი და იმავე აღწერის ბლოკიდან — ერთ ფურცლად არ ააწყო და ბადედ არ
დაალაგო.

ადამიანი — ეს აღწერა სამივე პრომპტში სიტყვასიტყვით გადადის:
„ოცდაათის ბოლოში მყოფი კაცი: მოკლედ შეკრეჭილი მუქი თმა, საფეთქლებთან ოდნავ შემცირებული; მოვლილი
შავი წვერი, ნიკაპთან რამდენიმე ჭაღარა ღერით; ყავისფერი თვალები; სწორი ცხვირი, ერთხელ მოტეხილი და
ძალიან ოდნავ გვერდზე დამჯდარი; მარცხენა წარბის გარე ნახევარზე პატარა ღია ნაიარევი; ზეთისხილისფერი
კანი ღია ფორებითა და ხილული ფაქტურით; აცვია უბრალო, ნახშირისფერი, მრგვალსაყელოიანი მერინოს პულოვერი.“

სამივეში უცვლელია: ვერტიკალური კადრი 4:5, თავი და მხრები, თავის თხემი ზედა კიდიდან კადრის სიმაღლის
დაახლოებით მეათედით ქვემოთ, ფიგურა ცენტრში, კამერა მის თვალის დონეზე და პირდაპირ, 85 მმ ექვივალენტი,
დიაფრაგმა f/4, ახლო თვალი სრულიად მკვეთრი, პირი დახურული, გამომეტყველება ნეიტრალური და მშვიდი, ფონი
უბრალო, საშუალო ნაცრისფერი და უწყვეტი; კამერამდე მანძილი და თეთრის ბალანსი სამივე კადრში ერთი და იგივე.
კანის ფაქტურა არ გლუვდება და არაფერი იშლება რეტუშით.

სქემა 1 — რემბრანდტისეული. ერთი საშუალო რბილი წყარო კამერიდან მარცხნივ, ობიექტივის ღერძიდან
ორმოცდახუთ გრადუსზე და თვალის ხაზიდან ორმოცდახუთი გრადუსით მაღლა. ცხვირის ჩრდილი ქვემოთ ეშვება და
მარჯვენა ლოყიდან ამომავალ ჩრდილს ხვდება — მარჯვენა ლოყაზე რჩება ერთი პატარა განათებული სამკუთხედი,
თვალზე არა უფრო განიერი და ცხვირზე არა უფრო გრძელი. შემავსებელი შუქი საერთოდ არ არის: ჩრდილიანი
მხარე განათებულზე სამი საფეხურით დაბლაა, ფონი კი მარჯვნივ ჩაბნელებაში გადადის.

სქემა 2 — „ნიჟარა“. ერთი დიდი წყარო პირდაპირ მის წინ და ზემოთ, ოცდაათი გრადუსით ქვემოთ დახრილი, და
თეთრი ამრეკლი პირდაპირ ქვემოთ, მკერდის სიმაღლეზე, ზემოთ მიმართული. ჩრდილები თითქმის ქრება: რჩება
მხოლოდ პატარა ჩრდილი ცხვირისა და ქვედა ტუჩის ქვეშ. თითოეულ თვალში ორი ბზინვაა — ერთი გუგის თავზე,
ერთი ქვემოთ. სახე მთელ სიგანეზე თანაბრადაა განათებული და ყურებთან ერთი საფეხურით ეცემა; ფონი პირველ
სქემაზე მთელი საფეხურით ნათელია.

სქემა 3 — გაპობილი განათება მოჭრილი კონტურით. მთავარი წყარო კამერიდან მარცხნივ, ოთხმოცდაათ გრადუსზე,
თვალის დონეზე, ახლოს და გაუფანტავი — განათებული და ბნელი ნახევარი ცხვირის ქედზე იყოფა. შემავსებელი
შუქი სრულიად არ არის: ჩრდილიანი ნახევარი ოთხი საფეხურით დაბლაა და დეტალს მთლიანად კარგავს. უკან და
კამერიდან მარჯვნივ ვიწრო, მკვეთრი კონტრაჟური შუქი მარჯვენა ყბის კიდესა და მარჯვენა მხრის თავს
ირიბად ეხება — მთავარ წყაროზე ერთი საფეხურით ნათელია და სხვაგან არსად არ იფანტება. ფონი თითქმის შავია.

სამივე კადრში კაცი ერთსა და იმავე ადამიანად და ერთსა და იმავე ასაკში უნდა იკითხებოდეს: იცვლება
მხოლოდ შუქი.
---
Produce three professional headshots of the same man under three named lighting schemes. Run them as three
separate generations from the identical description block below — do not lay them out as one sheet and do
not build a grid.
The person, carried word for word into all three prompts: "A man in his late thirties, close-cropped dark
hair receding a little at the temples, a trimmed black beard with a few grey hairs at the chin, brown eyes,
a straight nose broken once and set very slightly off-centre, a small pale scar through the outer half of
the left eyebrow, olive skin with open pores and visible texture, wearing a plain charcoal merino crew-neck."
Held constant in all three: 4:5 vertical, head and shoulders, the top of the head about one tenth of the
frame height below the top edge, the person centred, camera at his eye level and straight on, 85mm
equivalent, f/4, the near eye critically sharp, mouth closed, expression neutral and relaxed, a plain
mid-grey seamless background, the same camera distance and the same white balance in every frame. Skin
texture is not smoothed and nothing is retouched away.
Scheme 1 — Rembrandt. One medium softbox at camera left, forty-five degrees round from the lens axis and
forty-five degrees above the eyeline. The shadow cast by the nose runs down and meets the shadow rising
from the right cheek, leaving one small lit triangle on the right cheek no wider than his eye and no longer
than his nose. No fill of any kind: the shadow side sits three stops under the lit side, and the background
falls off to the right.
Scheme 2 — clamshell. One large source directly in front of him and above, tipped down at about thirty
degrees, and a white reflector directly below at chest height tipped up. Shadows almost disappear; only a
small shadow sits directly under the nose and under the lower lip. Two catchlights in each eye, one at the
top of the iris and one at the bottom. The face is evenly lit across its whole width, falling off about one
stop at the ears, and the background is a full stop brighter than in scheme 1.
Scheme 3 — split with a rim. The key is at ninety degrees to camera left, at eye level, close in and
undiffused, so the lit half and the dark half divide down the ridge of the nose. No fill at all: the shadow
half sits four stops under and loses all detail. Behind him and to camera right, a narrow hard rim light
skims the edge of the right jaw and the top of the right shoulder, a stop brighter than the key and
spilling onto nothing else. The background goes nearly black.
In all three the man must read as the same individual at the same age: only the light changes.
```

---

### NB-38 · Available light indoors, one window
`nano-banana` `gemini` — portrait, available light

**EN**
```
Photograph a woman at a kitchen table in the late afternoon using the window as the only source,
on colour negative film. The exposure decision is the whole picture, so it is written out below and
must be followed rather than corrected.

Subject: a woman in her sixties, short grey hair, reading glasses pushed up on her head, both hands
wrapped around a cup of tea that has gone cold. She is looking down and slightly left, at nothing
in particular; her mouth is relaxed and she is not performing an expression.

Composition: 4:5 vertical, camera at her seated eye level, about a metre and a half away, 50mm
equivalent, aperture wide at f/2. She sits on the right third facing left into the light; the empty
lit third of the table fills the bottom left of the frame with a bread board and a glass on it; the
wall behind her occupies the upper left.

Light: one tall window at camera left, a metre and a half from her, facing away from the sun so no
direct beam enters — only open sky. Every lamp in the flat is off and the door to the hall is shut.
There is no reflector, no bounce card, no second source of any kind.

Exposure reasoning: expose for the lit side of her face and let everything else go where it goes.
That places the window-side cheek in the upper mid-tones and drops the wall behind her four stops
under, into a near-black in which only the corner of a picture frame is barely readable. Do not
lift the shadows, do not add fill, do not bounce anything back from camera right. The shadow side
of her face keeps only a thin edge of light where the cheek turns toward the window, and the far
side of the room reads as one undifferentiated dark mass.

Falloff: light from a window close to a subject falls away fast, so her near hand is a full stop
brighter than her far hand, the rim of the cup catches a thin specular line, and the far edge of
the table is already dim.

Film character: a fast colour negative used near the bottom of its exposure range. Grain is coarse
and obvious in the shadows and almost invisible in the lit cheek; the shadows drift slightly cool
and green while the lit skin stays neutral-warm; contrast is low and the blacks are soft.

Focus: the near eye is sharp, the far ear is already soft, the background is fully out of focus.
```

**KA**
```
გადაიღე ქალი სამზარეულოს მაგიდასთან, შუადღის მიწურულს, ფერად ნეგატივზე — ერთადერთი წყარო ფანჯარაა.
ექსპოზიციის გადაწყვეტილება აქ თავად სურათია, ამიტომ ქვემოთ სიტყვასიტყვითაა გაწერილი და შესასრულებელია,
და არა შესასწორებელი.

ობიექტი: სამოცს გადაცილებული ქალი, მოკლე ჭაღარა თმით, საკითხავი სათვალე თმაზე აწეული; ორივე ხელით
გაციებული ჩაის ჭიქას ეჭიდება. ქვემოთ და ოდნავ მარცხნივ იყურება, არსაით კონკრეტულად; პირი მოდუნებული
აქვს და გამომეტყველებას არ თამაშობს.

კომპოზიცია: ვერტიკალური კადრი 4:5, კამერა მისი მჯდომარე თვალის დონეზე, მეტრნახევრის მოშორებით,
50 მმ ექვივალენტი, დიაფრაგმა ფართოდ გახსნილი — f/2. ქალი მარჯვენა მესამედში ზის, მარცხნივ, შუქისკენ
მიბრუნებული; მაგიდის ცარიელი განათებული მესამედი კადრის ქვედა მარცხენა ნაწილს ავსებს — ზედ პურის
დაფა და ჭიქაა; ზედა მარცხენა ნაწილს მის უკან მდებარე კედელი იკავებს.

განათება: კამერიდან მარცხნივ ერთი მაღალი ფანჯარა, მისგან მეტრნახევარში, მზისგან პირშექცეული — პირდაპირი
სხივი არ შემოდის, მხოლოდ ღია ცის შუქი. ბინაში ყველა ნათურა ჩამქრალია და დერეფნის კარი დახურულია.
არც ამრეკლია, არც თეთრი ფარი, არც რაიმე მეორე წყარო.

ექსპოზიციის ლოგიკა: ექსპოზიცია სახის განათებულ მხარეზე დააყენე და დანარჩენი იქ წავიდეს, სადაც წავა.
ამით ფანჯრისკენა ლოყა ზედა შუატონებში დაჯდება, უკანა კედელი კი ოთხი საფეხურით ქვემოთ, თითქმის შავში
ჩავა, სადაც მხოლოდ სურათის ჩარჩოს კუთხე თუ ამოიკითხება. ჩრდილები არ ასწიო, შემავსებელი შუქი არ
დაამატო, კამერიდან მარჯვნივ არაფერი აირეკლო. სახის ჩრდილიან მხარეს მხოლოდ თხელი განათებული კიდე
რჩება იქ, სადაც ლოყა ფანჯრისკენ ტრიალდება; ოთახის შორეული ნაწილი ერთიან, დაუნაწევრებელ მუქ მასად
იკითხება.

დაცემა: ობიექტთან ახლოს მდგარი ფანჯრის შუქი სწრაფად ეცემა — ახლო ხელი შორეულ ხელზე მთელი საფეხურით
ნათელია, ჭიქის კიდე თხელ ბზინვის ხაზს იჭერს, მაგიდის შორეული ნაპირი კი უკვე ბნელია.

ფირის ხასიათი: მაღალმგრძნობიარე ფერადი ნეგატივი, საკუთარი ექსპოზიციის დიაპაზონის ქვედა ზღვართან.
მარცვლოვნება ჩრდილებში მსხვილი და აშკარაა, განათებულ ლოყაზე კი თითქმის უხილავი; ჩრდილები ოდნავ ცივ
და მწვანე ტონში მიდის, განათებული კანი კი ნეიტრალურ-თბილი რჩება; კონტრასტი დაბალია და შავი რბილი.

ფოკუსი: ახლო თვალი მკვეთრია, შორეული ყური უკვე რბილი, ფონი სრულიად დაბუნდოვნებული.
---
Photograph a woman at a kitchen table in the late afternoon using the window as the only source, on colour
negative film. The exposure decision is the whole picture, so it is written out below and must be followed
rather than corrected.
Subject: a woman in her sixties, short grey hair, reading glasses pushed up on her head, both hands wrapped
around a cup of tea that has gone cold. She is looking down and slightly left, at nothing in particular;
her mouth is relaxed and she is not performing an expression.
Composition: 4:5 vertical, camera at her seated eye level, about a metre and a half away, 50mm equivalent,
aperture wide at f/2. She sits on the right third facing left into the light; the empty lit third of the
table fills the bottom left of the frame with a bread board and a glass on it; the wall behind her occupies
the upper left.
Light: one tall window at camera left, a metre and a half from her, facing away from the sun so no direct
beam enters — only open sky. Every lamp in the flat is off and the door to the hall is shut. There is no
reflector, no bounce card, no second source of any kind.
Exposure reasoning: expose for the lit side of her face and let everything else go where it goes. That
places the window-side cheek in the upper mid-tones and drops the wall behind her four stops under, into a
near-black in which only the corner of a picture frame is barely readable. Do not lift the shadows, do not
add fill, do not bounce anything back from camera right. The shadow side of her face keeps only a thin edge
of light where the cheek turns toward the window, and the far side of the room reads as one
undifferentiated dark mass.
Falloff: light from a window close to a subject falls away fast, so her near hand is a full stop brighter
than her far hand, the rim of the cup catches a thin specular line, and the far edge of the table is
already dim.
Film character: a fast colour negative used near the bottom of its exposure range — grain coarse and
obvious in the shadows and almost invisible in the lit cheek, shadows drifting slightly cool and green
while the lit skin stays neutral-warm, low contrast, soft blacks.
Focus: the near eye is sharp, the far ear is already soft, the background is fully out of focus.
```

---

### NB-39 · Long exposure on a night street
`nano-banana` `gemini` — long exposure, night

**EN**
```
Photograph a street in Vake, Tbilisi, at night with the shutter held open a long time. Do not think
in numbers: the shutter stays open long enough that a person walking at a normal pace crosses a
third of the frame before it closes. Everything in this brief follows from that one fact.

Composition: 16:9 horizontal. The camera is locked on a tripod on the pavement, at chest height,
level, 35mm equivalent, aperture stopped well down. The street runs away to the right; plane trees
line the near pavement; a nineteen-sixties apartment block with a row of lit windows and enclosed
balconies fills the left two thirds; a small kiosk sits at the right third with a zebra crossing in
front of it.

What is perfectly sharp, because the camera never moved: the trees down to the edge of every leaf,
the render and the balcony rails on the block, the window frames, the kiosk, the painted stripes of
the crossing, the kerb, and the litter in the gutter. Sharpness here is the evidence that the camera
was fixed.

What is a smear, because it moved while the shutter was open: the pedestrians. A man who kept
walking across the crossing has become a faint translucent band with no face, no hands and no
edges, and the railing behind him is clearly visible through his body. A woman who stopped halfway
for part of the exposure leaves a denser, more solid ghost exactly where she paused, fading at both
ends into nothing.

The marshutka: a minibus crossed the frame from left to right and its body has vanished entirely.
What it left is light. Its headlights drew two continuous warm-white lines running left to right
across the lower third at bumper height; its tail lights drew two red lines just above and behind
them; a row of small amber roof points drew a thin dotted line higher still. Every trail runs in
one direction only, left to right, unbroken, with no doubling, no dashes and no reversal anywhere.
Where the marshutka braked before the crossing, the red lines thicken and bend slightly upward.

Point sources: the streetlamps and the lit windows render as bright points with a clean
multi-pointed star, because the diaphragm is closed down. The wet asphalt returns all of it as
wider, softer, vertically stretched reflections directly beneath each source.

Exposure decision: expose for the lit facade and let the sky go black. Do not brighten the sky, do
not recover the shadows between the trees, and do not add haze or glow that the lights do not make
themselves.

No legible signage, no logo, no brand name, and no recognisable individual anywhere in frame.
```

**KA**
```
გადაიღე ვაკის ქუჩა ღამით, დიდხანს გახსნილი ჩამკეტით. ციფრებით არ იფიქრო: ჩამკეტი იმდენ ხანს რჩება
ღია, რომ ჩვეულებრივი ნაბიჯით მოსიარულე ადამიანი კადრის მესამედს გადაკვეთს, სანამ დაიხურება. ამ ბრიფში
ყველაფერი სწორედ ამ ერთი ფაქტიდან გამომდინარეობს.

კომპოზიცია: ჰორიზონტალური კადრი 16:9. კამერა ტროტუარზე, შტატივზე ფიქსირებულია, მკერდის სიმაღლეზე,
სწორად დაყენებული, 35 მმ ექვივალენტი, დიაფრაგმა კარგად შევიწროებული. ქუჩა მარჯვნივ მიდის; ახლო
ტროტუარს ჭადრები უწყვია; მარცხენა ორ მესამედს სამოციანი წლების საცხოვრებელი კორპუსი ავსებს —
განათებული ფანჯრების რიგითა და შეშუშებული აივნებით; მარჯვენა მესამედში პატარა ჯიხურია, მის წინ კი
გადასასვლელის ზოლები.

რა არის სრულიად მკვეთრი, რადგან კამერა არ დაძრულა: ჭადრები ყოველი ფოთლის კიდემდე, კორპუსის ბათქაში
და აივნების მოაჯირები, ფანჯრების ჩარჩოები, ჯიხური, გადასასვლელის შეღებილი ზოლები, ბორდიური და
ღარში ჩარჩენილი ნაგავი. აქ მკვეთრობა თავად არის იმის მტკიცებულება, რომ კამერა უძრავად იდგა.

რა გაიშალა ლაქად, რადგან ჩამკეტის ღიად ყოფნისას მოძრაობდა: ქვეითები. კაცი, რომელიც გადასასვლელზე
გაუჩერებლად გადიოდა, მკრთალ, გამჭვირვალე ზოლად იქცა — არც სახე აქვს, არც ხელები, არც კიდეები — და
მის სხეულში უკანა მოაჯირი აშკარად ჩანს. ქალი, რომელიც ექსპოზიციის ნაწილის განმავლობაში შუა გზაზე
შეჩერდა, ზუსტად იქ, სადაც გაჩერდა, უფრო მკვრივ აჩრდილად დარჩა, რომელიც ორივე ბოლოსკენ ნელ-ნელა ქრება.

მარშრუტკა: მიკროავტობუსმა კადრი მარცხნიდან მარჯვნივ გადაკვეთა და მისი კორპუსი მთლიანად გაქრა.
დარჩა მხოლოდ შუქი. ფარებმა ქვედა მესამედში, ბამპერის სიმაღლეზე, მარცხნიდან მარჯვნივ ორი უწყვეტი
თბილ-თეთრი ხაზი გაავლეს; უკანა შუქებმა მათ ზემოთ და უკან ორი წითელი ხაზი; სახურავის წვრილმა
ქარვისფერმა წერტილებმა კი კიდევ უფრო მაღლა თხელი წყვეტილი ხაზი. ყოველი კვალი მხოლოდ ერთი
მიმართულებით მიდის — მარცხნიდან მარჯვნივ, უწყვეტად, არსად გაორების, დახლეჩისა და უკუსვლის გარეშე.
იქ, სადაც მარშრუტკამ გადასასვლელამდე დაამუხრუჭა, წითელი ხაზები სქელდება და ოდნავ მაღლა იხრება.

წერტილოვანი წყაროები: ქუჩის ფარნები და განათებული ფანჯრები კაშკაშა წერტილებად იკითხება სუფთა,
მრავალსხივიანი ვარსკვლავით, რადგან დიაფრაგმა შევიწროებულია. სველი ასფალტი ამ ყველაფერს უკან
აბრუნებს — უფრო განიერი, რბილი, ვერტიკალურად გაჭიმული ანარეკლებით, პირდაპირ ყოველი წყაროს ქვეშ.

ექსპოზიციის გადაწყვეტილება: ექსპოზიცია განათებულ ფასადზე დააყენე და ცა შავად გაუშვი. ცა არ გაანათლო,
ხეებს შორის ჩრდილები არ ამოიყვანო და ისეთი ნისლი ან ნათება არ დაამატო, რომელსაც თავად ფარნები არ
ქმნიან.

კადრში არც წაკითხვადი წარწერა, არც ლოგო, არც ბრენდის სახელი და არცერთი ამოსაცნობი ადამიანი.
---
Photograph a street in Vake, Tbilisi, at night with the shutter held open a long time. Do not think in
numbers: the shutter stays open long enough that a person walking at a normal pace crosses a third of the
frame before it closes. Everything in this brief follows from that one fact.
Composition: 16:9 horizontal. The camera is locked on a tripod on the pavement, at chest height, level,
35mm equivalent, aperture stopped well down. The street runs away to the right; plane trees line the near
pavement; a nineteen-sixties apartment block with a row of lit windows and enclosed balconies fills the
left two thirds; a small kiosk sits at the right third with a zebra crossing in front of it.
What is perfectly sharp, because the camera never moved: the trees down to the edge of every leaf, the
render and the balcony rails, the window frames, the kiosk, the painted stripes of the crossing, the kerb,
and the litter in the gutter. Sharpness here is the evidence that the camera was fixed.
What is a smear, because it moved while the shutter was open: the pedestrians. A man who kept walking
across the crossing has become a faint translucent band with no face, no hands and no edges, and the
railing behind him is clearly visible through his body. A woman who stopped halfway for part of the
exposure leaves a denser, more solid ghost exactly where she paused, fading at both ends into nothing.
The marshutka: a minibus crossed the frame from left to right and its body has vanished entirely. What it
left is light. Its headlights drew two continuous warm-white lines running left to right across the lower
third at bumper height; its tail lights drew two red lines just above and behind them; a row of small amber
roof points drew a thin dotted line higher still. Every trail runs in one direction only, left to right,
unbroken, with no doubling, no dashes and no reversal anywhere. Where the marshutka braked before the
crossing, the red lines thicken and bend slightly upward.
Point sources: the streetlamps and the lit windows render as bright points with a clean multi-pointed star,
because the diaphragm is closed down. The wet asphalt returns all of it as wider, softer, vertically
stretched reflections directly beneath each source.
Exposure decision: expose for the lit facade and let the sky go black. Do not brighten the sky, do not
recover the shadows between the trees, and do not add haze or glow that the lights do not make themselves.
No legible signage, no logo, no brand name, and no recognisable individual anywhere in frame.
```

---

### NB-40 · Golden-hour backlit portrait
`nano-banana` `gemini` — backlight, golden hour

**EN**
```
Photograph a young woman on the Batumi seafront about twenty minutes before sunset, lit from
behind. Backlight is easy to get wrong in two directions — a black face or a washed-out haze — so
the fill and the flare are specified below and both must be followed.

Subject: a woman in her mid-twenties, dark hair loose and moving in the onshore wind, a thin
rust-coloured knit, no jewellery. She is turned slightly away from the lens, looking off to camera
left at something on the water, not smiling for the camera; one hand is lifting a strand of hair
off her face.

Composition: 4:5 vertical, chest up, the figure slightly right of centre. The sea horizon crosses
behind her at shoulder height; the pebble shoreline runs out of the bottom left corner; a line of
tamarisk sits far out of focus at the left edge. Camera at her eye level, straight on, 85mm
equivalent, f/2, focused on the near eye so the sea behind dissolves completely.

Main light: the sun is low and behind her, about fifteen degrees off the lens axis to camera right
rather than dead centre. It lays a hot orange rim along the top of her hair, down the edge of her
right shoulder and along the line of her jaw, separating her cleanly from the water, and it turns
the sea into a broad field of soft golden specular glitter thrown right out of focus.

Flare, controlled: let the edge of her hair occlude most of the sun's disc. One warm veil of flare
spills in from the upper right, lifting the contrast in that quadrant by about a stop, plus one
small soft polygonal ghost below and left of the sun. No rainbow streaks, no anamorphic line, no
overlay effect, and no flare crossing her eyes.

Fill, explicit: backlight alone would leave her face about four stops under. Place a large white
reflector just outside the frame at camera left, one metre from her and slightly below her chin,
angled up, returning sunlight to her face at roughly one and a half stops below the rim. The face
is then clearly lit and open, with soft shadows under the brow and the nose and a long low
catchlight in each eye. The face must not be a silhouette and must not go black. The reflector is
white, not silver: no hard specular hotspot on the cheek.

Colour: set the white balance for the warm light so her skin reads natural rather than orange,
while the sky and the sea keep their gold. Contrast is moderate, the shadows stay open and slightly
cool by comparison, and there is no crushed black anywhere in the frame.
```

**KA**
```
გადაიღე ახალგაზრდა ქალის კონტრაჟური პორტრეტი ბათუმის სანაპიროზე, მზის ჩასვლამდე დაახლოებით ოცი
წუთით ადრე. კონტრაჟურში ორი მიმართულებით შეიძლება წახდეს კადრი — შავი სახე ან გადარეცხილი ნისლი —
ამიტომ შემავსებელი შუქი და ბლიკი ქვემოთ ზუსტადაა გაწერილი და ორივე შესასრულებელია.

ობიექტი: ოცდახუთი წლის ქალი, მუქი თმა თავისუფლად და ზღვის ნიავში აწეული, თხელი ჟანგისფერი ნაქსოვი,
სამკაულის გარეშე. ობიექტივიდან ოდნავ მიბრუნებულია, კამერიდან მარცხნივ, წყალზე რაღაცას გასცქერის და
კამერისთვის არ იღიმება; ერთი ხელით თმის ღერს სახიდან იშორებს.

კომპოზიცია: ვერტიკალური კადრი 4:5, მკერდზევით, ფიგურა ცენტრიდან ოდნავ მარჯვნივ. ზღვის ჰორიზონტი მის
უკან მხრების სიმაღლეზე გადის; კენჭებიანი სანაპირო ქვედა მარცხენა კუთხიდან გადის კადრს; მარცხენა
კიდესთან, ღრმად დაბუნდოვნებული, იალღუნების რიგია. კამერა მისი თვალის დონეზე, პირდაპირ, 85 მმ
ექვივალენტი, დიაფრაგმა f/2, ფოკუსი ახლო თვალზე — უკანა ზღვა სრულიად იშლება.

მთავარი შუქი: მზე დაბალია და მის უკან დგას, ობიექტივის ღერძიდან დაახლოებით თხუთმეტი გრადუსით
კამერისკენ მარჯვნივ და არა ზუსტად ცენტრში. ის თმის თხემზე, მარჯვენა მხრის კიდესა და ყბის ხაზზე ცხელ
ნარინჯისფერ კონტურს დებს და ფიგურას წყალს სუფთად აცილებს; ზღვას კი განიერ, რბილ ოქროსფერ ბზინვის
ველად აქცევს, სრულიად ფოკუსგარეშე.

ბლიკი, კონტროლირებული: მზის დისკის უმეტესი ნაწილი თმის კიდემ დაფაროს. ზედა მარჯვენა კუთხიდან ერთი
თბილი ბლიკის ფარდა შემოდის და იმ მეოთხედში კონტრასტს დაახლოებით ერთი საფეხურით წევს; გარდა ამისა,
მზის ქვემოთ და მარცხნივ ერთი პატარა, რბილი მრავალკუთხა აჩრდილია. არც ცისარტყელისებრი ზოლი, არც
ანამორფული ხაზი, არც ზედდებული ეფექტი და არც ბლიკი, რომელიც თვალებს კვეთს.

შემავსებელი შუქი, პირდაპირ: მხოლოდ კონტრაჟურით სახე ოთხი საფეხურით ჩაბნელდებოდა. კადრს გარეთ,
კამერიდან მარცხნივ, მისგან ერთ მეტრში და ნიკაპზე ოდნავ დაბლა დადგი დიდი თეთრი ამრეკლი, ზემოთ დახრილი,
რომელიც მზის შუქს სახეზე აბრუნებს კონტურზე დაახლოებით საფეხურნახევრით დაბლა. შედეგად სახე ნათლად და
ღიად არის განათებული, წარბისა და ცხვირის ქვეშ რბილი ჩრდილებით და თითოეულ თვალში გრძელი, დაბალი
ბზინვით. სახე არც სილუეტი უნდა იყოს და არც შავში ჩავარდეს. ამრეკლი თეთრია და არა ვერცხლისფერი:
ლოყაზე მკვეთრი ბზინვის ლაქა არ გაჩნდეს.

ფერი: თეთრის ბალანსი თბილ შუქზე დააყენე, რომ კანი ნარინჯისფრად კი არა, ბუნებრივად წაიკითხოს, ცამ და
ზღვამ კი ოქროსფერი შეინარჩუნოს. კონტრასტი ზომიერია, ჩრდილები ღია და შედარებით გრილი რჩება, კადრში
კი ჩაჭრილი შავი არსად არის.
---
Photograph a young woman on the Batumi seafront about twenty minutes before sunset, lit from behind.
Backlight is easy to get wrong in two directions — a black face or a washed-out haze — so the fill and the
flare are specified below and both must be followed.
Subject: a woman in her mid-twenties, dark hair loose and moving in the onshore wind, a thin rust-coloured
knit, no jewellery. She is turned slightly away from the lens, looking off to camera left at something on
the water, not smiling for the camera; one hand is lifting a strand of hair off her face.
Composition: 4:5 vertical, chest up, the figure slightly right of centre. The sea horizon crosses behind
her at shoulder height; the pebble shoreline runs out of the bottom left corner; a line of tamarisk sits
far out of focus at the left edge. Camera at her eye level, straight on, 85mm equivalent, f/2, focused on
the near eye so the sea behind dissolves completely.
Main light: the sun is low and behind her, about fifteen degrees off the lens axis to camera right rather
than dead centre. It lays a hot orange rim along the top of her hair, down the edge of her right shoulder
and along the line of her jaw, separating her cleanly from the water, and it turns the sea into a broad
field of soft golden specular glitter thrown right out of focus.
Flare, controlled: let the edge of her hair occlude most of the sun's disc. One warm veil of flare spills in
from the upper right, lifting the contrast in that quadrant by about a stop, plus one small soft polygonal
ghost below and left of the sun. No rainbow streaks, no anamorphic line, no overlay effect, and no flare
crossing her eyes.
Fill, explicit: backlight alone would leave her face about four stops under. Place a large white reflector
just outside the frame at camera left, one metre from her and slightly below her chin, angled up, returning
sunlight to her face at roughly one and a half stops below the rim. The face is then clearly lit and open,
with soft shadows under the brow and the nose and a long low catchlight in each eye. The face must not be a
silhouette and must not go black. The reflector is white, not silver: no hard specular hotspot on the cheek.
Colour: set the white balance for the warm light so her skin reads natural rather than orange, while the sky
and the sea keep their gold. Contrast is moderate, the shadows stay open and slightly cool by comparison,
and there is no crushed black anywhere in the frame.
```

---

### NB-41 · Isometric cutaway of a Tbilisi courtyard flat
`nano-banana` `gemini` — isometric, cutaway, interior

**EN**
```
Draw an isometric cutaway of a one-bedroom flat on the first floor of an old Tbilisi courtyard
house — the kind reached by a wooden gallery that runs right around an inner yard. 1:1 square,
rendered at 2K. This is a constructed drawing, not a photograph.

The projection is the binding rule and everything else is subordinate to it. Use true isometric,
not a perspective view: the two horizontal axes run thirty degrees above the page horizontal, one
to the left and one to the right, all three axes are foreshortened equally, and every vertical edge
in the building stays vertical on the page. Lines that are parallel in the flat stay parallel in
the drawing and never converge. There is no vanishing point, no horizon line and no lens distortion
anywhere in the image. A floor tile in the far corner of the room must be drawn at exactly the same
size as a floor tile in the near corner — if the far end of the room looks smaller, the projection
is wrong and the drawing has failed.

The cutaway: the two walls nearest the viewer are removed completely and the flat stands open like
a doll's house. The two far walls are at full height with their cornices intact. Draw the cut edge
of each removed wall as a visible band of plaster over brick running along the floor line and up
the corner, so the viewer can read how thick the walls are.

Contents, all on one floor plate, arranged left to right: a main room with a high ceiling, a
moulded plaster cornice, dark patterned parquet, a low sofa under the window wall, a round table
with three chairs and a tall tiled stove in the corner; a pair of tall glazed doors on the far wall
opening onto a narrow wooden balcony with a carved railing and a line of washing; a small kitchen
on the right with an enamel sink, a two-burner stove and open shelves; and a short hallway with a
coat hook and a worn runner. Simplify every object into clean planes — no clutter and nothing
smaller than a teapot.

Light: a single implied source high on the left. Every cast shadow in the drawing falls down and to
the right at the same angle, and each shadow's length is proportional to its object's height by the
same ratio across the whole scene. Surfaces facing up are the lightest, surfaces facing left are
one step darker, surfaces facing right are two steps darker — apply that to every plane in the
image without exception.

Style: clean architectural illustration, matte flat fills with one soft shading step, a warm
palette of terracotta, ochre, sage and off-white, thin uniform outlines, no photographic texture,
no people and no text anywhere in the image.
```

**KA**
```
დახატე ძველი თბილისური ეზოიანი სახლის პირველი სართულის ბინის იზომეტრიული ჭრილი — იმ ტიპის სახლისა,
სადაც ბინამდე ხის აივანი მიდის და აივანი შიდა ეზოს გარს უვლის. კვადრატული კადრი 1:1, რენდერი 2K.
ეს აგებული ნახაზია და არა ფოტო.

მთავარი წესი პროექციაა და დანარჩენი ყველაფერი მას ემორჩილება. გამოიყენე ნამდვილი იზომეტრია და არა
პერსპექტივა: 2 ჰორიზონტალური ღერძი ფურცლის ჰორიზონტალიდან 30 გრადუსით მაღლა მიდის — ერთი მარცხნივ,
მეორე მარჯვნივ; სამივე ღერძი თანაბრადაა შემოკლებული; შენობის ყოველი ვერტიკალური წიბო ფურცელზე
ვერტიკალური რჩება. ხაზები, რომლებიც ბინაში პარალელურია, ნახაზზეც პარალელური რჩება და არსად
უახლოვდება ერთმანეთს. სურათში არ არის არც გაქრობის წერტილი, არც ჰორიზონტის ხაზი და არც ობიექტივის
დამახინჯება. ოთახის შორეულ კუთხეში მდებარე იატაკის ფილა ზუსტად იმავე ზომით უნდა დაიხატოს, რითაც
ახლო კუთხის ფილა — თუ ოთახის შორეული ბოლო უფრო პატარა გამოჩნდა, პროექცია მცდარია და ნახაზი
გამოსაგდებია.

ჭრილი: მაყურებელთან ყველაზე ახლოს მდგარი 2 კედელი სრულად ამოღებულია და ბინა თოჯინების სახლივით ღია
რჩება. შორეული 2 კედელი სრულ სიმაღლეზე დგას, კარნიზებიანად. ამოღებული კედლის ჭრილის კიდე დახატე
ხილული ზოლით — ბათქაში აგურზე — იატაკის ხაზის გასწვრივ და კუთხეში ზემოთ, რომ მაყურებელმა კედლის
სისქე წაიკითხოს.

რა დგას შიგნით, ერთ იატაკის სიბრტყეზე, მარცხნიდან მარჯვნივ: მთავარი ოთახი მაღალი ჭერით, თაბაშირის
კარნიზით, მუქი, ნახატიანი პარკეტით, ფანჯრის კედელთან დაბალი დივანი, მრგვალი მაგიდა 3 სკამით და
კუთხეში მაღალი, კაფელიანი ღუმელი; შორეულ კედელზე მაღალი მინიანი კარი, რომელიც ვიწრო ხის აივანზე
გადის მოჩუქურთმებული მოაჯირითა და გაფენილი სარეცხის ხაზით; მარჯვნივ პატარა სამზარეულო ემალის
ნიჟარით, ორსანთურიანი ქურითა და ღია თაროებით; და მოკლე დერეფანი ტანსაცმლის კაუჭითა და გაცვეთილი
ხალიჩით. ყოველი საგანი სუფთა სიბრტყედ გაამარტივე — ზედმეტი წვრილმანის გარეშე, ჩაიდანზე პატარა
არაფერი.

განათება: ერთი ნაგულისხმევი წყარო მაღლა, მარცხნივ. ნახაზში ყოველი დაცემული ჩრდილი ქვემოთ და
მარჯვნივ ეცემა, ერთი და იმავე კუთხით; ჩრდილის სიგრძე საგნის სიმაღლის იმავე პროპორციით იზრდება
მთელ სცენაში. ზემოთ მიმართული ზედაპირი ყველაზე ნათელია, მარცხნივ მიმართული — ერთი საფეხურით მუქი,
მარჯვნივ მიმართული — ორი საფეხურით მუქი; ეს წესი გამონაკლისის გარეშე ყველა სიბრტყეს მოარგე.

სტილი: სუფთა არქიტექტურული ილუსტრაცია, მქრქალი ბრტყელი შევსება ერთი რბილი საფეხურის ჩრდილით, თბილი
პალიტრა — ტერაკოტა, ოხრა, მწვანე-ნაცრისფერი და მოთეთრო; თხელი, ერთგვაროვანი კონტური; ფოტოგრაფიული
ფაქტურის გარეშე; ადამიანისა და ნებისმიერი წარწერის გარეშე.
---
Draw an isometric cutaway of a one-bedroom flat on the first floor of an old Tbilisi courtyard house —
the kind reached by a wooden gallery that runs right around an inner yard. 1:1 square, rendered at 2K.
This is a constructed drawing, not a photograph.
The projection is the binding rule and everything else is subordinate to it. Use true isometric, not a
perspective view: the two horizontal axes run thirty degrees above the page horizontal, one to the left
and one to the right, all three axes are foreshortened equally, and every vertical edge in the building
stays vertical on the page. Lines that are parallel in the flat stay parallel in the drawing and never
converge. There is no vanishing point, no horizon line and no lens distortion anywhere in the image. A
floor tile in the far corner of the room must be drawn at exactly the same size as a floor tile in the
near corner — if the far end of the room looks smaller, the projection is wrong and the drawing has
failed.
The cutaway: the two walls nearest the viewer are removed completely and the flat stands open like a
doll's house. The two far walls are at full height with their cornices intact. Draw the cut edge of each
removed wall as a visible band of plaster over brick running along the floor line and up the corner, so
the viewer can read how thick the walls are.
Contents, all on one floor plate, arranged left to right: a main room with a high ceiling, a moulded
plaster cornice, dark patterned parquet, a low sofa under the window wall, a round table with three
chairs and a tall tiled stove in the corner; a pair of tall glazed doors on the far wall opening onto a
narrow wooden balcony with a carved railing and a line of washing; a small kitchen on the right with an
enamel sink, a two-burner stove and open shelves; and a short hallway with a coat hook and a worn runner.
Simplify every object into clean planes — no clutter and nothing smaller than a teapot.
Light: a single implied source high on the left. Every cast shadow in the drawing falls down and to the
right at the same angle, and each shadow's length is proportional to its object's height by the same
ratio across the whole scene. Surfaces facing up are the lightest, surfaces facing left are one step
darker, surfaces facing right are two steps darker — apply that to every plane in the image without
exception.
Style: clean architectural illustration, matte flat fills with one soft shading step, a warm palette of
terracotta, ochre, sage and off-white, thin uniform outlines, no photographic texture, no people and no
text anywhere in the image.
```

---

### NB-42 · Gergeti as a tabletop diorama — tilt-shift miniature
`nano-banana` `gemini` — tilt-shift, miniature, diorama

**EN**
```
Photograph Gergeti Trinity church and the ridge it stands on as if the whole place were a tabletop
diorama built by a hobbyist and shot on a large-format camera with the lens tilted. 3:2 horizontal,
rendered at 2K. The place is real; the illusion to build is that it is half a metre wide.

Camera: high and far back, looking down on the scene at about forty degrees — the angle at which
you look at a model on a table, not the angle at which you photograph a mountain from another
mountain. Long lens, so the ridge compresses and the sense of distance flattens out.

The focus falloff is what sells the trick and it must be pushed far past anything a real lens would
do at this distance. One narrow horizontal band across the middle of the frame is critically sharp:
the church, its enclosing wall and a few metres of grass around it. Above and below that band the
blur grows fast and smoothly — the foreground slope at the bottom edge and the snowfield and sky at
the top edge are both blurred until individual features stop being readable — and nothing outside
the band is sharp anywhere.

The scale cues, all of them deliberate. The grass reads as model-railway flock rather than real
vegetation: slightly too even in colour and too uniform in height. The snow on the peak behind
reads as poured plaster with soft rounded edges instead of wind-carved crust. The gravel track up
the ridge is a smooth painted ribbon with no loose stones on it. The stone of the church is crisply
moulded, its edges a touch too regular, its joints a touch too even. The few visitors by the wall
are four millimetres tall, blurred, stiffly posed and without facial detail, like painted figures —
nobody in the frame is recognisable.

Colour: push saturation one clear step past natural. The greens of the grass and the blue of the
sky are richer than daylight would give them, contrast is raised, and the shadows stay open and
slightly blue rather than falling to black.

Light: one hard high source from the upper left, as if from a single lamp over a workbench, giving
short crisp shadows off the church and the wall, every one of them falling in the same direction.
```

**KA**
```
გადაიღე გერგეტის სამება და ქედი, რომელზეც დგას, ისე, თითქოს მთელი ადგილი მაგიდაზე აწყობილი დიორამაა —
ხელით აშენებული მაკეტი — და დიდფორმატიანი კამერით, დახრილი ობიექტივით იღებ. ჰორიზონტალური კადრი 3:2,
რენდერი 2K. ადგილი ნამდვილია — ასაგები ილუზია ის არის, რომ ის ნახევარი მეტრის სიგანისაა.

კამერა: მაღლა და შორს, სცენას დაახლოებით 40 გრადუსით ზემოდან უყურებს — ისე, როგორც მაგიდაზე მდგარ
მაკეტს შეხედავდი და არა ისე, როგორც მთას მეორე მთიდან იღებ. გრძელი ობიექტივი, ამიტომ ქედი იკუმშება
და სიშორის შეგრძნება ბრტყელდება.

ხრიკს ფოკუსის სწრაფი დაკარგვა ყიდის და ის გადაჭარბებული უნდა იყოს — ბევრად ძლიერი, ვიდრე ამ
მანძილზე ნამდვილი ობიექტივი მოგცემდა. კადრის შუაში ერთი ვიწრო ჰორიზონტალური ზოლი უმკვეთრესია:
ტაძარი, მისი გალავანი და გარშემო რამდენიმე მეტრი ბალახი. ამ ზოლის ზემოთ და ქვემოთ ბუნდოვნება
სწრაფად და თანაბრად იზრდება — ქვედა კიდეზე წინა პლანის ფერდობი, ზედა კიდეზე თოვლიანი მწვერვალი და
ცა იმდენად იბინდება, რომ ცალკეული დეტალი აღარ იკითხება; ზოლის გარეთ არსად არაფერი რჩება მკვეთრი.

მასშტაბის მინიშნებები — ყველა შეგნებული. ბალახი ნამდვილ მცენარეულობას კი არა, სამოდელო რკინიგზის
საფენს ჰგავს: ფერით ოდნავ ზედმეტად ერთგვაროვანი და სიმაღლით ზედმეტად თანაბარი. უკან მწვერვალზე
თოვლი ქარისგან გამოკვეთილ ქერქს კი არა, ჩამოსხმულ თაბაშირს ჰგავს — რბილი, მომრგვალებული კიდეებით.
ქედზე ასასვლელი ხრეშის გზა გლუვი, შეღებილი ლენტია, ცალკეული ქვის გარეშე. ტაძრის ქვა მკაფიოდაა
გამოძერწილი, მისი წიბო ოდნავ ზედმეტად სწორია, ნაკერი ოდნავ ზედმეტად თანაბარი. გალავანთან მდგარი
რამდენიმე ვიზიტორი 4 მილიმეტრის სიმაღლისაა, დაბინდული, უხერხულად გაშეშებული და სახის ნაკვთების
გარეშე — შეღებილი ფიგურებივით; კადრში არავინ არ არის ამოსაცნობი.

ფერი: სიხასხასე ბუნებრივზე ერთი მკაფიო საფეხურით მაღლა აწიე. ბალახის მწვანე და ცის ლურჯი უფრო
მაძღარია, ვიდრე დღის შუქი მოგცემდა; კონტრასტი აწეულია; ჩრდილები ღია და ოდნავ მოლურჯო რჩება და
შავში არ გადადის.

განათება: ერთი მკვეთრი, მაღალი წყარო ზედა მარცხენა მხრიდან — თითქოს სამუშაო მაგიდაზე ერთი ნათურა
ჰკიდია; ტაძრიდან და გალავნიდან მოკლე, მკაფიო ჩრდილები ეცემა, ყველა ერთი მიმართულებით.
---
Photograph Gergeti Trinity church and the ridge it stands on as if the whole place were a tabletop
diorama built by a hobbyist and shot on a large-format camera with the lens tilted. 3:2 horizontal, rendered at
2K. The place is real; the illusion to build is that it is half a metre wide.
Camera: high and far back, looking down on the scene at about forty degrees — the angle at which you look
at a model on a table, not the angle at which you photograph a mountain from another mountain. Long lens,
so the ridge compresses and the sense of distance flattens out.
The focus falloff is what sells the trick and it must be pushed far past anything a real lens would do at
this distance. One narrow horizontal band across the middle of the frame is critically sharp: the church,
its enclosing wall and a few metres of grass around it. Above and below that band the blur grows fast and
smoothly — the foreground slope at the bottom edge and the snowfield and sky at the top edge are both
blurred until individual features stop being readable — and nothing outside the band is sharp anywhere.
The scale cues, all of them deliberate. The grass reads as model-railway flock rather than real
vegetation: slightly too even in colour and too uniform in height. The snow on the peak behind reads as
poured plaster with soft rounded edges instead of wind-carved crust. The gravel track up the ridge is a
smooth painted ribbon with no loose stones on it. The stone of the church is crisply moulded, its edges a
touch too regular, its joints a touch too even. The few visitors by the wall are four millimetres tall,
blurred, stiffly posed and without facial detail, like painted figures — nobody in the frame is
recognisable.
Colour: push saturation one clear step past natural. The greens of the grass and the blue of the sky are
richer than daylight would give them, contrast is raised, and the shadows stay open and slightly blue
rather than falling to black.
Light: one hard high source from the upper left, as if from a single lamp over a workbench, giving short
crisp shadows off the church and the wall, every one of them falling in the same direction.
```

---

### NB-43 · Floating island — a headland lifted out of the ground
`nano-banana` `gemini` — surreal, geology, landscape

**EN**
```
Render a small coastal headland lifted out of the earth and left hanging in open sky, the
lighthouse still standing on top of it and the ground it was cut from hanging underneath. 4:5
vertical, rendered at 2K.

The island: an irregular chunk of land about forty metres across at the top, tapering downward to a
ragged point some sixty metres below the surface. The top surface is intact and undisturbed —
cropped sea grass, a gravel path, a whitewashed stone lighthouse with a black lantern housing, a
low drystone wall and two wind-bent pines leaning away from the same side. Nothing up there
suggests that anything unusual has happened, and that is deliberate: the illusion works because the
surface looks entirely ordinary.

The underside is the subject of the picture and it must read as a geological section, not as a
generic lump of rock. From the top down: fifteen centimetres of dark root-bound topsoil with grass
roots trailing out of the cut; a pale band of sandy subsoil; then layered sedimentary rock in
alternating grey and rust bands that stay roughly horizontal all the way round the mass, tilting
only gently, so the eye can follow one band across the whole island; below that a zone of coarse
broken stone; and from the lowest point a few long roots and one thin thread of water falling and
dispersing into vapour before it reaches the bottom of the frame.

Composition: the island sits slightly above centre and takes about half the frame width, with the
lighthouse breaking into the upper third. The camera is below the level of the island's top surface
and looks slightly up, so the section is well seen. Behind it, open sky fills the entire frame — a
bank of tall cumulus to the right catching light along its upper edge, thin haze low down — and
there is no land, no sea and no horizon line anywhere. The island is the only solid thing in the
picture.

Light: a low sun from the upper right. The lighthouse and the pines throw long shadows to the left
across the grass; the right flank of the rock section is warmly lit; the left flank falls into cool
shadow; and the underside is not black but filled with soft blue bounced skylight.

Style: realistic rendering held back from spectacle — believable rock and vegetation, natural
colour, no glow, no debris orbiting the island, no figures.
```

**KA**
```
დაარენდერე ზღვისპირა პატარა კონცხი, რომელიც მიწიდან ამოგლეჯილია და ღია ცაში ჰკიდია: შუქურა ისევ
მის თავზე დგას, ქვემოდან კი ის მიწა ჰკიდია, საიდანაც კონცხი მოწყდა. ვერტიკალური კადრი 4:5,
რენდერი 2K.

კუნძული: მიწის არასწორი ფორმის ნატეხი, ზემოდან დაახლოებით 40 მეტრი განივად, ქვემოთ კი თანდათან
ვიწროვდება და ზედაპირიდან 60 მეტრზე დაღარულ წვერში გადადის. ზედა ზედაპირი უვნებელია — დაბალი
ზღვისპირა ბალახი, ხრეშის ბილიკი, მოთეთრებული ქვის შუქურა შავი ფარნის თავით, დაბალი, უდუღაბო ქვის
გალავანი და 2 ფიჭვი, ქარისგან ერთი მიმართულებით მოხრილი. ზემოთ არაფერი მიანიშნებს, რომ რაღაც
არაჩვეულებრივი მოხდა — ეს შეგნებულია: ილუზია სწორედ იმიტომ მუშაობს, რომ ზედაპირი სრულიად ჩვეულებრივ
გამოიყურება.

ქვედა მხარე სურათის მთავარი თემაა და გეოლოგიურ ჭრილად უნდა იკითხებოდეს და არა ქვის უფორმო
ნატეხად. ზემოდან ქვემოთ: 15 სანტიმეტრი მუქი, ფესვებით გაბმული ზედა ნიადაგი, საიდანაც ბალახის
ფესვები ჭრილიდან გამოკიდებულია; ღია, ქვიშიანი გრუნტის ზოლი; შემდეგ ფენოვანი დანალექი ქანი
ნაცრისფერი და მოწითალო ზოლების მონაცვლეობით, რომლებიც მთელ მასაზე დაახლოებით ჰორიზონტალური რჩება
და მხოლოდ ოდნავაა დახრილი — მზერას ერთი ზოლი მთელ კუნძულზე გასდევს; ქვემოთ მსხვილი, დამსხვრეული
ქვის ზონა; ყველაზე დაბალი წერტილიდან კი რამდენიმე გრძელი ფესვი და წყლის ერთი თხელი ძაფი ჩამოდის და
კადრის ქვედა კიდემდე ორთქლად იფანტება.

კომპოზიცია: კუნძული ცენტრზე ოდნავ მაღლა ზის და კადრის სიგანის დაახლოებით ნახევარს იკავებს, შუქურა
კი ზედა მესამედში ჭრის. კამერა კუნძულის ზედაპირზე დაბლაა და ოდნავ მაღლა იყურება, რომ ჭრილი კარგად
ჩანდეს. უკან მთელ კადრს ღია ცა ავსებს — მარჯვნივ მაღალი გროვა-ღრუბლების ზოლი, ზედა კიდეზე შუქით
შემოვლებული, ქვემოთ კი თხელი ნისლი; არსად არ ჩანს არც ხმელეთი, არც ზღვა და არც ჰორიზონტის ხაზი.
კუნძული სურათში ერთადერთი მყარი საგანია.

განათება: დაბალი მზე ზედა მარჯვენა მხრიდან. შუქურა და ფიჭვები ბალახზე გრძელ ჩრდილს მარცხნივ
აგდებს; ქანის ჭრილის მარჯვენა მხარე თბილადაა განათებული; მარცხენა მხარე ცივ ჩრდილში ჩადის; ქვედა
მხარე კი შავი არ არის — მას ცის რბილი, მოლურჯო არეკვლა ავსებს.

სტილი: რეალისტური რენდერი ეფექტებზე უარის თქმით — დამაჯერებელი ქანი და მცენარეულობა, ბუნებრივი
ფერი, ნათების ეფექტის გარეშე, კუნძულის გარშემო მოფრინავი ნატეხების გარეშე, ფიგურების გარეშე.
---
Render a small coastal headland lifted out of the earth and left hanging in open sky, the lighthouse
still standing on top of it and the ground it was cut from hanging underneath. 4:5 vertical, rendered at
2K.
The island: an irregular chunk of land about forty metres across at the top, tapering downward to a
ragged point some sixty metres below the surface. The top surface is intact and undisturbed — cropped sea
grass, a gravel path, a whitewashed stone lighthouse with a black lantern housing, a low drystone wall
and two wind-bent pines leaning away from the same side. Nothing up there suggests that anything unusual
has happened, and that is deliberate: the illusion works because the surface looks entirely ordinary.
The underside is the subject of the picture and it must read as a geological section, not as a generic
lump of rock. From the top down: fifteen centimetres of dark root-bound topsoil with grass roots trailing
out of the cut; a pale band of sandy subsoil; then layered sedimentary rock in alternating grey and rust
bands that stay roughly horizontal all the way round the mass, tilting only gently, so the eye can follow
one band across the whole island; below that a zone of coarse broken stone; and from the lowest point a
few long roots and one thin thread of water falling and dispersing into vapour before it reaches the
bottom of the frame.
Composition: the island sits slightly above centre and takes about half the frame width, with the
lighthouse breaking into the upper third. The camera is below the level of the island's top surface and
looks slightly up, so the section is well seen. Behind it, open sky fills the entire frame — a bank of
tall cumulus to the right catching light along its upper edge, thin haze low down — and there is no land,
no sea and no horizon line anywhere. The island is the only solid thing in the picture.
Light: a low sun from the upper right. The lighthouse and the pines throw long shadows to the left across
the grass; the right flank of the rock section is warmly lit; the left flank falls into cool shadow; and
the underside is not black but filled with soft blue bounced skylight.
Style: realistic rendering held back from spectacle — believable rock and vegetation, natural colour, no
glow, no debris orbiting the island, no figures.
```

---

### NB-44 · Tbilisi landmarks as a 3D cartoon map
`nano-banana` `gemini` — map, 3d illustration, georgian text

**EN**
```
Build a three-dimensional cartoon map of Tbilisi's landmarks — the kind printed on a tourist
placemat. 16:9 horizontal, rendered at 2K. This is a stylised illustration, not a real map and not
an aerial photograph.

The ground plane is deliberately simplified and carries almost nothing: a broad pale sand-coloured
plate; the Mtkvari drawn as a smooth blue-grey ribbon curving through it from the upper right to
the lower left; one green mass for the wooded ridge on the west side; three or four tan ribbons for
the main roads; and a scatter of simple round trees. No small buildings, no street grid, no contour
lines. Everything that is not a landmark stays flat, quiet and low.

On that plate, stand the landmarks as chunky three-dimensional models seen from a high
three-quarter angle, each one rendered far larger than its true size relative to the ground — a
single building is the size of a city block, and that exaggeration is the whole idea. Simplify each
model down to its most recognisable silhouette, with rounded edges and no fine detail. Place, from
the upper left to the lower right: the fortress on the ridge with its stone towers and curtain
wall; the funicular line climbing the wooded slope to the tall thin television mast at the top; the
cluster of low brick domes of the sulphur baths by the river; the tall cathedral with its stepped
gold dome on the east bank; a glass and steel footbridge arching over the water; the columned opera
house beside the main avenue; and the botanical gorge with a small waterfall at the lower left.
Keep every model upright and turned toward the viewer, even where that is geographically
imprecise — legibility beats accuracy here.

Each landmark stands on a small oval base raised slightly off the ground plate, with a soft contact
shadow under it.

Labels: place one blank label plate beside each of the seven landmarks and one larger blank plate
across the top centre of the frame. Each plate is a flat rounded rectangle in off-white with a thin
grey border and a small pointer aimed at the landmark it belongs to. Leave every plate completely
empty — no lettering, no placeholder text, no squiggles standing in for words.

Light: one high source from the upper left. Every model's shadow falls down and to the right at the
same angle and lies flat on the ground plate.

Style: friendly toy-like 3D illustration, matte surfaces, a warm palette of terracotta, cream, sage
and dusty blue, no photorealism, no people, no vehicles, no logos of any kind.

# The Georgian names are meant to be set over the blank plates afterwards in a design tool — that is
# why this prompt asks for the plates to stay empty. If you do ask the model to letter them, expect
# the Georgian letterforms to come back needing repair and check the result letter by letter.
```

**KA**
```
ააგე თბილისის ღირსშესანიშნაობების სამგანზომილებიანი, მულტიპლიკაციური რუკა — ისეთი, ტურისტულ
სასუფრე ფურცელზე რომ ბეჭდავენ. ჰორიზონტალური კადრი 16:9, რენდერი 2K. ეს სტილიზებული ილუსტრაციაა
და არა ნამდვილი რუკა ან საჰაერო ფოტო.

მიწის სიბრტყე შეგნებულად გამარტივებულია და თითქმის არაფერი აქვს: ფართო, ღია ქვიშისფერი ფირფიტა;
მტკვარი გლუვი, მოლურჯო-ნაცრისფერი ლენტით, ზედა მარჯვენა კუთხიდან ქვედა მარცხენისკენ მოხრილი;
დასავლეთით ტყიანი ქედის ერთი მწვანე მასა; 4 მოყავისფრო ლენტი მთავარი გზებისთვის; და მიმოფანტული,
მარტივი, მრგვალი ხეები. პატარა შენობების, ქუჩების ბადისა და ჰორიზონტალების გარეშე. ყველაფერი,
რაც ღირსშესანიშნაობა არ არის, ბრტყელი, მშვიდი და დაბალი რჩება.

ამ ფირფიტაზე ღირსშესანიშნაობები მასიური, სამგანზომილებიანი მაკეტებივით დააყენე, მაღლიდან სამი
მეოთხედის კუთხით დანახული; თითოეული მიწასთან შედარებით ნამდვილზე ბევრად დიდია — ერთი შენობა მთელი
კვარტლის ზომისაა და სწორედ ეს გაზვიადებაა მთავარი იდეა. ყოველი მაკეტი მის ყველაზე ამოსაცნობ
სილუეტამდე გაამარტივე, მომრგვალებული წიბოებით და წვრილი დეტალების გარეშე. დაალაგე ზედა მარცხენა
კუთხიდან ქვედა მარჯვენისკენ: ქედზე მდგარი ციხე თავისი ქვის კოშკებითა და გალავნით; ფუნიკულიორის
ხაზი, რომელიც ტყიან ფერდობზე მაღლა, სატელევიზიო ანძამდე ადის; მდინარესთან გოგირდის აბანოების
დაბალი აგურის გუმბათების გროვა; აღმოსავლეთ ნაპირზე მაღალი ტაძარი საფეხურებიანი ოქროსფერი
გუმბათით; მინისა და ფოლადის საფეხმავლო ხიდი, წყალზე თაღად გადებული; მთავარ გამზირზე სვეტებიანი
ოპერის შენობა; და ქვედა მარცხენა კუთხეში ბოტანიკური ხეობა პატარა ჩანჩქერით. ყოველი მაკეტი სწორად
დგას და მაყურებლისკენაა შემობრუნებული, მაშინაც კი, როცა ეს გეოგრაფიულად ზუსტი არ არის — აქ
წაკითხვადობა სიზუსტეზე მნიშვნელოვანია.

ყოველი ღირსშესანიშნაობა პატარა ოვალურ კვარცხლბეკზე დგას, მიწის ფირფიტიდან ოდნავ აწეული, ქვეშ
რბილი, შემხები ჩრდილით.

წარწერების ადგილი: შვიდივე ღირსშესანიშნაობის გვერდით დადე თითო ცარიელი ფირფიტა და კადრის ზედა
ცენტრში — ერთი უფრო დიდი. ყოველი ფირფიტა ბრტყელი, მომრგვალებულკუთხოვანი, მოთეთრო
მართკუთხედია თხელი ნაცრისფერი კონტურითა და პატარა მიმთითებლით, რომელიც თავის ღირსშესანიშნაობაზე
იშვერს. ყველა ფირფიტა სრულიად ცარიელი დატოვე — ასოების, დროებითი ტექსტისა და სიტყვის მაგივრობის
გამწევი ხაზაკების გარეშე.

განათება: ერთი მაღალი წყარო ზედა მარცხენა მხრიდან. ყოველი მაკეტის ჩრდილი ქვემოთ და მარჯვნივ ეცემა,
ერთი და იმავე კუთხით, და მიწის ფირფიტაზე ბრტყლად წევს.

სტილი: მეგობრული, სათამაშოსებრი 3D ილუსტრაცია, მქრქალი ზედაპირებით, თბილი პალიტრით — ტერაკოტა,
კრემისფერი, მწვანე-ნაცრისფერი და მტვრიანი ლურჯი; ფოტორეალიზმის, ადამიანების, ავტომობილებისა და
ნებისმიერი ლოგოს გარეშე.

# ქართული სახელები ცარიელ ფირფიტებზე შემდეგ, დიზაინის პროგრამაში უნდა დაიდოს — სწორედ ამიტომ
# ითხოვს ეს პრომპტი მათ ცარიელს. თუ მაინც სთხოვ მოდელს წარწერების დაწერას, ქართული ასოები დიდი
# ალბათობით შესასწორებელი გამოვა — შედეგი ასოების დონეზე შეამოწმე.
---
Build a three-dimensional cartoon map of Tbilisi's landmarks — the kind printed on a tourist placemat.
16:9 horizontal, rendered at 2K. This is a stylised illustration, not a real map and not an aerial
photograph.
The ground plane is deliberately simplified and carries almost nothing: a broad pale sand-coloured plate;
the Mtkvari drawn as a smooth blue-grey ribbon curving through it from the upper right to the lower left;
one green mass for the wooded ridge on the west side; three or four tan ribbons for the main roads; and a
scatter of simple round trees. No small buildings, no street grid, no contour lines. Everything that is
not a landmark stays flat, quiet and low.
On that plate, stand the landmarks as chunky three-dimensional models seen from a high three-quarter
angle, each one rendered far larger than its true size relative to the ground — a single building is the
size of a city block, and that exaggeration is the whole idea. Simplify each model down to its most
recognisable silhouette, with rounded edges and no fine detail. Place, from the upper left to the lower
right: the fortress on the ridge with its stone towers and curtain wall; the funicular line climbing the
wooded slope to the tall thin television mast at the top; the cluster of low brick domes of the sulphur
baths by the river; the tall cathedral with its stepped gold dome on the east bank; a glass and steel
footbridge arching over the water; the columned opera house beside the main avenue; and the botanical
gorge with a small waterfall at the lower left. Keep every model upright and turned toward the viewer,
even where that is geographically imprecise — legibility beats accuracy here.
Each landmark stands on a small oval base raised slightly off the ground plate, with a soft contact
shadow under it.
Labels: place one blank label plate beside each of the seven landmarks and one larger blank plate across
the top centre of the frame. Each plate is a flat rounded rectangle in off-white with a thin grey border
and a small pointer aimed at the landmark it belongs to. Leave every plate completely empty — no
lettering, no placeholder text, no squiggles standing in for words.
Light: one high source from the upper left. Every model's shadow falls down and to the right at the same
angle and lies flat on the ground plate.
Style: friendly toy-like 3D illustration, matte surfaces, a warm palette of terracotta, cream, sage and
dusty blue, no photorealism, no people, no vehicles, no logos of any kind.
```

---

### NB-45 · Torn paper collage — an image through a ragged tear
`nano-banana` `gemini` — collage, paper, texture

**EN**
```
Make a single image of a photograph showing through a hand-torn hole in a sheet of paper. 1:1
square, rendered at 2K. There are two layers here and the difference between them is the whole
subject.

The top layer is a full-frame sheet of heavy grey-blue laid paper filling the image edge to edge,
photographed flat and straight on. It has a visible laid texture of fine parallel lines, a slightly
uneven cool tone and one soft crease running down the left quarter. This layer is matte and
absorbs light rather than reflecting it.

Through it, an opening about a third of the frame wide sits just right of centre and a little low.
It was torn by hand, not cut: the outline is irregular, with two long ragged runs, one short
straight section where the tear followed the grain of the sheet, and a small pinched notch at the
bottom. All the way round that edge the paper's core shows as a pale cream line roughly two
millimetres wide, with individual fibres lifting away from it and a few of them detached and
standing clear of the surface.

Along the upper edge of the opening the torn paper has lifted into a flap that curls toward the
viewer by about a centimetre. Under that flap lies a soft shadow, deepest where the flap stands
highest and fading to nothing where the paper settles flat again. The flap's underside is the same
cream core colour and catches a little light.

The lower layer, seen through the opening, is a photograph: a sunlit pebble beach with a shallow
wave drawing back over wet stones — sharp, saturated and warm. It must read as a separate, deeper
surface sitting a few millimetres below the paper, and the torn edge casts a thin shadow down onto
it along the top and the left of the opening.

Light: one soft source from the upper left, serving both layers. It grazes the paper so the laid
texture and the crease are clearly visible, and its direction matches the direction of the sun in
the photograph underneath, so the two layers belong to the same room even though they are different
images.

Style: studio still-life photography of a real physical object, natural colour, no digital collage
effects, no drop shadow added around the outside of the frame, nothing visible beyond the paper.
```

**KA**
```
შექმენი ერთი სურათი: ქაღალდის ფურცელში ხელით ამოგლეჯილ ხვრელში ფოტო მოჩანს. კვადრატული კადრი 1:1,
რენდერი 2K. აქ 2 ფენაა და მთავარი თემა სწორედ მათ შორის განსხვავებაა.

ზედა ფენა მძიმე, მოლურჯო-ნაცრისფერი, ვერჟეიანი ქაღალდის ფურცელია, რომელიც კადრს კიდიდან კიდემდე
ავსებს და ბრტყლად, პირდაპირაა გადაღებული. მას აქვს წვრილი პარალელური ხაზების ხილული ფაქტურა, ოდნავ
არათანაბარი, ცივი ტონი და მარცხენა მეოთხედში ერთი რბილი ნაკეცი. ეს ფენა მქრქალია და შუქს ირეკლავს
კი არა, ისრუტავს.

მასში, ცენტრიდან ოდნავ მარჯვნივ და ოდნავ დაბლა, კადრის სიგანის დაახლოებით მესამედის ხვრელია. ის
ხელით არის ამოგლეჯილი და არა ამოჭრილი: კონტური არათანაბარია — 2 გრძელი, დაფლეთილი მონაკვეთი, ერთი
მოკლე სწორი უბანი, სადაც გლეჯამ ფურცლის ბოჭკოს გაჰყვა, და ქვემოთ პატარა, მოჩქმეტილი ღარი. მთელ ამ
კიდეზე ქაღალდის შიდა ფენა ღია კრემისფერ, დაახლოებით 2 მილიმეტრის სიგანის ხაზად მოჩანს; მისგან
ცალკეული ბოჭკო ცილდება და რამდენიმე მათგანი ზედაპირს მოშორებული, ჰაერში დგას.

ხვრელის ზედა კიდეზე მოგლეჯილი ქაღალდი ფრთად აიწია და მაყურებლისკენ დაახლოებით სანტიმეტრით
იხრება. ამ ფრთის ქვეშ რბილი ჩრდილი წევს — ყველაზე ღრმა იქ, სადაც ფრთა მაღლა დგას, და ნელა ქრება
იქ, სადაც ქაღალდი ისევ ბრტყლად ჯდება. ფრთის შიდა მხარე იმავე კრემისფერია და ცოტა შუქს იჭერს.

ქვედა ფენა, რომელიც ხვრელში მოჩანს, ფოტოა: მზიანი კენჭებიანი სანაპირო, სადაც არაღრმა ტალღა სველ
ქვებზე უკან იწევს — მკვეთრი, მაძღარი და თბილი. ის ცალკე, უფრო ღრმა ზედაპირად უნდა იკითხებოდეს,
ქაღალდიდან რამდენიმე მილიმეტრით ქვემოთ; მოგლეჯილი კიდე ხვრელის ზემოთა და მარცხენა მხარეს მასზე
თხელ ჩრდილს აგდებს.

განათება: ერთი რბილი წყარო ზედა მარცხენა მხრიდან, ორივე ფენისთვის საერთო. ის ქაღალდს ირიბად ეცემა,
ამიტომ ვერჟეს ფაქტურა და ნაკეცი კარგად ჩანს; მისი მიმართულება ქვემოთ მდებარე ფოტოზე მზის
მიმართულებას ემთხვევა — ორი სხვადასხვა გამოსახულება ერთსა და იმავე ოთახს ეკუთვნის.

სტილი: ნამდვილი ფიზიკური საგნის სტუდიური ნატურმორტი, ბუნებრივი ფერი, ციფრული კოლაჟის ეფექტების
გარეშე, კადრის გარშემო დამატებული ჩრდილის გარეშე; ქაღალდს გარეთ არაფერი ჩანს.
---
Make a single image of a photograph showing through a hand-torn hole in a sheet of paper. 1:1 square,
rendered at 2K. There are two layers here and the difference between them is the whole subject.
The top layer is a full-frame sheet of heavy grey-blue laid paper filling the image edge to edge,
photographed flat and straight on. It has a visible laid texture of fine parallel lines, a slightly uneven
cool tone and one soft crease running down the left quarter. This layer is matte and absorbs light rather
than reflecting it.
Through it, an opening about a third of the frame wide sits just right of centre and a little low. It was
torn by hand, not cut: the outline is irregular, with two long ragged runs, one short straight section
where the tear followed the grain of the sheet, and a small pinched notch at the bottom. All the way round
that edge the paper's core shows as a pale cream line roughly two millimetres wide, with individual fibres
lifting away from it and a few of them detached and standing clear of the surface.
Along the upper edge of the opening the torn paper has lifted into a flap that curls toward the viewer by
about a centimetre. Under that flap lies a soft shadow, deepest where the flap stands highest and fading
to nothing where the paper settles flat again. The flap's underside is the same cream core colour and
catches a little light.
The lower layer, seen through the opening, is a photograph: a sunlit pebble beach with a shallow wave
drawing back over wet stones — sharp, saturated and warm. It must read as a separate, deeper surface
sitting a few millimetres below the paper, and the torn edge casts a thin shadow down onto it along the
top and the left of the opening.
Light: one soft source from the upper left, serving both layers. It grazes the paper so the laid texture
and the crease are clearly visible, and its direction matches the direction of the sun in the photograph
underneath, so the two layers belong to the same room even though they are different images.
Style: studio still-life photography of a real physical object, natural colour, no digital collage
effects, no drop shadow added around the outside of the frame, nothing visible beyond the paper.
```

---

### NB-46 · Recursive image-in-image — a print held up to its own view
`nano-banana` `gemini` — recursive, composite, alignment

**EN**
```
Photograph a hand holding a small print up against the view the print was made from, so that the
print continues the landscape behind it. 3:2 horizontal, rendered at 2K.

The scene: a gravel road running away from camera between two rows of tall poplars, a low stone
wall along the right-hand verge, a ridge of hills closing the distance and a wide sky with thin
cloud. Late afternoon, warm light coming from the left.

In the lower right of the frame a forearm and hand enter from the right edge and hold a matte
photographic print at arm's length. The print is about a quarter of the frame wide and its edges
are parallel to the edges of the photograph — not tilted. It is held by the thumb at its lower
right corner with two fingers behind it, and no finger crosses onto the printed image.

The alignment rule is what makes this picture work, so treat it as binding. The print shows the
same view from the same position, and every line that crosses its edge must meet its continuation
outside the print at the same height in the frame, at the same angle and at the same scale. The
horizon inside the print sits at exactly the same height as the horizon outside it. The right-hand
verge of the road, the top of the stone wall and the line of poplar trunks each pass behind the
print and reappear on the other side without a step, a kink or a change of thickness. If any of
those lines is offset where it crosses the print's edge, the image has failed and nothing else
about it matters.

What gives the print away, and only this: a white border about four millimetres wide on all four
sides; a slightly cool cast and one step less saturation than the live scene; a faint sheen where
the light catches its surface at a glancing angle; and a soft shadow cast by the print down onto
the hand below it.

Depth of field: focus on the print, so the poplars in the middle distance are gently soft and the
ridge softer still, while the print itself and the fingers are sharp.

Style: natural-light documentary photography, 50mm equivalent, f/2.8, natural colour, fine grain.
No face is visible and there is nobody else in the frame.
```

**KA**
```
გადაიღე კადრი, სადაც ხელს პატარა ფოტოანაბეჭდი უჭირავს იმ ხედის წინ, საიდანაც ეს ანაბეჭდი
გადაიღეს — ისე, რომ ანაბეჭდი უკანა პეიზაჟს აგრძელებს. ჰორიზონტალური კადრი 3:2, რენდერი 2K.

სცენა: ხრეშის გზა კამერიდან შორდება და მაღალი ალვის ხეების 2 რიგს შორის მიდის; მარჯვენა
გვერდულაზე დაბალი ქვის კედელი; სიშორეს გორაკების ქედი კეტავს; ზემოთ ფართო ცა თხელი ღრუბლით.
გვიანი შუადღე, თბილი შუქი მარცხნიდან.

კადრის ქვედა მარჯვენა ნაწილში მარჯვენა კიდიდან წინამხარი და ხელი შემოდის და მქრქალ ფოტოანაბეჭდს
გაწვდილ ხელზე იჭერს. ანაბეჭდი კადრის სიგანის დაახლოებით მეოთხედია და მისი კიდეები კადრის კიდეების
პარალელურია — დახრილი არ არის. ცერით ქვედა მარჯვენა კუთხეშია დაჭერილი, უკან კი 2 თითია; არცერთი
თითი დაბეჭდილ გამოსახულებაზე არ გადადის.

სურათს გასწორების წესი ამუშავებს — ეს სავალდებულოა. ანაბეჭდზე იგივე ხედია, იმავე წერტილიდან, და
ყოველი ხაზი, რომელიც ანაბეჭდის კიდეს კვეთს, გარეთ თავის გაგრძელებას უნდა შეხვდეს კადრში იმავე
სიმაღლეზე, იმავე კუთხით და იმავე მასშტაბით. ანაბეჭდის შიგნით ჰორიზონტი ზუსტად იმავე სიმაღლეზეა,
რაზეც გარეთ. გზის მარჯვენა გვერდულა, ქვის კედლის ზედა ხაზი და ალვის ხეების ღეროების ხაზი ანაბეჭდს
უკან გაივლის და მეორე მხარეს ისე გამოჩნდება, რომ არსად იყოს საფეხური, გადატეხვა ან სისქის ცვლილება.
თუ რომელიმე ეს ხაზი ანაბეჭდის კიდესთან გადახრილია, სურათი წარუმატებელია და დანარჩენს მნიშვნელობა
აღარ აქვს.

რით მოჩანს, რომ ეს ანაბეჭდია — მხოლოდ ამით: ოთხივე მხარეს დაახლოებით 4 მილიმეტრის სიგანის თეთრი
არშია; ცოცხალ სცენასთან შედარებით ოდნავ ცივი ტონი და ერთი საფეხურით ნაკლები სიხასხასე; სუსტი
ბზინვა იქ, სადაც შუქი მის ზედაპირს ირიბად ეცემა; და რბილი ჩრდილი, რომელსაც ანაბეჭდი ქვემოთ, ხელზე
აგდებს.

სიღრმის ველი: ფოკუსი ანაბეჭდზეა, ამიტომ შუა პლანის ალვის ხეები ოდნავ რბილია, ქედი კიდევ უფრო
რბილი, თავად ანაბეჭდი და თითები კი მკვეთრი.

სტილი: ბუნებრივ შუქზე გადაღებული დოკუმენტური ფოტო, 50 მმ ექვივალენტი, f/2.8, ბუნებრივი ფერი,
წვრილი მარცვალი. სახე არსად ჩანს და კადრში სხვა არავინაა.
---
Photograph a hand holding a small print up against the view the print was made from, so that the print
continues the landscape behind it. 3:2 horizontal, rendered at 2K.
The scene: a gravel road running away from camera between two rows of tall poplars, a low stone wall
along the right-hand verge, a ridge of hills closing the distance and a wide sky with thin cloud. Late
afternoon, warm light coming from the left.
In the lower right of the frame a forearm and hand enter from the right edge and hold a matte
photographic print at arm's length. The print is about a quarter of the frame wide and its edges are
parallel to the edges of the photograph — not tilted. It is held by the thumb at its lower right corner
with two fingers behind it, and no finger crosses onto the printed image.
The alignment rule is what makes this picture work, so treat it as binding. The print shows the same view
from the same position, and every line that crosses its edge must meet its continuation outside the print
at the same height in the frame, at the same angle and at the same scale. The horizon inside the print
sits at exactly the same height as the horizon outside it. The right-hand verge of the road, the top of
the stone wall and the line of poplar trunks each pass behind the print and reappear on the other side
without a step, a kink or a change of thickness. If any of those lines is offset where it crosses the
print's edge, the image has failed and nothing else about it matters.
What gives the print away, and only this: a white border about four millimetres wide on all four sides; a
slightly cool cast and one step less saturation than the live scene; a faint sheen where the light catches
its surface at a glancing angle; and a soft shadow cast by the print down onto the hand below it.
Depth of field: focus on the print, so the poplars in the middle distance are gently soft and the ridge
softer still, while the print itself and the fingers are sharp.
Style: natural-light documentary photography, 50mm equivalent, f/2.8, natural colour, fine grain. No face
is visible and there is nobody else in the frame.
```

---

### NB-47 · Product on an LED billboard, Pekini Avenue after rain
`nano-banana` `gemini` — mockup, billboard, night composite

**EN**
```
Build a night mockup of a product on a large LED billboard above Pekini Avenue in Tbilisi, after
rain. 16:9 horizontal, rendered at 2K. Treat it as a composite that has to survive being looked at
closely, not as a glowing rectangle pasted onto a street photograph.

The board: a landscape LED screen roughly eight metres wide, mounted on the flank of a late-Soviet
apartment block about four storeys up, with a visible steel frame around it and a maintenance
walkway along its bottom edge.

Viewing angle: the camera stands on the pavement on the opposite side of the avenue, about twenty
degrees off the screen's axis and well below it. The screen is therefore seen foreshortened — the
near edge is taller than the far edge, the horizontal lines of the frame converge toward the far
side, and the panel's brightness falls off gently toward that far edge, because LED panels are
directional and do not read as evenly bright from an angle.

Screen structure, and it must be visible at this distance: the image on the screen is made of
discrete LED dots on a regular grid with dark gaps between them, the dot pitch coarse enough to
read as texture rather than as smooth pixels. Give it one faint horizontal band of slightly
different brightness across the middle, as real panels have, and a soft moiré where the dot grid
meets the camera's sensor. The blacks on the screen are not true black but a dark grey lifted by
the panel's own glow.

What is on the screen: an invented product image only — a plain amber glass bottle standing on a
deep teal field, lit from its left, with a soft gradient behind it. Leave the lower fifth of the
screen as an empty flat teal band. No brand name, no logo, no wordmark and no lettering of any kind
anywhere on the screen. Every other sign, shopfront and vehicle in the frame is likewise free of
readable text and free of logos.

The light the screen throws into the street is what makes the composite believable, so build it
deliberately: a teal and amber wash across the wet asphalt directly below and slightly toward
camera, weakening with distance; a long smeared reflection of the whole board in the standing water
of the road, broken by ripples and by the ruts of tyre tracks; teal rim light along the wet kerb
and on the roofs and bonnets of two parked cars; a cool cast on the lower half of the building
opposite; and a faint haze in the air where the light passes through it.

Everything else in the street stays dark and ordinary: sodium-orange street lamps much warmer than
the screen, a few lit apartment windows, bare plane trees, and no pedestrian close enough to be
recognisable.

Style: night urban photography, 35mm equivalent, tripod, long exposure, natural colour, no lens
flare added and no artificial bloom around the screen beyond what the haze itself produces.
```

**KA**
```
ააგე ღამის მაკეტი: პროდუქტი დიდ LED-ეკრანზე თბილისში, პეკინის გამზირზე, წვიმის შემდეგ.
ჰორიზონტალური კადრი 16:9, რენდერი 2K. ეს სარეკლამო მაკეტირების სამუშაოა — ისეთი მონტაჟი, რომელმაც
ახლოდან დათვალიერებას უნდა გაუძლოს და არა ქუჩის ფოტოზე მიწებებული მბზინავი მართკუთხედი.

ფარი: ჰორიზონტალური LED-ეკრანი, დაახლოებით 8 მეტრი სიგანით, გვიანსაბჭოური საცხოვრებელი კორპუსის
გვერდით კედელზე, დაახლოებით მე-4 სართულის სიმაღლეზე; გარშემო ხილული ფოლადის კარკასი, ქვედა კიდეზე
კი მომსახურების ბაქანი.

დაკვირვების კუთხე: კამერა გამზირის მოპირდაპირე მხარეს, ტროტუარზე დგას, ეკრანის ღერძიდან
დაახლოებით 20 გრადუსით გადახრილი და მასზე ბევრად დაბლა. ამიტომ ეკრანი შემოკლებულად ჩანს — ახლო
კიდე უფრო მაღალია, ვიდრე შორეული; კარკასის ჰორიზონტალური ხაზები შორეული მხარისკენ უახლოვდება
ერთმანეთს; ეკრანის სიკაშკაშე კი შორეული კიდისკენ ნელა ეცემა, რადგან LED-პანელი მიმართულია და
ირიბად არათანაბრად ანათებს.

ეკრანის სტრუქტურა და ის ამ მანძილიდან ხილული უნდა იყოს: გამოსახულება შედგება ცალკეული LED-წერტილისგან,
რომლებიც წესიერ ბადეზე დგას და მათ შორის მუქი ღრიჭოებია; წერტილებს შორის ბიჯი იმდენად მსხვილია, რომ
ფაქტურად იკითხებოდეს და არა გლუვ პიქსელად. შუაში ჩაუტარე ერთი სუსტი ჰორიზონტალური ზოლი ოდნავ
განსხვავებული სიკაშკაშით, როგორც ნამდვილ პანელს აქვს, და რბილი მუარე იქ, სადაც ბადე კამერის მატრიცას
ხვდება. ეკრანზე შავი ნამდვილი შავი არ არის — ის მუქი ნაცრისფერია, თავად პანელის ნათებით აწეული.

რა არის ეკრანზე: მხოლოდ გამოგონილი პროდუქტის გამოსახულება — ქარვისფერი მინის უბრალო ბოთლი მუქ
ზურმუხტისფერ-ცისფერ ფონზე, მარცხნიდან განათებული, უკან რბილი გრადიენტით. ეკრანის ქვედა მეხუთედი
დატოვე ცარიელ, ერთფეროვან ზოლად. ეკრანზე არსად არ იყოს არც ბრენდის სახელი, არც ლოგო, არც
სავაჭრო ნიშანი და არც რაიმე წარწერა. კადრში ყველა სხვა აბრა, ვიტრინა და ავტომობილიც ასევე
წაკითხვადი ტექსტისა და ლოგოს გარეშეა.

მონტაჟს დამაჯერებლობას ქუჩაში გადმოსული შუქი ანიჭებს, ამიტომ ის შეგნებულად ააგე: ზურმუხტისფერი და
ქარვისფერი ლაქა უშუალოდ ქვემოთ, სველ ასფალტზე, კამერისკენ ოდნავ გადმოწეული და მანძილთან ერთად
სუსტდება; მთელი ფარის გრძელი, გაზელილი ანარეკლი გზაზე შემდგარ წყალში, ტალღებითა და საბურავების
ნაკვალევით დაფლეთილი; ზურმუხტისფერი კონტურის შუქი სველ ბორდიურზე და 2 გაჩერებული ავტომობილის
სახურავსა და კაპოტზე; ცივი ტონი მოპირდაპირე შენობის ქვედა ნახევარზე; და სუსტი ნისლი ჰაერში, სადაც
შუქი გაივლის.

ქუჩაში დანარჩენი ყველაფერი ბნელი და ჩვეულებრივი რჩება: ნატრიუმის ნარინჯისფერი ფარნები ეკრანზე
ბევრად თბილი, რამდენიმე განათებული ბინის ფანჯარა, შიშველი ჭადრები და არცერთი ფეხით მოსიარულე
იმდენად ახლოს, რომ ამოსაცნობი იყოს.

სტილი: ღამის ურბანული ფოტოგრაფია, 35 მმ ექვივალენტი, შტატივი, გრძელი ექსპოზიცია, ბუნებრივი ფერი,
ობიექტივის ხელოვნური ბრწყინვის გარეშე და ეკრანის გარშემო ხელოვნური შარავანდის გარეშე — გარდა იმისა,
რასაც თავად ნისლი იძლევა.
---
Build a night mockup of a product on a large LED billboard above Pekini Avenue in Tbilisi, after rain.
16:9 horizontal, rendered at 2K. Treat it as a composite that has to survive being looked at closely, not
as a glowing rectangle pasted onto a street photograph.
The board: a landscape LED screen roughly eight metres wide, mounted on the flank of a late-Soviet
apartment block about four storeys up, with a visible steel frame around it and a maintenance walkway
along its bottom edge.
Viewing angle: the camera stands on the pavement on the opposite side of the avenue, about twenty degrees
off the screen's axis and well below it. The screen is therefore seen foreshortened — the near edge is
taller than the far edge, the horizontal lines of the frame converge toward the far side, and the panel's
brightness falls off gently toward that far edge, because LED panels are directional and do not read as
evenly bright from an angle.
Screen structure, and it must be visible at this distance: the image on the screen is made of discrete LED
dots on a regular grid with dark gaps between them, the dot pitch coarse enough to read as texture rather
than as smooth pixels. Give it one faint horizontal band of slightly different brightness across the
middle, as real panels have, and a soft moiré where the dot grid meets the camera's sensor. The blacks on
the screen are not true black but a dark grey lifted by the panel's own glow.
What is on the screen: an invented product image only — a plain amber glass bottle standing on a deep teal
field, lit from its left, with a soft gradient behind it. Leave the lower fifth of the screen as an empty
flat teal band. No brand name, no logo, no wordmark and no lettering of any kind anywhere on the screen.
Every other sign, shopfront and vehicle in the frame is likewise free of readable text and free of logos.
The light the screen throws into the street is what makes the composite believable, so build it
deliberately: a teal and amber wash across the wet asphalt directly below and slightly toward camera,
weakening with distance; a long smeared reflection of the whole board in the standing water of the road,
broken by ripples and by the ruts of tyre tracks; teal rim light along the wet kerb and on the roofs and
bonnets of two parked cars; a cool cast on the lower half of the building opposite; and a faint haze in
the air where the light passes through it.
Everything else in the street stays dark and ordinary: sodium-orange street lamps much warmer than the
screen, a few lit apartment windows, bare plane trees, and no pedestrian close enough to be recognisable.
Style: night urban photography, 35mm equivalent, tripod, long exposure, natural colour, no lens flare
added and no artificial bloom around the screen beyond what the haze itself produces.
```

---

### NB-48 · Pencil wireframe raised to a high-fidelity UI mockup
`nano-banana` `gemini` — ui, mockup, editing, georgian text

**EN**
```
Turn the attached pencil wireframe into a high-fidelity interface mockup. 9:16 vertical, rendered
at 2K. This is a fidelity upgrade, not a redesign, and that distinction matters more than anything
else in this brief.

What the sketch contains, top to bottom, so you read it correctly: a status bar scrawl; a header
row with a back arrow on the left and a circular avatar on the right; a large title line; a
horizontal row of four small square category tiles, each with a scribbled icon and a short label
under it; a wide search field with a magnifier at its left end; a vertical list of five result
cards, each card being a square thumbnail on the left, two lines of text to the right of it and a
small price block at the far right; and a bottom bar with five evenly spaced icon slots, the second
of which is circled to mark it as active.

What must stay exactly as drawn: the order of the sections from top to bottom; the number of items
in every group — 4 category tile, 5 result card, 5 bottom-bar slot; the position of every element
within its row; the side of the row each element sits on; the relative heights of the sections; and
the proportions of every block, to within a few percent of the sketch. Do not move, add, remove,
merge, split or reorder anything. Do not introduce a component that is not in the sketch and do not
drop one because it looks redundant. Where a part of the sketch is ambiguous, keep its position and
give it the plainest possible treatment rather than inventing a different component in its place.

What changes is only the fidelity. Replace the pencil lines with clean geometry aligned to an
8-point grid. Give the cards a white surface, a 12-pixel corner radius and a soft shadow at 8
percent opacity. Replace the scribbled icons with consistent 24-pixel line icons at a uniform
1.5-pixel stroke weight. Set the type in a single clean sans-serif at three sizes only — title,
card heading, secondary line. Fill the thumbnails with soft neutral grey placeholder blocks. Use
one accent colour, a muted teal, for the active bottom-bar slot and for the price figures, and
greys for everything else. Put the whole screen on a very light warm grey background.

Text in the image, spelled exactly as written here: the title is "ახლოს შენთან"; the four category
labels are "საუზმე", "ფუნთუშა", "ტორტი", "პური"; the search field placeholder is "მოძებნე"; and
the price block on every card reads "₾ 12". The two text lines inside each card are drawn as
neutral grey bars of the right length rather than as words.

Style: clean product design mockup, flat, no device frame, no hand holding the phone, no background
scene, no decorative illustration, no logo.

# Georgian letterforms will very likely come back malformed at these small sizes. The reliable
# route is to ask for every label area to be left empty as a grey bar as well, and to set the
# Georgian type in a design tool afterwards — either way, check the result letter by letter.
```

**KA**
```
მიმაგრებული ფანქრის მონახაზი გადააქციე მაღალი სიზუსტის ინტერფეისის მაკეტად. ვერტიკალური კადრი 9:16,
რენდერი 2K. ეს სიზუსტის ამაღლებაა და არა ხელახალი დიზაინი — ამ ბრიფში ეს განსხვავება ყველაფერზე
მნიშვნელოვანია.

რა არის მონახაზზე, ზემოდან ქვემოთ, რომ სწორად წაიკითხო: სტატუსის ზოლის ხაზაკი; ზედა რიგი, მარცხნივ
უკან ისრითა და მარჯვნივ მრგვალი ავატარით; დიდი სათაურის ხაზი; 4 პატარა, კვადრატული კატეგორიის ფილის
ჰორიზონტალური რიგი, თითოეულზე ნახაზული ხატულა და ქვემოთ მოკლე წარწერა; განიერი საძიებო ველი
მარცხენა ბოლოში ლუპით; 5 შედეგის ბარათის ვერტიკალური სია, სადაც ყოველი ბარათი მარცხნივ კვადრატული
მინიატურაა, მის მარჯვნივ 2 ხაზი ტექსტი, ბოლო მარჯვენა მხარეს კი ფასის პატარა ბლოკი; და ქვედა ზოლი
5 თანაბრად განლაგებული ხატულის ადგილით, სადაც მეორე შემოხაზულია და აქტიურად აღნიშნული.

რა რჩება ზუსტად ისე, როგორც დახატულია: სექციების თანმიმდევრობა ზემოდან ქვემოთ; ელემენტების
რაოდენობა ყოველ ჯგუფში — 4 კატეგორიის ფილა, 5 შედეგის ბარათი, 5 ქვედა ზოლის ადგილი; ყოველი
ელემენტის მდებარეობა თავის რიგში; რიგის რომელ მხარესაც ელემენტი ზის; სექციების სიმაღლეთა
თანაფარდობა; და ყოველი ბლოკის პროპორცია მონახაზთან რამდენიმე პროცენტის სიზუსტით. არაფერი გადაადგილო,
არაფერი დაამატო, არაფერი ამოიღო, არაფერი გააერთიანო, არაფერი გაყო და თანმიმდევრობა არ შეცვალო.
არ შემოიტანო კომპონენტი, რომელიც მონახაზზე არ არის, და არ ამოაგდო ისეთი, რომელიც ზედმეტად გეჩვენება.
სადაც მონახაზი ბუნდოვანია, შეუნარჩუნე ადგილი და ყველაზე მარტივი გადაწყვეტა მიეცი — სხვა კომპონენტი
არ გამოიგონო.

იცვლება მხოლოდ სიზუსტე. ფანქრის ხაზები შეცვალე სუფთა გეომეტრიით, 8-პიქსელიან ბადეზე გასწორებული.
ბარათებს მიეცი თეთრი ზედაპირი, 12 პიქსელი მომრგვალება კუთხეებში და რბილი ჩრდილი 8 პროცენტის
გამჭვირვალობით. ნახაზული ხატულები შეცვალე ერთგვაროვანი, 24-პიქსელიანი ხაზოვანი ხატულებით, შტრიხის
ერთიანი სისქით — 1.5 პიქსელი. ტექსტი აკრიფე ერთი სუფთა უსერიფო შრიფტით და მხოლოდ 3 ზომით —
სათაური, ბარათის სათაური, მეორეული ხაზი. მინიატურები შეავსე რბილი, ნეიტრალური ნაცრისფერი ბლოკებით.
გამოიყენე ერთი აქცენტის ფერი — დაწყნარებული ზურმუხტისფერ-ცისფერი — ქვედა ზოლის აქტიური ადგილისა და
ფასის ციფრებისთვის, დანარჩენისთვის კი ნაცრისფერი. მთელი ეკრანი დადე ძალიან ღია, თბილ ნაცრისფერ ფონზე.

წარწერა სურათში, ზუსტად ასე: სათაური — „ახლოს შენთან“; 4 კატეგორიის წარწერა — „საუზმე“, „ფუნთუშა“,
„ტორტი“, „პური“; საძიებო ველის მინიშნება — „მოძებნე“; ყოველი ბარათის ფასის ბლოკი — „₾ 12“.
ბარათის შიგნით 2 ტექსტის ხაზი სიტყვების ნაცვლად შესაბამისი სიგრძის ნეიტრალური ნაცრისფერი ზოლით
დახატე.

სტილი: სუფთა პროდუქტის დიზაინის მაკეტი, ბრტყელი, მოწყობილობის კორპუსის გარეშე, ტელეფონის მჭერი
ხელის გარეშე, ფონური სცენის, დეკორატიული ილუსტრაციისა და ლოგოს გარეშე.

# ამ ზომაზე ქართული ასოები დიდი ალბათობით დამახინჯებული გამოვა. საიმედო გზაა, სთხოვო მოდელს,
# წარწერის ადგილიც ნაცრისფერ ზოლად დატოვოს ცარიელი და ქართული შრიფტი შემდეგ დიზაინის პროგრამაში
# დაადო — ორივე შემთხვევაში შედეგი ასოების დონეზე შეამოწმე.
---
Turn the attached pencil wireframe into a high-fidelity interface mockup. 9:16 vertical, rendered at 2K.
This is a fidelity upgrade, not a redesign, and that distinction matters more than anything else in this
brief.
What the sketch contains, top to bottom, so you read it correctly: a status bar scrawl; a header row with
a back arrow on the left and a circular avatar on the right; a large title line; a horizontal row of four
small square category tiles, each with a scribbled icon and a short label under it; a wide search field
with a magnifier at its left end; a vertical list of five result cards, each card being a square thumbnail
on the left, two lines of text to the right of it and a small price block at the far right; and a bottom
bar with five evenly spaced icon slots, the second of which is circled to mark it as active.
What must stay exactly as drawn: the order of the sections from top to bottom; the number of items in
every group — four category tiles, five result cards, five bottom-bar slots; the position of every element
within its row; the side of the row each element sits on; the relative heights of the sections; and the
proportions of every block, to within a few percent of the sketch. Do not move, add, remove, merge, split
or reorder anything. Do not introduce a component that is not in the sketch and do not drop one because it
looks redundant. Where a part of the sketch is ambiguous, keep its position and give it the plainest
possible treatment rather than inventing a different component in its place.
What changes is only the fidelity. Replace the pencil lines with clean geometry aligned to an 8-point
grid. Give the cards a white surface, a 12-pixel corner radius and a soft shadow at 8 percent opacity.
Replace the scribbled icons with consistent 24-pixel line icons at a uniform 1.5-pixel stroke weight. Set
the type in a single clean sans-serif at three sizes only — title, card heading, secondary line. Fill the
thumbnails with soft neutral grey placeholder blocks. Use one accent colour, a muted teal, for the active
bottom-bar slot and for the price figures, and greys for everything else. Put the whole screen on a very
light warm grey background.
Text in the image, spelled exactly as written here: the title is "ახლოს შენთან"; the four category labels
are "საუზმე", "ფუნთუშა", "ტორტი", "პური"; the search field placeholder is "მოძებნე"; and the price block
on every card reads "₾ 12". The two text lines inside each card are drawn as neutral grey bars of the
right length rather than as words.
Style: clean product design mockup, flat, no device frame, no hand holding the phone, no background scene,
no decorative illustration, no logo.
```

---

### NB-49 · Composition rescue — outpainting a crop back outward
`nano-banana` `gemini` — outpainting, editing, composition

**EN**
```
Extend the attached photograph outward. The original is a 1:1 square frame of a brick arcade along
one side of a courtyard, shot from under the arcade looking down its length, with the columns
receding toward a point right of centre. Output a 3:2 horizontal frame.

How the canvas is laid out: the original image keeps its full height and sits centred in the new
frame, and the extension is added to the left and to the right in equal amounts. Nothing is added
above or below. The original is not scaled, not rotated, not shifted and not re-cropped.

The existing pixels are not yours to touch. Every part of the original must survive unchanged —
same position, same colour, same brightness, same sharpness, same grain, same imperfections. Do not
re-render the arcade, do not clean up the brickwork, do not straighten a column, do not correct the
exposure, do not remove the dust spot in the upper area, do not sharpen and do not denoise. Do not
reinterpret anything that is already visible: if a detail is ambiguous in the original, it stays
ambiguous in the result.

In the new area on both sides, continue the scene as the camera would have recorded it. Three
things must carry across the seam without a break.

Perspective: the arch line, the floor line and the top of the column plinths all converge toward
the same vanishing point as in the original. Extend each one along its existing trajectory. Do not
start a second arcade at a different angle. The columns in the new area sit at the same rhythm as
the existing ones, spaced by that same perspective, narrowing at the correct rate.

Light: the sun enters from the left at the same angle. Every new shadow falls in the same
direction, at the same length for its object's height, with the same softness of edge and the same
colour in its fill as the shadows already in the frame. Brightness at the seam matches on both
sides closely enough that nothing shows.

Rendering character: the new area carries the same grain size and strength, the same depth of field
for its distance from the camera, the same slight fall in sharpness toward the corners, the same
mild vignetting continued outward, and the same colour treatment. It must be impossible to say
where the original ends.

Add no new subject of interest in the extension. It continues the same arcade, the same courtyard
wall and the same paving — nothing that pulls the eye away from what was already there, and no
person, animal or vehicle that was not in the original.
```

**KA**
```
გააფართოვე მიმაგრებული ფოტო. ორიგინალი კვადრატული კადრია, 1:1: ეზოს ერთ მხარეს გაყოლილი აგურის
არკადა, არკადის ქვემოდან, სიგრძეზე გადაღებული; სვეტები ცენტრიდან მარჯვნივ მდებარე წერტილისკენ
შორდება. გამოსავალი — ჰორიზონტალური კადრი 3:2.

როგორ ეწყობა ტილო: ორიგინალი სრულ სიმაღლეს ინარჩუნებს და ახალ კადრში ცენტრში ზის; დამატება მარცხნივ
და მარჯვნივ თანაბარი რაოდენობით ხდება. ზემოთ და ქვემოთ არაფერი ემატება. ორიგინალი არ მასშტაბდება,
არ ბრუნავს, არ ინაცვლებს და ხელახლა არ კადრირდება.

არსებულ პიქსელს ხელს არ ახლებ. ორიგინალის ყოველი ნაწილი უცვლელი რჩება — იმავე ადგილას, იმავე ფერით,
იმავე სიკაშკაშით, იმავე სიმკვეთრით, იმავე მარცვლითა და იმავე ნაკლით. არკადა ხელახლა არ დაარენდერო,
აგურის წყობა არ გაასუფთავო, სვეტი არ გაასწორო, ექსპოზიცია არ შეასწორო, ზედა ნაწილში მტვრის ლაქა არ
მოაშორო, სიმკვეთრე არ აწიო და ხმაური არ დაავიწროვო. არაფერი გადაიაზრო, რაც უკვე ჩანს: თუ დეტალი
ორიგინალში ბუნდოვანია, ის შედეგშიც ბუნდოვანი რჩება.

ორივე მხარეს ახალ არეში სცენა ისე გააგრძელე, როგორც კამერა ჩაწერდა. ნაკერზე 3 რამ უნდა გადავიდეს
გაწყვეტის გარეშე.

პერსპექტივა: თაღების ხაზი, იატაკის ხაზი და სვეტების კვარცხლბეკების ზედა ხაზი იმავე გაქრობის
წერტილისკენ უახლოვდება ერთმანეთს, რომელიც ორიგინალშია. თითოეული თავისივე ტრაექტორიით გააგრძელე.
სხვა კუთხით მეორე არკადა არ დაიწყო. ახალ არეში სვეტები იმავე რიტმით დგას, იმავე პერსპექტივით
განაწილებული, და სწორი ტემპით ვიწროვდება.

განათება: მზე მარცხნიდან შემოდის, იმავე კუთხით. ყოველი ახალი ჩრდილი იმავე მიმართულებით ეცემა, თავისი
საგნის სიმაღლის შესაბამისი სიგრძით, კიდის იმავე სირბილითა და შევსების იმავე ფერით, როგორიც კადრში
უკვე არსებულ ჩრდილებს აქვს. ნაკერზე სიკაშკაშე ორივე მხარეს იმდენად ემთხვევა, რომ არაფერი ჩანდეს.

რენდერის ხასიათი: ახალ არეს აქვს იგივე მარცვლის ზომა და სიძლიერე, კამერიდან იმ მანძილის შესაბამისი
სიღრმის ველი, კუთხეებისკენ სიმკვეთრის იგივე მსუბუქი დაცემა, იგივე სუსტი ვინიეტირება გარეთ
გაგრძელებული და ფერის იგივე დამუშავება. შეუძლებელი უნდა იყოს იმის თქმა, სად მთავრდება ორიგინალი.

დამატებულ არეში ახალი აქცენტი არ შემოიტანო. იქ იგივე არკადა, იგივე ეზოს კედელი და იგივე მოკირწყლული
იატაკი გრძელდება — არაფერი, რაც მზერას უკვე არსებულს მოაშორებს, და არც ადამიანი, ცხოველი თუ
ავტომობილი, რომელიც ორიგინალში არ იყო.
---
Extend the attached photograph outward. The original is a 1:1 square frame of a brick arcade along one
side of a courtyard, shot from under the arcade looking down its length, with the columns receding toward
a point right of centre. Output a 3:2 horizontal frame.
How the canvas is laid out: the original image keeps its full height and sits centred in the new frame,
and the extension is added to the left and to the right in equal amounts. Nothing is added above or below.
The original is not scaled, not rotated, not shifted and not re-cropped.
The existing pixels are not yours to touch. Every part of the original must survive unchanged — same
position, same colour, same brightness, same sharpness, same grain, same imperfections. Do not re-render
the arcade, do not clean up the brickwork, do not straighten a column, do not correct the exposure, do not
remove the dust spot in the upper area, do not sharpen and do not denoise. Do not reinterpret anything
that is already visible: if a detail is ambiguous in the original, it stays ambiguous in the result.
In the new area on both sides, continue the scene as the camera would have recorded it. Three things must
carry across the seam without a break.
Perspective: the arch line, the floor line and the top of the column plinths all converge toward the same
vanishing point as in the original. Extend each one along its existing trajectory. Do not start a second
arcade at a different angle. The columns in the new area sit at the same rhythm as the existing ones,
spaced by that same perspective, narrowing at the correct rate.
Light: the sun enters from the left at the same angle. Every new shadow falls in the same direction, at
the same length for its object's height, with the same softness of edge and the same colour in its fill as
the shadows already in the frame. Brightness at the seam matches on both sides closely enough that nothing
shows.
Rendering character: the new area carries the same grain size and strength, the same depth of field for
its distance from the camera, the same slight fall in sharpness toward the corners, the same mild
vignetting continued outward, and the same colour treatment. It must be impossible to say where the
original ends.
Add no new subject of interest in the extension. It continues the same arcade, the same courtyard wall and
the same paving — nothing that pulls the eye away from what was already there, and no person, animal or
vehicle that was not in the original.
```

---

### NB-50 · Removing a person and an object — clean plate reconstruction
`nano-banana` `gemini` — cleanup, editing, clean plate

**EN**
```
Remove two things from the attached photograph and reconstruct what was behind them. The image is a
3:2 horizontal shot of a carved stone church façade in flat overcast light. Keep the same 3:2 frame
and do not re-crop.

Remove exactly two elements: the visitor in the red jacket standing in the lower right third in
front of the lower carved band, and the green metal rubbish bin at the left edge of the steps.
Remove each of them completely, including its own contact shadow on the paving and the darker band
the bin casts up the bottom of the wall.

Put nothing in their place. Do not replace the person with another person, with the shadow of a
person, with a bag, a bollard, a plant or any other object, and do not add a new element anywhere
to balance the composition. Both areas become the continuation of the surfaces that surrounded
them, and nothing more than that.

Reconstruct each gap from its own neighbourhood. Where the person stood, rebuild the paving with
the same slab size, the same joint width, the same joint direction and the same wear pattern as the
paving on either side, and continue the carved stone band behind them so that its rhythm of figures
and its depth of relief run straight through — no repeated motif, no mirrored patch, no smeared
section. Where the bin stood, continue the step nosing and the plinth line at their existing
heights. The light stays flat and overcast, so the reconstructed areas carry the same soft, almost
directionless shading as their neighbours, with no new highlight and no new cast shadow.

Match the surrounding rendering exactly: the same grain size and strength, the same micro-texture
in the stone — pitting, lichen, old rain staining — the same sharpness for that distance from the
camera, and the same colour and brightness. A patch that is smoother, cleaner or flatter than the
stone around it is a failure even when nothing obvious is missing.

Everything outside the two removed areas stays pixel-identical: the whole façade, the carving, the
doorway, the steps, the sky along the top edge, the framing, the exposure, the white balance and
the grain. Do not relight the wall, do not straighten the verticals and do not tidy anything else
while you are in there.
```

**KA**
```
ამოიღე მიმაგრებული ფოტოდან 2 რამ და აღადგინე ის, რაც მათ უკან იყო. სურათი ჰორიზონტალური კადრია,
3:2: მოჩუქურთმებული ქვის ტაძრის ფასადი მოღრუბლულ, თანაბარ შუქზე. კადრის პროპორცია იგივე რჩება, 3:2,
და ხელახლა არ დააკადრირო.

ამოიღე ზუსტად 2 ელემენტი: წითელქურთუკიანი ვიზიტორი, რომელიც ქვედა მარჯვენა მესამედში, ქვედა
ჩუქურთმის ზოლის წინ დგას, და მწვანე ლითონის ნაგვის ურნა კიბის მარცხენა კიდესთან. თითოეული სრულად
მოაშორე — მათ შორის იატაკზე დაცემული ჩრდილიც და ის მუქი ზოლიც, რომელსაც ურნა კედლის ძირზე აჩენს.

მათ ადგილას არაფერი ჩასვა. ადამიანი არ ჩაანაცვლო სხვა ადამიანით, ადამიანის ჩრდილით, ჩანთით, ბოძით,
მცენარით ან რაიმე სხვა საგნით და კომპოზიციის გასაწონასწორებლად არსად არ დაამატო ახალი ელემენტი.
ორივე არე მხოლოდ იმ ზედაპირების გაგრძელება ხდება, რომლებიც მათ გარშემო იყო — და მეტი არაფერი.

ყოველი ხვრელი მისივე გარემოდან აღადგინე. იქ, სადაც ადამიანი იდგა, ხელახლა ააგე მოკირწყლული იატაკი —
იმავე ფილის ზომით, ნაკერის იმავე სიგანით, ნაკერის იმავე მიმართულებითა და ცვეთის იმავე ნახატით,
როგორიც ორივე მხარესაა; უკან კი ქვის ჩუქურთმის ზოლი ისე გააგრძელე, რომ ფიგურების რიტმი და რელიეფის
სიღრმე გაუწყვეტლად გაიაროს — გამეორებული მოტივის, სარკისებური ასლისა და გადაზელილი უბნის გარეშე.
იქ, სადაც ურნა იდგა, საფეხურის კიდე და ცოკოლის ხაზი მათსავე სიმაღლეზე გააგრძელე. შუქი ისევ თანაბარი
და მოღრუბლულია, ამიტომ აღდგენილ არეებს იგივე რბილი, თითქმის უმიმართულებო ჩრდილი აქვს, ახალი
ბზინვისა და ახალი დაცემული ჩრდილის გარეშე.

გარშემო რენდერს ზუსტად მოერგე: იგივე მარცვლის ზომა და სიძლიერე, ქვის იგივე მიკროფაქტურა —
დაწერტილება, ხავსი, წვიმის ძველი ლაქები — კამერიდან იმ მანძილის შესაბამისი სიმკვეთრე და იგივე ფერი
და სიკაშკაშე. უბანი, რომელიც გარშემო ქვაზე უფრო გლუვი, უფრო სუფთა ან უფრო ბრტყელია, წარუმატებლობაა
მაშინაც კი, როცა თვალშისაცემად არაფერი აკლია.

ამოღებული 2 არის გარეთ ყველაფერი პიქსელამდე უცვლელი რჩება: მთელი ფასადი, ჩუქურთმა, კარის ღიობი,
კიბე, ცა ზედა კიდეზე, კადრირება, ექსპოზიცია, თეთრის ბალანსი და მარცვალი. კედელი ხელახლა არ გაანათო,
ვერტიკალები არ გაასწორო და სხვა არაფერი მოალამაზო, სანამ იქ მუშაობ.
---
Remove two things from the attached photograph and reconstruct what was behind them. The image is a 3:2
horizontal shot of a carved stone church façade in flat overcast light. Keep the same 3:2 frame and do not
re-crop.
Remove exactly two elements: the visitor in the red jacket standing in the lower right third in front of
the lower carved band, and the green metal rubbish bin at the left edge of the steps. Remove each of them
completely, including its own contact shadow on the paving and the darker band the bin casts up the bottom
of the wall.
Put nothing in their place. Do not replace the person with another person, with the shadow of a person,
with a bag, a bollard, a plant or any other object, and do not add a new element anywhere to balance the
composition. Both areas become the continuation of the surfaces that surrounded them, and nothing more
than that.
Reconstruct each gap from its own neighbourhood. Where the person stood, rebuild the paving with the same
slab size, the same joint width, the same joint direction and the same wear pattern as the paving on
either side, and continue the carved stone band behind them so that its rhythm of figures and its depth of
relief run straight through — no repeated motif, no mirrored patch, no smeared section. Where the bin
stood, continue the step nosing and the plinth line at their existing heights. The light stays flat and
overcast, so the reconstructed areas carry the same soft, almost directionless shading as their
neighbours, with no new highlight and no new cast shadow.
Match the surrounding rendering exactly: the same grain size and strength, the same micro-texture in the
stone — pitting, lichen, old rain staining — the same sharpness for that distance from the camera, and the
same colour and brightness. A patch that is smoother, cleaner or flatter than the stone around it is a
failure even when nothing obvious is missing.
Everything outside the two removed areas stays pixel-identical: the whole façade, the carving, the
doorway, the steps, the sky along the top edge, the framing, the exposure, the white balance and the
grain. Do not relight the wall, do not straighten the verticals and do not tidy anything else while you
are in there.
```
