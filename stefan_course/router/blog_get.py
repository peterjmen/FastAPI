from fastapi import APIRouter
from typing import Optional
from enum import Enum
from fastapi import HTTPException
from router.blog_post import required_functionality
from fastapi import Depends

router = APIRouter(
    prefix="/blog",
    tags=["blog"])

# Out agove as to not be intercepted
@router.get("/all")
def get_all_blogs():
    
    return {"data": "all blogs"}


# Below is a generic method that must come last, or will intercept all others
@router.get("/{number}")  # ("/blog/{number}", status_code=status.HTTP_404_NOT_FOUND)
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

@router.get("/type/{type}")
def blog_type(type: BlogType):
    return {"message": f"blog type: {type}"}
# endregion - PREDEFINED

@router.get("/everything/")
def blog_everything(page = 1, pagesize = 10):
    return {"message": f"blog page: {page} and pagesize: {pagesize}"}

# # Better:
# @router.get('/blog/everything')
# def get_blogs(page: int = 1, page_siz e: int = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Another way to provide optional paramters:

@router.get("/everything/opt")
def blog_everything(page = 1, pagesize: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"blog page: {page} and pagesize: {pagesize}", "req": req_parameter}

@router.get("/{id}/comments/{comment_id}")
def comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"blog_id": id, "comment_id": comment_id, "valid": valid, "username": username}
