import tkinter as t
from tkinter import ttk

class Amostras:
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.root.title('Amostras')

        self.msg1 = t.Label(self.root, text='Filtros', font='arial 9 bold')
        self.msg1.place(x=30, y=0)

        self.msg2 = t.Label(self.root, text='Identificação', font='arial 16 bold')
        self.msg2.place(x=12, y=50)

        self.Identificacao = t.Entry(self.root, width=65, bord=2)
        self.Identificacao.place(x=160, y=55, height=30)

        self.msg3 = t.Label(self.root, text='Projeto', font='arial 14 bold')
        self.msg3.place(x=12, y=150)

        self.lista = [
                        "Projeto 1", 
                        "Projeto 2",
                        "Projeto 3",
                        "Projeto 4"]
        self.projeto = ttk.Combobox(self.root, values=self.lista, width=62)
        self.projeto.place(x=160, y=150, height=30)
        self.projeto.current(0)


        self.botao_pesquisar = t.Button(self.root, text=' Pesquisar ', font='arial 12 bold').place(x=570, y=149)#sem ação

        self.botao_adicionar = t.Button(self.root, text='+ Incluir Novo', font='arial 10 bold').place(x=580, y=265)#sem ação

        self.tree = ttk.Treeview(self.root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text=' ')

        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Projeto')

        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Identificação')

        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

        self.tree.column("coluna5", width=100, minwidth=50)
        self.tree.heading('#5', text='Ações')

        self.lista = ['1', 'Projeto I', 'ITA-09211', 'Dejailson', 'nada']#Colocar em uma função posteriormente
        for c in range(0, 3):
            self.tree.insert("", 'end',values=self.lista, tag='1')

        self.tree.place(x=15, y=300, height = 115, width=670)

        self.button2 = t.Button(self.root, text='Salvar').place(x=570, y=450, width=100)

        self.root.mainloop()

    def visu(self):
        pass



