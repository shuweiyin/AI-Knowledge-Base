"""
DrFrost Wrong Skills Scraper
════════════════════════════
Logs into DrFrost, scans all tasks, finds wrong answers,
maps each wrong skill to its unit, and saves results to JSON.

Usage:
    python3 drfrost_scraper.py

Output:
    drfrost_results.json  (same folder as this script)

After running, tell Claude: "DrFrost sync is ready, please update Notion"
Claude will read the JSON and refresh the Notion database automatically.
"""

import asyncio
import json
import os
from datetime import datetime
from playwright.async_api import async_playwright

# ── Credentials ────────────────────────────────────────────────────
USERNAME = "Liun@dulwich.org.uk"
PASSWORD = "Establishment&1"

# Output file (same folder as this script)
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "drfrost_results.json")


# ──────────────────────────────────────────────────────────────────
async def login(page):
    await page.goto("https://www.drfrost.org/login", wait_until="networkidle")
    try:
        if await page.locator("button:has-text('Accept')").first.is_visible(timeout=2000):
            await page.locator("button:has-text('Accept')").first.click()
    except:
        pass
    await page.locator("button:has-text('Microsoft')").first.click()
    await page.wait_for_selector("input[type='email']", timeout=8000)
    await page.fill("input[type='email']", USERNAME)
    await page.locator("input[value='Next'], button:has-text('Next')").first.click()
    await page.wait_for_selector("input[type='password']", timeout=8000)
    await page.fill("input[type='password']", PASSWORD)
    await page.locator("input[value='Sign in'], button:has-text('Sign in')").first.click()
    await page.wait_for_load_state("networkidle")
    try:
        no = page.locator("input[value='No'], button:has-text('No')").first
        if await no.is_visible(timeout=3000):
            await no.click()
            await page.wait_for_load_state("networkidle")
    except:
        pass
    return "dashboard" in page.url


async def get_tasks(page):
    result = {}

    async def capture(resp):
        if "tasks/list" in resp.url:
            try:
                body = await resp.body()
                result["data"] = json.loads(body.decode("utf-8", errors="replace"))
            except:
                pass

    page.on("response", capture)
    await page.goto(
        "https://www.drfrost.org/progress.php?mode=tasklist",
        wait_until="networkidle"
    )
    await page.wait_for_timeout(2000)
    return result.get("data", {}).get("tasks", [])


async def get_wrong_answers(page, aaid):
    resp    = await page.request.get(
        f"https://www.drfrost.org/api/tasks/attempt/{aaid}"
    )
    attempt = json.loads((await resp.body()).decode("utf-8", errors="replace"))
    answers = attempt.get("answers", {})
    wrong   = []
    for qnum, ans in answers.items():
        if not ans.get("iscorrect") and ans.get("ssid"):
            wrong.append({
                "qnum":         int(qnum),
                "ssid":         ans["ssid"],
                "their_answer": ans.get("theiranswer", []),
            })
    return wrong


async def lookup_unit(page, ssid):
    found = {}

    async def capture_explore(resp):
        if "/api/course/explore/" in resp.url:
            try:
                body = await resp.body()
                found["data"] = json.loads(body.decode("utf-8", errors="replace"))
                found["cuid"] = resp.url.split("/api/course/explore/")[-1]
            except:
                pass

    page.on("response", capture_explore)
    await page.goto(
        f"https://www.drfrost.org/explorer.php?ssid={ssid}",
        wait_until="networkidle"
    )
    await page.wait_for_timeout(1000)

    data       = found.get("data", {})
    unit_name  = data.get("name", "Unknown")
    cuid       = found.get("cuid", "")
    skill_name = f"ssid={ssid}"
    skill_code = ""

    for skill in data.get("skills", []):
        for sub in skill.get("subskills", []):
            if sub.get("ssid") == ssid:
                skill_name = skill.get("name", skill_name)
                skill_code = str(skill.get("publicid", ""))
                break

    return {
        "unit":       unit_name,
        "skill_name": skill_name,
        "skill_code": skill_code,
        "cuid":       cuid,
    }


async def scrape():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 900})
        page    = await context.new_page()

        # 1. Login
        print("⏳ Logging in...")
        ok = await login(page)
        if not ok:
            print("❌ Login failed")
            await browser.close()
            return
        print("✅ Logged in as Nemo Liu\n")

        # 2. Get all tasks
        print("⏳ Fetching all tasks...")
        all_tasks            = await get_tasks(page)
        tasks_with_attempts  = [t for t in all_tasks if t.get("attempts")]
        print(f"✅ {len(all_tasks)} tasks, {len(tasks_with_attempts)} completed\n")

        # 3. Collect wrong answers across all tasks
        ssid_data   = {}
        total_tasks = len(tasks_with_attempts)

        for idx, task in enumerate(tasks_with_attempts, 1):
            label    = task["label"]
            aaid     = task["attempts"][0]["aaid"]
            accuracy = float(task.get("accuracy", 0))
            print(f"  [{idx:02}/{total_tasks}] {label[:55]:<55} {accuracy:.0f}%")

            wrong = await get_wrong_answers(page, aaid)
            for w in wrong:
                ssid = w["ssid"]
                if ssid not in ssid_data:
                    ssid_data[ssid] = {
                        "ssid":        ssid,
                        "unit":        None,
                        "skill_name":  None,
                        "skill_code":  None,
                        "cuid":        None,
                        "wrong_count": 0,
                        "tasks":       [],
                    }
                ssid_data[ssid]["wrong_count"] += 1
                if label not in ssid_data[ssid]["tasks"]:
                    ssid_data[ssid]["tasks"].append(label)

        print(f"\n✅ {len(ssid_data)} unique wrong skills found\n")

        # 4. Map each ssid → unit + skill name
        print("⏳ Looking up unit names...")
        total_ssids = len(ssid_data)
        for i, ssid in enumerate(ssid_data.keys(), 1):
            info = await lookup_unit(page, ssid)
            ssid_data[ssid].update(info)
            print(f"  [{i:02}/{total_ssids}] [{info['unit']}] {info['skill_name'][:50]}")

        # 5. Build output
        skills = []
        for ssid, d in ssid_data.items():
            skills.append({
                "ssid":          ssid,
                "unit":          d["unit"] or "Unknown",
                "skill_name":    d["skill_name"] or f"Skill {ssid}",
                "skill_code":    d["skill_code"] or "",
                "wrong_count":   d["wrong_count"],
                "tasks":         d["tasks"],
                "practice_link": f"https://www.drfrost.org/do-question.php?ssid={ssid}",
                "review_link":   "https://www.drfrost.org/progress.php?mode=tasklist",
                "cuid":          d["cuid"] or "",
            })

        skills.sort(key=lambda x: (-x["wrong_count"], x["unit"]))

        output = {
            "scraped_at":         datetime.now().isoformat(),
            "student":            "Nemo Liu",
            "total_tasks":        len(all_tasks),
            "total_skills_wrong": len(skills),
            "skills":             skills,
        }

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Saved → {OUTPUT_FILE}")
        print(f"   {len(skills)} wrong skills across "
              f"{len(set(s['unit'] for s in skills))} units")
        print(f"\n👉 Now tell Claude: \"DrFrost sync is ready, please update Notion\"")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(scrape())
