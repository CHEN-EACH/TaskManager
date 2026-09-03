import database.init_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from database.database import get_db

app = FastAPI()

@app.get("/")
def start(db: Session = Depends(get_db)):

    stmt = text("SELECT name FROM sqlite_master WHERE type = 'table';")
    result = db.execute(stmt).scalars().all()

    return result

