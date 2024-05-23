runserver:
	python3 manage.py runserver

docker-compose-run:
	docker-compose up --build -d

tests:
	docker-compose exec -T app python3 manage.py test

clean-up:
	docker-compose down --volumes

coverage:
	coverage run --source='.' manage.py test
	coverage report

workers:
	celery -A config worker -l INFO

celery-beat:
	celery -A config beat --loglevel=info