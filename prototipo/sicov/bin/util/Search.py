from util.binario import Dados as dd
from config.Parametro import BANCO_DADOS
import shelve

def Search(amostra=None, projeto=None):
    dados = shelve.open(BANCO_DADOS)
    bancoInformacoes = []
    if amostra != None:
        listaAmostra = dados['Amostra']
        for lista in listaAmostra:
            if lista.identificacao in amostra[0] or (lista.nomeProjeto == amostra[1] and amostra[0] == ''):
                bancoInformacoes.append(lista)
                break
    else:
        listaProjeto = dados['Projeto']
        for lista in listaProjeto:
            for c in lista.pesquisadores:
                if c.coordenador == "Sim":
                    coordenador = c.nome
            if (projeto[0] in lista.nome and coordenador == projeto[2] and projeto[1] == lista.data) \
                or (projeto[0] == lista.nome or projeto[2] == coordenador or projeto[1] == lista.data):
                    bancoInformacoes.append(lista)
                    break
    return bancoInformacoes


