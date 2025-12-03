from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Node as NodeModel, Story, User
from app.schemas import NodeCreate, Node, NodeDetail
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=Node, status_code=status.HTTP_201_CREATED)
def create_node(
    node: NodeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new story node (paragraph/branch)"""
    # Verify story exists
    story = db.query(Story).filter(Story.id == node.story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    # Verify parent node exists if specified
    if node.parent_node_id:
        parent = db.query(NodeModel).filter(
            NodeModel.id == node.parent_node_id,
            NodeModel.story_id == node.story_id
        ).first()
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent node not found"
            )
    
    # Calculate order
    siblings = db.query(NodeModel).filter(
        NodeModel.story_id == node.story_id,
        NodeModel.parent_node_id == node.parent_node_id
    ).all()
    order = len(siblings)
    
    db_node = NodeModel(
        **node.model_dump(),
        author_id=current_user.id,
        order=order
    )
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node

@router.get("/story/{story_id}", response_model=List[NodeDetail])
def get_story_nodes(story_id: int, db: Session = Depends(get_db)):
    """Get all nodes for a story"""
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    nodes = db.query(NodeModel).filter(
        NodeModel.story_id == story_id
    ).order_by(NodeModel.order).all()
    
    return nodes

@router.get("/story/{story_id}/tree")
def get_story_tree(story_id: int, db: Session = Depends(get_db)):
    """Get story nodes as a tree structure"""
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Story not found"
        )
    
    # Get all nodes
    nodes = db.query(NodeModel).filter(
        NodeModel.story_id == story_id
    ).order_by(NodeModel.order).all()
    
    # Build tree structure
    node_dict = {node.id: {
        "id": node.id,
        "content": node.content,
        "author_id": node.author_id,
        "parent_node_id": node.parent_node_id,
        "order": node.order,
        "created_at": node.created_at.isoformat(),
        "children": []
    } for node in nodes}
    
    # Link children to parents
    root_nodes = []
    for node in nodes:
        if node.parent_node_id is None:
            root_nodes.append(node_dict[node.id])
        else:
            if node.parent_node_id in node_dict:
                node_dict[node.parent_node_id]["children"].append(node_dict[node.id])
    
    return {
        "story_id": story_id,
        "story_title": story.title,
        "root_nodes": root_nodes
    }

@router.get("/{node_id}", response_model=NodeDetail)
def get_node(node_id: int, db: Session = Depends(get_db)):
    """Get a specific node by ID"""
    node = db.query(NodeModel).filter(NodeModel.id == node_id).first()
    if not node:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Node not found"
        )
    return node

@router.delete("/{node_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_node(
    node_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a node"""
    node = db.query(NodeModel).filter(NodeModel.id == node_id).first()
    if not node:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Node not found"
        )
    
    if node.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this node"
        )
    
    db.delete(node)
    db.commit()
    return None
