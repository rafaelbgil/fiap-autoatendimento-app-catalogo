from .Categoria import Categoria


class Produto:
    id: int | None
    categoria: Categoria | int
    nome: str | None
    descricao: str | None
    preco: float | None
    imagem_url: str | None

    def __init__(self, nome, descricao, preco,categoria, id=None, imagem_url=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.id = id
        self.categoria = categoria
        self.imagem_url = imagem_url
