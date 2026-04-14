---
title: "Snake Game Builder — Claude Artifacts"
level: high-intro
topic: programming
status: published
created: 2026-04-13
tags: [claude-artifacts, snake-game, game-dev, html, javascript, canvas, game-loop, collision-detection, hands-on]
---

# 🐍 Snake Game Builder — Claude Artifacts

> **Hook:** Snake is one of the most famous games ever made — it shipped on Nokia phones in 1997 and was played by over 400 million people. Today, you're going to build your own version from scratch using AI, and then make it *better* than the original. No download. No setup. Just your ideas and Claude.

Snake is the perfect game to study because underneath its simple looks is a collection of **core computer science ideas** — game loops, arrays, collision detection, and coordinate systems — the same building blocks used in games like Minecraft, Pac-Man, and even self-driving cars.

---

## 🎯 What You'll Learn

By the end of this guide, you'll be able to:
- Build a fully playable Snake game using [[Claude Artifacts]] in minutes
- Understand how a **[[Game Loop]]** keeps a game running frame by frame
- See how **[[Arrays]]** are used to track the snake's body segments
- Recognize **[[Collision Detection]]** — how the game knows when the snake hits something
- Apply at least 2 improvement features to make the game your own

**Level:** High School Intro → Intermediate | **Time:** 60–90 minutes  
**Prerequisites:** [[Claude-Artifacts-Game-Builder]] (recommended but not required)

---

## 🧠 How Snake Works — The CS Behind the Game

Before we build, let's understand what the game is actually doing. Every tick of the game clock, Snake runs this same cycle:

```
┌──────────────────────────────────────────────┐
│               THE GAME LOOP                  │
│                                              │
│  1. READ INPUT  ← Did the player press a key?│
│       ↓                                      │
│  2. UPDATE STATE ← Move snake, check collisions│
│       ↓                                      │
│  3. DRAW FRAME ← Paint the new positions     │
│       ↓                                      │
│  ──── repeat ~10–15 times per second ────    │
└──────────────────────────────────────────────┘
```

The snake's body is stored as an **[[Array]]** of grid coordinates:

```
Snake body = [ [5,3], [4,3], [3,3] ]
              head   body   tail
              (col, row positions on the grid)
```

Every game tick:
- A **new head** is added in the direction the player is moving → `[6,3]`
- The **tail is removed** → `[3,3]` drops off
- Net result: the snake appears to *slide* forward!

When the snake eats food, the tail is **not removed** that tick — so the snake gets one block longer.

**[[Collision Detection]]** checks:
| Situation | Check | Result |
|-----------|-------|--------|
| Hit a wall | New head x < 0 or x > grid width | Game over |
| Hit itself | New head position = any body position | Game over |
| Ate food | New head position = food position | Grow + new food |

This is the same kind of thinking used in robotics, GPS navigation, and video game physics engines.

---

## 🪜 Step-by-Step: Build Your Snake Game

### ✅ Step 1 — Open Claude

