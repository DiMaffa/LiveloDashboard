from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    id: int = None
    nome: str
    preco: float

produtos = []
ultimo_id = 0

@app.get("/")
def root():
    return {"status": "online"}

@app.get("/ofertas")
def listar_ofertas():
    return []

@app.post("/produtos")
def criar_produto(item: Produto):
    global ultimo_id
    ultimo_id += 1
    item.id = ultimo_id
    produtos.append(item)
    return item

@app.get("/produtos")
def obter_produtos():
    return produtos

