# StoryWeave Backend API

**Collaborative Story Creation Platform - FastAPI Backend**

## 🚀 Project Overview

StoryWeave is a web-based collaborative storytelling platform that enables writers to create stories, contribute paragraphs, and develop branching narrative paths forming a visual "story tree."

This repository contains the **backend API** built with:
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **JWT Authentication** - Secure token-based auth
- **Firebase Integration** - Social authentication support
- **SQLite/PostgreSQL** - Database storage

---

## 📁 Project Structure

```
backend-storyweave/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── routes/              # API endpoints
│   │   ├── auth.py          # Authentication routes
│   │   ├── stories.py       # Story CRUD routes
│   │   └── nodes.py         # Node/branch routes
│   └── utils/
│       └── auth.py          # Auth utilities
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore
├── WORKFLOW.md             # 4-Day development plan
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+
- pip
- Virtual environment tool

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd backend-storyweave
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your configuration:
```env
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///./storyweave.db
FIREBASE_PROJECT_ID=your-firebase-project-id
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

Generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

5. **Run the development server**
```bash
uvicorn app.main:app --reload
```

6. **Access the API**
- API Root: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

---

## 📊 Database Schema

### Tables

**users**
- `id` - Primary key
- `firebase_uid` - Firebase user ID (unique)
- `email` - User email (unique)
- `username` - Username (unique)
- `display_name` - Display name
- `created_at` - Registration timestamp

**stories**
- `id` - Primary key
- `title` - Story title
- `description` - Story description
- `author_id` - Foreign key to users
- `is_public` - Public/private flag
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

**nodes**
- `id` - Primary key
- `story_id` - Foreign key to stories
- `parent_node_id` - Self-referential (for branching)
- `author_id` - Foreign key to users
- `content` - Paragraph content
- `order` - Display order
- `created_at` - Creation timestamp

### Relationships
- User → Stories (1:many)
- User → Nodes (1:many)
- Story → Nodes (1:many)
- Node → Children Nodes (1:many, self-referential)

**View the visual diagram:** Copy the schema from `WORKFLOW.md` to [dbdiagram.io](https://dbdiagram.io)

---

## 🔌 API Endpoints

### Health Check
- `GET /` - API welcome message
- `GET /health` - Health check

### Authentication (`/api/auth`)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/login` | Login user | No |
| GET | `/api/auth/me` | Get current user | Yes |

### Stories (`/api/stories`)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/stories` | Create new story | Yes |
| GET | `/api/stories` | List public stories | No |
| GET | `/api/stories/my-stories` | Get user's stories | Yes |
| GET | `/api/stories/{id}` | Get specific story | No |
| PUT | `/api/stories/{id}` | Update story | Yes |
| DELETE | `/api/stories/{id}` | Delete story | Yes |

### Nodes & Branches (`/api/nodes`)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/nodes` | Create node/branch | Yes |
| GET | `/api/nodes/story/{story_id}` | Get all nodes | No |
| GET | `/api/nodes/story/{story_id}/tree` | Get story tree | No |
| GET | `/api/nodes/{id}` | Get specific node | No |
| DELETE | `/api/nodes/{id}` | Delete node | Yes |

---

## 🔐 Authentication Flow

### 1. Register User (Frontend Firebase → Backend)
```bash
POST /api/auth/register
Content-Type: application/json

{
  "firebase_uid": "firebase-user-id",
  "email": "user@example.com",
  "username": "writer123",
  "display_name": "John Writer"
}
```

### 2. Login (Get JWT Token)
```bash
POST /api/auth/login?firebase_uid=firebase-user-id
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Use Token in Requests
```bash
GET /api/stories/my-stories
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 🌳 Story Tree Structure

The `/api/nodes/story/{story_id}/tree` endpoint returns a nested structure:

```json
{
  "story_id": 1,
  "story_title": "The Adventure Begins",
  "root_nodes": [
    {
      "id": 1,
      "content": "Once upon a time...",
      "author_id": 1,
      "parent_node_id": null,
      "order": 0,
      "created_at": "2025-12-02T10:00:00",
      "children": [
        {
          "id": 2,
          "content": "The hero went left...",
          "children": []
        },
        {
          "id": 3,
          "content": "The hero went right...",
          "children": []
        }
      ]
    }
  ]
}
```

---

## 🧪 Testing

### Using FastAPI Docs
1. Navigate to http://localhost:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Fill in parameters
5. Click "Execute"

### Using curl
```bash
# Health check
curl http://localhost:8000/health

# Register user
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "firebase_uid": "test123",
    "email": "test@example.com",
    "username": "testuser",
    "display_name": "Test User"
  }'

# Create story (with auth)
curl -X POST http://localhost:8000/api/stories \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "title": "My First Story",
    "description": "An amazing collaborative story",
    "is_public": true
  }'
```

---

## 🚀 Deployment

### Recommended Platforms
- **Render** (Free tier available)
- **Railway** (Free tier available)
- **Heroku** (Paid)
- **Fly.io** (Free tier available)

### Deployment Steps (Render Example)

1. **Prepare for deployment**
```bash
# Create requirements.txt if not exists
pip freeze > requirements.txt
```

2. **Create `render.yaml` (optional)**
```yaml
services:
  - type: web
    name: storyweave-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        sync: false
      - key: SECRET_KEY
        generateValue: true
      - key: PYTHON_VERSION
        value: 3.11.0
```

3. **Connect to Render**
   - Push code to GitHub
   - Create new Web Service on Render
   - Connect GitHub repository
   - Add environment variables
   - Deploy

4. **Set Environment Variables**
   - `SECRET_KEY` - Your secret key
   - `DATABASE_URL` - PostgreSQL URL (provided by Render)
   - `ALLOWED_ORIGINS` - Your frontend URL

---

## 📝 Development Workflow

See `WORKFLOW.md` for the complete 4-day development plan with:
- Team member assignments
- Day-by-day tasks
- Setup instructions
- Testing guidelines
- Deployment checklist

---

## 🤝 Team Collaboration

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/story-endpoints

# Make changes and commit
git add .
git commit -m "Add story CRUD endpoints"

# Push to remote
git push origin feature/story-endpoints

# Create Pull Request on GitHub
```

### Code Review Checklist
- [ ] Code follows PEP 8 style guidelines
- [ ] All endpoints tested in /docs
- [ ] Error handling implemented
- [ ] Authentication added where needed
- [ ] Comments added for complex logic

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Delete and recreate database
rm storyweave.db
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### CORS Errors
Add frontend URL to `.env`:
```env
ALLOWED_ORIGINS=http://localhost:3000,https://your-frontend.com
```

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JWT.io](https://jwt.io/) - Debug tokens
- [Firebase Auth](https://firebase.google.com/docs/auth)

---

## 📄 License

This project is part of a learning exercise for Phase 3 final project.

---

## 👥 Contributors

- Member 1: Database & Authentication
- Member 2: Story Management
- Member 3: Node & Branch System

---

**Built with ❤️ for collaborative storytelling**
