# Claude.md — Project Context & AI Assistant Guide

> This file tells Claude (and any AI assistant) exactly what this vault is, who it serves, and how to help. Keep it updated as the project evolves.

---

## 🎯 Project Mission

**Goal:** Build a structured, beginner-friendly knowledge base for teaching **Artificial Intelligence concepts** to **middle school and high school students** (ages 11–18).

This vault is the single source of truth for curriculum notes, lesson plans, code examples, project ideas, and teaching resources. Everything written here should be:

- **Age-appropriate** — clear language, relatable analogies, no unnecessary jargon
- **Engaging** — hands-on examples, real-world connections, interactive projects
- **Accurate** — technically correct, even if simplified
- **Progressive** — concepts build on each other from beginner → intermediate → advanced

---

## 👩‍🎓 Target Audience

| Level | Age Range | Prior Knowledge Assumed |
|-------|-----------|------------------------|
| Middle School | 11–14 | Basic computer use, curiosity |
| High School (Intro) | 14–16 | Some math (algebra), basic logic |
| High School (Advanced) | 16–18 | Algebra II, optional Python basics |

When writing notes or lessons, always **specify which level** a piece of content targets.

---

## 🗂️ Vault Structure

```
AI_Knowledge_Base/
├── 01-AI-Fundamentals/       ← Core AI concepts (what is AI, ML, neural networks)
├── 02-Programming-Basics/    ← Python & coding foundations for AI
├── 03-Claude-Applications/   ← Using Claude & LLMs in real projects
├── 04-Google-AI-Quests/      ← Google AI learning activities & quests
├── 05-Projects/              ← Student project templates & examples
├── 06-Resources/             ← Links, books, videos, tools, datasets
├── 🎯 Daily Notes/           ← Teaching journal, daily reflections
├── 📄 MOC-Main-Index.md      ← Master table of contents
├── 📄 MOC-Quick-Reference.md ← Quick-lookup cheat sheets
└── Claude.md                 ← This file (AI assistant context)
```

### Folder Purposes

- **01-AI-Fundamentals**: Conceptual lessons — what AI is, types of AI (narrow vs. general), machine learning, supervised/unsupervised learning, neural networks, ethics of AI.
- **02-Programming-Basics**: Python tutorials, Jupyter notebook walkthroughs, coding exercises designed for first-time programmers.
- **03-Claude-Applications**: Prompt engineering, using Claude API, building simple chatbots, real classroom use cases for LLMs.
- **04-Google-AI-Quests**: Notes and activities from Google's AI learning programs (Teachable Machine, ML for Kids, etc.).
- **05-Projects**: Guided project briefs students can follow — from simple (image classifier) to complex (sentiment analyzer).
- **06-Resources**: Curated external links, datasets, YouTube channels, books, and tools vetted for student use.

---

## 📝 Note-Writing Standards

### Frontmatter Template
Every note should start with:
```yaml
---
title: "Note Title"
level: middle | high-intro | high-advanced | all
topic: ai-fundamentals | programming | claude | google-ai | project | resource
status: draft | review | published
created: YYYY-MM-DD
tags: [ai, machine-learning, python, ...]
---
```

### Content Guidelines
1. **Start with a hook** — a real-world question or surprising fact to grab attention.
2. **Use analogies** — compare AI concepts to things students already know (e.g., "Training a model is like studying for a test").
3. **Include visuals** — diagrams, flowcharts, or links to images where possible.
4. **Add a "Try It" section** — a small hands-on activity at the end of every concept note.
5. **Link related notes** — use `[[wikilinks]]` to connect concepts across the vault.
6. **Keep paragraphs short** — aim for 3–5 sentences max per paragraph.

---

## 🤖 How Claude Should Help in This Vault

When assisting with this project, Claude should:

### Content Creation
- Write lesson notes at the correct reading level (specify: middle/high school)
- Create analogy-rich explanations for complex AI topics
- Draft student-facing worksheets, quizzes, and project briefs
- Suggest real-world examples relevant to teenagers (social media, gaming, music, sports)

### Curriculum Design
- Suggest logical lesson sequences and learning progressions
- Identify prerequisite knowledge gaps before introducing new topics
- Help map topics to standards (CSTA, ISTE, or Common Core Math where applicable)

### Code Examples
- Write **clean, commented Python code** for AI demos
- Keep code simple enough for beginners — prefer readability over cleverness
- Suggest tools like Google Colab, Teachable Machine, or ml5.js for no-install demos

### Organization
- Maintain consistent frontmatter and note structure
- Suggest which folder a new note belongs in
- Flag notes that need updating or are missing links

### 📖 Glossary Maintenance Rule
> **This rule is mandatory — never skip it.**

Every time a technical term is introduced anywhere in this vault:
1. **Add it to [[Glossary]]** with a student-friendly one-sentence definition (middle-school reading level)
2. **Link back** to the source note using `→ [[Source Note Name]]` at the end of the definition
3. **Use wikilinks in notes** — write `[[Term]]` so it links to the glossary entry (e.g., `[[Machine Learning]]`, `[[Wikilink]]`)
4. **Don't duplicate** — if a term already exists in the Glossary, update the existing entry instead of adding a new one
5. **Scope:** This applies to ALL note types — Concept Notes, Lesson Plans, Projects, Daily Notes, and any new note created

Glossary entry format:
```
**Term** — Definition in plain language. → [[Source Note]]
```

> When in doubt: if you had to explain this word to a curious 12-year-old, would they need to look it up? If yes → it belongs in the Glossary.

### Tone & Style
- Friendly and encouraging, not condescending
- Use "we" and "you" to make it conversational
- Avoid academic jargon unless it is being explicitly taught and defined

---

## 🚀 Current Focus & Priorities

> Update this section regularly to reflect what you're actively working on.

- [x] Build out `06-Resources/📋 TEMPLATES/` with 6 reusable skill templates
- [x] Create concept notes: "What is Obsidian" and "What is Claude Code" in `03-Claude-Applications/`
- [x] Set up `05-Projects/` with 4 beginner project files (wiki build, best practices, templates practice, learning habits)
- [x] Populate [[Glossary]] with all defined terms (45+ entries across AI, Obsidian, and tools)
- [ ] Build out `01-AI-Fundamentals` with core AI concept notes
- [ ] Create a "What is AI?" introductory lesson for middle schoolers
- [ ] Populate `📄 MOC-Main-Index.md` with the full curriculum map
- [ ] Add a student-facing `06-Resources` reading list

---

## 💡 Teaching Philosophy

> "The goal is not to train future ML engineers — it's to build AI-literate citizens who can think critically about the technology shaping their world."

Key beliefs guiding this curriculum:

1. **Demystify before you deepen** — students should feel AI is understandable before diving into math.
2. **Ethics from day one** — fairness, bias, and privacy are not add-ons; they are part of every lesson.
3. **Creativity over memorization** — students learn best by *making* things, not just reading about them.
4. **Failure is data** — debugging and iteration are core skills, not signs of weakness.

---

*Last updated: 2026-04-12 (Glossary rule added) | Vault: AI_Knowledge_Base*
