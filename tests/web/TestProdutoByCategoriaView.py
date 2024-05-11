import unittest
from unittest.mock import Mock, patch

from src.domain.entities.ProdutoFactory import ProdutoFactory
from src.domain.usecases.useCaseProduto import UseCaseProduto
from django.test import Client


class TestProdutoByCategoriaViw(unittest.TestCase):
    @patch('src.web.ProdutoByCategoriaView.UseCaseProduto')
    def test_obter_produto_por_categoria(self, mock_view):
        dicionario_produto_1 = {
            'id': '28169329-d22a-4f35-be06-51120a3466a3',
            'descricao': 'Descricao do produto de teste',
            'nome': 'Produto de Teste1',
            'preco': 10.90,
            'imagem_url': 'http://teste.com.br/teste',
            'id_categoria': '28169329-d22a-4f35-be06-51120a3466a4'
        }
        dicionario_produto_2 = {
            'id': '28169329-d22a-4f35-be06-51120a3466a5',
            'descricao': 'Descricao do produto de teste',
            'nome': 'Produto de Teste2',
            'preco': 10.90,
            'imagem_url': 'http://teste.com.br/teste',
            'id_categoria': '28169329-d22a-4f35-be06-51120a3466a6'
        }
        produto1 = ProdutoFactory.from_dict(dicionario_produto_1)
        produto2 = ProdutoFactory.from_dict(dicionario_produto_2)
        lista_produtos = [produto1, produto2]

        mock_view.obter_lista_produto_por_categoria.return_value = lista_produtos

        client = Client()
        response = client.get('/produto/findByCategoria/lanche/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], '28169329-d22a-4f35-be06-51120a3466a3')
