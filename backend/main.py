from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from database.database import get_db
from database.database import Base, engine
from model.user_model import User
from model.task_model import Task

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def start(db: Session = Depends(get_db)):

    stmt = text("SELECT name FROM sqlite_master WHERE type = 'table';")
    result = db.execute(stmt).scalars().all()

    return result

