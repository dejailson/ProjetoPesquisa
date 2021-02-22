import tkinter as t
from tkinter import ttk
from util.binario import Dados as dd

class Relatorio():
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("1000x450")
        self.root.title('Relatório do Processamento')
        self.imagem = dd()
        self.image = t.PhotoImage(file="C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_de_pesquisa\\files\\teste_tkinter\\img\\favicon.png")
        self.image=self.image.subsample(1,1)
        self.labelimg = t.Label(image=self.image)
        self.labelimg.place(x=12, y=0)

        self.legenda = t.Label(self.root, text='Legenda', font='Arial 12 bold').place(x=12, y=360)

        self.estagios()


        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=400, y=40)

        self.lista = [
                        "Projeto 1", 
                        "Projeto 2",
                        "Projeto 3",
                        "Projeto 4"]#Lsta será salva em um arquivo binário
        self.projeto = ttk.Combobox(self.root, values=self.lista, width=62)
        self.projeto.place(x=550, y=40, height=20, relwidth=0.42, relheight=0.01)
        self.projeto.current(0)


        self.msg3 = t.Label(self.root, text='Identificação', font='arial 12 bold')
        self.msg3.place(x=400, y=80)

        self.identificacao = t.Entry(self.root, width=62, bord=2)
        self.identificacao.place(x=550, y=80, height=20, relwidth=0.42, relheight=0.01)
        
        self.msg4 = t.Label(self.root, text='Número de Fêmeas Coletadas', font='arial 12 bold')
        self.msg4.place(x=400, y=120)

        self.NFemea = t.Entry(self.root, width=62, bord=2)
        self.NFemea.place(x=650, y=120, height=20, relwidth=0.32, relheight=0.01)

        self.msg5 = t.Label(self.root, text='Número de Ovos', font='arial 12 bold')
        self.msg5.place(x=400, y=160)

        self.NOvos = t.Entry(self.root, width=62, bord=2)
        self.NOvos.place(x=650, y=160, height=20, relwidth=0.32, relheight=0.01)

        self.msg6 = t.Label(self.root, text='Média do Volume dos Ovos', font='arial 12 bold')
        self.msg6.place(x=400, y=200)

        self.MVolumeOvos = t.Entry(self.root, width=62, bord=2)
        self.MVolumeOvos.place(x=650, y=200, height=20, relwidth=0.32, relheight=0.01)

        self.msg7 = t.Label(self.root, text='Média de Fecundidade', font='arial 12 bold')
        self.msg7.place(x=400, y=240)

        self.MFecundidade = t.Entry(self.root, width=62, bord=2)
        self.MFecundidade.place(x=650, y=240, height=20, relwidth=0.32, relheight=0.01)

        self.msg8 = t.Label(self.root, text='Volume da Massa dos Ovos', font='arial 12 bold')
        self.msg8.place(x=400, y=280)

        self.VMassaOvos = t.Entry(self.root, width=62, bord=2)
        self.VMassaOvos.place(x=650, y=280, height=20, relwidth=0.32, relheight=0.01)
        
        

        self.sair = t.Button(self.root, text='Sair', command=lambda:self.voltar()).place(x=860, y=400, width=100, relwidth=0.01)#sem ação

        self.root.mainloop()

    def voltar(self):
        self.root.destroy()
        from transicao import Transicao as T
        T(n=4)

    def estagios(self):
        #Definir função para o processamento de imagem
        self.part1 = t.Label(self.root, text='I - Fase Inicial', font='Arial 9 bold').place(x=12, y=390)
        self.part2 = t.Label(self.root, text='II - Fase Inicial', font='Arial 9 bold').place(x=12, y=410)
        self.part3 = t.Label(self.root, text='III - Fase Inicial', font='Arial 9 bold').place(x=12, y=430)

        self.vermelho = t.Label(self.root, text='Região em Vermelho - Óvulo', font='Arial 9 bold').place(x=150, y=390)
        self.azul = t.Label(self.root, text='Região em Azul - Mancha Ocular', font='Arial 9 bold').place(x=150, y=410)


