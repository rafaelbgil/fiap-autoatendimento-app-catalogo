from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategoriaSerializer
from src.db.CategoriaDaoOrm import CategoriaDaoOrm
from src.domain.entities.CategoriaFactory import CategoriaFactory
from src.domain.usecases.UseCaseCategoria import UseCaseCategoria
from src.presenters.FormatCategoria import FormatCategoria


class CategoriaView(APIView):
    serializer_class = CategoriaSerializer
    """
    Api para gerenciamento de categorias
    """

    @extend_schema(responses=CategoriaSerializer(many=True), summary='Obtém lista de categorias', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": "42f0ad6e-b5a2-4b40-940b-51d4c62a9b24",
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
                       value={"id": "42f0ad6e-b5a2-4b40-940b-51d4c62a9b24",
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
