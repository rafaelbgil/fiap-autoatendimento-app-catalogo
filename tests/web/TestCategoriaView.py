import unittest
from unittest.mock import Mock, patch

from src.domain.entities.Categoria import Categoria
from django.test import Client


class TestCategoriaView(unittest.TestCase):
    def setUp(self):
        self.categoria1 = Categoria('Bebidas', '28169329-d22a-4f35-be06-51120a3466a3')
        self.categoria2 = Categoria('lanches', '28169329-d22a-4f35-be06-51120a3466a4')
        self.lista_categorias = [self.categoria1, self.categoria2]

    @patch('src.web.CategoriaView.UseCaseCategoria')
    def test_listar_categorias(self, mock_use_case_categoria):
        mock_use_case_categoria.obter_lista_categoria.return_value = self.lista_categorias
        client = Client()
        response = client.get('/categoria/')
        self.assertEqual(response.json()[0]['id'], '28169329-d22a-4f35-be06-51120a3466a3')
        self.assertEqual(response.status_code, 200)

    @patch('src.web.CategoriaView.UseCaseCategoria')
    def test_criar_categoria(self, mock_use_case_categoria):
        mock_use_case_categoria.criar_categoria.return_value = self.categoria1
        dicionario_categoria = {
            'nome': 'Bebidas'
        }
        client = Client()
        response = client.post('/categoria/', data=dicionario_categoria, content_type='application/json',
                               headers={"accept": "application/json"})

        print(response.content_type)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.json()['id'],'28169329-d22a-4f35-be06-51120a3466a3')
