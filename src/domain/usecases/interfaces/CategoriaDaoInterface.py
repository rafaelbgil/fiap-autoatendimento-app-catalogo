from abc import ABC, abstractmethod
from src.domain.entities.Categoria import Categoria
from uuid import UUID


class CategoriaDaoInterface(ABC):
    @staticmethod
    @abstractmethod
    def obter_categoria(id: UUID) -> Categoria:
        pass

    @staticmethod
    @abstractmethod
    def remover_categoria(id: UUID) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def adicionar_categoria(categoria: Categoria):
        pass

    @staticmethod
    @abstractmethod
    def listar_categorias() -> list[Categoria]:
        pass
