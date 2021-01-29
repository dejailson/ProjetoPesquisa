import tkinter as t
from tkinter import ttk
from binario import Dados as dd
from time import sleep

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
        self.msg2.place(x=12, y=50)

        self.Nome = t.Entry(self.root, width=98, bord=2)
        self.Nome.place(x=90, y=55)

        self.msg3 = t.Label(self.root, text='Data     ', font='arial 12 bold')
        self.msg3.place(x=12, y=85)

        self.Data = t.Entry(self.root, width=45, bord=2)
        self.Data.place(x=90, y=84)

        self.msg4 = t.Label(self.root, text='Descrição  ', font='arial 12 bold')
        self.msg4.place(x=12, y=120)

        self.Descricao = t.Text(self.root, width=83, height = 5, bord=2)
        self.Descricao.place(x=15, y=150)

        self.msg5 = t.Label(self.root, text='EQUIPE', font='arial 16 bold')
        self.msg5.place(x=12, y=270)

        self.botao_adicionar = t.Button(self.root, text='+ Adicionar', font='arial 10 bold', command=lambda : self.tela_Cad()).place(x=600, y=265)

        self.tree = ttk.Treeview(self.root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), show="headings")

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
        self.lista = ['1', 'Rhuã Yuri', 'Bolsista', 'Não']#Para substituir
        
        self.tree.insert("", 'end',values=self.lista, tag='1')
        self.lista = ['2', 'Dejailson', 'Orientador', 'Sim']#Para substitur
        
        self.tree.insert("", 'end',values=self.lista, tag='1')

        self.tree.place(x=15, y=300, height = 115, width=670)
        self.root.mainloop()


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

        self.butao2 = t.Button(self.tela, text="Cancelar", font='arial 12 bold', command=self.cancelar)#Falta implementar
        self.butao2.place(x=200, y=180)
        self.tela.mainloop()

    def mudarTela(self):
        pass
    '''self.lista = [self.cont[0], self.Nome.get(), self.Data.get(),self.Descricao, [None] '''


    def adicionar(self):
        self.dados = dd()
        self.contador = self.dados.lerBin()
        if not self.contador == None:
            self.cont = self.contador[0][0]
            self.cont += 1
        else:
            self.cont = 1
        self.lista = [self.cont, self.pesquisador.get(), self.membro.get(), self.coordenador.get()]
        self.dados.gravarBin(self.lista)
        self.msg = t.Label(self.tela, text='Tarefa concluída', font='Arial 16 bold').place(x=12, y=230)
        self.tela.destroy()
        self.root.destroy()
        self.root = cadastrarProjeto()
        #Problemas caso o usuário feche a página sem apertar no botão cancelar ou salvar (pensei em colocar em um arquivo temporário, mas caso o programa seja encerrado de forma errônea os dados não vão ser apagados.)

    def cancelar(self):
        self.tela.destroy()

    def visu(self):
        dados = dd()
        return dados.lerBin()



