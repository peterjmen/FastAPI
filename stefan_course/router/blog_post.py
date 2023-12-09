from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alis: str

class Blogmodel(BaseModel):
    title: str
    content: str
    number_of_comments: int
    published: Optional[bool]
    image: Optional[Image] = None


@router.post("/")
def create_blog(blog: Blogmodel):
    return {'data': blog}


@router.post('new/id/{id}')
def create_blog(id: int, blog: Blogmodel, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: Blogmodel, id: int,
            comment_id: int = Query(None,
                # Here is metadata for the param
                # title='Comment ID on tje thing',  # Title for params currently does nohing
                description='Description of comment id',
                alias="Comment id:",  # Changes  name of param in docs
                # deprecated=True,  # Can flag as deprecated
            ),
            content: str = Body(..., 
                min_length=10,
                max_length=50,
                regex="^[a-z]*$"
            ),
            v: List[str] = Query(None)  # This is how you do optiona  l lists which has no default
    ): 
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        "content": content,
        "version": v
    }

# ? Body/query are constructs, where you put in info inside
# ... 3 dots called ellipses in python, makes it manddatory to have a body

def required_functionality():
    return {"message": "Learning FastAPI is important"}