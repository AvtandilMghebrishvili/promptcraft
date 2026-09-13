# Agents & automation / აგენტები და ავტომატიზაცია

Two groups. **Extraction contracts** — prompts for an AI node inside n8n, Zapier or Make, whose output is read by the next node. **Orchestrator briefs** — prompts for Perplexity, Manus or Claude, which describe a finished deliverable and the criteria it must meet.
Extraction output feeds a machine, not a person, so the schema is a contract: every field is typed, every absent value is `null`, and every wrong input has a named error object.
Orchestrators decompose the work internally, so scripting the steps for them makes the result worse — state the deliverable and the acceptance criteria, then stop.
Georgian entries use local formats: `საიდენტიფიკაციო კოდი`, `+995 5XX XXX XXX`, `ლარი`, `RS.ge`, `IBAN` starting `GE`.

ორი ჯგუფი. **ამოკრების კონტრაქტები** — პრომპტები AI-ნოდისთვის n8n-ში, Zapier-ში ან Make-ში, რომლის გამოსავალსაც შემდეგი ნოდი კითხულობს. **ორკესტრატორის ბრიფები** — პრომპტები Perplexity-სთვის, Manus-სთვის და Claude-სთვის, რომლებიც აღწერენ მზა შედეგს და მისი მიღების კრიტერიუმებს.
ამოკრების გამოსავალს ადამიანი კი არა, მანქანა კითხულობს — ამიტომ სქემა კონტრაქტია: ყოველ ველს აქვს ტიპი, ყოველი არარსებული მნიშვნელობა `null`-ია და ყოველ არასწორ შესატანს თავისი დასახელებული შეცდომის ობიექტი ხვდება.
ორკესტრატორი ამოცანას თვითონ შლის ეტაპებად — ნაბიჯების გაწერა შედეგს აუარესებს, ამიტომ დაასახელე მზა შედეგი და მიღების კრიტერიუმები და გაჩერდი.
ქართული ჩანაწერები ადგილობრივ ფორმატს იყენებს: `საიდენტიფიკაციო კოდი`, `+995 5XX XXX XXX`, `ლარი`, `RS.ge`, `IBAN` — `GE`-თი დაწყებული.

---

### AG-01 · Invoice to accounting row
`n8n` `zapier` `make` — extraction, finance

**EN**
```
INPUT: the text of one supplier invoice — OCR output or pasted text.

<document>
{{document_text}}
</document>

EXTRACT:
- supplier_name (string)
- supplier_tax_id (string, 9 or 11 digits, digits only)
- invoice_number (string)
- rs_ge_reference (string)
- invoice_date (string, ISO 8601 date)
- due_date (string, ISO 8601 date)
- currency (string, 3-letter ISO code)
- subtotal (number)
- vat_amount (number)
- total_amount (number)
- iban (string)
- line_items (array of {description: string, quantity: number, unit_price: number})

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- NEVER calculate one field from the others. A subtotal that is not printed is null, even when total_amount and vat_amount are both present.
- Amounts: digits and "." only. Strip currency symbols, spaces and thousand separators. "1 250,00 ₾" becomes 1250.00.
- currency is "GEL" when the amount is written in ლარი or ₾, and only then.
- supplier_tax_id: strip spaces, then accept only 9 or 11 digits. Any other length is null.
- iban: accept only a 22-character string starting with "GE". Anything else is null.
- rs_ge_reference is the RS.ge waybill or invoice reference printed on the document. It NEVER goes into invoice_number.
- If the document is not an invoice, return {"error":"NOT_AN_INVOICE"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ერთი მომწოდებლის ინვოისის ტექსტი — OCR-ის შედეგი ან ჩასმული ტექსტი.

<დოკუმენტი>
{{დოკუმენტის_ტექსტი}}
</დოკუმენტი>

EXTRACT:
- supplier_name (სტრიქონი)
- supplier_tax_id (სტრიქონი, 9 ან 11 ციფრი, მხოლოდ ციფრები)
- invoice_number (სტრიქონი)
- rs_ge_reference (სტრიქონი)
- invoice_date (სტრიქონი, ISO 8601 თარიღი)
- due_date (სტრიქონი, ISO 8601 თარიღი)
- currency (სტრიქონი, 3-ასოიანი ISO კოდი)
- subtotal (რიცხვი)
- vat_amount (რიცხვი)
- total_amount (რიცხვი)
- iban (სტრიქონი)
- line_items (მასივი: {description: სტრიქონი, quantity: რიცხვი, unit_price: რიცხვი})

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- ერთი ველი მეორისგან არასდროს გამოთვალო. თუ subtotal ამობეჭდილი არ არის, ის null-ია — მაშინაც კი, როცა total_amount და vat_amount ორივე გაქვს.
- თანხები: მხოლოდ ციფრები და „.“. მოაშორე ვალუტის სიმბოლო, ჰარეები და ათასების გამყოფი. „1 250,00 ₾“ იქცევა 1250.00-ად.
- currency არის "GEL" მაშინ, როცა თანხა ლარშია ან ₾-ითაა აღნიშნული — და მხოლოდ მაშინ.
- supplier_tax_id: ჰარეების მოშორების შემდეგ მიიღე მხოლოდ 9 ან 11 ციფრი. ნებისმიერი სხვა სიგრძე null-ია.
- iban: მიიღე მხოლოდ 22-სიმბოლოიანი სტრიქონი, რომელიც იწყება "GE"-თი. სხვა ყველაფერი null-ია.
- rs_ge_reference არის დოკუმენტზე ამობეჭდილი RS.ge-ის ზედნადების ან ინვოისის ნომერი. ის invoice_number-ში არასდროს ჩასვა.
- თუ დოკუმენტი ინვოისი არ არის, დააბრუნე {"error":"NOT_AN_INVOICE"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-02 · Inbound CV to hiring sheet
`n8n` `zapier` `make` — extraction, hr

**EN**
```
INPUT: the text of one inbound CV, from an email attachment or a form upload.

<cv>
{{cv_text}}
</cv>

