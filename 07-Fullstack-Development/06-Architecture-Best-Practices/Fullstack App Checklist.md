---
title: "Fullstack App — Architecture & Security Checklist"
topic: fullstack
status: published
created: 2026-04-13
tags: [architecture, security, checklist, nextjs, firebase, production, best-practices]
---

# ✅ Fullstack App — Architecture & Security Checklist

> The things that don't matter until they really matter. Cover these before going to production.

---

## 🏗️ Architecture Fundamentals

### Server vs Client Boundary

Next.js App Router blurs the line between server and client. Know the rule:

| Code | Runs On | Access To |
|------|---------|-----------|
| `src/app/api/*/route.ts` | Server | All env vars, Firebase Admin, Stripe secret |
| `'use client'` components | Browser | Only `NEXT_PUBLIC_*` vars |
| Server Components (default) | Server | All env vars (but no React state/hooks) |
| Server Actions | Server | All env vars |

> 🔴 **Never import `firebaseAdmin.ts` or use `STRIPE_SECRET_KEY` in client components.** Next.js tree-shakes some of this, but it's easy to accidentally leak secrets into the client bundle.

### Data Flow Pattern

```
Client Component
  → Server Action / API Route (verify auth token)
    → Firebase Admin / Stripe (trusted server-side calls)
      → Firestore / Stripe API
        → Return sanitized data to client
```

Never trust data that comes from the client without validating it server-side.

---

## 🔐 Security Checklist

### Authentication

- [ ] All API routes verify Firebase ID token before processing
- [ ] Token is refreshed regularly (`user.getIdToken(true)` forces refresh)
- [ ] Server uses `adminAuth.verifyIdToken()` — not client-side token inspection
- [ ] Sessions time out appropriately (Firebase tokens expire after 1 hour; auth state persists longer)

### Environment Variables

- [ ] No secrets in `NEXT_PUBLIC_*` variables
- [ ] `.env.local` is in `.gitignore`
- [ ] No hardcoded API keys, passwords, or tokens anywhere in code
- [ ] Production secrets stored in Cloud Run runtime vars (not in `cloudbuild.yaml`)
- [ ] Rotate keys if you ever accidentally commit them

### Firestore Security Rules

- [ ] No collection is `allow read, write: if true` in production
- [ ] Users can only read/write their own documents
- [ ] Server-only writes use `allow write: if false` (Admin SDK bypasses rules)
- [ ] Rules tested in Firebase Emulator or Rules Playground
- [ ] Catch-all `match /{document=**}` deny rule at the bottom

### Firebase Storage Rules

- [ ] No storage path is publicly writable without auth
- [ ] File size limits enforced in rules
- [ ] Content type validated in rules
- [ ] Private files use signed URLs, not permanent download URLs

### API Route Security

- [ ] All mutating routes (POST, PUT, DELETE) require authentication
- [ ] Input is validated before using in any query or action
- [ ] Stripe webhook validates the `stripe-signature` header
- [ ] No sensitive data returned in error responses (no stack traces to client)

---

## 🛡️ Input Validation

**Never trust client input.** Validate on the server.

### Recommended: Zod

```bash
npm install zod
```

```typescript
import { z } from 'zod'

// Define schema
const CreateOrderSchema = z.object({
  amount: z.number().int().min(50).max(100000),  // 50 cents to $1000
  currency: z.enum(['usd', 'gbp', 'eur']),
  promotionCode: z.string().max(50).optional(),
})

// In API route
export async function POST(req: Request) {
  const body = await req.json()
  
  const result = CreateOrderSchema.safeParse(body)
  if (!result.success) {
    return Response.json({ error: 'Invalid input', details: result.error.issues }, { status: 400 })
  }
  
  const { amount, currency, promotionCode } = result.data  // typed and validated
  // ... proceed safely
}
```

---

## 🚦 Rate Limiting

Prevent abuse of your API routes — especially payment endpoints.

### Simple In-Memory Rate Limiter (Development / Low Traffic)

