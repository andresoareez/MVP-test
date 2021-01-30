# import re
import requests

#responsável por validar dados importantes do cadastro para que não exista problemas com os dados no DB
#validacao para CEP, CELULAR, TELEFONE


def ValidaCep(cep):
    cep = str(cep)
    url = "https://viacep.com.br/ws/{}/json/".format(cep) #Com esse webservice e possivel fazer a coleta e
    #preenchimento automatico dos dados, uma melhoria que poderia ser implementada

    if len(cep) == 8:
        request = requests.get(url)
        dados = request.json()
        if dados is not False:
            return "{}-{}".format(cep[:5], cep[5:])


def ValidaCelular(celular):
    if len(celular) == 11:
        return "({}) {}-{}".format(celular[:2], celular[2:7], celular[7:])


def ValidaTelefone(telefone):
    if len(telefone) == 10:
        return "({}) {}-{}".format(telefone[:2], telefone[2:6], telefone[6:])