EXTRACT:
- full_name (string)
- email (string, lowercase)
- phone (string, "+995 5XX XXX XXX" for Georgian mobiles)
- city (string)
- current_title (string)
- current_employer (string)
- years_experience (number, one decimal place)
- education (array of {degree: string, institution: string, end_year: integer})
- skills (array of strings, in the candidate's own words)
- languages (array of {language: string, level: string})
- earliest_start_date (string, ISO 8601 date)
- salary_expectation (number)
- links (array of strings, full URLs)

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- years_experience: sum only roles that carry both a start and an end (or "present"). If any role lacks dates, the whole field is null. NEVER derive experience from a graduation year or from a job title.
- phone: a Georgian mobile is 9 digits beginning with 5 — output it as "+995 5XX XXX XXX" with single spaces. A number that carries a different country code stays exactly as written, spaces stripped.
- skills: copy the candidate's own wording. NEVER translate, NEVER expand an abbreviation, NEVER add a skill implied by a role.
- level inside languages: copy as printed ("B2", "fluent", "მშობლიური"). NEVER map it onto a scale.
- salary_expectation: only a number the candidate states. A range gives the lower bound. A number in any currency other than GEL is null.
- If the text is not a CV, return {"error":"NOT_A_CV"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ერთი შემოსული CV-ის ტექსტი — წერილზე მიმაგრებული ან ფორმიდან ატვირთული.

<რეზიუმე>
{{რეზიუმეს_ტექსტი}}
</რეზიუმე>

EXTRACT:
- full_name (სტრიქონი)
- email (სტრიქონი, პატარა ასოებით)
- phone (სტრიქონი, ქართული მობილურისთვის "+995 5XX XXX XXX")
- city (სტრიქონი)
- current_title (სტრიქონი)
- current_employer (სტრიქონი)
- years_experience (რიცხვი, ერთი ათწილადით)
- education (მასივი: {degree: სტრიქონი, institution: სტრიქონი, end_year: მთელი რიცხვი})
- skills (სტრიქონების მასივი, კანდიდატის საკუთარი ფორმულირებით)
- languages (მასივი: {language: სტრიქონი, level: სტრიქონი})
- earliest_start_date (სტრიქონი, ISO 8601 თარიღი)
- salary_expectation (რიცხვი)
- links (სტრიქონების მასივი, სრული URL-ები)

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- years_experience: შეკრიბე მხოლოდ ის პოზიციები, რომლებსაც დაწყებისა და დასრულების თარიღი (ან „დღემდე“) აქვს. თუ რომელიმე პოზიციას თარიღი აკლია, მთელი ველი null-ია. გამოცდილება არასდროს გამოიყვანო დამთავრების წლიდან ან თანამდებობის სახელწოდებიდან.
- phone: ქართული მობილური 9 ციფრია და 5-ით იწყება — ჩაწერე ფორმატით "+995 5XX XXX XXX", თითო ჰარით. სხვა ქვეყნის კოდის მქონე ნომერი დარჩეს ისე, როგორც წერია, ჰარეების გარეშე.
- skills: გადმოიტანე კანდიდატის ფორმულირება უცვლელად. არასდროს თარგმნო, არასდროს გახსნა აბრევიატურა, არასდროს დაამატო უნარი, რომელსაც პოზიცია გულისხმობს.
- level ველი languages-ში: გადმოიწერე ისე, როგორც წერია („B2“, „თავისუფლად“, „მშობლიური“). შკალაზე არასდროს გადაიყვანო.
- salary_expectation: მხოლოდ ის რიცხვი, რომელსაც კანდიდატი ასახელებს. დიაპაზონიდან აიღე ქვედა ზღვარი. ლარის გარდა სხვა ვალუტაში დასახელებული თანხა null-ია.
- თუ ტექსტი CV არ არის, დააბრუნე {"error":"NOT_A_CV"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-03 · Customer email to intent, urgency and entities
`n8n` `zapier` `make` — classification, support

**EN**
```
INPUT: one inbound customer email, subject and body.

<email>
{{email_text}}
</email>

EXTRACT:
- intent (string, exactly one of: "order_status", "refund_request", "complaint", "pricing_question", "technical_problem", "cancellation", "other")
- urgency (string, exactly one of: "P0", "P1", "P2", "P3")
- language (string, one of: "ka", "en", "ru", "other")
- customer_name (string)
- customer_email (string, lowercase)
- order_reference (string)
- products_mentioned (array of strings)
- money_amount (number)
- deadline_stated (string, ISO 8601 date)
- requires_human (boolean)
- one_line_summary (string, max 20 words, facts from the email only)

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- urgency comes from stated facts, never from tone or capital letters:
  P0 — the customer states the service is unusable, or that money left their account and nothing arrived.
  P1 — a paid order is late past a date the customer names.
  P2 — something works incorrectly but the customer can still transact.
  P3 — a question, a request, or feedback.
- requires_human is true when intent is "complaint" or "refund_request", when the email mentions a lawyer, a court, or the press, or when money_amount is above 500. Otherwise false.
- one_line_summary MUST NOT contain a fact that is not in the email, and MUST NOT contain a recommendation.
- If the message is an automated notification, a newsletter or a delivery receipt, return {"error":"NOT_A_CUSTOMER_EMAIL"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ერთი შემოსული წერილი მომხმარებლისგან — სათაური და ტექსტი.

<წერილი>
{{წერილის_ტექსტი}}
</წერილი>

EXTRACT:
- intent (სტრიქონი, ზუსტად ერთი: "order_status", "refund_request", "complaint", "pricing_question", "technical_problem", "cancellation", "other")
- urgency (სტრიქონი, ზუსტად ერთი: "P0", "P1", "P2", "P3")
- language (სტრიქონი: "ka", "en", "ru", "other")
- customer_name (სტრიქონი)
- customer_email (სტრიქონი, პატარა ასოებით)
- order_reference (სტრიქონი)
- products_mentioned (სტრიქონების მასივი)
- money_amount (რიცხვი, ლარში)
- deadline_stated (სტრიქონი, ISO 8601 თარიღი)
- requires_human (ლოგიკური)
- one_line_summary (სტრიქონი, მაქსიმუმ 20 სიტყვა, მხოლოდ წერილში დაფიქსირებული ფაქტი)

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- urgency დაადგინე დაფიქსირებული ფაქტით და არა ტონით ან დიდი ასოებით:
  P0 — მომხმარებელი წერს, რომ სერვისი არ მუშაობს, ან რომ თანხა ჩამოეჭრა და შედეგი არ მიუღია.
  P1 — გადახდილი შეკვეთა აგვიანებს იმ თარიღზე, რომელსაც მომხმარებელი ასახელებს.
  P2 — რაღაც არასწორად მუშაობს, მაგრამ მომხმარებელი მაინც ახერხებს ოპერაციის დასრულებას.
  P3 — კითხვა, თხოვნა ან უკუკავშირი.
- requires_human არის true, როცა intent არის "complaint" ან "refund_request", როცა წერილში ნახსენებია ადვოკატი, სასამართლო ან მედია, ან როცა money_amount 500-ზე მეტია. დანარჩენ შემთხვევაში — false.
- one_line_summary-ში არ უნდა იყოს ფაქტი, რომელიც წერილში არ წერია, და არ უნდა იყოს რეკომენდაცია.
- თუ წერილი ავტომატური შეტყობინება, სიახლეების დაგზავნა ან მიწოდების დადასტურებაა, დააბრუნე {"error":"NOT_A_CUSTOMER_EMAIL"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-04 · Meeting transcript to action items
`n8n` `zapier` `make` — extraction, operations

**EN**
```
INPUT: the transcript of one meeting.

<transcript>
{{transcript}}
</transcript>

EXTRACT:
- meeting_date (string, ISO 8601 date)
- attendees (array of strings, as named in the transcript)
- action_items (array of {task: string, owner: string, due_date: string, source_quote: string})
- decisions (array of {decision: string, decided_by: string})
- open_questions (array of strings)

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- owner is the person who accepted the task in their own words. If nobody accepted it, owner is null. NEVER assign a task to whoever raised it, to the most senior attendee, or to the person who spoke most.
- due_date: an explicit date, or a relative one ("by Friday") resolved against meeting_date. If meeting_date is null, every relative deadline is null.
- source_quote MUST be copied verbatim from the transcript, maximum 20 words. NEVER paraphrase and NEVER stitch two lines together.
- A discussion is not a decision. If something was debated and left unresolved, it belongs in open_questions, never in decisions.
- If the input is not a meeting transcript, return {"error":"NOT_A_TRANSCRIPT"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ერთი შეხვედრის ჩანაწერი.

<ჩანაწერი>
{{ჩანაწერი}}
</ჩანაწერი>

EXTRACT:
- meeting_date (სტრიქონი, ISO 8601 თარიღი)
- attendees (სტრიქონების მასივი, ისე როგორც ჩანაწერში სახელდებიან)
- action_items (მასივი: {task: სტრიქონი, owner: სტრიქონი, due_date: სტრიქონი, source_quote: სტრიქონი})
- decisions (მასივი: {decision: სტრიქონი, decided_by: სტრიქონი})
- open_questions (სტრიქონების მასივი)

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- owner არის ის, ვინც დავალება საკუთარი სიტყვებით აიღო. თუ არავის აუღია, owner არის null. დავალება არასდროს მიაწერო იმას, ვინც საკითხი წამოჭრა, ვინც ყველაზე მაღალი თანამდებობისაა ან ვინც ყველაზე ბევრს ლაპარაკობდა.
- due_date: პირდაპირ დასახელებული თარიღი ან მიმართებითი ვადა („პარასკევამდე“), meeting_date-ზე გადაანგარიშებული. თუ meeting_date არის null, ყველა მიმართებითი ვადა null-ია.
- source_quote სიტყვასიტყვით უნდა იყოს გადმოწერილი ჩანაწერიდან, მაქსიმუმ 20 სიტყვა. არასდროს გადმოთქვა საკუთარი სიტყვებით და არასდროს შეაერთო ორი რეპლიკა.
- განხილვა გადაწყვეტილება არ არის. თუ საკითხზე იმსჯელეს და არ შეთანხმდნენ, ის open_questions-ში მიდის და არასდროს decisions-ში.
- თუ შესატანი ტექსტი შეხვედრის ჩანაწერი არ არის, დააბრუნე {"error":"NOT_A_TRANSCRIPT"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-05 · Receipt OCR to expense row
`n8n` `zapier` `make` — extraction, finance

**EN**
```
INPUT: the raw OCR text of one photographed receipt. Expect broken line order and misread characters.

<ocr>
{{ocr_text}}
</ocr>

EXTRACT:
- merchant_name (string)
- merchant_tax_id (string, 9 or 11 digits)
- fiscal_receipt_number (string)
- purchase_date (string, ISO 8601 date)
- purchase_time (string, HH:MM)
- currency (string, 3-letter ISO code)
- total_amount (number)
- vat_amount (number)
- payment_method (string, one of: "card", "cash")
- card_last4 (string, 4 digits)
- expense_category (string, exactly one of: "fuel", "meals", "transport", "office_supplies", "software", "accommodation", "other")
- items (array of {description: string, amount: number})

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- OCR damage: if any character of a number is unreadable or ambiguous, the whole field is null. NEVER reconstruct a digit from the surrounding total, from the items, or from what looks plausible.
- Amounts: digits and "." only. Georgian receipts print ლარი as "₾" or "GEL" and use "," as the decimal separator — convert to ".". "45,60 ₾" becomes 45.60.
- total_amount is the printed final total, not a sum of items. If the printed total and the sum of items disagree, keep the printed total and do nothing else.
- merchant_tax_id: 9 or 11 digits after stripping spaces. Any other length is null.
- expense_category is chosen only from the list above, using merchant_name and items. If nothing matches, use "other".
- If the text is not a receipt, return {"error":"NOT_A_RECEIPT"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: გადაღებული ჩეკის დაუმუშავებელი OCR ტექსტი. ელოდე არეულ სტრიქონებს და არასწორად ამოცნობილ სიმბოლოებს.

<ocr>
{{ocr_ტექსტი}}
</ocr>

EXTRACT:
- merchant_name (სტრიქონი)
- merchant_tax_id (სტრიქონი, 9 ან 11 ციფრი)
- fiscal_receipt_number (სტრიქონი)
- purchase_date (სტრიქონი, ISO 8601 თარიღი)
- purchase_time (სტრიქონი, HH:MM)
- currency (სტრიქონი, 3-ასოიანი ISO კოდი)
- total_amount (რიცხვი)
- vat_amount (რიცხვი)
- payment_method (სტრიქონი: "card" ან "cash")
- card_last4 (სტრიქონი, 4 ციფრი)
- expense_category (სტრიქონი, ზუსტად ერთი: "fuel", "meals", "transport", "office_supplies", "software", "accommodation", "other")
- items (მასივი: {description: სტრიქონი, amount: რიცხვი})

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- OCR-ის დაზიანება: თუ რიცხვში თუნდაც ერთი სიმბოლო გაურკვეველია, მთელი ველი null-ია. ციფრი არასდროს აღადგინო ჯამის, პოზიციების ან „ლოგიკური“ მნიშვნელობის მიხედვით.
- თანხები: მხოლოდ ციფრები და „.“. ქართული ჩეკი ლარს წერს „₾“-ით ან „GEL“-ით და ათწილადს „,“-ით ყოფს — გადაიყვანე „.“-ზე. „45,60 ₾“ იქცევა 45.60-ად.
- total_amount არის ამობეჭდილი საბოლოო ჯამი და არა პოზიციების შეკრება. თუ ამობეჭდილი ჯამი და პოზიციების ჯამი არ ემთხვევა, დატოვე ამობეჭდილი და სხვა არაფერი გააკეთო.
- merchant_tax_id: ჰარეების მოშორების შემდეგ 9 ან 11 ციფრი. ნებისმიერი სხვა სიგრძე null-ია.
- expense_category აირჩიე მხოლოდ ზემოთ მოცემული სიიდან, merchant_name-ისა და items-ის მიხედვით. თუ არცერთი არ ერგება, ჩაწერე "other".
- თუ ტექსტი ჩეკი არ არის, დააბრუნე {"error":"NOT_A_RECEIPT"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-06 · Support ticket triage and routing
`n8n` `zapier` `make` — classification, support

**EN**
```
INPUT: one support ticket — subject, body, and any metadata the form captured.

<ticket>
{{ticket_text}}
</ticket>

EXTRACT:
- queue (string, exactly one of: "billing", "technical", "delivery", "account", "sales", "unroutable")
- priority (string, exactly one of: "P0", "P1", "P2", "P3")
- sla_hours (integer)
- tags (array of strings, from this list only: "refund", "outage", "bug", "how_to", "integration", "invoice", "password", "damaged_goods", "late_delivery")
- customer_tier (string, one of: "free", "standard", "enterprise")
- escalate_to (string)
- blocked_on_customer (boolean)
- duplicate_of (string, a ticket id written inside the ticket itself)
- summary (string, max 25 words)

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- sla_hours is fixed by priority: P0 = 2, P1 = 8, P2 = 24, P3 = 72. NEVER produce any other value.
- queue is "unroutable" when the ticket names no product, no order and no account. Do not guess a queue from the customer's mood.
- customer_tier: only from metadata that states it. NEVER infer a tier from spend, tone, or company name.
- escalate_to is filled only when priority is "P0" or tags contain "outage": write "on_call_engineer". Otherwise null.
- blocked_on_customer is true only when the ticket says the customer still owes us something — a file, a screenshot, an approval.
- summary contains only facts stated in the ticket: no diagnosis, no suggested fix, no apology.
- If the input is a marketing email, a bounce notification or an empty submission, return {"error":"NOT_A_SUPPORT_TICKET"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ერთი მხარდაჭერის თიქეთი — სათაური, ტექსტი და ფორმიდან მიღებული მონაცემები.

<თიქეთი>
{{თიქეთის_ტექსტი}}
</თიქეთი>

EXTRACT:
- queue (სტრიქონი, ზუსტად ერთი: "billing", "technical", "delivery", "account", "sales", "unroutable")
- priority (სტრიქონი, ზუსტად ერთი: "P0", "P1", "P2", "P3")
- sla_hours (მთელი რიცხვი)
- tags (სტრიქონების მასივი, მხოლოდ ამ სიიდან: "refund", "outage", "bug", "how_to", "integration", "invoice", "password", "damaged_goods", "late_delivery")
- customer_tier (სტრიქონი: "free", "standard", "enterprise")
- escalate_to (სტრიქონი)
- blocked_on_customer (ლოგიკური)
- duplicate_of (სტრიქონი, თიქეთის ნომერი, რომელიც თავად ტექსტშია მითითებული)
- summary (სტრიქონი, მაქსიმუმ 25 სიტყვა)

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- sla_hours ფიქსირებულია priority-ის მიხედვით: P0 = 2, P1 = 8, P2 = 24, P3 = 72. სხვა მნიშვნელობა არასდროს დააბრუნო.
- queue არის "unroutable" მაშინ, როცა თიქეთში არც პროდუქტი, არც შეკვეთა და არც ანგარიში არ სახელდება. რიგი მომხმარებლის განწყობით არ გამოიცნო.
- customer_tier: მხოლოდ იმ მონაცემიდან, სადაც ის პირდაპირ წერია. სტატუსი არასდროს გამოიყვანო თანხის, ტონის ან კომპანიის სახელის მიხედვით.
- escalate_to ივსება მხოლოდ მაშინ, როცა priority არის "P0" ან tags შეიცავს "outage"-ს: ჩაწერე "on_call_engineer". დანარჩენ შემთხვევაში null.
- blocked_on_customer არის true მხოლოდ მაშინ, როცა ტექსტიდან ჩანს, რომ მომხმარებელს ჩვენთვის რაღაც მოსაწოდებელი აქვს — ფაილი, სქრინშოტი, დადასტურება.
- summary შეიცავს მხოლოდ თიქეთში დაფიქსირებულ ფაქტს: არც დიაგნოზი, არც შემოთავაზებული გამოსავალი, არც ბოდიში.
- თუ შესატანი სარეკლამო წერილი, დაბრუნებული შეტყობინება ან ცარიელი ფორმაა, დააბრუნე {"error":"NOT_A_SUPPORT_TICKET"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-07 · Form submission validation and normalisation
`n8n` `zapier` `make` — validation, forms

**EN**
```
INPUT: one raw web form submission, exactly as the user typed it.

<submission>
{{submission}}
</submission>

EXTRACT:
- full_name (string, trimmed, internal whitespace collapsed to one space)
- email (string, lowercase, trimmed)
- phone (string, "+995 5XX XXX XXX")
- company_name (string)
- company_tax_id (string, 9 or 11 digits)
- preferred_date (string, ISO 8601 date)
- budget_amount (number)
- message (string, trimmed)
- consent_marketing (boolean)
- valid (boolean)
- field_errors (array of {field: string, code: string})

RULES:
- If a field is absent, use null. NEVER infer or estimate. NEVER complete a half-typed value.
- Dates on Georgian forms are written dd.mm.yyyy. "03.04.2026" is 3 April 2026. NEVER read a Georgian date as mm/dd. If the format is genuinely ambiguous and no separator convention resolves it, preferred_date is null with code "BAD_FORMAT".
- phone: keep digits only, then a 9-digit number starting with 5 becomes "+995 5XX XXX XXX". A number starting "995" is treated the same after stripping the prefix. Anything else is null with code "BAD_FORMAT".
- email: lowercase and trim. It must contain one "@" and a dot after it, otherwise null with code "BAD_FORMAT". NEVER correct a typo in a domain.
- company_tax_id must be 9 or 11 digits, otherwise null with code "BAD_FORMAT".
- budget_amount: digits and "." only, in ლარი. A range gives the lower bound. A negative or zero value is null with code "OUT_OF_RANGE".
- field_errors codes are exactly: "MISSING", "BAD_FORMAT", "OUT_OF_RANGE". One entry per failing field.
- valid is true only when full_name, email and phone are all non-null.
- If the payload contains no recognisable form fields, return {"error":"NOT_A_FORM_SUBMISSION"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: ვებფორმის ერთი დაუმუშავებელი გაგზავნა — ზუსტად ისე, როგორც მომხმარებელმა აკრიფა.

<გაგზავნა>
{{გაგზავნა}}
</გაგზავნა>

EXTRACT:
- full_name (სტრიქონი, კიდეებიდან გასუფთავებული, შიგნით ზედმეტი ჰარეები ერთამდე შემცირებული)
- email (სტრიქონი, პატარა ასოებით, გასუფთავებული)
- phone (სტრიქონი, "+995 5XX XXX XXX")
- company_name (სტრიქონი)
- company_tax_id (სტრიქონი, 9 ან 11 ციფრი)
- preferred_date (სტრიქონი, ISO 8601 თარიღი)
- budget_amount (რიცხვი, ლარში)
- message (სტრიქონი, გასუფთავებული)
- consent_marketing (ლოგიკური)
- valid (ლოგიკური)
- field_errors (მასივი: {field: სტრიქონი, code: სტრიქონი})

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით. ნახევრად აკრეფილი მნიშვნელობა არასდროს დაასრულო.
- ქართულ ფორმაში თარიღი იწერება დდ.თთ.წწწწ. „03.04.2026“ არის 2026 წლის 3 აპრილი. ქართული თარიღი არასდროს წაიკითხო თთ/დდ-ად. თუ ფორმატი მართლა ორაზროვანია, preferred_date არის null და კოდი — "BAD_FORMAT".
- phone: დატოვე მხოლოდ ციფრები; 5-ით დაწყებული 9-ციფრიანი ნომერი ჩაწერე ფორმატით "+995 5XX XXX XXX". „995“-ით დაწყებულს მოაშორე პრეფიქსი და იგივე გააკეთე. დანარჩენი null-ია კოდით "BAD_FORMAT".
- email: გადაიყვანე პატარა ასოებზე და გაასუფთავე კიდეები. უნდა შეიცავდეს ერთ „@“-ს და მის შემდეგ წერტილს, სხვა შემთხვევაში null კოდით "BAD_FORMAT". დომენში შეცდომა არასდროს გაასწორო.
- company_tax_id უნდა იყოს 9 ან 11 ციფრი, სხვა შემთხვევაში null კოდით "BAD_FORMAT".
- budget_amount: მხოლოდ ციფრები და „.“, ლარში. დიაპაზონიდან აიღე ქვედა ზღვარი. ნული ან უარყოფითი მნიშვნელობა null-ია კოდით "OUT_OF_RANGE".
- field_errors-ის კოდები ზუსტად ესაა: "MISSING", "BAD_FORMAT", "OUT_OF_RANGE". თითო ჩავარდნილ ველზე თითო ჩანაწერი.
- valid არის true მხოლოდ მაშინ, როცა full_name, email და phone სამივე შევსებულია.
- თუ მიღებულ მონაცემებში ამოსაცნობი ველი არ არის, დააბრუნე {"error":"NOT_A_FORM_SUBMISSION"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-08 · Website text to lead enrichment record
`n8n` `zapier` `make` — extraction, sales

**EN**
```
INPUT: the concatenated text of a company's website — home, about and contact pages.

<site>
{{site_text}}
</site>

EXTRACT:
- company_name (string)
- legal_form (string, one of: "შპს", "ინდ. მეწარმე", "სს", "ააიპ")
- tax_id (string, 9 or 11 digits)
- industry (string, max 4 words)
- description (string, max 30 words, built from their own wording)
- services (array of strings, as listed on the site)
- employee_count (integer)
- founded_year (integer)
- city (string)
- address (string)
- phone (string, "+995 5XX XXX XXX" for Georgian mobiles)
- email (string, lowercase)
- site_languages (array of strings, ISO 639-1 codes)
- social_links (array of strings, full URLs)
- pricing_published (boolean)
- last_updated_signal (string, ISO 8601 date)

RULES:
- If a field is absent, use null. NEVER infer or estimate.
- employee_count: only a number the site states. NEVER count faces on a team page, NEVER read "small team" or "over 50 specialists" as a number.
- founded_year: only from an explicit statement ("since 2014"). NEVER derive it from a copyright line.
- pricing_published is true only when an actual figure appears on the site. "Contact us for a quote" is false.
- description MUST reuse the company's own claims. NEVER add a benefit, a superlative or a market position the site does not state.
- last_updated_signal is the most recent date printed anywhere on the pages — a post, a news item, a copyright year. If none appears, null.
- If the text is a blog, a marketplace listing, a personal page or an error page, return {"error":"NOT_A_COMPANY_WEBSITE"} and nothing else.

OUTPUT: a single JSON object. No markdown fence, no commentary.
```

**KA**
```
INPUT: კომპანიის საიტის ტექსტი, გვერდები ერთად — მთავარი, „ჩვენ შესახებ“ და კონტაქტი.

<საიტი>
{{საიტის_ტექსტი}}
</საიტი>

EXTRACT:
- company_name (სტრიქონი)
- legal_form (სტრიქონი: "შპს", "ინდ. მეწარმე", "სს", "ააიპ")
- tax_id (სტრიქონი, 9 ან 11 ციფრი)
- industry (სტრიქონი, მაქსიმუმ 4 სიტყვა)
- description (სტრიქონი, მაქსიმუმ 30 სიტყვა, მათივე ფორმულირებიდან აწყობილი)
- services (სტრიქონების მასივი, ისე როგორც საიტზეა ჩამოთვლილი)
- employee_count (მთელი რიცხვი)
- founded_year (მთელი რიცხვი)
- city (სტრიქონი)
- address (სტრიქონი)
- phone (სტრიქონი, ქართული მობილურისთვის "+995 5XX XXX XXX")
- email (სტრიქონი, პატარა ასოებით)
- site_languages (სტრიქონების მასივი, ISO 639-1 კოდები)
- social_links (სტრიქონების მასივი, სრული URL-ები)
- pricing_published (ლოგიკური)
- last_updated_signal (სტრიქონი, ISO 8601 თარიღი)

RULES:
- თუ ველი არ არის, ჩაწერე null. არასდროს გამოიცნო და არასდროს შეაფასო მიახლოებით.
- employee_count: მხოლოდ ის რიცხვი, რომელსაც საიტი ასახელებს. გუნდის გვერდზე ფოტოები არასდროს დათვალო და „მცირე გუნდი“ ან „50-ზე მეტი სპეციალისტი“ რიცხვად არასდროს აქციო.
- founded_year: მხოლოდ პირდაპირი მითითებიდან („2014 წლიდან“). საავტორო უფლების ხაზიდან არასდროს გამოიყვანო.
- pricing_published არის true მხოლოდ მაშინ, როცა საიტზე კონკრეტული ციფრი წერია. „ფასის გასაგებად დაგვიკავშირდით“ — false.
- description უნდა დაეყრდნოს კომპანიის საკუთარ ფორმულირებას. არასდროს დაამატო სარგებელი, ზედსართავი ან საბაზრო პოზიცია, რომელიც საიტზე არ წერია.
- last_updated_signal არის გვერდებზე ამობეჭდილი ყველაზე ახალი თარიღი — პოსტი, სიახლე ან საავტორო უფლების წელი. თუ არცერთია, null.
- თუ ტექსტი ბლოგი, განცხადება, პირადი გვერდი ან შეცდომის გვერდია, დააბრუნე {"error":"NOT_A_COMPANY_WEBSITE"} და სხვა არაფერი.

OUTPUT: ერთი JSON ობიექტი. markdown-ფენსის გარეშე, კომენტარის გარეშე.
```

---

### AG-09 · Market scan table
`perplexity` `manus` `claude` — research, market

**EN**
```
Deliverable: a market scan table for {{market}} in {{geography}}, current as of {{date}}.

One row per company. Columns: company · what they sell, in their own words · price or price range · who they sell to · founded · headcount · funding or ownership · source link for every cell carrying a figure.

Acceptance criteria:
- Between {{min_rows}} and {{max_rows}} rows. Fewer is acceptable if the market really is that small — say so rather than padding the table with adjacent businesses.
- Every figure — price, headcount, founding year, funding — carries a link to the page it came from, plus the date that page was published. A figure without a link does not go in the table.
- If a company does not publish something, write "not published". If only one source states it, write the figure and mark the cell "single source". NEVER estimate, NEVER interpolate from competitors, NEVER carry a number over from an undated article.
- Prices in the seller's own currency, with the ₾ equivalent and the rate date beside it.
- Below the table: the three companies most likely missing from it and why you could not confirm them.
- Last line: the date of the oldest source used.

Do not describe your searches, your process, or what you tried. The table and the two notes under it are the whole deliverable.
```

**KA**
```
მზა შედეგი: ბაზრის მიმოხილვის ცხრილი — {{ბაზარი}}, რეგიონი {{გეოგრაფია}}, მდგომარეობა {{თარიღი}}-ის მიხედვით.

თითო კომპანია — ერთი სტრიქონი. სვეტები: კომპანია · რას ყიდის, საკუთარი სიტყვებით · ფასი ან ფასების დიაპაზონი · ვის ყიდის · დაარსების წელი · თანამშრომელთა რაოდენობა · დაფინანსება ან მფლობელი · წყაროს ბმული ყოველ უჯრაზე, სადაც ციფრი დგას.

მიღების კრიტერიუმები:
- {{მინიმუმი}}-დან {{მაქსიმუმი}} სტრიქონამდე. თუ ბაზარი მართლა პატარაა, ნაკლებიც მისაღებია — ეს პირდაპირ დაწერე და ცხრილი მომიჯნავე ბიზნესებით არ შეავსო.
- ყოველ ციფრს — ფასს, თანამშრომელთა რაოდენობას, დაარსების წელს, დაფინანსებას — უნდა ახლდეს ბმული იმ გვერდზე, საიდანაც აიღე, და იმ გვერდის გამოქვეყნების თარიღი. უბმულო ციფრი ცხრილში არ შედის.
- თუ კომპანია რამეს არ აქვეყნებს, დაწერე „არ არის გამოქვეყნებული“. თუ ციფრს მხოლოდ ერთი წყარო ადასტურებს, ჩაწერე და უჯრას მიაწერე „ერთი წყარო“. არასდროს შეაფასო მიახლოებით, არასდროს გამოიყვანო კონკურენტების მიხედვით და არასდროს გადმოიტანო უთარიღო სტატიის ციფრი.
- ფასი მიუთითე გამყიდველის ვალუტაში და გვერდით მიაწერე ლარის ექვივალენტი კურსისა და კურსის თარიღის მითითებით.
- ცხრილის ქვემოთ: სამი კომპანია, რომელიც სავარაუდოდ აკლია სიას, და რატომ ვერ დაადასტურე.
- ბოლო ხაზი: ყველაზე ძველი გამოყენებული წყაროს თარიღი.

ძებნის ნაბიჯები, პროცესი და მცდელობები არ აღწერო. ცხრილი და ქვემოთ ორი შენიშვნა — ეს არის სრული შედეგი.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### AG-10 · Supplier shortlist with pricing
`perplexity` `manus` `claude` — procurement, research

**EN**
```
Deliverable: a shortlist of {{n}} suppliers of {{product}} that can deliver to {{city}}, Georgia, ranked by total first-year cost at {{annual_volume}}.

For each supplier: name · what exactly they supply · unit price and the quantity it applies to · minimum order · lead time · delivery to Georgia (direct / via forwarder / none) · payment terms · whether they can invoice a Georgian company (RS.ge invoice, საიდენტიფიკაციო კოდი, IBAN starting GE) · one source link per figure.

Acceptance criteria:
- Ranked by total first-year cost, with the arithmetic shown on one line per supplier.
- Every price carries its link and its publication date. A price older than 12 months is marked with that date and treated as indicative, never as a quote.
- If a supplier does not publish pricing, write "not published" and keep them in the list with the rest of the row filled. NEVER estimate a price from a competitor, from a category average, or from an old figure converted at today's rate.
- Quote in the supplier's own currency, then the ₾ equivalent with the rate and the date you used.
- Anything about Georgian import duty, VAT on import, or certification requirements goes in its own column and cites the regulation. If it is not stated anywhere official, write "not stated".
- Close with: which two suppliers to request a quote from first, and the single missing fact that would most change the ranking.

Do not report your search steps. The table and the closing note are the deliverable.
```

**KA**
```
მზა შედეგი: {{n}} მომწოდებლის მოკლე სია — {{პროდუქტი}}, მიწოდებით {{ქალაქი}}-ში, საქართველოში; დალაგებული პირველი წლის ჯამური ხარჯით, მოცულობაზე {{წლიური_მოცულობა}}.

თითო მომწოდებელზე: სახელი · რას აწვდის ზუსტად · ერთეულის ფასი და რა რაოდენობაზე ვრცელდება · მინიმალური შეკვეთა · მიწოდების ვადა · მიწოდება საქართველოში (პირდაპირ / გადამზიდის გავლით / არ ახორციელებს) · ანგარიშსწორების პირობები · გამოწერს თუ არა ინვოისს ქართულ კომპანიაზე (RS.ge-ის ინვოისი, საიდენტიფიკაციო კოდი, GE-თი დაწყებული IBAN) · თითო ციფრზე თითო წყაროს ბმული.

მიღების კრიტერიუმები:
- დაალაგე პირველი წლის ჯამური ხარჯით; თითო მომწოდებელზე ერთ ხაზში აჩვენე გამოთვლა.
- ყოველ ფასს უნდა ახლდეს ბმული და გამოქვეყნების თარიღი. 12 თვეზე ძველ ფასს მიაწერე თარიღი და მოექეცი როგორც სარეკომენდაციოს და არა როგორც შეთავაზებას.
- თუ მომწოდებელი ფასს არ აქვეყნებს, დაწერე „არ არის გამოქვეყნებული“ და მაინც დატოვე სიაში — სტრიქონის დანარჩენი ველი შეავსე. ფასი არასდროს გამოიყვანო კონკურენტიდან, კატეგორიის საშუალოდან ან დღევანდელი კურსით გადაყვანილი ძველი ციფრიდან.
- ფასი დაწერე მომწოდებლის ვალუტაში, შემდეგ ლარის ექვივალენტი კურსისა და მისი თარიღის მითითებით.
- იმპორტის გადასახადი, დღგ იმპორტზე და სერტიფიცირების მოთხოვნა ცალკე სვეტში წერია, რეგულაციის მითითებით. თუ ოფიციალურად არსად წერია, დაწერე „მითითებული არ არის“.
- დაასრულე ორი პუნქტით: რომელ ორ მომწოდებელს სთხოვდი შეთავაზებას პირველად და ერთი დაკლებული ფაქტი, რომელიც რიგს ყველაზე მეტად შეცვლიდა.

ძებნის ნაბიჯები არ აღწერო. ცხრილი და დამასრულებელი შენიშვნა — ეს არის შედეგი.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### AG-11 · Weekly competitor-change digest
`perplexity` `manus` `claude` — monitoring, strategy

**EN**
```
Deliverable: a digest of what changed at {{competitors}} between {{start_date}} and {{end_date}}.

Group the changes under: pricing · product · positioning and messaging · hiring · funding and ownership · public incidents.

Each entry is one line: what changed, from what to what, the date it was observed, the link.

Acceptance criteria:
- Only changes with a dated source inside the window. A page that exists but carries no date goes under a separate heading, "undated — cannot be placed in the window".
- "From what to what" needs both states. If the current state is visible but the previous one is not, write "previous state not established" — NEVER reconstruct it from memory or from an archive you did not open.
- If a competitor shows no observable change, write "no observable change" under their name. An empty section is a finding, not a gap to fill.
- Report what was published, not what it means. No inference about intent, strategy, runway, or what a change "signals".
- If something is not published — headcount, churn, the reason for a price move — write "not published" and leave it there. NEVER estimate.
- Close with three sentences: the one change that most affects {{our_decision}}, and why.
```

**KA**
```
მზა შედეგი: დაიჯესტი იმისა, რა შეიცვალა კონკურენტებთან — {{კონკურენტები}} — პერიოდში {{დაწყება}}-დან {{დასრულება}}-მდე.

ცვლილებები დაალაგე სექციებად: ფასები · პროდუქტი · პოზიციონირება და კომუნიკაცია · დაქირავება · დაფინანსება და მფლობელობა · საჯარო ინციდენტები.

თითო ჩანაწერი ერთი ხაზია: რა შეიცვალა, რიდან რაზე, როდის დააფიქსირე, ბმული.

მიღების კრიტერიუმები:
- მხოლოდ ის ცვლილება, რომელსაც პერიოდში მოქცეული თარიღიანი წყარო აქვს. გვერდი, რომელიც არსებობს, მაგრამ თარიღი არ აწერია, ცალკე სათაურის ქვეშ მიდის: „უთარიღო — პერიოდში ვერ თავსდება“.
- „რიდან რაზე“ ორივე მდგომარეობას მოითხოვს. თუ ამჟამინდელი ჩანს, წინა კი არა, დაწერე „წინა მდგომარეობა დადგენილი არ არის“ — მეხსიერებით ან გაუხსნელი არქივით არასდროს აღადგინო.
- თუ კონკურენტთან ხილული ცვლილება არ ფიქსირდება, მის სახელქვეშ დაწერე „ხილული ცვლილება არ ფიქსირდება“. ცარიელი სექცია შედეგია და არა შესავსები ადგილი.
- დაწერე ის, რაც გამოქვეყნდა, და არა ის, რას ნიშნავს. განზრახვაზე, სტრატეგიაზე, ფინანსურ მარაგზე ან იმაზე, რას „მიანიშნებს“ ცვლილება, დასკვნა არ გააკეთო.
- თუ რამე გამოქვეყნებული არ არის — თანამშრომელთა რაოდენობა, გადინება, ფასის ცვლილების მიზეზი — დაწერე „არ არის გამოქვეყნებული“ და იქვე გაჩერდი. არასდროს შეაფასო მიახლოებით.
- დაასრულე სამი წინადადებით: ერთი ცვლილება, რომელიც ყველაზე მეტად მოქმედებს გადაწყვეტილებაზე {{ჩვენი_გადაწყვეტილება}}, და რატომ.
```

---

### AG-12 · Compliance requirements file
`perplexity` `manus` `claude` — compliance, research

**EN**
```
Deliverable: a requirements file for {{activity}} in Georgia — everything the business must have in place before it can legally operate.

One row per requirement. Columns: requirement · issuing or enforcing authority (შემოსავლების სამსახური / RS.ge, სურსათის ეროვნული სააგენტო, the municipality, and so on) · the law or regulation it comes from · fee · processing time · what it depends on (a registered entity, a lease, another permit) · renewal period · source link.

Acceptance criteria:
- Every requirement cites the regulation itself or the issuing authority's own page. Anything sourced only from a blog, a forum, or a consultancy's marketing page goes in a separate section, "reported but not confirmed in a primary source".
- Fees and processing times come from the authority's published schedule. If a fee or a timeline is not stated in an official source, write "not stated" — NEVER estimate from another permit, another country, or an older version of the rule.
- Order the rows by dependency: what must exist first appears first.
- Mark every source page whose last update is older than 24 months with its date.
- State separately what applies only above a revenue threshold, and name the threshold with its source.
- Close with: the three requirements most likely to have changed recently, and which office to call to confirm each.

Do not write a step-by-step registration walkthrough. The file is the deliverable.
```

**KA**
```
მზა შედეგი: მოთხოვნების ნუსხა საქმიანობისთვის {{საქმიანობა}} საქართველოში — ყველაფერი, რაც ბიზნესს უნდა ჰქონდეს, სანამ ლეგალურად დაიწყებს მუშაობას.

თითო მოთხოვნა — ერთი სტრიქონი. სვეტები: მოთხოვნა · გამცემი ან მაკონტროლებელი უწყება (შემოსავლების სამსახური / RS.ge, სურსათის ეროვნული სააგენტო, მუნიციპალიტეტი და ა.შ.) · კანონი ან რეგულაცია, საიდანაც გამომდინარეობს · საფასური · განხილვის ვადა · რაზეა დამოკიდებული (რეგისტრირებული სუბიექტი, იჯარის ხელშეკრულება, სხვა ნებართვა) · განახლების პერიოდი · წყაროს ბმული.

მიღების კრიტერიუმები:
- ყოველ მოთხოვნას უნდა ახლდეს თავად რეგულაცია ან გამცემი უწყების საკუთარი გვერდი. ის, რაც მხოლოდ ბლოგში, ფორუმში ან საკონსულტაციო კომპანიის სარეკლამო გვერდზე წერია, ცალკე სექციაში მიდის: „ნახსენებია, პირველწყაროთი დადასტურებული არ არის“.
- საფასური და ვადა აიღე უწყების გამოქვეყნებული ტარიფიდან. თუ ოფიციალურ წყაროში არ წერია, დაწერე „მითითებული არ არის“ — არასდროს გამოიყვანო სხვა ნებართვის, სხვა ქვეყნის ან წესის ძველი რედაქციის მიხედვით.
- სტრიქონები დაალაგე დამოკიდებულების მიხედვით: ის, რაც ჯერ უნდა არსებობდეს, წინ დგას.
- ყოველ წყაროს, რომელიც 24 თვეზე დიდი ხნის წინ განახლდა, მიაწერე მისი თარიღი.
- ცალკე დაწერე, რა მოქმედებს მხოლოდ ბრუნვის გარკვეული ზღვრის ზემოთ, და დაასახელე ეს ზღვარი წყაროსთან ერთად.
- დაასრულე: სამი მოთხოვნა, რომელიც დიდი ალბათობით ბოლო პერიოდში შეიცვალა, და რომელ უწყებას უნდა დაურეკო თითოეულის დასაზუსტებლად.

რეგისტრაციის ეტაპობრივი ინსტრუქცია არ დაწერო. ნუსხა თავად არის შედეგი.

დაწერე ბუნებრივ ქართულად, სიტყვასიტყვითი თარგმანის ინტონაციის გარეშე.
```

---

### AG-13 · Research brief that ends with the decisive question
`perplexity` `manus` `claude` — research, decision support

**EN**
```
Deliverable: a research brief on {{question}}, written for someone who must decide {{decision}} by {{date}}.

Sections, in this order: what is established · what is contested and by whom · what nobody has published · what this means for the decision · the one question that would most change the conclusion.

Acceptance criteria:
- Under 900 words.
- Every claim carries a source link. A claim you cannot link does not go in the brief.
- "Contested" means two named sources disagree. Name both, state what each says, and say which one has the stronger evidence and why. A single dissenting blog post is not a controversy.
- Where the evidence does not exist, say so in "what nobody has published". NEVER fill the gap with a plausible number, a projection, or an analogy from a different market. If a figure is not published, write "not published"; if a source declines to state it, write "not stated".
- "What this means for the decision" must name the two or three facts the decision actually turns on — not a summary of the sections above.
- The final section is one question, not a list. Its answer must be able to flip or materially change the recommendation, and you must state which answer points which way.
- No description of your research process and no list of sources you consulted but did not use.
```

**KA**
```
მზა შედეგი: კვლევითი ბრიფი კითხვაზე {{კითხვა}}, დაწერილი იმისთვის, ვინც {{თარიღი}}-მდე უნდა გადაწყვიტოს {{გადაწყვეტილება}}.

სექციები, ამ თანმიმდევრობით: რა არის დადგენილი · რაზეა უთანხმოება და ვის შორის · რა არავის გამოუქვეყნებია · რას ნიშნავს ეს გადაწყვეტილებისთვის · ერთი კითხვა, რომელიც დასკვნას ყველაზე მეტად შეცვლიდა.

მიღების კრიტერიუმები:
- 900 სიტყვამდე.
- ყოველ მტკიცებას უნდა ახლდეს წყაროს ბმული. მტკიცება, რომელსაც ბმულს ვერ მიაბამ, ბრიფში არ შედის.
- „უთანხმოება“ ნიშნავს, რომ ორი დასახელებული წყარო ერთმანეთს ეწინააღმდეგება. დაასახელე ორივე, დაწერე რას ამბობს თითოეული და რომელს აქვს უფრო ძლიერი მტკიცებულება და რატომ. ერთი განსხვავებული ბლოგპოსტი დავა არ არის.
- იქ, სადაც მტკიცებულება არ არსებობს, ეს სექციაში „რა არავის გამოუქვეყნებია“ დაწერე. ხარვეზი არასდროს ამოავსო დამაჯერებელი ციფრით, პროგნოზით ან სხვა ბაზრიდან გადმოტანილი ანალოგიით. თუ ციფრი გამოქვეყნებული არ არის, დაწერე „არ არის გამოქვეყნებული“; თუ წყარო მის დასახელებაზე თავს იკავებს — „მითითებული არ არის“.
- სექციაში „რას ნიშნავს ეს გადაწყვეტილებისთვის“ დაასახელე ორი ან სამი ფაქტი, რომელზეც გადაწყვეტილება რეალურად დგას — და არა წინა სექციების შეჯამება.
- ბოლო სექცია ერთი კითხვაა და არა სია. მისმა პასუხმა უნდა შეძლოს რეკომენდაციის შეცვლა ან შებრუნება, და შენ უნდა დაწერო, რომელი პასუხი რომელ მხარეს მიგვიყვანს.
- კვლევის პროცესი არ აღწერო და გამოუყენებელი წყაროების სია არ დაურთო.
```
