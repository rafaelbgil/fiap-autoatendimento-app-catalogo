from src.domain.entities.Produto import Produto
from .interfaces.ProdutoDaoInterface import ProdutoDaoInterface

class UseCaseProduto:
    @staticmethod
    def obter_lista_produtos(repository_produto: ProdutoDaoInterface) -> list[Produto]:
        return repository_produto.listar_produto()
    
    @staticmethod
    def obter_lista_produto_por_categoria(repository_produto: ProdutoDaoInterface, categoria_nome: str) -> list[Produto]:
        return repository_produto.listar_produto_por_categoria(categoria_nome=categoria_nome)
    
    @staticmethod
    def obter_produto(repository_produto: ProdutoDaoInterface, id: str) -> Produto:
        return repository_produto.obter_produto(id=id)
    
    @staticmethod
    def criar_produto(repository_produto: ProdutoDaoInterface, produto: Produto) -> Produto:
        return repository_produto.adicionar_produto(produto=produto)
    
    @staticmethod
    def atualizar_produto(repository_produto: ProdutoDaoInterface, produto: Produto, id: str) -> Produto:
        return repository_produto.atualizar_produto(produto=produto, id=id)

    @staticmethod
    def remover_produto(repository_produto: ProdutoDaoInterface, id: str) -> bool:
        return repository_produto.remover_produto(id=id)