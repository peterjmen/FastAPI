from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Must refresh, because we need to give the new created user an id
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()