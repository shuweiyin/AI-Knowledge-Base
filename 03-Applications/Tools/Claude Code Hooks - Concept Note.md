---
title: "Claude Code Hooks — What They Are and How to Use Them in Skills"
skill: concept-note
type: concept-note
tags: [claude-code, hooks, skills, automation, settings, lifecycle, plugin, high-intro]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-14
---

# Claude Code Hooks — Concept Note

## ⚡ Core Concept (One Sentence)

> A **hook** in Claude Code is an automatic trigger — a piece of code (or shell command) that fires on its own at a specific moment in Claude's session lifecycle, without you having to ask for it.

---

## 🤔 Why It Matters

Normally, Claude Code does exactly what *you* tell it to do, step by step. But some tasks should happen *every single time* — automatically — without you having to remember to ask. Hooks solve this. They are the system that lets Claude Code (and the tools built on top of it, called **[[Skills]]**) behave proactively. Understanding hooks is the key to understanding how Skills like the Vercel Plugin feel "magical" — they're not guessing what you need, they're using hooks to watch what you do and respond in real time.

---

## 📖 Detailed Explanation

### Part 1 — What Is a "Lifecycle"?

Before understanding hooks, you need to understand **lifecycle** — the predictable series of stages every Claude Code session goes through:

```
1. Session Starts  →  2. Claude Reads a File  →  3. Claude Uses a Tool
       ↓                        ↓                         ↓
4. Claude Writes a File  →  5. Claude Responds  →  6. Session Ends
```

Every one of these stages is a **lifecycle event**. A hook lets you say:
> *"Every time lifecycle event X happens, automatically run Y."*

This is exactly how an automatic door works — the door doesn't ask you to press a button. It uses a motion sensor (the hook) that fires every time it detects a person walking close (the lifecycle event).

---

### Part 2 — The Six Hook Types in Claude Code

Claude Code defines six lifecycle moments where hooks can fire:

| Hook Name | When It Fires | Common Use |
|-----------|--------------|------------|
| `PreToolUse` | **Before** Claude uses any tool (read, write, search…) | Validate or inject context before an action |
| `PostToolUse` | **After** Claude uses any tool | Log what happened, run follow-up checks |
| `Notification` | When Claude sends a notification or alert | Forward alerts to another system |
| `Stop` | When Claude finishes responding | Save output, run cleanup |
| `PreCompact` | Before Claude compresses old context | Archive important context before it's lost |
| `SubagentStop` | When a sub-agent finishes its task | Collect results from a background agent |

> 💡 Think of these hook names as the "motion sensors" placed at different spots along the hallway. You choose which sensor to use based on *where* you want to intercept the action.

---

### Part 3 — Where Hooks Live: `settings.json`

Hooks are configured in Claude Code's **`settings.json`** file — a JSON configuration file that controls Claude Code's behavior. This file lives in your Claude Code installation folder at:

```
~/.claude/settings.json
```

A hook entry looks like this:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'About to write a file!'"
          }
        ]
      }
    ]
  }
}
```

**Breaking this down piece by piece:**

| Part | What It Means |
|------|--------------|
| `"PreToolUse"` | *Which lifecycle event* triggers this hook (before a tool is used) |
| `"matcher": "Write"` | *Which tool* to watch for — only fires when Claude uses the Write tool |
| `"type": "command"` | *What kind of hook* — a shell command to run |
| `"command": "echo ..."` | *What to actually run* when the hook fires |

---

### Part 4 — How Skills Use Hooks

A **[[Skill]]** in Claude Code is a pre-packaged set of instructions, templates, and behaviors that can be installed to give Claude specialized knowledge. Skills are stored in your vault or project folder as Markdown files (you can see them in the `SKILLS/` folder of this vault).

The most powerful skills use hooks to behave automatically. Here's how that works:

#### 🔁 The Skill + Hook Loop

```
You work on a file
        ↓
Hook fires: "PreToolUse" on file edit
        ↓
Hook runs a command: reads the Skill's .md file
        ↓
Skill content is injected into Claude's context
        ↓
