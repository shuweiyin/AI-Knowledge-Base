---
title: "Firestore Database"
topic: fullstack
status: published
created: 2026-04-13
tags: [firebase, firestore, database, nosql, nextjs]
---

# 🗄️ Firestore Database

> Firestore is Firebase's NoSQL document database. Fast, real-time, and works seamlessly with Firebase Auth — but it thinks differently from SQL. Understanding its data model first saves hours of pain.

---

## The Data Model

Firestore is **not a table-based database**. It's organized as:

```
Collection (like a folder)
  └── Document (like a file — has an ID + fields)
        └── Subcollection (nested collection inside a document)
              └── Document
```

### Example Structure

```
users/                          ← Collection
  uid_abc123/                   ← Document (ID = Firebase user UID)
    name: "Alice"
    email: "alice@example.com"
    createdAt: Timestamp
    
    orders/                     ← Subcollection
      order_xyz/                ← Document
        amount: 2000
        status: "paid"
        createdAt: Timestamp

products/                       ← Collection
  prod_001/
    name: "Pro Plan"
    price: 2000
    currency: "usd"
```

### Key Mental Model Shifts from SQL

| SQL Concept | Firestore Equivalent |
|-------------|---------------------|
| Table | Collection |
| Row | Document |
| Column | Field |
| JOIN | Denormalization (duplicate data) or separate queries |
| Foreign key | Store document ID as a string field |
| Auto-increment ID | Firestore generates random IDs (or you choose the ID) |

> 📌 **Firestore is not great for complex queries** with multiple `WHERE` clauses and `ORDER BY` on different fields — those need composite indexes. Design your data around how you'll **read** it, not how it naturally relates.

---

## Setup

Already done if you followed [[07-Fullstack-Development/02-Local-Environment/Node.js & Next.js Setup]].

### Create Firestore Database

