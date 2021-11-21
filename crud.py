from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db: Session):
    return db.query(models.Item).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user: int):
    db_item = models.Item(**item.dict(), user_id=user)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item