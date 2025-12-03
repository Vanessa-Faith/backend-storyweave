"""
Sample data script for testing StoryWeave API
Run this after setting up the database to populate it with example data
"""

from app.database import SessionLocal
from app.models import User, Story, Node
from datetime import datetime

def create_sample_data():
    db = SessionLocal()
    
    try:
        # Clear existing data (optional - comment out if you want to keep existing data)
        # db.query(Node).delete()
        # db.query(Story).delete()
        # db.query(User).delete()
        # db.commit()
        
        # Create sample users
        user1 = User(
            firebase_uid="sample_user_1",
            email="alice@example.com",
            username="alice_writer",
            display_name="Alice the Writer"
        )
        
        user2 = User(
            firebase_uid="sample_user_2",
            email="bob@example.com",
            username="bob_storyteller",
            display_name="Bob the Storyteller"
        )
        
        user3 = User(
            firebase_uid="sample_user_3",
            email="carol@example.com",
            username="carol_author",
            display_name="Carol the Author"
        )
        
        db.add_all([user1, user2, user3])
        db.commit()
        db.refresh(user1)
        db.refresh(user2)
        db.refresh(user3)
        
        print(f"✅ Created {3} users")
        
        # Create sample stories
        story1 = Story(
            title="The Enchanted Forest",
            description="A magical adventure where your choices shape the story",
            author_id=user1.id,
            is_public=True
        )
        
        story2 = Story(
            title="Space Station Alpha",
            description="A sci-fi thriller aboard a mysterious space station",
            author_id=user2.id,
            is_public=True
        )
        
        story3 = Story(
            title="The Mystery Mansion",
            description="A detective story with multiple suspects and endings",
            author_id=user1.id,
            is_public=False
        )
        
        db.add_all([story1, story2, story3])
        db.commit()
        db.refresh(story1)
        db.refresh(story2)
        db.refresh(story3)
        
        print(f"✅ Created {3} stories")
        
        # Create sample nodes for Story 1 (Enchanted Forest) - Branching narrative
        node1 = Node(
            story_id=story1.id,
            parent_node_id=None,
            author_id=user1.id,
            content="You wake up in a mysterious forest. Sunlight filters through the ancient trees, and you hear the sound of running water nearby. A worn path leads deeper into the woods, while a smaller trail heads toward the sound of water.",
            order=0
        )
        db.add(node1)
        db.commit()
        db.refresh(node1)
        
        # Branch A: Follow the main path
        node2 = Node(
            story_id=story1.id,
            parent_node_id=node1.id,
            author_id=user2.id,
            content="You decide to follow the main path. As you walk, the trees seem to whisper secrets. Suddenly, you encounter a talking fox who offers to guide you.",
            order=0
        )
        db.add(node2)
        db.commit()
        db.refresh(node2)
        
        # Branch B: Head toward the water
        node3 = Node(
            story_id=story1.id,
            parent_node_id=node1.id,
            author_id=user3.id,
            content="You head toward the sound of water and discover a crystal-clear stream. On the other side, you see a glowing bridge made of moonlight.",
            order=1
        )
        db.add(node3)
        db.commit()
        db.refresh(node3)
        
        # Branch A1: Accept the fox's help
        node4 = Node(
            story_id=story1.id,
            parent_node_id=node2.id,
            author_id=user1.id,
            content="You accept the fox's offer. 'Follow me,' it says, leading you to a hidden grove where magical creatures gather. They welcome you as one of their own.",
            order=0
        )
        db.add(node4)
        db.commit()
        
        # Branch A2: Politely decline
        node5 = Node(
            story_id=story1.id,
            parent_node_id=node2.id,
            author_id=user2.id,
            content="You thank the fox but decide to continue alone. The forest grows darker, and you begin to hear strange music coming from somewhere ahead.",
            order=1
        )
        db.add(node5)
        db.commit()
        
        # Branch B1: Cross the moonlight bridge
        node6 = Node(
            story_id=story1.id,
            parent_node_id=node3.id,
            author_id=user3.id,
            content="You step onto the glowing bridge. It feels solid beneath your feet and transports you to a realm of eternal twilight, where time moves differently.",
            order=0
        )
        db.add(node6)
        db.commit()
        
        # Branch B2: Follow the stream
        node7 = Node(
            story_id=story1.id,
            parent_node_id=node3.id,
            author_id=user1.id,
            content="You decide to follow the stream instead. After a while, you discover a waterfall hiding a secret cave filled with ancient treasures.",
            order=1
        )
        db.add(node7)
        db.commit()
        
        print(f"✅ Created {7} nodes with branching paths for Story 1")
        
        # Create sample nodes for Story 2 (Space Station) - Linear narrative
        node8 = Node(
            story_id=story2.id,
            parent_node_id=None,
            author_id=user2.id,
            content="You arrive at Space Station Alpha, humanity's most advanced outpost. But something is wrong—the station is eerily quiet, and half the lights are out.",
            order=0
        )
        db.add(node8)
        db.commit()
        db.refresh(node8)
        
        node9 = Node(
            story_id=story2.id,
            parent_node_id=node8.id,
            author_id=user3.id,
            content="You check the main control room and find a cryptic message on the screen: 'They came from the dark. We couldn't stop them. Don't trust—' The message cuts off.",
            order=0
        )
        db.add(node9)
        db.commit()
        db.refresh(node9)
        
        node10 = Node(
            story_id=story2.id,
            parent_node_id=node9.id,
            author_id=user1.id,
            content="A sudden noise from the corridor makes you spin around. In the dim emergency lighting, you see a shadow moving. Then another. They're not human.",
            order=0
        )
        db.add(node10)
        db.commit()
        
        print(f"✅ Created {3} nodes for Story 2")
        
        print("\n" + "="*50)
        print("✨ Sample data created successfully!")
        print("="*50)
        print(f"\n📊 Summary:")
        print(f"   Users: {db.query(User).count()}")
        print(f"   Stories: {db.query(Story).count()}")
        print(f"   Nodes: {db.query(Node).count()}")
        print(f"\n💡 Test the API:")
        print(f"   1. Login as alice: POST /api/auth/login?firebase_uid=sample_user_1")
        print(f"   2. View stories: GET /api/stories")
        print(f"   3. View tree: GET /api/nodes/story/1/tree")
        print(f"\n🔗 API Docs: http://localhost:8000/docs")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("\n🌟 StoryWeave Sample Data Generator")
    print("="*50)
    create_sample_data()
