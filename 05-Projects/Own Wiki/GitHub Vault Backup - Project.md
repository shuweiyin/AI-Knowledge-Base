---
title: "GitHub Vault Backup"
skill: project
type: project
tags: [project, github, git, backup, version-control, obsidian, intermediate]
level: high-intro
topic: claude-applications
status: published
created: 2026-04-12
---

# GitHub Vault Backup — Project

## 🧪 Project Brief

| Field | Details |
|-------|---------|
| **Topic** | Using Git + GitHub to back up and version-control an Obsidian vault |
| **Project Title** | "Never Lose a Note" — GitHub Vault Backup |
| **Grade Level** | `[x] Grade 9-10` `[x] Grade 11-12` |
| **Duration** | 1–2 class periods (or ~90 minutes at home) |
| **Group Size** | `[x] Solo` |
| **Difficulty** | `[x] Intermediate` |
| **Prerequisites** | [[Build Your Own Wiki - Project]] · [[Obsidian Best Practices - Project]] |

---

## 🎯 Project Goal

**What students will build:**
A fully automated GitHub backup system for their Obsidian vault — every change saved, every version recoverable, and an optional public portfolio others can visit.

**What students will learn:**
- What [[Git]] and [[GitHub]] are, and why version control matters
- How to create a GitHub repository and connect it to a local vault
- How to use the Obsidian Git plugin to auto-commit and push changes
- How to read commit history to track their own learning over time
- How to recover a previous version of a note if something goes wrong

---

## 🛠️ Required Tools & Materials

