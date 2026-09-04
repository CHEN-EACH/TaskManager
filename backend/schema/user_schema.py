from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    
    account : str
    password : str
    nickname : str | None = None
    
class UserResponse(BaseModel):
    
    id : int
    account : str
    nickname : str | None = None
    
    model_config = ConfigDict(from_attributes=True)