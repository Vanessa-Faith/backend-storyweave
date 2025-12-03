"""
Authentication routes - Member 1
TODO: Implement these endpoints:
1. POST /api/auth/register - Register new user
2. POST /api/auth/login - Login and get JWT token
3. GET /api/auth/me - Get current user info

Reference: WORKFLOW.md Day 1-2 tasks for Member 1
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

# TODO: Import necessary schemas
# from app.schemas import UserCreate, User, Token

# TODO: Import auth utilities
# from app.utils.auth import create_access_token, get_current_user

# TODO: Implement register endpoint
@router.post("/register")
def register_user():
    """
    Register a new user with Firebase UID
    This should be called after Firebase authentication on the frontend
    
    Steps:
    1. Check if user already exists (firebase_uid, email, or username)
    2. Create new user in database
    3. Return user data
    """
    pass

# TODO: Implement login endpoint
@router.post("/login")
def login():
    """
    Login user and return JWT token
    Frontend should call this after successful Firebase authentication
    
    Steps:
    1. Find user by firebase_uid
    2. Create JWT access token
    3. Return token
    """
    pass

# TODO: Implement get current user endpoint
@router.get("/me")
def get_current_user_info():
    """
    Get current authenticated user information
    Requires authentication token in header
    """
    pass