```typescript
// src/lib/rateLimit.ts
const requests = new Map<string, { count: number; resetAt: number }>()

export function rateLimit(key: string, maxRequests: number, windowMs: number): boolean {
  const now = Date.now()
  const record = requests.get(key)

  if (!record || now > record.resetAt) {
    requests.set(key, { count: 1, resetAt: now + windowMs })
    return true  // allowed
  }

  if (record.count >= maxRequests) return false  // blocked
  
  record.count++
  return true
}
```

```typescript
// In API route
import { rateLimit } from '@/lib/rateLimit'

export async function POST(req: Request) {
  const ip = req.headers.get('x-forwarded-for') ?? 'unknown'
  
  if (!rateLimit(ip, 10, 60_000)) {  // 10 requests per minute
    return Response.json({ error: 'Too many requests' }, { status: 429 })
  }
  // ...
}
```

### Production: Use Upstash Redis

For stateless Cloud Run instances, use a distributed rate limiter:

```bash
npm install @upstash/ratelimit @upstash/redis
```

```typescript
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '1 m'),
})
```

---

## 📝 Error Handling

### Server-Side: Never Expose Stack Traces

```typescript
export async function POST(req: Request) {
  try {
    // ... your logic
    return Response.json({ success: true })
  } catch (error) {
    // ✅ Log full error server-side
    console.error('Payment creation failed:', error)
    
    // ✅ Return generic message to client (no stack trace)
    return Response.json({ error: 'An error occurred. Please try again.' }, { status: 500 })
  }
}
```

### Client-Side: User-Friendly Errors

```typescript
try {
  await loginWithEmail(email, password)
} catch (error: any) {
  // Map Firebase error codes to friendly messages
  const messages: Record<string, string> = {
    'auth/user-not-found': 'No account found with this email.',
    'auth/wrong-password': 'Incorrect password.',
    'auth/too-many-requests': 'Too many attempts. Please try again later.',
    'auth/email-already-in-use': 'This email is already registered.',
  }
  
  setError(messages[error.code] ?? 'Something went wrong. Please try again.')
}
```

---

## 🌐 CORS

Next.js API routes allow same-origin by default. If you have a separate frontend:

```typescript
// src/middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  if (request.method === 'OPTIONS') {
    return new NextResponse(null, {
      headers: {
        'Access-Control-Allow-Origin': process.env.NEXT_PUBLIC_APP_URL ?? '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      },
    })
  }
}
```

> 💡 For same-domain deployments (frontend + API on the same Next.js app), CORS is not needed.

---

## 📊 Logging & Monitoring

### Structured Logging for Cloud Run

Cloud Run integrates with Google Cloud Logging. Use structured JSON logs:

```typescript
// src/lib/logger.ts
export const logger = {
  info: (message: string, data?: object) => {
    console.log(JSON.stringify({ severity: 'INFO', message, ...data }))
  },
  error: (message: string, error?: unknown, data?: object) => {
    console.error(JSON.stringify({
      severity: 'ERROR',
      message,
      error: error instanceof Error ? { message: error.message, stack: error.stack } : error,
      ...data,
    }))
  },
}
```

```typescript
// Usage
logger.info('Payment created', { userId, amount, currency })
logger.error('Webhook processing failed', error, { eventType: event.type })
```

In Cloud Run, these structured logs appear in Google Cloud Logging with proper severity filtering.

---

## 💰 Cost Controls

### Cloud Run
- Set **max-instances** — prevents runaway scaling
- Set **min-instances=0** — scales to zero when idle
- Set memory/CPU limits — prevents over-provisioning

### Firestore
- Avoid `getDocs` on large collections without `limit()`
- Cache frequently-read data in React state or localStorage
- Use `onSnapshot` only where real-time is actually needed (it counts as a read per update)

### Firebase Storage
- Set file size limits in security rules
- Delete temp files after processing
- Consider lifecycle rules for old files: **Storage → Lifecycle rules**

### Stripe
- No ongoing cost for Stripe itself (pay per transaction)
- Always use test mode during development — test transactions are free

