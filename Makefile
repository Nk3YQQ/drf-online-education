run:
	docker-compose up --build -d

entrypoint:
	python3 manage.py migrate --no-input
	python3 manage.py cmg
	python3 manage.py csu
	python3 manage.py createmoderator
	python3 manage.py runserver 0.0.0.0:8000

tests:
	docker-compose exec -T app python3 manage.py test

linters:
	docker-compose exec -T app flake8 payment/
	docker-compose exec -T app flake8 service/
	docker-compose exec -T app flake8 users/

stop:
	docker-compose down

clean:
	docker-compose down --volumes

coverage:
	coverage run --source='.' manage.py test
	coverage report

worker:
	celery -A config worker -l INFO

beat:
	celery -A config beat --loglevel=info