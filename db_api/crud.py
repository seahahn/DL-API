from sqlalchemy.orm import Session
from db_api import models, schemas


def get_post(db: Session, post_id: int):
    return db.query(models.AiPost).filter(models.AiPost.idx == post_id).first()


def get_posts_by_div(db: Session, div: str):
    return db.query(models.AiPost).filter(models.AiPost.div == div).order_by(models.AiPost.created_at.desc()).all()


def get_posts(db: Session):
    return db.query(models.AiPost).all()


def create_post(db: Session, post: schemas.AiPostCreate):
    db_post = models.AiPost(**post.dict(exclude_unset=True))
    db.add(db_post)
    db.commit()
    return db_post

def update_post(db: Session, post_id: int, post: schemas.AiPostCreate):
    old_post = db.query(models.AiPost).filter(models.AiPost.idx == post_id).first()
    update_data = post.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(old_post, key, value)

    db.commit()
    return old_post

def delete_post(db: Session, post_id: int):
    post = db.query(models.AiPost).filter(models.AiPost.idx == post_id).first()
    db.delete(post)
    db.commit()
    return True