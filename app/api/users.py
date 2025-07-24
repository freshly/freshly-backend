from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.firebase_service import add_user_to_firebase

router = APIRouter()

class User(BaseModel):
    email: str
    name: str

@router.post("/users/")
async def register_user(user: User):
    try:
        await add_user_to_firebase(user.email, user.name)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))