# Shot language / კადრის ენა

Video models respond to production vocabulary, not to adjectives. `medium close-up`, `slow push-in`,
`single hard key from camera left` change the output; `dramatic`, `cinematic`, `beautiful` do not.
Every term below is the exact English string a model recognises, next to the Georgian word a crew
actually says on set, next to what it does. Write the shot in Georgian if that is how you think —
then paste the English.

ვიდეომოდელი რეაგირებს საწარმოო ტერმინოლოგიაზე და არა ზედსართავებზე. `medium close-up`,
`slow push-in`, `single hard key from camera left` შედეგს ცვლის; „დრამატული“, „კინემატოგრაფიული“,
„ლამაზი“ — არაფერს ცვლის. ქვემოთ თითოეული ტერმინი სამ ნაწილადაა: ზუსტი ინგლისური სტრიქონი,
რომელსაც მოდელი ცნობს; ქართული სიტყვა, რომელსაც გადასაღებ მოედანზე ნამდვილად ამბობენ; და ის,
რასაც ეს ტერმინი აკეთებს. კადრი ქართულად აწყვე — მოდელს კი ინგლისური სტრიქონი ჩააწოდე.

Shot structure follows [`../../references/frameworks.md`](../../references/frameworks.md) §8 Shot spec:
`[shot size]. [subject + one action]. Camera: … Lighting: … Mood: … Audio: … Duration: …`
Per-tool differences are in [`../../references/tool-routing.md`](../../references/tool-routing.md) §Video.

---

## 1. Shot size / პლანის სიდიდე

| English term | ქართული ტერმინი | What it shows · რას აჩვენებს | When to use it · როდის |
|---|---|---|---|
| `extreme wide shot` | `შორი პლანი` | Figure tiny inside the landscape; the place is the subject · ფიგურა პატარაა გარემოში — სუბიექტი ადგილია და არა ადამიანი | Opening a location, showing scale · ლოკაციის გახსნა, მასშტაბის ჩვენება |
| `wide shot` · `establishing shot` | `ზოგადი პლანი` · `დამდგენი კადრი` | Whole figure and the space around it · მთელი ფიგურა და სივრცე მის გარშემო | Geography first — who is where, before you go closer · ჯერ გეოგრაფია: ვინ სად არის, სანამ მიუახლოვდები |
| `full shot` | `სრული პლანი` | Head to feet, frame close to the body · თავიდან ფეხებამდე, კადრი სხეულს მიჰყვება | Body language, costume, dance, a fight · სხეულის ენა, კოსტიუმი, ცეკვა, ჩხუბი |
| `medium wide shot` · `cowboy shot` | `ამერიკული პლანი` | Cut mid-thigh; the figure plus a little room · კადრი ბარძაყის შუაზე იჭრება — ფიგურა და ცოტა სივრცე | Two people standing, a gesture that needs the hands · ორი მდგომი ადამიანი, ჟესტი, რომელსაც ხელები სჭირდება |
| `medium shot` | `საშუალო პლანი` | Waist up · წელზევით | Dialogue that is not yet intimate · დიალოგი, რომელიც ჯერ ინტიმური არ არის |
| `medium close-up` | `ახლო პლანი` | Chest to the top of the head · მკერდიდან თავის ზემოთა კიდემდე | The default interview and dialogue size · ინტერვიუსა და დიალოგის ნაგულისხმევი სიდიდე |
| `close-up` | `მსხვილი პლანი` | The face fills the frame, shoulders barely present · სახე ავსებს კადრს, მხრები ძლივს ჩანს | A reaction the viewer must read, not guess · რეაქცია, რომელიც მაყურებელმა უნდა წაიკითხოს და არა გამოიცნოს |
| `extreme close-up` | `დეტალი` · `ზემსხვილი პლანი` | One feature or object only — eyes, hands, a key · მხოლოდ ერთი დეტალი — თვალები, ხელები, გასაღები | Emphasis, or an object that carries the plot · აქცენტი ან საგანი, რომელიც სიუჟეტს ატარებს |
| `over-the-shoulder` | `მხრიდან გადაღებული პლანი` · `ოვერშოლდერი` | One person's shoulder in the near foreground, the other in focus · ერთის მხარი წინა პლანზე, მეორე ფოკუსში | Dialogue — it holds both people in one geography · დიალოგი — ორივეს ერთ გეოგრაფიაში ინარჩუნებს |
| `two-shot` | `ორმაგი პლანი` | Two figures in one frame, no cut between them · ორი ფიგურა ერთ კადრში, მონტაჟური ჭრის გარეშე | A relationship shown by the distance between bodies · ურთიერთობა, რომელსაც სხეულებს შორის მანძილი აჩვენებს |
| `POV shot` | `სუბიექტური კადრი` | What the character sees, from where their eyes are · ის, რასაც პერსონაჟი ხედავს, მისი თვალის სიმაღლიდან | Only when the previous shot established whose eyes · მხოლოდ მაშინ, როცა წინა კადრმა აჩვენა, ვისი თვალებია |
| `insert shot` | `ინსერტი` · `ჩანართი კადრი` | A detail cut in from outside the main action · დეტალი, რომელიც ძირითადი მოქმედების გარედან ერთვება | A phone screen, a label, a wound — what the wide cannot hold · ტელეფონის ეკრანი, წარწერა, ჭრილობა — რაც ზოგად პლანში არ ჩანს |

