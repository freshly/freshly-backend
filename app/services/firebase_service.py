import os
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app, firestore

# Load .env
load_dotenv()

# Initialize Firebase
cred_path = os.getenv("FIREBASE_CREDENTIALS")
if not cred_path:
    raise RuntimeError(
        "FIREBASE_CREDENTIALS environment variable is not set. "
        "Add it to your .env (e.g. FIREBASE_CREDENTIALS=app/services/firebase_key.json)"
    )

cred = credentials.Certificate(cred_path)
initialize_app(cred)
db = firestore.client()

def add_user_to_firebase(user_data: dict):
    email = user_data["email"].strip().lower()
    db = firestore.client()
    db.collection("waitlist").document(email).set(
        {
            "email": email,
            "createdAt": firestore.SERVER_TIMESTAMP,
        },
        merge=True,  # upsert; safe if they re-submit
    )

def get_waitlist_entries():
    """
    Retrieve all entries from the 'waitlist' collection.
    """
    waitlist_ref = db.collection("waitlist")
    return waitlist_ref.stream()
