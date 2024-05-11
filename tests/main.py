import requests


def consultar_cep(cep: str):
    consulta = requests.get(url=f'https://viacep.com.br/ws/{cep}/json/')
    if consulta.status_code == 200:
        return consulta.json()
    else:
        raise Exception('consulta invalida')


def consultar_algo(cep: str):
    try:
        consulta = requests.get(url=f'https://viacep.com.br/ws/{cep}/json/')
    except:
        raise Exception('consulta invalida')

    try:
        formatado = consulta.json()
    except:
        raise Exception('nao foi possivel exibir json')

    return formatado