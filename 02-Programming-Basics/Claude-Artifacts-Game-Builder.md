---
title: "Building Games with Claude Artifacts"
level: high-intro
topic: programming
status: published
created: 2026-04-13
tags: [claude-artifacts, game-dev, html, javascript, css, prompt-engineering, hands-on, interactive]
---

# 🎮 Building Games with Claude Artifacts

> **Hook:** What if you could describe a game in plain English — and have a working, playable version running in your browser in under 60 seconds? No downloads, no complicated setup — just you, a good idea, and a conversation with AI.

That's exactly what **[[Claude Artifacts]]** lets you do. In this guide, you'll go from "I have a game idea" to a fully playable, customized web game — step by step.

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Understand what Claude Artifacts are and how they work
- Write a clear, detailed prompt to generate a game
- Test and play your game directly in Claude's interface
- Use follow-up prompts to improve and personalize your game
- Export your game code so you can share or host it

**Level:** High School Intro | **Time:** 45–60 minutes  
**Prerequisites:** Basic familiarity with [[Claude]] | No coding experience required!

---

## 🤔 What Are Claude Artifacts?

When you ask [[Claude]] on [claude.ai](https://claude.ai) to build something visual — like a game, a webpage, or a data chart — it can generate the code **and** display a live, interactive preview right in the chat window. That preview is called an **[[Artifact]]**.

Think of it like this:
> 🧠 You describe the game → Claude writes the code → The Artifact *is* the game, running live

Artifacts are built using three web technologies:
| Technology | What It Does | Plain-English Analogy |
|-----------|-------------|----------------------|
| **HTML** | Creates the structure (buttons, text, layout) | The skeleton of a building |
| **CSS** | Styles the appearance (colors, fonts, animation) | The paint and decoration |
| **JavaScript** | Adds logic and interactivity (rules, score, events) | The electricity that makes it work |

You don't need to understand these to get started — Claude handles all three. But as you improve your game, you'll start to see how they fit together!

---

## 🎮 Five Game Ideas to Try

Before building, pick a game that excites you. Here are five options, from simple to more complex:

| # | Game | Difficulty | Best For | What You'll Practice |
|---|------|-----------|---------|---------------------|
| 🎯 A | **Number Guessing Game** | ⭐ Beginner | Everyone | If/else logic, loops |
| 🃏 B | **Memory Card Match** | ⭐⭐ Easy-Med | Visual learners | Arrays, DOM events |
| 🧠 **C** | **AI Trivia Quiz** | ⭐⭐ Easy-Med | This class! | Game state, UI design |
| 🐍 D | **Snake Game** | ⭐⭐⭐ Intermediate | Challenge-seekers | Game loop, collision |
| 🔨 E | **Whack-a-Mole** | ⭐⭐ Easy-Med | Quick fun | Timers, random events |

> 💡 **Class Recommendation:** We'll use **Option C — AI Trivia Quiz** as our walkthrough. It connects directly to your AI curriculum, looks impressive, and every student can make it personal by writing their own questions!

---

## 🪜 Step-by-Step: Build Your AI Trivia Quiz Game

### ✅ Step 1 — Open Claude and Start a New Chat

1. Go to [claude.ai](https://claude.ai) in your browser
2. Sign in with your account (or create a free one)
3. Click **New Chat** to start fresh
4. Make sure you're using **Claude Sonnet** or higher (check the model selector at the top)

**Expected result:** A blank chat window, ready for your prompt.

> ⚠️ **Important:** Artifacts work best on a laptop or desktop. Mobile browsers may not show the live preview.

---

### ✅ Step 2 — Write Your First Prompt

This is the most important step. A vague prompt gets a boring game; a *specific* prompt gets something amazing. Copy and paste the prompt below, or write your own version:

---

**📋 Starter Prompt (copy this!):**

```
Build me a fun AI Trivia Quiz game as an interactive HTML/CSS/JavaScript artifact. Here are the requirements:

GAME MECHANICS:
- Show one multiple-choice question at a time (4 answer options: A, B, C, D)
- Give instant feedback when an answer is clicked: show green for correct, red for wrong
- Show the correct answer if the player picks wrong
- Track and display a score (e.g., "3 / 5 correct")
- Show a results screen at the end with a fun message based on score

QUESTIONS (use these 5 AI trivia questions):
1. What does "AI" stand for?
   A) Automated Input  B) Artificial Intelligence ✓  C) Advanced Internet  D) Auto Indexing

2. Which company made Claude?
   A) Google  B) OpenAI  C) Anthropic ✓  D) Microsoft

3. What do we call the huge collection of data used to train AI?
   A) Big Data ✓  B) Cloud Storage  C) Wi-Fi  D) A Database

4. What is machine learning?
   A) Robots building machines  B) Computers learning from examples ✓  C) A coding language  D) A type of robot

5. What is a neural network inspired by?
   A) The internet  B) Social media  C) The human brain ✓  D) A telephone network

DESIGN:
- Bright, modern design with rounded buttons
- Show a progress bar (Question 1 of 5)
- Smooth animations when transitioning between questions
- Mobile-friendly layout
- Fun emoji reactions for correct/wrong answers
```

---

**Send that prompt** and wait about 10–20 seconds. Claude will generate your game!

**Expected result:** An Artifact panel opens on the right side of the screen showing your playable quiz game.

> 💡 **Tip:** If the Artifact doesn't appear, look for a small "Preview" button at the top of Claude's response and click it.

---

### ✅ Step 3 — Play Your Game & Find Issues

Before improving anything, **play the whole game through** as a student would:

**Testing checklist:**
- [ ] Does each question appear clearly?
- [ ] Do the answer buttons work when clicked?
- [ ] Is the correct/wrong feedback visible?
- [ ] Does the score update correctly?
- [ ] Does the final results screen appear?
- [ ] Does the "Play Again" button work?

Write down anything that feels off, looks wrong, or could be better. These become your improvement prompts in Step 5!

---

### ✅ Step 4 — Add Your Own Questions

Now make it *yours*. Ask Claude to replace the questions with your own custom trivia:

**📋 Customization Prompt:**

```
Great! Now replace the 5 questions with these new ones about [your topic]:

1. [Your question 1]
   A) [Option A]  B) [Option B] ✓  C) [Option C]  D) [Option D]

2. [Your question 2]
   ...

Keep everything else (design, animations, score tracking) exactly the same.
```

> 🎓 **Ideas for question topics:** AI ethics, history of computing, famous scientists, your school mascot trivia, local geography — anything that fits your class!

---

### ✅ Step 5 — Improve Your Game (Feature Upgrades)

This is where the real fun begins. Use the prompts below like a menu — pick the improvements you want and ask Claude one or two at a time:

---

## ⬆️ Improvement Feature Menu

### 🎨 Appearance Upgrades

**Dark Mode Toggle:**
```
Add a dark mode / light mode toggle button in the top-right corner. 
It should switch the whole game's color scheme instantly.
```

**Custom Theme:**
```
Redesign the color scheme to use a space theme — dark navy background, 
glowing cyan buttons, star emojis in the decorations. Keep all the game logic the same.
```

**Animated Background:**
```
Add a subtle animated gradient background that slowly shifts between 
two colors. Make it smooth and not distracting.
```

---

### ⏱️ Gameplay Upgrades

**Countdown Timer:**
```
Add a 15-second countdown timer for each question. If time runs out, 
mark it as wrong and move to the next question. Show the timer as 
a colored progress bar that turns red when under 5 seconds.
```

**Difficulty Levels:**
```
Add a difficulty selector on the start screen: Easy (20 seconds per question), 
Medium (10 seconds), Hard (5 seconds). Let the player choose before starting.
```

**Lifelines (like Who Wants to Be a Millionaire):**
```
Add two lifelines: 
1. "50/50" — removes two wrong answers
2. "Skip" — skips the current question without penalty
Each lifeline can only be used once per game. Show them as buttons.
```

---

### 📊 Score & Progress Upgrades

**High Score Tracker:**
```
Add a local high score that saves in the browser. Show the player's 
best score on the results screen. Add a "New High Score! 🏆" celebration 
animation if they beat it.
```

**Detailed Results:**
```
On the results screen, show a full review of every question — 
which ones the player got right (✅) and wrong (❌), and what 
the correct answer was for each wrong answer.
```

**XP / Leveling System:**
```
Add an XP system: correct answers give 100 XP, fast correct answers 
(under 5 seconds) give 150 XP. Show total XP on the results screen 
and unlock a "badge" at 400+ XP (e.g., "🧠 AI Expert!").
```

---

### 🔊 Sound & Effects Upgrades

**Sound Effects:**
```
Add browser-generated sound effects using the Web Audio API (no external files):
- A pleasant "ding" for correct answers
- A low "buzz" for wrong answers  
- A victory fanfare on the results screen
Add a mute button in the corner.
```

**Confetti Celebration:**
```
When the player gets a perfect score (all correct), trigger a 
confetti animation that rains down colored pieces. Use pure CSS/JS, 
no external libraries.
```

---

### 📤 Sharing & Saving Upgrades

**Copy Code Button:**
```
Add a button at the bottom: "📋 Copy Game Code". When clicked, it copies 
the full HTML source code to the clipboard so the student can save or share their game.
```

---

## 💡 Prompting Tips for Better Results

| ❌ Vague Prompt | ✅ Specific Prompt |
|----------------|------------------|
| "Make it look better" | "Change the background to dark blue, make buttons rounded with a glowing border" |
| "Add more questions" | "Add 5 more questions about machine learning, keeping the same format" |
| "Fix the bug" | "The score isn't updating after question 3. Check the score counter logic and fix it" |
| "Make it harder" | "Add a 10-second timer per question that counts down as a progress bar" |

**Golden Rule:** Describe *what you see*, *what you want*, and *what should stay the same*.

---

## 🏗️ Understanding What Claude Built

After playing with your game, try clicking the **"< >"** icon in the Artifact panel to view the source code. You'll see three sections:

```html
<!-- HTML: The structure -->
<div class="quiz-container">
  <h1>AI Trivia Quiz</h1>
  ...
</div>

<!-- CSS: The style -->
<style>
  .quiz-container { background: #1a1a2e; ... }
  .btn-correct { background: green; ... }
</style>

<!-- JavaScript: The logic -->
<script>
  let score = 0;
  function checkAnswer(choice) { ... }
</script>
```

You don't need to understand all of it — but see if you can find:
- [ ] Where the questions are stored (hint: look for your question text!)
- [ ] Where the score variable is (hint: search for `score`)
- [ ] What happens when a button is clicked (hint: look for `onClick` or `checkAnswer`)

---

## 🔬 Try It Activity

**Part A — Build it (20 min):**
1. Open [claude.ai](https://claude.ai) and use the Starter Prompt from Step 2
2. Play through the full game and note any issues
3. Replace the questions with 5 questions about *your own* topic

**Part B — Improve it (15 min):**
4. Pick **two** improvements from the Feature Menu above
5. Apply both using the provided prompts
6. Screenshot your final game and save it to `05-Projects/`

**Part C — Reflect (5 min):**
7. In your [[Daily Note]], answer: *"What surprised you about how fast Claude built the game? What would have been hardest to build yourself?"*

---

## ⭐ Challenge Mode: Build a Different Game

Feeling confident? Try building one of the other game types from scratch using this general structure:

**📋 Game Prompt Template:**
```
Build a [GAME NAME] game as an interactive HTML/CSS/JavaScript artifact.

GAME MECHANICS:
- [Describe how the game works in 3–5 bullet points]
- [Include win/lose conditions]
- [Include scoring if applicable]

DESIGN:
- [Colors and visual style you want]
- [Any specific UI elements — buttons, timers, etc.]

DIFFICULTY:
- [Easy version first, then I'll ask you to make it harder]
```

Try this with **Memory Card Match** or **Whack-a-Mole** for an extra challenge!

---

## 🔑 Key Terms

- **[[Claude Artifacts]]** — Interactive, live previews that Claude generates in the chat window — things like games, charts, and web apps
- **[[HTML]]** — The markup language that creates the structure and content of web pages
- **[[CSS]]** — The styling language that controls colors, fonts, layout, and animations on web pages
- **[[JavaScript]]** — The programming language that makes web pages interactive and adds game logic
- **[[Prompt Engineering]]** — The skill of writing clear, specific instructions to get better results from AI
- **[[Game Loop]]** — The repeating cycle in a game that checks for player input, updates the game state, and redraws the screen

---

## 🔗 Related Notes

*[[Interactive-Learning-Platforms]] · [[What is Claude Code - Concept Note]] · [[MOC-Main-Index]] · [[Glossary]]*

---

*Created: 2026-04-13 | Level: High School Intro | Topic: Programming + Claude Applications*
