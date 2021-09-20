import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd
from PIL import ImageTk,Image
from util.Search import Search
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from tela.cadastrarAmostra import CadastrarAmostra as CA
from util.modelo.amostras import Amostras
from config.Parametro import BANCO_DADOS, SUBPASTA_IMGS_AMOSTRAS
import config.Parametro as param
from tkinter import messagebox
import shelve

global listaG
listaG = []
class Amostras:
    def __init__(self):
        self.listaAmostras = []
        self.root = t.Tk()
        self.binario = dd()
        self.recurso = gr()
        self.root.iconbitmap(self.recurso.carregarIconeJanela())
        self.root.resizable(0, 0) 
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.root.title('Amostras')

        
        self.msg1 = t.Label(self.root, text='Filtros', font=param.FONTE_OUTRA[0])
        self.msg1.place(x=30, y=0)
        self.msg2 = t.Label(self.root, text='Identificação', font=param.FONTE_OUTRA[3])
        self.msg2.place(x=12, y=50)
        self.Identificacao = t.Entry(self.root, width=65, bord=2)
        self.Identificacao.place(x=160, y=55, height=30)

        self.msg3 = t.Label(self.root, text='Projeto', font=param.FONTE_OUTRA[2])
        self.msg3.place(x=12, y=150)
        self.recurso.monstarListaProjetos(root=self.root, tela='Amostra')
        self.botao_pesquisar = t.Button(self.root, text=' Pesquisar ', font=param.FONTE_PADRAO, comman= lambda: self.search()).place(x=570, y=149)#sem ação

        self.botao_adicionar = t.Button(self.root, text='+ Incluir Novo', font=param.FONTE_OUTRA[1], command=lambda:self.mudarTela())
        self.botao_adicionar.place(x=580, y=265)

        self.tree = ttk.Treeview(self.root, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4"), show="headings")
        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text=' ')
        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Projeto')
        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Identificação')
        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

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
        self.imagem_olhos_L = t.Button(image=self.imagem_olhos, command=lambda: self.viewAmostra()).place(x=610, y=315)

        self.caminho_lixeira = self.recurso.carregarIconeLixeira()
        self.img_lixeira = Image.open(self.caminho_lixeira)
        self.resu = self.red(self.img_lixeira)
        self.imagem_lixeira = ImageTk.PhotoImage(self.resu)
        self.imagem_lixeira_L = t.Button(image=self.imagem_lixeira, command=lambda: self.remover()).place(x=650, y=315)

        self.button2 = t.Button(self.root, text='Voltar', command=lambda:self.mudarTela(var=1))
        self.button2.place(x=570, y=450, width=100)

        self.visualizarAmo = t.Button(self.root, text='Visualizar Todas as Amostras', 
                                font='arial 10 bold', 
                                command=lambda:self.visu())
        self.visualizarAmo.place(x=20, y=450)

        self.root.mainloop()
    
    def search(self):
        self.lista = [self.Identificacao.get().strip(), self.recurso.projeto.get().strip()]
        self.visu(lista=Search(amostra=self.lista))

            
    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge

    def viewAmostra(self):
        if self.tree.selection() == ():
            messagebox.showerror("Erro","Selecione uma Amostra!")
        else:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            posicao = self.tree.selection()[0]
            posicao = self.tree.get_children().index(posicao)
            amostraR = self.listaAmostras[posicao][1]
            projetoR = self.listaAmostras[posicao][0]
            print(projetoR.nome)
            try:
                self.cam = self.recurso.montarCaminhoRecurso(SUBPASTA_IMGS_AMOSTRAS+'\\'+ amostraR.identificacao +'_'+ projetoR.nome +'.png')
                from tela.Relatorio_do_Processamento import Relatorio as rel
                self.root.destroy()
                rel(url=self.cam, amostra=amostraR, ver=None)
            except FileNotFoundError:
                messagebox.showerror("Erro!","A imagem da Amostra não se encontra mais salva no sistema de arquivo.")
            self.dados.close()

    def remover(self):
        if self.tree.selection() == ():
            messagebox.showwarning("Atenção!","Selecione uma Amostra!")
        else:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            posicao = self.tree.selection()[0]
            posicao = self.tree.get_children().index(posicao)
            amostraR = self.listaAmostras[posicao][1]
            projetoR = self.listaAmostras[posicao][0]
            projetoR = Search(projeto=[projetoR.nome, '', ''])[0]
            try:
                self.cam = self.recurso.montarCaminhoRecurso(SUBPASTA_IMGS_AMOSTRAS+'\\'+ amostraR.identificacao +'_'+ projetoR.nome  +'.png')
            except FileNotFoundError:
                pass
            for amostra in projetoR.amostras:
                print(f'1 - {amostra.identificacao}')
                if amostra.identificacao == amostraR.identificacao:
                    projetoR.amostras.remove(amostra)
            cont = 0
            for projeto in self.lista:
                if projeto.nome == projetoR.nome:
                    self.lista[cont] = projetoR
                cont += 1
            posicao = self.tree.selection()[0]
            self.tree.delete(posicao)
            self.dados['Projeto'] = self.lista
            self.dados.close()
            

    def visu(self, lista=None):
        listaAmostras = []
        posicao = self.tree.get_children()
        for c in range(len(posicao)):
            self.tree.delete(posicao[c])
        self.dados = shelve.open(BANCO_DADOS)
        if lista == None:
            self.lista = self.dados['Projeto']
        else:
            self.lista = lista
        for projeto in self.lista:
            self.cont = 1
            if len(projeto.amostras) > 0:
                for amostra in projeto.amostras:
                    self.list = [self.cont, projeto.nome, amostra.identificacao, projeto.coordenador.nome]
                    self.tree.insert("", 'end',values=self.list,  tag='1')
                    self.cont += 1
                    self.listaAmostras.append([projeto, amostra])
        self.dados.close()


    def mudarTela(self, var=None):
        if var == 1:
            self.root.destroy()
            from tela.TelaPrincipal import TelaPrincipal
            TelaPrincipal()
        else:
            #messagebox.showerror
            self.root.destroy()
            CA()





