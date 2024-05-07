runserver:
	python3 manage.py runserver

coverage:
	coverage run --source='.' manage.py test

report:
	coverage report