# Voice & music / ხმა და მუსიკა

Speech, music and podcast production. Shapes follow
[`../../references/tool-routing.md`](../../references/tool-routing.md) §Audio:
speech is `[emotion] [pace] [emphasis markers] [pause markers]`, music is
`[genre] [instrumentation] [BPM] [key/mood] [structure] [vocals or instrumental] [reference era]`.
Give the emotional **state** and let the read follow from it — `quietly furious` beats `say this angrily` —
and **mark** pauses with punctuation or break tags instead of describing them in prose.

**On the Georgian block.** ElevenLabs, Suno and Udio all take English direction far more reliably than
Georgian, so for AU-01 – AU-09 the `**KA**` block is a *working version*: the same brief in Georgian, so
you can build it and argue about it in your own language — then, after the `---` line, the string you
actually paste. Where the *spoken output* is Georgian, the pasted string keeps the direction in English
and the script in Georgian, because the script is the thing being read aloud.

**Georgian speech synthesis.** Quality varies enormously between providers — the same script can come
back clean from one voice and unusable from another, and Georgian text often needs phonetic respelling
or a manual re-record before it ships. Budget for a listen-through on every Georgian line.
ქართული TTS-ის ხარისხი პროვაიდერების მიხედვით მკვეთრად განსხვავდება — ერთი და იგივე ტექსტი ერთ ხმაში სუფთად წამოვა, მეორეში გამოუსადეგარი იქნება; ქართულ ტექსტს ხშირად ფონეტიკური გადაწერა ან ხელით ჩაწერა სჭირდება.

ქართული ბლოკი სამუშაო ვერსიაა — გენერატორში ჩასასმელად გამოიყენე `---` ხაზის შემდეგ მოცემული სტრიქონი.
პაუზა და აქცენტი ნიშნით მონიშნე და არა სიტყვებით აღწერე; ემოცია მდგომარეობით დაასახელე და არა შესრულების ბრძანებით.
AU-10 და AU-11 ჩვეულებრივი ინსტრუქციული პრომპტია ტექსტური მოდელისთვის — იქ ჩასასმელი სტრიქონი არ არის, EN და KA ბლოკები დამოუკიდებელია.
AU-10 and AU-11 are ordinary instruction prompts for a text model — plain EN / KA blocks, no paste string.

---

### AU-01 · Documentary narration, held back
`elevenlabs` — voice, narration

**EN**
```
Voice direction. Documentary narration, one speaker, no music underneath.
State: settled and unimpressed — someone who has stood in this place and is not selling it to you. Not warm, not cold.
Pace: 135 words per minute. Slow by a third across the final sentence.
Line ends fall. No upward inflection anywhere; this is not a presenter read.
Breath: audible intake before each paragraph, none inside a sentence.

Read the script exactly as punctuated. Em dashes are hard stops. Ellipses are half-beat hesitations, not trailing off. Break tags are silence.

"The wall went up in four months.<break time="0.8s" /> Four months — and it stood for six hundred years.
Nobody who laid a stone in it signed their name... none of them expected to be asked.<break time="0.6s" />
What you are looking at is the part they did not think was important."

Keep "six hundred" flat — no emphasis lift on the number. The weight is in the pause before it, not in the word.
```

**KA**
```
ხმის მიმართულება. დოკუმენტური ვოისოვერი, ერთი მთხრობელი, ქვეშ მუსიკის გარეშე.
მდგომარეობა: დამშვიდებული და აღუფრთოვანებელი — ადამიანი, რომელიც ამ ადგილას ნამდვილად იდგა და არაფერს გყიდის. არც თბილი, არც ცივი.
ტემპი: წუთში 135 სიტყვა. ბოლო წინადადებაზე ტემპი მესამედით შენელდეს.
ფრაზის ბოლო ქვევით ეშვება. ამაღლებული ინტონაცია არსად — ეს წამყვანის კითხვა არ არის.
სუნთქვა: ყოველი აბზაცის წინ ისმის ჩასუნთქვა, წინადადების შიგნით — არა.

ტექსტი ზუსტად პუნქტუაციის მიხედვით წაიკითხე. გრძელი ტირე — მკვეთრი გაჩერება. მრავალწერტილი — ნახევარი წამის ყოყმანი და არა ხმის ჩაკვდომა. break-ნიშანი — სიჩუმე.

„კედელი ოთხ თვეში ავიდა.<break time="0.8s" /> ოთხ თვეში — და ექვსასი წელი იდგა.
ვინც მასში ქვა ჩადო, არავის მოუწერია სახელი... არც ელოდა, რომ ოდესმე ჰკითხავდნენ.<break time="0.6s" />
ის, რასაც ახლა უყურებ, სწორედ ის ნაწილია, რომელიც მათთვის მნიშვნელოვანი არ ყოფილა.“

„ექვსასი“ თანაბრად წაიკითხე — ციფრზე აქცენტი არ ასწიო. სიმძიმე მის წინ პაუზაშია და არა თვითონ სიტყვაში.
---
Voice direction. Documentary narration, one speaker, no music underneath.
State: settled and unimpressed — someone who has stood in this place and is not selling it to you. Not warm, not cold.
Pace: 135 words per minute. Slow by a third across the final sentence.
Line ends fall. No upward inflection anywhere; this is not a presenter read.
Breath: audible intake before each paragraph, none inside a sentence.

Read the script exactly as punctuated. Em dashes are hard stops. Ellipses are half-beat hesitations, not trailing off. Break tags are silence.

"The wall went up in four months.<break time="0.8s" /> Four months — and it stood for six hundred years.
Nobody who laid a stone in it signed their name... none of them expected to be asked.<break time="0.6s" />
What you are looking at is the part they did not think was important."

Keep "six hundred" flat — no emphasis lift on the number. The weight is in the pause before it, not in the word.
```

---

