from flask import Blueprint, request, jsonify
from .tasks import send_notification, send_email_notification

main = Blueprint('main', __name__)

@main.route('/notify', methods=['POST'])
def notify():
    if request.is_json:
        data = request.get_json()

        # You can trigger async notification task here (if using Celery)
        send_notification.delay(data)

        return jsonify({"message": "Notification received", "data": data}), 200
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

@main.route('/send-email', methods=['POST'])
def send_email():
    if request.is_json:
        data = request.get_json()
        email = data.get("email")
        subject = data.get("subject")
        body = data.get("body")

        if not (email and subject and body):
            return jsonify({"error": "Missing email, subject or body"}), 400

        # Trigger Celery email notification
        send_email_notification.delay(email, subject, body)

        return jsonify({"message": "Email notification queued", "email": email}), 200
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415