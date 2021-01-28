# import re
import requests


def ValidaCep(cep):
    cep = str(cep)
    url = "https://viacep.com.br/ws/{}/json/".format(cep)

    if len(cep) == 8:
        request = requests.get(url)
        dados = request.json()
        if dados is not False:
            return "{}-{}".format(cep[:5], cep[5:])


def ValidaCelular(celular):
    if len(celular) == 11:
        return "({}) {}-{}".format(celular[:2], celular[2:7], celular[7:])


def ValidaTelefone(celular):
    if len(celular) == 10:
        return "({}) {}-{}".format(celular[:2], celular[2:6], celular[6:])
