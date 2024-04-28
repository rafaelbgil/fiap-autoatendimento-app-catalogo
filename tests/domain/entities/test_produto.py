import unittest
from src.domain.entities.ProdutoFactory import ProdutoFactory, _validar_descricao_produto, _validar_imagem_url_produto, _validar_nome_produto, _validar_preco_produto


class TestProdutoFactory(unittest.TestCase):
    def test_criar_produto_from_dict(self):
        dicionario_produto = {
            'id': 1,
            'descricao': 'Descricao do produto de teste',
            'nome': 'Produto de Teste',
            'preco': 10.90,
            'imagem_url': 'http://teste.com.br/teste',
            'id_categoria': 1
        }
        self.assertTrue(ProdutoFactory.from_dict(
            dicionario_produto=dicionario_produto))

    def test_validar_nome_produto_excecao_numero_caracteres(self):
        nome_produto = 'dsajdksajdksajkdasjkdjaskdjsakjdaskjdaskjdaskjdsakjdskajdkasjdkasjdsajkjdaksjdkasjda'
        self.assertRaises(ValueError, _validar_nome_produto, nome_produto)

    def test_validar_nome_produto_execao_nome_vazio(self):
        nome_produto = ''
        self.assertRaises(AttributeError, _validar_nome_produto, nome_produto)

    def test_validar_descricao_produto_excecao_numero_caracteres(self):
        descricao_produto = '''dsajdksajdksajkdasjkdjaskdjsakjdaskjdaskjdaskjdsakjdskajdkasjdkasjdsajkjdaksjdkasjda
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
            dsadaslkdaslkdsalkdaslkdlsakdlsakdlaskdlsakdlsakdlkaldksalkdaslkdaslkdslakdlaskdlakldaskdlskaldsakldsak
        '''
        self.assertRaises(ValueError, _validar_descricao_produto, descricao_produto)

    