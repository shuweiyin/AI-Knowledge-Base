---
title: "How to Deploy to Vercel"
skill: lesson-plan
type: lesson-plan
tags: [vercel, deployment, github, lesson-plan, hands-on, web-development, publish-an-application]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-12
---

# How to Deploy to Vercel — Lesson Plan

---

## 📋 Lesson Overview

| Field | Details |
|-------|---------|
| **Topic** | Deploying a web project to Vercel |
| **Level** | `high-intro` (Grade 9–10) |
| **Duration** | 75–90 minutes (one class period) |
| **Group Size** | Solo (or pairs for support) |
| **Prerequisites** | [[Frontend vs Backend - Concept Note]] · [[What is Vercel - Concept Note]] · [[GitHub Vault Backup - Project]] (Git basics) |
| **Tools Needed** | Computer with internet, GitHub account (free), Vercel account (free), any simple project to deploy |

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

1. **Explain** the full deployment pipeline: Code → Git → GitHub → Vercel → Live URL
2. **Connect** a GitHub repository to Vercel and trigger a first deployment
3. **Interpret** a Vercel deployment status (success, building, failed)
4. **Add** an environment variable to a Vercel project securely
5. **Share** a live project URL from their Vercel dashboard

---

## 🗺️ The Big Picture — The Deployment Pipeline

Before writing a single command, students should understand the full chain:

```
┌──────────────┐    git push    ┌──────────────┐    auto-trigger    ┌──────────────┐    live URL    ┌──────────────┐
│  Your Code   │ ────────────▶ │    GitHub    │ ─────────────────▶ │    Vercel    │ ─────────────▶ │  The World   │
│ (on laptop)  │               │ (cloud repo) │                    │  (builder)   │                │ (any browser)│
└──────────────┘               └──────────────┘                    └──────────────┘                └──────────────┘
```

Every step after the first `git push` is **automatic**. Vercel watches GitHub. The moment new code arrives, it builds and deploys your project — no clicking required.

---

## ⏱️ Lesson Timeline

| Time | Phase | Activity |
|------|-------|----------|
| 0–10 min | **Hook** | The "It's live!" moment |
| 10–20 min | **Direct Instruction** | Understanding the pipeline |
| 20–50 min | **Guided Practice** | First deployment walkthrough |
| 50–65 min | **Independent Practice** | Add env variable + make a change |
| 65–75 min | **Discussion** | Share URLs, reflect on the process |
| 75–80 min | **Exit Ticket** | Quick comprehension check |

---

## 🎣 Hook (0–10 min)

**Open with this question:** *"Raise your hand if you've built something on your computer that you wished other people could see — but you had no idea how to share it."*

Give students 2 minutes to think of a project (Minecraft world, a game, a website, a Python script). Then tell them:

> "By the end of today's class, any website or web app you build will be live on the internet — with a real URL you can text to your friends — in about 5 minutes. And every time you update your code, it updates live automatically."

Show a live example: open a project on Vercel, make a tiny text change, push to GitHub, and let students watch the Vercel dashboard rebuild in real time. The 30-second deploy is the hook.

---

## 📖 Direct Instruction (10–20 min)

### The Pipeline (5 min)
Draw or display the pipeline diagram from above. Walk through each step:

1. **You write code** — on your laptop, nothing is public yet
2. **`git add` + `git commit`** — Git takes a snapshot of your changes
3. **`git push`** — your snapshot travels to GitHub (cloud storage)
4. **Vercel detects the push** — Vercel is "watching" your GitHub repo
5. **Vercel builds your project** — it installs dependencies, compiles code
6. **Vercel deploys** — your built files go live at your `.vercel.app` URL

### Two Key Concepts (5 min)
- **What Vercel needs from you:** A GitHub repo, a build command (often `npm run build` or nothing for static HTML), and an output folder
- **What you must never do:** Put API keys in your code — remind students of [[Environment Variables and API Key Security - Concept Note]]

---

## 🧑‍💻 Guided Practice — First Deployment (20–50 min)

