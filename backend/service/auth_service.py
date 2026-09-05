import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-for-task-manager-2026"

def create_access_token(user_id):
    
    expire = datetime.now() + timedelta(minutes=30)
    
    payload = {
        "sub" : str(user_id),
        "exp" : expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
        )
    
    return token