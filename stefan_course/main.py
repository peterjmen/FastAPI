from fastapi import FastAPI
from router import blog_get
from router import blog_post



app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)


# Define methods 🔽 # On the functions
@app.get("/")  #creates get method that getst this fuction

# On the functions 🔽
def index():
    return {"Hello, World"}  # To run this on a browser, we will need to call this with get method


# To run uvicorn, the command is uvicorn main:app(in this case main for main.py) --reload (--reload is a flag what will reload server when change made)

@app.get("/gb",
         summary="A positive message, to say goodbye",
        #  description="This is a longer description of the endpoint",
        # response_description="This is the response description",
         ) # HTTP request here ->
def gb():  # Runs this function
    """
    - This seems like a **better** way to do descriptions, using markup in the def
    - Bullet points
    - Yay
    """
    data = {1: 'goodbye, world'}  # object/dictionary in python, but gets turned into JSON!! (awesome)
    return data  # This is what is actually returned when we go to that endpoint



