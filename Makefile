dev: migrate server

migrate:
	python -m alembic upgrade head

server:
	python -m uvicorn app.main\:app --reload

rollback:
	python -m alembic downgrade base
