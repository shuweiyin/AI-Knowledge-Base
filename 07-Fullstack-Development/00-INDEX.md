---
title: "Fullstack App Development — Index"
topic: fullstack
status: published
created: 2026-04-13
tags: [fullstack, nextjs, firebase, stripe, gcp, cloud-run, vercel, nodejs]
---

# 🏗️ Fullstack App Development

> Personal engineering reference for building and deploying production-grade fullstack apps using Next.js, Firebase, Stripe, and GCP Cloud Run.

---

## 🗺️ What's in This Section

| # | Topic | Note |
|---|-------|------|
| 1 | Planning with Claude — AskUserQuestion | [[07-Fullstack-Development/01-Planning-with-Claude/AskUserQuestion - How & When]] |
| 2 | From Plan to Code — Subagents | [[07-Fullstack-Development/01-Planning-with-Claude/Plan to Code - Using Subagents]] |
| 3 | Local Environment Setup | [[07-Fullstack-Development/02-Local-Environment/Node.js & Next.js Setup]] |
| 4 | Firebase Auth (Google + Email) | [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]] |
| 5a | Firestore Database | [[07-Fullstack-Development/03-Firebase/Firestore Database]] |
| 5b | Firebase Storage | [[07-Fullstack-Development/03-Firebase/Firebase Storage]] |
| 6 | Stripe Payments | [[07-Fullstack-Development/04-Stripe-Payments/Stripe Configuration Guide]] |
| 7a | Cloud Run vs Vercel — Decision Guide | [[07-Fullstack-Development/05-Deployment/Cloud Run vs Vercel - Decision Guide]] |
| 7b | GCP Cloud Run Setup | [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]] |
| 8 | Architecture & Security Checklist | [[07-Fullstack-Development/06-Architecture-Best-Practices/Fullstack App Checklist]] |

---

## 🔁 Recommended Learning Order

```
Local Setup → Planning with Claude → Firebase Auth → Firestore → Storage
     → Stripe → Cloud Run Setup → Cloud Run vs Vercel → Checklist
```

---

## ⚡ Quick Gotchas (Things That Will Burn You)

> Real lessons extracted from production deployments.

- 🔴 **Cloud Run env vars**: Always use `--update-env-vars`, never `--set-env-vars` — the latter wipes everything
- 🔴 **Firebase private key**: Must be single-line `\\n` format in Cloud Run (not real newlines)
- 🔴 **Firebase authorized domains**: Add BOTH the `*.run.app` URL and your custom domain
- 🔴 **Stripe Promotion Code ≠ Coupon ID** — customers type the Promotion Code, not the internal Coupon ID
- 🔴 **`NEXT_PUBLIC_*` vars** are baked at Docker build time, not at runtime — set them as build args
- 🔴 **`return_url` is required** in `confirmPayment` for Stripe redirect-based payment methods

---

## 🔗 Related Notes

- [[Huggle Project Deploy]] — Real production deployment reference (GCP + Stripe + Firebase)
- [[03-Applications/Publish-an-Application/What is Vercel - Concept Note]]
- [[03-Applications/Publish-an-Application/Environment Variables and API Key Security - Concept Note]]
