import os
import config.Parametro as param
from util.binario import Dados as dd
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

    def montarCaminhoRecurso(self, nomeRecurso):
        return os.path.join(self.DIRETORIO_RAIZ, param.PASTA_RECURSO,
                            param.PASTA_IMAGEM, nomeRecurso)

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
        self.dados1 = dd()
        self.informacoes = self.dados1.lerBin()
        self.lista = []
        if not self.informacoes == None:
            for c in self.informacoes[:]:
                self.lista.append(c[0])
        else:
            self.lista.append('Sem Projetos Cadastrado')
        self.projeto = ttk.Combobox(root, values=self.lista, width=62)
        self.projeto.place(x=self.a, y=self.b, height=self.c, relwidth=self.d, relheight=self.e)
        self.projeto.current(0)
        #x=550, y=40, height=20, relwidth=0.42, relheight=0.01
