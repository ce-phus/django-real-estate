# an if block where we can initiate env file
ifneq (,$(wildcarrd ./.env))
include .env 
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

show-logs:
	docker-compose logs

migrate:
	docker-compose exec api python3 manage.py makemigrations

makemigrations:
	docker-compose exec api python3 manage.py makemigrations

superuser:
	docker-compose exec api python3 manage.py createsuperuser

collectstatic:
	docker-compose exec api python3 manage.py collectstatic --no-input --clear

# brings down containers and removes all the volume
down -v:
	docker-compose down -v

# inspect my postgres volume
volume:
	docker volume inspect real_estate_postgres_data

estate-db:
	docker-compose exec postgres-db psql --username=postgres --dbname=real_estate

# testing our application, gets a report on the terminal
test:
	docker compose exec api pytest -p no:warnings --cov=.

# generating an html for our test application
test-html:
	docker-compose exec api pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker-compose exec api flake8.

# checking for any formatting issues
black-check:
	docker-compose exec api black --check --exclude=migrations .

# check after al the formating is done
black-diff:
	docker-compose exec api black --diff --exclude=migrations .

black:
	docker-compose exec api black --exclude=migrations

isort-check:
	docker-compose exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker-compose exec api isort . --check-only --skip migrations

isort:
	docker-compose exec api isort . --skip env --skip migrations