from src.domain.entities.Categoria import Categoria


class FormatCategoria:
    """
    Classe com métodos para formatar objetos do tipo Categoria
    """

    @staticmethod
    def from_categoria_to_dict(categoria: Categoria):
        return ({
            'id': categoria.id,
            'nome': categoria.nome
        })
