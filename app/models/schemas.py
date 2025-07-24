from pydantic import BaseModel
from typing import Optional

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

class User(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    phone: Optional[str] = None