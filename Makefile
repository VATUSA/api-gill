dev: migrate server

migrate:
	python -m alembic upgrade head

server:
	python -m uvicorn appv3..main\:api --reload

rollback:
	python -m alembic downgrade base

lint:
	python -m pre-commit run --all-files

test:
	python -m pytest --cache-clear --cov=app tests > coverage.txt
