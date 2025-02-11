from pydantic import BaseModel


class UserCreate(BaseModel):
    """新規ユーザー登録用スキーマ"""

    username: str
    password: str
