# app/main.py
import os, uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.contact import router as contact_router
from app.api.waitlist import router as waitlist_router

app = FastAPI(title="Freshly Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# now your contact endpoint lives at /api/contact
app.include_router(contact_router, prefix="/api/contact", tags=["contact"])
app.include_router(waitlist_router, prefix="/api/waitlist", tags=["waitlist"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Freshly Backend API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