Name the size in the first three words of the prompt. Leave it unstated and every tool defaults to wide.

პლანის სიდიდე პრომპტის პირველივე სამ სიტყვაში დაასახელე. თუ არ დაასახელებ, ყველა ინსტრუმენტი
ზოგად პლანს აირჩევს.

---

## 2. Camera movement / კამერის მოძრაობა

A movement without a speed and an extent is a suggestion, not an instruction. Always write both:
how fast, and how far.

მოძრაობა სიჩქარისა და მოცულობის გარეშე მინიშნებაა და არა მითითება. ორივე დაწერე: რამდენად სწრაფად
და რამდენად შორს.

| English term | ქართული ტერმინი | What it does · რას აკეთებს | Prompt phrasing · ფორმულირება პრომპტში |
|---|---|---|---|
| `static` · `locked off` | `სტატიკური კადრი` · `ჩამაგრებული კამერა` | No movement at all; the frame becomes a fixed window · მოძრაობა საერთოდ არ არის — კადრი ფიქსირებულ ფანჯრად იქცევა | `Camera: static, locked off on a tripod.` |
| `pan` | `პანორამა` (ჰორიზონტალური) | Turns on its axis left or right; it does not travel · თავის ღერძზე ბრუნავს მარჯვნივ ან მარცხნივ და ადგილს არ იცვლის | `Camera: slow pan left to right, 45° over the shot.` |
| `tilt` | `ვერტიკალური პანორამა` · `ტილტი` | Same axis turn, up or down · იგივე ღერძული მოძრაობა, ზემოთ ან ქვემოთ | `Camera: slow tilt up from the hands to the face.` |
| `push in` · `dolly in` | `დოლით შეტანა` · `მიახლოება` | Travels toward the subject; the background shifts with it · ფიზიკურად უახლოვდება სუბიექტს და ფონიც იცვლება | `Camera: slow push-in, 10% over the shot.` |
| `pull out` · `dolly out` | `დოლით გამოტანა` · `დაშორება` | Travels back; context enters the frame · უკან იწევს და კადრში კონტექსტი შემოდის | `Camera: steady pull-out from medium to wide over 6 seconds.` |
| `tracking` · `following shot` | `ტრეკინგი` · `თანმდევი მოძრაობა` | Moves alongside a moving subject, holding its size · მოძრავ სუბიექტს გვერდით მისდევს და მის ზომას ინარჩუნებს | `Camera: tracking left alongside her at walking pace, subject held at the same size.` |
| `crane` · `jib` | `კრანი` · `ჯიბი` | Vertical travel of the whole camera; the horizon moves through the frame · მთელი კამერა ვერტიკალურად მოძრაობს, ჰორიზონტი კადრში გადაადგილდება | `Camera: slow crane up, 3 metres over the shot, revealing the roofline.` |
| `orbit` · `arc` | `ორბიტა` · `შემოვლა` | Circles the subject at a constant distance · მუდმივ მანძილზე უვლის სუბიექტს გარშემო | `Camera: slow 90° orbit to the left around the table, constant distance.` |
| `handheld` | `ხელის კამერა` | Constant small instability; the operator becomes a presence · მუდმივი მცირე რხევა — ოპერატორი თავად ხდება თანდასწრება | `Camera: handheld, small constant drift, no whip.` |
| `steadicam` | `სტედიკამი` | Moves like a tracking shot but floats; no rails · ტრეკინგივით მოძრაობს, ოღონდ ცურავს, რელსების გარეშე | `Camera: steadicam following two steps behind, smooth, at walking pace.` |
| `whip pan` | `სწრაფი (მკვეთრი) პანორამა` | A pan fast enough to blur; often a hidden cut · იმდენად სწრაფი პანორამა, რომ კადრი იბინდება; ხშირად ფარულ ჭრად გამოიყენება | `Camera: whip pan right, 6 frames, motion blur through the turn.` |
| `zoom` | `ზუმი` · `ტრანსფოკატორი` | Focal length changes, the camera stays put · იცვლება ფოკუსური მანძილი, კამერა ადგილზე რჩება | `Camera: slow zoom in, focal length only, the camera does not move.` |
| `rack focus` · `focus pull` | `ფოკუსის გადატანა` | Focus moves between two planes — a reveal without a cut · ფოკუსი ერთი პლანიდან მეორეზე გადადის — გახსნა მონტაჟური ჭრის გარეშე | `Camera: rack focus from the foreground glass to the face behind it, over 1 second.` |

