from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

# MongoDB Atlas connection string
client = AsyncIOMotorClient("mongodb+srv://<yadavshubh1107>:<Gu15zZofPrBObaFM>@cluster0.u88co.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.school_blog  # Replace with your actual database name

# Pydantic model for blog post
class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the School Blog API!"}

# Create a Blog Post
@app.post("/posts/")
async def create_blog_post(post: BlogPost):
    # Add created_at if not provided
    if not post.created_at:
        post.created_at = datetime.now()

    # Insert post into MongoDB
    result = await db.posts.insert_one(post.dict())
    return {"id": str(result.inserted_id), **post.dict()}

# Read All Blog Posts
@app.get("/posts/")
async def read_blog_posts():
    posts = []
    async for post in db.posts.find():
        post["_id"] = str(post["_id"])  # Convert ObjectId to string
        posts.append(post)
    return {"posts": posts}

# Read a Single Blog Post
@app.get("/posts/{post_id}")
async def read_blog_post(post_id: str):
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post:
        post["_id"] = str(post["_id"])  # Convert ObjectId to string
        return post
    return {"error": "Post not found"}

# Update a Blog Post
@app.put("/posts/{post_id}")
async def update_blog_post(post_id: str, post: BlogPost):
    update_result = await db.posts.update_one(
        {"_id": ObjectId(post_id)}, {"$set": post.dict(exclude_unset=True)}
    )
    if update_result.modified_count == 1:
        updated_post = await db.posts.find_one({"_id": ObjectId(post_id)})
        updated_post["_id"] = str(updated_post["_id"])
        return updated_post
    return {"error": "Post not found or no changes made"}

# Delete a Blog Post
@app.delete("/posts/{post_id}")
async def delete_blog_post(post_id: str):
    delete_result = await db.posts.delete_one({"_id": ObjectId(post_id)})
    if delete_result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    return {"error": "Post not found"}
