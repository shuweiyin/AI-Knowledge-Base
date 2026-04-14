---
title: "Firebase Auth — Google & Email/Password Login"
topic: fullstack
status: published
created: 2026-04-13
tags: [firebase, authentication, google-login, email-login, nextjs]
---

# 🔐 Firebase Auth — Google & Email/Password Login

> Firebase Authentication handles the hard parts of login: tokens, sessions, OAuth flows, password hashing. You just wire up the UI.

---

## Firebase Console Setup

### 1. Create a Firebase Project

1. Go to https://console.firebase.google.com
2. Click **Add project** → give it a name
3. Disable Google Analytics if not needed (simpler setup)
4. Click **Create project**

### 2. Register Your Web App

1. In your Firebase project → click the **`</>`** (Web) icon
2. Give it a nickname (e.g. `my-app-web`)
3. **Don't** enable Firebase Hosting (you're using Vercel or Cloud Run)
4. Copy the `firebaseConfig` object — paste into your `.env.local` as `NEXT_PUBLIC_*` vars

### 3. Enable Auth Providers

Path: **Firebase Console → Authentication → Sign-in method**

#### Enable Google:
1. Click **Google** → toggle **Enable**
2. Set a project support email
3. Click **Save**

#### Enable Email/Password:
1. Click **Email/Password** → toggle **Enable**
2. Leave "Email link (passwordless)" OFF for now
3. Click **Save**

### 4. Add Authorized Domains ⚠️ (Critical)

Path: **Firebase Console → Authentication → Settings → Authorized domains**

Add every domain your app will run on:

| Domain | When to Add |
|--------|-------------|
| `localhost` | Already there by default |
| `your-app.vercel.app` | When deploying to Vercel |
| `your-custom-domain.com` | When using a custom domain |
| `your-service-xyz.run.app` | When deploying to Cloud Run |
| `your-custom-domain.com` | Also add your mapped custom domain |

> 🔴 **If you skip this step**: Google login popup will open and immediately close without completing. No error message — just a popup that flashes. This is one of the most confusing Firebase gotchas.

---

## Client-Side Auth Code

### Auth Context — `src/components/AuthProvider.tsx`

Wrap your app in this to provide auth state everywhere:

```typescript
'use client'

import { createContext, useContext, useEffect, useState } from 'react'
import { onAuthStateChanged, User } from 'firebase/auth'
import { auth } from '@/lib/firebase'

interface AuthContextType {
  user: User | null
  loading: boolean
}

const AuthContext = createContext<AuthContextType>({ user: null, loading: true })

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user)
      setLoading(false)
    })
    return unsubscribe  // cleanup on unmount
  }, [])

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
```

Add to `src/app/layout.tsx`:
```typescript
import { AuthProvider } from '@/components/AuthProvider'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  )
}
```

---

### Google Sign-In

```typescript
import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth'
import { auth } from '@/lib/firebase'

export async function signInWithGoogle() {
  const provider = new GoogleAuthProvider()
  
  // Optional: force account picker even if already signed in
  provider.setCustomParameters({ prompt: 'select_account' })
  
  try {
    const result = await signInWithPopup(auth, provider)
    return result.user
  } catch (error: any) {
    // User closed the popup — not a real error
    if (error.code === 'auth/popup-closed-by-user') return null
    throw error
  }
}
```

> 💡 Use `signInWithRedirect` instead of `signInWithPopup` on mobile — popups are often blocked on iOS Safari.

---

### Email / Password Sign-In

```typescript
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  sendPasswordResetEmail,
} from 'firebase/auth'
import { auth } from '@/lib/firebase'

// Register new user
export async function registerWithEmail(email: string, password: string) {
  const result = await createUserWithEmailAndPassword(auth, email, password)
  return result.user
}

// Sign in existing user
export async function loginWithEmail(email: string, password: string) {
  const result = await signInWithEmailAndPassword(auth, email, password)
  return result.user
}

// Password reset
export async function resetPassword(email: string) {
  await sendPasswordResetEmail(auth, email)
}
```

