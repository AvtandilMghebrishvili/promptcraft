# Harness / ჰარნესი

Drop-in standing-rules templates. Copy one into whichever file your tool reads, delete what does
not apply, fill in the rest. Then stop repeating those lines in every prompt.

მზა შაბლონები მუდმივი წესებისთვის. დააკოპირე იმ ფაილში, რომელსაც შენი ინსტრუმენტი კითხულობს,
წაშალე რაც არ გეხება, დანარჩენი შეავსე. შემდეგ ეს ხაზები ყოველ პრომპტში აღარ გაიმეორო.

| File | Read by |
|---|---|
| `CLAUDE.md` | Claude Code, Claude Desktop |
| `AGENTS.md` | Codex, and a growing number of agents |
| `.cursorrules` or `.cursor/rules/*.mdc` | Cursor |
| `.windsurfrules` | Windsurf |
| `.clinerules` | Cline |
| `.github/copilot-instructions.md` | GitHub Copilot |

The content is the same; only the filename differs. Put it at the repo root.

- **[`rules.md`](rules.md)** — English template
- **[`rules.ka.md`](rules.ka.md)** — Georgian template

## Why bother

Read [`../references/agent-harness.md`](../references/agent-harness.md) first. The short version:
standing facts that apply to every task should not be retyped in every prompt. They cost tokens
every time, and you forget one about a third of the time.

## The rule for keeping it short

**If you cannot say what a line prevents, delete it.**

A rules file that only grows becomes a tax on every request and eventually contradicts itself.
Prune it when you prune the code.

**წესი, რომელიც მას მოკლედ ინახავს: თუ ვერ ამბობ, რას იცავს კონკრეტული ხაზი — წაშალე.**

## What does not belong here

- Task-specific instructions — those go in the prompt
- Anything your formatter or linter already enforces — that goes in a hook or a pre-commit
- Long architecture essays — the agent reads the code better than your description of it
- Dated notes, one-off decisions, debugging scratch
