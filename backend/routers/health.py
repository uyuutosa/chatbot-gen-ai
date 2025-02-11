import platform
import time

from config import settings
from db import SessionLocal
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

start_time = time.time()  # サーバー起動時間を記録


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", tags=["Health"])
async def health_check():
    """API のヘルスチェック"""
    return {"status": "ok"}


@router.get("/db", tags=["Health"])
async def database_health_check(db: Session = Depends(get_db)):
    """データベース接続のヘルスチェック"""
    try:
        db.execute("SELECT 1")  # データベースにシンプルなクエリを実行
        return {"db_status": "connected"}
    except Exception as e:
        return {"db_status": "error", "detail": str(e)}


@router.get("/system", tags=["Health"])
async def system_info():
    """サーバーの情報を取得（Python / FastAPI / Uptime）"""
    uptime = round(time.time() - start_time, 2)
    return {
        "python_version": platform.python_version(),
        "fastapi_version": settings.FASTAPI_VERSION,
        "uptime_seconds": uptime,
    }
