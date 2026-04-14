---
title: "AskUserQuestion — How & When to Use It"
topic: fullstack
status: published
created: 2026-04-13
tags: [claude, planning, agentic, askuserquestion, prompt-engineering]
---

# 🙋 AskUserQuestion — How & When to Use It

> `AskUserQuestion` is a Claude tool that **pauses execution and asks the user a clarifying question** before proceeding. It's the difference between an agent that guesses and one that collaborates.

---

## What Is AskUserQuestion?

In Claude's agentic (tool-use) mode, Claude can call tools — read files, run bash, write code. `AskUserQuestion` is a special tool that interrupts the flow and surfaces a question directly to the user.

Think of it like this:

> 🤖 Claude is a contractor building your house. `AskUserQuestion` is Claude stopping before pouring the foundation to ask: *"Did you want the garage on the left or the right?"* — instead of just guessing and building the wrong thing.

Without it, Claude picks an assumption and keeps going. With it, Claude delegates the decision back to you when the answer **actually matters**.

---

## When Should Claude Use AskUserQuestion?

Use it when continuing without input would mean:

| Situation                        | Why It Matters                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| **Ambiguous requirements**       | Two reasonable interpretations exist — both are valid, but lead to different code         |
| **Irreversible actions**         | About to delete, overwrite, or deploy something that can't easily be undone               |
| **Missing critical context**     | A key piece of info wasn't provided (e.g., which database? which auth method?)            |
| **Multiple valid architectures** | The choice has real long-term consequences (e.g., monorepo vs. separate repos)            |
| **User preference matters**      | Style, naming conventions, folder structure — things with no "right" answer               |
| **Scope is unclear**             | "Build me a login page" — does that mean just the UI, or also the API route and DB logic? |

### When NOT to Use It

Don't ask when:
- The answer is obvious from context
- You can make a reasonable default and say so ("I'm using `src/` layout — let me know if you prefer otherwise")
- The question is trivial and doesn't affect the outcome
- You already asked once — don't keep interrupting

> 💡 **Rule of thumb**: If Claude can write a confident comment saying "I'm assuming X because Y", it should proceed. If it can't justify the assumption, it should ask.

---

## How It Works (Technical)

`AskUserQuestion` is a tool defined in Claude's tool schema. When Claude calls it, the agent loop **pauses**, the question is rendered to the user, and the answer is injected back as a tool result before the agent continues.

```json
// Claude calls this tool
{
  "tool": "AskUserQuestion",
  "input": {
    "question": "Should the Stripe webhook endpoint be protected by authentication, or should it only validate the Stripe signature?",
    "options": ["Stripe signature only (standard)", "Add extra auth layer"]
  }
}

// User answers → flows back as tool result → Claude continues
```

In the Claude Code harness, this shows up as an interactive prompt mid-session.

---

## 5 Real Examples

### Example 1 — Database Choice (Architecture Fork)

**Scenario**: You ask Claude to "add user profiles to the app."

**Bad**: Claude silently picks Firestore and builds the whole thing.

**Good**: Claude asks:

> *"For user profiles, should I store data in **Firestore** (already used for auth) or a separate **PostgreSQL** table? Firestore is simpler to set up but PostgreSQL is better for complex relational queries."*

**Why it matters**: This decision affects schema, queries, cost, and migrations — hard to undo later.

---

### Example 2 — Deployment Target (Irreversible Setup)

**Scenario**: "Deploy this app."

**Bad**: Claude picks Vercel, configures everything, and you later realize you needed Docker for the backend API routes.

**Good**: Claude asks:

> *"Where should I deploy this? Options:*
> *1. **Vercel** — zero config, best for pure Next.js with no heavy server-side work*
> *2. **GCP Cloud Run** — Docker container, needed if you're using Firebase Admin SDK server-side or have long-running processes"*

---

### Example 3 — Auth Scope (Ambiguous Requirements)

**Scenario**: "Add login to the app."

**Bad**: Claude builds Google-only login.

**Good**: Claude asks:

> *"What auth methods do you need?*
> *- Google sign-in only*
> *- Email/password only*
> *- Both*
> *- Also want magic link / phone auth?"*

---

### Example 4 — Stripe Mode (Critical: Test vs. Live)

**Scenario**: "Set up Stripe payments."

**Good**: Claude asks before touching any config:

> *"Are we setting up Stripe in **test mode** (`sk_test_...`) for development, or **live mode** (`sk_live_...`) for production? I want to make sure I don't accidentally configure live payment keys in a dev environment."*

**Why it matters**: Using live keys in dev = real charges on real cards.

---

### Example 5 — File Overwrite Warning (Irreversible Action)

**Scenario**: Claude is about to rewrite a large component.

**Good**: Claude asks:

> *"`AuthProvider.tsx` already exists and has 200+ lines. Should I:*
> *1. Rewrite it completely (your version will be lost)*
> *2. Extend it (add Google login alongside existing email login)*
> *3. Show you a diff first before making changes?"*

---

## Best Practices for Writing Plans That Trigger Good Questions

When you give Claude a task, you can **pre-answer** the common questions to reduce interruptions:

```
❌ Vague:
"Add payments to my app"

✅ Specific:
"Add Stripe payments to my Next.js app. Use test mode for now.
Support card payments only (no Alipay yet). Store payment status
in Firestore. The webhook endpoint should be /api/stripe-webhook."
```

The more context you provide upfront, the fewer questions Claude needs to ask — and the more focused the questions will be when it does ask.

---

## Summary

| | Details |
|---|---|
| **Purpose** | Pause execution to get a decision only the user can make |
| **Best used for** | Forks, irreversible actions, missing context, ambiguous scope |
| **Avoid when** | Assumption is reasonable and can be stated inline |
| **Formats** | Free text question, or question + options list |
| **Effect** | Agent pauses → user answers → agent resumes with that context |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/01-Planning-with-Claude/Plan to Code - Using Subagents]]
- [[07-Fullstack-Development/00-INDEX]]
