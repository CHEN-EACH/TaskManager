import database.init_db

from fastapi import FastAPI
from router import user_router

app = FastAPI()

app.include_router(user_router.router,prefix="/users")
