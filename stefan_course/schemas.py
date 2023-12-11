# Schemas.py

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str
    password: str

    # class Config:
    #     from_attributes = True  # Changed from orm_mode to from_attributes

class UserDisplay(BaseModel):
    email: str
    username: str
    class Config:
        orm_mode = True  # Allows the system to return database data automatically into the format we have provided