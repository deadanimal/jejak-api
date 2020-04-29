web: gunicorn jejakapi.wsgi -w 4 --max-requests 100
worker: celery -A  jejakapi worker --concurrency=8 -Ofair
beat: celery -A jejakapi beat
