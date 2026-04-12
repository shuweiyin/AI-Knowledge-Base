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

## 🔧 C — Claude & AI Tools

**API (Application Programming Interface)** — A way for two pieces of software to talk to each other. When the Claudian plugin sends your question to Claude, it uses Anthropic's API to do so — think of it as a standardized "power socket" for connecting apps.

**Claude Code** — An AI coding and knowledge assistant built by Anthropic that runs in your terminal or editor. Unlike a chatbot, it can read and edit files in your project, giving it full context to help with real work. → [[What is Claude Code - Concept Note]]

**Claude.md** — A special plain-text file placed in the root of a vault or project folder. It tells Claude about the project's purpose, goals, audience, and rules — acting like a permanent system prompt that shapes every interaction. → [[What is Claude Code - Concept Note]]

**Claudian Plugin** — A community plugin for Obsidian that connects Claude AI directly to your vault, letting you ask questions and generate content without leaving your notes. → [[Claudian plugin]]

**Context Window** — The maximum amount of text (measured in "tokens") that a language model can process at one time — its working memory. A larger context window means Claude can read more of your vault in one conversation. → [[What is Claude Code - Concept Note]]

**Large Language Model (LLM)** — A type of AI model trained on massive amounts of text data to understand and generate human language. Claude, GPT-4, and Gemini are all LLMs. They predict the most likely next word given the context — billions of times — to produce coherent text. → [[What is Claude Code - Concept Note]]

**MCP (Model Context Protocol)** — An open standard created by Anthropic that lets Claude connect to external tools and data sources — like your file system, calendar, web search, or databases — in a safe, controlled way. → [[What is Claude Code - Concept Note]]

**Prompt** — The text input you give to an AI model — your question, instruction, or request. The quality of your prompt heavily influences the quality of the response.

**Prompt Engineering** — The skill of designing effective prompts to get better, more useful responses from AI models. Involves specifying role, task, context, format, and constraints clearly. → [[AI Learning Habits - Project]]

**System Prompt** — A set of instructions given to an AI before a conversation begins, setting its role, tone, and rules. Claude.md functions as a system prompt for the Claudian plugin. → [[What is Claude Code - Concept Note]]

**Token** — The basic unit of text that language models process — roughly ¾ of a word. "Hello world" = 2 tokens. Models have a maximum token limit per conversation (the context window).

---

## 📚 O — Obsidian & Vault

**Daily Note** — A note in Obsidian automatically named with today's date (e.g., `2026-04-12 Daily`). Used as a learning log or journal to track what you studied, what confused you, and what you want to explore next. → [[AI Learning Habits - Project]]

**Dataview** — A powerful Obsidian community plugin that lets you query your notes like a database — e.g., "show me all notes tagged `status: draft`, sorted by date." Useful for building dynamic indexes and to-do lists.

**Frontmatter** — A block of YAML metadata placed at the very top of a Markdown note, between `---` lines. It holds structured information about the note — title, tags, status, date — that Obsidian and plugins can read and filter. → [[What is Obsidian - Concept Note]]

**Graph View** — A built-in Obsidian feature that displays all your notes as dots (nodes) and all wikilinks as lines (edges), creating a visual map of your knowledge web. Orphan notes (no connections) appear as isolated dots. → [[What is Obsidian - Concept Note]]

**Markdown** — A lightweight text formatting language used for all Obsidian notes. Uses simple symbols: `**bold**`, `*italic*`, `# Heading 1`, `- bullet point`, `[[wikilink]]`. Files are saved as plain `.md` text files. → [[What is Obsidian - Concept Note]]

**MOC (Map of Content)** — A special note that acts as a table of contents or index for a topic — it links to all related notes in one place, making it the hub of a topic web in your graph. → [[Obsidian Best Practices - Project]]

**Obsidian** — A free, local-first note-taking app where notes are Markdown files stored on your computer. Its superpower is wikilinks and Graph View — turning individual notes into an interconnected knowledge base. → [[What is Obsidian - Concept Note]]

**Orphan Note** — A note in Obsidian that has no wikilinks pointing to it or from it — it floats alone in the graph with no connections. Orphan notes are a signal that a concept hasn't been integrated into your knowledge web yet. → [[AI Learning Habits - Project]]

**PKM (Personal Knowledge Management)** — The practice of intentionally capturing, organizing, connecting, and using information to support thinking and learning. Obsidian is one of the most popular PKM tools.

**Plugin** — An add-on that extends Obsidian's built-in features. Core plugins come with Obsidian; Community plugins are built by users. Examples: Daily Notes (core), Dataview (community), Claudian (community). → [[What is Obsidian - Concept Note]]

**Vault** — The root folder that contains all of your Obsidian notes and configuration. Everything inside the vault folder is part of your knowledge base. Multiple vaults can exist on one computer. → [[What is Obsidian - Concept Note]]

**Wikilink** — A link between two notes created by wrapping a note name in double square brackets: `[[Note Name]]`. Clicking a wikilink opens the linked note; Obsidian draws these as edges in the Graph View. → [[What is Obsidian - Concept Note]]

**YAML** — A human-readable data format used for Obsidian frontmatter. Uses `key: value` pairs between `---` lines at the top of a note. Stands for "YAML Ain't Markup Language."

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

*Last updated: 2026-04-12 | Maintained by: Claudian (AI assistant)*  
*Rule: Every new term in any note → add it here. See [[Claude.md]] for the full rule.*
