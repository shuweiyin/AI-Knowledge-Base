---
title: "What is the Claude Code Harness"
skill: concept-note
type: concept-note
tags: [claude-code, harness, harness-engineering, hooks, settings, tools, automation]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-14
---

# What is the Claude Code Harness — Concept Note

## ⚡ Core Concept (One Sentence)

> The **harness** is the invisible runtime engine wrapped around Claude Code — it controls every tool call, fires hooks at the right moment, enforces permissions, and is what makes Claude Code an *automated agent* instead of just a chatbot.

---

## 🤔 Why It Matters

When you type a message to Claude Code and it reads a file, writes a note, and runs a command — who's actually in charge of that sequence? Not Claude alone. The **harness** is the layer that coordinates everything: it hands Claude its tools, watches what it tries to do, fires automatic responses, and keeps you safe. Understanding the harness means you understand the *real* power of Claude Code — and how to take full control of it.

---

## 📖 Detailed Explanation

### Part 1 — What Is a Harness?

In software engineering, a **harness** is a wrapper framework that surrounds a program and controls *how* it runs — giving it tools, checking its actions, and responding to events.

Think of it like the harness a rock climber wears: the climber (Claude) does the actual climbing, but the harness (the runtime) catches them if something goes wrong, controls how far they can move, and connects them to safety ropes (tools and permissions).

In Claude Code specifically, the harness is responsible for:

| Responsibility | What It Does |
|---|---|
| **Tool execution** | Provides Claude with tools: `Read`, `Write`, `Bash`, `Edit`, `Grep`, `Glob`, and more |
| **Hook firing** | Detects lifecycle events (e.g. "before writing a file") and runs shell commands automatically |
| **Permission enforcement** | Checks `settings.json` to decide what Claude is and isn't allowed to do |
| **Context injection** | Passes outputs from hooks back into Claude's context window |
| **Conversation loop** | Manages the back-and-forth turns between you and Claude |

### Part 2 — What Is Harness Engineering?

**[[Harness Engineering]]** is the practice of *designing and configuring the harness* to customize Claude's automatic behaviors. Instead of telling Claude what to do manually every time, you write rules in `settings.json` that the harness follows *on your behalf* — every session, every tool use, automatically.

Harness engineering is done through three main channels:

#### 1. `settings.json` — The Rulebook

