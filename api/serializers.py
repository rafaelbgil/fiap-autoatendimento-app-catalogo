from rest_framework import serializers
from .models import Categoria, Produto


class CategoriaSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)


class ProdutoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=40)
    preco = serializers.FloatField()
    id_categoria = serializers.UUIDField(required=False)
    descricao = serializers.CharField(max_length=1024, required=False)
    imagem_url = serializers.CharField(max_length=1024, required=False)
