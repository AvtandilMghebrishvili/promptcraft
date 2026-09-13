# Project rules

<!--
  Copy this to CLAUDE.md / AGENTS.md / .cursorrules at your repo root.
  Fill in the < > placeholders. DELETE every line that does not apply to you.
  If you cannot say what a line prevents, it does not belong here.
-->

## Stack

- Language and version: <e.g. TypeScript 5.6, Node 22>
- Framework: <e.g. Next.js 15, App Router>
- Package manager: <npm | pnpm | yarn | uv | poetry | go mod>
- Database: <e.g. Postgres 16 via Prisma>
- Deploy target: <e.g. Vercel | Fly.io | self-hosted>

## Commands

Use these exact commands. Do not invent variants.

```
install     <npm ci>
dev         <npm run dev>
test        <npm test>
test one    <npm test -- <path>>
lint        <npm run lint>
typecheck   <npm run typecheck>
build       <npm run build>
```

## Layout

Only the conventions that are not obvious from looking:

- <src/lib/ is shared code; src/app/ is routes only — never put logic in a route file>
- <Database access goes through src/db/*, never a direct client in a component>
- <Tests live next to the file as *.test.ts>

## Definition of done

Nothing is done until all of these pass:

- `<npm test>` passes
- `<npm run typecheck>` passes with no errors
- `<npm run lint>` passes with no new warnings
- New behaviour has a test that fails without the change

## Hard bans

- NEVER install, upgrade or remove a package without asking first
- NEVER modify files under `<migrations/ | .github/ | infra/>`
- NEVER run `git push --force`, `git reset --hard` on a shared branch, or `rm -rf`
- NEVER commit secrets, `.env` files, or credentials of any kind
- NEVER disable a test, a type check, or a lint rule to make something pass. Fix the cause or stop and report.
- NEVER change the public API surface in `<src/api/>` without saying so explicitly in your report

## Code standards

<Keep only what your formatter does not already enforce.>

- <No `any`. If a type is genuinely unknown, use `unknown` and narrow.>
- <Errors are wrapped with context, never swallowed.>
- <Functions that can fail return a result type; exceptions are for programmer error only.>
- <Prefer composition over inheritance; no class hierarchies deeper than one level.>
- <No new dependency for anything under 50 lines of code.>

## Git

- Branch names: `<type/short-description>` — e.g. `fix/empty-cart-500`
- Commit messages: `<imperative mood, under 72 chars, no scope prefix>`
- One logical change per commit
- <Never commit directly to `main`>

## How you should behave

These apply to every task, so they are not repeated in individual prompts.

- **Report as you go.** After each file you modify, print the filename and one line describing the change.
- **Non-destructive default.** When an instruction is ambiguous, choose the reading that destroys
  the least, and state which reading you chose.
- **Stop on tool failure.** If a command or tool call fails, STOP and report the actual error.
  NEVER fabricate a result or continue on an assumption.
- **Retry cap.** Retry a failed approach at most twice. Then stop and report what you tried.
- **Verify, do not infer.** "It works" means you ran the command and it passed. Reading your own
  diff is not verification.
- **Ask before scope growth.** If the fix requires touching a file outside the stated scope,
  STOP and say so rather than expanding on your own.
- **No silent cleanup.** Do not reformat, rename or "tidy" code that is not part of the task.

## Context

- Read `<docs/architecture.md>` before changes that cross module boundaries.
- Session notes and past decisions live in `<docs/decisions/>`. Read the relevant one; do not re-litigate a settled decision.
- <Known sharp edge: describe the one thing that has bitten people repeatedly.>
