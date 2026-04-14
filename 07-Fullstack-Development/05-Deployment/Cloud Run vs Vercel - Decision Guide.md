---
title: "Cloud Run vs Vercel — Decision Guide"
topic: fullstack
status: published
created: 2026-04-13
tags: [deployment, cloud-run, vercel, gcp, nextjs, docker, decision]
---

# ⚖️ Cloud Run vs Vercel — Decision Guide

> The right deployment platform dramatically simplifies your life. The wrong one creates invisible constraints you'll fight for months. Here's how to choose.

---

## Quick Decision Matrix

| Question | If YES → | If YES → |
|----------|----------|----------|
| Pure Next.js app, no custom server? | Vercel ✅ | |
| Uses Firebase Client SDK only (no Admin)? | Vercel ✅ | |
| Needs Firebase Admin SDK server-side? | Either works | Cloud Run ✅ better |
| Needs long-running server processes (> 60s)? | Cloud Run ✅ | |
| Needs a persistent Docker container at **runtime**? | Cloud Run ✅ | |
| Uses other GCP services (Pub/Sub, Cloud Tasks)? | Cloud Run ✅ | |
| Want zero-config deploy from Git? | Vercel ✅ | |
| Need to control the runtime environment exactly? | Cloud Run ✅ | |
| Have a multi-service backend (microservices)? | Cloud Run ✅ | |
| Building an MVP / side project fast? | Vercel ✅ | |
| Need cost predictability at scale? | Cloud Run ✅ | |
| Team is comfortable with Docker? | Cloud Run ✅ | |

---

## Side-by-Side Comparison

| Feature | Vercel | GCP Cloud Run |
|---------|--------|---------------|
| **Setup complexity** | Near zero (connect GitHub → done) | Medium (Dockerfile, cloudbuild.yaml, gcloud CLI) |
| **Next.js support** | First-class (made by same team) | Good (Next.js in Docker) |
| **Custom server** | ❌ No (serverless functions only) | ✅ Yes (full Node.js server) |
| **Docker at runtime** | ❌ No — code runs as serverless functions | ✅ Yes (required) |
| **Docker at build time** | ✅ Yes — Vercel builds inside Amazon Linux 2023 container (install tools via `dnf`) | ✅ Yes (full control) |
| **Cold starts** | ~200ms | ~500ms–2s (first request after idle) |
| **Execution timeout** | 60s (Pro: 300s) | Up to 60 minutes |
| **Concurrency** | 1 request per function instance | Up to 1000 per container instance |
| **Env vars** | Dashboard or CLI | Cloud Run console or cloudbuild.yaml |
| **`NEXT_PUBLIC_*` vars** | Set at deploy time, auto-baked | Must be `--build-arg` in Dockerfile |
| **Auto-scaling** | ✅ Instant | ✅ Yes (with cold start delay) |
| **Scale to zero** | ✅ Yes | ✅ Yes (free tier at zero) |
| **Pricing model** | Per function invocation + bandwidth | Per CPU/memory second + requests |
| **Free tier** | Generous (hobby plan) | Generous (2M requests/month) |
| **Custom domains** | Simple (DNS + dashboard) | Slightly more steps |
| **Preview deployments** | ✅ Every PR gets a URL | ❌ Manual setup required |
| **Deployment speed** | ~1 min | ~3–5 min (Docker build) |
| **GCP integration** | Requires extra setup | Native (same ecosystem) |

---

## ⚠️ Clarification: "Vercel Supports Docker" — What That Actually Means

You may have seen Vercel's [Build Image docs](https://vercel.com/docs/builds/build-image) and thought Vercel supports Docker deployment. Here's the distinction:

| | Vercel | Cloud Run |
|--|--------|-----------|
| **Build time** | ✅ Vercel runs your `npm run build` inside an **Amazon Linux 2023 container**. You can install extra build-time tools (e.g. `ffmpeg` for an image processing build step) using `dnf install`. | ✅ You write a full `Dockerfile` — complete control |
| **Runtime** | ❌ Your deployed code runs as **serverless functions** (microVMs). You cannot bring your own Dockerfile to control the server process. | ✅ Your Docker container **is** the server — persistent, long-running |

**The key difference**: Vercel uses Docker *internally* to build your app — but what gets deployed is not a Docker container. It's a bundle of serverless functions. You cannot write a `CMD ["node", "server.js"]` that runs persistently on Vercel.

If you need:
- Custom system dependencies **at build time only** (e.g. a binary for asset generation) → Vercel's `installCommand` + `dnf` is enough
- A **persistent server process** with full Docker control at runtime → Cloud Run

---

## When to Choose Vercel

### ✅ Use Vercel When:

**1. Pure Next.js App (No Heavy Backend)**
You're building a marketing site, dashboard, or SaaS where every "server" action is a short-lived API route (< 60s). Firebase client SDK, Stripe client — all fine.

**2. You Want to Ship Fast**
Connect GitHub repo → Vercel auto-deploys on every push. Preview URLs on every PR. Zero infrastructure knowledge required. For MVPs, side projects, and prototypes, this is unbeatable.

**3. Team Doesn't Know Docker**
No Dockerfile, no container registry, no `gcloud` CLI. Vercel abstracts all of it.

**4. Static + Incremental Static Regeneration (ISR)**
Vercel invented ISR. It's optimally supported there — edge caching, automatic revalidation.

**5. Multiple Environments Are Important**
Production + staging + per-PR previews all work automatically.

### Example Projects on Vercel
- Marketing website with a contact form
- SaaS dashboard (Next.js + Prisma/Postgres)
- Blog or documentation site
- Simple e-commerce with Stripe
- AI chatbot interface (calls external APIs)

