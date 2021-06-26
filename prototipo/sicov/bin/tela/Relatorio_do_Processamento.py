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
import cv2
class Relatorio():
    def __init__(self, url, amostra):
        self.Processamento = ProDI()
        self.url = url
        imagem = cv2.imread(url)
        
        self.listaOvos = self.Processamento.ExtrairCaracteristicas(imagem=imagem)
        self.camarao = Camarao(amostra.CCT, amostra.CA, amostra.T, self.listaOvos)
        self.mediaMassaOvos, self.volumeMassaOvos = self.camarao.volumeDaMassaDosOvos()
        self.amostra = amostra
        self.root = t.Tk()
        self.root.geometry("1000x450")
        self.root.title('Relatório do Processamento')
        self.recurso = gr()
        self.aquisicao = Aquisicao(url=self.url)
        

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

        self.MVolumeOvos = t.Label(self.root, text=self.mediaMassaOvos, font=self.font, bg='white', relief="solid")
        self.MVolumeOvos.place(x=650, y=200, height=20,
                               relwidth=0.32, relheight=0.01)

        self.msg7 = t.Label(
            self.root, text='Média de Fecundidade', font='arial 12 bold')
        self.msg7.place(x=400, y=240)

        self.MFecundidade = t.Label(self.root, text=str(self.camarao.MediaFecundidade)+'cm', font=self.font, bg='white', relief="solid")
        self.MFecundidade.place(x=650, y=240, height=20,
                                relwidth=0.32, relheight=0.01)

        self.msg8 = t.Label(
            self.root, text='Volume da Massa dos Ovos', font='arial 12 bold')
        self.msg8.place(x=400, y=280)

        self.VMassaOvos = t.Label(self.root, text=self.volumeMassaOvos, font=self.font, bg='white', relief="solid")
        self.VMassaOvos.place(x=650, y=280, height=20,
                              relwidth=0.32, relheight=0.01)

        self.sair = t.Button(self.root, text='Sair', command=lambda: self.voltar()).place(
            x=860, y=400, width=100, relwidth=0.01)  # sem ação

        self.root.mainloop()

    def voltar(self):
        self.root.destroy()
        from tela.cadastrarAmostra import CadastrarAmostra as CA 
        CA(im=self.url, caminho=self.url)



    def estagios(self):
        # Definir função para o processamento de imagem
        self.part1 = t.Label(self.root, text='I - Fase Inicial',
                             font='Arial 9 bold').place(x=12, y=390)
        self.part2 = t.Label(self.root, text='II - Fase Inicial',
                             font='Arial 9 bold').place(x=12, y=410)
        self.part3 = t.Label(self.root, text='III - Fase Inicial',
                             font='Arial 9 bold').place(x=12, y=430)

        self.vermelho = t.Label(
            self.root, text='Região em Vermelho - Óvulo', font='Arial 9 bold').place(x=150, y=390)
        self.azul = t.Label(self.root, text='Região em Azul - Mancha Ocular',
                            font='Arial 9 bold').place(x=150, y=410)