### AU-02 · Radio ad read in Georgian, emphasis and pauses marked
`elevenlabs` — voice, advertising, georgian-output

**EN**
```
Voice direction. 20-second radio spot, single voice. THE SPOKEN OUTPUT IS GEORGIAN — use a voice trained on or cloned from Georgian speech; a multilingual English voice will read Georgian letter-by-letter.
State: someone telling a friend about something that actually worked, mid-conversation. Slight smile. Not "announcing".
Pace: brisk, around 160 words per minute, but stop dead on the two marked breaks.
Emphasis is marked with <emphasis> tags — do not add emphasis anywhere else. Do not lift the brand name.

Georgian markup rules that survive this text:
- Mark every pause with a break tag, not with an ellipsis. Georgian TTS voices frequently swallow an ellipsis or read it as part of the preceding word.
- Georgian has no capital letters, so emphasis cannot be signalled by case. Use the tag, or isolate the word between commas.
- Write every number as a word — "ოცდახუთი პროცენტი", never "25%". Digit reading in Georgian is the least reliable part of every provider.
- Respell Latin brand and product names in Georgian letters for the read, keeping the correct spelling in the on-screen copy.
- If a word comes back wrong, the error is almost always in an aspirated/ejective pair (ტ/თ, კ/ქ, პ/ფ, ც/წ, ჭ/ჩ). Respell that syllable phonetically and regenerate rather than re-recording the whole line.

Script:
"ორშაბათს გავხსენი.<break time="0.5s" /> ხუთშაბათს უკვე <emphasis>ყველაფერი</emphasis> გადატანილი მქონდა.
არაფერი დამიკარგავს, არავისთვის დამირეკავს.<break time="0.6s" />
<emphasis>ერთ</emphasis> საღამოში."
```

**KA**
```
ხმის მიმართულება. ოცწამიანი სარეკლამო რგოლი, ერთი ხმა. სათქმელი ქართულია — აიღე ქართულ მეტყველებაზე გაწვრთნილი ან კლონირებული ხმა; მრავალენოვანი ინგლისური ხმა ქართულს ასო-ასო წაიკითხავს.
მდგომარეობა: ადამიანი, რომელიც მეგობარს საუბრის შუაში უყვება იმაზე, რაც ნამდვილად გამოუვიდა. ოდნავ ღიმილით. „გამოცხადების“ ინტონაციის გარეშე.
ტემპი: ცოცხალი, წუთში დაახლოებით 160 სიტყვა, მაგრამ მონიშნულ პაუზაზე სრული გაჩერება.
აქცენტი მხოლოდ <emphasis>-ნიშნითაა მონიშნული — სხვაგან აქცენტი არ დასვა. ბრენდის სახელი არ გამოყო.

ქართულ ტექსტზე მომუშავე ნიშნები:
- პაუზა ყოველთვის break-ნიშნით მონიშნე და არა მრავალწერტილით: ქართული ხმები მრავალწერტილს ხშირად „ყლაპავენ“ ან წინა სიტყვას აწებებენ.
- ქართულს მთავრული ასო არ აქვს, ამიტომ აქცენტს რეგისტრით ვერ მიუთითებ. გამოიყენე ნიშანი ან სიტყვა ორ მძიმეს შორის გაიყვანე.
- ყველა რიცხვი სიტყვით დაწერე — „ოცდახუთი პროცენტი“ და არა „25%“. ციფრების წაკითხვა ყველა პროვაიდერთან ყველაზე არასაიმედო ადგილია.
- ლათინურად დაწერილი ბრენდი ჩასაწერ ტექსტში ქართული ასოებით გადაწერე, ხოლო ეკრანზე გამოსატან ტექსტში სწორი ორთოგრაფია დატოვე.
- თუ სიტყვა არასწორად წამოვიდა, შეცდომა თითქმის ყოველთვის მკვეთრი და ფშვინვიერი თანხმოვნების წყვილშია (ტ/თ, კ/ქ, პ/ფ, ც/წ, ჭ/ჩ). ეს მარცვალი ფონეტიკურად გადაწერე და ხელახლა დააგენერირე — მთელი ფრაზის თავიდან ჩაწერა საჭირო არ არის.

ტექსტი:
„ორშაბათს გავხსენი.<break time="0.5s" /> ხუთშაბათს უკვე <emphasis>ყველაფერი</emphasis> გადატანილი მქონდა.
არაფერი დამიკარგავს, არავისთვის დამირეკავს.<break time="0.6s" />
<emphasis>ერთ</emphasis> საღამოში.“
---
Voice direction. 20-second radio spot, single voice. THE SPOKEN OUTPUT IS GEORGIAN — use a voice trained on or cloned from Georgian speech; a multilingual English voice will read Georgian letter-by-letter.
State: someone telling a friend about something that actually worked, mid-conversation. Slight smile. Not "announcing".
Pace: brisk, around 160 words per minute, but stop dead on the two marked breaks.
Emphasis is marked with <emphasis> tags — do not add emphasis anywhere else. Do not lift the brand name.
Numbers are written out as words on purpose; read them as written. Do not re-read any Latin characters.

Script (Georgian, read exactly as written and punctuated):
„ორშაბათს გავხსენი.<break time="0.5s" /> ხუთშაბათს უკვე <emphasis>ყველაფერი</emphasis> გადატანილი მქონდა.
არაფერი დამიკარგავს, არავისთვის დამირეკავს.<break time="0.6s" />
<emphasis>ერთ</emphasis> საღამოში.“
```

---

### AU-03 · Audiobook — one character against the narrator
`elevenlabs` — voice, audiobook

