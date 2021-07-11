from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import models


def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_by_name(db: Session, name: str, id: int):
    return db.query(models.User).filter(or_(models.User.name == name, models.User.id == id)).first()



def create_batch(db: Session, user):
    for i in range(0,len(user)):
        query = models.User(name=user[i]['Name'], id=user[i]['Id'])
        db.add(query)
    db.commit()
    db.refresh(query)
    return "Users successfully Add to DB you can now go ahead to test"


def create_user(db: Session, user):
    query = models.User(name=user.name, id=user.id)
    db.add(query)
    db.commit()
    db.refresh(query)
    return query


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
