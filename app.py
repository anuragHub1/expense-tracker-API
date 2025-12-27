from fastapi import FastAPI
from src.db.session import engine
from src.db.base import Base
from src.db.models import user

app=FastAPI(title="Expense tracker API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def welcome():
    return {"message":"welcome"}