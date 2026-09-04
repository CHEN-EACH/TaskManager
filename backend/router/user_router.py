from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schema.user_schema import UserCreate, UserResponse
from service import user_service
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
    