from django.db import models
from uuid import uuid4

# Create your models here.


class Categoria(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=40, blank=False, unique=True)
    objects = models.Manager()

class Produto(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=40, null=False)
    descricao = models.CharField(max_length=1024, null=True)
    preco = models.FloatField(null=False)
    imagem_url = models.CharField(max_length=1024, null=True)
    categoria = models.ForeignKey(
        to=Categoria, on_delete=models.CASCADE, null=True)

    objects = models.Manager()