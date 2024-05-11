from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategoriaSerializer
from src.db.CategoriaDaoOrm import CategoriaDaoOrm
from src.domain.usecases.UseCaseCategoria import UseCaseCategoria


class CategoriaDetalhesView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(summary='Obtém dados de categoria selecionada', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": "42f0ad6e-b5a2-4b40-940b-51d4c62a9b24",
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
