# StoryWeave Backend - Team Member Assignments

## 👥 Team Structure

### Member 1 (Backend Lead) 👑
**Focus:** Database & Authentication

**Responsibilities:**
- Design and implement database schema
- Set up JWT authentication system
- Manage Firebase integration
- Coordinate with other members
- Handle deployment

**Files to work on:**
- `app/models.py` - Database models
- `app/utils/auth.py` - Authentication utilities
- `app/routes/auth.py` - Auth endpoints
- `app/database.py` - Database configuration

**Key Endpoints:**
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

---

### Member 2 (Backend Developer) 📚
**Focus:** Story Management

**Responsibilities:**
- Implement story CRUD operations
- Handle story permissions (public/private)
- Add pagination and filtering
- Story-related validations

**Files to work on:**
- `app/routes/stories.py` - Story endpoints
- `app/schemas.py` - Story schemas (StoryCreate, Story, etc.)
- Story-related parts of `app/models.py`

**Key Endpoints:**
- `POST /api/stories` - Create story
- `GET /api/stories` - List stories
- `GET /api/stories/{id}` - Get story
- `PUT /api/stories/{id}` - Update story
- `DELETE /api/stories/{id}` - Delete story
- `GET /api/stories/my-stories` - User's stories

---

### Member 3 (Backend Developer) 🌳
**Focus:** Node & Branch System

**Responsibilities:**
- Implement node creation and linking
- Build story tree structure
- Handle branch navigation
- Ensure tree integrity

**Files to work on:**
- `app/routes/nodes.py` - Node endpoints
- `app/schemas.py` - Node schemas (NodeCreate, Node, etc.)
- Node-related parts of `app/models.py`

**Key Endpoints:**
- `POST /api/nodes` - Create node/branch
- `GET /api/nodes/story/{story_id}` - Get all nodes
- `GET /api/nodes/story/{story_id}/tree` - **Get tree structure** (IMPORTANT!)
- `GET /api/nodes/{id}` - Get single node
- `DELETE /api/nodes/{id}` - Delete node

---

## 📅 Task Distribution by Day

### Day 1: Foundation

| Member | Morning | Afternoon |
|--------|---------|-----------|
| **Member 1** | Setup + Database diagram | JWT auth implementation |
| **Member 2** | Setup + Review schemas | Start story CRUD (POST, GET list) |
| **Member 3** | Setup + Understand tree structure | Start node creation (POST) |

### Day 2: Core Features

| Member | Morning | Afternoon |
|--------|---------|-----------|
| **Member 1** | Complete auth endpoints | Add auth to protected routes |
| **Member 2** | Complete story CRUD | Add pagination + privacy |
| **Member 3** | Complete node endpoints | **Build tree structure endpoint** |

### Day 3: Integration & Testing

| Member | Morning | Afternoon |
|--------|---------|-----------|
| **Member 1** | Fix auth bugs + CORS | Prepare deployment |
| **Member 2** | Fix story bugs + docs | Write API examples |
| **Member 3** | Fix tree bugs + validation | Create sample data |

### Day 4: Deployment

| Member | Morning | Afternoon |
|--------|---------|-----------|
| **Member 1** | Deploy backend | Test deployed API |
| **Member 2** | Update CORS + monitoring | Frontend handoff |
| **Member 3** | Test tree on deployed API | Create integration guide |

---

## 🔄 How Members Work Together

### Member 1 → Member 2 & 3
- Provides authentication system
- Members 2 & 3 use `get_current_user` dependency
- Example:
```python
@router.post("/")
def create_story(
    story: StoryCreate,
    current_user: User = Depends(get_current_user)  # ← From Member 1
):
    # Member 2's code here
```

### Member 2 → Member 3
- Member 2 creates stories
- Member 3 creates nodes that belong to stories
- Member 3 validates story exists before creating nodes

### Member 3 → Member 2
- Member 3's tree structure helps visualize stories
- Member 2 might display node count in story list

