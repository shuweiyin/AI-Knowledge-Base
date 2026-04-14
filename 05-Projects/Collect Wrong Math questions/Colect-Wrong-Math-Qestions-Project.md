---
title: "DrFrost → Notion Sync: A Real Agent Project"
type: project-log
level: high-advanced
topic: claude-applications
tags: [agent, automation, playwright, notion, drfrost, web-scraping, API, real-world-project]
status: published
created: 2026-04-14
---

# 🤖 DrFrost → Notion Sync — Project Log

> **A real-world AI agent project built step by step: from a simple question to a fully automated system.**

---

## 🪝 The Hook

Imagine you've done 26 maths homework assignments on DrFrost. Somewhere across all those tasks, you got 51 questions wrong — spread across 15 different topics. Finding them manually would take an hour. Knowing *which unit* each wrong question belongs to? Even longer.

**What if an AI agent could do it in 5 minutes — and send the results straight to Notion?**

That's exactly what this project builds.

---

## 🎯 Project Overview

**What it does:** Automatically logs into DrFrost, scans every completed homework task, identifies every wrong answer, maps each wrong skill to its unit, and writes a structured revision database in Notion — with a one-click practice link per skill.

**Who it's for:** Nemo Liu (Year 8, Dulwich College) — but the approach applies to any student using DrFrost.

**Why it matters as a teaching example:** This is a *real* agent project solving a *real* problem. It uses login automation, REST API discovery, data processing, and Notion MCP — all tools a modern AI engineer would use.

---

## 💡 The Problem It Solves

Before this project, the workflow to find weak areas was:
1. Open DrFrost manually
2. Click each homework task one by one
3. Scroll through questions to find the wrong ones
4. Write down which topic each wrong question belonged to
5. Repeat for all 26 tasks
6. Manually create a revision list somewhere

**Time taken:** 45–60 minutes. **Chance of missing something:** High.

After this project:
1. Run one terminal command
2. Tell Claude "sync to Notion"
3. Open Notion — everything is there

**Time taken:** 5 minutes, fully automatic. This is the power of agents.

---

## 🗺️ Architecture

The full system has three stages working together:

```
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: LOGIN & SCRAPE (Python + Playwright)              │
│                                                             │
│  Terminal command → headless browser opens                  │
│  → logs into DrFrost via Microsoft SSO                      │
│  → calls DrFrost's internal REST API                        │
│  → collects wrong answers per task                          │
│  → looks up unit name per skill                             │
│  → saves results to drfrost_results.json                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: ANALYSIS (Claude)                                 │
│                                                             │
│  Claude reads drfrost_results.json                          │
│  → understands the structure                                │
│  → decides how to organise rows in Notion                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3: WRITE TO NOTION (Notion MCP)                      │
│                                                             │
│  Claude uses Notion MCP tools                               │
│  → clears old database rows                                 │
│  → inserts 51 fresh rows with skill, unit, practice link    │
│  → database is ready to use                                 │
└─────────────────────────────────────────────────────────────┘
```

> **Key insight:** The agent isn't one thing — it's a *pipeline*. Each stage does what it's best at. Python is great at browser automation. Claude is great at reasoning and organising data. Notion MCP handles the output layer. Splitting responsibilities like this is called a **[[Multi-Agent Architecture]]**.

---

## 🔍 Phase 1 — Reconnaissance

> *"Before you build, you must understand."*

The first instinct when building web automation is to start coding. The smarter approach is to **explore first**. We spent time understanding DrFrost before writing a single line of real code.

### The login challenge

DrFrost uses **Microsoft SSO (Single Sign-On)** — you click "Login with Microsoft" and get redirected to Microsoft's login page before coming back to DrFrost. This raised three concerns:

| Concern | Reality |
|---|---|
| Multi-Factor Authentication (MFA) | No MFA on second login — confirmed safe to automate |
| School device restrictions | Personal computer — no IT policy blocking it |
| Cookie consent overlay blocking clicks | Yes — needed to dismiss it first before clicking login |

**Decision made:** Automate the Microsoft SSO flow directly with Playwright, rather than using a cookie export workaround. Simpler for the user — just run the script.

### The surprising discovery — DrFrost has a REST API

Most websites store data in their HTML. DrFrost is a modern **React app** — the page is mostly empty HTML; the real data loads via **[[REST API]]** calls in the background.

By intercepting network traffic (watching what the browser requests behind the scenes), we found clean JSON endpoints:

- `/api/tasks/list` → all homework tasks
- `/api/tasks/attempt/{id}` → every question answer, marked correct or wrong
- `/api/course/explore/{id}` → the unit name and all skills inside it

