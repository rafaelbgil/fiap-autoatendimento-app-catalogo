from pydantic import BaseModel


class CategoriaBaseModel(BaseModel):
    nome: str
    
    class Config:
        orm_mode = True


class ProdutoBaseModelAdd(BaseModel):
    id_categoria: int
    nome: str
    descricao: str 
    preco: float 
    imagem_url: str | None

    class Config:
        orm_mode = True