**Zoom is not a dolly.** A dolly moves the camera, so the relationship between near and far objects
changes and the shot reads as *approaching*. A zoom only changes focal length from a fixed position,
so the perspective is frozen and the shot reads as *flattening*. Models confuse the two constantly —
if you want the dolly, write `push-in, the camera physically moves`; if you want the zoom, write
`zoom, focal length only, the camera does not move`.

**ზუმი დოლი არ არის.** დოლის დროს კამერა გადაადგილდება, ახლო და შორეულ საგნებს შორის დამოკიდებულება
იცვლება და კადრი *მიახლოებად* იკითხება. ზუმისას მხოლოდ ფოკუსური მანძილი იცვლება ერთი ადგილიდან,
პერსპექტივა გაყინულია და კადრი *გაბრტყელებად* იკითხება. მოდელები ამ ორს მუდმივად ურევენ ერთმანეთში —
თუ დოლი გინდა, დაწერე `push-in, the camera physically moves`; თუ ზუმი გინდა — `zoom, focal length
only, the camera does not move`.

Every tool adds an orbit or a slow push when the camera line is missing. If you want no movement,
say `Camera: static, locked off` — silence is not the same instruction.

ყველა ინსტრუმენტი თავისით ამატებს შემოვლას ან ნელ მიახლოებას, როცა კამერის ხაზი გამოტოვებულია.
თუ მოძრაობა არ გინდა, დაწერე `Camera: static, locked off` — დუმილი იგივე მითითება არ არის.

---

## 3. Lighting / განათება

Name the **source** and the **direction relative to camera**. `soft light` is a texture, not an
instruction. `soft light from a large window at camera left` is an instruction.

დაასახელე **წყარო** და **მიმართულება კამერასთან მიმართებით**. „რბილი შუქი“ ფაქტურაა და არა მითითება;
„რბილი შუქი დიდი ფანჯრიდან, კამერიდან მარცხნივ“ — მითითებაა.

| English term | ქართული ტერმინი | What it does · რას აკეთებს | Prompt phrasing · ფორმულირება |
|---|---|---|---|
| `key light` | `ძირითადი შუქი` | The main source; it decides where the shadows fall · მთავარი წყარო — ის წყვეტს, სად დაეცემა ჩრდილი | `single key from a window at camera left, 45° off axis` |
| `fill light` | `შემავსებელი შუქი` | Lifts the shadow side; how much fill sets how gentle the image is · ჩრდილიან მხარეს ანათებს — რამდენსაც შეავსებ, იმდენად რბილია კადრი | `weak fill from camera right, two stops under the key` · `no fill` |
| `back light` · `rim light` | `კონტრაჟური` · `კონტურული შუქი` | Separates subject from background with a line of light · სუბიექტს ფონისგან შუქის ზოლით გამოყოფს | `hard back light behind her head, rimming hair and shoulder` |
| `hard light` | `ხისტი (მკვეთრი) შუქი` | Small source: sharp-edged shadows, visible texture · მცირე წყარო — მკვეთრკიდიანი ჩრდილები, ხილული ფაქტურა | `hard midday sun from frame right, sharp-edged shadows` |
| `soft light` | `რბილი შუქი` | Large source: the shadow edge dissolves · დიდი წყარო — ჩრდილის კიდე იშლება | `soft light from a large window frame left, shadow edges dissolving` |
| `high key` | `ღია ტონალობის განათება` | Bright overall, low contrast, almost no black · საერთოდ ღია კადრი, დაბალი კონტრასტი, შავი თითქმის არ არის | `high key, even light, no black anywhere in the frame` |
| `low key` | `მუქი ტონალობის განათება` | Most of the frame in shadow, small lit areas · კადრის უმეტესობა ჩრდილშია, განათებული ადგილები მცირეა | `low key, one source, background falling to black` |
| `practical light` | `პრაქტიკული შუქი` | A lamp, screen or fire visible in frame that is also lighting the shot · ნათურა, ეკრანი ან ცეცხლი, რომელიც კადრში ჩანს და თან ანათებს | `a single bare bulb hanging in frame is the only source` |
| `motivated light` | `მოტივირებული შუქი` | Off-screen light the scene explains — a window, an open door · კადრს გარეთ დარჩენილი შუქი, რომელსაც სცენა ხსნის — ფანჯარა, ღია კარი | `light spilling from an open doorway off frame left` |
| `golden hour` | `ოქროს საათი` | Low warm sun, long shadows; about an hour after sunrise or before sunset · დაბალი თბილი მზე, გრძელი ჩრდილები — მზის ამოსვლიდან ან ჩასვლამდე დაახლოებით 1 საათი | `golden hour, low sun from frame right, long shadows across the floor` |
| `blue hour` | `ლურჯი საათი` | After sunset: even cold ambient, no sun direction · მზის ჩასვლის შემდეგ — თანაბარი ცივი შუქი, მზის მიმართულების გარეშე | `blue hour, cold even ambient, practicals already on` |
| `overcast` · `diffuse` | `ღრუბლიანი, გაბნეული შუქი` | The sky becomes one big soft source; nothing casts a shadow · ცა ერთ დიდ რბილ წყაროდ იქცევა, ჩრდილი არაფერს ეცემა | `flat overcast daylight, soft, no cast shadows` |
| `backlit` · `contre-jour` | `კონტრაჟურში გადაღებული` | The source is behind the subject: silhouette or halo · წყარო სუბიექტის უკანაა — გამოდის სილუეტი ან შარავანდი | `backlit against the window, the face two stops under` |
| `chiaroscuro` | `კიაროსკურო` (მკვეთრი შუქ-ჩრდილი) | One hard source, no fill, a hard division of light and dark · ერთი ხისტი წყარო, შემავსებლის გარეშე, შუქისა და სიბნელის მკვეთრი გაყოფა | `single hard source from camera left, no fill, half the face in darkness` |
| `top light` | `ზედა შუქი` | Source directly overhead; the eye sockets go dark · წყარო პირდაპირ ზემოთ — თვალის ფოსოები ბნელდება | `hard light from directly above, eye sockets in shadow` |
| `bounce` | `არეკლილი შუქი` · `ბაუნსი` | Light thrown off a surface; softens and redirects · ზედაპირიდან არეკლილი შუქი — არბილებს და მიმართულებას უცვლის | `sun bounced off a white wall at camera right, soft, low contrast` |

