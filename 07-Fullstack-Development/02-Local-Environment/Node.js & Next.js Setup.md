---
title: "Local Environment Setup — Node.js & Next.js"
topic: fullstack
status: published
created: 2026-04-13
tags: [nodejs, nextjs, nvm, local-dev, environment, setup]
---

# 💻 Local Environment Setup — Node.js & Next.js

> Everything you need to go from a blank machine to a running Next.js fullstack app in one pass.

---

## Overview

```
nvm → Node.js (LTS) → npm/pnpm → create-next-app → .env.local → run dev
```

---

## Step 1 — Install nvm (Node Version Manager)

**Never install Node.js directly.** Use `nvm` so you can switch Node versions per project.

### macOS / Linux
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Then restart your terminal, or run:
```bash
source ~/.zshrc    # or ~/.bashrc
```

Verify:
```bash
nvm --version   # should print something like 0.39.7
```

### Windows
Use **nvm-windows**: https://github.com/coreybutler/nvm-windows/releases
Download and run the installer.

---

## Step 2 — Install Node.js LTS

```bash
nvm install --lts          # installs latest LTS (e.g. 20.x)
nvm use --lts              # activate it
nvm alias default --lts    # make it the default for new terminals
```

Verify:
```bash
node --version   # e.g. v20.12.0
npm --version    # e.g. 10.5.0
```

> 💡 **Which version?** Always use LTS (Long-Term Support) for production apps. Avoid odd-numbered versions (21, 23) — they're experimental.

---

## Step 3 — (Optional) Install pnpm

`pnpm` is faster and more disk-efficient than `npm`. Many Next.js projects use it.

```bash
npm install -g pnpm
pnpm --version
```

You can also use `npm` — both work fine. Just be consistent within a project.

---

## Step 4 — Create a Next.js App

```bash
npx create-next-app@latest my-app
```

You'll be prompted:
```
✔ Would you like to use TypeScript? › Yes
✔ Would you like to use ESLint? › Yes
✔ Would you like to use Tailwind CSS? › Yes
✔ Would you like to use `src/` directory? › Yes
✔ Would you like to use App Router? › Yes
✔ Would you like to customize the import alias? › No
```

> 📌 Always choose **App Router** (not Pages Router) for new projects — it's the current Next.js standard.

Then:
```bash
cd my-app
npm run dev      # starts on http://localhost:3000
```

---

## Step 5 — Install Firebase & Stripe

```bash
npm install firebase           # Firebase v9+ (modular SDK)
npm install firebase-admin     # Server-side Firebase (Admin SDK)
npm install stripe             # Stripe Node SDK (server-side)
npm install @stripe/stripe-js  # Stripe browser SDK (client-side)
npm install @stripe/react-stripe-js  # React components for Stripe
```

---

## Step 6 — Set Up Environment Variables

**Never hardcode secrets.** Use `.env.local` for local development.

### Create `.env.local`

```bash
touch .env.local
```

```ini
# .env.local — local dev only, never commit this file

# Firebase (Client SDK) — safe to expose, but still keep out of git
NEXT_PUBLIC_FIREBASE_API_KEY=AIza...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abc123

# Firebase Admin SDK — SERVER SIDE ONLY, never expose
FIREBASE_ADMIN_PROJECT_ID=your-project
FIREBASE_ADMIN_CLIENT_EMAIL=firebase-adminsdk@your-project.iam.gserviceaccount.com
FIREBASE_ADMIN_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----\n"

# Stripe
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### Variable Naming Rules

| Prefix | Where Available | Use For |
|--------|----------------|---------|
| `NEXT_PUBLIC_` | Browser + Server | Firebase client config, Stripe publishable key, app URL |
| (no prefix) | Server only | Firebase Admin private key, Stripe secret key, webhook secret |

> ⚠️ **Never put secret keys in `NEXT_PUBLIC_` variables** — they get embedded in the client JS bundle and are visible to anyone.

### Add to `.gitignore`

Your `.gitignore` should already include `.env.local` from `create-next-app`. Double-check:

```bash
grep ".env" .gitignore
# Should show:  .env*.local
```

If not, add it manually:
```
.env*.local
.env.local
.env.production.local
```

---

## Step 7 — Project Structure

Recommended structure for a fullstack Next.js + Firebase + Stripe app:

```
my-app/
├── src/
│   ├── app/                        ← Next.js App Router pages
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   └── api/                    ← API Routes (server-side)
│   │       ├── stripe-webhook/
│   │       │   └── route.ts
│   │       └── create-payment/
│   │           └── route.ts
│   ├── lib/                        ← Shared utilities
│   │   ├── firebase.ts             ← Firebase client init
│   │   ├── firebaseAdmin.ts        ← Firebase Admin init (server only)
│   │   ├── firestore.ts            ← Firestore helpers
│   │   ├── storage.ts              ← Firebase Storage helpers
│   │   └── stripe.ts               ← Stripe helpers
│   ├── components/                 ← React components
│   │   ├── AuthProvider.tsx        ← Auth context
│   │   ├── CheckoutForm.tsx        ← Stripe payment form
│   │   └── ...
│   └── types/                      ← TypeScript types
│       └── index.ts
├── public/
├── .env.local                      ← Never commit
├── .gitignore
├── next.config.ts
├── package.json
└── tsconfig.json
```

---

## Step 8 — Initialize Firebase Config Files

### `src/lib/firebase.ts` (Client SDK)

```typescript
import { initializeApp, getApps } from 'firebase/app'
import { getAuth } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'
import { getStorage } from 'firebase/storage'

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
}

// Prevent multiple initializations in Next.js hot reload
const app = getApps().length ? getApps()[0] : initializeApp(firebaseConfig)

export const auth = getAuth(app)
export const db = getFirestore(app)
export const storage = getStorage(app)
```

### `src/lib/firebaseAdmin.ts` (Server-Side Admin SDK)

```typescript
import { initializeApp, getApps, cert } from 'firebase-admin/app'
import { getAuth } from 'firebase-admin/auth'
import { getFirestore } from 'firebase-admin/firestore'

const adminApp = getApps().length === 0
  ? initializeApp({
      credential: cert({
        projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
        clientEmail: process.env.FIREBASE_ADMIN_CLIENT_EMAIL,
        // Replace \\n with real newlines (needed when key is stored as env var)
        privateKey: process.env.FIREBASE_ADMIN_PRIVATE_KEY?.replace(/\\n/g, '\n'),
      }),
    })
  : getApps()[0]

export const adminAuth = getAuth(adminApp)
export const adminDb = getFirestore(adminApp)
```

> 🔑 The `.replace(/\\n/g, '\n')` is critical — environment variables store newlines as literal `\n` text, but the private key needs real newlines.

---

## Common npm Scripts

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit"
  }
}
```

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start local dev server with hot reload |
| `npm run build` | Production build (use this to catch type errors) |
| `npm run start` | Run the production build locally |
| `npm run type-check` | Check TypeScript without building |

---

## Troubleshooting Common Issues

| Problem | Fix |
|---------|-----|
| `Module not found: firebase/app` | Run `npm install firebase` |
| Firebase "app already initialized" error | Use `getApps().length` guard (shown above) |
| Env vars are `undefined` | Check `NEXT_PUBLIC_` prefix for client-side vars; restart dev server after editing `.env.local` |
| `process.env` works server-side but not client | Add `NEXT_PUBLIC_` prefix |
| Type errors from Firebase | Install `@types/node` if needed; Firebase v9+ has built-in types |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]]
- [[07-Fullstack-Development/03-Firebase/Firestore Database]]
- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[07-Fullstack-Development/00-INDEX]]
