from db import SessionLocal
from dependencies import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from schemas import UserCreate
from security import hash_password
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/me", response_model=dict)
async def read_user_me(current_user: User = Depends(get_current_user)):
    """ログイン中のユーザー情報を取得"""
    return {"username": current_user.username}


@router.put("/update-password/")
async def update_password(
    new_password: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """ログイン中のユーザーのパスワードを変更"""
    hashed_password = hash_password(new_password)
    current_user.hashed_password = hashed_password
    db.commit()
    return {"message": "パスワードを更新しました"}


@router.delete("/delete/")
async def delete_user(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """ログイン中のユーザーを削除"""
    db.delete(current_user)
    db.commit()
    return {"message": "ユーザーを削除しました"}


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """新規ユーザー登録"""
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="このユーザー名は既に使用されています"
        )

    hashed_password = hash_password(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "ユーザーが登録されました", "username": new_user.username}
