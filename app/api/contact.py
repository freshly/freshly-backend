from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ContactForm(BaseModel):
    name: str
    email: str
    message: str
    phone: Optional[str] = None

@router.post("/contact")
async def submit_contact_form(contact: ContactForm):
    # Here you would typically handle the contact form submission,
    # such as sending an email or storing it in a database.
    return {"message": "Contact form submitted successfully", "data": contact}