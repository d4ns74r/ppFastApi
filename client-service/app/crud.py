from sqlalchemy.orm import Session
from . import models, schemas
from .utils import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_info(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
