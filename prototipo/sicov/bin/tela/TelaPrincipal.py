import tkinter as t
from tela.Projeto import Projeto
from tela.Amostras import Amostras
from util.binario import Dados as dd
from PIL import ImageTk, Image
from util.GerenciadorRecurso import GerenciadorRecurso as gr
import config.Parametro as param
from tela.ObjetoPadrao import ObjetoPadrao as ob

class TelaPrincipal():
    def __init__(self):
        self.root = t.Tk()
        self.root.configure(bg='white')
        self.binario = dd()
        self.recurso = gr()
        self.root.iconbitmap(self.recurso.carregarIconeJanela())
        self.root.geometry('800x500')
        self.root.title('SisCov')
        self.root.resizable(0, 0) 
        self.menu = t.Menu(self.root, tearoff=0)
        self.Menu = t.Menu(self.menu, tearoff=0)
        self.menu.add_command(label='Tela de Projeto',
                              command=lambda: self.Pro())
        self.menu.add_command(label='Tela de Amostras',
                              command=lambda: self.Amo())
        self.menu.add_command(label='Objeto Padrão',
                              command=lambda: ob())
        self.menu.add_separator()
        self.menu.add_command(label='Fechar', command=lambda: self.root.quit())
        self.Menu.add_cascade(label='Informações', menu=self.menu)
        self.root.config(menu=self.Menu)
        self.titulo = t.Label(
            self.root, text='Sistema de Contagem de Ovos', font=param.FONTE_TITULO, bg='white').pack()
        self.nada = t.Label(self.root, text='   ', font=param.FONTE_TITULO, bg='white').pack()
        
        self.recurso.banco()
        self.nome_img = self.recurso.carregarImagemFundo()
        self.img = ImageTk.PhotoImage(Image.open(self.nome_img))
        self.ima_l = t.Label(imag=self.img, width=700, height=400).pack()

        self.root.mainloop()

    def Pro(self):
        self.root.destroy()
        Projeto()

    def Amo(self):
        self.root.destroy()
        Amostras()
