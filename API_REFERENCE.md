# StoryWeave API - Complete Endpoint Reference

## 🌐 Base URL
- **Development**: `http://localhost:8000`
- **Production**: `https://your-app.render.com`

---

## 📍 All Endpoints at a Glance

### Health & Info
```
GET  /                    → Welcome message
GET  /health              → Health check status
GET  /docs                → Interactive API documentation (Swagger UI)
GET  /redoc               → Alternative API documentation
```

---

## 🔐 Authentication Endpoints (`/api/auth`)

### Register New User
```http
POST /api/auth/register
Content-Type: application/json

{
  "firebase_uid": "string",
  "email": "user@example.com",
  "username": "unique_username",
  "display_name": "Display Name"
}

Response: 201 Created
{
  "id": 1,
  "firebase_uid": "string",
  "email": "user@example.com",
  "username": "unique_username",
  "display_name": "Display Name",
  "created_at": "2025-12-02T10:00:00"
}
```

### Login User
```http
POST /api/auth/login?firebase_uid=string

Response: 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Get Current User Info
```http
GET /api/auth/me
Authorization: Bearer <token>

Response: 200 OK
{
  "id": 1,
  "firebase_uid": "string",
  "email": "user@example.com",
  "username": "username",
  "display_name": "Display Name",
  "created_at": "2025-12-02T10:00:00"
}
```

---

## 📚 Story Endpoints (`/api/stories`)

### Create New Story
```http
POST /api/stories
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "My Amazing Story",
  "description": "A collaborative adventure",
  "is_public": true
}

Response: 201 Created
{
  "id": 1,
  "title": "My Amazing Story",
  "description": "A collaborative adventure",
  "author_id": 1,
  "is_public": true,
  "created_at": "2025-12-02T10:00:00",
  "updated_at": null
}
```

### List All Public Stories
```http
GET /api/stories?skip=0&limit=20

Response: 200 OK
[
  {
    "id": 1,
    "title": "Story Title",
    "description": "Description",
    "author_id": 1,
    "is_public": true,
    "created_at": "2025-12-02T10:00:00",
    "updated_at": null,
    "author": {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "display_name": "Display Name",
      "firebase_uid": "string",
      "created_at": "2025-12-02T10:00:00"
    }
  }
]
```

### Get User's Own Stories
```http
GET /api/stories/my-stories
Authorization: Bearer <token>

Response: 200 OK
[
  {
    "id": 1,
    "title": "My Story",
    "description": "Description",
    "author_id": 1,
    "is_public": false,
    "created_at": "2025-12-02T10:00:00",
    "updated_at": null
  }
]
```

### Get Specific Story
```http
GET /api/stories/{story_id}

Response: 200 OK
{
  "id": 1,
  "title": "Story Title",
  "description": "Description",
  "author_id": 1,
  "is_public": true,
  "created_at": "2025-12-02T10:00:00",
  "updated_at": null,
  "author": {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "display_name": "Display Name",
    "firebase_uid": "string",
    "created_at": "2025-12-02T10:00:00"
  }
}
```

### Update Story
```http
PUT /api/stories/{story_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated description",
  "is_public": false
}

Response: 200 OK
{
  "id": 1,
  "title": "Updated Title",
  "description": "Updated description",
  "author_id": 1,
  "is_public": false,
  "created_at": "2025-12-02T10:00:00",
  "updated_at": "2025-12-02T11:00:00"
}
```

### Delete Story
```http
DELETE /api/stories/{story_id}
Authorization: Bearer <token>

Response: 204 No Content
```

---

## 🌳 Node & Branch Endpoints (`/api/nodes`)

### Create New Node (Paragraph/Branch)
```http
POST /api/nodes
Authorization: Bearer <token>
Content-Type: application/json

{
  "story_id": 1,
  "parent_node_id": null,  // null for root node, or ID of parent
  "content": "Once upon a time in a magical forest..."
}

Response: 201 Created
{
  "id": 1,
  "story_id": 1,
  "parent_node_id": null,
  "author_id": 1,
  "content": "Once upon a time in a magical forest...",
  "order": 0,
  "created_at": "2025-12-02T10:00:00"
}
```

### Get All Nodes for a Story
```http
GET /api/nodes/story/{story_id}

Response: 200 OK
[
  {
    "id": 1,
    "story_id": 1,
    "parent_node_id": null,
    "author_id": 1,
    "content": "First paragraph...",
    "order": 0,
    "created_at": "2025-12-02T10:00:00",
    "author": {
      "id": 1,
      "username": "username",
      "display_name": "Display Name",
      ...
    },
    "children": [...]
  }
]
```

### Get Story Tree Structure (IMPORTANT!)
```http
GET /api/nodes/story/{story_id}/tree

