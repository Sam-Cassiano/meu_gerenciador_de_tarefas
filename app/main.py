from fastapi import FastAPI
from app.routes import tasks
from app.database import engine, Base

# Cria tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Inclui rotas
app.include_router(tasks.router)
