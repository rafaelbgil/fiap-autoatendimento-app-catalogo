from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CategoriaSerializer, ProdutoSerializer
from src.presenters.FormatCategoria import FormatCategoria
from src.presenters.FormatProduto import FormatProduto

from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse

from src.domain.entities.CategoriaFactory import CategoriaFactory
from src.domain.usecases.UseCaseCategoria import UseCaseCategoria
from src.domain.usecases.useCaseProduto import UseCaseProduto
from src.db.CategoriaDaoOrm import CategoriaDaoOrm
from src.db.ProdutoDaoOrm import ProdutoDaoOrm
from src.domain.entities.ProdutoFactory import ProdutoFactory


class CategoriaView(APIView):
    serializer_class = CategoriaSerializer
    """
    Api para gerenciamento de categorias
    """

    @extend_schema(responses=CategoriaSerializer(many=True), summary='Obtém lista de categorias', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "doces"},
                       request_only=False,
                       response_only=True,
                       )
    ])
    def get(self, request, format=None):
        """
        Api para listar categorias
        """
        categorias = UseCaseCategoria.obter_lista_categoria(repository_categoria=CategoriaDaoOrm)
        serializer = CategoriaSerializer(data=categorias, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Adiciona nova categoria', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "salgados"},
                       request_only=False,
                       response_only=True,
                       ),

        OpenApiExample('Exemplo de uso',
                       value={"nome": "salgados"},
                       request_only=True,
                       response_only=False,
                       )
    ])
    def post(self, request, format=None):
        """
        Api para adicionar categoria
        """

        try:
            categoria = UseCaseCategoria.criar_categoria(
                repository_categoria=CategoriaDaoOrm, categoria=CategoriaFactory.from_dict(request.data))
        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CategoriaSerializer(
            data=FormatCategoria.from_categoria_to_dict(categoria=categoria))

        try:
            if not serializer.is_valid():
                return Response({'status': 'erro', 'detalhes': serializer._errors}, status=status.HTTP_400_BAD_REQUEST)


        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': 'Não foi possível cadastrar a nova categoria.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=FormatCategoria.from_categoria_to_dict(categoria=categoria),
                        status=status.HTTP_201_CREATED)


class CategoriaDetalhesView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(summary='Obtém dados de categoria selecionada', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "salgados"},
                       request_only=False,
                       response_only=True,
                       )
    ])
    def get(self, request, id: str, format=None):
        """
        Obtém dados de categoria selecionada
        """
        try:
            categoria = UseCaseCategoria.obter_categoria(repository_categoria=CategoriaDaoOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(instance=categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Remove categoria selecionada')
    def delete(self, request, id: int, format=None):
        """
        Remove categoria selecionada
        """
        try:
            UseCaseCategoria.remover_categoria(repository_categoria=CategoriaDaoOrm, id=id)
            return Response(data={'status': 'sucesso', 'detalhes': 'Categoria removida com sucesso.'},
                            status=status.HTTP_200_OK)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)


class ProdutoView(APIView):
    serializer_class = ProdutoSerializer
    """
    Api para gerencimamento de produtos
    """

    @extend_schema(responses=ProdutoSerializer(many=True), summary='Obtém lista de produtos')
    def get(self, request, format=None):
        """
        Api para obter lista de **produtos**
        """
        produtos = UseCaseProduto.obter_lista_produtos(
            repository_produto=ProdutoDaoOrm)
        serializer = ProdutoSerializer(instance=produtos, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Adiciona novo produto')
    def post(self, request, format=None):
        """
        Api para cadastrar **produto**
        """
        try:
            produto_ob = ProdutoFactory.from_dict(request.data)
            produto = UseCaseProduto.criar_produto(
                repository_produto=ProdutoDaoOrm, produto=ProdutoFactory.from_dict(dicionario_produto=request.data))
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FormatProduto.from_produto_to_dict(produto), status=status.HTTP_201_CREATED)


class ProdutoDetalhesView(APIView):
    """
    Api para gerenciamento de produto
    """
    serializer_class = ProdutoSerializer

    @extend_schema(summary='Obtém dados de produto selecionado', responses={
        200: OpenApiResponse(description='Json Response'),
        400: OpenApiResponse(description='Validation error')
    })
    def get(self, request, id: str, format=None):
        """
        Api para visualizar dados de produto selecionado
        """
        try:
            produto = UseCaseProduto.obter_produto(
                repository_produto=ProdutoDaoOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProdutoSerializer(instance=produto)
        return Response(serializer.data)

    @extend_schema(summary='Atualiza produto selecionado')
    def put(self, request, id: str, format=None):
        """
        Api para atualizar produto selecionado
        """
        try:
            produto_atualizado = UseCaseProduto.atualizar_produto(
                repository_produto=ProdutoDaoOrm, produto=ProdutoFactory.from_dict(request.data, update=True), id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()})
        return Response(FormatProduto.from_produto_to_dict(produto_atualizado))

    @extend_schema(summary='Remove produto selecionado')
    def delete(self, request, id: str, format=None):
        """
        Api para remover produto selecionado
        """
        try:
            UseCaseProduto.remover_produto(repository_produto=ProdutoDaoOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


class ProdutoByCategoriaView(APIView):
    """
    Api para obter lista de produtos por Categoria
    """

    @extend_schema(summary='Obtém dados de produto selecionado', responses={
        200: OpenApiResponse(description='Lista de Produtos'),
        404: OpenApiResponse(description='Categoria não encontrada')
    })
    def get(self, request, categoria: str, format=None):
        """
        Api para obter lista de produtos por categoria
        """
        try:
            lista_produtos = UseCaseProduto.obter_lista_produto_por_categoria(repository_produto=ProdutoDaoOrm,
                                                                          categoria_nome=categoria)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProdutoSerializer(instance=lista_produtos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)