from database.database import engine, Base
from model.task_model import Task
from model.user_model import User

Base.metadata.create_all(engine)