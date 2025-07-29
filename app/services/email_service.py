import smtplib
from email.message import EmailMessage
from app.config import settings

def send_contact_email(first_name: str, last_name: str, sender_email: str, message: str):
    msg = EmailMessage()
    msg["Subject"] = "📨 New Contact Form Submission"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = settings.EMAIL_TO
    msg.set_content(f"""
You’ve got a new message from your website contact form:

First name: {first_name}
Last name: {last_name}
Email: {sender_email}

Message:
{message}
""")

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
        smtp.send_message(msg)