---

## When to Choose Cloud Run

### ✅ Use Cloud Run When:

**1. Firebase Admin SDK in Server Code**
The Admin SDK needs service account credentials (private key). It works fine on Vercel too, but Cloud Run keeps everything in the GCP ecosystem — IAM, secrets, logging all in one place.

**2. Long-Running Processes**
Generating PDFs, processing large files, calling slow external APIs, running ML inference. Vercel times out at 60 seconds (300s on Pro). Cloud Run handles up to 60 minutes.

**3. WebSockets or Streaming Responses**
Vercel functions are stateless HTTP. Cloud Run runs a persistent server — it supports WebSockets, server-sent events, and streaming natively.

**4. You're Already in the GCP Ecosystem**
Using Firestore, Cloud Storage, Cloud Tasks, Pub/Sub, or BigQuery? Cloud Run is already authenticated via IAM. No extra credential management.

**5. Cost at Scale**
Cloud Run bills per 100ms of CPU/memory used. At high volume, this is often cheaper than Vercel's per-invocation pricing. At zero traffic, you pay nothing.

**6. Multi-Service Architecture**
Running multiple microservices? Each Cloud Run service is isolated, independently scalable, and can communicate internally via service-to-service auth.

**7. Full Control Over Runtime**
Need a specific Node.js version, custom system dependencies (`ffmpeg`, `ImageMagick`, `wkhtmltopdf`), or a non-Node runtime? Dockerfile gives you full control.

### Example Projects on Cloud Run
- Full-stack app with Firebase Admin + Stripe webhooks 
- PDF generation service
- Video processing pipeline
- Multi-tenant SaaS with complex auth
- AI backend calling multiple external services
- Any app that already uses GCP infrastructure

---

## The Hybrid Architecture (Best of Both)

For many apps, the optimal architecture uses **both**:

```
┌─────────────────────────────────────────────┐
│                 Users                        │
└────────────────────┬────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
   ┌─────▼──────┐          ┌─────▼──────────┐
   │   Vercel   │          │  GCP Cloud Run  │
   │            │          │                 │
   │ Next.js    │          │ API server      │
   │ Frontend   │◄────────►│ (Node/Express)  │
   │ + SSR      │          │ Long processes  │
   │ + Static   │          │ WebSockets      │
   └────────────┘          └─────────────────┘
```

Front-end and simple API routes → Vercel.
Heavy processing, long-running tasks → Cloud Run.

---

## Cost Comparison (Rough Estimates)

### Small App (~10K users/month)
| Platform | Estimated Cost |
|----------|---------------|
| Vercel Hobby | Free |
| Vercel Pro | $20/month |
| Cloud Run | ~$0–5/month |

### Medium App (~100K users/month)
| Platform | Estimated Cost |
|----------|---------------|
| Vercel Pro | $20/month + overages |
| Cloud Run | ~$10–30/month |

### High Traffic (~1M requests/month)
| Platform | Estimated Cost |
|----------|---------------|
| Vercel (with overages) | Can get expensive quickly |
| Cloud Run | Predictable per-usage billing |

> 💡 Cloud Run scales to zero (no traffic = no cost). Vercel's hobby plan also scales to zero. The cost gap mainly matters at medium-to-high scale.

---

## Migration Path

If you start on Vercel and later need Cloud Run:

1. Add a `Dockerfile` to your Next.js app
2. Create a `cloudbuild.yaml`
3. Move `NEXT_PUBLIC_*` vars to Docker build args
4. Move server secrets to Cloud Run runtime vars
5. Update Firebase authorized domains
6. Point DNS to Cloud Run's URL

It's manageable — but plan ahead if you know you'll need Cloud Run features.

---

## Decision Flowchart

```
Start
  │
  ▼
Do you need Firebase Admin SDK?
  ├── No → Both work, lean Vercel (simpler)
  └── Yes → Both work, lean Cloud Run (GCP native)

Do you have long-running server tasks (> 60s)?
  ├── No → Vercel fine
  └── Yes → Cloud Run required

Do you need Docker at RUNTIME (persistent server process)?
  ├── No → Vercel fine (it uses a container internally at build time, but not at runtime)
  └── Yes → Cloud Run required

Do you need custom system dependencies at BUILD TIME only (e.g. a binary for asset generation)?
  ├── Yes → Vercel works (use installCommand + dnf)
  └── Need them at runtime too → Cloud Run

Are you already using GCP services?
  ├── No → Vercel simpler
  └── Yes → Cloud Run (native integration)

Is this an MVP / side project?
  ├── Yes → Vercel (speed to ship)
  └── No → Evaluate based on above

Team comfortable with Docker?
  ├── No → Vercel
  └── Yes → Either works
```

---

## Summary Recommendation

| Project Type                         | Recommendation                         |
| ------------------------------------ | -------------------------------------- |
| Marketing site, blog                 | Vercel                                 |
| Simple SaaS (Next.js + DB + Stripe)  | Vercel (start here, migrate if needed) |
| Firebase Admin + Stripe              | Cloud Run ✅                            |
| App with WebSockets / streaming      | Cloud Run ✅                            |
| PDF/video/image processing           | Cloud Run ✅                            |
| GCP-native microservices             | Cloud Run ✅                            |
| MVP you need live in 1 hour          | Vercel ✅                               |
| Production app with Docker expertise | Cloud Run ✅                            |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[Huggle Project Deploy]]
- [[03-Applications/Publish-an-Application/What is Vercel - Concept Note]]
- [[07-Fullstack-Development/00-INDEX]]
