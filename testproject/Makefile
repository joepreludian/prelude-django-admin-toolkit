.DEFAULT_GOAL := run

install:
	poetry install

run:
	PYTHONUNBUFFERED=1 poetry run honcho start

test:
	poetry run pytest --cov prelude_django_admin_toolkit

behave:
	poetry run python manage.py behave
