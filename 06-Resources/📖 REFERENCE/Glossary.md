---
title: "AI Knowledge Base — Glossary"
type: reference
tags: [glossary, reference, definitions, AI, obsidian]
status: published
created: 2026-04-12
---

# 📖 Glossary

> **Maintainance Rule:** Every new technical term introduced in any note must have an entry here.  
> Definitions should be written at **middle-school reading level** — clear enough for an 11-year-old, accurate enough for an 18-year-old.  
> Format: `**Term** — Definition. → [[Source Note]]`

---

## How to Use This Glossary

- **Students:** Look up any word you don't understand. Every term links back to the note where it's taught.
- **Teachers / Claude:** When adding a new term to any note's "Key Terms" section, add the same term here immediately.
- **Linking rule:** In notes, write terms as `[[Term]]` so they link directly to the glossary entry.

---

## 🤖 A — AI & Machine Learning

**Big Data** — Extremely large collections of data that are too big for a regular computer to handle on its own. AI systems need big data to learn from — the more examples you give them, the better they get. Think of it like studying for a test with 10 questions vs. 10 million questions. → [[Interactive-Learning-Platforms]]

**Code.org** — A free educational website with game-like coding lessons for students of all ages. It uses drag-and-drop code blocks (no typing required at first!) to teach programming concepts like loops, events, and conditionals. → [[Interactive-Learning-Platforms]]

**Google AI Quests** — A collection of interactive, self-guided learning missions from Google Research that teach how AI and big data work in the real world — through short readings, visuals, and hands-on mini-activities. → [[Interactive-Learning-Platforms]]

**Algorithm** — A set of step-by-step instructions a computer follows to solve a problem or complete a task — like a recipe, but for machines. → [[What is Obsidian - Concept Note]]

**Anthropic** — The AI safety company founded in 2021 that built Claude. Their mission is to research and develop AI that is safe, honest, and beneficial for humanity. → [[What is Claude Code - Concept Note]]

**Artificial Intelligence (AI)** — The field of computer science focused on building machines that can perform tasks that normally require human intelligence — like understanding language, recognizing images, making decisions, or learning from experience.

**Bias (AI Bias)** — When an AI system produces unfair or skewed results because the training data it learned from was unrepresentative or reflected human prejudices. Example: a face-recognition system that works better on some skin tones than others because most training photos were of one group.

**Computer Vision** — A branch of AI that teaches computers to "see" and interpret images and videos — used in facial recognition, self-driving cars, medical imaging, and more.

**Dataset** — A collection of data (examples, images, text, numbers) used to train or test an AI model. The quality and diversity of a dataset directly affects how well the AI learns.

**Deep Learning** — A type of machine learning that uses neural networks with many layers to learn from large amounts of data. Most modern AI breakthroughs — image recognition, voice assistants, language models — use deep learning.

**Feature** — A measurable piece of information used as input to a machine learning model. Example: in a spam detector, features might include the number of exclamation marks, the sender's address, or specific words in the subject line.

**Inference** — When a trained AI model is used to make predictions or decisions on new, unseen data. "Training" is studying; "inference" is taking the test.

**Label** — In supervised learning, a label is the correct answer attached to a piece of training data. Example: an image labeled "cat" tells the model what that image represents, so it can learn to recognize cats.

**Machine Learning (ML)** — A type of AI where computers learn patterns from data instead of following explicit step-by-step rules. Instead of programming "if this, then that," you show the model thousands of examples and it figures out the pattern. → [[What is Claude Code - Concept Note]]

**Model** — The result of training a machine learning algorithm on data — the "brain" that has learned patterns and can now make predictions. A model is what gets deployed in real applications.

**Natural Language Processing (NLP)** — A branch of AI focused on helping computers understand, interpret, and generate human language (text and speech). Powers chatbots, translation tools, voice assistants, and large language models.

**Neural Network** — A type of machine learning model loosely inspired by how neurons in the brain connect and fire. Made of layers of connected "nodes" that pass and transform information to detect patterns.

