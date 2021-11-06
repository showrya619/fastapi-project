from fastapi import FastAPI,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi.exceptions import HTTPException



class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: Optional[int] = None


app = FastAPI()


my_posts = [{"title":"title of post 1", "content":"content of post 1","id":1},
            {"title":"Foood", "content":"Biryani","id":2}]



def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def del_post(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            del my_posts[i]


#decorater in python turns function into a path operation
@app.get("/")
#"/" - root path
#PATH Operation
#Function defination - async (API, asynchronously)
async def root():
    return {"message":"welcome to my first api"}



@app.get("/posts")
async def get_posts():
    return {"data":my_posts}



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



@app.post("/posts",status_code=status.HTTP_201_CREATED)
#With pydantic and best naming conventions
async def create_postsv2(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,99999999)
    my_posts.append(post_dict)
    return {"data":post_dict}



@app.get("/posts/{id}")
def get_post(id: int, response:Response):
    post = find_post(id)

    #post = find_post(int(id)) - This is handled in path pareameter
    #return {"post_details":f"Here is the post {id}"}
    
    #Return status code 404 if item not found    
    #With Hardcoding
    # if not post:
    #     response.status_code = 404
    
    #With status function in FastAPI
    # if not post:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message":f"post with id {id} not found"}

    #With HTTP Exception in FastAPI
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")

    return {"post_details":post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response:Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    delete_post = del_post(id)

    return {"post_details":f"post with id {id} has been deleted"}