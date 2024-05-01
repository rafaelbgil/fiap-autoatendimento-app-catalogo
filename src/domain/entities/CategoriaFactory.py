from .Categoria import Categoria
from src.uitls.validar_uuid import validar_uuid

def _validar_nome_categoria(nome: str) -> str:
    if len(nome) > 40:
        raise AttributeError('Excedido o tamanho máximo de caracteres para categoria(max: 40).')
    if len(nome) == 0:
        raise AttributeError('Nome da categoria definido como vazio.')
    return nome


class CategoriaFactory:
    @staticmethod
    def from_dict(dicionario_categoria: dict) -> Categoria:
        if 'nome' in dicionario_categoria:
            nome = _validar_nome_categoria(dicionario_categoria['nome'])
        else:
            raise AttributeError('Nome da categoria não preenchido.')
        
        id = None
        if 'id' in dicionario_categoria:
            id = validar_uuid(dicionario_categoria['id'])
        
        return Categoria(nome=nome, id=id)