Response: 200 OK
{
  "story_id": 1,
  "story_title": "The Enchanted Forest",
  "root_nodes": [
    {
      "id": 1,
      "content": "You wake up in a mysterious forest...",
      "author_id": 1,
      "parent_node_id": null,
      "order": 0,
      "created_at": "2025-12-02T10:00:00",
      "children": [
        {
          "id": 2,
          "content": "You follow the main path...",
          "author_id": 2,
          "parent_node_id": 1,
          "order": 0,
          "created_at": "2025-12-02T10:15:00",
          "children": [
            {
              "id": 4,
              "content": "You accept the fox's offer...",
              "author_id": 1,
              "parent_node_id": 2,
              "order": 0,
              "created_at": "2025-12-02T10:30:00",
              "children": []
            },
            {
              "id": 5,
              "content": "You politely decline...",
              "author_id": 2,
              "parent_node_id": 2,
              "order": 1,
              "created_at": "2025-12-02T10:35:00",
              "children": []
            }
          ]
        },
        {
          "id": 3,
          "content": "You head toward the water...",
          "author_id": 3,
          "parent_node_id": 1,
          "order": 1,
          "created_at": "2025-12-02T10:20:00",
          "children": []
        }
      ]
    }
  ]
}
```

### Get Specific Node
```http
GET /api/nodes/{node_id}

Response: 200 OK
{
  "id": 1,
  "story_id": 1,
  "parent_node_id": null,
  "author_id": 1,
  "content": "Node content...",
  "order": 0,
  "created_at": "2025-12-02T10:00:00",
  "author": {...},
  "children": [...]
}
```

### Delete Node
```http
DELETE /api/nodes/{node_id}
Authorization: Bearer <token>

Response: 204 No Content
```

---

## 🔑 Authentication Flow

### For Frontend Integration:

```javascript
// 1. User signs up with Firebase (frontend)
const userCredential = await createUserWithEmailAndPassword(auth, email, password);
const firebaseUid = userCredential.user.uid;

// 2. Register user in your backend
const registerResponse = await fetch('http://localhost:8000/api/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    firebase_uid: firebaseUid,
    email: email,
    username: username,
    display_name: displayName
  })
});

// 3. Login to get JWT token
const loginResponse = await fetch(`http://localhost:8000/api/auth/login?firebase_uid=${firebaseUid}`, {
  method: 'POST'
});
const { access_token } = await loginResponse.json();

// 4. Store token (localStorage, secure cookie, etc.)
localStorage.setItem('token', access_token);

// 5. Use token in subsequent requests
const response = await fetch('http://localhost:8000/api/stories', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${access_token}`
  },
  body: JSON.stringify({
    title: 'My Story',
    description: 'A great story',
    is_public: true
  })
});
```

---

## 🌳 Tree Structure Explanation

### How Branching Works:

```
Root Node (id: 1, parent: null)
├── Branch A (id: 2, parent: 1)
│   ├── Choice A1 (id: 4, parent: 2)
│   └── Choice A2 (id: 5, parent: 2)
└── Branch B (id: 3, parent: 1)
    ├── Choice B1 (id: 6, parent: 3)
    └── Choice B2 (id: 7, parent: 3)
```

### Creating This Structure:

```javascript
// 1. Create root node
POST /api/nodes
{
  "story_id": 1,
  "parent_node_id": null,
  "content": "Root content"
}
// Returns: { "id": 1, ... }

// 2. Create first branch from root
POST /api/nodes
{
  "story_id": 1,
  "parent_node_id": 1,
  "content": "Branch A content"
}
// Returns: { "id": 2, ... }

// 3. Create second branch from root
POST /api/nodes
{
  "story_id": 1,
  "parent_node_id": 1,
  "content": "Branch B content"
}
// Returns: { "id": 3, ... }

// 4. Create sub-branch from Branch A
POST /api/nodes
{
  "story_id": 1,
  "parent_node_id": 2,
  "content": "Choice A1 content"
}
// Returns: { "id": 4, ... }

// And so on...
```

---

## 📝 Query Parameters

### Stories List
- `skip` (int, default: 0) - Number of records to skip (pagination)
- `limit` (int, default: 20) - Maximum records to return

Example:
```
GET /api/stories?skip=20&limit=10  # Get stories 21-30
```

---

## ⚠️ Error Responses

### 400 Bad Request
```json
{
  "detail": "User with this email already exists"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden
```json
{
  "detail": "Not authorized to update this story"
}
```

### 404 Not Found
```json
{
  "detail": "Story not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

---

## 🧪 Testing Examples

### Using curl:

```bash
# Register
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"firebase_uid":"test123","email":"test@test.com","username":"testuser","display_name":"Test User"}'

# Login
curl -X POST "http://localhost:8000/api/auth/login?firebase_uid=test123"

# Create story (replace TOKEN)
curl -X POST http://localhost:8000/api/stories \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"title":"Test Story","description":"A test","is_public":true}'

# Get tree structure
curl http://localhost:8000/api/nodes/story/1/tree
```

### Using JavaScript Fetch:

```javascript
// Create story
const createStory = async (token) => {
  const response = await fetch('http://localhost:8000/api/stories', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      title: 'My Story',
      description: 'Description',
      is_public: true
    })
  });
  return await response.json();
};

// Get tree
const getTree = async (storyId) => {
  const response = await fetch(`http://localhost:8000/api/nodes/story/${storyId}/tree`);
  return await response.json();
};
```

---

## 🎯 Quick Reference Card

**Need to...**
- **Register user**: `POST /api/auth/register`
- **Login**: `POST /api/auth/login?firebase_uid=X`
- **Create story**: `POST /api/stories` 🔒
- **List stories**: `GET /api/stories`
- **Add paragraph**: `POST /api/nodes` 🔒
- **Get tree**: `GET /api/nodes/story/{id}/tree`

🔒 = Requires `Authorization: Bearer <token>` header

---

**For more details, visit: http://localhost:8000/docs**
