import tkinter as t
import os
import pickle

class Dados:
    def __init__(self, NomeArquivo='Projetos.dat'):
        self.nomePasta = 'Dados_do_Projeto'
        self.NomeArquivo = NomeArquivo
    
    def criar_Pasta(self):
        if not os.path.isdir(self.nomePasta):
            os.mkdir(self.nomePasta)
            return True
        return False

    def monstar_Cam(self):
        if not self.nomePasta == None:
            return os.path.join(self.nomePasta, self.NomeArquivo)
        return self.NomeArquivo

    def salvarBin(self, conteudo):
        self.caminho_Arq = self.monstar_Cam()
        self.arq = open(self.caminho_Arq, 'wb')
        self.arq.write(self.serializar(conteudo))
        self.arq.close()

    def serializar(self, conteudo):
        return pickle.dumps(conteudo)

    def criarArquivo(self):
        self.caminho_Arq = self.monstar_Cam()
        self.arq = open(self.caminho_Arq, 'wb')
        self.arq.close()

    def lerBin(self):
        self.caminho_Arq = self.monstar_Cam()
        if os.path.isfile(self.caminho_Arq):
            with open(self.caminho_Arq, 'rb') as self.arq:
                return self.deserializar(self.arq)
        return None

    def deserializar(self, conteudo):
        return pickle.load(conteudo)

    def gravarBin(self, conteudo):
        self.lista = self.lerBin()
        if self.lista == None:
            self.lista = []
        self.lista.append(conteudo)
        self.salvarBin(self.lista)

    def buscarCaminho(self, nome):
        dirlist = os.getcwd()
        if '\\' in dirlist:
            dirlist = dirlist + '\\prototipo\\fonte\\' + nome
        else:
            dirlist = dirlist + '/prototipo/fonte/' + nome
        return dirlist