**EN**
```
Voice direction. Audiobook, single reader performing both the narrator and one character. Two settings, generated separately and cut together.

NARRATOR baseline — state: neutral, attentive, slightly forward-leaning. Pace 150 wpm. Mid chest placement. No character colour at all.

CHARACTER — an innkeeper, seventies, who has told this story too many times:
State: bored patience with a flicker of pride he would deny.
Timbre: lower than the narrator by about a third, drier, more air in the tone.
Pace: 120 wpm, and he takes the pauses the narrator would not.
Distinguish him by placement, pace and breath only. NEVER by accent, and never by a comic voice.

Script — narrator lines plain, character speech inside the quotation marks.

He had asked the question before, and got the same answer.<break time="0.5s" />
"The room at the back is not for guests." A pause, longer than it needed to be. "It has not been for guests since my father."
Then, as if the subject had never come up: "You will want breakfast at seven."

The character's second line drops half a step in pitch from the first. The third returns to his ordinary voice — the door has closed.
```

**KA**
```
ხმის მიმართულება. აუდიოწიგნი, ერთი შემსრულებელი კითხულობს მთხრობელსაც და ერთ პერსონაჟსაც. ორი განსხვავებული პარამეტრი, ცალ-ცალკე დააგენერირე და მონტაჟში შეაერთე.

მთხრობლის საბაზისო ხმა — მდგომარეობა: ნეიტრალური, ყურადღებიანი, ოდნავ წინ გადახრილი. ტემპი: წუთში 150 სიტყვა. ხმა მკერდის შუა რეგისტრში. პერსონაჟის შეფერილობა სრულიად გამორიცხულია.

პერსონაჟი — სასტუმროს პატრონი, სამოცდაათს გადაცილებული, რომელსაც ეს ამბავი მეტისმეტად ბევრჯერ აქვს მოყოლილი:
მდგომარეობა: მოწყენილი მოთმინება და სადღაც სიღრმეში სიამაყე, რომელსაც თვითონვე უარყოფდა.
ტემბრი: მთხრობელზე დაახლოებით მესამედით დაბალი, უფრო მშრალი, ხმაში მეტი ჰაერით.
ტემპი: წუთში 120 სიტყვა, და პაუზას იქ იღებს, სადაც მთხრობელი არ აიღებდა.
გამოარჩიე მხოლოდ რეგისტრით, ტემპითა და სუნთქვით. აქცენტით — არასოდეს; კომიკური ხმით — არასოდეს.

ტექსტი — მთხრობლის ფრაზები სადად, პერსონაჟის ნათქვამი ბრჭყალებში.

ეს კითხვა უკვე დაესვა და იგივე პასუხი მიიღო.<break time="0.5s" />
„უკანა ოთახი სტუმრებისთვის არ არის.“ პაუზა, საჭიროზე გრძელი. „მამაჩემის შემდეგ სტუმრები იქ არ დაუყენებიათ.“
მერე ისე, თითქოს საუბარი არც ყოფილიყო: „საუზმე შვიდზე მოგინდებათ.“

პერსონაჟის მეორე ფრაზა პირველზე ნახევარი ტონით დაბლა ეშვება. მესამე მის ჩვეულ ხმას უბრუნდება — კარი დაიკეტა.
---
Voice direction. Audiobook, single reader performing both the narrator and one character. Two settings, generated separately and cut together.

NARRATOR baseline — state: neutral, attentive, slightly forward-leaning. Pace 150 wpm. Mid chest placement. No character colour at all.

CHARACTER — an innkeeper, seventies, who has told this story too many times:
State: bored patience with a flicker of pride he would deny.
Timbre: lower than the narrator by about a third, drier, more air in the tone.
Pace: 120 wpm, and he takes the pauses the narrator would not.
Distinguish him by placement, pace and breath only. NEVER by accent, and never by a comic voice.

Script — narrator lines plain, character speech inside the quotation marks.

He had asked the question before, and got the same answer.<break time="0.5s" />
"The room at the back is not for guests." A pause, longer than it needed to be. "It has not been for guests since my father."
Then, as if the subject had never come up: "You will want breakfast at seven."

The character's second line drops half a step in pitch from the first. The third returns to his ordinary voice — the door has closed.
```

---

### AU-04 · Conversational read that does not sound synthesised
`elevenlabs` — voice, conversational, georgian-output

**EN**
```
Voice direction. A short spoken explainer, one person talking to one person. THE SPOKEN OUTPUT IS GEORGIAN — use a Georgian-trained or cloned voice, and listen to the whole take before you ship it.
State: relaxed, mildly amused, thinking as they speak. They know this well enough not to perform it.
Pace: uneven on purpose — quicker through the familiar part, slower where they qualify themselves. Around 145 wpm on average.
Stability low: let the delivery drift between takes. A perfectly even read is the sound we are trying to avoid.

What makes a Georgian read sound synthetic, and what to do instead:
- Over-articulation. Written-register full forms make the voice hit every syllable. Write the spoken contraction: "კარგია", not "კარგი არის"; "ეგაა", not "ეს არის ის".
- Every sentence landing on a full stop. Leave two sentences unfinished with a comma and let the next clause pick them up.
- No fillers at all. Keep one — "მოკლედ" or "აბა" at the top of a clause — and no more; a second one reads as a mistake.
- Long clean clauses. Break one clause into a fragment and a repair: say a thing, then correct it.
- Mark pauses with break tags, never with ellipses; mark emphasis with tags, since Georgian has no capitals to lean on.

Script:
„მოკლედ,<break time="0.3s" /> პირველი კვირა ყველას გიჭირს. ეგაა.
მე მეგონა, რომ პროგრამა უნდა მესწავლა — არა, <emphasis>ხალხი</emphasis> უნდა გაიცნო ჯერ.<break time="0.5s" />
პროგრამა მერე თავისით მოდის.“
```