| Tool | Purpose | Cost | Link |
|------|---------|------|------|
| [Git](https://git-scm.com) | Version control engine on your computer | Free | git-scm.com |
| [GitHub](https://github.com) | Cloud host for your vault's repository | Free | github.com |
| Obsidian Git plugin | Auto-commit + push from inside Obsidian | Free | Community plugin |
| Obsidian | Your vault | Free | obsidian.md |

> 💡 *Everything here is free. GitHub's free tier is more than enough for a personal vault.*

---

## 🧠 Background: What Are Git and GitHub?

**[[Git]]** is a tool that tracks every change you make to files over time — like an unlimited undo history for your entire vault. Every time you "commit," Git saves a snapshot of your notes at that moment.

**[[GitHub]]** is a website that stores your Git history in the cloud, so your vault is backed up online and accessible from any device.

Think of it this way:
- **Git** = the camera that takes photos of your vault
- **GitHub** = the photo album stored safely in the cloud
- **Commit** = pressing the shutter button ("save this moment")
- **Push** = uploading the new photos to the album

---

## 📦 Step-by-Step Instructions

### Step 1 — Install Git on Your Computer *(~10 minutes)*

**What to do:**

**On Mac:**
1. Open Terminal (search "Terminal" in Spotlight)
2. Type `git --version` and press Enter
3. If Git is already installed, you'll see a version number — skip to Step 2
4. If not, macOS will prompt you to install Xcode Command Line Tools — click Install and wait
5. Once done, run `git --version` again to confirm it works

**On Windows:**
1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download and run the installer — accept all default settings
3. Open "Git Bash" from your Start menu
4. Type `git --version` to confirm installation

**Configure your identity** (required — Git uses this to label your commits):
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

**Expected result:** Running `git --version` returns something like `git version 2.43.0`

**Common mistake:** Skipping the identity configuration → **Fix:** Commits will fail or show "unknown user." Run the two config commands above before moving on.

---

### Step 2 — Create a GitHub Repository *(~10 minutes)*

**What to do:**
A [[repository]] (or "repo") is the GitHub home for your vault — a cloud folder that stores every version of every file.

1. Go to [github.com](https://github.com) and create a free account if you don't have one
2. Click the **+** button (top right) → **New repository**
3. Fill in the form:
   - **Repository name:** `my-ai-wiki` (or whatever you named your vault — no spaces)
   - **Description:** `My personal AI learning knowledge base`
   - **Visibility:** Choose `Private` (recommended for personal notes) or `Public` (visible to anyone — great as a portfolio)
   - **DO NOT** check "Add a README file" — your vault already has content
4. Click **Create repository**
5. GitHub shows you a page with setup commands — **keep this tab open**, you'll need it in Step 3

**Expected result:** An empty GitHub repository is created and waiting for your vault.

**Private vs. Public — which should you choose?**

| | Private | Public |
|--|---------|--------|
| Who can see it | Only you | Anyone on the internet |
| Best for | Personal reflections, drafts | Portfolios, sharing with teachers |
| Can you change later? | Yes, anytime | Yes, anytime |

> 💡 *Start private. You can always make it public later when your vault looks polished.*

---

### Step 3 — Connect Your Vault to GitHub *(~15 minutes)*

**What to do:**
Turn your vault folder into a Git repository and link it to GitHub.

1. Open Terminal (Mac) or Git Bash (Windows)
2. Navigate into your vault folder:
   ```bash
   cd "/path/to/your/vault"
   ```
   > **Tip:** On Mac, type `cd ` (with a space), then drag your vault folder from Finder into the Terminal window — it will auto-fill the path.

3. Initialize Git in your vault:
   ```bash
   git init
   ```

4. Create a `.gitignore` file to exclude Obsidian's internal config (you don't want to sync this):
   ```bash
   echo ".obsidian/workspace.json" > .gitignore
   echo ".obsidian/workspace-mobile.json" >> .gitignore
   echo ".trash/" >> .gitignore
   ```

5. Stage all your vault files for the first commit:
   ```bash
   git add .
   ```

6. Make your first commit — this is your "starting snapshot":
   ```bash
   git commit -m "Initial vault commit"
   ```

7. Connect your local vault to your GitHub repository (copy the exact URL from the GitHub tab you left open):
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   ```

8. Push your vault to GitHub:
   ```bash
   git push -u origin main
   ```
   > If it asks for your GitHub password, use a **Personal Access Token** instead (GitHub disabled password auth in 2021). See the troubleshooting table below.

**Expected result:** Refresh your GitHub repository page — you should see all your vault files listed there.

**Troubleshooting:**

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| `fatal: not a git repository` | You're in the wrong folder | Run `pwd` to check your location, use `cd` to navigate to vault |
| `remote origin already exists` | You ran Step 7 twice | Run `git remote remove origin` then try Step 7 again |
| `Authentication failed` | GitHub requires a token, not a password | Create a Personal Access Token at github.com → Settings → Developer Settings → Tokens |
| `error: src refspec main does not match` | Git uses `master` not `main` | Replace `main` with `master` in the push command |

---

### Step 4 — Install Obsidian Git Plugin for Auto-Backup *(~15 minutes)*

**What to do:**
Typing Git commands every time you study is tedious. The Obsidian Git plugin automates it — your vault backs up on a timer, silently in the background.

1. In Obsidian: **Settings → Community Plugins → Browse**
2. Search `Obsidian Git` → Install → Enable
3. Open the plugin settings (Settings → Obsidian Git):

| Setting | Recommended Value | Why |
|---------|------------------|-----|
| **Auto pull interval** | `10` minutes | Sync from GitHub when you open Obsidian |
| **Auto commit-and-sync interval** | `30` minutes | Save automatically every 30 min while you work |
| **Commit message** | `vault backup: {{date}}` | Every commit is timestamped automatically |
| **Pull updates on startup** | ✅ Enabled | Always start with the latest version |

4. Test it manually: open the Command Palette (`Cmd/Ctrl + P`) → search `Obsidian Git: Commit all changes` → run it
5. Check your GitHub repo — a new commit should appear within seconds

**Expected result:** Your vault now auto-commits every 30 minutes and pushes to GitHub without you having to do anything.

**Common mistake:** Not setting up GitHub authentication before installing the plugin → **Fix:** Complete Step 3 first. The plugin needs Git to already be configured and authenticated.

---

### Step 5 — Read Your Commit History *(~10 minutes)*

**What to do:**
Your Git history is a timeline of every change you've ever made — a record of your learning journey.

**In Terminal:**
```bash
git log --oneline
```
This shows a compact list like:
```
a3f2c1b vault backup: 2026-04-12 21:30
9d8e7a6 vault backup: 2026-04-12 21:00
b1c4d5e Added Machine Learning concept note
3e2f1a0 Initial vault commit
```

**In Obsidian:**
- Open the Command Palette → `Obsidian Git: Open source control view`
- You'll see a visual timeline of all your commits

**In GitHub:**
- Visit your repository → click **Commits** (above the file list)
- Click any commit to see exactly which lines were added (green) or removed (red)

**Reflect:** Look at your 10 most recent commits.
- *What days did you study most?*
- *Which notes changed the most?*
- *Can you see your understanding deepen over time?*

---

### Step 6 — Recover a Previous Version *(~10 minutes)*

**What to do:**
This is the superpower of Git — you can go back to any version of any note, any time.

**Scenario:** You edited a note yesterday and now it's a mess. You want yesterday's version back.

**Option A — Recover one file (safest):**
```bash
# Find the commit ID from git log
git log --oneline 06-Resources/📋 TEMPLATES/SKILL-2-Concept-Note.md

# Restore that file to a specific commit
git checkout COMMIT-ID -- "path/to/your-note.md"
```

**Option B — View an old version without changing anything:**
1. Go to your GitHub repository
2. Click on any note file → click **History** (top right)
3. Click any past commit → you'll see exactly what the note looked like at that moment
4. Copy what you need, paste it back into Obsidian

**Option C — Obsidian Git's built-in file history:**
- Right-click any note in Obsidian → `Obsidian Git: View file history`
- Browse through versions visually

**Expected result:** You can find and restore any previous version of any note without losing current work.

---

## ⭐ Grading Rubric

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|----------------|----------------|
| **Git setup** | Git installed, identity configured, working | Installed but minor config issue | Installed, not configured | Not installed |
| **GitHub repo** | Repo created, vault pushed, all files visible | Most files pushed | Partial push | Not connected |
| **Obsidian Git plugin** | Auto-commit running; commit history shows regular entries | Plugin installed, manual commits only | Plugin installed, not working | Not installed |
| **Commit history** | 5+ meaningful commits with timestamps | 3–4 commits | 1–2 commits | No commits |
| **Recovery test** | Successfully viewed or restored an old version | Located old version in GitHub | Attempted but didn't complete | Not attempted |

**Total: \_\_ / 20**

---

## 🚀 Extension Challenges

- **Level Up 1:** Write a meaningful commit message for each study session instead of the auto-generated one — e.g., `"added neural networks concept note, linked to ML overview"`. Your commit log becomes a readable learning diary.
- **Level Up 2:** Make your repository **public** and share the link. Your vault is now a public portfolio that teachers, colleges, or employers can see.
- **Level Up 3:** Learn two branches — keep `main` for polished, published notes and create a `drafts` branch for works-in-progress. Merge to main when a note is ready. This mirrors professional software development workflow.

---

## 🤝 Ethics Checkpoint

- If your repository is **public**, anyone can see your notes — including personal reflections in Daily Notes. What would you keep private, and how? (Hint: `.gitignore`)
- If you use Claude to help write notes and push them to a public repo, should you disclose that AI assisted you? Why?
- Git tracks **every deletion** as well as every addition. Does knowing that nothing is truly "deleted" change how you write first drafts?

---

## 🔑 New Terms — Added to Glossary

- **[[Git]]** — version control tool
- **[[GitHub]]** — cloud repository host
- **[[Repository]]** — the tracked project folder
- **[[Commit]]** — a saved snapshot of changes
- **[[Push]]** — uploading commits to GitHub
- **[[Pull]]** — downloading commits from GitHub
- **[[.gitignore]]** — file listing paths Git should not track

> 📖 See full definitions: [[Glossary]]

---

## 🔗 Related Notes

- [[Build Your Own Wiki - Project]]
- [[Obsidian Best Practices - Project]]
- [[AI Learning Habits - Project]] ← mentions Git as backup Option B
- [[What is Obsidian - Concept Note]]
- [[Claudian plugin]]