---

## 🎯 Daily Standup Format

**Each member reports (5 min each):**

### Member 1 Example:
```
✅ Completed: JWT token generation
🔄 Working on: Firebase integration
🚧 Blocked by: Need Firebase project credentials
🤝 Helping: Will assist Member 2 with auth integration this afternoon
```

### Member 2 Example:
```
✅ Completed: Story creation and list endpoints
🔄 Working on: Story update and delete
🚧 Blocked by: None
🤝 Need help: Will need Member 1's auth system by EOD
```

### Member 3 Example:
```
✅ Completed: Basic node creation
🔄 Working on: Tree structure algorithm
🚧 Blocked by: Need clarification on max tree depth
🤝 Helping: Will share tree visualization with team
```

---

## 💬 Communication Guidelines

### When to Notify the Team

**Immediately notify if:**
- You're blocked for > 30 minutes
- You need to change shared files (like `models.py`)
- You discovered a bug in another member's code
- You'll be unavailable for > 1 hour

**Daily updates:**
- Morning: What you're working on today
- Evening: What you completed + tomorrow's plan

**Share when done:**
- Completed endpoints (so others can integrate)
- Database schema changes
- API contract changes

---

## 🔀 Git Workflow

### Branch Naming
- **Member 1**: `feature/auth-system`, `feature/jwt-tokens`
- **Member 2**: `feature/story-crud`, `feature/story-pagination`
- **Member 3**: `feature/node-creation`, `feature/tree-structure`

### Before Starting Work
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### Before Pushing
```bash
# Make sure your code works
uvicorn app.main:app --reload

# Test your endpoints in /docs

# Commit with clear message
git add .
git commit -m "feat: add story creation endpoint"
git push origin feature/your-feature-name
```

### Pull Request Template
```markdown
## What does this PR do?
Implements story creation and list endpoints

## Endpoints added:
- POST /api/stories
- GET /api/stories

## How to test:
1. Run server
2. Go to /docs
3. Test story creation
4. Verify story list

## Dependencies:
- Requires authentication system (Member 1)

## Screenshots/Examples:
[Paste example request/response]
```

---

## 🆘 Who to Ask for Help

### Authentication Issues
→ Ask **Member 1**
- JWT token problems
- Authorization errors
- Firebase integration

### Database/Model Issues
→ Ask **Member 1** or discuss as team
- Model relationships
- Database queries
- Schema changes

### Story Endpoints
→ Ask **Member 2**
- Story CRUD operations
- Story permissions
- Story validation

### Node/Tree Issues
→ Ask **Member 3**
- Branch creation
- Tree structure
- Node relationships

### General FastAPI Questions
→ Discuss as team or check docs

---

## ✅ Definition of Done for Each Member

### Member 1 Checklist
- [ ] Database diagram on dbdiagram.io
- [ ] All models defined and tested
- [ ] JWT token generation works
- [ ] Auth endpoints complete
- [ ] `get_current_user` dependency working
- [ ] Firebase config documented
- [ ] Backend deployed

### Member 2 Checklist
- [ ] All story CRUD endpoints work
- [ ] Pagination implemented
- [ ] Privacy (public/private) works
- [ ] User can only edit own stories
- [ ] API documentation written
- [ ] Example requests provided

### Member 3 Checklist
- [ ] Node creation works
- [ ] Parent-child linking works
- [ ] Tree structure endpoint returns correct JSON
- [ ] Can handle deep branches (5+ levels)
- [ ] Circular reference validation
- [ ] Sample story tree created

---

## 🎉 Team Success Metrics

By end of 4 days:
- ✅ 15+ working endpoints
- ✅ Full authentication flow
- ✅ Complete story CRUD
- ✅ Working tree structure
- ✅ Deployed and accessible
- ✅ Documented for frontend team

**Remember: You're a team. Help each other succeed! 🤝**