**KA**
```
ხმის მიმართულება. მოკლე სალაპარაკო ახსნა, ერთი ადამიანი ერთ ადამიანს ესაუბრება. სათქმელი ქართულია — აიღე ქართულზე გაწვრთნილი ან კლონირებული ხმა და მზა ვერსია ბოლომდე მოისმინე, სანამ გამოიყენებ.
მდგომარეობა: მოდუნებული, ოდნავ გართობილი, ლაპარაკის პროცესში ფიქრობს. საკმარისად კარგად იცის, რომ არ „ითამაშოს“.
ტემპი: განზრახ არათანაბარი — ნაცნობ ნაწილში აჩქარებული, თვითშესწორების ადგილას შენელებული. საშუალოდ წუთში 145 სიტყვა.
სტაბილურობა დაბალი: დუბლებს შორის კითხვა თავისუფლად „ცურავდეს“. სწორედ იდეალურად თანაბარი კითხვაა ის ხმა, რომელსაც გავურბივართ.

რა აჟღერებს ქართულ კითხვას სინთეზურად და რა ვქნათ ამის ნაცვლად:
- გადამეტებული არტიკულაცია. წიგნური სრული ფორმები ხმას ყოველ მარცვალზე ურტყამს. დაწერე სალაპარაკო ფორმა: „კარგია“ და არა „კარგი არის“; „ეგაა“ და არა „ეს არის ის“.
- ყოველი წინადადება წერტილზე რომ ეშვება. ორი წინადადება მძიმეზე დაასრულე და შემდეგმა ნაწილმა აიტაცოს.
- სიტყვა-შემავსებლის სრული არარსებობა. დატოვე ერთი — „მოკლედ“ ან „აბა“ ფრაზის დასაწყისში — და მეტი არა: მეორე უკვე შეცდომად ისმის.
- გრძელი, გაწმენდილი ფრაზები. ერთი ფრაზა დაამტვრიე: თქვი რაღაც და მერე თვითონვე შეასწორე.
- პაუზა break-ნიშნით მონიშნე და არა მრავალწერტილით; აქცენტი ნიშნით მონიშნე, რადგან ქართულს მთავრული ასო არ აქვს.

ტექსტი:
„მოკლედ,<break time="0.3s" /> პირველი კვირა ყველას გიჭირს. ეგაა.
მე მეგონა, რომ პროგრამა უნდა მესწავლა — არა, <emphasis>ხალხი</emphasis> უნდა გაიცნო ჯერ.<break time="0.5s" />
პროგრამა მერე თავისით მოდის.“
---
Voice direction. A short spoken explainer, one person talking to one person. The spoken output is Georgian — use a Georgian-trained or cloned voice.
State: relaxed, mildly amused, thinking as they speak. They know this well enough not to perform it.
Pace: uneven on purpose — quicker through the familiar part, slower where they qualify themselves. Around 145 wpm on average.
Stability low: let the delivery drift. A perfectly even read is the sound we are trying to avoid.
Read the contractions as written — do not expand them. Keep the one filler at the top. Break tags are silence; emphasis tags are the only stressed words.

Script (Georgian, read exactly as written):
„მოკლედ,<break time="0.3s" /> პირველი კვირა ყველას გიჭირს. ეგაა.
მე მეგონა, რომ პროგრამა უნდა მესწავლა — არა, <emphasis>ხალხი</emphasis> უნდა გაიცნო ჯერ.<break time="0.5s" />
პროგრამა მერე თავისით მოდის.“
```

---

### AU-05 · Loopable background bed for video
`suno` — music, instrumental, loop

**EN**
```
Loopable instrumental bed for video. Genre: minimal downtempo, close to library music. Instrumentation: Rhodes electric piano playing sustained two-note voicings, upright bass plucked softly on beats 1 and 3, brushed snare, one low sine pad underneath. 72 BPM, A minor, calm and unresolved. Structure: eight bars that repeat identically — no intro, no build, no resolution, and the last bar must run into the first without a seam. Instrumental, no vocals, no lead melody and no hook that pulls attention. Reference era: 1970s analogue tape warmth with faint hiss. Mix: everything sits under dialogue, no transient spikes, no cymbal crashes, nothing above 8 kHz. Length 30 seconds.
```

**KA**
```
ლუპისთვის ვარგისი ინსტრუმენტული ბექგრაუნდი ვიდეოსთვის. ჟანრი: მინიმალისტური დაუნტემპო, ბიბლიოთეკური მუსიკის ტიპის. ინსტრუმენტები: როუდზის ელექტროპიანინო გაწელილ ორბგერიან აკორდებში, კონტრაბასი რბილად, პირველსა და მესამე დარტყმაზე, ჯაგრისით დაკრული მცირე დასარტყამი, ქვემოთ ერთი დაბალი სინუსოიდური პედი. ტემპი 72 BPM, ტონალობა ლა მინორი, განწყობა მშვიდი და გადაუწყვეტელი. სტრუქტურა: რვა ტაქტი, რომელიც იდენტურად მეორდება — ინტრო, აღმავლობა და დასასრული არ არის; ბოლო ტაქტი პირველს ნაკერის გარეშე უნდა გადაებას. ინსტრუმენტული, ვოკალის გარეშე, წამყვანი მელოდიისა და ყურადღების მიმზიდველი ჰუკის გარეშე. ეპოქა: 70-იანების ანალოგური ფირის სითბო, ძლივს გასაგონი შიშინით. მიქსი: ყველაფერი დიალოგის ქვეშ დგება, მკვეთრი შეტევების, ტარელკის დარტყმებისა და 8 კჰც-ზე მაღალი სიხშირეების გარეშე. ხანგრძლივობა 30 წამი.
---
Loopable instrumental bed for video. Genre: minimal downtempo, close to library music. Instrumentation: Rhodes electric piano playing sustained two-note voicings, upright bass plucked softly on beats 1 and 3, brushed snare, one low sine pad underneath. 72 BPM, A minor, calm and unresolved. Structure: eight bars that repeat identically — no intro, no build, no resolution, and the last bar must run into the first without a seam. Instrumental, no vocals, no lead melody and no hook that pulls attention. Reference era: 1970s analogue tape warmth with faint hiss. Mix: everything sits under dialogue, no transient spikes, no cymbal crashes, nothing above 8 kHz. Length 30 seconds.
```