Directions are always written from the camera's point of view, not the subject's: `camera left`
means the left of your frame. `frame left`, `frame right`, `off frame left` all work.

მიმართულებას ყოველთვის კამერის და არა პერსონაჟის თვალით წერ: `camera left` შენი კადრის მარცხენა
მხარეა. მუშაობს აგრეთვე `frame left`, `frame right`, `off frame left`.

---

## 4. Lens and depth / ობიექტივი და სიღრმე

| English term | ქართული ტერმინი | What it does · რას აკეთებს | Prompt phrasing · ფორმულირება |
|---|---|---|---|
| `wide-angle lens, 14–35mm` | `ფართოკუთხოვანი ობიექტივი` | Exaggerates distance: near objects grow, the space feels bigger · მანძილს აზვიადებს — ახლო საგნები დიდდება, სივრცე ფართოვდება | `shot on a 24mm wide lens, foreground exaggerated` |
| `normal lens, 40–58mm` | `ნორმალური ობიექტივი` | Closest to how the eye reads distance; neutral · ყველაზე ახლოსაა იმასთან, როგორც თვალი აღიქვამს მანძილს — ნეიტრალურია | `shot on a 50mm lens, neutral perspective` |
| `telephoto lens, 85–300mm` | `გრძელფოკუსიანი (ტელე) ობიექტივი` | Flattens depth, isolates the subject against a compressed background · სიღრმეს აბრტყელებს და სუბიექტს შეკუმშული ფონისგან გამოყოფს | `shot on a 135mm telephoto, background compressed` |
| `shallow depth of field` | `მცირე სიღრმის ველი` | Only one plane is sharp; attention is forced · ფოკუსში მხოლოდ ერთი პლანია — ყურადღება იძულებითია | `shallow depth of field, only the eyes sharp` |
| `deep depth of field` | `დიდი სიღრმის ველი` | Foreground and background both sharp; the viewer chooses · წინა და უკანა პლანი ერთდროულად ფოკუსშია — მაყურებელი თავად ირჩევს | `deep focus, foreground and background both sharp` |
| `aperture, f/1.4 – f/16` | `დიაფრაგმა` | The number that sets depth of field; a small number means a narrow field · რიცხვი, რომელიც სიღრმის ველს განსაზღვრავს — მცირე რიცხვი ვიწრო ველს ნიშნავს | `f/1.8` to isolate · `f/8` when everything must read |
| `compression` | `პერსპექტივის შეკუმშვა` | A long lens stacks distant planes onto each other · გრძელფოკუსიანი ობიექტივი შორეულ პლანებს ერთმანეთზე აწყობს | `200mm, the crowd stacked flat behind him` |
| `macro` | `მაკრო` | Extreme close focus on a small object, very shallow field · ძალიან ახლო ფოკუსი მცირე საგანზე, უკიდურესად ვიწრო ველი | `macro, 100mm, condensation on the glass filling the frame` |
| `anamorphic` | `ანამორფული ობიექტივი` | Wide ratio, oval bokeh, horizontal flares · განიერი თანაფარდობა, ოვალური ბოკე, ჰორიზონტალური ბლიკები | `anamorphic, 2.39:1, oval bokeh, horizontal flare` |

