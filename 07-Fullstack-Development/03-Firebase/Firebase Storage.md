---
title: "Firebase Storage"
topic: fullstack
status: published
created: 2026-04-13
tags: [firebase, storage, file-upload, nextjs, cloud-storage]
---

# 📦 Firebase Storage

> Firebase Storage is a cloud file storage service built on top of Google Cloud Storage. Use it to store user-uploaded images, PDFs, videos, and other files — with built-in security rules tied to Firebase Auth.

---

## When to Use Firebase Storage vs Alternatives

| Use Case | Best Choice |
|----------|-------------|
| User profile photos, document uploads | Firebase Storage ✅ |
| Large video files (> 1GB) | Google Cloud Storage directly or Cloudflare R2 |
| Static assets (CSS, JS, public images) | CDN / Vercel / public folder |
| AI-generated files to download | Firebase Storage ✅ |
| Temporary files (< 24h) | Signed URL + scheduled deletion |

---

## Setup

### 1. Enable Storage in Firebase Console

1. Firebase Console → **Storage** → **Get started**
2. Choose **Production mode** (you'll write rules)
3. Choose a bucket location (same region as Firestore for lower latency)

You'll get a default bucket: `your-project.appspot.com`

### 2. Install SDK

Already included if you installed `firebase`:
```bash
npm install firebase  # includes storage
```

Client init is already in `src/lib/firebase.ts` — `storage` is exported from there.

---

## Basic File Operations

### Upload a File

```typescript
import { ref, uploadBytes, getDownloadURL } from 'firebase/storage'
import { storage } from '@/lib/firebase'

export async function uploadFile(
  file: File,
  path: string   // e.g. "users/uid_abc123/profile.jpg"
): Promise<string> {
  const storageRef = ref(storage, path)
  const snapshot = await uploadBytes(storageRef, file)
  const downloadURL = await getDownloadURL(snapshot.ref)
  return downloadURL  // permanent public URL (if rules allow)
}
```

### Upload with Metadata

```typescript
import { ref, uploadBytes } from 'firebase/storage'
import { storage } from '@/lib/firebase'

const metadata = {
  contentType: file.type,          // 'image/jpeg', 'application/pdf', etc.
  customMetadata: {
    uploadedBy: user.uid,
    originalName: file.name,
  }
}

await uploadBytes(storageRef, file, metadata)
```

### Upload with Progress (uploadBytesResumable)

```typescript
import { ref, uploadBytesResumable, getDownloadURL } from 'firebase/storage'
import { storage } from '@/lib/firebase'

export function uploadWithProgress(
  file: File,
  path: string,
  onProgress: (percent: number) => void
): Promise<string> {
  return new Promise((resolve, reject) => {
    const storageRef = ref(storage, path)
    const task = uploadBytesResumable(storageRef, file)

    task.on(
      'state_changed',
      (snapshot) => {
        const percent = (snapshot.bytesTransferred / snapshot.totalBytes) * 100
        onProgress(Math.round(percent))
      },
      (error) => reject(error),
      async () => {
        const url = await getDownloadURL(task.snapshot.ref)
        resolve(url)
      }
    )
  })
}
```

### Get Download URL

```typescript
import { ref, getDownloadURL } from 'firebase/storage'
import { storage } from '@/lib/firebase'

const url = await getDownloadURL(ref(storage, 'users/uid_abc123/profile.jpg'))
```

### Delete a File

```typescript
import { ref, deleteObject } from 'firebase/storage'
import { storage } from '@/lib/firebase'

await deleteObject(ref(storage, 'users/uid_abc123/old-photo.jpg'))
```

### List Files in a Folder

```typescript
import { ref, listAll } from 'firebase/storage'
import { storage } from '@/lib/firebase'

const folderRef = ref(storage, `users/${user.uid}/uploads`)
const result = await listAll(folderRef)

// result.items = array of file references
// result.prefixes = array of subfolder references
const urls = await Promise.all(result.items.map(getDownloadURL))
```

---

## React Hook: File Upload with Progress

```typescript
'use client'

import { useState } from 'react'
import { ref, uploadBytesResumable, getDownloadURL } from 'firebase/storage'
import { storage } from '@/lib/firebase'
import { useAuth } from '@/components/AuthProvider'

export function useFileUpload() {
  const { user } = useAuth()
  const [progress, setProgress] = useState(0)
  const [uploading, setUploading] = useState(false)
  const [url, setUrl] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const upload = (file: File, folder = 'uploads') => {
    if (!user) { setError('Must be signed in'); return }

    setUploading(true)
    setError(null)
    
    const path = `${folder}/${user.uid}/${Date.now()}_${file.name}`
    const task = uploadBytesResumable(ref(storage, path), file)

    task.on(
      'state_changed',
      (snap) => setProgress(Math.round((snap.bytesTransferred / snap.totalBytes) * 100)),
      (err) => { setError(err.message); setUploading(false) },
      async () => {
        const downloadUrl = await getDownloadURL(task.snapshot.ref)
        setUrl(downloadUrl)
        setUploading(false)
        setProgress(100)
      }
    )
  }

  return { upload, uploading, progress, url, error }
}
```

```typescript
// Usage in a component
function ProfilePhotoUpload() {
  const { upload, uploading, progress, url } = useFileUpload()

  return (
    <div>
      <input
        type="file"
        accept="image/*"
        onChange={(e) => e.target.files?.[0] && upload(e.target.files[0], 'profile-photos')}
      />
      {uploading && <p>Uploading... {progress}%</p>}
      {url && <img src={url} alt="Uploaded" />}
    </div>
  )
}
```

---

## File Path Conventions

Use a consistent naming scheme to avoid collisions:

```
users/{uid}/profile/avatar.jpg         ← User profile photo (overwrite same path)
users/{uid}/uploads/{timestamp}_{name} ← User uploads (unique per file)
products/{productId}/images/main.jpg   ← Product images
exports/{uid}/{timestamp}_export.pdf   ← Generated files for download
temp/{uid}/{timestamp}_{name}          ← Temporary files (clean up via Cloud Functions)
```

---

## Security Rules

Path: **Firebase Console → Storage → Rules**

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {

    // Profile photos: user can read/write their own
    match /users/{userId}/profile/{allPaths=**} {
      allow read: if true;   // public profile photos
      allow write: if request.auth != null && request.auth.uid == userId;
    }

    // User uploads: only the owner can read/write
    match /users/{userId}/uploads/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Exports: only the owner can read; no direct write (server-side only)
    match /exports/{userId}/{allPaths=**} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if false;  // server writes via Admin SDK
    }
    
    // Deny everything else
    match /{allPaths=**} {
      allow read, write: if false;
    }
  }
}
```

### File Size & Type Validation in Rules

```javascript
match /users/{userId}/uploads/{fileName} {
  allow write: if request.auth.uid == userId
    && request.resource.size < 10 * 1024 * 1024  // max 10MB
    && request.resource.contentType.matches('image/.*');  // images only
}
```

---

## Generating Signed URLs (Server-Side, Time-Limited)

For private files that shouldn't be permanently public — generate a signed URL that expires:

```typescript
// src/app/api/get-file-url/route.ts
import { adminStorage } from '@/lib/firebaseAdmin'  // see note below

