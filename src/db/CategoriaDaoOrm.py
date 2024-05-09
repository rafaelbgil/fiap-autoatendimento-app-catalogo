from src.gateway.CategoriaGateway import CategoriaGateway
from src.domain.entities.Categoria import Categoria
from src.domain.entities.CategoriaFactory import CategoriaFactory
from api.models import Categoria as CategoriaModel
from uuid import UUID


class CategoriaDaoOrm(CategoriaGateway):
    @staticmethod
    def obter_categoria(id: str) -> Categoria:
        try:
            id_uuid = UUID(id)
        except:
            raise AttributeError(
                'Código de categoria inválido, favor informar um número.')

        try:
            categoria_queryset = CategoriaModel.objects.get(id=id_uuid)
        except:
            raise Exception('Categoria não encontrada.')

        return CategoriaFactory.from_dict(categoria_queryset.__dict__)

    @staticmethod
    def remover_categoria(id: int) -> bool:
        try:
            categoria_queryset = CategoriaModel.objects.get(id=id)
            categoria_queryset.delete()
        except:
            raise Exception(
                'Categoria não foi encontrada ou não pode ser removida. Verifique o código informado.')
        return True

    @staticmethod
    def adicionar_categoria(categoria: Categoria):
        categoria_orm = CategoriaModel()
        for atributo in categoria.__dict__.keys():
            if categoria.__dict__[atributo] and categoria.__dict__[atributo] != 'None':
                categoria_orm.__setattr__(
                    atributo, categoria.__dict__[atributo])
        try:
            categoria_orm.save()
        except Exception as error:
            raise Exception('Não foi possível adicionar a categoria. %s' % (error.__str__()))

        categoria.id = categoria_orm.id
        return categoria

    @staticmethod
    def listar_categorias() -> list[Categoria]:
        categorias_queryset = CategoriaModel.objects.all()
        categorias = []
        for categoria in categorias_queryset:
            categorias.append(CategoriaFactory.from_dict(
                dicionario_categoria=categoria.__dict__))

        return categorias
