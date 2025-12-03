from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User as UserModel
from app.schemas import UserCreate, User, Token
from app.utils.auth import create_access_token

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user with Firebase UID
    This should be called after Firebase authentication on the frontend
    """
    # Check if user already exists
    existing_user = db.query(UserModel).filter(
        (UserModel.firebase_uid == user.firebase_uid) |
        (UserModel.email == user.email) |
        (UserModel.username == user.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email, username, or Firebase UID already exists"
        )
    
    # Create new user
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login", response_model=Token)
def login(firebase_uid: str, db: Session = Depends(get_db)):
    """
    Login user and return JWT token
    Frontend should call this after successful Firebase authentication
    """
    user = db.query(UserModel).filter(UserModel.firebase_uid == firebase_uid).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found. Please register first."
        )
    
    # Create access token
    access_token = create_access_token(data={"sub": user.firebase_uid})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=User)
def get_current_user_info(current_user: UserModel = Depends(get_db)):
    """Get current authenticated user information"""
    from app.utils.auth import get_current_user
    return Depends(get_current_user)
