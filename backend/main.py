from fastapi import FastAPI
from app.api.api_router import api_router
from app.db.session import engine, Base

# Створюємо таблиці (для демо; у продакшні використовуємо Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Event Platform API', version='0.1.0')

# Підключаємо всі роутери
app.include_router(api_router, prefix='/api')

@app.get('/ping')
def ping():
    return {'ping': 'pong'}

