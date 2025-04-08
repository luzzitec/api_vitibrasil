from fastapi import FastAPI
from api.routes import producao

app = FastAPI(title="API Vitibrasil")

# Inclui as rotas do módulo produção
app.include_router(producao.router, prefix="/api")