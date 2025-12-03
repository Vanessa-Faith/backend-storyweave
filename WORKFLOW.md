# StoryWeave Backend - 4-Day Workflow Plan
## Team: 3 Members | Duration: 4 Days | Start: Backend First

---

## 📋 Team Member Assignments

### **Member 1 (Backend Lead): Database & Authentication**
- Database schema design & models
- Authentication system (JWT + Firebase)
- User management endpoints

### **Member 2 (Backend Dev): Story Management**
- Story CRUD operations
- Story API endpoints
- Story visibility/permissions

### **Member 3 (Backend Dev): Node & Branch System**
- Node/paragraph creation
- Branch management
- Story tree structure

---

## 📅 Day-by-Day Breakdown

### **DAY 1: Setup & Database Foundation**

#### Morning Session (3-4 hours)
**ALL MEMBERS:**
- [ ] Clone repository and setup Python environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create `.env` file from `.env.example`
- [ ] Review project structure together

**Member 1 (Lead):**
- [ ] Create database diagram on dbdiagram.io
  - Tables: users, stories, nodes
  - Define relationships (1-to-many, self-referential for nodes)
  - Export SQL and share with team
- [ ] Verify database models in `app/models.py` match diagram
- [ ] Test database connection: run `uvicorn app.main:app --reload`

**Member 2:**
- [ ] Review `app/schemas.py` (Pydantic models)
- [ ] Add any missing validation rules
- [ ] Test story schemas with sample data

**Member 3:**
- [ ] Review `app/models.py` Node model
- [ ] Understand parent-child relationship for branching
- [ ] Draft node tree structure logic

#### Afternoon Session (3-4 hours)
**Member 1:**
- [ ] Implement JWT token generation in `app/utils/auth.py`
- [ ] Test token creation and verification
- [ ] Set up Firebase Admin SDK configuration
- [ ] Document authentication flow

**Member 2:**
- [ ] Start implementing story CRUD in `app/routes/stories.py`
- [ ] Implement POST `/api/stories` (create story)
- [ ] Implement GET `/api/stories` (list stories)

**Member 3:**
- [ ] Start implementing node routes in `app/routes/nodes.py`
- [ ] Implement POST `/api/nodes` (create node)
- [ ] Test parent-child node relationships

**End of Day 1 Check-in:**
- Database is running ✅
- Models are finalized ✅
- Basic endpoints respond ✅

---

### **DAY 2: Core API Development**

#### Morning Session (3-4 hours)
**Member 1:**
- [ ] Complete `/api/auth/register` endpoint
- [ ] Complete `/api/auth/login` endpoint
- [ ] Implement `get_current_user` dependency
- [ ] Test authentication flow end-to-end
- [ ] Document auth headers needed for protected routes

