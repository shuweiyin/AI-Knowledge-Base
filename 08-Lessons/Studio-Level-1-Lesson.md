---
title: "Studio Level 1 — Online Lesson Programme"
level: high-intro
topic: programming
status: draft
created: 2026-04-13
tags: [studio, lesson, react, music-sampler, vercel, github, howler, vite, intermediate, online, saturday]
---

# 🔵 Studio Level 1 — Online Lesson Programme

> *A 6-week project-based programme for students aged 12 and above. Students build and deploy a real music web application — live on the internet.*

---

## 📢 Dear Parents — Why This Matters

There is a significant difference between a student who *uses* technology and one who *builds* it. Studio Level 1 is where that shift happens.

In these 6 sessions, your child will not follow a pre-written tutorial. They will plan, design, build, debug, and deploy a complete web application — a professional-quality music sampler called **"Beat Lab"** — using the same tools and workflow used by real software developers today.

**This is not a toy project.** When they finish, their app will have a real URL on the internet. They can send it to friends, add it to a school portfolio, or show it to a future employer. It works on phones and desktops. It plays real audio. And every part of it was built by them.

**What will your child learn?**

| Skill | Why It Matters |
|---|---|
| **React** — the world's most used framework for building websites | Powers Facebook, Instagram, Airbnb, and millions of other sites |
| **Deploying to the internet** | Transforms code from "something on my laptop" into "something anyone can visit" |
| **Audio programming** | How apps load, trigger, and control sound in a browser |
| **Professional UI design** | How to use AI to generate a polished, production-quality interface |
| **Version control with GitHub** | The industry-standard tool for saving, sharing, and collaborating on code |
| **Prompt engineering** | Writing precise AI instructions to build complex features quickly |
| **Debugging** | Reading error messages, identifying problems, and fixing them — a core developer skill |
| **AI ethics** | Understanding questions of authorship, sampling rights, and AI's role in creative work |

**What will your child walk away with?**
- A **live, deployed music web app** at a real public URL
- A **GitHub repository** — the beginning of a professional portfolio
- Experience with a **real developer workflow**: build → test → fix → deploy
- The confidence to say: *"I built that."*

---

## 📋 Programme at a Glance

|                     | Detail                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------- |
| **Level**           | Studio Level 1                                                                                |
| **Duration**        | 6 weeks · 1 session per week · 1 hour per session                                             |
| **Schedule**        | Every Saturday · **7:00–8:00pm UK time**                                                      |
| **Format**          | Online (live, teacher-led)                                                                    |
| **Language**        | English                                                                                       |
| **Group size**      | Maximum **8 students** — every student gets individual attention                              |
| **Age**             | Minimum 12 years old · No upper limit                                                         |
| **Price**           | **£120 per student** for the full 6-week block                                                |
| **What's included** | All lesson materials · Teacher support · **Claude AI account provided** · No extra tool costs |
| **What you need**   | Laptop or desktop · Stable internet                                                           |

> 💡 **The £120 covers everything.** Your child does not need to purchase any software, subscriptions, or tools. The Claude AI account used in lessons is provided and managed by the teacher.

---

## 📅 Session-by-Session Plan

### Session 1 — Setup & First Project *(1 hour)*

> **Goal:** Every student has a working development environment and sees a live React app running on their own screen by the end of the hour.

| | |
|---|---|
| **What we do** | Install Node.js and npm together as a class (teacher guides each student step by step) · Create free GitHub and Vercel accounts · Scaffold a brand new React + Vite project · Install Tailwind CSS and Howler.js · Run the app in the browser and confirm everything works · Introduction to what "Beat Lab" will look like when finished |
| **Key concepts** | What is React · What is npm · What is a development environment · Why GitHub and Vercel matter |
| **Tools** | Node.js · npm · GitHub · Vercel · Terminal · *(Cursor available if students want to browse files)* |
| **Student takeaway** | "My computer is set up like a real developer's. I can see my own app running." |

> 💡 **No pre-session setup needed.** Node.js installation is done together as a class at the start of Session 1. Just bring a laptop with a stable internet connection.

---

### Session 2 — Design Your Sampler UI *(1 hour)*

> **Goal:** A professionally designed sampler interface renders on screen, and the student understands its component structure.

| | |
|---|---|
| **What we do** | Introduction to React components and JSX (how React describes what you see on screen) · Use Claude Code's `frontend-design` skill to generate a bold, studio-quality UI for the sampler · Review the generated design as a class · Make personal adjustments (colours, layout, fonts) · Understand how the `SamplerPad` component and the main `App` layout relate to each other |
| **Key concepts** | React components · JSX · Props · UI design principles · What makes an interface feel professional |
| **Tools** | Claude Code · React · Tailwind CSS |
| **Student takeaway** | "I have a real-looking app design and I understand why it's structured the way it is." |

---

### Session 3 — Sounds & Pads *(1 hour)*

> **Goal:** The sampler has 8 real audio samples loaded, and each pad displays correctly with its name, key, and colour.

