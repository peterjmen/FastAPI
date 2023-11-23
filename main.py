from fastapi import FastAPI
import random   #from random number gen

# create instance of app
app = FastAPI()

@app.get('/')
# this will be the first response the user gets:
async def root():
    return {'example': 'the text of this is an example', 'data':999}

# --reload - makes code automatically applied

@app.get('/random/')
async def get_random():
    rn:int = random.randint(0,100)
    return {'number': rn, 'limit': '100'}

@app.get('/random/{limit}')
async def get_random(limit: int):
    rn = random.randint(0,limit)
    return {'number': rn, 'limit': limit}

@app.get('/shoes')
async def get_shoes():
    return {'info': "eat my shoes"}
