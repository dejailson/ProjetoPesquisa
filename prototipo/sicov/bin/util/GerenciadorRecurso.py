import os
import config.Parametro as param
from util.binario import Dados as dd
from config.Parametro import BANCO_DADOS
import shelve
from tkinter import ttk


class GerenciadorRecurso:
    DIRETORIO_RAIZ = os.path.realpath('..')

    def __init__(self):
        pass

    def carregarIconeLapis(self):
        icon_lapis = os.path.join(param.SUBPASTA_ICONE, param.ICONE_LAPIS)
        return self.montarCaminhoRecurso(icon_lapis)

    def carregarIconeOlho(self):
        icon_olho = os.path.join(param.SUBPASTA_ICONE, param.ICONE_OLHO)
        return self.montarCaminhoRecurso(icon_olho)

    def carregarIconeLixeira(self):
        icon_lixeira = os.path.join(param.SUBPASTA_ICONE, param.ICONE_LIXEIRA)
        return self.montarCaminhoRecurso(icon_lixeira)

    def carregarImagemFundo(self):
        imagem_fundo = os.path.join(param.SUBPASTA_FUNDO, param.IMAGEM_FUNDO)
        return self.montarCaminhoRecurso(imagem_fundo)

    def carregarIconeJanela(self):
        imagem_fundo = os.path.join(param.SUBPASTA_ICONE, param.ICONE_JANELA)
        return self.montarCaminhoRecurso(imagem_fundo)

    def montarCaminhoRecurso(self, nomeRecurso):
        return os.path.join(self.DIRETORIO_RAIZ, param.PASTA_RECURSO,
                            param.PASTA_IMAGEM, nomeRecurso)

    def excluirImagem(self, urlArquivo):
        os.remove(urlArquivo)

    def monstarListaProjetos(self, root, tela=None):
        self.a = 0 
        self.b = 0 
        self.c = 0
        self.d = None
        self.e = None
        if tela == 'Amostra':
            self.a = 160
            self.b = 150
            self.c = 30
        else:
            self.a = 550
            self.b = 40
            self.c = 20
            self.d = 0.42
            self.e = 0.01
        self.bd = shelve.open(BANCO_DADOS)
        self.informacoes = self.bd['Projeto']
        self.lista = []
        if not self.informacoes == []:
            for c in self.informacoes[:]:
                self.lista.append(c.nome)
        else:
            self.lista.append('Sem Projetos Cadastrado')
        self.projeto = ttk.Combobox(root, values=self.lista, width=62)
        self.projeto.place(x=self.a, y=self.b, height=self.c, relwidth=self.d, relheight=self.e)
        self.projeto.current(0)
        #x=550, y=40, height=20, relwidth=0.42, relheight=0.01
    
    def banco(self):
        self.bd = shelve.open(BANCO_DADOS)
        if 'Projeto' not in self.bd:
            self.bd['Projeto'] = []
            self.bd['Objeto'] = []
            self.bd.close()

    def setObjetoPadrao(self, largura, altura):
        self.bd = shelve.open(BANCO_DADOS)
        self.lista = self.bd['Objeto']
        self.lista = [largura, altura]
        self.bd['Objeto'] = self.lista
        self.bd.close()

    def getObjetoPadrao(self):
        self.bd = shelve.open(BANCO_DADOS)
        self.lista = self.bd['Objeto']
        self.bd.close()
        return self.lista
        
            
