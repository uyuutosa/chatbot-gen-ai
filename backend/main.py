from fastapi import FastAPI
from routers import auth, chat, health, user

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(health.router, prefix="/health", tags=["Health"])


@app.get("/")
async def root():
    return {"message": "FastAPI Chat with JWT Auth"}
