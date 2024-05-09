import unittest
import uuid

import api.models
from src.db.CategoriaDaoOrm import CategoriaDaoOrm
from src.domain.entities.CategoriaFactory import CategoriaFactory
from src.domain.entities.Categoria import Categoria
from api.models import Categoria as CategoriaModel
from unittest.mock import Mock, patch, MagicMock
import os


class TestCategoriaDaoOrm(unittest.TestCase):

    def test_uuid_tipo_invalido(self):
        self.assertRaises(AttributeError, CategoriaDaoOrm.obter_categoria, 1)

    @patch('src.db.CategoriaDaoOrm.CategoriaModel')
    def test_obter_categoria(self, mock_categoria_model):
        mock_categoria_model_return = Mock()
        mock_categoria_model_return.id = '42f0ad6e-b5a2-4b40-940b-51d4c62a9b24'
        mock_categoria_model_return.nome = 'Bebidas'

        mock_categoria_model.objects.get.return_value = mock_categoria_model_return

        retorno_categoria = CategoriaDaoOrm.obter_categoria('42f0ad6e-b5a2-4b40-940b-51d4c62a9b24')
        self.assertEqual(retorno_categoria.nome, 'Bebidas')
        self.assertIsInstance(retorno_categoria, Categoria)

    @patch('src.db.CategoriaDaoOrm.CategoriaModel')
    def test_remover_categoria(self, mock_categoria_model):
        retorno_remocao = CategoriaDaoOrm.remover_categoria('42f0ad6e-b5a2-4b40-940b-51d4c62a9b24')
        self.assertTrue(retorno_remocao)

    @patch('src.db.CategoriaDaoOrm.CategoriaModel')
    def test_listar_categorias(self, mock_categoria_model):
        categoria1 = CategoriaModel(nome="Bebidas", id='42f0ad6e-b5a2-4b40-940b-51d4c62a9b24')
        categoria2 = CategoriaModel(nome="Doces", id='42f0ad6e-b5a2-4b40-940b-51d4c62a9b25')

        mock_categoria_lista = [categoria1, categoria2]

        mock_categoria_model.objects.all.return_value = mock_categoria_lista
        retorno_lista = CategoriaDaoOrm.listar_categorias()
        self.assertIsInstance(retorno_lista, list)
        self.assertIsInstance(retorno_lista[0], Categoria)
        self.assertEqual(retorno_lista[0].nome, 'Bebidas')
