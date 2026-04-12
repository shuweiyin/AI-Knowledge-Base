---
title: "AI Learning Habits"
skill: project
type: project
tags: [project, habits, daily-notes, graph-view, prompt-craft, backup, intermediate]
level: all
topic: claude-applications
status: published
created: 2026-04-12
---

# AI Learning Habits — Project

## 🧪 Project Brief

| Field | Details |
|-------|---------|
| **Topic** | Building habits that make your knowledge base grow stronger over time |
| **Project Title** | "The Long Game" — AI Learning Habits |
| **Grade Level** | `[x] All Levels` |
| **Duration** | Ongoing — 4-week habit-building project |
| **Group Size** | `[x] Solo` (personal habits are personal!) |
| **Difficulty** | `[x] Beginner → Intermediate` |
| **Prerequisites** | [[Build Your Own Wiki - Project]] (your vault should already exist) |

---

## 🎯 Project Goal

**What students will build:**
A set of 5 recurring habits that make their knowledge base compound over time — not just a vault, but a *thinking system* that gets smarter every week.

**What students will learn:**
- How to use Daily Notes to document learning and create a timeline of growth
- How to use Graph View weekly to find and fix knowledge gaps
- How to write better prompts to Claude (prompt crafting as a skill)
- How to back up and protect their vault (version history, cloud sync)
- How to share or export notes for others to use

> 💡 *A knowledge base you don't maintain slowly dies. These habits keep it alive.*

---

## 🛠️ Required Tools & Materials

| Tool | Purpose | Cost |
|------|---------|------|
| Obsidian | Your vault | Free |
| [[Claudian plugin]] | AI inside Obsidian | Free |
| Obsidian Daily Notes plugin | Built-in — enable in Core Plugins | Free |
| iCloud / Dropbox / Git | Backup & sync | Free (basic) |

---

## 📦 The 5 Habits

> This project is structured differently from the others — instead of a one-time build, you adopt one habit per week over 4 weeks (Habits 4 & 5 combine in Week 4).

---

### Habit 1 — Daily Notes: The 5-Minute Learning Log *(Week 1)*

**What it is:**
A daily note is a note automatically named with today's date (e.g., `2026-04-12 Daily`). Every day you study AI, you write 5 minutes of notes in it. Over time, this creates a timeline of your learning journey.

**Setup:**
1. In Obsidian, go to **Settings → Core Plugins → Daily Notes** → Enable
2. Set the folder to `🎯 Daily Notes/` and the format to `YYYY-MM-DD Daily`
3. Create a Daily Notes template (in your `📋 TEMPLATES/` folder) named `Daily Note Template`:

```markdown
---
title: "{{date}} Daily Note"
type: daily-note
tags: [daily, learning-log]
date: {{date}}
---

# 📅 {{date}} — Learning Log

## What I studied today
- 

## What I understood well
- 

## What confused me
- 

## New wikilinks I added
- [[  ]]

## One question I want to ask Claude
> 

## Claude's response summary
> 
```

4. Set this as your Daily Notes template in settings
5. For the next 7 days, open your daily note at the start or end of each study session

**Why this habit matters:**
When you look back at 30 daily notes, you'll see your own thinking evolve. Confusion becomes understanding. Questions get answered. It's the most honest record of how you actually learn.

**Weekly check:** Are there any questions from daily notes that you never followed up on? Pick one and research it now.

---

### Habit 2 — Weekly Graph Review *(Week 2)*

**What it is:**
Once a week, spend 10 minutes in Graph View looking for problems in your knowledge web.

**The 3 things to look for:**