Millimetres are the cheapest instruction in a video prompt: `24mm` and `135mm` produce visibly
different shots of the same subject, while `wide-angle look` produces neither reliably.

მილიმეტრი ვიდეოპრომპტში ყველაზე იაფი მითითებაა: `24mm` და `135mm` ერთსა და იმავე სუბიექტზე თვალსაჩინოდ
სხვადასხვა კადრს გამოიღებს, `wide-angle look` კი — არც ერთს საიმედოდ.

---

## 5. Words that do nothing / სიტყვები, რომლებიც არაფერს აკეთებს

| Does nothing · არაფერს აკეთებს | Write this instead · ამის ნაცვლად დაწერე |
|---|---|
| `cinematic` · „კინემატოგრაფიული“ | Name the lens, the aspect ratio and the light · დაასახელე ობიექტივი, კადრის თანაფარდობა და შუქი: `35mm, 2.39:1, single soft key from a window frame left` |
| `dramatic lighting` · „დრამატული განათება“ | `single hard key from camera left, no fill, background falling to black` · ერთი ხისტი შუქი კამერიდან მარცხნივ, შემავსებლის გარეშე, ფონი შავში გადადის |
| `beautiful` · `stunning` · `gorgeous` — „ლამაზი“, „თვალწარმტაცი“ | Delete. It describes your reaction, not the shot · წაშალე. ეს შენს შთაბეჭდილებას აღწერს და არა კადრს |
| `high quality` · `4K` · `8K` · `masterpiece` · `award-winning` — „მაღალი ხარისხის“, „4K“, „შედევრი“ | Delete. Resolution is a setting in the tool, not a word in the prompt · წაშალე. გარჩევადობას ინსტრუმენტის პარამეტრი განსაზღვრავს და არა პრომპტის სიტყვა |
| `epic` · „ეპიკური“ | Name the shot size and the thing that gives scale · დაასახელე პლანის სიდიდე და ის, რაც მასშტაბს აჩენს: `extreme wide, the walker one thirtieth of the frame height against the ridge` |
| `dynamic camera` · „დინამიური კამერა“ | Name the move, its speed and its extent · დაასახელე მოძრაობა, სიჩქარე და მოცულობა: `slow crane up, 3 metres over the shot` |

The rule behind the table: if a word does not change what a camera, a light or a lens would have to
do on a real set, it is not carrying anything. Cut it and spend the tokens on the source, the
direction and the distance.

წესი, რომელზეც ეს ცხრილი დგას: თუ სიტყვა არ ცვლის იმას, რასაც რეალურ მოედანზე კამერა, ხელსაწყო ან
ობიექტივი გააკეთებდა, ის არაფერს ატარებს. ამოაგდე და ტოკენი წყაროზე, მიმართულებასა და მანძილზე
დახარჯე.

---

## 6. Assembled examples / აწყობილი მაგალითები

Eight shots. Each one changes a single vocabulary choice and leaves the rest alone, so you can see
what that choice is worth. SL-01/SL-02 are the same woman at two sizes; SL-05/SL-06 are the same
bench, static and handheld.

რვა კადრი. თითოეულში ერთი ტერმინი იცვლება და დანარჩენი უცვლელი რჩება — ასე ჩანს, რას აკეთებს
თითოეული არჩევანი. SL-01/SL-02 ერთი და იგივე ქალია ორ სხვადასხვა პლანში; SL-05/SL-06 — ერთი და
იგივე სკამი, სტატიკურად და ხელის კამერით.

---

### SL-01 · Extreme wide — the place is the subject
`sora` `veo` `runway` — shot size, establishing

**EN**
```
Extreme wide shot, the figure about one fifth of the frame height. A woman stands at the rail of a third-floor wooden balcony in an old Tbilisi courtyard and does not move. Camera: static, locked off on a tripod. Lighting: late afternoon sun from frame right, hard, raking across the carved balcony posts; the courtyard below in full shade. Mood: waiting. Audio: a television through an open window, pigeons on the roof, no music. Duration: 6s.
```

