from flask import Flask
from redis import Redis
from .celery import make_celery

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

    # Initialize Redis
    app.redis = Redis(host='localhost', port=6379, db=0)

    # Initialize Celery
    celery = make_celery(app)

    # Import routes after Celery is initialized
    from .routes import main
    app.register_blueprint(main)

    return app, celery