from fastapi import FastAPI, status, HTTPException
from enum import Enum
from typing import Optional

app = FastAPI()


# Define methods 🔽 # On the functions
@app.get("/")  #creates get method that getst this fuction

# On the functions 🔽
def index():
    return {"Hello, World"}  # To run this on a browser, we will need to call this with get method


# To run uvicorn, the command is uvicorn main:app(in this case main for main.py) --reload (--reload is a flag what will reload server when change made)

@app.get("/gb") # HTTP request here ->
def gb():  # Runs this function
    data = {1: 'goodbye, world'}  # object/dictionary in python, but gets turned into JSON!! (awesome)
    return data  # This is what is actually returned when we go to that endpoint

# Out agove as to not be intercepted
@app.get("/blog/all")
def get_all_blogs():
    return {"data": "all blogs"}


# Below is a generic method that must come last, or will intercept all others
@app.get("/blog/{number}")  # ("/blog/{number}", status_code=status.HTTP_404_NOT_FOUND)
def blog(number: int):
    if number > 10:
        # return {"message": "There are not that many blogs"}
        raise HTTPException(status_code=404, detail="There are not that many blogs")
    else:
        return {"message": f"blog number: {number}"}


# region - PREdefined input for api
class BlogType(str, Enum):
    good = "good"
    bad = "bad"
    ugly = "ugly"

@app.get("/blog/type/{type}")
def blog_type(type: BlogType):
    return {"message": f"blog type: {type}"}
# endregion - PREDEFINED

@app.get("/blog/everything/")
def blog_everything(page = 1, pagesize = 10):
    return {"message": f"blog page: {page} and pagesize: {pagesize}"}

# # Better:
# @app.get('/blog/everything')
# def get_blogs(page: int = 1, page_size: int = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Another way to provide optional paramters:

@app.get("/blog/everything/opt")
def blog_everything(page = 1, pagesize: Optional[int] = None):
    return {"message": f"blog page: {page} and pagesize: {pagesize}"}

@app.get("/blog/{id}/comments/{comment_id}")
def comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"blog_id": id, "comment_id": comment_id, "valid": valid, "username": username}


