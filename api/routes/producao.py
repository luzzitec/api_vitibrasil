from fastapi import APIRouter
from api.services.scraper import extrair_tabela_producao

router = APIRouter()

@router.get("/producao")
def get_producao():
    df = extrair_tabela_producao()
    return df.to_dict(orient="records")