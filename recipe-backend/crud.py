from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_random_recipes(db: Session, n: int, exclude_ids: list = []):
    return db.query(models.Recipe).filter(~models.Recipe.id.in_(exclude_ids)).order_by(func.random()).limit(n).all()
