# Georgian localisation style guide
# ქართული ლოკალიზაციის სტილის გზამკვლევი

This is the document that makes PromptCraft different from a translated prompt list.
Read it before writing or reviewing any Georgian prompt in this repo.

ეს არის დოკუმენტი, რომელიც PromptCraft-ს ნათარგმნი პრომპტების სიისგან განასხვავებს.
წაიკითხე, სანამ ამ რეპოში რომელიმე ქართულ პრომპტს დაწერ ან შეამოწმებ.

---

## 0. The one rule

**Do not translate the English prompt. Write the Georgian prompt from the same intent.**

Open the English version, understand what it is trying to make the model do, close it,
and write the Georgian prompt as if the English one never existed. Then compare for
coverage — not for wording.

A Georgian prompt that maps 1:1 onto the English sentences is a failed prompt even when
every word is correct.

---

## 1. Register: how the prompt addresses the model

**Use `შენ`-form imperative. Always.**

| ✅ | ❌ | Why |
|---|---|---|
| `დაწერე` | `გთხოვთ დაწეროთ` | Politeness padding costs tokens and adds nothing. The model is not a colleague. |
| `გააანალიზე` | `გაანალიზება გჭირდება` | Imperative is unambiguous; nominalisation is not an instruction. |
| `შენ ხარ გამოცდილი რედაქტორი` | `თქვენ ხართ გამოცდილი რედაქტორი` | `თქვენ`-form drags formal-register vocabulary into the output. |
| `არ გამოიყენო` | `გთხოვთ, არ გამოიყენოთ` | Same reason. |

**Exception:** when the prompt instructs the model to *produce* text addressed to a human —
a client email, a customer reply — the produced text may be `თქვენ`-form. Say so explicitly:
`დაწერე წერილი თქვენობით, ოფიციალური რეგისტრით.` The instruction stays `შენ`-form; only the output changes.

---

## 2. Terminology: keep the loanwords people actually use

Georgian technical vocabulary is loanword-heavy and that is fine. Purist replacements make a
prompt read like a school translation exercise and — worse — reduce the model's recognition
of the concept.

### Keep as-is

`პრომპტი` · `ტოკენი` · `მოდელი` · `კონტენტი` · `ბრენდი` · `ფორმატი` · `სტრუქტურა` ·
`დედლაინი` · `ბიუჯეტი` · `მარკეტინგი` · `კამპანია` · `სტარტაპი` · `ინვესტორი` ·
`კომპოზიცია` · `რენდერი` · `კადრი` · `მონტაჟი` · `ინტერფეისი` · `ბექენდი` · `ფრონტენდი` ·
`დებაგინგი` · `რეფაქტორინგი` · `კომიტი` · `რეპოზიტორი` · `ტესტი` · `ლოგი` · `ფიჩერი` ·
`სპრინტი` · `ფიდბექი` · `ონბორდინგი` · `ჩეკლისტი` · `შაბლონი` · `თემპლეიტი`

### Translate — these have real Georgian equivalents in active use

| English | Use | Not |
|---|---|---|
| output | `გამოსავალი`, `შედეგი` | `აუთფუთი` |
| input | `შესატანი მონაცემები`, `მასალა` | `ინფუთი` |
| audience | `აუდიტორია`, `სამიზნე ჯგუფი` | — |
| constraint | `შეზღუდვა` | `კონსტრეინტი` |
| requirement | `მოთხოვნა` | `რექვაირმენტი` |
| goal | `მიზანი` | `გოული` |
| draft | `მონახაზი`, `პირველადი ვერსია` | `დრაფტი` (acceptable but weaker) |
| summary | `შეჯამება` | `სამარი` |
| step | `ეტაპი`, `ნაბიჯი` | `სტეპი` |
| tone | `ტონი`, `კილო` | — |

### Never invent

If you find yourself coining a Georgian compound for a concept that everyone in the field
names in English, stop. Use the loanword. `პრომპტი` is not `მოთხოვნის ტექსტური ფორმულირება`.

---

## 3. Syntax: stop transposing English

Georgian word order is flexible but **information-structure driven**, and the verb carries
person, number, tense and often the object. English sentence shapes do not survive transposition.

### Role assignment

```
EN  You are an experienced financial analyst who works with Georgian SMEs.
❌  შენ ხარ გამოცდილი ფინანსური ანალიტიკოსი ვინც მუშაობს ქართულ მცირე ბიზნესთან.
✅  შენ ხარ ფინანსური ანალიტიკოსი, რომელსაც ქართულ მცირე და საშუალო ბიზნესთან მუშაობის გამოცდილება აქვს.
```
The `✅` version uses `რომელსაც … აქვს` instead of a stranded `ვინც მუშაობს`, and puts the
experience where Georgian puts it — in a possessive construction.

