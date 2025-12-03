from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Story as StoryModel, User
from app.schemas import StoryCreate, Story, StoryDetail, StoryUpdate
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=Story, status_code=status.HTTP_201_CREATED)
def create_story(
    story: StoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new story"""
    db_story = StoryModel(**story.model_dump(), author_id=current_user.id)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

@router.get("/", response_model=List[StoryDetail])
def get_stories(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get all public stories"""
    stories = db.query(StoryModel).filter(
        StoryModel.is_public == True
    ).offset(skip).limit(limit).all()
    return stories

@router.get("/my-stories", response_model=List[Story])
def get_my_stories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current user's stories"""
    stories = db.query(StoryModel).filter(
        StoryModel.author_id == current_user.id
    ).all()
    return stories

@router.get("/{story_id}", response_model=StoryDetail)
def get_story(story_id: int, db: Session = Depends(get_db)):
    """Get a specific story by ID"""
    story = db.query(StoryModel).filter(StoryModel.id == story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    if not story.is_public:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This story is private"
        )
    
    return story

@router.put("/{story_id}", response_model=Story)
def update_story(
    story_id: int,
    story_update: StoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a story"""
    story = db.query(StoryModel).filter(StoryModel.id == story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    if story.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this story"
        )
    
    # Update only provided fields
    update_data = story_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(story, field, value)
    
    db.commit()
    db.refresh(story)
    return story

@router.delete("/{story_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_story(
    story_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a story"""
    story = db.query(StoryModel).filter(StoryModel.id == story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    if story.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this story"
        )
    
    db.delete(story)
    db.commit()
    return None
