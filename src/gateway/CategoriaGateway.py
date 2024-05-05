from abc import ABC
from src.domain.usecases.interfaces.CategoriaDaoInterface import CategoriaDaoInterface


class CategoriaGateway(CategoriaDaoInterface, ABC):
    pass
