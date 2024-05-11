from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProdutoSerializer
from src.db.ProdutoDaoOrm import ProdutoDaoOrm
from src.domain.usecases.useCaseProduto import UseCaseProduto


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
