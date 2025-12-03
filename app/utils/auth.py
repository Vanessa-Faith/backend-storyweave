"""
Authentication utilities - Member 1
TODO: Implement JWT token management and user authentication

Reference implementation available in: reference_implementations/auth_utils_REFERENCE.py

Tasks:
1. Implement create_access_token() - Generate JWT tokens
2. Implement verify_token() - Validate JWT tokens  
3. Implement get_current_user() - Get authenticated user from token
4. (Optional) Add Firebase token verification

See WORKFLOW.md Day 1-2 for detailed steps
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.config import settings
from app.database import get_db
from app.models import User
from app.schemas import TokenData

security = HTTPBearer()

# TODO: Implement create_access_token function
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token
    
    Args:
        data: Dictionary with user data (usually {"sub": firebase_uid})
        expires_delta: Optional custom expiration time
        
    Returns:
        Encoded JWT token string
        
    Steps:
    1. Copy the data dictionary
    2. Calculate expiration time (use expires_delta or default from settings)
    3. Add expiration to data: {"exp": expire_time}
    4. Encode with jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    5. Return the encoded token
    
    Hint: Check reference_implementations/auth_utils_REFERENCE.py for example
    """
    pass  # TODO: Implement this


# TODO: Implement verify_token function
def verify_token(token: str) -> TokenData:
    """
    Verify and decode a JWT token
    
    Args:
        token: JWT token string
        
    Returns:
        TokenData object with firebase_uid
        
    Raises:
        HTTPException 401 if token is invalid
        
    Steps:
    1. Try to decode token with jwt.decode()
    2. Extract firebase_uid from payload (key: "sub")
    3. If firebase_uid is None, raise HTTPException
    4. Return TokenData(firebase_uid=firebase_uid)
    5. Catch JWTError and raise HTTPException 401
    
    Hint: Check reference_implementations/auth_utils_REFERENCE.py for example
    """
    pass  # TODO: Implement this


# TODO: Implement get_current_user function
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Get the current authenticated user from token
    
    This is used as a dependency in protected routes:
    @router.get("/protected")
    def protected_route(current_user: User = Depends(get_current_user)):
        # current_user is automatically injected here
        
    Args:
        credentials: Token from Authorization header (automatic)
        db: Database session (automatic)
        
    Returns:
        User object from database
        
    Raises:
        HTTPException 404 if user not found
        
    Steps:
    1. Extract token from credentials.credentials
    2. Verify token using verify_token()
    3. Query database for user by firebase_uid
    4. If user not found, raise HTTPException 404
    5. Return user
    
    Hint: Check reference_implementations/auth_utils_REFERENCE.py for example
    """
    pass  # TODO: Implement this


# OPTIONAL: Firebase token verification
def verify_firebase_token(id_token: str):
    """
    Verify Firebase ID token (OPTIONAL - for later enhancement)
    
    This requires Firebase Admin SDK to be properly initialized.
    For now, focus on JWT-based auth above.
    
    When implementing:
    1. Use firebase_auth.verify_id_token(id_token)
    2. Return decoded token
    3. Handle exceptions appropriately
    """
    pass  # Optional enhancement
