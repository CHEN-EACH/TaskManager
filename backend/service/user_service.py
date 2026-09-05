from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from schema.user_schema import UserCreate, UserLogin
from model.user_model import User

password_hash = PasswordHash.recommended()

def hash_password(password : str):
    
    return password_hash.hash(password)

def create_user(db : Session, user_data : UserCreate):
    
    account = user_data.account
    stmt = select(User).where(User.account == account)
    user = db.execute(stmt).scalars().one_or_none()
    if user is None:
        
        new_user = User(
            account = user_data.account,
            password_hash = hash_password(user_data.password),
            nickname = user_data.nickname
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
        
    else:
        
        raise ValueError("用户已存在")
    
def verify_password(db:Session, user_data : UserLogin):
    
    stmt = select(User).where(User.account == user_data.account)
    user = db.execute(stmt).scalars().one_or_none()
    if user is None:
        
        raise ValueError("用户名或密码错误")
    
    if not password_hash.verify(user_data.password,user.password_hash):
       
       raise ValueError("用户名或密码错误")
    
    return user
    