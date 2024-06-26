from src.domain.entities.ProdutoFactory import ProdutoFactory
from src.domain.usecases.interfaces.ProdutoDaoInterface import ProdutoDaoInterface
from api.models import Produto as ProdutoModel
from api.models import Categoria as CategoriaModel
from src.domain.entities.Produto import Produto
from src.uitls.validar_uuid import validar_uuid


class ProdutoDaoOrm(ProdutoDaoInterface):
    @staticmethod
    def obter_produto(id: str) -> Produto:
        try:
            produto_orm = ProdutoModel.objects.get(id=validar_uuid(id))
        except:
            raise Exception('Produto nao encontrado')

        produto = ProdutoFactory.from_dict(dicionario_produto=produto_orm.__dict__)
        if produto_orm.categoria:
            produto.id_categoria = produto_orm.categoria.id
        produto.id = produto_orm.id

        return produto

    @staticmethod
    def listar_produto() -> list[Produto]:
        produtos_queryset = ProdutoModel.objects.all()
        lista_produtos = []

        if not produtos_queryset:
            return lista_produtos

        for produto_orm in produtos_queryset:
            produto = ProdutoFactory.from_dict(dicionario_produto=produto_orm.__dict__)
            produto.id_categoria = produto_orm.categoria_id
            lista_produtos.append(produto)

        return lista_produtos

    @staticmethod
    def listar_produto_por_categoria(categoria_nome: str) -> list[Produto]:
        try:
            categoria_orm = CategoriaModel.objects.get(nome__iexact=categoria_nome)
        except:
            raise Exception('Categoria não encontrada')

        list_produtos_orm = categoria_orm.produto_set.all()
        lista_produtos = []
        for produto_orm in list_produtos_orm:
            produto = produto_orm.__dict__
            produto['id_categoria'] = produto_orm.categoria_id
            #lista_produtos.append(ProdutoFactory.from_dict(dicionario_produto=produto_orm.__dict__))
            lista_produtos.append(ProdutoFactory.from_dict(dicionario_produto=produto))

        return lista_produtos

    @staticmethod
    def adicionar_produto(produto: Produto) -> Produto:
        categoria = None
        if produto.id_categoria:
            try:
                categoria = CategoriaModel.objects.get(id=produto.id_categoria)
            except:
                raise Exception('Categoria não foi encontrada.')

        produto_orm = ProdutoModel()
        for atributo in produto.__dict__.keys():
            if produto.__dict__[atributo] and produto.__dict__[atributo] != 'None':
                if atributo in produto_orm.__dict__:
                    produto_orm.__setattr__(atributo, produto.__dict__[atributo])
        produto_orm.categoria = categoria
        try:
            produto_orm.save()
        except Exception as erro:
            raise Exception('Não foi possível adicionar o produto.')

        if produto_orm.categoria_id:
            produto.id_categoria = produto_orm.categoria_id

        if produto_orm.id:
            produto.id = produto_orm.id

        return produto

    @staticmethod
    def remover_produto(id: str) -> bool:
        try:
            produto = ProdutoModel.objects.get(id=validar_uuid(id))
        except:
            raise Exception('Id de produto não encontrado.')

        try:
            produto.delete()
        except:
            raise Exception('Não foi possível remover o produto')

        return True

    @staticmethod
    def atualizar_produto(produto: Produto, id: str) -> Produto:
        categoria = None
        if produto.id_categoria:
            categoria = CategoriaModel.objects.get(id=validar_uuid(produto.id_categoria))
        produto_orm = ProdutoModel.objects.get(id=validar_uuid(id))
        for atributo in produto.__dict__.keys():
            if produto.__dict__[atributo] and produto.__dict__[atributo] != 'None':
                if atributo in produto_orm.__dict__:
                    produto_orm.__setattr__(atributo, produto.__dict__[atributo])

        if categoria:
            produto_orm.categoria = categoria
        produto_orm.save(force_update=True)

        produto_atualizado = ProdutoFactory.from_dict(dicionario_produto=produto_orm.__dict__)
        if categoria:
            produto_atualizado.id_categoria = validar_uuid(produto.id_categoria)
        return produto_atualizado