export async function POST(req: Request) {
  const { filePath } = await req.json()
  
  const [url] = await adminStorage
    .bucket('your-project.appspot.com')
    .file(filePath)
    .getSignedUrl({
      action: 'read',
      expires: Date.now() + 15 * 60 * 1000,  // 15 minutes
    })

  return Response.json({ url })
}
```

Add to `firebaseAdmin.ts`:
```typescript
import { getStorage } from 'firebase-admin/storage'
export const adminStorage = getStorage(adminApp)
```

---

## Connecting Storage URLs to Firestore

A common pattern: store the file path (not URL) in Firestore, generate the URL on demand.

```typescript
// After upload, save path to Firestore
const path = `users/${user.uid}/uploads/${Date.now()}_${file.name}`
await uploadBytes(ref(storage, path), file)

await updateDoc(doc(db, 'users', user.uid), {
  resumePath: path,   // store path, not URL
})

// Later, get the URL when needed
const path = userProfile.resumePath
const url = await getDownloadURL(ref(storage, path))
```

Why store path instead of URL? URLs can change (e.g., bucket migration), but paths stay stable. You can also delete and re-upload to the same path.

---

## Storage vs Firestore — What Goes Where?

| Data Type | Where to Store |
|-----------|---------------|
| User text, numbers, dates, IDs | Firestore |
| Files (images, PDFs, videos, audio) | Firebase Storage |
| File metadata (name, size, type, path) | Firestore (alongside or with doc) |
| Download URLs | Firestore (can cache here) or generate fresh each time |

---

## Common Gotchas

| Issue | Fix |
|-------|-----|
| "Permission denied" on upload | Check Storage security rules — is user authenticated? |
| URL returns 403 after rules change | Existing URLs don't change — rules affect new reads |
| File path collisions | Include timestamp or UUID in path: `${Date.now()}_${file.name}` |
| Large files time out | Use `uploadBytesResumable` — it handles network interruptions |
| CORS errors when fetching file | Firebase Storage handles CORS for web apps automatically |
| Can't delete from client | Requires `write` permission in rules (many apps restrict delete to server-side) |

---

## 🔗 Related Notes

- [[07-Fullstack-Development/03-Firebase/Firebase Auth - Google & Email]]
- [[07-Fullstack-Development/03-Firebase/Firestore Database]]
- [[07-Fullstack-Development/05-Deployment/GCP Cloud Run Setup]]
- [[07-Fullstack-Development/00-INDEX]]