**Overfitting** — When a model learns the training data too well — including its noise and quirks — and performs poorly on new data. Like memorizing exam answers without understanding the concepts.

**Supervised Learning** — A type of machine learning where the model trains on labeled data (examples with correct answers). The model learns to map inputs to outputs by studying thousands of examples.

**Training Data** — The dataset used to teach a machine learning model. The model adjusts its internal settings ("weights") based on this data until it can make accurate predictions.

**Unsupervised Learning** — A type of machine learning where the model finds patterns in data that has no labels — it discovers structure on its own. Used for clustering, anomaly detection, and dimensionality reduction.

---

## 🎵 A — Audio & Music

**BPM (Beats Per Minute)** — A number that describes how fast or slow a piece of music is — it counts how many musical beats happen in one minute. A slow ballad might be 60 BPM; a fast trap beat is usually 130–160 BPM. → [[Music Sampler Web App - Project]]

**Howler.js** — A free, open-source JavaScript library that makes it easy to load and play audio files in a web browser. It handles the tricky parts automatically — like unlocking audio after a user click, looping, volume control, and cross-browser compatibility. → [[Music Sampler Web App - Project]]

**Royalty-Free** — A type of media license that lets you use a piece of audio, music, or image in your project without paying a fee every time it's used. You may still need to credit the creator. Looperman samples are royalty-free. → [[Music Sampler Web App - Project]]

**Sampler** — A device or app that stores a collection of short recorded sounds (called "samples") and plays them back instantly when triggered by a button, pad, or keyboard key. Beat machines, drum pads, and music production apps all work as samplers. → [[Music Sampler Web App - Project]]

---

## 🎮 A — Arrays & Algorithms

**Array** — An ordered list of items stored in a single variable in code. Each item has an index number starting at 0. In Snake, the entire body of the snake is one array — each element is an [x, y] position. Adding to the front and removing from the back makes the snake appear to move. → [[Snake-Game-Builder]]

**Collision Detection** — The logic in a game or simulation that checks whether two objects are occupying the same space. In Snake, collision detection checks if the head has hit a wall, itself, or food — and decides what happens next. The same technique is used in self-driving cars and robotics. → [[Snake-Game-Builder]]

**Pathfinding** — An algorithm that finds the best route from one point to another while avoiding obstacles. Used in GPS navigation, game enemy AI, robotics, and the Snake AI mode. The most famous pathfinding algorithm is called BFS (Breadth-First Search). → [[Snake-Game-Builder]]

---

## 🌐 B — Build & Deployment

**Build Command** — The instruction a deployment platform (like Vercel) runs to compile your project into files ready for the internet — e.g., `npm run build` or `next build`. If this command fails, the deployment fails. → [[How to Deploy to Vercel - Lesson Plan]]

**Build Log** — A real-time transcript of every step Vercel executes while building and deploying your project. When a deployment fails, the build log shows exactly which step broke and why — the developer's primary debugging tool. → [[Reading Build Logs and Debugging - Concept Note]]

**Backend** — The server-side part of a web application that users never see directly — it stores data in databases, handles login logic, and makes secure API calls. Because users can't see it, this is where secret API keys and business logic belong. → [[Frontend vs Backend - Concept Note]]

---

## 🔧 C — Claude & AI Tools

**API (Application Programming Interface)** — A way for two pieces of software to talk to each other. When the Claudian plugin sends your question to Claude, it uses Anthropic's API to do so — think of it as a standardized "power socket" for connecting apps.

**Multi-Agent Architecture** — A design pattern where a complex task is split across multiple specialised agents or tools, each doing what it does best. For example: one agent scrapes a website, another analyses the data, a third writes results to Notion. Like a team where each person has a clear role. → [[Colect-Wrong-Math-Qestions-Project]]

