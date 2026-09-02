from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.database import get_db

app = FastAPI()

@app.get("/")
def start(db : Session = Depends(get_db)):
    
    stmt = select(1)
    result = db.execute(stmt).scalar()
    
    return result