### Conditional instructions

```
EN  If the input contains no dates, return "NO_DATE" instead of guessing.
❌  თუ შესატანი შეიცავს არა თარიღებს, დააბრუნე "NO_DATE" ნაცვლად გამოცნობის.
✅  თუ ტექსტში თარიღი არ გვხვდება, გამოცნობის ნაცვლად დააბრუნე "NO_DATE".
```
Georgian negation attaches to the verb (`არ გვხვდება`), not to the noun. And `ნაცვლად` takes
the genitive and goes *before* what it replaces.

### Lists of constraints

```
EN  MUST NOT exceed 200 words. MUST cite a source for every number.
❌  არ უნდა აღემატებოდეს 200 სიტყვებს. უნდა ციტირდეს წყარო ყოველი რიცხვისთვის.
✅  ტექსტი არ უნდა აღემატებოდეს 200 სიტყვას. ყოველ ციფრს უნდა ახლდეს წყაროს მითითება.
```
Note: `200 სიტყვას` — Georgian numerals take the singular. `200 სიტყვებს` is wrong and it is
the single most common error in machine-translated Georgian prompts.

### Purpose clauses

```
EN  Rewrite the text to make it clearer for non-specialists.
❌  გადაწერე ტექსტი რომ გახადო ის უფრო ნათელი არა-სპეციალისტებისთვის.
✅  გადაწერე ტექსტი ისე, რომ არასპეციალისტმაც გაიგოს.
```

---

## 4. Grammar traps that keep appearing

| Trap | Wrong | Right |
|---|---|---|
| Numeral + noun | `5 დღეები`, `200 სიტყვებს` | `5 დღე`, `200 სიტყვას` |
| `-ის` vs `-ს` after vowel-final stems | `კომპანიაის` | `კომპანიის` |
| Plural of loanwords | `ბრენდსები` | `ბრენდები` |
| `რომელიც` case agreement | `კომპანია, რომელიც აქვს` | `კომპანია, რომელსაც აქვს` |
| Redundant `არის` | `ეს არის არის მნიშვნელოვანი` / `მიზანი არის რომ` | `მიზანია` |
| Calqued "make sure" | `დარწმუნდი, რომ გააკეთო` | `აუცილებლად გააკეთე` / `გადაამოწმე, რომ …` |
| Calqued "feel free to" | `თავისუფლად იგრძენი თავი` | (delete it — it carries no instruction) |
| Calqued "in terms of" | `ტერმინებში` | `თვალსაზრისით` / restructure |
| English capitals | `Marketing სტრატეგია` | Georgian has no capitals; use quotes or a colon for emphasis |
| Latin punctuation habits | `„…“` vs `"…"` | Georgian quotation marks are `„ “` |

---

## 5. Context adaptation: swap the world, not just the words

A prompt is useless if its examples reference a country the user does not live in.
When adapting, replace the *referent*, not the vocabulary.

| Domain | English default | Georgian adaptation |
|---|---|---|
| Currency | dollars, USD | `ლარი`, `₾`; mention `აშშ დოლარი` only when the scenario is genuinely cross-border |
| Tax / registration | IRS, EIN, LLC | `შემოსავლების სამსახური` / `RS.ge`, `საიდენტიფიკაციო კოდი`, `შპს`, `ინდივიდუალური მეწარმე`, `მცირე ბიზნესის სტატუსი` |
| Banking | Chase, routing number | `TBC`, `საქართველოს ბანკი`, `IBAN`, `ანგარიშის ნომერი` |
| Jobs | Indeed, LinkedIn-only flow | `jobs.ge`, `hr.ge`, `LinkedIn` as one channel among several |
| Education | SAT, GPA, college applications | `ეროვნული გამოცდები`, `სკოლის ატესტატი`, `უნივერსიტეტში ჩაბარება`, `მაგისტრატურა` |
| Healthcare | insurance copay, HMO | `სამედიცინო დაზღვევა`, `საყოველთაო ჯანდაცვა`, `კლინიკა` |
| Property | zip code, HOA | `საკადასტრო კოდი`, `საჯარო რეესტრი`, `ბინათმესაკუთრეთა ამხანაგობა` |
| Retail / e-commerce | Amazon, Etsy | `Facebook Marketplace`, `MyMarket`, `Extra.ge`, `Vendoo`, own Instagram shop |
| Delivery | FedEx, USPS | `Glovo`, `Wolt`, `Georgian Post`, `კურიერი` |
| Seasonality | Thanksgiving, Black Friday | `ახალი წელი`, `შობა (7 იანვარი)`, `აღდგომა`, `ბლექ ფრაიდეი` (now real here), `29 მაისი`–`ტურისტული სეზონი` |
| Geography for scene-setting | New York, Central Park | `თბილისი`, `ბათუმი`, `ყაზბეგი`, `სიღნაღი`, `ვაკე`, `მთაწმინდა`, `ძველი თბილისი` |
| Industry examples | Silicon Valley SaaS | `ღვინის მარანი`, `ტურისტული სააგენტო`, `IT-აუთსორსინგი`, `სასტუმრო`, `სამშენებლო კომპანია`, `რესტორანი` |