**Playwright** — A free Python (and JavaScript) library that lets you control a web browser automatically from code — clicking buttons, filling forms, and reading page content without a human touching the mouse. Used in the DrFrost sync project to log in and call APIs. → [[Colect-Wrong-Math-Qestions-Project]]

**REST API** — A standard way for web apps to share data over the internet, returning clean structured data (usually JSON) instead of HTML. Most modern apps have a hidden REST API underneath — even if they don't advertise it. → [[Colect-Wrong-Math-Qestions-Project]]

**Single Sign-On (SSO)** — A login system that lets one account (like Microsoft or Google) authenticate you across many different services, so you only need one password. Automating SSO requires following the redirect chain between sites. → [[Colect-Wrong-Math-Qestions-Project]]

**Claude Artifacts** — A feature in Claude (at claude.ai) that generates live, interactive previews of code directly in the chat window — things like games, web apps, charts, and calculators that you can use immediately without any setup. Built using HTML, CSS, and JavaScript. → [[Claude-Artifacts-Game-Builder]]

**Claude Code** — An AI coding and knowledge assistant built by Anthropic that runs in your terminal or editor. Unlike a chatbot, it can read and edit files in your project, giving it full context to help with real work. → [[What is Claude Code - Concept Note]]

**Claude.md** — A special plain-text file placed in the root of a vault or project folder. It tells Claude about the project's purpose, goals, audience, and rules — acting like a permanent system prompt that shapes every interaction. → [[What is Claude Code - Concept Note]]

**Claudian Plugin** — A community plugin for Obsidian that connects Claude AI directly to your vault, letting you ask questions and generate content without leaving your notes. → [[Claudian plugin]]

**Context Window** — The maximum amount of text (measured in "tokens") that a language model can process at one time — its working memory. A larger context window means Claude can read more of your vault in one conversation. → [[What is Claude Code - Concept Note]]

**Large Language Model (LLM)** — A type of AI model trained on massive amounts of text data to understand and generate human language. Claude, GPT-4, and Gemini are all LLMs. They predict the most likely next word given the context — billions of times — to produce coherent text. → [[What is Claude Code - Concept Note]]

**MCP (Model Context Protocol)** — An open standard created by Anthropic that lets Claude connect to external tools and data sources — like your file system, calendar, web search, or databases — in a safe, controlled way. → [[What is Claude Code - Concept Note]]

**Managed Agent** — A Claude AI configured to autonomously complete multi-step tasks by using tools, making decisions, and looping until the job is done — without a human directing every single step. Think of it as giving Claude a goal instead of a command. → [[Claude Managed Agents - Concept Note]]

**Agentic Loop** — The repeated cycle at the heart of every AI agent: *observe the environment → reason about what to do → act using a tool → observe the result → repeat*. The loop runs until the task is complete or an iteration limit is hit. → [[Claude Managed Agents - Concept Note]]

**Orchestrator Agent** — A high-level AI agent that breaks a big goal into smaller tasks and delegates them to sub-agents working in parallel — like a project manager directing a team. The orchestrator combines their results into a final output. → [[Claude Managed Agents - Concept Note]]

**Sub-Agent** — A specialist AI agent that handles one focused part of a larger workflow, directed by an orchestrator agent. Sub-agents can run at the same time (parallel), making complex pipelines faster. → [[Claude Managed Agents - Concept Note]]

**Tool Use** — The ability for an AI model to call external functions — like web search, reading files, running code, or calling an API — giving it "hands" to act in the real world beyond just generating text. → [[Claude Managed Agents - Concept Note]]

**Computer Use** — A Claude capability (currently in beta) that lets an AI agent see a computer screen via screenshots and control it with mouse and keyboard actions — enabling automation of any desktop software, not just APIs. → [[Claude Managed Agents - Concept Note]]

**Prompt Injection** — A security attack where malicious text hidden in content an agent reads (emails, webpages, documents) tries to override the agent's original instructions and make it do something harmful or unintended. → [[Claude Managed Agents - Concept Note]]