**Why this matters:** Working directly with an API is *far* more reliable than scraping HTML. HTML changes with redesigns; API data structures change much less often.

### The ssid → unit mapping trick

Every wrong answer had a `ssid` (sub-skill ID) — a number like `8570`. But a number alone tells you nothing. The unit name ("Surface Area & Volume") is what makes it useful for revision.

The trick: navigating to `explorer.php?ssid=8570` caused DrFrost to automatically call `/api/course/explore/{cuid}` — which returned the unit name and all skills inside it. By watching the network call, we extracted exactly what we needed.

**Analogy:** It's like asking someone for directions by pretending to walk toward a destination — watching which road they point you to tells you the route, even if they never said it out loud.

---

## 🔧 Phase 2 — Building the Scraper

### Why Playwright, not Computer Use

[[Computer Use]] lets Claude literally see your screen and click things — like a human using a computer. It sounds impressive, but for this task it was the wrong tool.

| | Computer Use | Playwright Script |
|---|---|---|
| Speed | Slow (screenshot every step) | Fast (direct API calls) |
| Reliability | Breaks if UI changes | Stable (uses API, not visuals) |
| Cost | High (many tokens per screenshot) | Near zero |
| Schedulable | Complex | Simple |

**Decision made:** Use Playwright for the mechanical work (login, navigation, API calls). Reserve Claude's intelligence for the analysis layer — reading, understanding, and organising the data.

> **The lesson:** Always use the right tool for each layer. Don't use a hammer to turn a screw.

### How wrong answers are detected

Each answer object from the API has a field: `"iscorrect": true` or `"iscorrect": false`. The script simply filters for `false`. No guessing, no text parsing — the data is already structured.

This is a key principle of working with APIs: **trust the data structure, don't infer from text.**

### Handling the skill lookup efficiently

