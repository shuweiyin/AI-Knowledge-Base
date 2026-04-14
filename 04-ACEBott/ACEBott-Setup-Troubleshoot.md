---
title: "ACEBott — Setup & Troubleshooting Guide (Mac)"
level: all
topic: acebott
status: published
created: 2026-04-13
tags: [acebott, setup, troubleshoot, driver, mac, acecode]
---

# ACEBott — Setup & Troubleshooting Guide (Mac)

> Having trouble getting your ACEBott controller car working on a Mac? This guide walks through the two most common problems — the driver not installing and the app not opening — with step-by-step fixes and screenshots.

---

## 📦 Downloads & Files

Before you start, make sure you have these two files available. Click the links to open them from the vault:

| File | What it is | How to use |
|------|-----------|------------|
| [[controller car.sb3]] | Scratch program for the controller car | Open in ACECode (Upload mode) |
| [[CH341SER_MAC.ZIP]] | Mac USB serial driver (backup installer) | Unzip and install if the default driver fails |

> **Tip:** If the links above don't open automatically, find both files in `06-Resources/🔗 TOOLS-AND-LINKS/ACEBOTT/` inside the vault.

---

## 🚀 Normal Setup Steps

1. Download and install the **ACECode** app on your Mac.
2. Plug in your ACEBott controller car via USB.
3. Open ACECode — you should see your device listed.
4. Load `[[controller car.sb3]]` and select **"Tutorials"** in Upload mode.
5. Click **"Upload"** to send the program to the car.

If steps 3 or 1 give you trouble, see the fixes below.

---

## 🔧 Problem 1 — Driver Cannot Install

**Symptom:** You installed the serial driver but clicking the Install button does nothing, or the installation fails silently.

### Fix — Step by Step

**Step 1.** If the normal driver installation fails, use the backup driver instead:
→ Unzip **[[CH341SER_MAC.ZIP]]** and run the installer inside it.

**Step 2.** If clicking the Install button does nothing, macOS has blocked the driver extension. Open:
**System Settings → General → Login Items & Extensions**

![[image1.png]]

**Step 3.** Scroll down to the **Extensions** section and click **"Driver Extensions"**.
You will see `cn.wch.CH34xVCPDriver` listed there.

![[image2.png]]

**Step 4.** A popup will appear showing the **CH34xVCPDriver** toggle. Enable it and click **Done**.

![[image3.png]]

**Step 5.** Now go back and run the **CH34xVCPDriver** installer from your Applications folder again.
This time it will show **"Success"**.

**Step 6.** Unplug and **reconnect the car** via USB.
In ACECode, your device will now appear in the device list.

**Step 7.** Select **"Tutorials"** in Upload mode, then click **"Upload"**. You're good to go!

---

## 🔧 Problem 2 — App Won't Open ("Not Opened" Warning)

**Symptom:** When you try to open ACECode, macOS shows this dialog:

![[image4.png]]

> *"Apple could not verify ACECode is free of malware that may harm your Mac or compromise your privacy."*

This happens because ACECode is not downloaded from the Mac App Store. **It is safe to open** — just follow these steps.

### Fix — Step by Step

**Step 1.** Click **Done** (do NOT click "Move to Bin").

**Step 2.** Open **System Settings → Privacy & Security**.
Scroll down to the **Security** section.

![[image5.png]]

**Step 3.** You will see a message saying **ACECode was blocked**. Click **"Open Anyway"**.

**Step 4.** macOS will ask you to confirm — click **Open**.
ACECode will now launch normally. You only need to do this once.

> **Reference:** [How to fix "Apple cannot check it for malicious software" — CleanMyMac](https://cleanmymac.com/blog/apple-cant-check-malicious-software)

---

## 📋 Quick Troubleshooting Checklist

Use this checklist if something still isn't working:

- [ ] ACECode app is installed on the Mac
- [ ] USB cable is properly connected (try a different cable if unsure)
- [ ] "Open Anyway" was selected in Privacy & Security (Problem 2 fix)
- [ ] Driver is installed — ran CH34xVCPDriver installer from Applications (Problem 1 fix)
- [ ] Driver extension is enabled in Login Items & Extensions (Problem 1, Steps 2–4)
- [ ] Car was unplugged and reconnected after driver install
- [ ] Device shows up in ACECode's device list
- [ ] `[[controller car.sb3]]` is loaded and "Tutorials" / Upload mode is selected

---

## 🔗 Related Notes

- [[Driver can not install]] — original clipping with screenshots
- [[Solve Can not Open App Problem]] — original clipping for the app warning fix
- Source files: `06-Resources/🔗 TOOLS-AND-LINKS/ACEBOTT/`
