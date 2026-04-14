---
title: "Obsidian Best Practices"
skill: project
type: project
tags: [project, obsidian, best-practices, claude-md, file-structure, intermediate]
level: all
topic: claude-applications
status: published
created: 2026-04-12
---

# Obsidian Best Practices — Project

## 🧪 Project Brief

| Field | Details |
|-------|---------|
| **Topic** | Professional Obsidian habits for a lasting knowledge base |
| **Project Title** | "Build It Right" — Obsidian Best Practices |
| **Grade Level** | `[x] All Levels` |
| **Duration** | 2 class periods (or ~2 hours) |
| **Group Size** | `[x] Solo` |
| **Difficulty** | `[x] Beginner → Intermediate` |
| **Prerequisites** | [[Build Your Own Wiki - Project]] (recommended first) |

---

## 🎯 Project Goal

**What students will build:**
A well-structured, professionally organized Obsidian vault with a meaningful `Claude.md`, consistent folder hierarchy, proper frontmatter on every note, and a working MOC (Map of Content).

**What students will learn:**
- Why structure matters for a knowledge base that lasts
- How to write a `Claude.md` that makes AI help more effective
- How to design a folder system that scales as your vault grows
- How to use frontmatter, tags, and naming conventions consistently
- How to create MOC notes that connect your whole knowledge base

---

## 🛠️ Required Tools & Materials

| Tool | Purpose | Cost |
|------|---------|------|
| Obsidian | Your vault | Free |
| [[Claudian plugin]] | AI review of your structure | Free |
| This vault as a reference | Example of best practices in action | Free |

---

## 📦 Step-by-Step Instructions

### Step 1 — Write a Powerful `Claude.md` *(~20 minutes)*

**What to do:**
Your `Claude.md` is the most important file in your vault. It tells Claude everything it needs to know about you and your goals — so every response it gives is tailored to you.

A great `Claude.md` answers these questions:

```markdown
# Claude.md

## Who I Am
[Your name, grade level, school subject context]

## My Learning Goal
[What you want to learn or build with this vault]

## My Audience
[Who this knowledge base is for — yourself? classmates? a teacher?]

## How I Want Claude to Help Me
[e.g., "Explain things simply", "Use analogies", "Don't write for me — guide me"]

## Topics I'm Studying
[List 5–10 topics your vault will cover]

## What NOT to Do
[e.g., "Don't use too much jargon", "Don't write entire essays for me"]
```

**Steps:**
1. Create or open `Claude.md` in your vault root
2. Fill in each section above honestly — the more specific, the better
3. Ask Claude via the [[Claudian plugin]]: *"Read my Claude.md. Does it give you enough context to help me effectively? What's missing?"*
4. Revise based on Claude's feedback

**Expected result:** A Claude.md that Claude can use to give you personalized, relevant help on the first try.

**Why this matters:** Without `Claude.md`, Claude treats every conversation as if it's the first time you've met. With a good `Claude.md`, Claude knows your level, your goals, and your preferences before you even ask a question.

---

### Step 2 — Design Your Folder Structure *(~25 minutes)*

**What to do:**
A good folder structure should feel obvious — anyone looking at your vault should understand it in 30 seconds.

**The 3 main approaches:**

| Approach | Structure | Best For |
|----------|-----------|----------|
| **By Topic** | `AI-Fundamentals/`, `Ethics/`, `Projects/` | Deep study of specific subjects |
| **By Type** | `Concepts/`, `Lessons/`, `Projects/`, `Resources/` | Mixed content, using templates |
| **Hybrid** (recommended) | Topic folders containing typed sub-notes | Large vaults with many topics |

**This vault uses the hybrid approach** — look at the current structure as your reference model:
```
01-AI-Fundamentals/       ← topic
02-Programming-Basics/    ← topic  
03-Applications/   ← topic (with typed notes inside)
04-FullStack-App/         ← topic  
05-Projects/              ← type
06-Resources/             ← type
  📋 TEMPLATES/           ← sub-type
  📖 REFERENCE/           ← sub-type
```

