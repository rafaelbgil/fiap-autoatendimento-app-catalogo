from abc import ABC, abstractmethod
from src.domain.entities.Produto import Produto


class ProdutoDaoInterface(ABC):
    @staticmethod
    @abstractmethod
    def obter_produto(id: str) -> Produto:
        pass

    @staticmethod
    @abstractmethod
    def listar_produto_por_categoria(categoria_nome: str) -> list[Produto]:
        pass

    @staticmethod
    @abstractmethod
    def listar_produto() -> list[Produto]:
        pass

    @staticmethod
    @abstractmethod
    def remover_produto(id: str) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def adicionar_produto(produto: Produto) -> Produto:
        pass

    @staticmethod
    @abstractmethod
    def atualizar_produto(produto: Produto, id: str) -> Produto:
        pass
