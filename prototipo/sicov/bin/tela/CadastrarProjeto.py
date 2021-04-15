import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd
from util.modelo.projeto import Projeto
from util.modelo.pesquisador import Pesquisador
import config.Parametro as param 
import shelve
from config.Parametro import BANCO_DADOS


class cadastrarProjeto:
    def __init__(self):
        self.dados_membros = []
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=10)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=10)
        self.root.title('Cadastro de Projeto')
        
        self.validarSimNao = 0
        self.cont = 1

        self.msg1 = t.Label(self.root, text='Dados do Projeto',
                            font='arial 16 bold')
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

        self.botao_adicionar = t.Button(self.root, text='+ Adicionar',
                                        font='arial 10 bold', 
                                        command=lambda : self.tela_Cad())
        self.botao_adicionar.place(x=600, y=265)

        self.tree = ttk.Treeview(self.root, selectmode="browse", 
                                column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"), 
                                show="headings")
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

        self.cancelarP = t.Button(self.root, text='Cancelar', 
                                font='arial 10 bold', 
                                command=lambda:self.mudarTela())
        self.cancelarP.place(x=20, y=450)
        self.salvarP = t.Button(self.root, text='Salvar', 
                                font='arial 10 bold', 
                                command=lambda:self.salvar())
        self.salvarP.place(x=620, y=450)

        self.root.mainloop()


    def tela_Cad(self):
        self.tela = t.Tk()
        self.tela.geometry("400x300")
        self.tela.title('Cadastrar Participante')

        self.msgInicial = t.Label(self.tela, text='Cadastrar Participante', 
                                  font='arial 14 bold')
        self.msgInicial.place(x=100, y=10)

        self.mensagem1 = t.Label(self.tela, text='Matrícula', 
                                 font='arial 12 bold')
        self.mensagem1.place(x=12, y=50)

        self.matricula = t.Entry(self.tela, width=45, bord=2)
        self.matricula.place(x=120, y=50)

        self.mensagem2 = t.Label(self.tela, text='Pesquisador', 
                                 font='arial 12 bold')
        self.mensagem2.place(x=12, y=90)

        self.pesquisador = t.Entry(self.tela, width=45, bord=2)
        self.pesquisador.place(x=120, y=90)

        self.mensagem3 = t.Label(self.tela, text='Membro', font='arial 12 bold')
        self.mensagem3.place(x=12, y=130)

        self.membro = ttk.Combobox(self.tela, 
                                   values=['Bolsista', 'Orientador', 
                                           'Voluntário'],
                                    width=42)
        self.membro.place(x=120, y=130)
        self.membro.current(0)

        self.mensagem4 = t.Label(self.tela, text='Coordenador', 
                                 font='arial 12 bold')
        self.mensagem4.place(x=12, y=170)
        self.listSimNao = ['Sim', 'Não']
        if self.validarSimNao == 1:
            self.listSimNao = ['Não']
        self.coordenador = ttk.Combobox(self.tela, 
                                        values=self.listSimNao, width=42)
        self.coordenador.place(x=120, y=170)
        self.coordenador.current(0)

        self.butao1 = t.Button(self.tela, text="Salvar", font='arial 12 bold',
                               command=self.adicionar)
        self.butao1.place(x=100, y=250)
        self.butao2 = t.Button(self.tela, text="Cancelar", font='arial 12 bold', 
                               command=lambda: self.mudarTela(root=self.tela))
        self.butao2.place(x=200, y=250)

        self.tela.mainloop()

    def mudarTela(self, root=None):
        if root == None:
            self.root.destroy()
            from tela.Projeto import Projeto as PJ
            PJ()
        else:
            root.destroy()

    def salvar(self):
        self.verCont
        self.ver = [self.Nome.get().strip(), self.Data.get().strip(), self.Descricao.get(1.0, t.END).strip(), self.dados_membros]
        for i in self.ver:
            if i == '':
                self.verCont += 1
        if self.verCont > 0:
            pass

        self.projeto = Projeto(nome=self.Nome.get().strip(), 
                               data=self.Data.get().strip(), 
                               descricao=self.Descricao.get(1.0, t.END).strip(), 
                               pesquisadores=self.dados_membros)
         
        try: 
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            self.lista.append(self.projeto)
            self.dados['Projeto'] = self.lista
            self.dados.close()
        except:
            print('Erro!')
        self.mudarTela()

    def adicionar(self):
        self.verCont
        self.ver = [self.pesquisador.get().strip(), self.pesquisador.get().strip()]
        for i in self.ver:
            if i == '':
                self.verCont += 1
        if self.verCont > 0:
            pass
        self.Membro_Pesquisador = Pesquisador(nome=self.pesquisador.get().strip(), 
                                            matricula=self.pesquisador.get().strip(), 
                                            tipoMembro=self.membro.get().strip(), 
                                            coordenador=self.coordenador.get().strip())
        if self.Membro_Pesquisador.coordenador == 'Sim':
            self.validarSimNao = 1
        self.dados_membros.append(self.Membro_Pesquisador)
        self.tela.destroy()

        self.lista = self.dados_membros[-1].listaAtributos
        self.lista.insert(0, self.cont)
        self.tree.insert("", 'end',values=self.lista,  tag='1')
        self.cont  += 1
        
    def visu(self):
        pass
        #self.dados = shelve.open(BANCO_DADOS)
        #self.lista = self.dados['Projeto']
        #self.dados.close()
        #self.list = []
        #for c in self.lista:
        #    for d in c.pesquisadores:
        #        self.list = d
        #        self.tree.insert("", 'end',values=self.list.listaAtributos,  tag='1')
