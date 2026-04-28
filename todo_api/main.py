from fastapi import FastAPI

from . import models
from .database import engine
from .routers import categories


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(categories.router)


@app.get("/")
def read_root():
    return {"message": "Todo API is running"}