**Member 2:**
- [ ] Complete GET `/api/stories/{story_id}` (get single story)
- [ ] Complete PUT `/api/stories/{story_id}` (update story)
- [ ] Complete DELETE `/api/stories/{story_id}` (delete story)
- [ ] Add GET `/api/stories/my-stories` (user's own stories)
- [ ] Test all story endpoints with Postman/Thunder Client

**Member 3:**
- [ ] Complete GET `/api/nodes/story/{story_id}` (get all nodes)
- [ ] Implement GET `/api/nodes/{node_id}` (get single node)
- [ ] Implement DELETE `/api/nodes/{node_id}` (delete node)
- [ ] Test node creation with different parents

#### Afternoon Session (3-4 hours)
**Member 1:**
- [ ] Add authorization checks to all protected routes
- [ ] Test unauthorized access scenarios
- [ ] Help Member 2 & 3 integrate auth into their endpoints

**Member 2:**
- [ ] Add pagination to story list endpoint
- [ ] Implement story privacy (public/private stories)
- [ ] Add story search/filter functionality (bonus)
- [ ] Write API documentation for story endpoints

**Member 3:**
- [ ] **CRITICAL:** Implement GET `/api/nodes/story/{story_id}/tree`
- [ ] Build tree structure from flat node list
- [ ] Return nested JSON representing story branches
- [ ] Test with multiple branching paths
- [ ] Document tree structure format

**End of Day 2 Check-in:**
- All CRUD endpoints working ✅
- Authentication protecting routes ✅
- Story tree structure functional ✅

---

### **DAY 3: Integration & Testing**

#### Morning Session (3-4 hours)
**ALL MEMBERS:**
- [ ] Team testing session - test each other's endpoints
- [ ] Use FastAPI's `/docs` (Swagger UI) to test all endpoints
- [ ] Create test scenarios for complex branching stories

**Member 1:**
- [ ] Fix any authentication bugs found during testing
- [ ] Add error handling for expired tokens
- [ ] Implement token refresh (if time permits)
- [ ] Update CORS settings for frontend domain

**Member 2:**
- [ ] Fix any story endpoint bugs
- [ ] Add proper error messages
- [ ] Ensure story updates trigger `updated_at` timestamp
- [ ] Test story deletion cascades to nodes

**Member 3:**
- [ ] Fix any node/branch bugs
- [ ] Optimize tree structure query performance
- [ ] Add validation for circular references in branches
- [ ] Test deep branching (5+ levels)

#### Afternoon Session (3-4 hours)
**Member 1:**
- [ ] Prepare deployment configuration
- [ ] Create deployment checklist
- [ ] Set up environment variables for production
- [ ] Test database migrations

**Member 2:**
- [ ] Write API documentation (README section)
- [ ] Create example API requests/responses
- [ ] Document error codes and messages

**Member 3:**
- [ ] Create sample data script for testing
- [ ] Populate database with example stories
- [ ] Document tree navigation logic for frontend team

**ALL MEMBERS:**
- [ ] Code review session
- [ ] Ensure consistent code style
- [ ] Add comments to complex logic
- [ ] Update TODO list for remaining items

**End of Day 3 Check-in:**
- All endpoints tested thoroughly ✅
- Documentation complete ✅
- Ready for frontend integration ✅

---

### **DAY 4: Deployment & Polish**

#### Morning Session (3-4 hours)
**Member 1:**
- [ ] Deploy backend to Render/Railway/Heroku
- [ ] Configure production database (PostgreSQL recommended)
- [ ] Set up environment variables on hosting platform
- [ ] Test deployed API endpoints

**Member 2:**
- [ ] Monitor deployment with Member 1
- [ ] Update CORS to allow frontend domain
- [ ] Test API from frontend deployment URL
- [ ] Create API status dashboard/health check

**Member 3:**
- [ ] Create comprehensive API testing collection (Postman/Insomnia)
- [ ] Test all endpoints on deployed backend
- [ ] Document base URL for frontend team
- [ ] Create quick start guide for frontend integration

#### Afternoon Session (2-3 hours)
**ALL MEMBERS:**
- [ ] Final testing of deployed API
- [ ] Share API documentation with frontend team
- [ ] Handoff meeting: explain endpoints, auth flow, tree structure
- [ ] Create example requests for frontend team

**Buffer Time:**
- [ ] Fix any last-minute deployment issues
- [ ] Add rate limiting (if time permits)
- [ ] Add request logging (if time permits)
- [ ] Performance optimization

**End of Day 4:**
- ✅ Backend fully deployed
- ✅ API documentation complete
- ✅ Frontend team ready to integrate

---

## 🛠️ Setup Instructions for Each Member

### Initial Setup (Everyone)
```bash
# 1. Clone the repository
git clone <repository-url>
cd backend-storyweave

# 2. Create Python virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp .env.example .env

# 6. Edit .env file with your settings
# Generate SECRET_KEY:
python -c "import secrets; print(secrets.token_urlsafe(32))"

# 7. Run the development server
uvicorn app.main:app --reload

# 8. Open browser to http://localhost:8000/docs
# You should see FastAPI's interactive documentation
```

### Testing Your Endpoints
```bash
# Option 1: Use FastAPI's built-in docs
# Navigate to http://localhost:8000/docs

# Option 2: Use curl
curl http://localhost:8000/health

# Option 3: Install Thunder Client extension in VS Code
# Or use Postman
```

---

## 📊 Database Schema (dbdiagram.io)

```sql
Table users {
  id integer [primary key]
  firebase_uid varchar [unique, not null]
  email varchar [unique, not null]
  username varchar [unique, not null]
  display_name varchar
  created_at timestamp [default: `now()`]
}

Table stories {
  id integer [primary key]
  title varchar [not null]
  description text
  author_id integer [not null]
  is_public boolean [default: true]
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table nodes {
  id integer [primary key]
  story_id integer [not null]
  parent_node_id integer [null]
  author_id integer [not null]
  content text [not null]
  order integer [default: 0]
  created_at timestamp [default: `now()`]
}

Ref: stories.author_id > users.id
Ref: nodes.story_id > stories.id
Ref: nodes.parent_node_id > nodes.id [note: "Self-referential for branching"]
Ref: nodes.author_id > users.id
```

**Copy this code to dbdiagram.io to visualize the schema!**

---

## 🔑 API Endpoints Overview

### Authentication (`/api/auth`)
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token
- `GET /api/auth/me` - Get current user info

### Stories (`/api/stories`)
- `POST /api/stories` - Create story 🔒
- `GET /api/stories` - List all public stories
- `GET /api/stories/my-stories` - Get user's stories 🔒
- `GET /api/stories/{id}` - Get specific story
- `PUT /api/stories/{id}` - Update story 🔒
- `DELETE /api/stories/{id}` - Delete story 🔒

### Nodes & Branches (`/api/nodes`)
- `POST /api/nodes` - Create node/branch 🔒
- `GET /api/nodes/story/{story_id}` - Get all nodes for story
- `GET /api/nodes/story/{story_id}/tree` - **Get story tree structure**
- `GET /api/nodes/{id}` - Get specific node
- `DELETE /api/nodes/{id}` - Delete node 🔒

🔒 = Requires authentication (Bearer token)

---

## 🚨 Common Issues & Solutions

### Issue: Import errors
**Solution:** Make sure virtual environment is activated and dependencies are installed

### Issue: Database not found
**Solution:** The SQLite database is created automatically on first run. Check that `storyweave.db` exists.

### Issue: CORS errors when frontend tries to connect
**Solution:** Add frontend URL to `ALLOWED_ORIGINS` in `.env` file

### Issue: 401 Unauthorized on protected routes
**Solution:** Include `Authorization: Bearer <token>` header in requests

### Issue: Can't access /docs
**Solution:** Make sure server is running on the correct port: `uvicorn app.main:app --reload --port 8000`

---

## 📞 Communication Protocol

### Daily Standup (15 min)
- What I did yesterday
- What I'm doing today
- Any blockers

### When Stuck (Don't wait > 30 min)
1. Check documentation
2. Ask in team chat
3. Schedule quick pair programming session

### Code Review
- Push code regularly
- Request review before merging to main
- Review each other's PRs within 2 hours

---

## ✅ Definition of Done

### Each Endpoint Must Have:
- [ ] Proper error handling
- [ ] Input validation
- [ ] Authentication (where needed)
- [ ] Tested in /docs
- [ ] Documented in README

### Backend Complete When:
- [ ] All endpoints respond correctly
- [ ] Authentication works end-to-end
- [ ] Tree structure returns properly formatted JSON
- [ ] Deployed and accessible via URL
- [ ] Documentation shared with frontend team

---

## 🎯 Success Metrics

By end of Day 4, you should have:
1. ✅ Deployed backend API with public URL
2. ✅ 15+ working endpoints
3. ✅ Full authentication system
4. ✅ Story branching/tree system functional
5. ✅ Complete API documentation
6. ✅ Frontend team ready to integrate

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [JWT.io](https://jwt.io/) - Debug JWT tokens
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [dbdiagram.io](https://dbdiagram.io/) - Database design
- [Render Deployment](https://render.com/) - Free backend hosting

---

**Remember: Communication is key! Update your team daily on progress.**

**Good luck! 🚀**