Claude now has expert knowledge — without you asking
```

**Real example from the [[Claude Code Vercel Plugin - Concept Note]]:**

When you edit `next.config.ts`, the Vercel Plugin's `PreToolUse` hook detects it, matches the file path against a pattern, and injects the `nextjs` skill automatically. Claude immediately knows the latest Next.js + Vercel best practices — even though you never said "use the Vercel skill."

#### 🔧 A Simple Skill Hook in Practice

Here's a minimal example: a skill that reminds Claude to check the Glossary every time it writes a Markdown file.

**Step 1 — Create the skill file** (`SKILLS/glossary-reminder.md`):
```markdown
# Glossary Reminder Skill
Whenever you write a new concept term in a Markdown note,
always add it to [[Glossary]] with a student-friendly definition.
Format: **Term** — Definition. → [[Source Note]]
```

**Step 2 — Add a hook in `settings.json`**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "cat ~/.claude/skills/glossary-reminder.md"
          }
        ]
      }
    ]
  }
}
```

Now, every time Claude writes a `.md` file, it first reads the glossary reminder. The behavior is enforced *automatically* — no need to say "remember the glossary rule" every session.

---

### Part 5 — Matcher Patterns: Choosing What to Watch

The `matcher` field controls *which tools* the hook watches. You can be broad or specific:

| Matcher | What It Watches |
|---------|----------------|
| `"Write"` | Only the Write tool (creating/overwriting files) |
| `"Edit"` | Only the Edit tool (modifying files) |
| `"Bash"` | Any Bash/terminal command Claude runs |
| `"Read"` | Any file Claude reads |
| `""` (empty) | All tools — fires on every single tool use |

You can also use **glob patterns** (wildcard file path patterns) in more advanced setups to match specific file types or folder paths.

---

### Part 6 — Hook Output: What Claude Sees

When a hook's command runs, Claude Code captures the **standard output** (the text printed to the terminal) and injects it into Claude's context as additional information. This is the mechanism that makes skill injection work:

```
Hook command runs → prints skill text → Claude reads that text → Claude knows the skill
```

Think of it like a sticky note that automatically appears on Claude's desk every time it opens a certain drawer. The sticky note (skill content) was pre-written; the hook is the mechanism that puts it there at the right moment.

---

## 🪄 Analogies & Stories

**Analogy 1 — The Automatic Coffee Machine ☕**
You don't tell your coffee machine "start brewing" every morning. You set a *timer* (the hook) that fires at 7:00 AM (the lifecycle event) and starts the machine automatically. Claude hooks are the same: you set them once, and they run every time the right moment arrives.

**Analogy 2 — The Basketball Coach's Playbook 📋**
Imagine a basketball coach who tapes a different reminder card to the scoreboard depending on the quarter. At the start of Q3, a card appears: "Switch to zone defense." The players don't need to ask — the coach (the hook) placed the right reminder (the skill) at exactly the right moment (lifecycle event). Claude hooks work the same way.

**Analogy 3 — IFTTT ("If This, Then That") 🔁**
You might know IFTTT — the automation service that says "if it rains, send me a text." Hooks are Claude Code's version of IFTTT: `if PreToolUse matches Write, then inject this skill content.` Same pattern, same power.

---

## ❓ Common Student Questions

**Q: Do I need to write hooks to use Claude Code?**
A: No! Most users never touch hooks. They are an **advanced feature** used by plugin developers and teachers who want to enforce rules automatically. You can use Claude Code perfectly well without them.

**Q: If hooks run automatically, can they do dangerous things?**
A: Hooks run shell commands — which means a poorly written hook *could* do something unexpected. This is why you should only install plugins and hooks from sources you trust. Always review `settings.json` if something feels off.

**Q: Can a hook make Claude do something I didn't ask for?**
A: Hooks inject *context* (text) into Claude's awareness, but Claude still makes its own decisions about what to do. A hook can't force Claude to delete your files — it can only add information to Claude's context. Think of hooks as giving Claude a briefing, not giving it orders.

**Q: What's the difference between a hook and a skill?**
A: They work together but are different things. A **Skill** is the *knowledge content* — a Markdown file with instructions or expertise. A **Hook** is the *delivery mechanism* — the automatic trigger that decides *when* to show Claude that skill. Skills without hooks must be invoked manually; skills with hooks fire automatically.

---

## ⚠️ Common Misconceptions

