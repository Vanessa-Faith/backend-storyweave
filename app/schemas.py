from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    display_name: Optional[str] = None

class UserCreate(UserBase):
    firebase_uid: str

class User(UserBase):
    id: int
    firebase_uid: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Story Schemas
class StoryBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_public: bool = True

class StoryCreate(StoryBase):
    pass

class StoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None

class Story(StoryBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class StoryDetail(Story):
    author: User
    
    class Config:
        from_attributes = True

# Node Schemas
class NodeBase(BaseModel):
    content: str

class NodeCreate(NodeBase):
    story_id: int
    parent_node_id: Optional[int] = None

class Node(NodeBase):
    id: int
    story_id: int
    parent_node_id: Optional[int]
    author_id: int
    order: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class NodeDetail(Node):
    author: User
    children: List['Node'] = []
    
    class Config:
        from_attributes = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    firebase_uid: Optional[str] = None
