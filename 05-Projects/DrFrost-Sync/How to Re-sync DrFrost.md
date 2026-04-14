---
title: "How to Re-sync DrFrost Wrong Skills to Notion"
type: guide
tags: [drfrost, notion, automation, nemo]
status: published
created: 2026-04-14
---

# 🔄 How to Re-sync DrFrost → Notion

Run this **any time after completing new homework** on DrFrost to refresh your weak-skills list in Notion.

---

## Two steps, takes ~5 minutes

### Step 1 — Run the scraper

Open **Terminal** and run:

```bash
python3 "/Users/shuweiyin/Documents/my-workspace/obsitian/AI_Knowledge_Base/05-Projects/DrFrost-Sync/drfrost_scraper.py"
```

It will:
- Log into DrFrost automatically
- Scan all your tasks for wrong answers
- Map each wrong skill to its unit
- Save results to `drfrost_results.json`

You'll see output like:
```
✅ Logged in as Nemo Liu
✅ 28 tasks, 28 completed
✅ 47 unique wrong skills found
👉 Now tell Claude: "DrFrost sync is ready, please update Notion"
```

---

### Step 2 — Ask Claude to update Notion

Come back here (Claudian / Claude Code) and say:

> **"DrFrost sync is ready, please update Notion"**

Claude will:
1. Read the new `drfrost_results.json`
2. Clear the old rows from your Notion database
3. Insert fresh rows with updated data

---

## Files in this folder

| File | Purpose |
|---|---|
| `drfrost_scraper.py` | The scraper script — run this |
| `drfrost_results.json` | Output from last scrape (auto-updated) |
| `notion_config.json` | Notion database IDs (don't edit) |
| `How to Re-sync DrFrost.md` | This guide |

---

## Notion database

🔗 [Math Improve → DrFrost Weak Skills](https://www.notion.so/Math-Improve-34250e88a6f68068be35f22b6e1d07e2)

**Status column guide:**
- ⬜ Not Started — haven't practised this skill yet
- 🔄 In Progress — practising but not confident yet
- ✅ Done — mastered, won't show up in next sync if no longer wrong

---

## Troubleshooting

**"python3 not found"**
→ Install Python: https://www.python.org/downloads/

**"No module named playwright"**
→ Run: `pip3 install playwright && python3 -m playwright install chromium`

**Login fails**
→ Check if the password has changed. Update `USERNAME` / `PASSWORD` in `drfrost_scraper.py`

**Scraper is slow**
→ Normal — it visits each skill's page to look up the unit name. 50 skills ≈ 4–5 minutes.