**KA**
```
შორი პლანი; ფიგურა კადრის სიმაღლის დაახლოებით მეხუთედია. ქალი ძველი თბილისური ეზოს მესამე სართულზე, ხის აივნის მოაჯირთან დგას და არ მოძრაობს. კამერა: სტატიკური, შტატივზე ჩამაგრებული. განათება: შუადღის შემდგომი მზე კადრიდან მარჯვნივ, ხისტი, ირიბად ეცემა აივნის მოჩუქურთმებულ სვეტებს; ეზო ქვემოთ სრულ ჩრდილშია. განწყობა: მოლოდინი. ხმა: ტელევიზორი ღია ფანჯრიდან, მტრედები სახურავზე, მუსიკის გარეშე. ხანგრძლივობა: 6 წამი.
---
Extreme wide shot, the figure about one fifth of the frame height. A woman stands at the rail of a third-floor wooden balcony in an old Tbilisi courtyard and does not move. Camera: static, locked off on a tripod. Lighting: late afternoon sun from frame right, hard, raking across the carved balcony posts; the courtyard below in full shade. Mood: waiting. Audio: a television through an open window, pigeons on the roof, no music. Duration: 6s.
```

---

### SL-02 · Same woman, medium close-up — now it is a face, not a place
`sora` `veo` `runway` — shot size, performance

**EN**
```
Medium close-up, chest to the top of the head, the woman slightly left of centre. She lifts her eyes from the courtyard to something off frame right and holds the look. Camera: static, locked off on a tripod. Lighting: the same late afternoon sun from frame right, hard, one cheek lit and the other falling into shadow, no fill. Mood: waiting. Audio: a television through an open window, pigeons on the roof, no music. Duration: 6s.
```

**KA**
```
ახლო პლანი — მკერდიდან თავის ზემოთა კიდემდე; ქალი ცენტრიდან ოდნავ მარცხნივ. ეზოდან თვალს აშორებს, კადრს გარეთ, მარჯვნივ იხედება და მზერას ინარჩუნებს. კამერა: სტატიკური, შტატივზე ჩამაგრებული. განათება: იგივე შუადღის შემდგომი მზე კადრიდან მარჯვნივ, ხისტი; ერთი ლოყა განათებულია, მეორე ჩრდილში გადადის, შემავსებელი შუქის გარეშე. განწყობა: მოლოდინი. ხმა: ტელევიზორი ღია ფანჯრიდან, მტრედები სახურავზე, მუსიკის გარეშე. ხანგრძლივობა: 6 წამი.
---
Medium close-up, chest to the top of the head, the woman slightly left of centre. She lifts her eyes from the courtyard to something off frame right and holds the look. Camera: static, locked off on a tripod. Lighting: the same late afternoon sun from frame right, hard, one cheek lit and the other falling into shadow, no fill. Mood: waiting. Audio: a television through an open window, pigeons on the roof, no music. Duration: 6s.
```

---

### SL-03 · Rack focus carries the reveal
`sora` `veo` `runway` — camera, focus

**EN**
```
Medium shot at a stall in the Dezerter bazaar in Tbilisi. Rows of churchkhela hang across the foreground, sharp; the seller stands two metres behind them, soft. Camera: static; rack focus from the churchkhela to the seller's face over about one second, the foreground going soft as she comes sharp. Lighting: overcast daylight through the market's corrugated roof, soft, no cast shadows. Mood: plain, observational. Audio: market chatter, a crate dropped somewhere off frame, no music. Duration: 5s.
```

**KA**
```
საშუალო პლანი დეზერტირების ბაზრის დახლთან, თბილისში. წინა პლანზე ჩამოკიდებული ჩურჩხელის რიგები, ფოკუსში; გამყიდველი მათ უკან, ორ მეტრში, ფოკუსს გარეთ. კამერა: სტატიკური; ფოკუსის გადატანა ჩურჩხელიდან გამყიდველის სახეზე დაახლოებით 1 წამში — წინა პლანი ბუნდოვანდება, სახე იკვეთება. განათება: ღრუბლიანი დღის შუქი ბაზრის თუნუქის სახურავიდან, რბილი, ჩრდილების გარეშე. განწყობა: მშრალი, დამკვირვებლის. ხმა: ბაზრის ხმაური, კადრს გარეთ სადღაც ყუთი ვარდება, მუსიკის გარეშე. ხანგრძლივობა: 5 წამი.
---
Medium shot at a stall in the Dezerter bazaar in Tbilisi. Rows of churchkhela hang across the foreground, sharp; the seller stands two metres behind them, soft. Camera: static; rack focus from the churchkhela to the seller's face over about one second, the foreground going soft as she comes sharp. Lighting: overcast daylight through the market's corrugated roof, soft, no cast shadows. Mood: plain, observational. Audio: market chatter, a crate dropped somewhere off frame, no music. Duration: 5s.
```