---

## 🔄 Secrets Rotation Strategy

When you need to rotate a secret (leaked key, periodic rotation):

1. **Stripe keys**: Generate new key in Stripe Dashboard → update Cloud Run var → deploy new revision → delete old key
2. **Firebase Admin key**: Generate new service account JSON → update Cloud Run var → verify working → delete old key
3. **Firebase API key**: Regenerate in Firebase Console → update build vars in cloudbuild.yaml substitutions → redeploy
4. **Webhook secrets**: Create new Stripe webhook endpoint → update `STRIPE_WEBHOOK_SECRET` → verify → delete old endpoint

> 💡 Store secrets in **GCP Secret Manager** for automatic versioning and rotation support — more robust than plain Cloud Run env vars for production.

---

## 📦 Dependency Management

```bash
# Check for outdated packages
npm outdated

# Check for security vulnerabilities
npm audit
npm audit fix  # auto-fix where possible

# Update a specific package
npm update firebase

# Check what's included in your bundle
npx @next/bundle-analyzer  # add ANALYZE=true to .env.local
```

Keep Firebase, Stripe, and Next.js up to date — they release security patches regularly.

---

## 🧪 Testing Checklist (Before Going Live)

### Authentication
- [ ] Google login works
- [ ] Email/password login works
- [ ] Password reset email sends and works
- [ ] Logout clears session
- [ ] Protected routes redirect unauthenticated users

### Payments
- [ ] Payment with test card `4242 4242 4242 4242` succeeds
- [ ] Payment with decline card `4000 0000 0000 0002` shows error
- [ ] Webhook fires and creates Firestore order record
- [ ] Promotion code applies correct discount
- [ ] `return_url` redirects to correct page after Alipay/redirect methods

### Firebase
- [ ] Firestore reads/writes work
- [ ] Security rules prevent unauthorized access (test in emulator)
- [ ] File upload works and URL is accessible
- [ ] File size/type limits enforced

### Deployment
- [ ] Production build (`npm run build`) succeeds without errors
- [ ] All environment variables set correctly
- [ ] Firebase Authorized Domains includes production domain
- [ ] HTTPS works (SSL certificate active)
- [ ] Error pages (404, 500) display correctly

---

## 📁 Project Structure Reference

```
my-app/
├── src/
│   ├── app/
│   │   ├── layout.tsx          ← Wrap with AuthProvider here
│   │   ├── page.tsx
│   │   ├── (auth)/             ← Route group for auth pages
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── dashboard/page.tsx  ← Protected route
│   │   └── api/
│   │       ├── create-payment/route.ts
│   │       └── stripe-webhook/route.ts
│   ├── lib/
│   │   ├── firebase.ts         ← Client Firebase init
│   │   ├── firebaseAdmin.ts    ← Server Firebase Admin init
│   │   ├── firestore.ts        ← Firestore CRUD helpers
│   │   ├── storage.ts          ← Firebase Storage helpers
│   │   ├── stripe.ts           ← Stripe server instance
│   │   ├── rateLimit.ts        ← Rate limiting utility
│   │   └── logger.ts           ← Structured logging
│   ├── components/
│   │   ├── AuthProvider.tsx    ← Auth context
│   │   ├── ProtectedRoute.tsx  ← Redirect if not auth
│   │   ├── CheckoutForm.tsx    ← Stripe Elements form
│   │   └── StripeProvider.tsx  ← Stripe Elements provider
│   └── types/
│       └── index.ts            ← Shared TypeScript types
├── .env.local                  ← Never commit
├── Dockerfile
├── cloudbuild.yaml
├── next.config.ts
└── package.json
```

---

## 🔗 Related Notes

- [[07-Fullstack-Development/02-Local-Environment/Node.js & Next.js Setup]]
- [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]]
- [[07-Fullstack-Development/03-Firebase/Firestore Database]]
- [[07-Fullstack-Development/04-Stripe-Payments/Stripe Configuration Guide]]
- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[07-Fullstack-Development/00-INDEX]]
