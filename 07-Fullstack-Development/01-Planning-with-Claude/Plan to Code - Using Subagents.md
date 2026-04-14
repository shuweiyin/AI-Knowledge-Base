---
title: "From Plan to Code — Using Subagents"
topic: fullstack
status: published
created: 2026-04-13
tags: [claude, subagents, planning, agentic, orchestration, claude-code]
---

# 🤖 From Plan to Code — Using Subagents

> Subagents let you delegate focused, bounded tasks to a fresh Claude instance while you (or the orchestrator) maintain the big picture. Knowing when to use them is a skill that separates fast builds from tangled messes.

---

## The Core Mental Model

Think of your Claude Code session as a **general contractor**:

- **You** = the architect (holds the vision, makes decisions)
- **Main Claude session** = the site supervisor (coordinates, holds context)
- **Subagents** = specialist workers (plumber, electrician, drywaller — each focused on their task)

You wouldn't have your electrician also manage the project schedule. Similarly, don't ask one Claude session to simultaneously hold 5 large files in context, write tests, refactor components, and update documentation.

```
You (Architect)
    │
    └── Main Claude (Orchestrator)
            ├── Subagent A: "Write the Firebase Auth module"
            ├── Subagent B: "Write the Stripe webhook handler"
            └── Subagent C: "Write unit tests for the above"
```

---

## What Is a Subagent?

In Claude Code, a subagent is spawned via the `Agent` tool. It:

