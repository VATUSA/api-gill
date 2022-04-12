
# VATUSA API

## Dev Requirements
 * Python 3.10
 * Docker
 * virtualenv

## Setup
1. Create virtualenv: `python -m venv venv`
2. Activate virtualenv: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install pre-commit hooks: `pre-commit install`

## Development
* Add a migration: `python -m alembic revision --autogenerate -m "Added ..."`, migrations will automaticlly be run by docker-compose.
* Create tests for any code possible. Run tests with `pytest --cache-clear --cov=app tests > coverage.txt`, include the coverage report in commits.
* I'd recommend just using the database for active development, especially if you use WSL, and only use the full api and postgres compose setup for all up testing.

## Running the app
* Using docker: `docker-compose up -d --force-recreate` docker will spin up a database, run the db migrations and start the api
* Without docker: `python -m alembic upgrade head && python -m uvicorn app.v1.main:api --reload`
* Note, without docker you will need to adjust various environment settings to connect to a local test database.
