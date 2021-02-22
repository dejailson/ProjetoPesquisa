import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd

global d_membros
d_membros = []
class cadastrarProjeto:
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=10)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=10)
        

        self.root.title('Cadastro de Projeto')

        self.msg1 = t.Label(self.root, text='Dados do Projeto', font='arial 16 bold')
        self.msg1.place(x=12, y=20)

        self.msg2 = t.Label(self.root, text='Nome   ', font='arial 12 bold')
        self.msg2.place(x=12, y=50, relwidth=None, relheight=0.048)

        self.Nome = t.Label(self.root, width=98,  bg='white', relief="groove")
        self.Nome.place(x=90, y=55, relwidth=0.85, relheight=0.048)

        self.msg3 = t.Label(self.root, text='Data     ', font='arial 12 bold')
        self.msg3.place(x=12, y=85, relwidth=None, relheight=0.048)

        self.Data = t.Label(self.root, width=45, bg='white', relief="groove")
        self.Data.place(x=90, y=84, relwidth=None, relheight=0.048)

        self.msg4 = t.Label(self.root, text='Descrição  ', font='arial 12 bold')
        self.msg4.place(x=12, y=120)

        self.Descricao = t.Label(self.root, width=83, height = 5, bg='white', relief="groove")
        self.Descricao.place(x=15, y=150, relwidth=0.96, relheight=0.16)

        self.msg5 = t.Label(self.root, text='EQUIPE', font='arial 16 bold')
        self.msg5.place(x=12, y=270, relwidth=None, relheight=0.048)

        self.tree = ttk.Treeview(self.root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

        
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.vsb.place(x=640, y=300, height=137)

        self.tree.configure(yscrollcommand=self.vsb.set)

        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text=' ')

        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Pesquisador')

        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Membro')

        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

        self.tree.column("coluna5", width=100, minwidth=50)
        self.tree.heading('#5', text='Ações')
        
        self.visu()
        
        self.tree.place(x=15, y=300, height = 115, width=83, relwidth=0.75, relheight=0.038)
        self.voltar = t.Button(self.root, text='Voltar', command=self.mudarTela).place(x=550, y=450, width=100)
        

        self.root.mainloop()
        #self.visu()


   

    def mudarTela(self):
        self.root.destroy()
        from tela.transicao import Transicao as T
        T(n=1)

    def cancelar(self, tela):
        tela.destroy()
    

    def visu(self):
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
cadastrarProjeto()