**Prompt** — The text input you give to an AI model — your question, instruction, or request. The quality of your prompt heavily influences the quality of the response.

**Prompt Engineering** — The skill of designing effective prompts to get better, more useful responses from AI models. Involves specifying role, task, context, format, and constraints clearly. → [[AI Learning Habits - Project]]

**System Prompt** — A set of instructions given to an AI before a conversation begins, setting its role, tone, and rules. Claude.md functions as a system prompt for the Claudian plugin. → [[What is Claude Code - Concept Note]]

**Token** — The basic unit of text that language models process — roughly ¾ of a word. "Hello world" = 2 tokens. Models have a maximum token limit per conversation (the context window).

**Vercel API Token** — A secret key generated in the Vercel dashboard that gives external tools permission to control your Vercel account via the API. Must be stored securely, never in code. → [[Environment Variables and API Key Security - Concept Note]]

---

## 🚀 D — Deployment & Web

**CI/CD** — Continuous Integration / Continuous Deployment: the practice of automatically building, testing, and deploying code every time a developer pushes a change. Vercel implements CI/CD — push to GitHub, and your live site updates within seconds. → [[What is Vercel - Concept Note]]

**Database** — A structured system for storing and retrieving data that a backend application reads from and writes to. Examples: user accounts, posts, messages. Databases live on the server, never in the browser. → [[Frontend vs Backend - Concept Note]]

**Dependency** — An external package or library your project needs to run, listed in `package.json`. If a dependency is missing when Vercel builds your project, the build fails with "Cannot find module." → [[Reading Build Logs and Debugging - Concept Note]]

**Deployment** — The process of taking code from your computer (or GitHub) and making it live and accessible on the internet so anyone with the URL can use it. → [[How to Deploy to Vercel - Lesson Plan]]

**Domain Name** — The human-readable web address of a site (e.g., `google.com`, `myproject.vercel.app`). You can connect a custom domain to any Vercel project — usually purchased for $10–15/year. → [[What is Vercel - Concept Note]]

---

## 💻 E — Environment & Security

**Environment Variable** — A named value stored outside your code (in the operating system or a hosting platform like Vercel) that your app reads at runtime. Used to store secrets like API keys so they never appear in your code files. → [[Environment Variables and API Key Security - Concept Note]]

**API Key** — A secret string of characters that identifies and authorizes your app when calling an external service's API. Treat it like a password — never put it in code or push it to GitHub. → [[Environment Variables and API Key Security - Concept Note]]

**.env file** — A local-only file containing environment variables in `KEY=value` format (e.g., `ANTHROPIC_API_KEY=sk-ant-...`). Must always be listed in `.gitignore` so it never gets pushed to GitHub. → [[Environment Variables and API Key Security - Concept Note]]

**Exit Code** — A number returned by a program when it finishes. `0` means success; any other number means failure. "Exit code 1" in a Vercel build log means your build script crashed — look above that line for the real error. → [[Reading Build Logs and Debugging - Concept Note]]

---

## 🎨 D — Design Tools

**design.md** — A plain Markdown file exported from Google Stitch that describes your entire design system — colors, fonts, spacing, and component patterns — in a format that AI coding tools like Claude can read and apply consistently when building your frontend. → [[Google Stitch - Design with AI]]

**frontend-design (Skill)** — A built-in Claude Code skill that generates distinctive, production-grade frontend interfaces directly from a description. It commits to a bold aesthetic direction (typography, color, motion, layout) and deliberately avoids the generic "AI-generated" look. → [[frontend-design Skill - Build UI with Claude]]

**Google Stitch** — A free, browser-based AI design tool from Google Labs that turns a text description or sketch into polished UI screens. It generates a full design system and lets you export a `design.md` file for AI coding tools to build from. → [[Google Stitch - Design with AI]]

---

## ⚛️ F — Frameworks & Build Tools

