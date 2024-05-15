from behave import *
from unittest.mock import Mock
from json import loads

from src.domain.entities.Categoria import Categoria
from src.domain.entities.CategoriaFactory import CategoriaFactory
from src.domain.usecases.UseCaseCategoria import UseCaseCategoria


@given(u'que foram informados os dados para criacao da categoria')
def step_impl(context):
    context.categoria = CategoriaFactory.from_dict(loads(context.text))


@given(u'após a validação os dados estão corretos')
def step_impl(context):
    assert (isinstance(context.categoria, Categoria))


@when(u'a rotina de criação de catalogo for executada')
def step_impl(context):
    dicionario_categoria = {
        "nome": context.categoria.nome,
        "id": "3a95b89e-7ee7-4c4d-a09a-d6674b93701e"
    }
    print(dicionario_categoria)
    mock = Mock()
    UseCaseCategoria = mock
    context.categoria_nova = UseCaseCategoria.criar_categoria.return_value = CategoriaFactory.from_dict(
        dicionario_categoria=dicionario_categoria)


@then(u'será retornado o id do catalogo e suas informações')
def step_impl(context):
    print(context.categoria_nova.__dict__)
    return context.categoria_nova