| Problem | What It Looks Like | Fix |
|---------|-------------------|-----|
| **Orphan notes** | A dot with no connecting lines | Add at least 1 wikilink to connect it |
| **Over-linked hub** | One note with 10+ connections, all others sparse | Create MOC notes to distribute links |
| **Missing notes** | A wikilink that appears red (note doesn't exist yet) | Create the stub note and fill it in |

**Steps:**
1. Open Graph View (left sidebar icon)
2. Enable **Orphans** in the graph filters to make solo nodes visible
3. Identify 1–3 orphan notes and add wikilinks
4. Look for any **red/broken links** in your notes (hover over them in the editor)
5. In your daily note, write: *"Graph Review: I fixed [X]. I noticed [Y]. I want to add [Z]."*

**The habit:** Do this every Sunday (or pick a consistent day). 10 minutes, no more.

**Why this habit matters:**
A knowledge base with broken links and orphan notes is like a library where half the books are on the wrong shelf. Regular graph reviews keep your vault navigable and honest.

---

### Habit 3 — Prompt Crafting: Ask Claude Better Questions *(Week 3)*

**What it is:**
Writing good prompts to Claude is a skill — like asking a good question in class. Vague prompts get vague answers. Specific prompts get useful answers.

**The Prompt Craft Framework (use this every time):**

```
[ROLE] You are a [who Claude should be — e.g., "high school AI teacher"]
[TASK] [What you want — be specific]
[CONTEXT] [What Claude needs to know — your level, your topic, your vault]
[FORMAT] [How you want the answer — bullet points, a table, 100 words, etc.]
[CONSTRAINT] [What to avoid — e.g., "no jargon", "don't write it for me, guide me"]
```

**Example — Bad prompt:**
> *"Explain neural networks"*

**Example — Good prompt:**
> *"You are a patient high school teacher. Explain how neural networks learn using a single, memorable analogy that a 14-year-old would find funny or surprising. Keep it under 100 words. Avoid math entirely."*

**Practice activity:**
1. Pick any concept in your vault you don't fully understand
2. Write a bad prompt → read Claude's response
3. Rewrite using the Prompt Craft Framework → read Claude's response
4. Compare the two answers — note the difference in your daily note
5. Save your best prompts in a note called `My Best Prompts` inside `06-Resources/`

**The habit:** Before every Claude session, write your prompt in a draft first. Read it once. Is it specific? Does it say what format you want?

**Why this habit matters:**
Prompt crafting is one of the most valuable AI skills you can develop right now. Every company working with AI needs people who can direct AI effectively. The habit starts here.

---

### Habit 4 — Backup & Sync: Never Lose Your Work *(Week 4, Part A)*

**What it is:**
Your vault is just files on your computer. If your computer breaks, your knowledge base could be gone. Set up a backup system now.

**Option A — iCloud / Dropbox (easiest):**
1. Move your entire vault folder into your iCloud Drive or Dropbox folder
2. Obsidian will still work normally — it just reads from that location now
3. Your vault automatically syncs to the cloud and your other devices

**Option B — Git + GitHub (most powerful, free):**
1. Install [Git](https://git-scm.com) (free)
2. Create a free [GitHub](https://github.com) account
3. Install the **Obsidian Git** community plugin
4. Set it to auto-commit every 30 minutes
5. Your vault now has a full version history — you can see every change ever made

**Option C — Obsidian Sync (official, paid):**
- $4/month — syncs between all your devices with end-to-end encryption
- Worth it if you study on multiple devices

**The habit (Option A or B):**
- Check once a week that your backup is working (look at iCloud or GitHub)
- Once a month, open a backed-up old version and see how much your vault has grown

**Why this habit matters:**
You're building something valuable. Protect it. Also — version history lets you see your own learning progress, which is one of the most motivating things you can do.

---

### Habit 5 — Share & Export: Turn Notes into Value *(Week 4, Part B)*

**What it is:**
Your knowledge base shouldn't just live on your hard drive. Sharing forces you to write clearly, and your notes might help someone else.

**3 ways to share from Obsidian:**

| Method | What It Does | Best For |
|--------|-------------|----------|
| **Export to PDF** | Print any note as a PDF | Sharing a lesson plan or study guide |
| **Copy as Markdown** | Share the raw `.md` file | Other Obsidian users |
| **Obsidian Publish** | Create a public website from your vault | Sharing your entire wiki online |

**Practice activity:**
1. Pick your best-written Concept Note
2. Export it as PDF (File → Export to PDF)
3. Share it with a classmate or family member who doesn't know about AI
4. Ask them: *"After reading this, could you explain the concept to someone else?"*
5. Revise the note based on their feedback
6. Write in your daily note: *"I shared [note name]. The feedback was: [what they said]. I changed: [what you fixed]."*

**The habit:** Once per month, share one note with someone outside your class. Their confusion will teach you what you don't yet know how to explain.

**Why this habit matters:**
The best test of understanding is teaching. If you can explain it simply enough for someone else to understand, you truly know it. This is the final loop that closes the learning cycle.

---

## ⭐ 4-Week Progress Tracker

> Check off each habit as you establish it:

| Week | Habit | Mon | Tue | Wed | Thu | Fri | Done? |
|------|-------|-----|-----|-----|-----|-----|-------|
| 1 | Daily Notes | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 2 | Graph Review (weekly) | — | — | — | — | ☐ | ☐ |
| 3 | Prompt Crafting | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 4A | Backup set up | — | — | — | — | ☐ | ☐ |
| 4B | Share one note | — | — | — | — | ☐ | ☐ |

---

## ⭐ Grading Rubric

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|----------------|----------------|
| **Daily Notes** | 10+ daily notes with all sections filled | 7–9 notes | 4–6 notes | Fewer than 4 |
| **Graph Reviews** | 3+ weekly reviews documented; orphans fixed | 2 reviews | 1 review | None |
| **Prompt Crafting** | Comparison documented; visible improvement in prompt quality | Good prompt examples saved | Some prompts saved | No evidence of practice |
| **Backup** | Working backup + can explain the method | Backup set up | Attempted | No backup |
| **Sharing** | Note shared + feedback received + note revised | Shared but no revision | Attempted | Not done |

**Total: \_\_ / 20**

---

## 🚀 Extension Challenges

- **Level Up 1:** Set up the **Obsidian Git** plugin and share your vault as a public GitHub repository — your entire learning journey becomes an open portfolio
- **Level Up 2:** Write a "meta-reflection" note at the end of Month 1: *"How has my thinking about AI changed in the last 4 weeks? What does my graph look like compared to Week 1?"*
- **Level Up 3:** Teach one of these 5 habits to a classmate who hasn't started yet. Document the teaching session in your daily note.

---

## 🤝 Ethics Checkpoint

- When you share your notes (Habit 5), how do you handle content that Claude helped write? Should you credit the AI?
- Your daily notes might contain personal reflections — how do you decide what to keep private vs. share in a public vault?
- **Digital dependency:** If Obsidian disappeared tomorrow and you couldn't access your vault, how much of your AI knowledge could you reconstruct from memory? What does that tell you about the depth of your learning?

---

## 🔗 Related Notes

- [[Build Your Own Wiki - Project]]
- [[Obsidian Best Practices - Project]]
- [[Templates and Skills Practice - Project]]
- [[What is Obsidian - Concept Note]]
- [[What is Claude Code - Concept Note]]
- [[Claudian plugin]]
- [[🎯 Daily Notes]]