| Misconception | The Truth |
|--------------|-----------|
| "Hooks are the same as skills" | Hooks *deliver* skills — they are the trigger mechanism, not the content |
| "You need hooks to use skills" | You can read and use skill files manually by referencing them in your prompt |
| "Hooks run inside Claude's brain" | Hooks run as *shell commands on your computer* — Claude reads their output as context |
| "Once a hook fires, Claude must obey it" | Hooks inject context; Claude still exercises judgment about what to do |

---

## 🔑 Key Terms & Definitions

- **[[Hook]]** — An automatic trigger in Claude Code that fires at a specific lifecycle moment and runs a shell command. The output of that command is injected into Claude's context.
- **[[Lifecycle Event]]** — A predictable stage in a Claude Code session (e.g., "before writing a file," "after using a tool") where hooks can attach.
- **[[Skill]]** — A Markdown file containing specialized knowledge, instructions, or rules that can be injected into Claude's context manually or automatically via hooks.
- **[[settings.json]]** — The Claude Code configuration file (stored at `~/.claude/settings.json`) where hooks and other behaviors are defined.
- **[[Matcher]]** — The pattern inside a hook definition that determines which tool or event triggers the hook.
- **[[Skill Injection]]** — The process of automatically adding skill content to Claude's context when a matching lifecycle event fires.
- **[[PreToolUse]]** — The most commonly used hook type — fires before Claude uses any tool, giving you a chance to inject context first.

> 📖 See full glossary: [[Glossary]]

---

## 🖐️ Try It — Quick Activity

**Activity:** Explore How a Hook Shapes Claude's Behavior
**Time:** 10–15 minutes
**Level:** High School — Intro
**Materials:** Claude Code or Claudian plugin, any text editor

**Part A — Observe Hook Behavior (No Setup Required)**
1. Open this vault in Claude Code or the Claudian plugin
2. Ask Claude: *"What should I do every time I introduce a new technical term in a note?"*
3. Claude should reference the Glossary rule — this behavior is shaped by the `CLAUDE.md` system prompt, which works exactly like a session-start hook
4. **Reflection:** *"Where did Claude learn this rule? Did you tell it in this conversation?"*

**Part B — Design a Hook (No Coding Required)**
Think of a repetitive task you'd want Claude to handle automatically. Complete this sentence:

> "Every time Claude **[does what]**, it should automatically **[do what]**."

Examples:
- *"Every time Claude writes a Python file, it should remind me to add comments."*
- *"Every time Claude starts a session in my project, it should tell me today's top priority."*

Then describe what the hook would look like: What lifecycle event? What matcher? What command would it run?

**Part C — Advanced Challenge (Optional)**
If you have Claude Code installed with terminal access, try reading your `~/.claude/settings.json` file. Does it contain any hooks already? Compare what you see to the examples in this note.

---

## 🤝 Ethics Connection

Hooks introduce an interesting question about **transparency and control**. If a plugin automatically injects instructions into Claude's context via hooks — without you seeing it happen — how do you know what Claude has been told? You might think you're getting Claude's unbiased response, but a hook could be shaping that response with instructions from a plugin developer.

This is why **open-source plugins** matter: if you can read the hook's source code, you can see exactly what it injects. Closed, black-box plugins are harder to trust. When working with AI tools, always ask: *"Is this tool's behavior transparent to me?"*

> 📎 See also: [[AI Ethics - Concept Note]] *(coming soon)*

---

## 📚 Want to Learn More?

- [Claude Code Hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) — *Official reference for all hook types and configuration*
- [Claude Code settings.json reference](https://docs.anthropic.com/en/docs/claude-code/settings) — *Full list of configurable options*
- [[Claude Code Vercel Plugin - Concept Note]] — *A real-world example of hooks + skills working together*
- [[What is Claude Code - Concept Note]] — *Start here if you're new to Claude Code*

---

## 🔗 Related Notes

| Note | Connection |
|------|-----------|
| [[What is Claude Code - Concept Note]] | Foundation — understand Claude Code before hooks |
| [[Claude Code Vercel Plugin - Concept Note]] | Real-world example: how a plugin uses all four hook types |
| [[Glossary]] | Definitions for every bold term in this note |

---

*Created: 2026-04-14 | Level: High School — Intro | Topic: Claude Applications*
