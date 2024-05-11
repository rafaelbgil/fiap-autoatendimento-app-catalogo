import unittest
from unittest.mock import Mock, patch
from src.domain.entities.ProdutoFactory import ProdutoFactory
from django.test import Client
class TestProdutoDetalhesView(unittest.TestCase):
    @patch('src.web.ProdutoDetalhesView.UseCaseProduto')
    def test_obter_produto(self, mock_use_case_produto):
        dicionario_produto = {
            'id': '28169329-d22a-4f35-be06-51120a3466a3',
            'descricao': 'Descricao do produto de teste',
            'nome': 'Produto de Teste1',
            'preco': 10.90,
            'imagem_url': 'http://teste.com.br/teste',
            'id_categoria': '28169329-d22a-4f35-be06-51120a3466a4'
        }
        produto = ProdutoFactory.from_dict(dicionario_produto)

        mock_use_case_produto.obter_produto.return_value(produto)

        client = Client()
        response = client.get('/produto/28169329-d22a-4f35-be06-51120a3466a3/')
        self.assertEqual(response.status_code, 200)

    @patch('src.web.ProdutoDetalhesView.UseCaseProduto')
    def test_remover_produto(self, mock_use_case_produto):
        mock_use_case_produto.remover_produto.return_value = True
        client = Client()
        response = client.delete('/produto/28169329-d22a-4f35-be06-51120a3466a3/')
        self.assertEqual(response.status_code, 200)

    @patch('src.web.ProdutoDetalhesView.UseCaseProduto')
    def test_atualizar_produto(self, mock_use_case_produto):
        dicionario_produto = {
            'id': '28169329-d22a-4f35-be06-51120a3466a3',
            'descricao': 'Descricao do produto de teste',
            'nome': 'Produto de Teste1',
            'preco': 10.90,
            'imagem_url': 'http://teste.com.br/teste',
            'id_categoria': '28169329-d22a-4f35-be06-51120a3466a4'
        }
        mock_use_case_produto.atualizar_produto.return_value = dicionario_produto
        client = Client()
        response = client.put('/produto/28169329-d22a-4f35-be06-51120a3466a3/')
        self.assertEqual(response.status_code, 200)