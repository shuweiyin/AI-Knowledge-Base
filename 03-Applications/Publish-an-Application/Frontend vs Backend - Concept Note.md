---
title: "Frontend vs Backend — What Am I Actually Deploying?"
skill: concept-note
type: concept-note
tags: [frontend, backend, web-development, deployment, static-site, server, api, publish-an-application]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-12
---

# Frontend vs Backend — Concept Note

## ⚡ Core Concept (One Sentence)

> Every web application has two sides: the **frontend** (what users see in their browser) and the **backend** (the hidden engine that stores data and runs logic on a server) — and knowing which side you're deploying changes everything about how you do it.

---

## 🤔 Why It Matters

Before you deploy anything to [[Vercel]], you need to answer one question: *what kind of thing am I actually publishing?* A personal portfolio page and an AI chatbot app look similar from the outside — both run in a browser — but they work completely differently under the hood. Mixing them up is the most common reason deployments fail or behave unexpectedly.

---

## 📖 Detailed Explanation

### Part 1 — The Frontend

The **[[frontend]]** is everything the user sees and touches directly in their web browser:

- The buttons, text, colors, and layout (HTML + CSS)
- The animations and interactivity (JavaScript)
- Forms, menus, images, and pages

A frontend has **no secret logic**. Every line of code is downloaded to the user's browser when they visit your site — which means anyone can open "View Source" and read it. This is important: **you must never put API keys or passwords in frontend code.**

**Examples of pure-frontend projects:**
- A personal portfolio website
- A static blog
- A school project homepage
- A JavaScript quiz or game with no database

### Part 2 — The Backend

The **[[backend]]** is the hidden part of an application that runs on a **server** — a computer somewhere in the world that users never see directly:

- Stores and retrieves data from a [[database]]
- Handles user login and authentication
- Makes calls to external APIs (like the Claude API) *safely*, away from the user
- Runs business logic that shouldn't be public

When you chat with an AI assistant on a website, your message travels from your browser (frontend) → to a server (backend) → the server calls the Claude API with the secret key → gets a response → sends it back to your browser. The API key never touches your browser.

### Part 3 — The Three Types of Apps You Might Deploy

| Type | What It Is | Backend Needed? | Vercel Support |
|------|-----------|-----------------|----------------|
| **Static Site** | HTML/CSS/JS files, no server logic | ❌ No | ✅ Perfect fit |
| **Frontend + Serverless Functions** | Static site + small backend snippets | ✅ Mini-backend | ✅ Built-in with Vercel |
| **Full-Stack App** | Full frontend + full backend (e.g., Next.js) | ✅ Full backend | ✅ Native support |

Most student AI projects fall into the **middle category** — a frontend that needs a tiny backend function to safely call an AI API.

### Part 4 — What Vercel Does

[[Vercel]] is a **[[hosting]]** platform that can handle all three types above. It's especially good at:
- Hosting static sites instantly (zero configuration)
- Running **[[serverless functions]]** — small backend snippets that spin up only when needed, so you don't need to manage a full server
- Auto-deploying every time you push code to [[GitHub]]

---

## 🪄 Analogies & Stories

**Analogy 1 — The Restaurant 🍽️**
The **frontend** is the dining room — the tables, menus, décor, and waiters. Customers experience it directly. The **backend** is the kitchen — the recipes, ingredients, and chefs are hidden from customers. The kitchen holds secret recipes (your API keys and business logic); the dining room never reveals them. Vercel is like the restaurant building itself — it provides the space for both to operate.

**Analogy 2 — The Iceberg 🧊**
A website is like an iceberg. The frontend is the visible tip above water — beautiful, designed to be seen. The backend is the massive part below — doing all the heavy lifting, storing the data, keeping secrets. Users only ever see the tip.

---

## ❓ Common Student Questions

**Q: My project is just HTML and CSS — do I need a backend?**
A: Nope! A pure HTML/CSS/JS site is a "static site." Vercel can host it in under a minute with no backend required.

