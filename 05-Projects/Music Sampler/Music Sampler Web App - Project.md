---
title: "Music Sampler Web App"
skill: project
type: project
tags: [project, react, tailwind, howler, music, frontend-design, vercel, looperman, web-audio, high-intro]
level: high-intro
topic: claude-applications
status: draft
created: 2026-04-13
---

# 🎛️ Music Sampler Web App — Project

## 🧪 Project Brief

| Field | Details |
|-------|---------|
| **Topic** | Build a browser-based 8-pad beat sampler with real sounds |
| **Project Title** | "Beat Lab" — Your Own Music Sampler |
| **Grade Level** | `[x] High School Intro` (Grade 9–10) |
| **Duration** | 4–5 class periods (or a full weekend build) |
| **Group Size** | `[x] Solo` or `[ ] Pairs` |
| **Difficulty** | `[x] Intermediate` |
| **Tech Stack** | React · Tailwind CSS · Vite · Howler.js |
| **Prerequisites** | [[Frontend vs Backend - Concept Note]] · [[How to Deploy to Vercel - Lesson Plan]] · Basic comfort with the terminal |

---

## 🎯 What You'll Build

> 🖼️ **The vision:** A dark, studio-quality web app with 8 glowing sample pads. Click a pad — or press a keyboard key — and it fires a real hip-hop sound. The interface feels like a real music production tool, not a school project.

**Core features your sampler will have:**

- ✅ **8 sample pads** in a 2×4 grid — each plays a different sound
- ✅ **Keyboard shortcuts** — keys A, S, D, F, G, H, J, K trigger each pad
- ✅ **Visual feedback** — pads glow and pulse when a sound plays
- ✅ **Master volume slider** — control the overall volume
- ✅ **BPM display** — shows the tempo of your samples
- ✅ **Mobile-friendly** — pads respond to touch on a phone

**What you'll learn:**

- How to build a real React app from scratch using Claude Code
- How to load and play audio in the browser using Howler.js
- How to use the `frontend-design` skill to create a professional UI
- How to find and legally use sample audio from Looperman
- How to deploy a live web app with Vercel

---

## 🎵 Step 1 — Find Your Sounds on Looperman

Before writing a single line of code, you need **8 audio samples**. You'll get them from [Looperman](https://www.looperman.com) — a free library of royalty-free loops and one-shots made by real producers.

### What Is Looperman?

Looperman is a community-driven website where music producers upload free samples. Every file is **royalty-free**, meaning you can use them in your projects without paying anyone. You just can't resell or redistribute the raw sample files themselves.

### 🎹 The 8 Sounds You Need

For a hip-hop / trap style sampler, collect one file for each pad:

| Pad # | Key | Sound Type | What to Search On Looperman |
|-------|-----|------------|-----------------------------|
| 1 | A | **Kick Drum** | `trap kick` or `hip hop kick` |
| 2 | S | **Snare** | `trap snare` or `hip hop snare` |
| 3 | D | **Hi-Hat (closed)** | `trap hi hat` or `closed hat` |
| 4 | F | **Open Hi-Hat** | `open hat trap` |
| 5 | G | **Clap** | `trap clap` or `hip hop clap` |
| 6 | H | **808 Bass** | `808 bass` or `sub bass hit` |
| 7 | J | **Percussion / Rim** | `trap perc` or `rim shot` |
| 8 | K | **Melody Loop** | `trap melody loop` or `hip hop melody` |

> 💡 **Tip:** For pads 1–7, look for **one-shots** (short single hits, not loops). For pad 8, a short **melodic loop** (2–4 bars) works great.

### 🔍 How to Search Looperman Step-by-Step