---

### AU-06 · Podcast intro sting
`suno` — music, podcast, sting

**EN**
```
Short intro sting for a documentary podcast. Genre: dry modern electronic, no orchestral swell. Instrumentation: muted low synth bass, a single marimba figure of four notes, one filtered white-noise sweep rising underneath, soft kick on beats 1 and 3, no snare. 100 BPM, D minor, curious rather than dramatic. Structure: two bars of the marimba figure alone, two bars with bass and kick joining, then one final accented hit with a half-second tail and nothing after it. Instrumental, no vocals. Reference era: contemporary, clean, close to a Scandinavian radio ident. Total length 8 seconds — the final hit must decay into clean silence so a voice can enter on top.
```

**KA**
```
მოკლე ინტროს სტინგი დოკუმენტური პოდკასტისთვის. ჟანრი: მშრალი თანამედროვე ელექტრონიკა, საორკესტრო აღმავლობის გარეშე. ინსტრუმენტები: დახშული დაბალი სინთეზატორული ბასი, მარიმბის ერთი ოთხბგერიანი ფიგურა, ქვემოდან ამომავალი გაფილტრული თეთრი ხმაურის სვიპი, რბილი ბოჭკა პირველსა და მესამე დარტყმაზე, მცირე დასარტყამის გარეშე. ტემპი 100 BPM, ტონალობა რე მინორი, განწყობა ცნობისმოყვარე და არა დრამატული. სტრუქტურა: ორი ტაქტი მხოლოდ მარიმბის ფიგურა, ორი ტაქტი ბასისა და ბოჭკის შემოსვლით, ბოლოს ერთი აქცენტირებული დარტყმა ნახევარწამიანი კუდით და მის შემდეგ არაფერი. ინსტრუმენტული, ვოკალის გარეშე. ეპოქა: თანამედროვე, სუფთა, სკანდინავიური რადიოს იდენტის მსგავსი. სრული ხანგრძლივობა 8 წამი — ბოლო დარტყმა სუფთა სიჩუმეში უნდა ჩაქრეს, რომ ზემოდან ხმა შემოვიდეს.
---
Short intro sting for a documentary podcast. Genre: dry modern electronic, no orchestral swell. Instrumentation: muted low synth bass, a single marimba figure of four notes, one filtered white-noise sweep rising underneath, soft kick on beats 1 and 3, no snare. 100 BPM, D minor, curious rather than dramatic. Structure: two bars of the marimba figure alone, two bars with bass and kick joining, then one final accented hit with a half-second tail and nothing after it. Instrumental, no vocals. Reference era: contemporary, clean, close to a Scandinavian radio ident. Total length 8 seconds — the final hit must decay into clean silence so a voice can enter on top.
```

---

### AU-07 · Full track in a named genre, with structure
`udio` — music, vocals, song

**EN**
```
Genre: 1990s trip-hop. Instrumentation: a dusty sampled break up front, deep sub bass, Wurlitzer electric piano chords, one muted trumpet line answering the vocal, vinyl crackle running throughout. 86 BPM, F minor, heavy and unhurried. Structure: intro 8 bars (drums and crackle only) – verse 16 – chorus 8 – verse 16 – chorus 8 – outro 8 with the drums dropping out and the Wurlitzer left alone. Vocals: one female voice, low in her range, close-miked, half-sung and half-spoken, sitting a fraction behind the beat; no backing harmonies except a doubled line on the last chorus. Reference era: Bristol, 1995. Mix: drums loud and compressed, bass round with no click, everything else dark and behind them. Length about 3 minutes.
```

**KA**
```
ჟანრი: 90-იანების ტრიპ-ჰოპი. ინსტრუმენტები: მტვრიანი სემპლირებული დასარტყამი წინა პლანზე, ღრმა საბ-ბასი, ვურლიცერის ელექტროპიანინოს აკორდები, დახშული საყვირის ერთი ფრაზა, რომელიც ვოკალს პასუხობს, და მთელ ტრეკზე გამავალი ვინილის ხრაშუნი. ტემპი 86 BPM, ტონალობა ფა მინორი, განწყობა მძიმე და აუჩქარებელი. სტრუქტურა: ინტრო 8 ტაქტი (მხოლოდ დასარტყამი და ხრაშუნი) – კუპლეტი 16 – სამღერალი 8 – კუპლეტი 16 – სამღერალი 8 – დასასრული 8 ტაქტი, სადაც დასარტყამი ქრება და ვურლიცერი მარტო რჩება. ვოკალი: ერთი ქალის ხმა, თავისი დიაპაზონის ქვედა ნაწილში, მიკროფონთან ახლოს, ნახევრად ნამღერი და ნახევრად ნათქვამი, რიტმს ოდნავ ჩამორჩენილი; მეორე ხმა მხოლოდ ბოლო სამღერალზე ერთვება. ეპოქა: ბრისტოლი, 1995 წელი. მიქსი: დასარტყამი ხმამაღალი და შეკუმშული, ბასი მრგვალი, კლიკის გარეშე, დანარჩენი ბნელი და მათ უკან. ხანგრძლივობა დაახლოებით 3 წუთი.
---
Genre: 1990s trip-hop. Instrumentation: a dusty sampled break up front, deep sub bass, Wurlitzer electric piano chords, one muted trumpet line answering the vocal, vinyl crackle running throughout. 86 BPM, F minor, heavy and unhurried. Structure: intro 8 bars (drums and crackle only) – verse 16 – chorus 8 – verse 16 – chorus 8 – outro 8 with the drums dropping out and the Wurlitzer left alone. Vocals: one female voice, low in her range, close-miked, half-sung and half-spoken, sitting a fraction behind the beat; no backing harmonies except a doubled line on the last chorus. Reference era: Bristol, 1995. Mix: drums loud and compressed, bass round with no click, everything else dark and behind them. Length about 3 minutes.
```

