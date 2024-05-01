from fastapi import FastAPI
from ..domain.entities.CategoriaFactory import CategoriaFactory
from ..domain.entities.Produto import Produto
from .basemodel.Models import CategoriaBaseModel, ProdutoBaseModelAdd

from src.db.database import engine, SessionLocal
from src.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/categoria")
async def get_categoria():
    return {"message": "Hello World"}

@app.post("/categoria")
async def post_categoria(categoria: CategoriaBaseModel):
    print(categoria.model_dump())
    categoria_validada = CategoriaFactory.from_dict(dicionario_categoria=categoria.model_dump())
    return {"message": categoria_validada}

@app.get("/categoria/{categoria_id}")
async def get_categoria_id(categoria_id : int):
    return {"message" : categoria_id}

@app.put("/categoria/{categoria_id}")
async def put_categoria_id(categoria_id : int):
    return {"message" : categoria_id}

@app.delete("/categoria/{categoria_id}")
async def delete_categoria_id(categoria_id : int):
    return {"message" : categoria_id}

@app.get("/produto")
async def get_produto():
    return {"message": "Hello World"}

@app.post("/produto")
async def post_produto(produto: ProdutoBaseModelAdd):
    return {"message": "Hello World"}

@app.get("/produto/{produto_id}")
async def get_produto_id(produto_id: int):
    return {"message": "Hello World"}

@app.put("/produto/{produto_id}")
async def put_produto_id(produto_id: int):
    return {"message": "Hello World"}

@app.delete("/produto/{produto_id}")
async def delete_produto_id(produto_id: int):
    return {"message": "Hello World"}

@app.get('/produto/findByCategoria/{categoria}')
async def get_produto_by_categoria(categoria: str):
    return {"message": "Hello World"}