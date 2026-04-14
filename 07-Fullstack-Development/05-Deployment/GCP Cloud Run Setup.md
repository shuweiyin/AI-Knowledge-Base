---
title: "GCP Cloud Run Setup"
topic: fullstack
status: published
created: 2026-04-13
tags: [gcp, cloud-run, docker, deployment, nextjs, firebase, cloudbuild]
---

# 🚀 GCP Cloud Run Setup

> Step-by-step guide to deploying a Next.js + Firebase + Stripe app on GCP Cloud Run. Includes hard-won lessons from the Huggle production deployment.

---

## Prerequisites

- GCP project created at https://console.cloud.google.com
- `gcloud` CLI installed and authenticated
- Docker Desktop installed (for local testing)
- Your Next.js app is working locally

---

## Step 1 — Install & Configure gcloud CLI

```bash
# macOS (Homebrew)
brew install --cask google-cloud-sdk

# Authenticate
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Verify
gcloud config get-value project
```

---

## Step 2 — Enable Required APIs

Run once per project (you'll be prompted automatically on first build, but doing it upfront avoids mid-deploy failures):

```bash
gcloud services enable \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  containerregistry.googleapis.com \
  secretmanager.googleapis.com
```

---

## Step 3 — Write the Dockerfile

In your project root, create `Dockerfile`:

```dockerfile
# Stage 1: Install dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --only=production

# Stage 2: Build the Next.js app
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# NEXT_PUBLIC_* vars must be baked in at build time
# Pass them as build args
ARG NEXT_PUBLIC_FIREBASE_API_KEY
ARG NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN
ARG NEXT_PUBLIC_FIREBASE_PROJECT_ID
ARG NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET
ARG NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID
ARG NEXT_PUBLIC_FIREBASE_APP_ID
ARG NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY
ARG NEXT_PUBLIC_APP_URL

ENV NEXT_PUBLIC_FIREBASE_API_KEY=$NEXT_PUBLIC_FIREBASE_API_KEY
ENV NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=$NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN
ENV NEXT_PUBLIC_FIREBASE_PROJECT_ID=$NEXT_PUBLIC_FIREBASE_PROJECT_ID
ENV NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=$NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET
ENV NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=$NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID
ENV NEXT_PUBLIC_FIREBASE_APP_ID=$NEXT_PUBLIC_FIREBASE_APP_ID
ENV NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=$NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY
ENV NEXT_PUBLIC_APP_URL=$NEXT_PUBLIC_APP_URL

RUN npm run build

# Stage 3: Production runner
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000
ENV PORT=3000
CMD ["node", "server.js"]
```

### Enable Standalone Output in `next.config.ts`

```typescript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',  // Required for Docker deployment
}

export default nextConfig
```

---

## Step 4 — Write cloudbuild.yaml

This file tells Cloud Build how to build and deploy. Create at project root:

```yaml
steps:
  # Step 1: Build the Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '--tag'
      - 'gcr.io/$PROJECT_ID/my-app:$COMMIT_SHA'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_API_KEY=${_NEXT_PUBLIC_FIREBASE_API_KEY}'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=${_NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN}'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_PROJECT_ID=${_NEXT_PUBLIC_FIREBASE_PROJECT_ID}'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=${_NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET}'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=${_NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID}'
      - '--build-arg'
      - 'NEXT_PUBLIC_FIREBASE_APP_ID=${_NEXT_PUBLIC_FIREBASE_APP_ID}'
      - '--build-arg'
      - 'NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=${_NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY}'
      - '--build-arg'
      - 'NEXT_PUBLIC_APP_URL=${_NEXT_PUBLIC_APP_URL}'
      - '.'

  # Step 2: Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/my-app:$COMMIT_SHA']

  # Step 3: Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'my-app'                              # Cloud Run service name
      - '--image=gcr.io/$PROJECT_ID/my-app:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'             # public access
      - '--memory=512Mi'
      - '--cpu=1'
      - '--min-instances=0'
      - '--max-instances=10'
      # 🔴 CRITICAL: use --update-env-vars, NOT --set-env-vars
      # --set-env-vars wipes all existing env vars on every deploy
      # --update-env-vars only updates what you specify
      - '--update-env-vars=NODE_ENV=production'

images:
  - 'gcr.io/$PROJECT_ID/my-app:$COMMIT_SHA'

# Substitution variables for NEXT_PUBLIC_* (set these in Cloud Build trigger)
substitutions:
  _NEXT_PUBLIC_FIREBASE_API_KEY: ''
  _NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN: ''
  _NEXT_PUBLIC_FIREBASE_PROJECT_ID: ''
  _NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET: ''
  _NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID: ''
  _NEXT_PUBLIC_FIREBASE_APP_ID: ''
  _NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: ''
  _NEXT_PUBLIC_APP_URL: ''
```

---

## Step 5 — Set Cloud Run Runtime Environment Variables

These are the **server-side secrets** — set them once in the Cloud Run console, and `--update-env-vars` will never touch them.

Path: **Cloud Run → your-service → Edit & Deploy New Revision → Variables & Secrets**

| Variable | Value | Notes |
|----------|-------|-------|
| `FIREBASE_ADMIN_PROJECT_ID` | `your-project-id` | |
| `FIREBASE_ADMIN_CLIENT_EMAIL` | `firebase-adminsdk@...` | From service account JSON |
| `FIREBASE_ADMIN_PRIVATE_KEY` | `-----BEGIN PRIVATE KEY-----\nMIIE...` | **Single line, `\n` as literal text** |
| `STRIPE_SECRET_KEY` | `sk_live_...` | Live key for production |
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | From Stripe Dashboard after creating endpoint |

### ⚠️ FIREBASE_ADMIN_PRIVATE_KEY Format

This is the #1 cause of Cloud Run deployment failures. When pasting into Cloud Run:

```
# ✅ CORRECT — single line, \n as literal characters (backslash + n)
-----BEGIN PRIVATE KEY-----\nMIIEvQ...rest of key...\n-----END PRIVATE KEY-----\n

# ❌ WRONG — with real line breaks
-----BEGIN PRIVATE KEY-----
MIIEvQ...
-----END PRIVATE KEY-----

# ❌ WRONG — with outer quotes
"-----BEGIN PRIVATE KEY-----\nMIIEvQ...\n-----END PRIVATE KEY-----\n"
```

Your server code converts `\\n` → real newlines:
```typescript
privateKey: process.env.FIREBASE_ADMIN_PRIVATE_KEY?.replace(/\\n/g, '\n')
```

---

## Step 6 — Grant Cloud Build Permissions

Cloud Build needs IAM roles to deploy to Cloud Run.

```bash
# Get your project number
gcloud projects describe YOUR_PROJECT_ID --format='value(projectNumber)'

# Grant required roles to Cloud Build service account
PROJECT_NUMBER=123456789
CLOUD_BUILD_SA="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/storage.admin"
```

If you skip this: you'll get `PERMISSION_DENIED` errors on the deploy step.

---

## Step 7 — Deploy

```bash
gcloud builds submit --config cloudbuild.yaml .
```

Build time: ~3–5 minutes. Cloud Run automatically routes traffic to the new revision.

---

## Step 8 — Custom Domain

### Option A: Cloud Run Domain Mapping

Path: **Cloud Run → your-service → Custom domains → Add mapping**

1. Enter your domain (e.g. `app.yourdomain.com`)
2. Cloud Run gives you DNS records (CNAME or A record)
3. Add to your DNS provider (Cloudflare, GoDaddy, etc.)
4. Wait 5–30 minutes for DNS propagation
5. Cloud Run auto-provisions TLS/HTTPS

### Option B: Load Balancer (Advanced)

Use if you need CDN, WAF, or multiple backends behind one domain. More complex setup — not usually needed for most apps.

---

## Step 9 — Add Domain to Firebase Authorized Domains

⚠️ **Do this before testing login** — or Google Auth will silently fail.

Path: **Firebase Console → Authentication → Settings → Authorized domains**

Add both:
- `your-service-xyz-123.run.app` (Cloud Run auto-generated domain)
- `app.yourdomain.com` (your custom domain)

---

## Updating Your Deployment

Every time you update code:

```bash
gcloud builds submit --config cloudbuild.yaml .
```

Cloud Run creates a new revision and shifts traffic automatically. Zero downtime.

---

## --update-env-vars vs --set-env-vars ⚠️

This is the most critical operational gotcha.

| Flag | Behavior |
|------|---------|
| `--update-env-vars=KEY=VALUE` | Only changes the specified vars. Other vars (Firebase key, Stripe secret) are **untouched**. ✅ |
| `--set-env-vars=KEY=VALUE` | **Replaces ALL env vars** with only what you specify. Everything else is wiped. ❌ |

**Always use `--update-env-vars` in `cloudbuild.yaml`.**

If you accidentally used `--set-env-vars` and wiped your secrets:
1. Go to Cloud Run → your service → Edit & Deploy New Revision
2. Variables & Secrets → re-enter all the values from Step 5
3. Deploy

Signs that this happened: 401 Unauthorized, Firebase Admin initialization failed, Stripe webhook errors.

---

## Viewing Logs

```bash
# Stream logs
gcloud run services logs read my-app --region=us-central1 --limit=50

# Or in Cloud Console:
# Cloud Run → your-service → Logs → filter by severity: ERROR
```

---

## Cloud Run Configuration Reference

| Setting | Recommended | Notes |
|---------|-------------|-------|
| Memory | 512Mi–1Gi | 512Mi is fine for most Next.js apps |
| CPU | 1 | 2 if you're doing heavy processing |
| Min instances | 0 | Scales to zero (cost-saving) |
| Max instances | 10–100 | Depends on expected traffic |
| Request timeout | 300s | Increase if you have long operations |
| Concurrency | 80 (default) | Max concurrent requests per instance |
| Region | Closest to users | `us-central1`, `europe-west1`, etc. |

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| 401 Unauthorized on all requests | Firebase private key wiped | Re-enter env vars in Cloud Run |
| Google login popup flashes | Firebase Authorized Domains missing | Add `*.run.app` and custom domain |
| Stripe webhook 400 errors | Webhook secret wrong or missing | Check `STRIPE_WEBHOOK_SECRET` in Cloud Run |
| `PERMISSION_DENIED` in Cloud Build | Missing IAM roles | Grant Cloud Run Admin + Service Account User |
| App loads but env vars are undefined | `NEXT_PUBLIC_*` not set as build args | Add them to cloudbuild.yaml `--build-arg` |
| Cold start latency > 5s | Min instances = 0 + large image | Set min-instances=1 or reduce image size |
| Build fails: "cannot find module" | `node_modules` not in Docker image | Check `npm ci` step in Dockerfile |

---

## Full Deployment Checklist

```
Before first deploy:
  [ ] Dockerfile created with standalone output
  [ ] next.config.ts has output: 'standalone'
  [ ] cloudbuild.yaml uses --update-env-vars
  [ ] Cloud Build service account has IAM roles
  [ ] All NEXT_PUBLIC_* vars set as Cloud Build substitutions
  [ ] All secret vars set in Cloud Run runtime (Step 5)
  [ ] Firebase Authorized Domains includes *.run.app URL

After first deploy:
  [ ] Test Google login
  [ ] Test email login
  [ ] Test Stripe payment (test mode)
  [ ] Test Stripe webhook (Stripe CLI)
  [ ] Check Cloud Run logs for errors

Before going live:
  [ ] Switch to Stripe live keys
  [ ] Add custom domain + update Firebase Authorized Domains
  [ ] Set NEXT_PUBLIC_APP_URL to production URL
  [ ] Configure Stripe webhook endpoint with production URL
  [ ] Test payment flow end-to-end
```

---

## 🔗 Related Notes

- [[07-Fullstack-Development/05-Deployment/Cloud Run vs Vercel - Decision Guide]]
- [[07-Fullstack-Development/04-Stripe-Payments/Stripe Configuration Guide]]
- [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]]
- [[Huggle Project Deploy]]
- [[07-Fullstack-Development/00-INDEX]]
