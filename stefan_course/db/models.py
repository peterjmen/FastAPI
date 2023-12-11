from db.database import Base
from sqlalchemy import Column, Integer, String

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))  # Length specified here
    email = Column(String(255))     # Length specified here
    password = Column(String(255))  # Length specified here