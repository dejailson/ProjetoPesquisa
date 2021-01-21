import tkinter as t
from tkinter import ttk
from salvar_arq import Salvar_Bin as sb

class cadastrarProjeto:
    def __init__(self, root):
        root.geometry("700x500")
        self.w1 = t.LabelFrame(root)
        self.w2 = t.LabelFrame(root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=10)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=10)
        

        root.title('Cadastro de Projeto')

        self.msg1 = t.Label(root, text='Dados do Projeto', font='arial 16 bold')
        self.msg1.place(x=12, y=20)

        self.msg2 = t.Label(root, text='Nome   ', font='arial 12 bold')
        self.msg2.place(x=12, y=50)

        self.Nome = t.Entry(root, width=98, bord=2)
        self.Nome.place(x=90, y=55)

        self.msg3 = t.Label(root, text='Data     ', font='arial 12 bold')
        self.msg3.place(x=12, y=85)

        self.Data = t.Entry(root, width=45, bord=2)
        self.Data.place(x=90, y=84)

        self.msg4 = t.Label(root, text='Descrição  ', font='arial 12 bold')
        self.msg4.place(x=12, y=120)

        self.Descricao = t.Text(root, width=83, height = 5, bord=2)
        self.Descricao.place(x=15, y=150)

        self.msg5 = t.Label(root, text='EQUIPE', font='arial 16 bold')
        self.msg5.place(x=12, y=270)

        self.botao_adicionar = t.Button(root, text='+ Adicionar', font='arial 10 bold', command=lambda : self.tela_Cad()).place(x=600, y=265)

        self.tree = ttk.Treeview(root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

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

        self.tree.place(x=15, y=300, height = 115, width=670)

    def visu(self):
        self.arq = sb()
        #self.lista1 = self.arq.ler_Arq('Projetos.txt', 'Dados_do_Projeto').split(',') / arquivo não completado
        self.lista1 = ['1', 'Rhuã Yuri', 'Bolsista', 'Não', 'nada']
        for c in range(0, int(len(self.lista1)/5)):
            self.tree.insert("", 'end',values=self.lista1[:c+5], tag='1')

    def tela_Cad(self):
        self.tela = t.Tk()
        self.tela.geometry("400x250")
        self.tela.title('Cadastrar Participante')

        self.msgInicial = t.Label(self.tela, text='Cadastrar Participante', font='arial 14 bold')
        self.msgInicial.place(x=100, y=10)

        self.mensagem1 = t.Label(self.tela, text='Pesquisador', font='arial 12 bold')
        self.mensagem1.place(x=12, y=50)

        self.pesquisador = t.Entry(self.tela, width=45, bord=2)
        self.pesquisador.place(x=120, y=50)

        self.mensagem2 = t.Label(self.tela, text='Membro', font='arial 12 bold')
        self.mensagem2.place(x=12, y=90)

        self.membro = t.Entry(self.tela, width=45, bord=2)
        self.membro.place(x=120, y=90)

        self.mensagem3 = t.Label(self.tela, text='Coordenador', font='arial 12 bold')
        self.mensagem3.place(x=12, y=130)

        self.coordenador = t.Entry(self.tela, width=45, bord=2)
        self.coordenador.place(x=120, y=130)

        self.butao1 = t.Button(self.tela, text="Salvar", font='arial 12 bold', command=self.adicionar)#Implementação incompleta
        self.butao1.place(x=100, y=180)

        self.butao2 = t.Button(self.tela, text="Cancelar", font='arial 12 bold')#Falta implementar
        self.butao2.place(x=200, y=180)
        self.tela.mainloop()

    def adicionar(self):
        pass
        '''lista = ['1', self.pesquisador.get(), self.membro.get(), self.coordenador.get(), 'nada', '1']
        sb(lista)
        print('jh')'''

    

root = t.Tk()
cadastrarProjeto(root)
t.mainloop()
