---
title: "X Thread Writer"
skill: x-thread-writer
type: skill
tags: [skill, x, twitter, content, writing, publishing]
status: published
created: 2026-04-13
usage: "Invoke this skill with a TOPIC to extract vault knowledge and produce a ready-to-post X thread."
---

# 🐦 SKILL — X Thread Writer

> **Purpose:** Turn any topic from this vault (folders `01`–`07`) into a punchy, engaging X (Twitter) thread — ready to copy and post.
>
> **How to invoke:** Say _"Use the X Thread Writer skill for: [your topic]"_
> Example topics:
> - `Use Obsidian + Claude to build your own second brain`
> - `Publish an app via Vercel in under 10 minutes`
> - `How machine learning actually works — no math required`

---

## 🧠 STEP 1 — Understand the Topic & Source Notes

When invoked with a `{{TOPIC}}`:

1. **Identify the primary folder(s)** to search (see folder map below).
2. **Read all relevant notes** in those folders related to the topic.
3. **Also scan** [[📄 MOC-Main-Index.md]] and [[📄 MOC-Quick-Reference.md]] for any cross-references.
4. **Extract the core ideas** — look for:
   - Key definitions or concepts
   - Step-by-step processes
   - Surprising facts, contrasts, or analogies
   - "Why it matters" angles
   - Common misconceptions to bust
   - Actionable tips or takeaways

### Folder → Topic Map

| Folder | Best for |
|--------|----------|
| `01-AI-Fundamentals` | What is AI, ML, neural networks, ethics |
| `02-Programming-Basics` | Python, coding, beginner dev tips |
| `03-Applications` | Obsidian, Claude Code, LLMs, second brain |
| `04-ACEBott` | Chatbot building, automation |
| `05-Projects` | Project walkthroughs, builds, results |
| `06-Resources` | Tools, links, templates, references |
| `07-Fullstack-Development` | Web dev, deployment (Vercel, etc.) |

---

## ✍️ STEP 2 — Build the Thread Structure

A good X thread follows this proven skeleton:

```
[Tweet 1]  HOOK       — Stop the scroll. Bold claim, question, or surprising stat.
[Tweet 2]  CONTEXT    — Why does this matter right now?
[Tweet 3–N] BODY      — The key points, one idea per tweet.
[Last-1]   RECAP      — Quick summary ("Here's what we covered:")
[Last]     CTA        — Call to action (follow, bookmark, reply, share)
```

### Thread Length Guide

| Topic complexity | Recommended tweets |
|------------------|--------------------|
| Simple tip / tool intro | 5–7 tweets |
| Concept explanation | 7–10 tweets |
| Step-by-step tutorial | 10–15 tweets |

---

## 📐 STEP 3 — X Formatting Rules

Apply **all** of these rules when drafting:

### Character & Style
- Each tweet: **max 280 characters** (aim for 200–250 for readability)
- Number each tweet: `1/`, `2/`, `3/` … `N/` (where N = total)
- Use **short paragraphs** — 1–2 sentences max per tweet
- Use **line breaks** liberally for visual breathing room
- **Bold key terms** with CAPS (since X has no markdown): e.g., `OBSIDIAN`, `VERCEL`, `AI`
- Use plain emojis sparingly — 1–2 per tweet max, only where they add meaning

### Hook Patterns (pick one for Tweet 1)
- **The Bold Claim:** `"Most people waste hours in note apps. Here's how to build a second brain in 30 minutes with Obsidian + Claude 🧠"`
- **The Surprising Fact:** `"I deployed a full web app to Vercel in 8 minutes. No server setup. No DevOps. Here's exactly how 👇"`
- **The Question:** `"What if your notes could talk back to you? That's what Claude + Obsidian actually does. A thread 🧵"`
- **The Contrast:** `"Old way: Google Docs, folders, chaos. New way: Obsidian + AI. Here's the difference 👇"`

### Body Tweet Patterns (use variety)
- **Step format:** `Step 3: Connect notes with [[wikilinks]]. Now every idea links to every other idea. Your vault becomes a map, not a list.`
- **Tip format:** `Pro tip: Use frontmatter tags like status: draft → published. You'll always know what's ready and what needs work.`
- **Analogy format:** `Think of Obsidian like a personal Wikipedia — but YOU write every article, and YOU control the links.`
- **Contrast format:** `Notion lives in the cloud. Obsidian lives on YOUR machine. No subscription. No lock-in. Just files.`

### CTA Options (Tweet N)
- `Follow me for more tools + workflows for building with AI.`
- `If this was useful → RT the first tweet so others find it 🙏`
- `Drop your questions below ↓ Happy to go deeper on any step.`
- `Bookmark this thread for when you're ready to build.`

---

## 📋 OUTPUT FORMAT

Deliver the finished thread in this exact format so it's easy to copy-paste:

```
---
🐦 X THREAD — {{TOPIC}}
Source notes: [[Note 1]], [[Note 2]], ...
Thread length: N tweets
---

1/N
[Tweet text here]

2/N
[Tweet text here]

...

N/N
[CTA tweet here]

---
✅ Ready to post. Estimated read time: ~X minutes.
```

---

## 🔁 EXAMPLE — Worked Output

**Topic:** `Use Obsidian + Claude to build your own second brain`
**Source notes scanned:** [[What is Obsidian - Concept Note]], [[What is Claude Code - Concept Note]]

---

**1/8**
Most people lose 80% of what they learn.

Not because they're lazy — because their notes are scattered chaos.

Here's how OBSIDIAN + CLAUDE turns that chaos into a second brain 🧠👇

**2/8**
OBSIDIAN is a free note-taking app where every note is a plain `.md` file — on YOUR computer.

No cloud lock-in. No subscription. Just files you own.

**3/8**
The magic: you link notes together with [[double brackets]].

Every idea connects to every other idea.
Your vault becomes a MAP, not a pile.

**4/8**
CLAUDE CODE lives inside Obsidian.

You talk to it like a senior developer / editor / teacher — and it reads, writes, and organizes your notes with you.

**5/8**
The workflow:
→ Learn something new
→ Write a note in Obsidian
→ Ask Claude to extract key points, link related notes, and update your Glossary

One habit. Compounding knowledge.

**6/8**
It's not just note-taking.
It's building a KNOWLEDGE BASE that grows with you.

Every note links back. Every concept is defined.
You always know where to find anything.

**7/8**
Here's what you need to start:
✅ Download Obsidian (free)
✅ Install Claude Code plugin
✅ Create your first 3 folders: Concepts / Projects / Resources

That's it. Start small.

**8/8**
Follow me if you want more tools + workflows for learning with AI.

RT the first tweet if this was useful 🙏
Questions? Drop them below ↓

---

## 📎 NOTES FOR THE WRITER

- Always **cite which vault notes** you drew from (list them in the output header)
- If a key concept is missing from the vault, **flag it** and suggest creating a note
- Keep the voice **punchy and personal** — X rewards directness
- Avoid academic phrases like "It is worth noting that..." — just say it
- The thread should feel like **advice from a smart friend**, not a blog post

---

*Skill created: 2026-04-13 | Vault: AI_Knowledge_Base | Category: Content Publishing*