The file at `~/.claude/settings.json` is where all harness rules live. It defines:
- Which **hooks** fire and when
- Which **tools** Claude is allowed to use
- Which **shell commands** should auto-run at lifecycle moments

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'About to write a file. Check path is inside vault.'"
          }
        ]
      }
    ]
  }
}
```

#### 2. Hooks — The Automatic Triggers

A **[[Hook]]([[Claude Code Hooks - Concept Note]])** is a rule that fires automatically when a specific lifecycle event occurs. You write hooks in `settings.json`; the harness executes them. Claude never sees the hook config — it only receives the *output* injected into its context.

The four hook types in Claude Code:

| Hook Type | When It Fires |
|---|---|
| **[[PreToolUse]]** | *Before* Claude uses any tool — most common, great for validation |
| **PostToolUse** | *After* a tool completes — good for logging or follow-up actions |
| **SessionStart** | When a new session begins — good for injecting project context |
| **Notification** | When Claude sends an update message |

#### 3. Skills — Packaged Harness Configurations

A **[[Skill]]** (like the ones in this vault's `SKILLS/` folder) is a pre-built bundle of harness knowledge + behaviors. When you call a skill (e.g. `/commit`), it injects expert instructions into Claude's context. The `/update-config` skill is specifically for modifying `settings.json` — it is the primary tool for harness engineering.

---

### Part 3 — With Harness vs. Without Harness

This is the most important comparison for understanding what the harness actually *does*:

| Situation | Without Harness Configuration | With Harness Engineering |
|---|---|---|
| **Starting a session** | Claude starts with zero context about your project | A `SessionStart` hook fires and injects your `Claude.md`, project rules, and any background knowledge |
| **Writing a file** | Claude writes whatever, wherever | A `PreToolUse` hook on `Write` validates the path is inside the vault first — and warns if not |
| **Recurring task** | You have to ask Claude every time | A scheduled hook or cron task runs automatically at set intervals |
| **Adding a new tool (plugin)** | You manually explain to Claude what it can do | The plugin registers hooks that inject its knowledge on every relevant action |
| **Automated behaviors** | You type "from now on, always do X" — and it forgets next session | You configure it in `settings.json` — the harness *always* does it |
| **Complex workflow** | Claude is a chatbot; you orchestrate every step | Claude is an agent; the harness orchestrates steps autonomously |

> **Key insight:** The harness is what transforms Claude from a *question-answering chatbot* into a *persistent, autonomous agent* that works with you across sessions.

---

## 🪄 Analogies & Stories

**Analogy 1 — The Stage Manager 🎭**
Claude is the actor on stage — talented, responsive, brilliant. But the *stage manager* (the harness) is behind the scenes calling every cue: "Lights up now. Microphone on. Props ready." The actor doesn't know when the cues happen — the stage manager controls the flow. Without the stage manager, the show would still *work*, but nothing would happen automatically.

**Analogy 2 — The OS Running an App 💻**
Think of Claude as a single app (like Safari or Word). The harness is the **operating system** running underneath it — allocating memory (tools), enforcing rules (permissions), and responding to events (hooks). Without the OS, the app can't do much. With a well-configured OS, the app can do far more than it could alone.

**Analogy 3 — Rules of a Video Game 🎮**
A game character (Claude) can run, jump, and attack. But the *game engine* (harness) decides what counts as a wall, what triggers a cutscene, and what plays a sound effect. The harness defines the world the character moves through.

---

## ❓ Common Student Questions

**Q: If the harness is so powerful, why can't I just talk to Claude and skip it?**
A: You can! For simple one-off tasks, conversation is enough. But whenever you want behaviors that *persist* across sessions — like "always check the Glossary before writing a new note," or "always validate file paths" — you need the harness. Memory through conversation resets; memory through `settings.json` is permanent.

**Q: Who writes the harness — me or Claude?**
A: You configure it, but Claude (via the `/update-config` skill) can *write the configuration for you*. This is meta: you use Claude Code to engineer the harness that controls Claude Code.

**Q: Can the harness run things without me asking?**
A: Yes — that's the whole point. Hooks fire automatically. The `SessionStart` hook runs the moment you open Claude Code, before you even type anything. `PreToolUse` hooks fire before every matched tool call, silently, every time.

**Q: Is the harness safe? What if a hook does something wrong?**
A: The harness only executes shell commands you define. Claude itself cannot modify `settings.json` without you explicitly asking it to (via a skill). The harness doesn't have unsupervised authority — you always write the hooks.

---

## ⚠️ Common Misconceptions

| Misconception | The Truth |
|---|---|
| "Hooks are written by Claude" | Hooks are written by *you* (or configured with Claude's help via `/update-config`). Claude cannot edit its own harness autonomously |
| "The harness only works with code projects" | It works in *any* project folder — including an Obsidian vault! Hooks can fire on note writes, vault searches, anything |
| "Automated behaviors = I lose control" | The opposite — harness engineering *increases* your control. You define the rules; Claude follows them |
| "Settings.json is only for advanced users" | Even a single hook (like auto-injecting your `Claude.md`) has massive impact. You don't need 50 rules to benefit |
| "The harness is Claude's 'brain'" | The harness is Claude's *environment*. Claude's reasoning happens inside the LLM. The harness shapes *what Claude perceives and can do* |

---

## 🔑 Key Terms & Definitions

- **[[Harness]]**: The runtime engine surrounding Claude Code that manages tools, fires hooks, enforces permissions, and runs automated behaviors — invisible but essential
- **[[Harness Engineering]]**: The practice of designing and configuring the harness (via `settings.json` and skills) to create persistent automated behaviors
- **[[Hook]]**: A rule in `settings.json` that fires automatically at a lifecycle event and runs a shell command — the primary building block of harness engineering
- **[[PreToolUse]]**: The most-used hook type — fires *before* any tool call. Use it to validate, warn, or inject context before Claude acts
- **[[PostToolUse]]**: A hook type that fires *after* a tool completes — useful for logging, follow-up checks, or chaining actions
- **[[SessionStart]]**: A hook type that fires when a Claude Code session begins — ideal for injecting project-level context automatically
- **[[Lifecycle Event]]**: A named moment in Claude Code's execution (session start, before/after tool use, notification) where hooks can attach
- **[[settings.json]]**: The Claude Code configuration file at `~/.claude/settings.json` — the rulebook for the harness
- **[[Skill]]**: A packaged set of harness knowledge and behaviors; invoked with `/skill-name` to inject expert context or run pre-built workflows
- **[[Matcher]]**: The filter inside a hook that decides which tool or event triggers that hook (e.g. `"matcher": "Write"` means only file-write events)

> 📖 See full glossary: [[Glossary]]

---

## 🖐️ Try It — Three Activities

### Activity A — Inspect Your Harness (5 min)
**Goal:** See what hooks (if any) are already configured.

1. Open a terminal
2. Run: `cat ~/.claude/settings.json`
3. Look for a `"hooks"` key — that's your current harness configuration
4. If it's empty or missing, your harness is unconfigured — no automatic behaviors yet

**Reflect:** *"What behaviors do you wish happened automatically in every Claude Code session?"*

---

### Activity B — Add Your First Hook (15 min)
**Goal:** Make Claude greet you with the vault name at the start of every session.

1. Open Claude Code in this vault
2. Type: `/update-config`
3. Ask Claude: *"Add a SessionStart hook that echoes 'Welcome to AI_Knowledge_Base — remember to update the Glossary for every new term!'"*
4. Start a new session and watch the message appear automatically

**Reflect:** *"How would you use a SessionStart hook to make Claude smarter about your projects?"*

---

### Activity C — The Before vs. After Experiment (20 min)
**Goal:** Experience the difference between a raw Claude session and a harness-configured one.

1. **Without hooks:** Open Claude Code and ask it to write a new note. Notice what it does by default.
2. **With a PreToolUse hook on Write:** Ask Claude to add a hook that checks if any Write operation would overwrite an existing file and warns you first.
3. Now try writing a note that already exists.
4. **Compare:** Did the harness catch something that the raw session missed?

---

## 🤝 Ethics Connection

Harness engineering raises the question of **control and autonomy**. When you configure a hook to fire automatically — without a human approving each action — you are giving a machine a kind of standing permission. This is powerful and useful, but also means errors can repeat automatically before you notice them.

Good harness engineering practice includes:
- **Starting small** — add one hook at a time and test it
- **Staying transparent** — know what every hook in your `settings.json` does
- **Reviewing periodically** — delete hooks that are outdated or no longer needed
- **Keeping humans in the loop** for anything irreversible (deleting files, sending messages, publishing content)

> *"Automation amplifies your intentions — good ones and bad ones alike. Engineer thoughtfully."*

> 📎 See also: [[AI Ethics - Concept Note]] *(coming soon)*

---

## 📚 Want to Learn More?

- [Claude Code documentation — Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) — *Official reference for all hook types and settings.json config*
- [Claude Code documentation — Settings](https://docs.anthropic.com/en/docs/claude-code/settings) — *Full settings.json reference*
- [[Claude Code Hooks - Concept Note]] — *Deep dive into hooks already in this vault*
- [[What is Claude Code - Concept Note]] — *Start here if you're new to Claude Code*

---

## 🔗 Related Notes

| Note | Relationship |
|---|---|
| [[What is Claude Code - Concept Note]] | Foundation — understand Claude Code before the harness |
| [[Claude Code Hooks - Concept Note]] | Deep dive into the most important harness building block |
| [[What is Obsidian - Concept Note]] | The environment the harness operates inside for this vault |

---

*Created: 2026-04-14 | Level: High-Intro → High-Advanced | Topic: Claude Applications / Tools*
