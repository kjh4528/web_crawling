from fastapi import FastAPI

from . import models
from .database import engine
from .routers import categories, todos

# DB테이블 준비 
models.Base.metadata.create_all(bind=engine)
## create_all()은 기본적으로 테이블이 없으면 생성, 있으면 건드리지 않아, 구조변경은 잘 관리하지 못함
## SQLAlchemy 기반 DB 변경사항 관리 마이그레이션 도구 -> Alembic 

# fastAPI 앱 생성 
app = FastAPI()

# 라우터 연결 
app.include_router(categories.router)
app.include_router(todos.router)

# 연결 확인 
@app.get("/")
def read_root():
    return {"message": "Todo API is running"}
