# VATUSA API

## Dev Requirements

- Python 3.10
- Docker
- virtualenv

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

### Docker

```bash
$> docker-compose up -d
```

### Without Docker

This project uses a Makefile to define make "targets" which are really just scripts that run.

```bash
$> make migrate # runs all migrations
$> make server # runs local server
$> make dev # runs migrate and server together
$> make rollback # rolls back all migrations
```
