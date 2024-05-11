import unittest
from unittest.mock import Mock, patch
from main import consultar_cep


class TestCep(unittest.TestCase):
    def setUp(self):
        self.mock_response = Mock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
        }

    @patch('main.requests')
    def test_cep_correto(self, mock_requests):
        mock_requests.get.return_value = self.mock_response
        retorno_consulta = consultar_cep('07192017')
        self.assertIsInstance(retorno_consulta, dict)

    @patch('main.requests')
    def test_cep_incorreto(self, mock_requests):
        # mock_response = Mock()
        # mock_response.side_effect = Exception('consulta invalida222')
        mock_requests.get.side_effect = Exception('consultassssssa222')

        self.assertRaisesRegex(Exception, 'consulta invalida', consultar_cep, '071920170')
