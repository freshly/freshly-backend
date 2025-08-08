# app/api/waitlist.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import Waitlist as WaitlistSchema
from app.services.firebase_service import add_user_to_firebase

router = APIRouter()

@router.post("/", status_code=201)
def register_waitlist(user: WaitlistSchema):
    try:
        add_user_to_firebase(user.dict())
        return {"message": "Added to waitlist"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add to waitlist: {e}")
