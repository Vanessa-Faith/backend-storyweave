from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserRead, Token
from app.utils.auth import create_access_token, get_current_user


router = APIRouter(prefix="/api/auth", tags=["auth"])

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):

    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == user_in.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    

    user = User(
        firebase_uid=user_in.firebase_uid,
        email=user_in.email,
        username=user_in.username,
        display_name=user_in.display_name,
    )

    if hasattr(user_in, "password") and user_in.password:
        user.hashed_password = hash_password(user_in.password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if hasattr(user_in, "password") and user_in.password:
        if not verify_password(user_in.password, getattr(user, "hashed_password", "")):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        

    access_token = create_access_token(data={"sub": user.firebase_uid})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