**Component (React)** — A reusable, self-contained piece of UI code in React — like a custom building block. A SamplerPad, a NavBar, and a VolumeSlider are all components. You define a component once and use it as many times as you need. → [[Music Sampler Web App - Project]]

**npm (Node Package Manager)** — The command-line tool used to install JavaScript libraries (called "packages") into your project. Running `npm install howler` adds Howler.js; running `npm run build` compiles your project for deployment. → [[Music Sampler Web App - Project]]

**Props (React)** — Short for "properties" — the settings you pass into a React component to customize how it looks or behaves. Like arguments to a function: `<SamplerPad name="KICK" color="#ff0" isPlaying={true} />` passes three props to the pad. → [[Music Sampler Web App - Project]]

**React** — A popular JavaScript library for building user interfaces. It organizes a webpage into reusable "components" — small, independent pieces of UI — and efficiently updates only the parts of the page that change. → [[Music Sampler Web App - Project]]

**Tailwind CSS** — A CSS framework where you style elements by adding short utility class names directly in your HTML or JSX — like `bg-black`, `text-white`, `p-4`, `rounded-xl` — instead of writing a separate CSS file. → [[Music Sampler Web App - Project]]

**Vite** — A fast, modern build tool for starting and running JavaScript projects (especially React) during development. Much faster than older tools — it starts in under a second and updates the browser instantly when you save a file. → [[Music Sampler Web App - Project]]

---

## 🖥️ F — Frontend & Web

**Frontend** — The part of a web application that runs in the user's browser — HTML, CSS, and JavaScript that create the visual interface. Frontend code is always public; never put secrets here. → [[Frontend vs Backend - Concept Note]]

**Canvas API** — A built-in browser tool that lets JavaScript draw shapes, colors, images, and animations onto an HTML `<canvas>` element — like a digital whiteboard your code can paint on. Snake's entire game board, snake body, and food are all drawn with the Canvas API. → [[Snake-Game-Builder]]

**Game Loop** — The heart of any video game: a cycle that runs many times per second, checking for player input, updating the game state (score, positions, collisions), and redrawing the screen. Almost every game — from Snake to Fortnite — runs on a game loop. → [[Claude-Artifacts-Game-Builder]]

**HTML (HyperText Markup Language)** — The standard language used to create the structure and content of web pages. HTML uses "tags" like `<button>`, `<h1>`, and `<div>` to organize text, images, and interactive elements. → [[Claude-Artifacts-Game-Builder]]

**CSS (Cascading Style Sheets)** — The language that controls how HTML elements look — colors, fonts, sizes, spacing, animations, and layout. While HTML is the skeleton, CSS is the clothing and decoration. → [[Claude-Artifacts-Game-Builder]]

**JavaScript** — The programming language that makes web pages interactive and dynamic. It responds to user actions (like clicks and key presses), updates content without reloading, and powers all browser-based games and apps. → [[Claude-Artifacts-Game-Builder]]

---

## 📚 O — Obsidian & Vault

**Daily Note** — A note in Obsidian automatically named with today's date (e.g., `2026-04-12 Daily`). Used as a learning log or journal to track what you studied, what confused you, and what you want to explore next. → [[AI Learning Habits - Project]]

**Commit** — A saved snapshot of all changes made to a Git repository at a specific point in time. Like pressing "save" on your entire vault — every commit is permanently recorded with a timestamp and message. → [[GitHub Vault Backup - Project]]

**Dataview** — A powerful Obsidian community plugin that lets you query your notes like a database — e.g., "show me all notes tagged `status: draft`, sorted by date." Useful for building dynamic indexes and to-do lists.

**.gitignore** — A special file in a Git repository that lists files and folders Git should never track or upload. Used in Obsidian vaults to exclude internal config files like `.obsidian/workspace.json` that shouldn't be shared. → [[GitHub Vault Backup - Project]]

**Git** — A free, open-source tool that tracks every change made to files in a folder over time, creating a full version history. Used by developers and students to back up work and collaborate without losing anything. → [[GitHub Vault Backup - Project]]

