from . import celery

@celery.task
def send_notification(data):
    print(f"Sending notification: {data}")

import smtplib
from email.mime.text import MIMEText

@celery.task
def send_email_notification(email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'you@example.com'
    msg['To'] = email

    try:
        # Use the local SMTP server for testing
        s = smtplib.SMTP('localhost', 1025)
        s.send_message(msg)
        s.quit()
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")