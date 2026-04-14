---
title: "Stripe Configuration Guide"
topic: fullstack
status: published
created: 2026-04-13
tags: [stripe, payments, nextjs, webhook, payment-intent, cloud-run]
---

# 💳 Stripe Configuration Guide

> A production-tested guide to integrating Stripe with Next.js. Informed by real deployment experience from the Huggle project on GCP Cloud Run. Read this before touching any Stripe code.

---

## Core Concepts

| Term | What It Is |
|------|-----------|
| **Publishable Key** (`pk_test_...` / `pk_live_...`) | Client-side key — safe to expose in browser JS |
| **Secret Key** (`sk_test_...` / `sk_live_...`) | Server-side only — never expose to browser |
| **PaymentIntent** | A server-side object representing one payment attempt |
| **Payment Element** | Stripe's pre-built React UI that handles card, Alipay, WeChat, etc. |
| **Webhook** | Stripe calls your server when payment events happen |
| **Webhook Signing Secret** (`whsec_...`) | Used to verify webhook calls really come from Stripe |
| **Promotion Code** | Customer-facing code (e.g. `SAVE20`) — maps to a Coupon |
| **Coupon** | Internal discount rule — customers never type this directly |

---

## Environment Variables

```ini
# .env.local

# Client-safe (browser)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...

# Server-only (never expose)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

> ⚠️ **Test vs Live**: Use `pk_test_` / `sk_test_` during development. Only switch to live keys (`pk_live_` / `sk_live_`) in production. Live keys charge real cards.

---

## Install Stripe

```bash
npm install stripe              # Server-side Node SDK
npm install @stripe/stripe-js   # Client-side browser SDK
npm install @stripe/react-stripe-js  # React UI components
```

---

## Server Setup — `src/lib/stripe.ts`

```typescript
import Stripe from 'stripe'

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-06-20',  // pin to a specific version
})
```

---

## Step 1 — Create a PaymentIntent (Server)

The server creates the PaymentIntent and returns the `client_secret` to the browser. **The browser never calls Stripe directly to create payment intents** — that would bypass your server-side checks.

```typescript
// src/app/api/create-payment/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { stripe } from '@/lib/stripe'
import { adminAuth } from '@/lib/firebaseAdmin'

export async function POST(req: NextRequest) {
  // 1. Verify the user is authenticated
  const token = req.headers.get('Authorization')?.split('Bearer ')[1]
  if (!token) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  
  const decoded = await adminAuth.verifyIdToken(token)
  
  // 2. Parse the request
  const { amount, currency = 'usd', promotionCode } = await req.json()

  // 3. (Optional) Validate a promotion code
  let discountedAmount = amount
  if (promotionCode) {
    const codes = await stripe.promotionCodes.list({ code: promotionCode, active: true })
    if (codes.data.length > 0) {
      const coupon = codes.data[0].coupon
      if (coupon.percent_off) {
        discountedAmount = Math.round(amount * (1 - coupon.percent_off / 100))
      }
    }
  }

  // 4. Create the PaymentIntent
  const paymentIntent = await stripe.paymentIntents.create({
    amount: discountedAmount,      // in cents, e.g. 2000 = $20.00
    currency,
    automatic_payment_methods: { enabled: true },  // enables card, Alipay, WeChat Pay, etc.
    metadata: {
      userId: decoded.uid,         // attach user ID for webhook reference
      promotionCode: promotionCode ?? '',
    },
  })

  return NextResponse.json({
    clientSecret: paymentIntent.client_secret,
    amount: discountedAmount,
  })
}
```

---

## Step 2 — Stripe Payment UI (Client)

### Provider Wrapper

```typescript
// src/components/StripeProvider.tsx
'use client'

import { Elements } from '@stripe/react-stripe-js'
import { loadStripe } from '@stripe/stripe-js'

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!)

export function StripeProvider({ children, clientSecret }: {
  children: React.ReactNode
  clientSecret: string
}) {
  return (
    <Elements stripe={stripePromise} options={{ clientSecret }}>
      {children}
    </Elements>
  )
}
```

### Checkout Form

```typescript
// src/components/CheckoutForm.tsx
'use client'

