# StoryWeave Backend - Quick Start Guide

## 🎯 For Team Leaders: First Steps

### 1. Initial Team Setup Meeting (30 min)

**Before the meeting, send everyone:**
- Link to this repository
- `WORKFLOW.md` document
- Their assigned role

**During the meeting:**
1. Review the project structure together
2. Assign roles clearly:
   - **Member 1**: Database & Authentication (Lead)
   - **Member 2**: Story Management
   - **Member 3**: Node & Branch System
3. Set up communication channels (Discord/Slack/WhatsApp)
4. Schedule daily standup time (15 min each day)
5. Agree on Git workflow (feature branches)

---

## 🚀 Setup for Each Team Member (Day 1 Morning)

### Step 1: Clone and Setup (15 min)
```bash
# 1. Clone
git clone <your-repo-url>
cd backend-storyweave

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env

# 5. Generate secret key and add to .env
python -c "import secrets; print(secrets.token_urlsafe(32))"
# Copy output and paste into .env as SECRET_KEY value

# 6. Test run
uvicorn app.main:app --reload

# 7. Open browser to http://localhost:8000/docs
# You should see the FastAPI documentation page
```

**✅ Success check:** If you see the Swagger UI, you're ready!

---

## 📋 Day 1 Tasks Breakdown

### Member 1 (Lead) - Morning Tasks
1. ✅ Complete team setup (done above)
2. Go to [dbdiagram.io](https://dbdiagram.io)
3. Copy the database schema from `WORKFLOW.md`
4. Paste and visualize the schema
5. Export as PNG and share with team
6. Verify `app/models.py` matches the diagram
7. Test database creation:
```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
ls -la  # You should see storyweave.db
```

### Member 2 - Morning Tasks
1. ✅ Complete setup (done above)
2. Read through `app/schemas.py`
3. Understand Pydantic models (StoryCreate, Story, etc.)
4. Open http://localhost:8000/docs
5. Try the health check endpoint
6. Familiarize yourself with FastAPI docs interface

### Member 3 - Morning Tasks
1. ✅ Complete setup (done above)
2. Read `app/models.py` - focus on Node model
3. Understand the `parent_node_id` field (this creates branches!)
4. Draw a simple tree diagram on paper:
   ```
   Root Node (id: 1, parent: null)
   ├── Branch A (id: 2, parent: 1)
   │   ├── Choice A1 (id: 4, parent: 2)
   │   └── Choice A2 (id: 5, parent: 2)
   └── Branch B (id: 3, parent: 1)
   ```

---

## 🎓 Understanding the Project Architecture

### How Authentication Works
1. User signs up with Firebase (frontend)
2. Frontend sends `firebase_uid` to `/api/auth/register`
3. Backend creates user record
4. User logs in via `/api/auth/login`
5. Backend returns JWT token
6. Frontend stores token
7. Frontend sends token in header for protected routes

### How Story Branching Works
1. User creates a story (POST `/api/stories`)
2. User adds first paragraph as a node (POST `/api/nodes`)
   - `parent_node_id` = null (it's the root)
3. User adds second paragraph
   - `parent_node_id` = 1 (continues from first)
4. User wants to create a branch
   - Adds another node with `parent_node_id` = 1
   - Now node 1 has TWO children!
5. Tree structure grows with each branch

### How the API is Organized
```
app/
├── main.py           → FastAPI app, includes all routers
├── config.py         → Reads .env variables
├── database.py       → Database connection & session
├── models.py         → Database tables (SQLAlchemy)
├── schemas.py        → Request/response models (Pydantic)
├── routes/           → API endpoints
│   ├── auth.py       → /api/auth/* endpoints
│   ├── stories.py    → /api/stories/* endpoints
│   └── nodes.py      → /api/nodes/* endpoints
└── utils/
    └── auth.py       → JWT token helpers
```

---

## 🔧 Development Tips

### Testing Your Endpoints

**Method 1: FastAPI Docs (Easiest)**
1. Go to http://localhost:8000/docs
2. Click endpoint you want to test
3. Click "Try it out"
4. Fill in request body/parameters
5. Click "Execute"
6. See response below

**Method 2: curl**
```bash
# Test register
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "firebase_uid": "test123",
    "email": "test@test.com",
    "username": "testuser",
    "display_name": "Test User"
  }'
```

**Method 3: Thunder Client (VS Code Extension)**
1. Install Thunder Client extension
2. Create new request
3. Set method and URL
4. Add body/headers
5. Send

### Common Git Commands
```bash
# Start new feature
git checkout -b feature/your-feature-name

# See what changed
git status

# Add changes
git add .

# Commit
git commit -m "Descriptive message"

# Push to GitHub
git push origin feature/your-feature-name

# Get latest changes from main
git checkout main
git pull origin main
git checkout feature/your-feature-name
git merge main
```

### Debugging Tips
```bash
# See server logs
# They appear in terminal where you ran uvicorn

# Test database queries in Python shell
python
>>> from app.database import SessionLocal
>>> from app.models import User
>>> db = SessionLocal()
>>> users = db.query(User).all()
>>> print(users)
```

---

## 📞 Communication Templates

### Daily Standup Format (Each person 5 min)
```
**What I did yesterday:**
- Completed auth registration endpoint
- Started working on login endpoint

**What I'm doing today:**
- Finish login endpoint
- Test authentication flow
- Help Member 2 integrate auth

**Blockers:**
- Need clarification on Firebase token verification
```

### When Asking for Help
```
**Problem:**
Getting 500 error when creating story

**What I tried:**
1. Checked database connection
2. Verified story model
3. Tested endpoint in /docs

**Error message:**
[paste error here]

**Code snippet:**
[paste relevant code]

**Can someone help?**
@Member1
```

---

## 🎯 Success Checklist for Day 1

By end of Day 1, everyone should have:
- [ ] Repository cloned and running
- [ ] Virtual environment set up
- [ ] Dependencies installed
- [ ] Can access /docs at http://localhost:8000/docs
- [ ] Database file created (storyweave.db)
- [ ] Understanding of their assigned component
- [ ] At least 1 endpoint in progress

---

## 🚨 Troubleshooting Common Issues

### Issue: "Module not found" errors
```bash
# Make sure venv is activated
source venv/bin/activate

# Reinstall
pip install -r requirements.txt
```

### Issue: "Port already in use"
```bash
# Kill process on port 8000
# Linux/Mac:
lsof -ti:8000 | xargs kill -9

# Windows:
netstat -ano | findstr :8000
taskkill /PID [PID_NUMBER] /F

# Or use different port
uvicorn app.main:app --reload --port 8001
```

### Issue: Database errors
```bash
# Delete and recreate
rm storyweave.db
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### Issue: Import errors in VS Code
1. Press Ctrl+Shift+P (Cmd+Shift+P on Mac)
2. Type "Python: Select Interpreter"
3. Choose the venv interpreter (should show ./venv/bin/python)

---

## 📚 Learning Resources

### FastAPI Basics
- [Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
- Watch: "FastAPI Tutorial" by Tech With Tim (YouTube)

### SQLAlchemy
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- Focus on: models, relationships, queries

### JWT Authentication
- [JWT.io](https://jwt.io/) - Understand JWT structure
- Paste your tokens here to decode and inspect

---

## 📅 Meeting Schedule Suggestion

**Daily Standup: 9:00 AM (15 min)**
- Quick status updates
- Blocker discussion
- Plan for the day

**End of Day Sync: 5:00 PM (30 min)**
- Demo what was built
- Code review if needed
- Plan next day

**Mid-day Check-in (Optional): 2:00 PM (10 min)**
- Quick Slack/Discord message
- "How's it going? Need help?"

---

## ✅ Ready to Start?

1. ✅ Complete setup steps above
2. ✅ Join team communication channel
3. ✅ Open `WORKFLOW.md` and find your Day 1 tasks
4. ✅ Start with the morning session tasks
5. ✅ Ask questions when stuck (don't wait > 30 min!)

**Remember: This is a team project. Communication is key!**

**Good luck! 🚀**