1. Go to [claude.ai](https://claude.ai) and sign in
2. Start a **New Chat**
3. Use **Claude Sonnet** or higher (check the model dropdown at top)

> ⚠️ **Important:** Snake uses the keyboard (arrow keys or WASD). Always click **inside the game** before pressing keys — the Artifact panel needs "focus" to detect input.

---

### ✅ Step 2 — Send the Starter Prompt

Copy the prompt below exactly. It's detailed on purpose — specific prompts produce dramatically better results:

---

**📋 Starter Prompt (copy this!):**

```
Build a complete, playable Snake game as an interactive HTML/CSS/JavaScript artifact. 
Use an HTML5 Canvas for rendering. Here are the full requirements:

GRID & CANVAS:
- 20×20 grid of cells, each cell is 25×25 pixels (canvas = 500×500px)
- Dark background (#1a1a2e), grid lines are subtle (rgba(255,255,255,0.05))
- Snake cells are bright green (#00ff88) with a slightly darker border
- Food is a red circle (#ff4757) centered in its cell

GAME MECHANICS:
- Snake starts at the center of the grid, length 3, moving RIGHT
- Arrow keys AND WASD both control direction
- The snake cannot reverse direction (pressing LEFT while moving RIGHT does nothing)
- Food spawns at a random empty cell when eaten
- Snake grows by 1 cell each time it eats food
- Game ends when the snake hits a wall OR hits its own body
- Game speed: starts at 150ms per tick, gets 5ms faster every 5 foods eaten (minimum 60ms)

HUD (display above the canvas):
- Current score (1 point per food)
- Current speed level (Level 1 = 150ms, Level 2 = 145ms, etc.)
- High score (saved in localStorage so it persists between sessions)

GAME OVER SCREEN (overlay on the canvas):
- Semi-transparent dark overlay
- "GAME OVER" in large text
- Final score and high score
- "Press SPACE or click to restart" instruction

START SCREEN:
- Show a start screen before the game begins
- Display the controls (arrow keys / WASD)
- "Press SPACE to start" instruction

VISUAL POLISH:
- Snake head is a brighter/slightly different shade than the body
- When food is eaten, flash the score briefly
- Smooth appearance — no flickering
```

---

Send this and wait ~15–20 seconds. Claude will generate the full game.

**Expected result:** A playable Snake game appears in the Artifact panel with a start screen. Click the panel, press SPACE, and play!

> 💡 **If the arrow keys scroll the page instead of moving the snake:** This means the Artifact panel doesn't have focus. Click directly on the canvas/game area first, then use arrow keys.

---

### ✅ Step 3 — Play & Test

**Run through this checklist** before moving on to improvements:

**Controls:**
- [ ] Arrow keys move the snake correctly in all 4 directions
- [ ] WASD also works
- [ ] Snake cannot reverse (pressing opposite direction is ignored)

**Game mechanics:**
- [ ] Snake grows when eating food
- [ ] New food appears after eating
- [ ] Game over triggers on wall collision
- [ ] Game over triggers on self-collision
- [ ] Score increments correctly

**Speed & HUD:**
- [ ] Speed increases as score grows
- [ ] Level counter updates
- [ ] High score saves between restarts (close & reopen the Artifact to test)

**Screens:**
- [ ] Start screen shows at the beginning
- [ ] Game over overlay appears with score
- [ ] SPACE / click restarts correctly

Write down anything that feels off. Every bug you find becomes a one-sentence prompt to fix it.

---

### ✅ Step 4 — Fix Any Issues

If something doesn't work right, describe it plainly:

**📋 Bug Fix Prompt Template:**
```
The [X] isn't working correctly. Specifically: [describe what you see].
It should [describe what you expect]. Please fix only this issue 
and keep everything else exactly the same.
```

**Common issues and fixes:**

| Problem | Fix Prompt |
|---------|-----------|
| Arrow keys scroll the browser | "Prevent the default browser scroll behavior for arrow keys inside the canvas" |
| Snake teleports to wrong position | "The snake head coordinates seem to jump — check the direction update logic" |
| Food spawns on the snake | "Make sure food only spawns on empty cells — cells not occupied by any snake segment" |
| High score doesn't persist | "Use localStorage to save and load the high score between sessions" |

---

### ✅ Step 5 — Choose Your Improvements

Now the fun part. Use the prompts below like a **feature menu** — pick what interests you and add them one at a time:

---

## ⬆️ Improvement Feature Menu

### 🎨 Visual Upgrades

---

#### 🌈 Gradient Snake Body
```
Make the snake body a gradient — the head is bright green (#00ff88), 
and each segment gradually fades to a darker green (#004422) at the tail. 
Use the segment index to calculate the color for each cell.
```

**What you'll learn:** How arrays store ordered data, and how index position maps to visual properties.

---

#### ✨ Particle Explosion on Food Eaten
```
When the snake eats food, spawn 8–12 small colored particles that 
fly outward from the food position and fade out over 0.3 seconds. 
Use the Canvas requestAnimationFrame for smooth animation. 
The particles should be small circles (3–5px radius) in random warm colors.
```

**What you'll learn:** Particle systems — the same technique used in explosions, fire, and magic effects in real games.

---

#### 🌙 Theme Switcher
```
Add a theme switcher button above the canvas that cycles through 3 themes:
1. "Neon" (current: dark bg, green snake, red food)  
2. "Retro" (black bg, white snake, yellow food — like the original Nokia)
3. "Ocean" (navy bg, cyan snake, orange food)
Switching theme should take effect immediately, even mid-game.
```

---

#### 🎞️ Smooth Snake Movement
```
Instead of the snake jumping cell-by-cell, add sub-cell interpolation so 
the snake appears to glide smoothly between grid positions. The snake 
should still follow the grid logic — only the visual rendering should 
be smooth. Use requestAnimationFrame and a lerp (linear interpolation) 
between the previous and next cell position.
```

**What you'll learn:** Interpolation — a key technique in animation, robotics, and game engines.

---

### ⚙️ Gameplay Upgrades

---

#### 🌀 Wrap-Around Walls (Portal Mode)
```
Add a toggle button labeled "Portal Mode 🌀". When enabled, 
the snake wraps around the edges instead of dying — going off 
the right side appears on the left, going off the top appears at the bottom. 
When disabled, hitting a wall ends the game as normal.
```

**What you'll learn:** Modulo arithmetic (`%`) — the math trick that makes wrap-around work.

---

#### 🍎 Multi-Food Mode
```
Add a "Multi-Food" toggle. When enabled, 3 food items appear on the board 
simultaneously instead of 1. Each has a different color and point value:
- Red apple: 1 point (common)
- Gold star: 3 points (uncommon) 
- Purple gem: 5 points (rare)
All three respawn individually when eaten.
```

---

#### 💀 Obstacle Walls
```
After the player reaches score 10, begin randomly placing 1–2 gray wall 
blocks on the board every 5 points scored. Hitting a wall block ends the game 
(same as hitting the border). Wall blocks never spawn on the snake or food. 
Show the number of current obstacles in the HUD.
```

---

#### ⏸️ Pause Feature
```
Add pause functionality: pressing P or ESC pauses the game and shows 
a "PAUSED — Press P to resume" overlay on the canvas. 
The game timer stops completely while paused. 
Add a small pause icon button above the canvas as well.
```

---

#### 🍒 Bonus Food Timer
```
Every 20 seconds, spawn a special bonus food item (a flashing gold circle) 
that is worth 5 points. It disappears after 8 seconds if not eaten. 
Show a countdown bar under the canvas while the bonus is active.
```

---

### 📊 Score & Progression Upgrades

---

#### 🏆 Leaderboard (Top 5 Scores)
```
Replace the single high score with a Top 5 local leaderboard. 
After each game over, if the score qualifies, prompt the player 
to enter their name (max 10 characters) and save it. 
Show the leaderboard on the game over screen as a styled table. 
Persist everything in localStorage.
```

---

#### 🎖️ Achievement Badges
```
Add an achievement system with these unlockable badges:
- 🌱 "First Bite" — eat your first food
- 🔟 "Double Digits" — reach score 10
- ⚡ "Speed Demon" — reach Level 5
- 🐍 "Long Boi" — reach length 20
- 💀 "Survivor" — play for 2 minutes without dying

Show newly unlocked achievements as a pop-up banner at the top of the canvas.
Store unlocked achievements in localStorage permanently.
```

---

#### 📈 Stats Screen
```
Add a "Stats" button above the canvas. Clicking it shows a panel with 
lifetime statistics (stored in localStorage):
- Total games played
- Total food eaten (all time)
- Longest snake ever (max length reached)
- Best speed level reached
- Total time played (in minutes)
Show this as a clean card layout next to the canvas.
```

---

### 🔊 Sound Upgrades

---

#### 🎵 Sound Effects (No External Files)
```
Add browser-generated sound effects using the Web Audio API (no external files needed):
- Eat food: a short, pleasant "pop" tone (sine wave, ~200ms)
- Game over: a descending "wah-wah" tone (2 notes, dropping pitch)
- Level up: a quick ascending 3-note fanfare
- Bonus food appears: a shimmering high tone

Add a 🔊/🔇 mute toggle button above the canvas. 
Default state: sounds ON.
```

---

#### 🎶 Background Music Generator
```
Add procedural background music using the Web Audio API — a simple 
looping 8-bit style melody that plays during the game. 
The tempo should increase as the snake speeds up. 
Include the mute button to silence everything (music + effects).
```

---

### 🤖 AI Upgrades (Advanced!)

---

#### 🤖 Auto-Play AI Mode
```
Add an "AI Mode" toggle button. When enabled, the snake is controlled 
automatically by a simple pathfinding algorithm (BFS or greedy nearest-food). 
The AI should navigate toward the food while trying to avoid walls and its own body. 
Show "🤖 AI Playing" in the HUD when active. 
The player can take back control by pressing any arrow key.
```

**What you'll learn:** This is real-world [[Pathfinding]] — the same algorithm used in GPS navigation and game enemy AI!

---

#### 🌡️ Heatmap Overlay
```
After a game ends, show a semi-transparent heatmap overlay on the canvas 
showing which cells the snake visited most during that game. 
Cells visited more often glow warmer (red), rarely visited cells stay cool (blue). 
Show a "Heatmap" toggle button on the game over screen.
```

**What you'll learn:** Data visualization — how raw numbers (visit counts) become visual information.

---

### 📤 Sharing Upgrades

---

#### 📸 Screenshot Button
```
Add a "📸 Save Screenshot" button that captures the current canvas state 
and downloads it as a PNG file named "snake-score-[X].png" where X is 
the current score. Use the Canvas toDataURL() method.
```

---

#### 📋 Copy Code Button
```
Add a "📋 Copy Source Code" button below the game. 
When clicked, it copies the entire HTML/CSS/JS source code to the clipboard 
and briefly shows "Copied! ✓" as confirmation. 
This lets students save and share their customized game.
```

---

## 🔬 Understanding the Code: Guided Exploration

Click the **`< >`** icon in the Artifact panel to view the source code. Try to find these parts:

### 🗺️ Treasure Hunt
Use `Ctrl+F` (find) to search for each keyword:

| Search Term | What You'll Find | CS Concept |
|-------------|-----------------|------------|
| `snake.push` | Where a new head segment is added | **Arrays** — adding to the front |
| `snake.pop` | Where the tail is removed each tick | **Arrays** — removing from the end |
| `setInterval` | The game loop timer | **[[Game Loop]]** — repeated execution |
| `collision` | The collision detection function | **[[Collision Detection]]** |
| `localStorage` | Where high scores are saved | **Browser Storage** — data persistence |
| `keydown` | Where keyboard input is captured | **Event Listeners** — responding to input |
| `ctx.fillRect` | Where snake squares are drawn | **Canvas API** — painting graphics |

---

### 🧩 The Snake Array — A Visual Explanation

When the snake is at positions `[[5,3], [4,3], [3,3]]` and moves RIGHT:

```
BEFORE MOVE:          AFTER MOVE (ate nothing):
■ ■ ■ → →            → ■ ■ ■ →
[3,3][4,3][5,3]       [3,3][4,3][5,3][6,3]
                       ↑remove tail  ↑add new head
                      = [4,3][5,3][6,3]
```

When the snake eats food (skip the `pop`):
```
BEFORE:     → ■ ■ ■ 🍎         AFTER (snake grew!):
            [3,3][4,3][5,3][6,3]food    [3,3][4,3][5,3][6,3][7,3]
                                         tail stays!     new head
```

This is why arrays are perfect for Snake — **push** and **pop** handle grow/shrink in one line each.

---

## 🏗️ Going Further: What Could You Build Next?

Now that you understand the core mechanics, here are project ideas that use the same building blocks:

| Project | How It Connects to Snake |
|---------|------------------------|
| **Pac-Man** | Same grid, same collision detection, enemies use pathfinding |
| **Maze Solver** | Pathfinding through a grid — same coordinate system |
| **Self-Driving Car Demo** | Vehicles avoid obstacles using collision detection |
| **2-Player Snake** | Two snakes, two keyboards, shared grid — multiplayer! |
| **Snake AI Training** | Teach an AI to play Snake using reinforcement learning |

---

## ✅ Try It Activities

**Part A — Build It (30 min)**
1. Use the Starter Prompt to generate your Snake game
2. Play through it and complete the testing checklist
3. Fix at least one issue using the bug fix prompts

**Part B — Improve It (20 min)**
4. Pick **two** upgrades from the Feature Menu — at least one from **Visual** and one from **Gameplay**
5. Apply them one at a time using the copy-paste prompts
6. Test after each upgrade to make sure nothing broke

**Part C — Explore the Code (10 min)**
7. Complete the **Treasure Hunt** above — find all 7 keywords in the source code
8. For each one, write one sentence in your [[Daily Note]] explaining what it does in plain English

**Part D — Reflect (10 min)**
9. Answer in your Daily Note: *"What is one thing the Snake game has in common with a real-world technology? (Hint: think about GPS, robots, or social media algorithms.)"*

---

## 🔑 Key Terms

- **[[Claude Artifacts]]** — Live, interactive previews Claude generates in the chat window using HTML, CSS, and JavaScript
- **[[Game Loop]]** — The repeating cycle (input → update → draw) that keeps a game running frame by frame
- **[[Arrays]]** — An ordered list of items in code; Snake uses an array to track every body segment's position
- **[[Collision Detection]]** — The logic that checks whether two objects (snake + wall, snake + food) occupy the same space
- **[[Canvas API]]** — A JavaScript tool for drawing shapes, images, and animations directly onto an HTML canvas element
- **[[Pathfinding]]** — An algorithm that finds the shortest or safest route from point A to point B — used in GPS, games, and robotics
- **[[localStorage]]** — A browser feature that lets a website save small amounts of data on your computer, so it persists after the page is closed

---

## 🔗 Related Notes

*[[Claude-Artifacts-Game-Builder]] · [[Interactive-Learning-Platforms]] · [[What is Claude Code - Concept Note]] · [[MOC-Main-Index]] · [[Glossary]]*

---

*Created: 2026-04-13 | Level: High School Intro → Intermediate | Topic: Programming + Game Development*
