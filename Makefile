celery:
	celery -A core worker --loglevel=info --pool=solo

flower:
	celery -A core flower --port=5001

run:
	python manage.py runserver