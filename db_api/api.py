from fastapi import Depends, HTTPException, Header
from typing import Optional
from sqlalchemy.orm import Session

from db_api import crud, models, schemas
from db_api.database import SessionLocal, engine

import jwt, os
from dotenv import load_dotenv
load_dotenv()

models.Base.metadata.create_all(bind=engine)

SECRET_KEY = os.getenv('SECRET_KEY')
ADMIN_MEMBERSHIP_CODE = os.getenv('ADMIN_MEMBERSHIP_CODE')
JWT_ISS = os.getenv('JWT_ISS')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 관리자 인증이 필요한 기능에 JWT 토큰 인증 과정을 붙이기 위한 데코레이터
def verify_token(original):
    def wrapper(db: Session = Depends(get_db), post: Optional[schemas.AiPostCreate] = None, post_id: Optional[int] = None, token: Optional[str] = Header(None)):
        try:
            # 토큰을 검증하여 유효한 토큰인지 확인
            at = token
            at_data = jwt.decode(at, SECRET_KEY, algorithms="HS256")

            # access token 안에 있는 membership 값이 관리자 계정 코드와 같으면 관리자 계정으로 인증
            if at_data['membership'] == int(ADMIN_MEMBERSHIP_CODE):
                return original(post_id, post, db)
            else:
                return HTTPException(status_code=401, detail="Unauthorized")
        except Exception as e:
            return {"result":False, "token_state":False, "message":str(e)}

    return wrapper

def index():
    return {"message": "Welcome to AI Play Deep Learning API"}

@verify_token
def create_post(_, post: schemas.AiPostCreate, db: Session = Depends(get_db)):
    """
    AI Play 웹 앱 내 ML/DL 예시 프로젝트 목록의 게시물(post)을 추가하는 기능

    Args:
        post (schemas.AiPostCreate): 게시물 추가를 위한 데이터(스키마로 정의됨)
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Returns:
        dict: 생성된 게시물 데이터
    """
    return crud.create_post(db=db, post=post)


@verify_token
def update_post(post_id: int, post: schemas.AiPostCreate, db: Session = Depends(get_db)):
    """
    AI Play 웹 앱 내 ML/DL 예시 프로젝트 목록의 게시물(post)을 수정하는 기능

    Args:
        post_id (int): 게시물 고유 번호
        post (schemas.AiPostCreate): 게시물 수정을 위한 데이터(스키마로 정의됨)
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Returns:
        dict: 수정된 게시물 데이터
    """
    return crud.update_post(db=db, post_id=post_id, post=post)

@verify_token
def delete_post(post_id: int, _, db: Session = Depends(get_db)):
    """
    AI Play 웹 앱 내 ML/DL 예시 프로젝트 목록의 게시물(post)을 삭제하는 기능

    Args:
        post_id (int): 게시물 고유 번호
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Returns:
        Boolean: 삭제 성공 시 True를 반환
    """
    return crud.delete_post(db=db, post_id=post_id)

@verify_token
def read_posts(db: Session = Depends(get_db)):
    """
    AI Play 웹 앱 내 ML/DL 예시 프로젝트 목록의 게시물(post) 전체를 불러오는 기능

    관리자 전용 기능으로 사용 예정

    Args:
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Returns:
        array: 전체 게시물 목록
    """
    posts = crud.get_posts(db=db)
    return posts

def read_posts_by_div(div: str, db: Session = Depends(get_db)):
    """
    div(ml/dl) 값에 해당되는 예시 프로젝트 목록의 게시물(post)들을 불러오는 기능

    Args:
        div (str): 게시물 분류 값. ml 또는 dl.
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Returns:
        array: 지정된 분류 내 게시물 목록
    """
    posts = crud.get_posts_by_div(db=db, div=div)
    return posts

def read_post(post_id: int, db: Session = Depends(get_db)):
    """
    게시물 고유 번호(post_id) 값에 해당되는 예시 프로젝트 목록의 게시물(post)을 불러오는 기능

    Args:
        post_id (int): 게시물 고유 번호
        db (Session, optional): 연결된 DB 객체. Defaults to Depends(get_db).

    Raises:
        HTTPException: 게시물이 없으면 에러 반환

    Returns:
        dict: 지정된 게시물 데이터
    """
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        return HTTPException(status_code=404, detail="Post not found")
    return db_post