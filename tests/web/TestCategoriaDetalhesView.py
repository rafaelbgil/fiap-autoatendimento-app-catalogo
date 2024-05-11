import unittest
from unittest.mock import Mock, patch

from src.domain.entities.Categoria import Categoria
from django.test import Client


class TestCategoriaDetalhesView(unittest.TestCase):
    def setUp(self):
        self.categoria1 = Categoria('Bebidas', '28169329-d22a-4f35-be06-51120a3466a3')
        self.client = Client()

    @patch('src.web.CategoriaDetalhesView.UseCaseCategoria')
    def test_obter_categoria(self, mock_use_case_categoria):
        mock_use_case_categoria.obter_categoria.return_value = self.categoria1
        response = self.client.get(path='/categoria/28169329-d22a-4f35-be06-51120a3466a3/')
        self.assertEqual(response.status_code, 200)

    @patch('src.web.CategoriaDetalhesView.UseCaseCategoria')
    def test_remover_categoria(self, mock_use_case_categoria):
        mock_use_case_categoria.remover_categoria.return_response = True
        response = self.client.delete(path='/categoria/28169329-d22a-4f35-be06-51120a3466a3/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['detalhes'], 'Categoria removida com sucesso.')
