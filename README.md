
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

## Running the app
* Using docker: `docker-compose up -d` docker will spin up a database, run the db migrations and start the api
* Without docker: `python -m alembic upgrade head && python -m uvicorn app.main:app --reload`
* Note, without docker you will need to adjust various environment settings to connect to a local test database.
