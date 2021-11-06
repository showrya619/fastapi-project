from fastapi import FastAPI
from fastapi.params import Body
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


@app.post("/createposts")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"   }