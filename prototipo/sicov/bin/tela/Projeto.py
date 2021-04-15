import tkinter as t
import config.Parametro as param
from tkinter import ttk
from tela.CadastrarProjeto import cadastrarProjeto as CP
from util.binario import Dados as dd
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from PIL import ImageTk
from PIL import Image
import shelve
from config.Parametro import BANCO_DADOS

class Projeto():
    def __init__(self):
        self.recurso = gr()

        self.pro = t.Tk()
        self.pro.geometry("700x500")
        self.w1 = t.LabelFrame(self.pro)
        self.w2 = t.LabelFrame(self.pro)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.pro.title('Projeto')

        self.msg1 = t.Label(self.pro, text='Filtros', font=param.FONTE_OUTRA[0])
        self.msg1.place(x=30, y=0)
        self.msg2 = t.Label(self.pro, text='Nome   ', font=param.FONTE_OUTRA[3])
        self.msg2.place(x=12, y=50)
        self.Nome = t.Entry(self.pro, width=50, bord=2)
        self.Nome.place(x=160, y=55, height=30)
        self.msg3 = t.Label(self.pro, text='Data', font=param.FONTE_OUTRA[3])
        self.msg3.place(x=465, y=55)
        self.Data = t.Entry(self.pro, width=25, bord=2)
        self.Data.place(x=520, y=55, height=30)
        self.msg4 = t.Label(self.pro, text='Coordenador     ', font=param.FONTE_OUTRA[2])
        self.msg4.place(x=12, y=150)
        self.coordenador = t.Entry(self.pro, width=50, bord=2)
        self.coordenador.place(x=160, y=150, height=30)

        self.botao_pesquisar = t.Button(self.pro, text=' Pesquisar ', font=param.FONTE_PADRAO)
        self.botao_pesquisar.place(x=540, y=150)#sem ação
        self.botao_adicionar = t.Button(self.pro, text='+ Incluir Novo', font=param.FONTE_OUTRA[1],  
                                        command=lambda : self.mudarTela())
        self.botao_adicionar.place(x=580, y=265)
        
        self.tree = ttk.Treeview(self.pro, selectmode="browse", 
                                column=("coluna1", "coluna2", "coluna3", "coluna4"),
                                show="headings")
        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text=' ')
        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Projeto')
        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Data')
        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

        self.visu()

        self.tree.place(x=15, y=300, height = 115, width=540)

        self.button2 = t.Button(self.pro, text='Voltar', 
                                command=lambda:self.mudarTela(var=1))
        self.button2.place(x=570, y=450, width=100)
        

        self.caminho_lapis = self.recurso.carregarIconeLapis()
        self.img_lapis = Image.open(self.caminho_lapis)
        self.resu = self.red(self.img_lapis)
        self.imagem_lapis = ImageTk.PhotoImage(self.resu)
        self.imagem_lapis_L = t.Button(image=self.imagem_lapis).place(x=570, y=315)

        self.caminho_olhos = self.recurso.carregarIconeOlho()
        self.img_olhos = Image.open(self.caminho_olhos)
        self.resu = self.red(self.img_olhos)
        self.imagem_olhos = ImageTk.PhotoImage(self.resu)
        self.imagem_olhos_L = t.Button(image=self.imagem_olhos).place(x=610, y=315)

        self.caminho_lixeira = self.recurso.carregarIconeLixeira()
        self.img_lixeira = Image.open(self.caminho_lixeira)
        self.resu = self.red(self.img_lixeira)
        self.imagem_lixeira = ImageTk.PhotoImage(self.resu)
        self.imagem_lixeira_L = t.Button(image=self.imagem_lixeira).place(x=650, y=315)

        self.pro.mainloop()

    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge

    def mudarTela(self, var=None):
        self.pro.destroy()
        if var == None:
            CP()
        else:
            from tela.TelaPrincipal import TelaPrincipal
            TelaPrincipal()

    def visu(self, num=None):
        self.dados = shelve.open(BANCO_DADOS)
        self.lista = self.dados['Projeto']
        self.cont = 1
        for c in self.lista:
            self.list = [self.cont]
            self.list.append(c.nome)
            self.list.append(c.data)
            for d in c.pesquisadores:
                if d.coordenador == 'Sim':
                    self.list.append(d.nome)
            self.tree.insert("", 'end',values=self.list,  tag='1')
            self.cont += 1
        self.dados.close()
        
                

