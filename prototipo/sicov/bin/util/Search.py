from util.binario import Dados as dd
from util.modelo.projeto import Projeto
from config.Parametro import BANCO_DADOS
import shelve

def Search(amostra=None, projeto=None):
    AmostraDef = amostra
    ProjetoDef = projeto
    dados = shelve.open(BANCO_DADOS)
    bancoInformacoes = []
    listaProjetos = dados['Projeto']
    if AmostraDef != None: 
        for projeto in listaProjetos:
            if projeto.nome == amostra[1] and amostra[0] == '':
                bancoInformacoes.append(projeto) 
            else:
                if projeto.nome.lower() == AmostraDef[1].lower():
                    for amostra in projeto.amostras:
                        if AmostraDef[0].lower() in amostra.identificacao.lower():
                            bancoInformacoes.append(Projeto(nome=projeto.nome,
                                                        data=projeto.data,
                                                        descricao=projeto.descricao,
                                                        pesquisadores=projeto.pesquisadores,
                                                        coordenador=projeto.coordenador))
                            bancoInformacoes[0].setAmostra(amostra)
                            break
    else:
        listaProjeto = dados['Projeto']
        for projeto in listaProjeto:
            if (ProjetoDef[0].lower() in projeto.nome.lower() and projeto.coordenador.nome.lower() == ProjetoDef[2].lower() and ProjetoDef[1]== projeto.data) \
                or (ProjetoDef[0].lower() == projeto.nome.lower() or ProjetoDef[2].lower() == projeto.coordenador.nome.lower() or ProjetoDef[1] == projeto.data):
                    bancoInformacoes.append(projeto)
                    break
    return bancoInformacoes


