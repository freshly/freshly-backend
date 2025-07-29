from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.services.email_service import send_contact_email

router = APIRouter()

class ContactIn(BaseModel):
    first_name: str
    last_name:  str
    email:      EmailStr
    message:    str

@router.post("/")
async def submit_contact(form: ContactIn):
    try:
        send_contact_email(
            form.first_name,
            form.last_name,
            form.email,
            form.message,
        )
    except Exception as e:
        raise HTTPException(500, detail="Failed to send email")
    return {"status": "ok"}
