from fastapi import FastAPI

app = FastAPI()

from rotas_autenticacao import roteador_autenticacao
from rotas_pedidos import roteador_pedidos

app.include_router(roteador_autenticacao)
app.include_router(roteador_pedidos)


#para rodar o nosso codigo, executar no terminal uvicorn main:app --reload




#get -> leitura/pegar
#post -> enviar/criar
#patch/put -> edição
#delete -> deletar