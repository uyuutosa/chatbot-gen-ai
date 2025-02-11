from datetime import timedelta

from config import settings
from db import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from security import create_access_token, hash_password, verify_password
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register/")
async def register(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="ユーザー名はすでに存在します")

    hashed_password = hash_password(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "ユーザー登録完了"}


@router.post("/login/")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="無効な認証情報"
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )  # ✅ 修正
    access_token = create_access_token({"sub": username}, access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