---

### AU-08 · Ambient texture with no melody
`udio` — music, ambient, texture

**EN**
```
Ambient texture. No melody, no chord progression, no beat of any kind. Sources: bowed double bass harmonics, a granular time-stretch of one struck piano note, and a distant field recording of wind moving against a metal surface. No BPM — nothing that implies a pulse, no rhythmic gating. Tonal centre C, held as a single drone with two layers detuned a few cents apart so they beat slowly against each other; the drone never resolves and never changes pitch. Structure: one continuous 90-second swell, rising for the first 60 seconds and falling for the last 30, with no sections and nothing that repeats on a recognisable cycle. Instrumental, no vocals. Long reverb tail, low-passed above 6 kHz, no stereo movement.
```

**KA**
```
ამბიენტური ფაქტურა. მელოდიის, ჰარმონიული მსვლელობისა და რაიმე სახის რიტმის გარეშე. წყაროები: კონტრაბასის ხემით აღებული ფლაჟოლეტები, ერთი დაკრული საფორტეპიანო ბგერის გრანულარულად გაწელილი ვერსია და შორეული ჩანაწერი ქარისა, რომელიც ლითონის ზედაპირს ეხახუნება. ტემპი არ არის — არაფერი, რაც პულსს მიანიშნებს; რიტმული გეითის გარეშე. ტონალური ცენტრი დო, შენარჩუნებული როგორც ერთი ბურდონი ორი ფენით, რომლებიც რამდენიმე ცენტით არის ერთმანეთისგან აცდენილი და ნელა „სცემენ“; ბურდონი არასოდეს წყდება და სიმაღლეს არ იცვლის. სტრუქტურა: ერთი უწყვეტი, 90-წამიანი აღმავლობა-დაღმავლობა — პირველი 60 წამი იზრდება, ბოლო 30 წამი ცხრება; ნაწილებად დაყოფის გარეშე, ისე, რომ არაფერი მეორდებოდეს ამოსაცნობი ციკლით. ინსტრუმენტული, ვოკალის გარეშე. გრძელი რევერბერაციის კუდი, 6 კჰც-ზე ზემოთ მოჭრილი, სტერეოში მოძრაობის გარეშე.
---
Ambient texture. No melody, no chord progression, no beat of any kind. Sources: bowed double bass harmonics, a granular time-stretch of one struck piano note, and a distant field recording of wind moving against a metal surface. No BPM — nothing that implies a pulse, no rhythmic gating. Tonal centre C, held as a single drone with two layers detuned a few cents apart so they beat slowly against each other; the drone never resolves and never changes pitch. Structure: one continuous 90-second swell, rising for the first 60 seconds and falling for the last 30, with no sections and nothing that repeats on a recognisable cycle. Instrumental, no vocals. Long reverb tail, low-passed above 6 kHz, no stereo movement.
```

---

### AU-09 · Three-part male harmony over a held drone
`suno` — music, vocals, polyphony

**EN**
```
A vocal piece built on three-part male harmony over a sustained bass drone. The lowest voice holds one pitch underneath an entire phrase and does not move with the others. The two upper voices move in close intervals — seconds, fourths and fifths — and are meant to rub against each other rather than settle into thirds; the dissonance is the sound, not an error to smooth out. Full chest voice throughout, no vibrato, no head voice except one short ornamented yodelled figure on the top line at the end of each phrase. Intonation slightly wide of equal temperament — do not auto-tune the intervals toward a piano. Free rhythm, roughly 60 BPM implied, no fixed metre and no percussion. Tonal centre D. Instrumentation: unaccompanied voices for the first 40 seconds, then a low bowed string drone doubles the bass voice underneath. Structure: bass voice alone 8 seconds – the two upper voices enter stacked above it – one full three-part phrase – the phrase repeated a tone higher – a final cadence in which all three voices converge onto a single unison. Vocals only, close-miked in a stone room with about 2 seconds of natural reverb. Length about 2 minutes.
```

