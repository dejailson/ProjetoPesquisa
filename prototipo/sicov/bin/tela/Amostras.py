import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd
from PIL import ImageTk,Image
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from tela.cadastrarAmostra import CadastrarAmostra as CA
from config.Parametro import BANCO_DADOS
import config.Parametro as param
import shelve

global listaG
listaG = []
class Amostras:
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.root.title('Amostras')

        self.binario = dd()
        self.recurso = gr()

        self.msg1 = t.Label(self.root, text='Filtros', font=param.FONTE_OUTRA[0])
        self.msg1.place(x=30, y=0)
        self.msg2 = t.Label(self.root, text='Identificação', font=param.FONTE_OUTRA[3])
        self.msg2.place(x=12, y=50)
        self.Identificacao = t.Entry(self.root, width=65, bord=2)
        self.Identificacao.place(x=160, y=55, height=30)

        self.msg3 = t.Label(self.root, text='Projeto', font=param.FONTE_OUTRA[2])
        self.msg3.place(x=12, y=150)
        self.recurso.monstarListaProjetos(root=self.root, tela='Amostra')
        self.botao_pesquisar = t.Button(self.root, text=' Pesquisar ', font=param.FONTE_PADRAO).place(x=570, y=149)#sem ação

        self.botao_adicionar = t.Button(self.root, text='+ Incluir Novo', font=param.FONTE_OUTRA[1], command=lambda:self.mudarTela())
        self.botao_adicionar.place(x=580, y=265)

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

        self.visu()

        self.tree.place(x=15, y=300, height = 115, width=540)

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

        self.button2 = t.Button(self.root, text='Voltar', command=lambda:self.mudarTela(var=1))
        self.button2.place(x=570, y=450, width=100)

        self.root.mainloop()
            
    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge

    def visu(self, numero=None):#incompleto
        self.dados = shelve.open(BANCO_DADOS)
        self.lista = self.dados['Amostra']
        self.cont = 1
        for c in self.lista:
            self.list = [self.cont]
            self.list.append(c.nomeProjeto)
            self.list.append(c.identificacao)
            self.tree.insert("", 'end',values=self.list,  tag='1')
            self.cont += 1
        self.dados.close()
        '''
        self.dados1 = dd(NomeArquivo='Amostras_Projeto.dat')
        self.dados2 = dd()
        self.informacoes1 = self.dados1.lerBin()#dados dos projetos cadastrados
        self.informacoes2 = self.dados2.lerBin()#informações sobre as amostras
        self.lista = []
        try:
            self.cont = 1
            for c in self.informacoes1:
                self.lista = [self.cont, c[0], c[1]]#c[0] quivale ao nome do projeto no arquivo projeto.dat
                for x in self.informacoes2[:]:#irá pecorrer cada amostra cadastrada
                    #irá verificar se o nome do projeto cadastrado é igual
                    #x[0] é a posição que está localizado o nome do projeto no arquivo das amostras
                    if c[0] == x[0]:
                        for d in x[3]:#pecorre os memros cadastrado no projeto
                            if 'Sim' in d[:]:#verifica o membro que está cadastrado como coordenador
                                self.lista.append(d[1])#nome do membro coordenador
                                self.tree.insert("", 'end',values=self.lista, tag='1')
                                break
                        break
                self.cont += 1
        except:
            return None'''

    def mudarTela(self, var=None):
        if var == 1:
            self.root.destroy()
            from tela.TelaPrincipal import TelaPrincipal
            TelaPrincipal()
        else:
            self.root.destroy()
            CA()





