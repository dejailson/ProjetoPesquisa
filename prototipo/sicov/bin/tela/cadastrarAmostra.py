import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd
from PIL import ImageTk,Image
from tkinter import filedialog as fdg
from tela.Relatorio_do_Processamento import Relatorio as rel
from processamento.aquisicao_img import Aquisicao
from util.GerenciadorRecurso import GerenciadorRecurso as gr

class CadastrarAmostra():
    def __init__(self, im=None, caminho=None):
        self.root = t.Tk()
        self.root.geometry("1000x400")
        self.root.title('Cadastro da Amostra')
        self.imagem = dd()
        if im != None:
            self.procurarB(num=im, url=caminho)
        self.procurar = t.Button(self.root, text='Procurar', command=lambda:self.procurarB()).place(x=12, y=360, width=350)

        self.recurso = gr()


        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=400, y=40)
        
        self.recurso.monstarListaProjetos(root=self.root)

        self.msg3 = t.Label(self.root, text='Identificação', font='arial 12 bold')
        self.msg3.place(x=400, y=80)

        self.identificacao = t.Entry(self.root, width=62, bord=2)
        self.identificacao.place(x=550, y=80, height=20, relwidth=0.42, relheight=0.01)
        
        self.msg4 = t.Label(self.root, text='Número de Fêmeas Coletadas', font='arial 12 bold')
        self.msg4.place(x=400, y=120)

        self.NFemea = t.Entry(self.root, width=62, bord=2)
        self.NFemea.place(x=650, y=120, height=20, relwidth=0.32, relheight=0.01)
        
        self.Processar = t.Button(self.root, text=' Processar ').place(x=500, y=200, width=100, relwidth=0.01)#sem ação

        self.Salvar = t.Button(self.root, text=' Salvar ', command=lambda:self.adicionar()).place(x=620, y=200, width=100, relwidth=0.01)#sem ação

        self.Cancelar = t.Button(self.root, text=' Cancelar ', command=lambda:self.mudarTela(var=2)).place(x=740, y=200, width=100, relwidth=0.01)#sem ação

        self.VisuRelat = t.Button(self.root, text='Visualizar Relatório', command=lambda:self.mudarTela()).place(x=860, y=200, width=100, relwidth=0.01)#sem ação

        self.root.mainloop()

    def adicionar(self):
        self.dados = dd(NomeArquivo='Amostras_Projeto.dat')
        self.projeto = self.recurso.projeto.get()
        self.lista = [self.projeto.strip(), 
            self.identificacao.get().strip(), 
            self.NFemea.get().strip()]
        try:
            self.dados.gravarBin(self.lista)
        except:
            self.dados.salvarBin(self.lista)
        self.root.destroy()
        from tela.Amostras import Amostras
        Amostras()

    def procurarB(self, num=None, url=None):
        self.caminho_img = url
        if num == None:
            try:
                self.caminho_img = fdg.askopenfilename(title='Procurar Imgem', filetypes=(('Arquivos png', '*.png'), ('Arquivos jpg', '*.jpg'), ('Todos os Arquivos', '*.*')))
                self.aquisicao = Aquisicao(url=self.caminho_img, validador=1)
            except AttributeError:
                self.caminho_img = None
        else:
            self.aquisicao = Aquisicao(url=self.caminho_img)

    def mudarTela(self, var=None):
        from tela.Amostras import Amostras
        if var == 1:
            self.root.destroy()
            Amostras()
        elif var == 2:
            self.root.destroy()
            Amostras()

        else:
            try:
                if self.caminho_img != None:
                    self.root.destroy()
                    rel(url=self.caminho_img)
                else:
                    self.alerta = t.Label(self.root, text='Erro: Escolha uma imagem', font='Arial 15 bold')
                    self.alerta.place(x=580, y=280)
                        
            except AttributeError:
                self.alerta = t.Label(self.root, text='Erro: Escolha uma imagem', font='Arial 15 bold')
                self.alerta.place(x=580, y=280)




