import tkinter as t
from tela.Amostras import Amostras
from util.binario import Dados as dd
from PIL import ImageTk, Image
from util.GerenciadorRecurso import GerenciadorRecurso as gr
import config.Parametro as param
from tela.cadastrarAmostra import CadastrarAmostra as CA 
import shelve
import os

class ViewAmostras():
    def __init__(self, projeto):
        self.root = t.Tk()
        self.root.geometry('800x500')
        self.root.title('amostras')
        self.recurso = gr()
        self.root.iconbitmap(self.recurso.carregarIconeJanela())
        posicao = self.tree.get_children()
        
        self.dados = shelve.open(param.BANCO_DADOS)
        self.lista = self.dados['Amostra']
        self.cont = 1
        self.lista1 = []

        for c in self.lista:
            if c.nomeProjeto == projeto:
                img = os.path.join(param.SUBPASTA_IMGS_AMOSTRAS, projeto+'_'+c.identificao+'.png')
                self.lista1.append(self.recurso.montarCaminhoRecurso(img))
                self.button1 = t.Button(self.root, text=c.identificao,
                                command=lambda x=self.recurso.montarCaminhoRecurso(img): 
                                self.mudarTela(x, c)).pack()
        self.dados.close()

        self.root.mainloop()

    def mudarTela(self, x=None, amostra=None):
        if x == None:
            pass
        else:
            self.root.destroy()
            CA(im=x, caminho=x, amostra=amostra)


     

