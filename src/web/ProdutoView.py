from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProdutoSerializer
from src.db.ProdutoDaoOrm import ProdutoDaoOrm
from src.domain.entities.ProdutoFactory import ProdutoFactory
from src.domain.usecases.useCaseProduto import UseCaseProduto
from src.presenters.FormatProduto import FormatProduto


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
