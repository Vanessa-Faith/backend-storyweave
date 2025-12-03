from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.routes import auth, stories, nodes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StoryWeave API",
    description="Collaborative Story Creation Platform API",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(stories.router, prefix="/api/stories", tags=["Stories"])
app.include_router(nodes.router, prefix="/api/nodes", tags=["Nodes & Branches"])

@app.get("/")
def read_root():
    return {
        "message": "Welcome to StoryWeave API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
