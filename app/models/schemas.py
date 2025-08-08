from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactForm(BaseModel):
    first: str
    last: str
    email: EmailStr
    message: str

class Waitlist(BaseModel):
    email: EmailStr