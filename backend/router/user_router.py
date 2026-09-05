from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schema.user_schema import UserCreate, UserResponse, UserLogin
from service import user_service, auth_service
router = APIRouter()

@router.post("/register",response_model=UserResponse)
def user_create(user_data:UserCreate, db: Session = Depends(get_db)):
    
    try:
        return user_service.create_user(db,user_data)
    
    except ValueError as e:
        raise HTTPException(
            status_code = 409,
            detail = str(e)
        )
        
@router.post("/login")
def user_login(user_data : UserLogin, db : Session = Depends(get_db)):
    
    try:
        user = user_service.verify_password(db,user_data)
        
    except ValueError as e:
        raise HTTPException(
            status_code = 401,
            detail = str(e)
        )
        
    return {
    "access_token": auth_service.create_access_token(user.id),
    "token_type": "bearer"
    }
    
    
    