from abc import ABC, abstractmethod
from domain.entities.Produto import Produto
from uuid import UUID


class ProdutoGateway(ABC):
    @staticmethod
    @abstractmethod
    def listar_produtos():
        pass

    @staticmethod
    @abstractmethod
    def obter_produto_por_id(id: UUID):
        pass

    @staticmethod
    @abstractmethod
    def adicionar_produto(produto: Produto, categoria_id: UUID):
        pass

    @staticmethod
    @abstractmethod
    def atualizar_produto(id: UUID, produto: Produto):
        pass

    @staticmethod
    @abstractmethod
    def remover_produto_por_id(id: UUID):
        pass