**GitHub** — A website that stores Git repositories in the cloud, making them accessible from anywhere and shareable with others. Think of it as Google Drive, but specifically designed for tracked, versioned files. → [[GitHub Vault Backup - Project]]

**Frontmatter** — A block of YAML metadata placed at the very top of a Markdown note, between `---` lines. It holds structured information about the note — title, tags, status, date — that Obsidian and plugins can read and filter. → [[What is Obsidian - Concept Note]]

**Graph View** — A built-in Obsidian feature that displays all your notes as dots (nodes) and all wikilinks as lines (edges), creating a visual map of your knowledge web. Orphan notes (no connections) appear as isolated dots. → [[What is Obsidian - Concept Note]]

**Markdown** — A lightweight text formatting language used for all Obsidian notes. Uses simple symbols: `**bold**`, `*italic*`, `# Heading 1`, `- bullet point`, `[[wikilink]]`. Files are saved as plain `.md` text files. → [[What is Obsidian - Concept Note]]

**MOC (Map of Content)** — A special note that acts as a table of contents or index for a topic — it links to all related notes in one place, making it the hub of a topic web in your graph. → [[Obsidian Best Practices - Project]]

**Obsidian** — A free, local-first note-taking app where notes are Markdown files stored on your computer. Its superpower is wikilinks and Graph View — turning individual notes into an interconnected knowledge base. → [[What is Obsidian - Concept Note]]

**Orphan Note** — A note in Obsidian that has no wikilinks pointing to it or from it — it floats alone in the graph with no connections. Orphan notes are a signal that a concept hasn't been integrated into your knowledge web yet. → [[AI Learning Habits - Project]]

**PKM (Personal Knowledge Management)**

**Pull** — Downloading the latest commits from a GitHub repository to your local computer. Keeps your local vault in sync with the cloud version, especially useful when working across multiple devices. → [[GitHub Vault Backup - Project]]

**Push** — Uploading your local Git commits to a GitHub repository. This is how your vault gets backed up to the cloud after you commit changes. → [[GitHub Vault Backup - Project]]

**PKM (Personal Knowledge Management)** — The practice of intentionally capturing, organizing, connecting, and using information to support thinking and learning. Obsidian is one of the most popular PKM tools.

**Plugin** — An add-on that extends Obsidian's built-in features. Core plugins come with Obsidian; Community plugins are built by users. Examples: Daily Notes (core), Dataview (community), Claudian (community). → [[What is Obsidian - Concept Note]]

**Repository** — A project folder tracked by Git, containing all your files plus the complete history of every change ever made. Your Obsidian vault becomes a repository when you run `git init` inside it. → [[GitHub Vault Backup - Project]]

**Vault** — The root folder that contains all of your Obsidian notes and configuration. Everything inside the vault folder is part of your knowledge base. Multiple vaults can exist on one computer. → [[What is Obsidian - Concept Note]]

**Wikilink** — A link between two notes created by wrapping a note name in double square brackets: `[[Note Name]]`. Clicking a wikilink opens the linked note; Obsidian draws these as edges in the Graph View. → [[What is Obsidian - Concept Note]]

**YAML** — A human-readable data format used for Obsidian frontmatter. Uses `key: value` pairs between `---` lines at the top of a note. Stands for "YAML Ain't Markup Language."

---

## 💾 L — Local Storage & Browser Data

**localStorage** — A browser feature that lets a website save small pieces of data (like high scores or settings) directly on your computer. The data stays saved even after you close the tab or restart your computer — until you clear your browser data. Snake uses localStorage to remember your high score. → [[Snake-Game-Builder]]

---

## 🔁 P — Publishing & Hosting

**Preview Deployment** — A temporary live URL that Vercel automatically creates for every branch or pull request, letting you test changes on the real internet before merging them into your main (production) site. → [[What is Vercel - Concept Note]]