**KA**
```
ვოკალური ნაწარმოები სამხმიან მამაკაცურ ჰარმონიაზე, გაწელილი ბასის ბურდონის ზემოთ. ყველაზე დაბალი ხმა მთელი ფრაზის განმავლობაში ერთ ბგერას იკავებს და დანარჩენებთან ერთად არ მოძრაობს. ორი ზედა ხმა ახლო ინტერვალებში მოძრაობს — სეკუნდა, კვარტა, კვინტა — და ერთმანეთს უნდა „ეხახუნებოდეს“, ტერციაში ჩაწოლის ნაცვლად; დისონანსი აქ ჟღერადობაა და არა გასასწორებელი შეცდომა. მთელ ნაწარმოებში მკერდის რეგისტრი, ვიბრატოს გარეშე; თავის რეგისტრი მხოლოდ ერთხელ — ზედა ხმის მოკლე, მოქცეული იოდლისებრი ფიგურა ყოველი ფრაზის ბოლოს. ინტონაცია თანაბარტემპერირებულ წყობაზე ოდნავ ფართო — ინტერვალები ფორტეპიანოს წყობისკენ ავტომატურად არ გაასწორო. რიტმი თავისუფალი, დაახლოებით 60 BPM იგულისხმება, ფიქსირებული მეტრისა და დასარტყამების გარეშე. ტონალური ცენტრი რე. შემადგენლობა: პირველი 40 წამი მხოლოდ ხმები, აკომპანიმენტის გარეშე; შემდეგ ბასის ხმას ქვემოდან ხემიანი საკრავის დაბალი ბურდონი ედუბლირება. სტრუქტურა: ბასის ხმა მარტო 8 წამი – ზემოდან შემოდის ორი ზედა ხმა – ერთი სრული სამხმიანი ფრაზა – იგივე ფრაზა ერთი ტონით მაღლა – დასკვნითი კადენცია, სადაც სამივე ხმა ერთ უნისონში იყრის თავს. მხოლოდ ვოკალი, მიკროფონთან ახლოს, ქვის ოთახის აკუსტიკაში, დაახლოებით 2 წამიანი ბუნებრივი რევერბერაციით. ხანგრძლივობა დაახლოებით 2 წუთი.
---
A vocal piece built on three-part male harmony over a sustained bass drone. The lowest voice holds one pitch underneath an entire phrase and does not move with the others. The two upper voices move in close intervals — seconds, fourths and fifths — and are meant to rub against each other rather than settle into thirds; the dissonance is the sound, not an error to smooth out. Full chest voice throughout, no vibrato, no head voice except one short ornamented yodelled figure on the top line at the end of each phrase. Intonation slightly wide of equal temperament — do not auto-tune the intervals toward a piano. Free rhythm, roughly 60 BPM implied, no fixed metre and no percussion. Tonal centre D. Instrumentation: unaccompanied voices for the first 40 seconds, then a low bowed string drone doubles the bass voice underneath. Structure: bass voice alone 8 seconds – the two upper voices enter stacked above it – one full three-part phrase – the phrase repeated a tone higher – a final cadence in which all three voices converge onto a single unison. Vocals only, close-miked in a stone room with about 2 seconds of natural reverb. Length about 2 minutes.
```

---

### AU-10 · Script into a timed, marked-up VO script
`claude` `gpt` — production, voiceover

*Plain instruction prompt — no paste string.*

**EN**
```
<context>
A draft script needs to be turned into a recording script for a single voice actor or a TTS voice.
The reader needs timing, breath and stress marked on the page — not described.
</context>

<script>
{{draft_script}}
</script>

<target_duration>{{seconds}}</target_duration>
<language>{{language}}</language>

<task>
Rewrite the script as a timed VO script with delivery markup.
</task>

<rules>
- Calculate at 150 words per minute for English, 140 for Georgian. Cut or expand the copy to hit the target duration within 5 percent, and say in one line what you cut.
- MUST mark every pause with an explicit tag: <break time="0.3s" />, 0.5s, or 0.8s. NEVER write "pause here" in prose.
- MUST mark stressed words with <emphasis>…</emphasis>. At most one stressed word per sentence; a script with stress everywhere has none.
- MUST break the script into numbered beats of no more than 25 words, each with its own running timecode (00:00, 00:06, …).
- For each beat, give ONE state line naming the speaker's emotional state and pace — a state, not a performance instruction. "resigned, slowing" is right; "read this sadly" is wrong.
- If the language is Georgian: write every number as a word, respell Latin brand names in Georgian letters for the read only, and NEVER use ellipses as pause marks — TTS voices swallow them. Flag any word whose aspirated/ejective consonants (ტ/თ, კ/ქ, პ/ფ, ც/წ, ჭ/ჩ) are likely to be mispronounced, and give a phonetic respelling beside it.
- NEVER change a factual claim, a name or a number in the source script.
</rules>

<output_format>
A table: beat number | timecode | marked-up line | state and pace.
Then: total word count, calculated runtime, and the one-line note on what was cut or added.
Then: a list of words flagged for pronunciation, each with its respelling, or "none".
</output_format>
```

**KA**
```
<კონტექსტი>
სცენარის მონახაზი უნდა გადაიქცეს ჩასაწერ ტექსტად ერთი დიქტორისთვის ან TTS-ხმისთვის.
მკითხველს ფურცელზე სჭირდება დროის, სუნთქვისა და აქცენტის ნიშნები — და არა მათი სიტყვიერი აღწერა.
</კონტექსტი>

<სცენარი>
{{სცენარის_მონახაზი}}
</სცენარი>

<სამიზნე_ხანგრძლივობა>{{წამი}}</სამიზნე_ხანგრძლივობა>
<ენა>{{ენა}}</ენა>

<დავალება>
გადაწერე სცენარი როგორც დროში გათვლილი ვოისოვერის ტექსტი, შესრულების ნიშნებით.
</დავალება>

<წესები>
- გათვალე წუთში 150 სიტყვა ინგლისურისთვის და 140 ქართულისთვის. ტექსტი ისე შეკვეცე ან გააფართოვე, რომ სამიზნე ხანგრძლივობას 5 პროცენტის ფარგლებში მოერგოს, და ერთ ხაზში დაწერე, რა ამოიღე.
- ყოველი პაუზა ცალკე ნიშნით მონიშნე: <break time="0.3s" />, 0.5s ან 0.8s. ტექსტში სიტყვები „აქ პაუზა“ არ დაწერო.
- აქცენტირებული სიტყვა მონიშნე <emphasis>…</emphasis> ნიშნით. წინადადებაზე მაქსიმუმ ერთი სიტყვა; თუ ყველგან აქცენტია, აქცენტი აღარსად არის.
- სცენარი დაყავი დანომრილ ბლოკებად, თითოეული მაქსიმუმ 25 სიტყვა, და თითოეულს დაურთე მზარდი ტაიმკოდი (00:00, 00:06, …).
- ყოველ ბლოკს დაამატე ერთი ხაზი მოსაუბრის ემოციური მდგომარეობითა და ტემპით — სწორედ მდგომარეობა და არა შესრულების ბრძანება. „შეგუებული, ნელდება“ — სწორია; „წაიკითხე სევდიანად“ — არასწორი.
- თუ ენა ქართულია: ყველა რიცხვი სიტყვით დაწერე, ლათინურად დაწერილი ბრენდი მხოლოდ ჩასაწერ ტექსტში ქართული ასოებით გადაწერე და პაუზის ნიშნად მრავალწერტილი არასოდეს გამოიყენო — TTS-ხმები მას ყლაპავენ. ცალკე გამოყავი სიტყვები, სადაც მკვეთრი და ფშვინვიერი თანხმოვნების წყვილი (ტ/თ, კ/ქ, პ/ფ, ც/წ, ჭ/ჩ) არასწორად წაკითხვის რისკს ქმნის, და გვერდით ფონეტიკური ჩაწერა მიუწერე.
- საწყის ტექსტში ფაქტი, სახელი ან ციფრი არ შეცვალო.
</წესები>

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

<გამოსავალი>
ცხრილი: ბლოკის ნომერი | ტაიმკოდი | მონიშნული ტექსტი | მდგომარეობა და ტემპი.
შემდეგ: სიტყვების საერთო რაოდენობა, გათვლილი ხანგრძლივობა და ერთხაზიანი შენიშვნა იმის შესახებ, რა ამოიღე ან დაამატე.
ბოლოს: გამოთქმის რისკის მქონე სიტყვების სია ფონეტიკური ჩაწერით, ან „ასეთი სიტყვა არ არის“.
</გამოსავალი>
```

