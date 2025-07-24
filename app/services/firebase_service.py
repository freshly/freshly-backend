import os

# ↳ only needed once in your whole program; doing it here is convenient
from dotenv import load_dotenv
load_dotenv()

from firebase_admin import credentials, initialize_app, firestore

# read the path out of an env-var instead of hard-coding it
cred_path = os.getenv("FIREBASE_CREDENTIALS")      # set in .env
if not cred_path:
    raise RuntimeError(
        "FIREBASE_CREDENTIALS environment variable is not set. "
        "Add it to your .env (e.g. FIREBASE_CREDENTIALS=app/services/firebase_key.json)"
    )

cred = credentials.Certificate(cred_path)
initialize_app(cred)
db = firestore.client()


def add_user_to_firebase(user_data):
    """Add a new user to the Firebase database."""
    users_ref = db.collection('users')
    users_ref.add(user_data)

def get_users_from_firebase():
    """Retrieve all users from the Firebase database."""
    users_ref = db.collection('users')
    return users_ref.stream()