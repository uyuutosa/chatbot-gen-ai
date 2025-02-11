import fastapi
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import (
    BaseSettings,  # ✅ 修正: `pydantic_settings` から `BaseSettings` をインポート
)

load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=60, env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    DATABASE_URL: str = Field(default="sqlite:///./users.db", env="DATABASE_URL")

    FASTAPI_VERSION: str = fastapi.__version__  # FastAPI のバージョン情報を追加

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