There were 51 unique wrong skills (ssids). Each one needed a unit name. Rather than calling a single bulk API (which didn't exist), the script visits `explorer.php?ssid=X` for each one — 51 small lookups.

**Trade-off:** Slower (adds ~3 minutes) but 100% accurate. A faster approach (guessing unit names from skill codes) would risk errors. For a revision tool, accuracy matters more than speed.

---

## 🗂️ Phase 3 — Notion Integration

### Why Notion MCP, not Notion API

To write to Notion from code, the normal approach is: get a Notion API token → store it securely → write Python code that calls Notion's API.

The better approach here: **Notion MCP is already connected to Claude.** No token needed. No extra setup. Claude can write to Notion directly, as if it were a native capability.

**Decision made:** Claude handles the Notion layer entirely via MCP. The Python script only scrapes — it doesn't touch Notion at all.

> **The lesson:** Before building an integration from scratch, check what tools are already available. The best code is code you don't have to write.

### Database schema decisions

The database needed to be **useful to a student**, not just technically complete. Each column was chosen with a purpose:

| Column | Why it's there |
|---|---|
| **Skill** | What specifically went wrong |
| **Unit** | Which topic area to revise |
| **Code** | DrFrost's internal skill number (for reference) |
| **Times Wrong** | Priority signal — wrong more often = revise first |
| **Tasks** | Which homework(s) triggered this — for context |
| **Practice Link** | One click → practise this exact skill on DrFrost |
| **Review Link** | One click → see the original task |
| **Status** | Student marks progress manually |
| **Last Synced** | Know when the data was last refreshed |

**Columns deliberately left out:** Raw question text (changes each attempt — not stable), student's wrong answer (discouraging, not useful for revision).

### How batch insertion works

Notion MCP allows creating up to 100 rows in a single call. All 51 rows were inserted in 2 batches (25 + 26). The previous rows are cleared on re-sync so there are no duplicates.

---

## 📁 File Structure

All project files live in:
`05-Projects/DrFrost-Sync/`

| File | Purpose |
|---|---|
| `drfrost_scraper.py` | The automation script — runs the browser, calls DrFrost API, saves JSON |
| `drfrost_results.json` | Output from the last scrape — read by Claude for Notion sync |
| `notion_config.json` | Notion database IDs — so Claude knows where to write |
| `How to Re-sync DrFrost.md` | Step-by-step guide for re-running |
| `DrFrost-Notion-Sync-Project.md` | This file — the project log |

---

## 🚀 How to Use (Quick Reference)

**When:** After completing new DrFrost homework, or every 2–4 weeks.

**Step 1:** Open Terminal and run:
```
python3 "05-Projects/DrFrost-Sync/drfrost_scraper.py"
```

**Step 2:** When it finishes, tell Claude:
> *"DrFrost sync is ready, please update Notion"*

**Step 3:** Open your Notion database and review the updated rows.

Full guide: [[How to Re-sync DrFrost]]

---

## 🔮 Roadmap — What's Next

This project was built in stages. The current version (Option C) gives individual practice links. Future versions will go further:

| Version | What it adds | Complexity |
|---|---|---|
| **C — Current ✅** | Individual skill practice links in Notion | Done |
| **B — Next** | Auto-generate a combined DrFrost practice session per *unit* — one link per weak unit, covers all wrong skills in it | Medium |
| **A — Future** | One single mixed practice session combining *all* wrong skills across all units | Medium-High |

Options B and A require one more step: automating the DrFrost Explorer's skill-selection UI to trigger the "Practise" button and capture the session link. The groundwork is already in place.

---

## 🧠 Key Technical Learnings

These discoveries are useful for anyone building a similar agent project:

**1. Modern web apps hide clean APIs**
React/Next.js apps load data via fetch calls, not in the HTML. Always intercept network traffic before assuming you need to scrape HTML. You often find a cleaner, more stable API underneath.

**2. The "navigate and watch" trick**
When you can't find a direct API endpoint, navigate to the feature you need in the browser and watch what API calls it triggers. The browser does the work of revealing the endpoint.

**3. Split the pipeline by capability**
Don't force one tool to do everything. Python + Playwright for browser automation. Claude for reasoning. Notion MCP for output. Each tool at what it's best at.

**4. MCP removes integration friction**
Claude's MCP connections (Notion, Gmail, Google Calendar) are pre-authenticated and ready to use — no token setup, no API boilerplate. Check available MCPs before building a custom integration.

**5. Reconnaissance before code**
The most valuable time spent on this project was the first few hours — just exploring the site, testing APIs, and understanding data structures. Every minute of exploration saved ten minutes of debugging later.

---

## 📅 Build Log

| Date | What was done | Outcome |
|---|---|---|
| 2026-04-14 | Discussed requirements — 5 automation scenarios | Agreed on DrFrost wrong skills as first project |
| 2026-04-14 | Phase 1 recon — login, page structure, network interception | Discovered clean REST API; login via Microsoft SSO confirmed working |
| 2026-04-14 | Phase 2 recon — attempt API, wrong answer structure, unit mapping | Found `iscorrect` field + `ssid → explorer → unit` trick |
| 2026-04-14 | Phase 3 recon — Notion MCP confirmed, practice URL confirmed | `do-question.php?ssid=X` confirmed as practice link |
| 2026-04-14 | Built `drfrost_scraper.py` — full pipeline | Scraped 26 tasks, 51 wrong skills, 15 units |
| 2026-04-14 | Created Notion database + inserted 51 rows via MCP | Live in Notion at Math Improve → DrFrost Weak Skills |
| 2026-04-14 | Saved all files to vault, wrote re-sync guide | Project fully documented and re-runnable |

---

## 🔑 Key Terms

- **[[Managed Agent]]** — An AI configured to complete multi-step tasks autonomously using tools
- **[[Agentic Loop]]** — The observe → reason → act → repeat cycle that powers agents
- **[[REST API]]** — A standard way for web apps to share data; returns clean JSON instead of HTML
- **[[MCP (Model Context Protocol)]]** — Standard that lets Claude connect to external tools like Notion
- **[[Multi-Agent Architecture]]** — Splitting a complex task across multiple specialised agents or tools
- **[[Computer Use]]** — Claude's ability to see a screen and control mouse/keyboard (not used here — too slow)
- **[[Playwright]]** — A Python library for automating web browsers programmatically
- **[[Single Sign-On (SSO)]]** — A login system where one account (e.g. Microsoft) authenticates you across multiple services

> 📖 See full glossary: [[Glossary]]

---

## 🖐️ Try It — Build Your Own Version

**Challenge for advanced students:**
Can you adapt this project for a different platform? For example:

1. **Khan Academy** — find your weakest exercise types and list them in Notion
2. **Duolingo** — extract your most-missed vocabulary words
3. **Any school portal** — extract your grade history and visualise trends

The pattern is always the same:
1. Intercept the network to find the API
2. Authenticate (handle login)
3. Extract the data you care about
4. Send it somewhere useful

> 📎 See also: [[Claude Managed Agents - Concept Note]] for the theory behind what makes this an agent project

---

*Project built: 2026-04-14 | Student: Nemo Liu, Dulwich College Year 8 | Built with: Claude Code + Playwright + Notion MCP*
