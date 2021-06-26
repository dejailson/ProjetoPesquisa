import tkinter as t
from tkinter import ttk
import cv2
from util.binario import Dados as dd
from PIL import ImageTk,Image
from tkinter import filedialog as fdg
from tela.Relatorio_do_Processamento import Relatorio as rel
from processamento.aquisicao_img import Aquisicao
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from util.modelo.amostras import Amostras
from config.Parametro import BANCO_DADOS
import shelve
global amostra
class CadastrarAmostra():
    def __init__(self, im=None, caminho=None):
        self.dados_membros = []
        self.root = t.Tk()
        self.root.geometry("1000x400")
        self.root.title('Cadastro da Amostra')
        self.imagem = dd()
        if im != None:
            self.procurarB(num=im, url=caminho)
        self.procurar = t.Button(self.root, text='Procurar', command=lambda:self.procurarB()).place(x=12, y=360, width=350)

        self.recurso = gr()


        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=380, y=40)
        
        self.recurso.monstarListaProjetos(root=self.root)

        self.msg3 = t.Label(self.root, text='Identificação', font='arial 12 bold')
        self.msg3.place(x=380, y=80)

        self.identificacao = t.Entry(self.root, width=62, bord=2)
        self.identificacao.place(x=550, y=80, height=20, relwidth=0.42, relheight=0.01)
        
        self.msg4 = t.Label(self.root, text='Número de Fêmeas Coletadas', font='arial 12 bold')
        self.msg4.place(x=380, y=120)

        self.NFemea = t.Entry(self.root, width=62, bord=2)
        self.NFemea.place(x=630, y=120, height=20, relwidth=0.32, relheight=0.01)

        self.msg5 = t.Label(self.root, text='Comprimento do Cefalotórax', font='arial 12 bold')
        self.msg5.place(x=380, y=160)

        self.cefalotorax = t.Entry(self.root, width=52, bord=2)
        self.cefalotorax.place(x=630, y=160, height=20)

        self.msg6 = t.Label(self.root, text='Comprimento do Abdome', font='arial 12 bold')
        self.msg6.place(x=380, y=200)

        self.abdomem = t.Entry(self.root, width=52, bord=2)
        self.abdomem.place(x=630, y=200, height=20)

        self.msg7 = t.Label(self.root, text='Comprimento do Telson', font='arial 12 bold')
        self.msg7.place(x=380, y=240)

        self.telson = t.Entry(self.root, width=52, bord=2)
        self.telson.place(x=630, y=240, height=20)


        self.Processar = t.Button(self.root, text=' Processar ', command=lambda:self.mudarTela())
        self.Processar.place(x=500, y=320, width=100, relwidth=0.01)
        self.Salvar = t.Button(self.root, text=' Salvar ', command=lambda:self.adicionar())
        self.Salvar.place(x=620, y=320, width=100, relwidth=0.01)
        self.Cancelar = t.Button(self.root, text=' Cancelar ', command=lambda:self.mudarTela(var=2))
        self.Cancelar.place(x=740, y=320, width=100, relwidth=0.01)
        self.VisuRelat = t.Button(self.root, text='Visualizar Relatório', command=None)#sem ação
        self.VisuRelat.place(x=860, y=320, width=100, relwidth=0.01)

        self.root.mainloop()

    def adicionar(self):
        self.amostra = Amostras(nomeProjeto=self.recurso.projeto.get().strip(), 
                                            identificacao=self.identificacao.get().strip(), 
                                            numFemeas=self.NFemea.get().strip(),
                                            CCT=self.cefalotorax.get().strip(),
                                            CA=self.abdomem.get().strip(),
                                            T=self.telson.get().strip())

        amostra = self.amostra
        try: 
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Amostra']
            self.lista.append(self.amostra)
            self.dados['Amostra'] = self.lista
            self.dados.close()
        except:
            print('Erro!')
        self.mudarTela(var=1)

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

    def mudarTela(self, var=None ):
        self.amostra = Amostras(nomeProjeto=self.recurso.projeto.get().strip(), 
                                            identificacao=self.identificacao.get().strip(), 
                                            numFemeas=self.NFemea.get().strip(),
                                            CCT=self.cefalotorax.get().strip(),
                                            CA=self.abdomem.get().strip(),
                                            T=self.telson.get().strip())
        from tela.Amostras import Amostras as tela_amostras
        if var == 1 and 2:
            self.root.destroy()
            tela_amostras()

        else:
            try:
                if self.caminho_img != None:
                    self.root.destroy()
                    rel(url=self.caminho_img, amostra=self.amostra)
                    
                else:
                    self.alerta = t.Label(self.root, text='Erro: Escolha uma imagem', font='Arial 15 bold')
                    self.alerta.place(x=580, y=280)
                        
            except AttributeError:
                self.alerta = t.Label(self.root, text='Erro: Escolha uma imagem', font='Arial 15 bold')
                self.alerta.place(x=580, y=280)




