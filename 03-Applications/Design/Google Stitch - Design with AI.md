---
title: "Google Stitch — Design with AI"
type: concept-note
tags: [google-stitch, design, UI, design-md, claude, AI-tools, frontend]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-13
---

# 🎨 Google Stitch — Design with AI

## ⚡ Core Concept (One Sentence)

> **Google Stitch** is a free, browser-based AI design tool that turns a text description (or a rough sketch) into polished UI screens — and then exports your entire design system as a `design.md` file that Claude can read and build from.

---

## 🤔 Why It Matters

Most developers jump straight into code before they've thought through what the UI should actually look like. Stitch flips the order: **design first, code second**. You describe what you want in plain English, Stitch generates realistic screens in seconds, and once you're happy with the look and feel, you export a `design.md` file that gives Claude everything it needs to build a consistent, matching frontend.

This is one of two main ways to design a website with AI assistance — see [[frontend-design Skill - Build UI with Claude]] for the alternative approach.

---

## 🖌️ How to Design in Stitch

**Access:** [stitch.withgoogle.com](https://stitch.withgoogle.com/) — runs entirely in the browser, no install, just a Google account.

### Step-by-Step Workflow

**1. Start a new project**
Open Stitch and click **New Project**. Give it a name — e.g., *"Student Dashboard App"*.

**2. Describe your UI in natural language**
Type a prompt like:
> *"A mobile dashboard for high school students to track their AI learning progress. Clean, modern, dark theme with cards for each subject."*

Stitch generates a set of screens based on your description.

**3. Refine with follow-up prompts**
Don't like something? Just describe the change:
> *"Make the header bigger and add a progress ring to each card."*

You can also **upload a sketch or wireframe** as a starting point — Stitch will replicate the layout with polished styling.

**4. Stitch screens together**
Click the **Stitch** button to link your screens into an interactive flow. Then hit **Play** to preview the full prototype — click through it like a real app.

**5. Review the design system**
Stitch automatically extracts your **design tokens** — the colors, fonts, and spacing it used — and displays them as a panel. This becomes the foundation of your `design.md`.

---

## 📤 Exporting design.md

### What is design.md?

`design.md` is a plain Markdown file that captures your **entire design system in a format AI coding tools can read**. It's not just a screenshot — it's a structured spec that includes:

- 🎨 **Color palette** — every color with its hex value and semantic name (e.g., `primary`, `surface`, `error`)
- ✍️ **Typography scale** — font families, sizes, weights, and line heights
- 📐 **Spacing system** — margin/padding values and layout grid
- 🧩 **Component patterns** — how buttons, cards, nav bars, and other elements are structured

Think of it as handing an AI a complete design rulebook before asking it to write any code.

### How to Export

1. Click the **Export** button (top right of the Stitch canvas)
2. Choose **design.md** from the export options
3. Save the downloaded file into your project folder (e.g., `DESIGN.md` in your project root)

---

## 🤖 Handing design.md to Claude

Once you have your `DESIGN.md`, you have two options to get Claude to build from it:

### Option A — Via MCP (Live Sync)
If you have the **Stitch MCP** configured in Claude Code:
- Stitch and Claude Code stay connected
- Changes in Stitch automatically sync to Claude
- Best for: ongoing projects where you keep refining the design

### Option B — Paste Directly (Quick & Simple)
Paste the contents of your `DESIGN.md` into Claude chat or Claude Code with a prompt like:

```
Here is my design spec:

[paste DESIGN.md contents here]

Build this as a React app with Tailwind CSS. Start with the home screen.
```

This works perfectly for single projects. It's simpler and requires no MCP setup.

> 💡 **Tip:** Place your `DESIGN.md` in the root of your project folder. Claude Code will read it automatically when you ask it to build frontend components.

---

## 🔑 Key Terms

- **[[Google Stitch]]** — the AI design canvas tool at stitch.withgoogle.com
- **[[design.md]]** — the AI-readable design spec exported from Stitch
- **[[MCP (Model Context Protocol)]]** — the standard that lets Stitch connect live to Claude Code

> 📖 See full glossary: [[Glossary]]

---

## 🖐️ Try It — Quick Activity

**Goal:** Go from a text prompt to a `design.md` file in under 10 minutes.

1. Go to [stitch.withgoogle.com](https://stitch.withgoogle.com/) and sign in with your Google account
2. Create a new project and type this prompt:
   > *"A landing page for a teen AI learning app. Bright, energetic, with a hero section, feature cards, and a sign-up button."*
3. Generate the screen — explore the design tokens panel
4. Click **Stitch** → link to a second screen → hit **Play** to preview
5. Export as **design.md** and open it in a text editor — read through it
6. Paste the `design.md` content into Claude and ask: *"Build the hero section from this design spec as HTML and CSS."*

**Reflect:** *What did Claude produce? Does it match what Stitch designed?*

---

## 🔗 Related Notes

- [[frontend-design Skill - Build UI with Claude]] — the alternative approach: skip the design tool and go straight to polished code with Claude
- [[What is Claude Code - Concept Note]] — understanding the AI assistant you're handing design.md to
- [[07-Fullstack-Development/00-INDEX]] — the broader fullstack development workflow this fits into
- [[03-Applications/Publish-an-Application/What is Vercel - Concept Note]] — deploying the frontend once it's built
