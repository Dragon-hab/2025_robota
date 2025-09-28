# Event Platform - Back-end (FastAPI)
Demo scaffold for the Event Platform project.

## Stack
- Python 3.10+
- FastAPI
- SQLAlchemy (ORM)
- Pydantic
- Uvicorn
- SQLite for demo (configurable to PostgreSQL)

## Run (development)
1. Create virtualenv: `python -m venv .venv && source .venv/bin/activate`
2. Install deps: `pip install -r requirements.txt`
3. Start server: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

## Notes
- Configuration is read from environment variable `DATABASE_URL`. Default uses SQLite file `./dev.db`.
- For production, point `DATABASE_URL` to a PostgreSQL instance, and use Alembic for migrations.
- JWT secret is set via `SECRET_KEY` env var for demo; change in production.
