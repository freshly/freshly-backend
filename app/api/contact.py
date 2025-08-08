# app/api/contact.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import ContactForm as ContactIn
from app.services.email_service import send_contact_email
import traceback

router = APIRouter()

@router.post("/", status_code=201)
async def submit_contact(form: ContactIn):
    try:
        await send_contact_email(form.first, form.last, form.email, form.message)
        return {"status": "ok"}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")
