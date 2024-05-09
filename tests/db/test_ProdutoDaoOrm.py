import unittest
from unittest.mock import Mock, MagicMock, patch

from src.db.ProdutoDaoOrm import ProdutoDaoOrm
from api.models import Produto as ProdutoModel
from api.models import Categoria as CategoriaModel
from src.domain.entities.Produto import Produto


class TestProdutoDaoOrm(unittest.TestCase):

    @patch('src.db.ProdutoDaoOrm.ProdutoModel')
    def test_obter_produto(self, mock_produto_model):
        mock_produto_retorno = Mock()
        mock_produto_retorno.nome = 'Coca Cola'
        mock_produto_retorno.descricao = 'Refrigerante'
        mock_produto_retorno.id_categoria = '6859a83f-7165-4515-a4f4-b061928b5136'
        mock_produto_retorno.preco = 5.9
        mock_produto_retorno.imagem_url = 'http://example.com/imagem'

        mock_produto_model.objects.get.return_value = mock_produto_retorno

        retorno_produto = ProdutoDaoOrm.obter_produto('6859a83f-7165-4515-a4f4-b061928b5137')

        self.assertIsInstance(retorno_produto, Produto)

    @patch('src.db.ProdutoDaoOrm.ProdutoModel')
    def test_lista_produto(self, mock_produto_model):
        produto = ProdutoModel(nome='Coca Cola',
                               categoria=CategoriaModel(nome='refrigerante', id='6859a83f-7165-4515-a4f4-b061928b5136'),
                               id='6859a83f-7165-4515-a4f4-b061928b5137', preco=6.9, descricao='Refrigerante',
                               imagem_url='http://example.com/imagem')
        lista_produto_model = [produto]

        mock_produto_model.objects.all.return_value = lista_produto_model
        lista_produtos = ProdutoDaoOrm.listar_produto()
        self.assertIsInstance(lista_produtos, list)
        self.assertIsInstance(lista_produtos[0], Produto)
        self.assertEqual(lista_produtos[0].nome, 'Coca Cola')
        self.assertEqual(lista_produtos[0].id_categoria, '6859a83f-7165-4515-a4f4-b061928b5136')

    @patch('src.db.ProdutoDaoOrm.CategoriaModel')
    @patch('src.db.ProdutoDaoOrm.ProdutoModel')
    def test_lista_produto_por_categoria(self, mock_produto_model, mock_categoria_model):
        produto = ProdutoModel(nome='Coca Cola',
                               categoria=CategoriaModel(nome='refrigerante', id='6859a83f-7165-4515-a4f4-b061928b5136'),
                               id='6859a83f-7165-4515-a4f4-b061928b5137', preco=6.9, descricao='Refrigerante',
                               imagem_url='http://example.com/imagem')
        lista_produto_model = [produto]

        mock_produto_set = Mock()
        mock_produto_set.produto_set.all.return_value = lista_produto_model

        mock_categoria_model.objects.get.return_value = mock_produto_set

        lista_produtos = ProdutoDaoOrm.listar_produto_por_categoria('refrigerante')

        self.assertIsInstance(lista_produtos, list)
        self.assertIsInstance(lista_produtos[0], Produto)
        self.assertEqual(lista_produtos[0].nome, 'Coca Cola')