1. Go to [looperman.com](https://www.looperman.com)
2. Click **"Loops"** in the top navigation
3. Use the **search bar** (e.g., type `trap kick`)
4. In the filter panel on the left, set:
   - **Genre:** Hip Hop or Trap
   - **BPM:** 80–140 (typical trap tempo range)
   - **Format:** MP3 *(most compatible with all browsers)*
5. Listen to a few previews — pick the one that sounds cleanest
6. Click the **Download** button (free, no account needed for most files)

### 📂 Rename and Organize Your Files

After downloading, rename each file to match this exact list — this makes the code much cleaner:

```
kick.mp3
snare.mp3
hihat.mp3
openhat.mp3
clap.mp3
bass808.mp3
perc.mp3
melody.mp3
```

Keep them in a folder on your Desktop called `sounds` for now. You'll move them into the project in Step 5.

> ⚠️ **Important:** Only use **MP3 or WAV** format. `.flac` and `.ogg` files are not supported in all browsers. When in doubt, pick MP3.

---

## 🛠️ Step-by-Step Build Guide in Claude Code

Work through these 9 steps in order. Each step includes the exact prompt to type in Claude Code.

---

### Step 2 — Create the React App

**What this does:** Runs the one command that creates a new React project using Vite. This is the most important command in the whole setup — the `--template react` flag is what tells Vite *which framework* to use. Without it, Vite asks you to choose interactively, which can be confusing.

**Run these commands in your terminal, one at a time:**

```bash
npm create vite@latest beat-lab -- --template react
```

```bash
cd beat-lab
```

```bash
npm install
```

```bash
npm run dev
```

**Expected result:** Your terminal shows a local address like `http://localhost:5173`. Open it in your browser — you should see the default Vite + React welcome page. This confirms Node.js, npm, and React are all working correctly.

> 💡 **What just happened?**
> - `npm create vite@latest beat-lab` — downloaded Vite and created a new project folder called `beat-lab`
> - `--template react` — told Vite to set it up as a **React** project (not Vue, Svelte, or plain JavaScript)
> - `npm install` — downloaded all the libraries the project needs
> - `npm run dev` — started a local development server so you can see your app in the browser

> ⚠️ **If `npm` is not found:** Node.js is not installed correctly. Ask your teacher — this will be resolved together in Session 1.

---

### Step 3 — Set Up Dependencies & Folder Structure

**What this does:** Installs Tailwind CSS and Howler.js, then creates the folder structure the project needs.

**Prompt to type in Claude Code:**

```
I have a new Vite + React project called "beat-lab" already running. Now I need to finish setting it up.

Please do the following:
1. Install Tailwind CSS (follow the official Vite + Tailwind setup guide)
2. Install Howler.js for audio playback
3. Create this folder structure inside /src/:
   - /components/SamplerPad.jsx   (empty component file)
   - /components/SamplerGrid.jsx  (empty component file)
   - /data/sounds.js              (empty config file)
   - /assets/sounds/              (empty folder — I'll add MP3s here)
4. Clean up the default Vite boilerplate (remove the counter demo, reset App.jsx to a blank shell)

Show me each terminal command separately so I can run them one at a time.
```

**Expected result:** A clean project with React + Tailwind running and the folder structure set up. The welcome page in the browser should now show a blank white page (the cleaned-up App.jsx).

**Common error:** Tailwind not applying styles → Ask Claude: *"My Tailwind classes aren't working. Check my tailwind.config.js content array and index.css imports."*

---

### Step 4 — Design the UI with Claude Code

You'll use Claude Code's built-in `frontend-design` skill to generate a professional interface. This skill deliberately avoids generic AI-generated designs — it commits to a bold aesthetic direction and executes it fully.

> 📖 Background reading: [[frontend-design Skill - Build UI with Claude]]

**Prompt to type in Claude Code:**

```
Use the frontend-design skill to design the full UI for an 8-pad music sampler web app.

Context:
- Genre: hip-hop / trap
- 8 pads arranged in a 2x4 grid
- Each pad shows: sample name (e.g. KICK, SNARE), keyboard shortcut key (A–K), and a glow animation when the sound is playing
- Header: app name "BEAT LAB", BPM display showing a number, master volume slider
- Vibe: dark studio session — like a real music production tool a teenager would actually use. Professional, not toy-like.
- Tech: React components with Tailwind CSS classes

Generate the full React JSX for the main App layout and a SamplerPad component. Include all Tailwind classes and CSS animations inline. Do not use any external UI libraries.
```

**What to expect:** Claude will choose a bold aesthetic direction — likely dark backgrounds with glowing accent colors, strong typography, and CSS keyframe animations for the active pad state. It may surprise you with its choices. That's the point.

**After Claude responds:**
- Read through the JSX it generates — do you understand the structure?
- Ask Claude: *"Why did you choose this visual direction? What makes it feel professional?"*
- If you want any adjustments (different color, font, layout), ask: *"Change the accent color to [color]. Keep everything else the same."*

---

### Step 5 — Add Your Sound Files

**What this does:** Moves your Looperman samples into the project so Vite can bundle them.

1. Open your `beat-lab` project folder in Finder (or File Explorer)
2. Navigate to `/src/assets/sounds/`
3. Copy all 8 MP3 files from your Desktop `sounds` folder into this folder
4. Verify the folder looks like this:

```
/src/assets/sounds/
  kick.mp3
  snare.mp3
  hihat.mp3
  openhat.mp3
  clap.mp3
  bass808.mp3
  perc.mp3
  melody.mp3
```

**Then type this prompt:**

```
Create the sounds configuration file at /src/data/sounds.js.

Define and export an array called SOUNDS with 8 objects. Each object should have:
- id: number (1–8)
- name: display name in ALL CAPS (KICK, SNARE, HI-HAT, OPEN HAT, CLAP, 808, PERC, MELODY)
- file: import path to the MP3 in /src/assets/sounds/ 
- keyBinding: keyboard key (A, S, D, F, G, H, J, K)
- color: a unique Tailwind-compatible hex color for each pad (pick colors that look great on a dark background — think neon/electric tones)

Use ES module static imports for the audio files at the top of the file (e.g., import kickSrc from '../assets/sounds/kick.mp3').
```

> 💡 **Why static imports?** Vite needs to know about your MP3 files at build time so it can bundle them. Static imports at the top of the file tell Vite: "this file is part of my project."

---

### Step 6 — Build the SamplerPad Component

**What this does:** Creates the individual pad that shows the sound name, key, and reacts when played.

**Prompt to type:**

```
Build the SamplerPad React component at /src/components/SamplerPad.jsx.

Props it should accept:
- name: string — the display name (e.g. "KICK")
- keyBinding: string — the keyboard key (e.g. "A")  
- color: string — the pad's unique hex color
- isPlaying: boolean — true while the sound is playing
- onClick: function — called when the pad is clicked

Behavior:
- When isPlaying is true: show the active/glow state with a CSS scale animation (quick punch: scale up to 1.08, then return to 1.0 in 150ms)
- The pad color should be used for the border/glow, not the background (keep the pad background dark)
- Show the keyBinding in a small pill badge in the top-right corner of the pad
- The pad name should be centered and in a bold, large font

Use only Tailwind CSS classes and inline style for the dynamic color. No external UI libraries.
Match the dark aesthetic from the UI design we generated in Step 4.
```

---

### Step 7 — Wire Up Audio and Keyboard Controls

**What this does:** Connects the pads to real sound playback and adds keyboard shortcuts.

**Prompt to type:**

```
Now wire everything together in /src/App.jsx.

Here's what I need:

1. Import Howl from 'howler' and all sounds from /src/data/sounds.js
2. On app load, create a Howl instance for each sound (preload: true). Store them in a ref or useMemo so they don't reload on every render.
3. Create a playSound(id) function that:
   - Finds the Howl instance for that id
   - Stops it if it's already playing (so rapid taps replay from start)
   - Plays it
4. Track which pad is "playing" in React state: use an object like { 1: false, 2: false, ... }. Set a pad to true when its sound starts (Howler's onplay callback), false when it ends (Howler's onend callback).
5. Add a keyboard event listener in useEffect:
   - A → playSound(1), S → playSound(2), D → playSound(3), F → playSound(4)
   - G → playSound(5), H → playSound(6), J → playSound(7), K → playSound(8)
   - Remove the listener on component unmount (cleanup function in useEffect)
6. Add a master volume slider: use Howler.Howler.volume(value) where value is 0.0 to 1.0. Wire the slider's onChange to this.
7. Render the SamplerGrid, passing down playSound and the isPlaying state for each pad.

Also build /src/components/SamplerGrid.jsx — it maps over the SOUNDS array and renders a SamplerPad for each one, in a 2x4 grid using Tailwind grid classes.
```

**Expected result:** Clicking any pad or pressing A–K plays the corresponding sound. The pad visually reacts while audio plays.

**Common error:** Sounds not playing → Ask Claude: *"My Howler sounds aren't playing. Check if the import paths in sounds.js are correct and if Howler is initialized before first user interaction."*

> 💡 **Why Howler.js?** Browsers require a user interaction before playing audio (you can't autoplay on page load). Howler handles this automatically — the first time you click a pad, it "unlocks" the browser's audio engine for the whole session.

---

### Step 8 — Polish and Final Touches

**What this does:** Adds the small details that make it feel finished and professional.

**Prompt to type:**

```
Add these finishing touches to the Beat Lab sampler. Make each change one at a time and confirm it works before moving to the next:

1. LAST PLAYED indicator: Below the pad grid, show a small text line that says "Last played: [PAD NAME]" — update it every time a pad triggers. Fade it in with a CSS opacity transition.

2. KEYBOARD GUIDE: Add a subtle hint text somewhere in the UI that says "Use A–K keys to play". Style it as secondary/muted text so it doesn't compete with the pads.

3. MOBILE TOUCH: Test that pads respond to touch events. In React, onClick handles touch automatically — but make sure the pad hit area is large enough (minimum 80px × 80px on mobile). Add a media query or Tailwind responsive class if needed.

4. MUTE toggle: Add a small mute icon button to each pad. When muted, the pad is visually dimmed and its sound doesn't play. Store mute state in the parent component as an object like { 1: false, 2: false, ... }.

5. PRE-DEPLOY BUILD CHECK: Run `npm run build` and paste me the terminal output. Fix any errors or warnings before we move to deployment.
```

---

## 🚀 Step 9 — Deploy to Vercel

Once `npm run build` completes with no errors, you're ready to go live.

> 📖 Full guide: [[How to Deploy to Vercel - Lesson Plan]] — follow that lesson for the complete walkthrough. The condensed version is below.

### Condensed Deployment Checklist

**In terminal — set up Git and push to GitHub:**

```bash
cd beat-lab
git init
git add .
git commit -m "Initial commit: Beat Lab music sampler"
```

Then create a new **public or private repository** on [github.com](https://github.com) named `beat-lab`, then:

```bash
git remote add origin https://github.com/YOUR-USERNAME/beat-lab.git
git push -u origin main
```

**On Vercel:**

1. Go to [vercel.com](https://vercel.com) → **Add New Project**
2. Import your `beat-lab` GitHub repository
3. Vercel auto-detects Vite — verify these settings:
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
4. Click **Deploy**

**After deploy:**

- Your app is live at `beat-lab-[username].vercel.app`
- Every future `git push` auto-deploys a new version
- Share the URL with your class or friends 🎉

> 💡 **Tip:** If the build fails on Vercel, use this Claude Code prompt: *"My Vercel build failed with this error: [paste build log]. What's wrong and how do I fix it?"* — also see [[Reading Build Logs and Debugging - Concept Note]].

---

## ⭐ Grading Rubric

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|----------------|----------------|
| **Audio works** | All 8 pads play distinct sounds; no errors | 6–7 pads work | 4–5 pads work | Fewer than 4 |
| **Keyboard shortcuts** | All A–K keys trigger pads reliably | Most keys work | Some keys work | Keys don't work |
| **Visual design** | Professional look; active state, colors, and layout all polished | Mostly polished, 1–2 rough spots | Functional but unpolished | No styling beyond defaults |
| **Code quality** | Components are separated, sounds.js config is clean, no unused code | Mostly clean | Some structure | All in one file, messy |
| **Deployed on Vercel** | Live URL works, loads in under 3 seconds | Live URL works | Partially deployed | Not deployed |
| **Volume + Mute** | Both volume slider and mute per pad work | One of the two works | Attempted | Not attempted |

**Total: \_\_ / 24**

---

## 🚀 Extension Challenges

- **Level Up 1 — BPM Metronome:** Add a toggleable metronome click that ticks at the displayed BPM. Use `setInterval` + a tick sound. *Hint: ask Claude, "Add a metronome that plays a click sound at 90 BPM using setInterval. Include start/stop toggle."*
- **Level Up 2 — Record a Beat:** Let users record a sequence of pad presses with timestamps, then replay the sequence automatically. This turns the sampler into a basic step sequencer.
- **Level Up 3 — Custom Samples:** Add an `<input type="file" accept="audio/*">` to each pad so users can upload their own sounds and replace the defaults.
- **Level Up 4 — Shareable Beat:** Encode the current mute/volume state in the URL query string so users can share their exact pad configuration with a link.
- **Level Up 5 — Waveform Visualizer:** Use the Web Audio API's `AnalyserNode` to draw a real-time waveform or frequency bar chart with a `<canvas>` element when a sound plays.

---

## 🤝 Ethics Checkpoint

Before you share your project, discuss these questions with a classmate or write a short reflection:

**On sampling and credit:**
- Looperman samples are royalty-free — but the producers who made them are real people. Did you credit them anywhere in your app? Should you? How could you add a credits section?
- If you pushed to a **public** GitHub repo, your MP3 files are now publicly downloadable. Is that okay under Looperman's terms? *(Check: looperman.com/terms)*

**On AI and authorship:**
- Claude Code generated most of the React code in this project. Does that make you the developer? What did *you* contribute that an AI couldn't?
- If you submitted this project in a class, what would you need to disclose about how it was built?

**On music and AI:**
- Generative AI tools (like Suno, Udio, and AIVA) can now create full songs in seconds. How is that different from using Looperman samples? Where do you think the line is between "inspiration" and "copying"?

*Write 3–4 sentences responding to any one of these questions. Save it in a note called `Beat Lab Reflection` in your vault.*

---

## 🔑 New Terms — Added to Glossary

- **[[BPM (Beats Per Minute)]]** — how fast or slow a piece of music is, measured by the number of beats in one minute
- **[[Sampler]]** — a device or app that stores short recorded sounds and plays them back when triggered
- **[[Howler.js]]** — a JavaScript audio library that makes it easy to load and play sounds in a web browser
- **[[React]]** — a JavaScript library for building user interfaces out of reusable components
- **[[Tailwind CSS]]** — a CSS framework where you style elements using short class names directly in your HTML/JSX
- **[[Vite]]** — a fast build tool for starting and running React (and other) projects during development
- **[[Royalty-Free]]** — a license that lets you use audio or media in your project without paying ongoing fees
- **[[npm (Node Package Manager)]]** — the command-line tool used to install JavaScript libraries into your project
- **[[Component (React)]]** — a reusable, self-contained piece of UI code in React — like a custom building block
- **[[Props (React)]]** — settings passed into a React component to customize how it looks or behaves

> 📖 See full definitions: [[Glossary]]

---

## 🔗 Related Notes

- [[frontend-design Skill - Build UI with Claude]] — the skill used to design the sampler UI
- [[Google Stitch - Design with AI]] — alternative: design the UI visually first, then hand off to Claude Code
- [[How to Deploy to Vercel - Lesson Plan]] — full deployment walkthrough
- [[What is Vercel - Concept Note]] — what Vercel is and how it works
- [[Frontend vs Backend - Concept Note]] — why this app is frontend-only
- [[Environment Variables and API Key Security - Concept Note]] — if you add a backend API later
- [[Claude Code Vercel Plugin - Concept Note]] — deploy directly from Claude Code without opening the Vercel dashboard
- [[Reading Build Logs and Debugging - Concept Note]] — what to do when the Vercel build fails
