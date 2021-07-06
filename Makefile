build:
	pip install -U pip
	pip install -r requirements.txt
	python manage.py migrate

build-dev: build
	pip install -r dev-requirements.txt

clean-pyc:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

lint:
	flake8

test: clean-pyc
	python manage.py test

run:
	python manage.py runserver