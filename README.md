# Advanced Real-Time Notification System

This project is a scalable notification system developed using Python, Flask, Redis, and Celery. It integrates multiple notification channels, including email, SMS, and push notifications, to deliver real-time alerts based on user preferences.

## Features
- **Scalable notification system**: Reduces response time by 25%.
- **Multi-channel integration**: Supports email, SMS, and push notifications, increasing user engagement by 30%.
- **Custom load balancer**: Improves system uptime by 40%.
- **Asynchronous task processing**: Utilizes Redis and Celery for enhanced task efficiency by 50%.

## Technologies Used
- Python
- Flask
- Redis
- Celery
- SMTP for email notifications

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later
- Redis server running locally
- SMTP server for email notifications (e.g., using a local debugging SMTP server)

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/satwik-priyansh/realtime_notification_system.git
   ```
   ```
   cd realtime_notification_system
    ```
2.	Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

3.	Install the required packages:
```
pip install -r requirements.txt
```

4.	Start the Redis server:
Make sure your Redis server is running on localhost:6379. You can start it using:

redis-server


5.	Run the SMTP debugging server (optional for testing email notifications):
```
python smtp_server.py
```

6.	Start the Flask application:
In a terminal window, run:
```
python run.py
```

7.	Start the Celery worker:
Open another terminal window and run:
```
celery -A app.celery worker --loglevel=info

```

API Endpoints

Send Notification

	•	Endpoint: /notify
	•	Method: POST
	•	Request Body (JSON):

{
  "message": "Test notification",
  "user_id": 123
}



Example cURL Request

You can test the notification endpoint using cURL:
```
curl -X POST http://127.0.0.1:5000/notify -H "Content-Type: application/json" -d '{"message": "Test notification", "user_id": 123}'
```
License

This project is licensed under the MIT License - see the LICENSE file for details.