**Do not over-localise.** If the user is writing for a global audience, keep the global referent.
Adaptation serves the scenario, not a quota.

---

## 6. When the model must output Georgian

Models drift into translationese when asked to write Georgian. Counter it explicitly.

Add this line — or a variant — to any prompt whose output is Georgian:

```
დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

For higher-stakes text, extend it:

```
დაწერე ბუნებრივ ქართულად. აკრძალულია:
- ინგლისური სიტყვათწყობის გადმოტანა
- უცხო კალკები („დარწმუნდი რომ“, „ეს არის ის, რაც“)
- რიცხვის შემდეგ მრავლობითი („5 დღეები“ → „5 დღე“)
- ზედმეტი თავაზიანობის ფორმულები
```

And when register matters, name it:

```
რეგისტრი: [ოფიციალური | ნახევრად ოფიციალური | სასაუბრო | სარეკლამო]
```

---

## 7. Review checklist for a Georgian prompt

Before an entry is merged, all of these must be true.

- [ ] Addresses the model in `შენ`-form imperative
- [ ] No `გთხოვთ` / `გთხოვთ, რომ` politeness padding
- [ ] Every numeral followed by a singular noun
- [ ] No word-order transposition from the English version — read it aloud; it must sound Georgian
- [ ] Loanwords used where the field uses loanwords; no invented purist compounds
- [ ] No calqued idioms (`დარწმუნდი რომ`, `თავისუფლად`, `ტერმინებში`)
- [ ] Context referents adapted (currency, institutions, platforms, geography) where the scenario is local
- [ ] If output is Georgian, the naturalness line is present
- [ ] `{{ცვლადები}}` named in Georgian, not left in English
- [ ] Covers the same functional ground as the English version — verified by function, not by sentence count

---

## 8. Worked example

**Intent:** a prompt that turns a rough product description into marketplace copy.

### English

```
You are a marketplace copywriter. Rewrite the rough product description below into
a listing that converts.

<product>
{{rough_description}}
</product>

Rules:
- MUST be under 120 words
- MUST open with the single strongest benefit, not the product category
- MUST include exactly 4 bullet points of specifications
- NEVER use "high quality", "premium", or "best in class"
- Write for a buyer comparing three similar listings on their phone

Output: title (max 60 characters), then the body, then the 4 bullets.
```

### Georgian — written from intent, not translated

```
შენ ხარ ონლაინ მაღაზიის კოპირაიტერი. ქვემოთ მოცემული სახელდახელო აღწერიდან
შეადგინე განცხადება, რომელიც გაყიდვას მოიტანს.

<პროდუქტი>
{{სახელდახელო_აღწერა}}
</პროდუქტი>

წესები:
- ტექსტი არ უნდა აღემატებოდეს 120 სიტყვას
- პირველივე წინადადებაში დაასახელე მთავარი სარგებელი და არა პროდუქტის კატეგორია
- მიუთითე ზუსტად 4 ბულეტი მახასიათებლებით
- აკრძალულია ფრაზები: „მაღალი ხარისხის“, „პრემიუმ“, „საუკეთესო ბაზარზე“
- წერე ისე, თითქოს მყიდველი ტელეფონიდან ადარებს სამ მსგავს განცხადებას

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.

გამოსავალი: სათაური (მაქსიმუმ 60 სიმბოლო), შემდეგ ძირითადი ტექსტი, ბოლოს 4 ბულეტი.
```

**What changed and why:**

- `marketplace copywriter` → `ონლაინ მაღაზიის კოპირაიტერი`. `მარკეტპლეისი` exists but reads as
  jargon here; the local frame is `ონლაინ მაღაზია` / `განცხადება`.
- `a listing that converts` → `განცხადება, რომელიც გაყიდვას მოიტანს`. `კონვერტირდება` would be a
  calque; Georgian marketers say the outcome, not the metric.
- `MUST be under 120 words` → `არ უნდა აღემატებოდეს 120 სიტყვას` — singular after the numeral.
- `NEVER use "high quality"` → the banned phrases are given *in Georgian*, because that is what the
  model would generate. Banning the English string would do nothing.
- The naturalness line was added — it is not in the English version and does not need to be.
- `title (max 60 characters)` → `სიმბოლო`, not `ხასიათი`. (`character` has two meanings; the machine
  translation of this exact string is a recurring failure.)
