import unittest
from src.domain.entities.CategoriaFactory import CategoriaFactory, _validar_nome_categoria
from uuid import uuid4


class TestCategoriaFactory(unittest.TestCase):
    def test_criar_categoria_from_dict_sem_id(self):
        dicionario_categoria = {
            'nome': 'refrigerante',
            'id': None
        }
        categoria = CategoriaFactory.from_dict(dicionario_categoria=dicionario_categoria)
        self.assertEqual(categoria.nome, 'refrigerante')

    def test_criar_categoria_uuid_invalido(self):
        dicionario_categoria = {
            'nome': 'refrigerante',
            'id': 'dsadsadsa'
        }
        #categoria = CategoriaFactory.from_dict(dicionario_categoria=dicionario_categoria)
        self.assertRaises(AttributeError, CategoriaFactory.from_dict, dicionario_categoria)

    def test_criar_categoria_from_dict_com_id(self):
        dicionario_categoria = {
            'nome': 'refrigerante',
            'id': uuid4()
        }
        categoria = CategoriaFactory.from_dict(dicionario_categoria=dicionario_categoria)
        self.assertEqual(categoria.nome, 'refrigerante')

    def test_categoria_nome_null(self):
        dicionario_categoria = {
            'id': 1
        }

        self.assertRaises(AttributeError, CategoriaFactory.from_dict, [dicionario_categoria])

    def test_categoria_nome_caracteres_excedidos(self):
        nome = 'abcdferffffffffdkdlfkdlkfldkfldklfdklfdklsdkfldsklfskdlfkdslfkdslkfdslkfdslkfdslkfdslkfldskflsdk'

        self.assertRaises(AttributeError, _validar_nome_categoria, nome)

    def test_categoria_nome_sem_caracteres(self):
        nome = ''

        self.assertRaises(AttributeError, _validar_nome_categoria, nome)


