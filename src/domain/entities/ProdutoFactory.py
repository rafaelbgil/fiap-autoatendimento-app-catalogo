from .Produto import Produto
from .Categoria import Categoria
from src.uitls.validar_uuid import validar_uuid


def _validar_nome_produto(nome: str, update=False) -> str:
    if len(nome) > 40:
        raise ValueError(
            'Excedido o tamanho máximo de caracteres para o nome(max: 40).')
    if len(nome) == 0 and update == False:
        raise AttributeError('Nome do produto definido como vazio.')
    return nome


def _validar_categoria(categoria: Categoria):
    if isinstance(categoria, Categoria):
        return categoria
    else:
        raise TypeError(
            'Campo categoria não recebeu um objeto do tipo categoria.')


def _validar_descricao_produto(descricao: str) -> str:

    if len(descricao) > 1024:
        raise ValueError(
            'Excedido o tamanho máximo de caracteres para a descricao(max: 1024).')
    return descricao


def _validar_imagem_url_produto(imagem_url: str) -> str:
    if len(imagem_url) > 1024:
        raise ValueError(
            'Excedido o tamanho máximo de caracteres para a descricao(max: 1024).')
    return imagem_url


def _validar_preco_produto(preco: int | float | str, update=False) -> float | None:
    if isinstance(preco, int) or isinstance(preco, float):
        return float(preco)

    if (preco == None or preco == 'None' or len(preco) == 0) and (update == True):
        return None

    if isinstance(preco, str):
        return float(preco.replace(',', '.'))
    else:
        raise AttributeError(
            'Formato de preco inválido, utilize somente inteiros ou float.')


class ProdutoFactory:
    @staticmethod
    def from_dict(dicionario_produto, update=False) -> Produto:
        id = None
        nome = None
        descricao = None
        categoria = None
        preco = None
        imagem_url = None

        nome = _validar_nome_produto(
            nome=dicionario_produto['nome'], update=update)
        descricao = _validar_descricao_produto(
            descricao=dicionario_produto['descricao'])
        preco = _validar_preco_produto(
            preco=dicionario_produto['preco'], update=update)
        imagem_url = _validar_imagem_url_produto(
            imagem_url=dicionario_produto['imagem_url'])

        if 'id' in dicionario_produto:
            id = validar_uuid(dicionario_produto['id'])

        if 'categoria' in dicionario_produto:
            categoria = _validar_categoria(dicionario_produto['categoria'])

        return Produto(id=id, nome=nome, descricao=descricao, preco=preco, categoria=categoria, imagem_url=imagem_url)