---

### SL-04 · Motivated practical — the bulb is inside the frame
`sora` `veo` `runway` — lighting, practical

**EN**
```
Wide shot inside a Kakheti marani at night. A man crouches and lifts the clay lid off a buried qvevri. Camera: static, locked off, low, the lens about level with the qvevri lids. Lighting: one bare bulb hanging in frame above him is the only source — hard, from directly above, his eye sockets in shadow, the vaulted walls falling to black two metres out. Mood: private, unhurried. Audio: stone scraping on clay, a dog outside, no music. Duration: 6s.
```

**KA**
```
ზოგადი პლანი ღამით, კახურ მარანში. მამაკაცი ჩაჯდება და მიწაში ჩაფლულ ქვევრს თიხის სარქველს ხდის. კამერა: სტატიკური, ჩამაგრებული, დაბლა — ობიექტივი ქვევრის სარქველების დონეზე. განათება: ერთადერთი წყარო კადრში ჩამოკიდებული შიშველი ნათურაა — ხისტი, პირდაპირ ზემოდან; თვალის ფოსოები ჩრდილშია, თაღოვანი კედლები ორ მეტრში შავში გადადის. განწყობა: პირადი, აუჩქარებელი. ხმა: ქვა თიხაზე ხახუნობს, გარეთ ძაღლი, მუსიკის გარეშე. ხანგრძლივობა: 6 წამი.
---
Wide shot inside a Kakheti marani at night. A man crouches and lifts the clay lid off a buried qvevri. Camera: static, locked off, low, the lens about level with the qvevri lids. Lighting: one bare bulb hanging in frame above him is the only source — hard, from directly above, his eye sockets in shadow, the vaulted walls falling to black two metres out. Mood: private, unhurried. Audio: stone scraping on clay, a dog outside, no music. Duration: 6s.
```

---

### SL-05 · Locked off — the camera is not involved
`sora` `veo` `runway` — camera, register

**EN**
```
Wide shot. A teenage boy sits alone on a metal bench at the Didube marshrutka station, a rucksack between his feet, watching the vans pull out. Camera: static, locked off on a tripod, the boy small in the left third of the frame. Lighting: flat overcast daylight, soft, no direction, no cast shadows. Mood: detached, observational. Audio: idling diesel engines, a destination shouted twice, no music. Duration: 7s.
```

**KA**
```
ზოგადი პლანი. მოზარდი ბიჭი მარტო ზის დიდუბის სამარშრუტო ტაქსების სადგურის რკინის სკამზე, ზურგჩანთა ფეხებს შორის უდევს, და უყურებს, როგორ მიდიან მიკროავტობუსები. კამერა: სტატიკური, შტატივზე ჩამაგრებული; ბიჭი პატარაა, კადრის მარცხენა მესამედში. განათება: ღრუბლიანი დღის თანაბარი შუქი, რბილი, მიმართულებისა და ჩრდილების გარეშე. განწყობა: დისტანცირებული, დამკვირვებლის. ხმა: დიზელის ძრავები უქმად, ორჯერ გადაძახებული მიმართულება, მუსიკის გარეშე. ხანგრძლივობა: 7 წამი.
---
Wide shot. A teenage boy sits alone on a metal bench at the Didube marshrutka station, a rucksack between his feet, watching the vans pull out. Camera: static, locked off on a tripod, the boy small in the left third of the frame. Lighting: flat overcast daylight, soft, no direction, no cast shadows. Mood: detached, observational. Audio: idling diesel engines, a destination shouted twice, no music. Duration: 7s.
```

---

### SL-06 · Same bench, handheld — only the camera line changed
`sora` `veo` `runway` — camera, register

**EN**
```
Wide shot. A teenage boy sits alone on a metal bench at the Didube marshrutka station, a rucksack between his feet, watching the vans pull out. Camera: handheld, small constant drift and breath, the frame reacquiring him every couple of seconds, no whip and no zoom. Lighting: flat overcast daylight, soft, no direction, no cast shadows. Mood: restless, close to him. Audio: idling diesel engines, a destination shouted twice, no music. Duration: 7s.
```