**Hosting** — Storing your website's files on a server and serving them to anyone who visits your URL. Vercel handles all hosting infrastructure so you only write code, not manage servers. → [[What is Vercel - Concept Note]]

---

## 🔁 R — Runtime & Logs

**Runtime Log** — A record of errors that happen in your live app *after* deployment — when users interact with it and something crashes. Separate from the build log, which only covers the build phase. → [[Reading Build Logs and Debugging - Concept Note]]

---

## 📐 S — Skills & Templates

**Concept Note** — A type of note (Skill 2) that provides a deep-dive explanation of a single topic — includes a core concept summary, analogies, misconceptions, key terms, a "Try It" activity, and an ethics connection. → [[SKILL-2-Concept-Note]]

**Discussion Guide** — A type of note (Skill 4) containing structured questions at three difficulty levels (Recall → Analysis → Ethics) for facilitating classroom conversation on a topic. → [[SKILL-4-Discussion]]

**Lesson Plan** — A type of note (Skill 3) that structures a full classroom lesson — hook, direct instruction, guided practice, independent activity, discussion, and exit ticket. → [[SKILL-3-Lesson-Plan]]

**Module Overview** — A type of note (Skill 1) that provides the high-level curriculum blueprint for a topic — learning objectives, weekly structure, prerequisites, and assessment plan. → [[SKILL-1-Module-Overview]]

**Naming Convention** — A consistent rule for naming files and folders so they are predictable and wikilinks resolve correctly. This vault uses `{{TOPIC}} - Type` (e.g., `Machine Learning - Concept Note`). → [[Obsidian Best Practices - Project]]

**Skill Template** — A reusable note structure for a specific type of content (concept note, lesson plan, quiz, etc.) using `{{TOPIC}}` as a placeholder. Copying a skill template and replacing `{{TOPIC}}` creates a new, fully cross-linked note. → [[00-SKILLS-INDEX]]

**Topic Suite** — The full set of 6 notes (Module Overview, Concept Note, Lesson Plan, Discussion, Project, Quiz) created from skill templates for a single topic. All 6 notes cross-link to each other automatically through the `{{TOPIC}} - Type` naming pattern. → [[Templates and Skills Practice - Project]]

---

## 🌍 V — Vercel & Deployment Tools

**Vercel** — A free cloud platform that automatically builds and deploys web projects from GitHub. Every `git push` triggers a new deployment in about 30 seconds, with a live `.vercel.app` URL. Used by students and large companies alike. → [[What is Vercel - Concept Note]]

**Vercel Plugin** — A personal plugin for Claude Code (installed with `npx plugins add vercel/vercel-plugin`) that turns Claude into a Vercel expert. It automatically injects Vercel skills, provides specialist agents, and enables slash commands — all triggered by lifecycle hooks that watch what you're working on. → [[Claude Code Vercel Plugin - Concept Note]]

**Static Site** — A website made entirely of fixed files (HTML, CSS, JavaScript) with no server-side processing. Static sites are the simplest type to deploy — Vercel can host them with zero configuration. → [[Frontend vs Backend - Concept Note]]

**Serverless Function** — A small piece of backend code that runs only when it's called (on demand), without needing a full-time server running. Vercel runs serverless functions automatically — ideal for securely calling APIs like Claude without a dedicated backend server. → [[Frontend vs Backend - Concept Note]]

**Skill Injection** — The Vercel Plugin's ability to automatically add deep Vercel knowledge to Claude's context when it detects relevant file paths or commands — e.g., editing `next.config.ts` injects the `nextjs` skill without you having to ask. → [[Claude Code Vercel Plugin - Concept Note]]

**Specialist Agent** — A focused mode of Claude with deep expertise in one domain, provided by the Vercel Plugin. The three agents are `deployment-expert`, `performance-optimizer`, and `ai-architect` — invoked on demand for focused tasks. → [[Claude Code Vercel Plugin - Concept Note]]