import { useState } from 'react'
import { PaymentElement, useStripe, useElements } from '@stripe/react-stripe-js'

export function CheckoutForm() {
  const stripe = useStripe()
  const elements = useElements()
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!stripe || !elements) return

    setLoading(true)
    setError(null)

    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        // 🔴 return_url is REQUIRED for redirect-based methods (Alipay, etc.)
        return_url: `${process.env.NEXT_PUBLIC_APP_URL}/payment-success`,
      },
    })

    if (error) {
      // Payment failed or user canceled
      setError(error.message ?? 'Payment failed')
      setLoading(false)
    }
    // If no error + redirect methods: Stripe redirects automatically
    // For card payments: onSuccess fires here
  }

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button type="submit" disabled={!stripe || loading}>
        {loading ? 'Processing...' : 'Pay Now'}
      </button>
    </form>
  )
}
```

### Checkout Page That Wires It Together

```typescript
// src/app/checkout/page.tsx
'use client'

import { useState, useEffect } from 'react'
import { StripeProvider } from '@/components/StripeProvider'
import { CheckoutForm } from '@/components/CheckoutForm'
import { useAuth } from '@/components/AuthProvider'
import { auth } from '@/lib/firebase'

export default function CheckoutPage() {
  const { user } = useAuth()
  const [clientSecret, setClientSecret] = useState('')

  useEffect(() => {
    if (!user) return
    
    async function createIntent() {
      const token = await auth.currentUser!.getIdToken()
      const res = await fetch('/api/create-payment', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ amount: 2000, currency: 'usd' }),
      })
      const { clientSecret } = await res.json()
      setClientSecret(clientSecret)
    }
    
    createIntent()
  }, [user])

  if (!clientSecret) return <div>Loading payment...</div>

  return (
    <StripeProvider clientSecret={clientSecret}>
      <CheckoutForm />
    </StripeProvider>
  )
}
```

---

## Step 3 — Webhook Handler

The webhook is how Stripe tells your server "the payment succeeded." **Don't fulfill orders without webhook confirmation** — client-side success callbacks can be faked.

```typescript
// src/app/api/stripe-webhook/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { stripe } from '@/lib/stripe'
import { adminDb } from '@/lib/firebaseAdmin'

export async function POST(req: NextRequest) {
  // 1. Read raw body (must be raw bytes for signature verification)
  const body = await req.text()
  const sig = req.headers.get('stripe-signature')!

  // 2. Verify the webhook signature
  let event
  try {
    event = stripe.webhooks.constructEvent(
      body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET!
    )
  } catch (err: any) {
    console.error('Webhook signature verification failed:', err.message)
    return NextResponse.json({ error: 'Invalid signature' }, { status: 400 })
  }

  // 3. Handle the event
  if (event.type === 'payment_intent.succeeded') {
    const intent = event.data.object
    const userId = intent.metadata.userId

    // Mark order as paid in Firestore
    await adminDb.collection('orders').add({
      userId,
      stripePaymentIntentId: intent.id,
      amount: intent.amount,
      currency: intent.currency,
      status: 'paid',
      paidAt: new Date(),
    })
    
    console.log(`Payment succeeded for user ${userId}`)
  }

  return NextResponse.json({ received: true })
}

// IMPORTANT: disable body parsing — Stripe requires raw body for signature verification
export const config = {
  api: { bodyParser: false }
}
```

> ⚠️ In Next.js App Router, `req.text()` already gives you the raw body — no special config needed. The `config.bodyParser: false` is only needed for Pages Router.

---

## Stripe Dashboard Configuration

### Payment Methods

Path: **Stripe Dashboard → Settings → Payment methods**

Enable the payment methods you want. With `automatic_payment_methods: { enabled: true }`, Stripe automatically shows all enabled methods in the Payment Element.

To disable a method (e.g., Alipay): just toggle it off in the Dashboard — no code change needed.

### Webhook Configuration

Path: **Stripe Dashboard → Developers → Webhooks → Add endpoint**

| Field | Value |
|-------|-------|
| Endpoint URL | `https://your-domain.com/api/stripe-webhook` |
| Listen to | Select specific events |
| Events to select | `payment_intent.succeeded` (+ any others you handle) |

