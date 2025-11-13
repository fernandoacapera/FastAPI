from fastapi import APIRouter

roteador_pedidos = APIRouter(prefix='/pedidos', tags=['pedidos'])

@roteador_pedidos.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema.
    Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem":"Você acessou a rota de pedidos"}