**Slash Command** — A typed command starting with `/` that triggers a specific action inside Claude Code. The Vercel Plugin provides five: `/vercel-plugin:deploy`, `/vercel-plugin:env`, `/vercel-plugin:status`, `/vercel-plugin:bootstrap`, and `/vercel-plugin:marketplace`. → [[Claude Code Vercel Plugin - Concept Note]]

**Harness** — The invisible runtime engine wrapped around Claude Code that provides tools, fires hooks at the right moments, enforces permissions, and turns Claude from a chatbot into an autonomous agent. You configure it via `settings.json`; it works silently in the background every session. → [[What is the Claude Code Harness - Concept Note]]

**Harness Engineering** — The practice of designing and configuring the Claude Code harness to create persistent, automatic behaviors — by writing hooks, setting permissions, and using skills in `settings.json`. Like programming the rules of the environment Claude lives in. → [[What is the Claude Code Harness - Concept Note]]

**Hook** — An automatic trigger in Claude Code that fires at a specific lifecycle moment (like "before writing a file") and runs a shell command. The output of that command is injected into Claude's context — so Claude gets new knowledge without you having to ask. → [[Claude Code Hooks - Concept Note]]

**Hooks** — Automatic triggers built into a plugin that fire at specific moments in a Claude Code session. The Vercel Plugin uses four hooks: session-start context injection, session-start repo profiling, pre-tool-use skill injection, and pre-write validation. → [[Claude Code Vercel Plugin - Concept Note]]

**Lifecycle Event** — A predictable stage in a Claude Code session — like "session starts," "before a file is written," or "after a tool is used" — where hooks can attach and fire automatically. Think of it as a named checkpoint in a relay race where a baton (instruction) can be passed. → [[Claude Code Hooks - Concept Note]]

**Matcher** — The pattern inside a hook definition that determines which tool or event triggers the hook. For example, `"matcher": "Write"` means the hook only fires when Claude uses the Write tool. → [[Claude Code Hooks - Concept Note]]

**PostToolUse** — A Claude Code hook type that fires *after* a tool completes its action — useful for logging what happened, triggering follow-up checks, or chaining one action after another automatically. → [[What is the Claude Code Harness - Concept Note]]

**PreToolUse** — The most commonly used Claude Code hook type — fires *before* Claude uses any tool (reading, writing, running a command). Lets you inject context or validate behavior before an action happens. → [[Claude Code Hooks - Concept Note]]

**SessionStart** — A Claude Code hook type that fires the moment a new session begins — before you type anything. Perfect for automatically injecting project context, rules, or a welcome message into every session. → [[What is the Claude Code Harness - Concept Note]]

**settings.json** — The Claude Code configuration file stored at `~/.claude/settings.json`. This is where hooks, custom behaviors, and tool permissions are defined. Think of it as Claude Code's rule book — what it checks before every session. → [[Claude Code Hooks - Concept Note]]

**Skill** — A packaged set of expert instructions and harness behaviors for Claude Code, invoked with a `/skill-name` command. Skills inject specialist knowledge into Claude's context or run pre-built workflows — like calling in an expert consultant for a specific task. → [[What is the Claude Code Harness - Concept Note]]

**Ecosystem Graph** — The Vercel Plugin's relational knowledge map of the entire Vercel platform — every product, library, CLI command, and API — injected into Claude at the start of every session so it always has baseline Vercel knowledge. → [[Claude Code Vercel Plugin - Concept Note]]

**Secret** — Any sensitive value — API key, password, database connection string — that must never appear in your code or be pushed to GitHub. Secrets are stored in `.env` files locally and in hosting platform dashboards (like Vercel's Environment Variables panel) in production. → [[Environment Variables and API Key Security - Concept Note]]

---

*Last updated: 2026-04-14 (added Harness, Harness Engineering, PostToolUse, SessionStart, Skill from What is the Claude Code Harness - Concept Note) | Maintained by: Claudian (AI assistant)*  
*Rule: Every new term in any note → add it here. See [[Claude.md]] for the full rule.*