**Q: I want to use the Claude API in my app. Does that mean I need a backend?**
A: Yes — and this is critical. You must never call the Claude API directly from your frontend JavaScript, because your API key would be visible to everyone. You need a backend function (Vercel makes this easy with Serverless Functions) that makes the API call privately.

**Q: What's the difference between a website and a web app?**
A: A **website** is mostly static information (like a blog or portfolio). A **web app** is interactive and dynamic — it responds to user input, stores data, and changes based on who's using it (like Gmail or a chatbot). The line is blurry, but the key difference is whether it *does* things vs. just *shows* things.

**Q: What is Next.js and why does everyone talk about it with Vercel?**
A: Next.js is a JavaScript framework built by the same team that makes Vercel. It lets you write both frontend and backend code in one project, and Vercel knows exactly how to deploy it. Think of it as a complete restaurant kit — everything included and perfectly compatible with the building (Vercel).

---

## ⚠️ Common Misconceptions

| Misconception | The Truth |
|--------------|-----------|
| "My frontend code is private" | Frontend code is always public — anyone can read it in their browser's dev tools |
| "I need a backend for every project" | Static sites need no backend at all — Vercel hosts them instantly |
| "API keys are safe in JavaScript files" | Never. API keys in frontend JS are exposed to the entire internet |
| "Vercel only works with React or Next.js" | Vercel works with plain HTML, Python, Vue, Svelte, and many more |

---

## 🔑 Key Terms & Definitions

- **[[Frontend]]** — The part of a web application users see and interact with in their browser (HTML, CSS, JavaScript)
- **[[Backend]]** — The server-side logic, databases, and API calls hidden from users
- **[[Static Site]]** — A website made of fixed files (HTML/CSS/JS) with no server-side processing
- **[[Serverless Function]]** — A small piece of backend code that runs only when called, without needing a full-time server
- **[[Hosting]]** — Making your files available on the internet so anyone can visit your site via a URL
- **[[Database]]** — A structured store of data that the backend reads from and writes to
- **[[Vercel]]** — A hosting platform specialized in deploying frontends and serverless functions

> 📖 See full glossary: [[Glossary]]

---

## 🖐️ Try It — Quick Activity

**Activity:** Spot the Frontend and Backend
**Time:** 10 minutes
**Materials:** Any web browser

**Instructions:**
1. Open any website you use daily (Instagram, YouTube, Google)
2. Right-click anywhere → **"View Page Source"** (or press `Ctrl+U` / `Cmd+U`)
3. You're now looking at the **frontend** code — HTML the server sent to your browser
4. Notice: no passwords, no database contents, no secret logic — just structure and layout
5. Ask yourself: *"Where is the actual data (my posts, my videos) coming from?"* → That's the **backend**

**Reflect:** *"What information on this site would break everything if it were public? Where do you think that's being kept?"*

---

## 🤝 Ethics Connection

Frontend code being public is a double-edged sword. On one hand, it makes the web **open and inspectable** — you can learn how websites are built just by viewing source. On the other hand, it means any secret you accidentally put in frontend code is instantly exposed to billions of people.

This asymmetry — public frontend, private backend — is also why **data privacy** matters. When a company says your data is "secure," they mean it's protected on the backend. But if their frontend has bugs, attackers can trick users into sending data to the wrong place. Understanding the boundary is the first step to building responsibly.

> 📎 See also: [[Environment Variables and API Key Security - Concept Note]]

---

## 🔗 Related Notes in This Topic Suite

| # | Note | Link |
|---|------|------|
| 1 | **Frontend vs Backend** ← *you are here* | [[Frontend vs Backend - Concept Note]] |
| 2 | What is Vercel | [[What is Vercel - Concept Note]] |
| 3 | Environment Variables & Security | [[Environment Variables and API Key Security - Concept Note]] |
| 4 | Claude Code Vercel Plugin | [[Claude Code Vercel Plugin - Concept Note]] |
| 5 | How to Deploy to Vercel | [[How to Deploy to Vercel - Lesson Plan]] |
| 6 | Reading Build Logs & Debugging | [[Reading Build Logs and Debugging - Concept Note]] |