**Steps:**
1. Sketch your ideal folder structure on paper first (don't open Obsidian yet)
2. Ask yourself: *"If I have 100 notes in 6 months, will this still make sense?"*
3. Create the folders in Obsidian
4. Move any existing notes into the right folders
5. Ask Claude: *"Here is my folder structure: [paste it]. Does it make sense for an AI learning vault? What would you change?"*

**Expected result:** A clear folder hierarchy you can explain to a classmate in one sentence per folder.

**Tip:** *Use numbers at the start of folder names (`01-`, `02-`) to force alphabetical ordering — they'll always appear in the sequence you intend.*

---

### Step 3 — Apply Consistent Frontmatter *(~20 minutes)*

**What to do:**
Frontmatter is the YAML metadata block at the top of every note. Used consistently, it lets you filter, sort, and search your notes powerfully.

**Standard frontmatter for this vault:**
```yaml
---
title: "Full Note Title"
type: concept-note | lesson-plan | project | quiz | discussion | resource
tags: [AI, topic-name, level-name]
level: middle | high-intro | high-advanced | all
status: draft | review | published
created: YYYY-MM-DD
---
```

**Steps:**
1. Open 3 existing notes in your vault
2. Add proper frontmatter to each (use the template above)
3. Use Obsidian's **Properties** panel (click the `{ }` icon) to verify fields are correct
4. Create a saved search or filter to show all notes with `status: draft` — these are your "to-do" notes
5. Ask Claude: *"Look at this note's frontmatter. Is anything missing or inconsistent?"*

**Expected result:** At least 5 notes with complete, consistent frontmatter.

**Common mistake:** Forgetting `created` date → **Fix:** Always add it the day you create the note. Dates become invaluable when you look back at 100 notes.

---

### Step 4 — Naming Conventions *(~15 minutes)*

**What to do:**
Consistent naming makes links predictable and the vault searchable.

**Rules for this vault:**

| Rule                                | Good ✅                           | Bad ❌                   |
| ----------------------------------- | -------------------------------- | ----------------------- |
| Use hyphens, not spaces             | `Machine-Learning`               | `Machine Learning`      |
| Include type suffix for typed notes | `Neural Networks - Concept Note` | `Neural Networks Notes` |
| Date-prefix daily notes             | `2026-04-12 Daily`               | `Today's notes`         |
| Capitalize topic words              | `AI Ethics`                      | `ai ethics`             |
| No special characters               | `Prompt-Engineering`             | `Prompt_Engineering!`   |

**Steps:**
1. Review 5 notes in your vault — do their names follow the rules above?
2. Rename any that don't (right-click → Rename in Obsidian — links update automatically!)
3. Apply the `{{TOPIC}} - Type` naming pattern (from [[00-SKILLS-INDEX]]) to any typed notes
4. Ask Claude: *"Here are my 10 note names: [list them]. Do they follow a consistent naming convention?"*

**Expected result:** All notes follow the naming rules. Wikilinks still work after renaming (Obsidian handles this automatically).

---

### Step 5 — Build a MOC (Map of Content) *(~25 minutes)*

**What to do:**
A MOC is a note that acts as a table of contents for a topic — it links to all related notes in one place, like a hub in your web.

**Example MOC structure:**
```markdown
---
title: "MOC — Machine Learning"
type: moc
tags: [MOC, machine-learning]
---

# 🗺️ Map of Content — Machine Learning

## Concept Notes
- [[Machine Learning - Concept Note]]
- [[Supervised Learning - Concept Note]]
- [[Neural Networks - Concept Note]]

## Lesson Plans
- [[Machine Learning - Lesson Plan]]

## Projects
- [[Machine Learning - Project]]

## Discussions & Quizzes
- [[Machine Learning - Discussion]]
- [[Machine Learning - Quiz]]

## External Resources
- [[External-Resources]]
```

**Steps:**
1. Pick your most developed topic (the one with the most notes)
2. Create a new note named `MOC — [Topic Name]`
3. Add every related note as a wikilink, organized by type
4. Open Graph View — your MOC should appear as the most-connected node for that topic
5. Add a link to your MOC from your main `📄 MOC-Main-Index.md`

**Expected result:** One complete MOC note that links to at least 4 other notes. The graph shows it as a hub.

---

## ⭐ Grading Rubric

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|----------------|----------------|
| **Claude.md** | Specific, personal, covers all 6 sections | Covers most sections | Brief or vague | Missing or empty |
| **Folder Structure** | Logical, scalable, explained clearly | Mostly logical | Some structure | No clear structure |
| **Frontmatter** | 5+ notes with complete, consistent frontmatter | 3–4 notes with frontmatter | 1–2 notes | None |
| **Naming Conventions** | All notes follow rules | Most follow rules | Inconsistent | No conventions applied |
| **MOC** | Complete hub with 4+ links, appears in graph | 3 links, in graph | Created but few links | Missing |

**Total: \_\_ / 20**

---

## 🚀 Extension Challenges

- **Level Up 1:** Create a MOC for *every* major topic in your vault, then link all MOCs from `📄 MOC-Main-Index.md`
- **Level Up 2:** Set up a **Daily Notes** template (see [[AI Learning Habits - Project]]) so every study session is automatically documented
- **Level Up 3:** Use the Dataview plugin to create an auto-updating table of all `status: draft` notes — a live to-do list for your vault

---

## 🤝 Ethics Checkpoint

- Your `Claude.md` tells Claude about you — what level of personal detail is appropriate to share with an AI?
- If two students have identical folder structures but very different `Claude.md` files, whose vault will be more useful and why?
- What would happen to your knowledge base if Obsidian shut down tomorrow? (Think: data ownership, file formats, backups)

---

## 🔗 Related Notes

- [[Build Your Own Wiki - Project]]
- [[Templates and Skills Practice - Project]]
- [[AI Learning Habits - Project]]
- [[What is Obsidian - Concept Note]]
- [[Claudian plugin]]
- [[00-SKILLS-INDEX]]
- [[📄 MOC-Main-Index]]
