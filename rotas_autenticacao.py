from fastapi import APIRouter

roteador_autenticacao = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@roteador_autenticacao.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado":False}