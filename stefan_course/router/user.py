from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create User 
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)  #Here we return one user display

# Read All users
@router.get("/", response_model=List[UserDisplay])  #  Here we return a list of user displays
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# read one user
@router.get("/{user_id}", response_model=UserDisplay)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, user_id)

# Update user

# Delete user
