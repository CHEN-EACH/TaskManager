import database.init_db
from datetime import datetime
from sqlalchemy.orm import Session
from database.database import SessionLocal
from model.user_model import User
from model.task_model import Task

db = SessionLocal()
time_now = datetime.now()

user = User(
    account = '12345',
    password_hash = "uieigiuvhiudhg",
    nickname = "CHEN"
)

db.add(user)
print(user.id)
db.commit()
db.refresh(user)

task = Task(
    user_id = user.id,
    status = "undo",
    title = "practice algorithm",
    created_at = time_now,
    updated_at = time_now,
    priority = 1
)

user.tasks.append(task)
db.add(task)
db.commit()
db.refresh(task)

print(task.id)
print(task.user.account)
print(user.tasks[0].title)
print(user.id)

db.close()