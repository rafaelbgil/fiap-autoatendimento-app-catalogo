from uuid import UUID


class Categoria:
    id: UUID | None
    nome: str

    def __init__(self, nome=None, id=None):
        self.nome = nome
        self.id = id