After creating, copy the **Signing secret** (`whsec_...`) → set as `STRIPE_WEBHOOK_SECRET` in your environment.

> 📌 For local testing, use **Stripe CLI**:
> ```bash
> brew install stripe/stripe-cli/stripe
> stripe login
> stripe listen --forward-to localhost:3000/api/stripe-webhook
> ```
> This gives you a temporary `whsec_...` for local development.

---

## Promotion Codes

### ⚠️ Promotion Code ≠ Coupon ID

This is a real gotcha from production:

| Concept | What It Is | Who Uses It |
|---------|-----------|-------------|
| **Coupon** | Internal discount rule (e.g. "20% off") | Backend only — has an internal ID like `AbCdEf12` |
| **Promotion Code** | Customer-facing code (e.g. `SAVE20`) | Customers type this in your UI |

**Always create a Promotion Code, not use the Coupon ID directly.**

Path: **Stripe Dashboard → Billing → Coupons**
1. Create a Coupon (set percentage or fixed discount)
2. Open the Coupon → scroll to bottom → **Create promotion code**
3. Set the code string (e.g. `SAVE20`)

### Validate a Promotion Code in Code

```typescript
const codes = await stripe.promotionCodes.list({
  code: 'SAVE20',    // the customer-entered code
  active: true,
})

if (codes.data.length === 0) {
  // Invalid or expired code
}

const promoCode = codes.data[0]
const coupon = promoCode.coupon

if (coupon.percent_off) {
  newAmount = Math.round(originalAmount * (1 - coupon.percent_off / 100))
} else if (coupon.amount_off) {
  newAmount = originalAmount - coupon.amount_off
}
```

---

## Cloud Run Environment Variable Checklist

When deploying to GCP Cloud Run, these must be set as runtime variables (not build args):

| Variable | Example Value | Notes |
|----------|--------------|-------|
| `STRIPE_SECRET_KEY` | `sk_live_...` | Server-side only |
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Copy from Stripe Dashboard after creating endpoint |

> From the Huggle project: `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` is a build-time variable — bake it into the Docker image as a `--build-arg`, not a Cloud Run runtime var.

See [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]] for full environment variable setup.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Payment 400: Missing return_url` | `confirmPayment` missing `return_url` | Always include `return_url` in `confirmPayment` |
| `400: automatic_payment_methods not set` | Alipay/WeChat need `automatic_payment_methods: { enabled: true }` | Add to PaymentIntent creation |
| Webhook `400: No signatures found` | Using `req.json()` instead of `req.text()` | Use raw body: `await req.text()` |
| Promotion code "invalid" | Passing Coupon ID instead of Promotion Code | Create a Promotion Code in Dashboard |
| `sk_live` in dev environment | Wrong key in `.env.local` | Use `sk_test_` for local dev |
| Client secret `undefined` | Server failed silently | Add proper error handling + logging in the API route |

---

## Payment Flow Summary

```
User clicks "Pay"
    │
    ▼
Client → POST /api/create-payment (with Firebase auth token)
    │
    ▼
Server: verify token → create PaymentIntent → return clientSecret
    │
    ▼
Client: stripe.confirmPayment(elements, { return_url })
    │
    ├── Card: resolves immediately on success
    └── Alipay/WeChat: redirects user → returns to return_url
    │
    ▼
Stripe → POST /api/stripe-webhook (payment_intent.succeeded)
    │
    ▼
Server: verify signature → fulfill order in Firestore
```

---

## 🔗 Related Notes

- [[07-Fullstack-Development/03-Firebase/Firestore Database]]
- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[Huggle Project Deploy]]
- [[07-Fullstack-Development/00-INDEX]]
