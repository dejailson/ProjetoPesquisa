import tkinter as t
from tkinter import ttk
from CadastrarProjeto import cadastrarProjeto as CP
from binario import Dados as dd

class Projeto():
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.root.title('Projeto')

        self.msg1 = t.Label(self.root, text='Filtros', font='arial 9 bold')
        self.msg1.place(x=30, y=0)

        self.msg2 = t.Label(self.root, text='Nome   ', font='arial 16 bold')
        self.msg2.place(x=12, y=50)

        self.Nome = t.Entry(self.root, width=50, bord=2)
        self.Nome.place(x=160, y=55, height=30)

        self.msg3 = t.Label(self.root, text='Data', font='arial 16 bold')
        self.msg3.place(x=465, y=55)

        self.Data = t.Entry(self.root, width=25, bord=2)
        self.Data.place(x=520, y=55, height=30)

        self.msg4 = t.Label(self.root, text='Coordenador     ', font='arial 14 bold')
        self.msg4.place(x=12, y=150)

        self.coordenador = t.Entry(self.root, width=50, bord=2)
        self.coordenador.place(x=160, y=150, height=30)

        self.botao_pesquisar = t.Button(self.root, text=' Pesquisar ', font='arial 12 bold').place(x=540, y=150)#sem ação

        self.botao_adicionar = t.Button(self.root, text='+ Incluir Novo', font='arial 10 bold', command=lambda : self.chamar()).place(x=580, y=265)#sem ação

        self.tree = ttk.Treeview(self.root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text=' ')

        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Projeto')

        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Data')

        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

        self.tree.column("coluna5", width=100, minwidth=50)
        self.tree.heading('#5', text='Ações')

        self.visu()#Colocar em um função posteriormente

        self.tree.place(x=15, y=300, height = 115, width=670)

        self.button2 = t.Button(self.root, text='Voltar', command=lambda:self.voltar()).place(x=570, y=450, width=100)

        self.root.mainloop()
    
    def voltar(self):
        self.root.destroy()
        from transicao import Transicao as T
        T(n=6)

    def chamar(self):
        self.root.destroy()
        CP()

    def visu(self, num=None):
        self.dados = dd()
        self.informacoes = self.dados.lerBin()
        self.cont = 1
        try:
            for c in self.informacoes:
                self.lista = [self.cont, c[0], c[1]]
                for d in c[3][:]:
                    if d[3] in 'Sim':
                        self.lista.append(d[1])
                        self.tree.insert("", 'end',values=self.lista, tag='1')
                        break
                self.cont += 1
        except:
            self.tree.insert("", 'end',values=[], tag='1')
                




