from src.domain.entities.Categoria import Categoria
from src.domain.usecases.interfaces.CategoriaDaoInterface import CategoriaDaoInterface 

class UseCaseCategoria:
    def obter_lista_categoria(repository_categoria: CategoriaDaoInterface) -> list[Categoria]:
        return repository_categoria.listar_categorias()
    
    def obter_categoria(repository_categoria: CategoriaDaoInterface, id: int) -> Categoria:
        return repository_categoria.obter_categoria(id=id)
    
    def criar_categoria(repository_categoria: CategoriaDaoInterface, categoria: Categoria) -> Categoria:
        return repository_categoria.adicionar_categoria(categoria=categoria)
    
    def remover_categoria(repository_categoria: CategoriaDaoInterface, id: int) -> bool:
        return repository_categoria.remover_categoria(id=id)
   