|                      |                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What we do**       | Find 8 royalty-free audio samples · Download and rename each file cleanly · Add them to the project's asset folder · Build the `sounds.js` configuration file that defines every pad · Build the `SamplerPad` component with its glow animation and key badge |
| **Key concepts**     | Royalty-free audio · File organisation · React component props · CSS animations · Configuration files                                                                                                                                                         |
| **Tools**            | Claude Code · React                                                                                                                                                                                                                                           |
| **Student takeaway** | "My app has 8 pads with real sounds loaded, and each one looks exactly how I want it."                                                                                                                                                                        |

---

### Session 4 — Make It Play *(1 hour)*

> **Goal:** Every pad plays real sound when clicked or when the matching keyboard key is pressed.

| | |
|---|---|
| **What we do** | Connect Howler.js to the sound configuration so each pad plays its audio file · Add keyboard shortcuts (keys A–K trigger pads 1–8) · Build the master volume slider · Track which pad is actively playing and show the visual glow state · Test every pad with clicks and key presses |
| **Key concepts** | Howler.js · React state (`useState`) · `useEffect` and event listeners · Keyboard events · Why browsers require user interaction before playing audio |
| **Tools** | Claude Code · Howler.js · React |
| **Student takeaway** | "Every pad plays a real sound. I can perform a beat using just my keyboard." |

---

### Session 5 — Polish *(1 hour)*

> **Goal:** The app feels finished, professional, and ready for public launch.

| | |
|---|---|
| **What we do** | Add a "Last played" indicator below the pads · Add a keyboard guide hint for new users · Confirm pads respond to touch on mobile devices · Add a mute toggle per pad (individual pad can be silenced) · Run `npm run build` — the final build check · Fix any errors or warnings that appear · Final visual review as a group |
| **Key concepts** | UI polish and user experience · Mobile responsiveness · Build process · Reading and fixing build errors |
| **Tools** | Claude Code · React · Terminal |
| **Student takeaway** | "My app passes the build check and looks professional on both laptop and phone." |

---

### Session 6 — Launch Day 🚀 *(1 hour)*

> **Goal:** The app is live on the internet at a real public URL. The student has shared it.

| | |
|---|---|
| **What we do** | Initialise a Git repository and commit all code · Push to GitHub · Connect GitHub repository to Vercel · Deploy — watch the build logs complete · Visit the live URL · Share the link with the class · Ethics discussion: who is the author of AI-assisted code? Are royalty-free samples truly free? · Brief showcase: each student demos their sampler |
| **Key concepts** | Git commit · GitHub push · Vercel deployment · Build logs · AI authorship · Intellectual property in music |
| **Tools** | Git · GitHub · Vercel · Claude Code |
| **Student takeaway** | "My app is live. I have a real URL I can share with anyone in the world." |

---

## 💷 Pricing

| | |
|---|---|
| **Full 6-week Studio Level 1 block** | **£120 per student** |
| **Payment covers** | All 6 sessions · All teaching materials · **Claude AI account** · Teacher support throughout |
| **Nothing extra to pay** | No software purchases · No subscriptions · No hidden costs |

---

## ✅ Requirements Checklist

Before the first session, please confirm your child has the following:

- [ ] **Laptop or desktop computer** — tablets and phones cannot run developer tools
- [ ] **Stable internet connection** — video call + development tools running simultaneously
- [ ] **Free access to these websites** — GitHub.com · Vercel.com · Looperman.com · Claude.ai *(students in regions where these sites are restricted will not be able to participate)*
- [ ] **English reading ability** — all lessons are taught and written in English

> 💡 **Claude AI account:** No action needed. The teacher provides and manages all Claude accounts used in lessons.

---

## 🎓 Entry Requirements

### Recommended Path
Complete [[Foundation-Level-Lesson|Foundation Level]] first. Foundation Level builds the confidence, vocabulary, and prompt engineering instincts that make Studio Level significantly easier and more enjoyable.

### Direct Entry by Evaluation
Students who have not completed Foundation Level are welcome to apply. The teacher will conduct a short conversation to confirm readiness. The evaluation covers:

| Area | What We Check |
|---|---|
| **Coding concepts** | Can you explain what if/else does? What is a loop? Can you read simple logic and predict what it does? |
| **AI concepts** | What is AI? What is Big Data? How does a machine learn from examples? |
| **Prompt skills** | Have you used AI to create something — an image, a plan, a piece of writing? Can you write a clear, specific prompt to get a useful result? |

> There are no wrong answers in the evaluation. The goal is to understand where the student is, so the teacher can give them the right support from day one.

---

## 🔗 Source Notes

*[[Music Sampler Web App - Project]] · [[frontend-design Skill - Build UI with Claude]] · [[How to Deploy to Vercel - Lesson Plan]] · [[What is Vercel - Concept Note]] · [[Frontend vs Backend - Concept Note]] · [[Foundation-Level-Lesson]] · [[Glossary]]*

---

*Created: 2026-04-13 | Programme: Studio Level 1 | Format: Online | Schedule: Saturday 7–8pm UK | Language: English*
