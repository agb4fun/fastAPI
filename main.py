from fastapi import FastAPI, response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional
app = FastAPI ()




class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None


myPosts = [
    {"title":"title of post 1", "content":"content of post 1", "id": 1}
    {"title": "favorite foods","content": "I like pizza","id": 2}
]



def find_index_post(id):
    for i,p in enumerate(myPosts):
        if p["id"] == id
        return i




@app.get("/")
def root():
    return {"message":"Hello World"}



@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/posts")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data":post}

@app.delete("/posts/{id}")
def delete_post():
    #deleting post
    #find the index that has required id
    index = find_index_post(id)
    myPosts.pop(index)
    return {"message":"post was successfully deleted"}
