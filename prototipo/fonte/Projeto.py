import tkinter as t
from tkinter import ttk

class Projeto:
    def __init__(self):
        root = t.Tk()
        root.geometry("700x500")
        self.w1 = t.LabelFrame(root)
        self.w2 = t.LabelFrame(root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        root.title('Projeto')

        self.msg1 = t.Label(root, text='Filtros', font='arial 9 bold')
        self.msg1.place(x=30, y=0)

        self.msg2 = t.Label(root, text='Nome   ', font='arial 16 bold')
        self.msg2.place(x=12, y=50)

        self.Nome = t.Entry(root, width=50, bord=2)
        self.Nome.place(x=160, y=55, height=30)

        self.msg3 = t.Label(root, text='Data', font='arial 16 bold')
        self.msg3.place(x=465, y=55)

        self.Data = t.Entry(root, width=25, bord=2)
        self.Data.place(x=520, y=55, height=30)

        self.msg4 = t.Label(root, text='Coordenador     ', font='arial 14 bold')
        self.msg4.place(x=12, y=150)

        self.coordenador = t.Entry(root, width=50, bord=2)
        self.coordenador.place(x=160, y=150, height=30)

        self.botao_pesquisar = t.Button(root, text='Pesquisar', font='arial 10 bold').place(x=540, y=150)#sem ação

        self.botao_adicionar = t.Button(root, text='+ Incluir Novo', font='arial 10 bold').place(x=580, y=265)#sem ação

        self.tree = ttk.Treeview(root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

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

        self.lista = ['1', 'Projeto I', '12/03/2018', 'Dejailson', 'nada']
        for c in range(0, 3):
            self.tree.insert("", 'end',values=self.lista, tag='1')

        self.tree.place(x=15, y=300, height = 115, width=670)

        self.button2 = t.Button(root, text='Salvar').place(x=570, y=450, width=100)

        root.mainloop()


Projeto()