**KA**
```
ზოგადი პლანი. მოზარდი ბიჭი მარტო ზის დიდუბის სამარშრუტო ტაქსების სადგურის რკინის სკამზე, ზურგჩანთა ფეხებს შორის უდევს, და უყურებს, როგორ მიდიან მიკროავტობუსები. კამერა: ხელის კამერა, მუდმივი მცირე რხევა და სუნთქვა; კადრი ყოველ ორ წამში ხელახლა პოულობს მას; მკვეთრი პანორამისა და ზუმის გარეშე. განათება: ღრუბლიანი დღის თანაბარი შუქი, რბილი, მიმართულებისა და ჩრდილების გარეშე. განწყობა: მოუსვენარი, მასთან ახლოს. ხმა: დიზელის ძრავები უქმად, ორჯერ გადაძახებული მიმართულება, მუსიკის გარეშე. ხანგრძლივობა: 7 წამი.
---
Wide shot. A teenage boy sits alone on a metal bench at the Didube marshrutka station, a rucksack between his feet, watching the vans pull out. Camera: handheld, small constant drift and breath, the frame reacquiring him every couple of seconds, no whip and no zoom. Lighting: flat overcast daylight, soft, no direction, no cast shadows. Mood: restless, close to him. Audio: idling diesel engines, a destination shouted twice, no music. Duration: 7s.
```

---

### SL-07 · Telephoto compression does the isolating
`sora` `veo` `runway` — lens, depth

**EN**
```
Medium close-up on a 200mm telephoto lens, shallow depth of field at f/2.8. A man walks straight toward camera along Rustaveli Avenue, his size in the frame barely changing; the crowd behind him stacks up flat and out of focus, the plane trees compressed into a single wall of green. Camera: static, long lens, no zoom. Lighting: overcast midday, soft and even, no cast shadows. Mood: isolated in a crowd. Audio: traffic, footsteps, one car horn, no music. Duration: 6s.
```

**KA**
```
ახლო პლანი 200 მმ გრძელფოკუსიანი ობიექტივით, მცირე სიღრმის ველი, დიაფრაგმა f/2.8. მამაკაცი პირდაპირ კამერისკენ მოდის რუსთაველის გამზირზე და კადრში მისი ზომა თითქმის არ იცვლება; უკან ხალხი ბრტყლად ეწყობა ერთმანეთზე, ფოკუსს გარეთ, ჭადრები ერთ მწვანე კედლად იკუმშება. კამერა: სტატიკური, გრძელფოკუსიანი ობიექტივი, ზუმის გარეშე. განათება: ღრუბლიანი შუადღე, რბილი და თანაბარი, ჩრდილების გარეშე. განწყობა: მარტოობა ხალხში. ხმა: ტრანსპორტი, ნაბიჯები, ერთხელ მანქანის სიგნალი, მუსიკის გარეშე. ხანგრძლივობა: 6 წამი.
---
Medium close-up on a 200mm telephoto lens, shallow depth of field at f/2.8. A man walks straight toward camera along Rustaveli Avenue, his size in the frame barely changing; the crowd behind him stacks up flat and out of focus, the plane trees compressed into a single wall of green. Camera: static, long lens, no zoom. Lighting: overcast midday, soft and even, no cast shadows. Mood: isolated in a crowd. Audio: traffic, footsteps, one car horn, no music. Duration: 6s.
```

---

### SL-08 · Scale instead of "epic"
`sora` `veo` `runway` — shot size, lighting

**EN**
```
Extreme wide shot. Gergeti Trinity church sits on its ridge with Kazbegi behind it; a single walker on the path is about one thirtieth of the frame height, and that is what gives the mountain its size. Camera: slow crane up, 3 metres over the shot, the horizon dropping through the frame. Lighting: golden hour, low sun behind the ridge, the church rim-lit and its front face in shadow, the valley below already blue. Mood: cold, indifferent. Audio: wind across the grass, no music. Duration: 8s.
```

**KA**
```
შორი პლანი. გერგეტის სამება ქედზე დგას, უკან ყაზბეგი; ბილიკზე ერთი მოსიარულე კადრის სიმაღლის დაახლოებით 1/30-ია — სწორედ ეს აძლევს მთას ზომას. კამერა: ნელი აწევა კრანით, 3 მეტრი მთელ კადრზე; ჰორიზონტი კადრში ქვევით ჩადის. განათება: ოქროს საათი, დაბალი მზე ქედის უკნიდან — ეკლესია კონტრაჟურშია, ფასადი ჩრდილში, ხეობა ქვემოთ უკვე ლურჯია. განწყობა: ცივი, გულგრილი. ხმა: ქარი ბალახში, მუსიკის გარეშე. ხანგრძლივობა: 8 წამი.
---
Extreme wide shot. Gergeti Trinity church sits on its ridge with Kazbegi behind it; a single walker on the path is about one thirtieth of the frame height, and that is what gives the mountain its size. Camera: slow crane up, 3 metres over the shot, the horizon dropping through the frame. Lighting: golden hour, low sun behind the ridge, the church rim-lit and its front face in shadow, the valley below already blue. Mood: cold, indifferent. Audio: wind across the grass, no music. Duration: 8s.
```
