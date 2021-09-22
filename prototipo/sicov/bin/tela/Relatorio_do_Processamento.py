import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd
from PIL import Image, ImageTk
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from processamento.ProcessamentoDeImagem import ProcessamentoDeImagem as ProDI
from processamento.aquisicao_img import Aquisicao
from util.modelo.amostras import Amostras
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from util.modelo.camarao import Camarao
import numpy as np
import cv2
class Relatorio():
    def __init__(self, url, amostra, ver=None):
        self.Processamento = ProDI()
        self.ver = ver
        self.url = url
        
        self.root = t.Tk()
        self.root.resizable(0, 0)
        self.root.geometry("1000x450")
        self.root.title('Relatório do Processamento')
        self.recurso = gr()
        self.recurso = gr()
        try:
            self.root.iconbitmap(self.recurso.carregarIconeJanela())
        except:
            pass
        imagem = cv2.imread(url)
        
        imagem, self.listaOvos = self.Processamento.ExtrairCaracteristicas(imagem)

        self.camarao = Camarao(amostra.CCT, amostra.CA, amostra.T, self.listaOvos)
        self.mediaMassaOvos, self.volumeMassaOvos = self.camarao.volumeDaMassaDosOvos()
        self.mediaMassaOvos = str(self.mediaMassaOvos).split('.')
        self.mediaMassaOvos = self.mediaMassaOvos[0] + '.' + self.mediaMassaOvos[1][:2]


        self.volumeMassaOvos = str(self.volumeMassaOvos).split('.')
        self.volumeMassaOvos = self.volumeMassaOvos[0] + '.' + self.volumeMassaOvos[1][:2]
        self.amostra = amostra
        imagem = Aquisicao(imagem, 2)
        #imagem = ImageTk.PhotoImage(imagem)
        #self.imge_label = t.Label(image=imagem, height="350", width="350").place(x=12, y=0)
        

        self.legenda = t.Label(self.root, text='Legenda', font='Arial 12 bold').place(x=12, y=360)


        self.legenda = t.Label(self.root, text='Legenda',
                               font='Arial 12 bold').place(x=12, y=360)

        self.estagios()
        self.font = 'arial 12 bold'
        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=400, y=40)

        self.recurso.monstarListaProjetos(root=self.root)

        self.msg3 = t.Label(self.root, text='Identificação',
                            font='arial 12 bold')
        self.msg3.place(x=400, y=80)

        self.identificacao = t.Label(self.root, text=amostra.identificacao, font=self.font, bg='white', relief="solid")
        self.identificacao.place(
            x=550, y=80, height=20, relwidth=0.42, relheight=0.01)

        self.msg4 = t.Label(
            self.root, text='Número de Fêmeas Coletadas', font='arial 12 bold')
        self.msg4.place(x=400, y=120)

        self.NFemea = t.Label(self.root, text=self.amostra.numFemeas, font=self.font, bg='white', relief="solid")
        self.NFemea.place(x=650, y=120, height=20,
                          relwidth=0.32, relheight=0.01)

        self.msg5 = t.Label(
            self.root, text='Número de Ovos', font='arial 12 bold')
        self.msg5.place(x=400, y=160)

        self.NOvos = t.Label(self.root, text=len(self.listaOvos), font=self.font, bg='white', relief="solid")
        self.NOvos.place(x=650, y=160, height=20,
                         relwidth=0.32, relheight=0.01)

        self.msg6 = t.Label(
            self.root, text='Média do Volume dos Ovos', font='arial 12 bold')
        self.msg6.place(x=400, y=200)

        self.MVolumeOvos = t.Label(self.root, text=self.mediaMassaOvos + 'mm³', font=self.font, bg='white', relief="solid")
        self.MVolumeOvos.place(x=650, y=200, height=20,
                               relwidth=0.32, relheight=0.01)

        self.msg7 = t.Label(
            self.root, text='Média de Fecundidade', font='arial 12 bold')
        self.msg7.place(x=400, y=240)
        self.MediaFecundidade = str(self.camarao.MediaFecundidade).split('.')
        self.MediaFecundidade = self.MediaFecundidade[0] + '.' + self.MediaFecundidade[1][:2]
        self.MFecundidade = t.Label(self.root, text=self.MediaFecundidade + 'ovos/tamanho da fêmia', font=self.font, bg='white', relief="solid")
        self.MFecundidade.place(x=650, y=240, height=20,
                                relwidth=0.32, relheight=0.01)

        self.msg8 = t.Label(
            self.root, text='Volume da Massa dos Ovos', font='arial 12 bold')
        self.msg8.place(x=400, y=280)

        self.VMassaOvos = t.Label(self.root, text=self.volumeMassaOvos + 'mm³', font=self.font, bg='white', relief="solid")
        self.VMassaOvos.place(x=650, y=280, height=20,
                              relwidth=0.32, relheight=0.01)

        self.sair = t.Button(self.root, text='Sair', command=lambda: self.voltar()).place(
            x=860, y=400, width=100, relwidth=0.01)  # sem ação

        self.root.mainloop()

    def voltar(self):
        self.root.destroy()
        if self.ver == None:
            from tela.cadastrarAmostra import CadastrarAmostra as CA 
            CA(im=self.url, caminho=self.url, amostra=self.amostra)
        else:
            from tela.Amostras import Amostras as tela_amostras
            tela_amostras()



    def estagios(self):
        # Definir função para o processamento de imagem
        self.part1 = t.Label(self.root, text='Circulo Externo - Circurferencia do Ovo',
                             font='Arial 9 bold').place(x=12, y=390)
        self.part2 = t.Label(self.root, text='Circulo Interno - Centroide',
                             font='Arial 9 bold').place(x=12, y=410)
        





