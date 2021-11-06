from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional




class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: Optional[int] = None


app = FastAPI()


#decorater in python turns function into a path operation
@app.get("/")
#"/" - root path
#PATH Operation
#Function defination - async (API, asynchronously)
async def root():
    return {"message":"welcome to my first api"}



@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createpostsv1")
#Without pydantic
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"   }


@app.post("/createpostsv2")
#With pydantic
async def create_postsv2(post: Post):
    #print(new_post.dict())
    print(post.title)
    print(post.content)
    print(post.published)
    print(post.rating)
    return {"data":post.dict()}