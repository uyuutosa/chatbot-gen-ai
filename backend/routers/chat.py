from typing import Dict

import jwt
from config import settings
from fastapi import APIRouter, HTTPException, Query, WebSocket, WebSocketDisconnect

router = APIRouter()

# WebSocket 接続を管理するための辞書（ユーザーIDごとにWebSocketを保持）
active_connections: Dict[str, WebSocket] = {}


def verify_jwt_token(token: str):
    """JWT トークンを検証し、ユーザー名を取得する"""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload.get("sub")  # JWT の `sub` フィールドにユーザー名を格納
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401, detail="JWT トークンの有効期限が切れています"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="無効な JWT トークン")


@router.websocket("/chat")
async def websocket_chat(websocket: WebSocket, token: str = Query(...)):
    """JWT トークン認証付きの WebSocket チャット"""
    username = verify_jwt_token(token)
    if not username:
        await websocket.close()
        return

    # 接続を受け入れ
    await websocket.accept()
    active_connections[username] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            # 受け取ったメッセージを全ユーザーに送信
            for user, conn in active_connections.items():
                if conn != websocket:
                    await conn.send_text(f"{username}: {data}")
    except WebSocketDisconnect:
        # ユーザーが切断した場合、接続を削除
        del active_connections[username]