- Starts **fresh** — no memory of the parent session's conversation
- Has **all the same tools** (read, write, bash, grep, etc.)
- Returns a **single result message** to the parent
- Can optionally run in an **isolated git worktree** (so it can't break your working branch)

```json
// The Agent tool call the orchestrator makes
{
  "tool": "Agent",
  "input": {
    "description": "Write Firebase Auth module",
    "prompt": "Create src/lib/firebaseAuth.ts that exports signInWithGoogle() and signInWithEmail(email, password). Use Firebase v9 modular SDK. Include JSDoc comments. The Firebase config is already in src/lib/firebaseConfig.ts — read that file first.",
    "subagent_type": "general-purpose",
    "isolation": "worktree"   // optional: isolated branch
  }
}
```

---

## When to Use a Subagent

### ✅ Good Candidates for Subagents

| Situation | Why |
|-----------|-----|
| **Self-contained module** | Clear inputs/outputs, doesn't need the full conversation history |
| **Parallel independent tasks** | Writing Auth + Stripe + Firestore simultaneously (no shared state yet) |
| **Risky / destructive work** | Use `isolation: worktree` so changes are sandboxed |
| **Context window is getting full** | Offload a large, bounded task before you hit limits |
| **Specialized research** | "Find all usages of X in the codebase" — delegate to an Explore agent |
| **Code review** | Ask a fresh agent with no bias to review what was just written |

### ❌ Don't Use Subagents When

| Situation | Why |
|-----------|-----|
| The task needs conversation history | Subagent starts cold — no memory of decisions made |
| You need back-and-forth iteration | Subagents return once; use the main session for dialogue |
| The task is trivial (< 5 min work) | Spawning overhead isn't worth it |
| Tasks have tight dependencies | If B needs A's exact output to proceed, do them in sequence in main session |
| You need `AskUserQuestion` mid-task | Subagents can't interrupt — clarify first, then spawn |

---

## Writing Good Subagent Prompts

A subagent starts with **zero context**. Your prompt must be self-contained.

### Bad Prompt ❌
```
"Implement the auth module we discussed"
```
The subagent has no idea what "we discussed" means.

### Good Prompt ✅
```
"Create /src/lib/firebaseAuth.ts for a Next.js 14 app using Firebase v9 
modular SDK. 

Export these three functions:
  - signInWithGoogle() → uses signInWithPopup + GoogleAuthProvider
  - signInWithEmail(email, password) → uses signInWithEmailAndPassword
  - signOut() → uses Firebase signOut

The Firebase app instance is already initialized in /src/lib/firebase.ts
— read that file first before writing anything.

Add JSDoc comments. Handle errors by throwing with a user-friendly message.
Do not create new files beyond the one requested."
```

### Checklist for Subagent Prompts

- [ ] State the **exact file(s)** to create or modify
- [ ] List **what to read first** (so it has the right context)
- [ ] Define **inputs and outputs** precisely
- [ ] Name the **tech stack and versions** (Firebase v9, Next.js 14, etc.)
- [ ] Specify **what NOT to do** (don't create extra files, don't modify X)
- [ ] If you need a specific format back, describe it

---

## Parallel vs Sequential Subagents

### Parallel (Independent Tasks)

Spawn multiple subagents in one message when their work doesn't overlap:

```
Main Session spawns simultaneously:
├── Agent A: "Write /src/lib/firebaseAuth.ts"
├── Agent B: "Write /src/lib/stripe.ts"  
└── Agent C: "Write /src/lib/firestore.ts"
```

All three run at the same time → faster delivery. Safe because they write to different files.

### Sequential (Dependent Tasks)

When B needs A's output, wait for A first:

```
Step 1: Agent A → "Write the Firebase Auth module"
           ↓ (returns result)
Step 2: Agent B → "Write the AuthContext using the module A just created at src/lib/firebaseAuth.ts"
```

Don't try to parallelize dependent tasks — the second agent won't know what the first produced.

---

## The `isolation: worktree` Flag

Adding `isolation: "worktree"` creates a **temporary git branch** for the subagent to work in:

- Changes are isolated from your working branch
- If the subagent makes no changes → worktree is auto-cleaned up
- If it makes changes → you get back the branch name and can review before merging

**Use it when**:
- The task could break things (large refactor, file deletions)
- You want to review the diff before it lands in your branch
- Multiple parallel agents are writing different features

```json
{
  "isolation": "worktree"
}
```

---

## Subagent Types

| Type | Use For |
|------|---------|
| `general-purpose` | Writing code, multi-step tasks, research + implementation |
| `Explore` | Read-only codebase investigation — finding files, searching patterns |
| `Plan` | Designing architecture, planning implementation strategy before coding |

For most coding tasks → `general-purpose`.
For "figure out how X works in this codebase" → `Explore`.
For "design the right approach before we build" → `Plan`.

---

## Real Workflow Example: Building a Fullstack Feature

**Goal**: Add Stripe one-time payment to an existing Next.js + Firebase app.

```
Phase 1 — Plan (main session + AskUserQuestion)
  ├── Clarify: test mode or live? one-time or subscription?
  ├── Clarify: store payment in Firestore or Postgres?
  └── Clarify: which page triggers the payment?

Phase 2 — Build (parallel subagents)
  ├── Agent A: "Write /src/lib/stripe.ts — createPaymentIntent server action"
  ├── Agent B: "Write /app/api/stripe-webhook/route.ts — handle payment_intent.succeeded"
  └── Agent C: "Write /src/components/CheckoutForm.tsx — Stripe Elements UI"

Phase 3 — Wire (main session)
  └── Connect the components, update routing, add env var docs

Phase 4 — Review (subagent)
  └── Agent D (Explore): "Audit the Stripe integration for security issues — 
      check webhook signature validation, secret key exposure, and error handling"
```

---

## Summary

| Concept | Key Point |
|---------|-----------|
| **Subagent = fresh start** | No conversation memory — your prompt must be self-contained |
| **Use for bounded tasks** | Clear inputs, clear outputs, limited scope |
| **Parallel when independent** | Fire multiple agents at once for faster builds |
| **Sequential when dependent** | Wait for A before starting B |
| **`isolation: worktree`** | Sandbox risky changes in a temp branch |
| **Clarify before spawning** | Use `AskUserQuestion` in main session first — subagents can't ask |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/01-Planning-with-Claude/AskUserQuestion - How & When]]
- [[07-Fullstack-Development/00-INDEX]]