---

### AU-11 · Podcast episode outline with segment durations
`claude` `gpt` — production, podcast

*Plain instruction prompt — no paste string.*

**EN**
```
<context>
Podcast: {{show_name}}, {{format}} (interview / two-host / solo narrative).
Audience: {{audience}}. Episode topic: {{topic}}. Guest, if any: {{guest_and_credentials}}.
Total runtime: {{minutes}} minutes.
</context>

<task>
Write the episode outline as a running order with a duration on every segment.
</task>

<rules>
- Segment durations MUST add up to the total runtime. Show the arithmetic at the end.
- The cold open is 30–45 seconds and MUST be a specific moment or claim from later in the episode, never a description of what the episode is about.
- Every segment gets: a title, a duration, the one thing the listener should take from it, and the exact line that hands over to the next segment.
- For an interview: no more than six questions in the main body. Each one is a single sentence and open — NEVER a question answerable with yes or no, never two questions stacked into one.
- Mark two points in the outline where the episode could be cut for time, and say what is lost at each.
- Name the ad or sponsor slots by position and duration if {{ad_breaks}} is not "none", and place them at a natural break, not mid-argument.
- NEVER write filler segments ("intro chat", "general discussion"). If a segment has no specific purpose, delete it and give its minutes to a segment that does.
</rules>

<output_format>
Running order table: segment | duration | running total | purpose | handover line.
Then the cold open, written out in full.
Then the two cut points with what each one costs.
</output_format>
```

**KA**
```
<კონტექსტი>
პოდკასტი: {{გადაცემის_სახელი}}, ფორმატი: {{ფორმატი}} (ინტერვიუ / ორი წამყვანი / სოლო თხრობა).
აუდიტორია: {{აუდიტორია}}. ეპიზოდის თემა: {{თემა}}. სტუმარი, თუ არის: {{სტუმარი_და_გამოცდილება}}.
სრული ხანგრძლივობა: {{წუთი}} წუთი.
</კონტექსტი>

<დავალება>
დაწერე ეპიზოდის გეგმა როგორც მსვლელობის რიგი, სადაც ყოველ სეგმენტს თავისი ხანგრძლივობა აქვს.
</დავალება>

<წესები>
- სეგმენტების ხანგრძლივობის ჯამი ზუსტად უნდა ემთხვეოდეს სრულ ხანგრძლივობას. ბოლოში აჩვენე გამოთვლა.
- გახსნითი ნაწილი 30–45 წამია და აუცილებლად ეპიზოდის მოგვიანებითი კონკრეტული მომენტი ან ნათქვამი უნდა იყოს და არა იმის აღწერა, რაზეც ეპიზოდია.
- ყოველ სეგმენტს ახლავს: სათაური, ხანგრძლივობა, ერთი აზრი, რომელიც მსმენელს უნდა დარჩეს, და ზუსტი ფრაზა, რომლითაც შემდეგ სეგმენტზე გადადიხარ.
- ინტერვიუსთვის: ძირითად ნაწილში მაქსიმუმ 6 კითხვა. თითოეული ერთი წინადადებაა და ღიაა — კითხვა, რომელსაც „კი“ ან „არა“ პასუხობს, აკრძალულია; ორი კითხვა ერთში ჩაწყობილი — ასევე.
- მონიშნე ორი ადგილი, სადაც ეპიზოდი დროის გამო შეიძლება შემოკლდეს, და თითოეულზე დაწერე, რა იკარგება.
- თუ {{სარეკლამო_ბლოკები}} არ არის „არცერთი“, დაასახელე სარეკლამო ბლოკის ადგილი და ხანგრძლივობა და ჩასვი ბუნებრივ გადასვლაზე და არა მსჯელობის შუაში.
- შემავსებელი სეგმენტი („შესავალი საუბარი“, „ზოგადი მსჯელობა“) არ დაწერო. თუ სეგმენტს კონკრეტული დანიშნულება არ აქვს, წაშალე და მისი წუთები იმ სეგმენტს მიეცი, რომელსაც აქვს.
</წესები>

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
რეგისტრი: სასაუბრო.

<გამოსავალი>
მსვლელობის ცხრილი: სეგმენტი | ხანგრძლივობა | დაგროვილი დრო | დანიშნულება | გადასვლის ფრაზა.
შემდეგ სრულად დაწერილი გახსნითი ნაწილი.
ბოლოს ორი შესამოკლებელი ადგილი და თითოეულის ფასი.
</გამოსავალი>
```
