from abc import ABC, abstractmethod
from domain.entities.Categoria import Categoria
from uuid import UUID

class CategoriaGateway(ABC):
    @staticmethod
    @abstractmethod
    def listar_categorias():
        pass

    @staticmethod
    @abstractmethod
    def obter_categoria_por_id(id: UUID):
        pass

    @staticmethod
    @abstractmethod
    def obter_categoria_por_nome(nome: str):
        pass

    @staticmethod
    @abstractmethod
    def adicionar_categoria(categoria: Categoria):
        pass

    @staticmethod
    @abstractmethod
    def atualizar_categoria(id: int, categoria: Categoria):
        pass

    @staticmethod
    @abstractmethod
    def remover_categoria_por_id(id: UUID):
        pass
