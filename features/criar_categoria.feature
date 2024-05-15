Funcionalidade: Adicionar categoria ao catalogo
    Cenário: Criacao de categoria via api
        Dado que foram informados os dados para criacao da categoria
            '''
                { "nome": "Bebidas" }
            '''
        E após a validação os dados estão corretos
        Quando a rotina de criação de catalogo for executada
        Então será retornado o id do catalogo e suas informações