### Sign Out

```typescript
import { signOut } from 'firebase/auth'
import { auth } from '@/lib/firebase'

export async function logout() {
  await signOut(auth)
}
```

---

## Server-Side Auth (Verifying Tokens in API Routes)

When a client makes a request to your Next.js API route, verify the Firebase ID token server-side before trusting it.

### Client: Send the Token

```typescript
// In your React component or fetch helper
async function callProtectedApi(data: any) {
  const user = auth.currentUser
  if (!user) throw new Error('Not authenticated')
  
  const token = await user.getIdToken()
  
  const res = await fetch('/api/protected-route', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  return res.json()
}
```

### Server: Verify the Token

```typescript
// src/app/api/protected-route/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { adminAuth } from '@/lib/firebaseAdmin'

export async function POST(req: NextRequest) {
  const authHeader = req.headers.get('Authorization')
  if (!authHeader?.startsWith('Bearer ')) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  }

  const token = authHeader.split('Bearer ')[1]
  
  try {
    const decodedToken = await adminAuth.verifyIdToken(token)
    const userId = decodedToken.uid
    
    // Now you know who the user is — proceed
    const body = await req.json()
    // ... do your logic
    
    return NextResponse.json({ success: true })
  } catch {
    return NextResponse.json({ error: 'Invalid token' }, { status: 401 })
  }
}
```

---

## Getting User Data

```typescript
import { useAuth } from '@/components/AuthProvider'

function ProfilePage() {
  const { user, loading } = useAuth()

  if (loading) return <div>Loading...</div>
  if (!user) return <div>Please sign in</div>

  return (
    <div>
      <img src={user.photoURL ?? '/default-avatar.png'} alt="avatar" />
      <p>{user.displayName}</p>
      <p>{user.email}</p>
      <p>UID: {user.uid}</p>  {/* Use this as the Firestore document ID */}
    </div>
  )
}
```

### Key User Fields

| Field | Type | Notes |
|-------|------|-------|
| `user.uid` | string | Unique user ID — use as Firestore doc key |
| `user.email` | string \| null | Always present for email auth; present for Google |
| `user.displayName` | string \| null | Set by Google; null for email/password by default |
| `user.photoURL` | string \| null | Google profile photo; null for email/password |
| `user.emailVerified` | boolean | False until user clicks verification link |

---

## Storing User Profiles in Firestore

Firebase Auth stores minimal data. For extra profile info, create a Firestore document when a user signs up:

```typescript
import { doc, setDoc, serverTimestamp } from 'firebase/firestore'
import { db } from '@/lib/firebase'
import { User } from 'firebase/auth'

export async function createUserProfile(user: User) {
  const ref = doc(db, 'users', user.uid)
  
  await setDoc(ref, {
    uid: user.uid,
    email: user.email,
    displayName: user.displayName ?? '',
    photoURL: user.photoURL ?? '',
    createdAt: serverTimestamp(),
  }, { merge: true })  // merge: true = won't overwrite on subsequent logins
}
```

Call this after every sign-in (Google or email) — `merge: true` makes it idempotent.

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| Popup flashes and closes immediately | Domain not in Firebase Authorized Domains | Add domain in Firebase Console → Auth → Settings |
| `auth/invalid-api-key` | Wrong Firebase config | Check `NEXT_PUBLIC_FIREBASE_API_KEY` |
| `auth/weak-password` | Password < 6 chars | Enforce minimum in your UI |
| `auth/email-already-in-use` | Duplicate registration | Show "sign in instead" option |
| `auth/user-not-found` | Login with unregistered email | Show "sign up instead" option |
| `auth/wrong-password` | Wrong password | Show "forgot password?" link |
| `auth/popup-blocked` | Browser blocking popup | Use `signInWithRedirect` as fallback |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/02-Local-Environment/Node.js & Next.js Setup]]
- [[07-Fullstack-Development/03-Firebase/Firestore Database]]
- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[07-Fullstack-Development/00-INDEX]]