Work through this step by step as a class. Students follow along on their own computers.

---

### Step 1 — Prepare Your Project (5 min)

If students don't have a project, create a minimal one right now:

1. Create a new folder called `my-first-deploy`
2. Inside it, create `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First Deployment</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background: #0070f3;
      color: white;
      text-align: center;
    }
    h1 { font-size: 3rem; }
    p  { font-size: 1.25rem; opacity: 0.85; }
  </style>
</head>
<body>
  <div>
    <h1>🚀 I'm Live on the Internet!</h1>
    <p>Deployed with Vercel on 2026-04-12</p>
  </div>
</body>
</html>
```

3. Initialize Git and push to GitHub:
```bash
cd my-first-deploy
git init
git add .
git commit -m "Initial commit: my first deployment"
```
4. Create a new GitHub repository called `my-first-deploy` (no README), then:
```bash
git remote add origin https://github.com/YOUR-USERNAME/my-first-deploy.git
git push -u origin main
```

**Expected result:** Your project is now on GitHub.

---

### Step 2 — Connect Vercel to GitHub (5 min)

1. Go to [vercel.com](https://vercel.com) and sign in (or create a free account)
2. Click **"Add New Project"** (top right)
3. Under **"Import Git Repository"**, you'll see your GitHub repos listed
4. Find `my-first-deploy` and click **"Import"**

Vercel automatically detects it's a plain HTML project and configures itself. You'll see:
- **Framework Preset:** `Other` (for plain HTML)
- **Root Directory:** `./`
- **Build Command:** *(leave blank for plain HTML)*
- **Output Directory:** `./`

5. Click **"Deploy"**

---

### Step 3 — Watch the Build (5 min)

The Vercel dashboard shows a live build log. Walk students through what they see:

```
[10:23:01] Cloning github.com/username/my-first-deploy (Branch: main, Commit: abc1234)
[10:23:02] Cloning completed: 312ms
[10:23:03] Running build in Washington, D.C., USA (East) — iad1
[10:23:04] Build Completed in /vercel/output [391ms]
[10:23:05] Deploying outputs...
[10:23:06] ✅ Deployment completed
```

Point out:
- The commit hash (`abc1234`) — it matches the GitHub commit
- The region — Vercel serves from the nearest data center
- The total time — usually 20–45 seconds for a simple project

When it shows **"Congratulations! Your project has been successfully deployed."** — click the URL.

**🎉 Moment of celebration:** Students see their page live on the internet.

---

### Step 4 — Add a Preview Deployment (5 min)

Show students how every branch gets its own URL:

```bash
git checkout -b update-colors
```

Edit `index.html` — change the background color from `#0070f3` to `#ff4d00`:

```bash
git add .
git commit -m "Change background to orange"
git push origin update-colors
```

Back in Vercel dashboard → **Deployments** tab — a new deployment appears for the `update-colors` branch with a *different* URL. The main site (`main` branch) is unchanged. This is a [[Preview Deployment]].

---

## 🔒 Independent Practice — Env Variable + Update (50–65 min)

### Task A — Add an Environment Variable (10 min)

1. In Vercel dashboard → your project → **Settings → Environment Variables**
2. Add:
   - **Name:** `SITE_AUTHOR`
   - **Value:** your name
   - **Environments:** check Production, Preview, Development
3. Click **Save**

Then update `index.html` to display a message: *"This project will be built to read `SITE_AUTHOR` from the environment."* (For plain HTML this is conceptual — the full wiring is covered in [[Claude Code Vercel Plugin - Concept Note]] for dynamic apps.)

### Task B — Intentionally Break & Fix (5 min)

This is the most important practice:

1. Add a syntax error to your HTML (e.g., leave a tag unclosed)
2. Push it: `git add . && git commit -m "broken version" && git push`
3. Watch the Vercel dashboard — the deployment may still succeed for plain HTML (HTML is forgiving), but for a JavaScript project it would fail
4. For a more realistic failure: delete `index.html`, push, watch the "No output directory found" error
5. Restore the file, push again, watch it redeploy successfully

**Key lesson:** Vercel never takes down your live site for a failed deployment — the *previous* working version stays live until a new deployment succeeds.

---

## 💬 Discussion (65–75 min)

Have students share their live URLs with the class. Then discuss:

**Recall:**
- What are the four steps in the deployment pipeline?
- What does Vercel do automatically after every `git push`?

**Analysis:**
- How is deploying to Vercel different from just emailing someone a file?
- Why does Vercel keep the old version live when a new deployment fails?

**Critical Thinking:**
- If you pushed a broken version and it went live immediately to 10,000 users, what would you do? How would Vercel's deployment history help?
- A company pushes 50 deployments a day. How does automatic deployment (CI/CD) change the way their team works compared to a manual process?

---

## 🎟️ Exit Ticket (75–80 min)

Students answer three questions in their notes or on paper:

1. **Draw or describe** the deployment pipeline in your own words (Code → ? → ? → Live URL)
2. **What is a Preview Deployment** and why is it useful?
3. **One thing I would do differently** on my next deployment — based on what went wrong or what surprised me today

---

## ⭐ Grading Rubric

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|----------------|----------------|
| **Project deployed** | Live URL works, correct content | Live URL works | Partially deployed | Not deployed |
| **Pipeline understanding** | Can explain all 4 steps accurately | Explains 3 steps | Explains 2 steps | Cannot explain |
| **Env variable added** | Added, named clearly, correct environments | Added but misconfigured | Attempted | Not attempted |
| **Preview deployment** | Created and can explain the difference | Created | Attempted | Not attempted |
| **Exit ticket** | All 3 questions complete, thoughtful | 2 questions complete | 1 question | Blank |

**Total: \_\_ / 20**

---

## 🚀 Extension Challenges

- **Level Up 1:** Connect a custom domain to your Vercel project (requires buying a domain — $10–15/year). Vercel walks you through the DNS setup step by step.
- **Level Up 2:** Add a second page to your site (`about.html`), push it, and confirm the live site updates automatically.
- **Level Up 3:** Use the [[Claude Code Vercel Plugin - Concept Note|Claude Code Vercel Plugin]] to trigger your next deployment and check its status — without opening the Vercel dashboard at all.
- **Level Up 4:** Convert your plain HTML project to a simple Next.js app. Vercel auto-detects it and reconfigures the deployment.

---

## 🤝 Ethics Checkpoint

- You just made something accessible to *everyone on the internet*. Did you include anything personal (your full name, school, location, photo)? Is that intentional?
- Preview deployments have long, random URLs — does that make them "private"? (No — they're still publicly accessible if someone has the URL.)
- If an AI tool (like Claude Code via the Vercel plugin) deploys something that breaks your live site, who is responsible for fixing it?

---

## 🔑 New Terms — Added to Glossary

- **[[Vercel]]** — cloud deployment platform
- **[[Deployment]]** — making code live on the internet
- **[[CI/CD]]** — automatic build and deploy on every code push
- **[[Preview Deployment]]** — temporary URL for a branch, before merging to main
- **[[Build Command]]** — the instruction Vercel runs to compile your project

> 📖 See full definitions: [[Glossary]]

---

## 🔗 Related Notes in This Topic Suite

| # | Note | Link |
|---|------|------|
| 1 | Frontend vs Backend | [[Frontend vs Backend - Concept Note]] |
| 2 | What is Vercel | [[What is Vercel - Concept Note]] |
| 3 | Environment Variables & Security | [[Environment Variables and API Key Security - Concept Note]] |
| 4 | Claude Code Vercel Plugin | [[Claude Code Vercel Plugin - Concept Note]] |
| 5 | **How to Deploy to Vercel** ← *you are here* | [[How to Deploy to Vercel - Lesson Plan]] |
| 6 | Reading Build Logs & Debugging | [[Reading Build Logs and Debugging - Concept Note]] |
