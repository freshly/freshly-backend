from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactForm(BaseModel):
    first: str
    last: str
    email: EmailStr
    message: str

class User(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    phone: Optional[str] = None