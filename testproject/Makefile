.DEFAULT_GOAL := run

install:
	poetry install

run:
	PYTHONUNBUFFERED=1 poetry run honcho start

test:
	poetry run python manage.py test

behave:
	poetry run python manage.py behave