1. Firebase Console → **Firestore Database** → **Create database**
2. Choose **Production mode** (we'll write proper rules)
3. Choose a region (e.g. `us-central1` or `europe-west1` — pick close to your users)

---

## Basic CRUD Operations (Client SDK)

```typescript
import {
  doc, collection,
  getDoc, getDocs, setDoc, addDoc, updateDoc, deleteDoc,
  query, where, orderBy, limit,
  serverTimestamp,
  onSnapshot,
} from 'firebase/firestore'
import { db } from '@/lib/firebase'
```

### Create a Document

```typescript
// With auto-generated ID
const ref = await addDoc(collection(db, 'posts'), {
  title: 'Hello World',
  authorId: user.uid,
  createdAt: serverTimestamp(),
})
console.log('New post ID:', ref.id)

// With a specific ID (great for user profiles: use user.uid)
await setDoc(doc(db, 'users', user.uid), {
  email: user.email,
  createdAt: serverTimestamp(),
})
```

### Read a Single Document

```typescript
const snap = await getDoc(doc(db, 'users', user.uid))

if (snap.exists()) {
  const data = snap.data()
  console.log(data.email)
} else {
  console.log('User not found')
}
```

### Read a Collection (Query)

```typescript
// Get all posts by this user, newest first
const q = query(
  collection(db, 'posts'),
  where('authorId', '==', user.uid),
  orderBy('createdAt', 'desc'),
  limit(20)
)

const snapshot = await getDocs(q)
const posts = snapshot.docs.map(doc => ({
  id: doc.id,
  ...doc.data()
}))
```

### Update a Document

```typescript
// updateDoc only changes specified fields — does not overwrite the whole doc
await updateDoc(doc(db, 'users', user.uid), {
  displayName: 'New Name',
  updatedAt: serverTimestamp(),
})

// setDoc with merge: true also works
await setDoc(doc(db, 'users', user.uid), {
  displayName: 'New Name',
}, { merge: true })
```

### Delete a Document

```typescript
await deleteDoc(doc(db, 'posts', postId))
```

---

## Real-Time Listener

Subscribe to live updates — document re-renders whenever data changes:

```typescript
import { useEffect, useState } from 'react'
import { onSnapshot, doc } from 'firebase/firestore'
import { db } from '@/lib/firebase'

function useUserProfile(uid: string) {
  const [profile, setProfile] = useState<any>(null)

  useEffect(() => {
    const unsub = onSnapshot(doc(db, 'users', uid), (snap) => {
      if (snap.exists()) setProfile({ id: snap.id, ...snap.data() })
    })
    return unsub  // unsubscribe when component unmounts
  }, [uid])

  return profile
}
```

---

## Server-Side Firestore (Admin SDK)

Use in API routes where you need full access regardless of security rules:

```typescript
// src/app/api/admin-action/route.ts
import { adminDb } from '@/lib/firebaseAdmin'

export async function POST(req: Request) {
  // adminDb bypasses all security rules — use only server-side
  const snap = await adminDb.collection('users').doc(userId).get()
  const data = snap.data()
  
  await adminDb.collection('orders').add({
    userId,
    amount: 2000,
    status: 'pending',
    createdAt: new Date(),
  })
}
```

> ⚠️ **Admin SDK ignores security rules.** It has full read/write access. Only use it in server-side code (API routes, server actions) — never expose it client-side.

---

## Security Rules

By default in Production mode, **all reads and writes are denied**. You must write rules.

Path: **Firebase Console → Firestore Database → Rules**

### Basic Rules Template

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Users can only read/write their own document
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Orders: user can read own orders, only server can create
    match /orders/{orderId} {
      allow read: if request.auth != null && request.auth.uid == resource.data.userId;
      allow write: if false;  // only server-side Admin SDK can write
    }

    // Public read, no write
    match /products/{productId} {
      allow read: if true;
      allow write: if false;
    }
    
    // Catch-all: deny everything else
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

### Rule Helpers

```javascript
// Check if user is authenticated
request.auth != null

// Check if user owns the document (document field = user's UID)
request.auth.uid == resource.data.userId

// Check if user owns the document (document ID = user's UID)
request.auth.uid == userId

// Check incoming write data
request.resource.data.status == 'pending'
```

> 💡 **Test your rules** in the Firestore Rules Playground (in the console) before deploying. It's easy to accidentally leave a collection wide-open.

---

## TypeScript Typing for Firestore

Create types for your documents to avoid runtime errors:

```typescript
// src/types/index.ts
import { Timestamp } from 'firebase/firestore'

export interface UserProfile {
  uid: string
  email: string
  displayName: string
  photoURL: string
  createdAt: Timestamp
}

export interface Order {
  id?: string  // Firestore doc ID, optional when creating
  userId: string
  amount: number       // in cents (e.g. 2000 = $20.00)
  currency: string     // 'usd', 'gbp', etc.
  status: 'pending' | 'paid' | 'failed'
  stripePaymentIntentId?: string
  createdAt: Timestamp
}
```

```typescript
// Typed document read
import { UserProfile } from '@/types'

const snap = await getDoc(doc(db, 'users', uid))
const profile = snap.data() as UserProfile
```

---

## Indexes

Firestore requires a **composite index** for queries that filter on one field and sort on a different field.

```typescript
// This query needs a composite index:
query(
  collection(db, 'orders'),
  where('userId', '==', uid),   // filter on field A
  orderBy('createdAt', 'desc')  // sort on field B
)
```

When you run a query without the needed index, Firestore throws an error in the console **with a direct link to create the index**. Just click the link — it auto-fills the index config.

Path for manual index creation: **Firebase Console → Firestore → Indexes → Composite**

---

## Data Modeling Patterns

### Pattern 1: User-Owned Documents

Each user has a document in `users/` keyed by their UID. Sub-data lives in subcollections.

```
users/{uid}/
  profile fields...
  
  orders/{orderId}/
    order fields...
```

### Pattern 2: Flat Collections with userId Field

All orders in one top-level collection, each with a `userId` field. Easier to query across users (admin view), but requires index.

```
orders/{orderId}/
  userId: "abc123"
  amount: 2000
```

### Pattern 3: Denormalization (copy data to avoid joins)

```
// In an order document, copy the user's name at purchase time
orders/{orderId}/
  userId: "abc123"
  userName: "Alice Smith"   ← copied from user profile
  amount: 2000
```

This avoids needing to join `orders` with `users` every time you display an order. Firestore is schemaless, so duplication is normal and expected.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `setDoc` without `merge: true` on updates | It **overwrites** the entire document — use `updateDoc` for partial updates |
| Querying with multiple `where` + `orderBy` without composite index | Create the composite index (Firestore gives you the link) |
| Storing amounts as floats (e.g. `19.99`) | Store as **integers in cents** (`1999`) — no floating-point rounding issues |
| Not unsubscribing from `onSnapshot` | Memory leak — always `return unsub` in `useEffect` |
| Calling Firestore in every render | Memoize or use a custom hook |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]]
- [[07-Fullstack-Development/03-Firebase/Firebase Storage]]
- [[07-Fullstack-Development/04-Stripe-Payments/Stripe Configuration Guide]]
- [[07-Fullstack-Development/00-INDEX]]
