import tkinter as t 
from tkinter import ttk
from binario import Dados as dd
from transicao import Transicao as tr

class Selecao:
    def __init__(self, x=None):
        self.root = t.Tk()
        self.root.geometry('600x300')
        self.root.title('Selecione o Projeto')
        self.titulo = t.Label(self.root, text='Selecione o Projeto', font='Arial 20 bold').pack()

        
        self.root.configure(bg='white')

        self.visu()#Colocar em um função posteriormente



        self.root.mainloop()

    def visu(self, num=None):
        self.dados = dd()
        self.informacoes = self.dados.lerBin()
        self.cont = 1
        self.contador = 0
        self.pal = []
        
        for c in self.informacoes:
            self.lista = [self.cont, c[0], c[1]]
            self.palavra = ''
            for d in c[3][:]:
                if d[3] in 'Sim':
                    self.lista.append(d[1])
                    for c in self.lista:
                        self.palavra = self.palavra + str(c) + '  '
                    self.buton = t.Button(self.root, text=self.palavra, bg='white', width=50, command=lambda: self.avancar(self.buton))
                    self.buton.pack()
                    self.pal.append([self.palavra])
                    self.contador +=1
                    break
            self.cont += 1

    def avancar(self, palavra):
        tr(1)

Selecao()