import tkinter as t
from tkinter import ttk
from binario import Dados as dd

class CadastrarAmostra():
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("1000x400")
        self.root.title('Cadastro da Amostra')
        self.imagem = dd()
        '''self.imagem.nomePasta = 'Prototipos_Projeto'
        self.imagem.NomeArquivo = 'ovos.jpg'
        self.caminho = self.imagem.monstar_Cam()#A imagem deve ser aberta com a biblioteca OpenCV'''
        self.image = t.PhotoImage(file="C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_de_pesquisa\\files\\teste_tkinter\\img\\favicon.png")
        self.image=self.image.subsample(1,1)
        self.labelimg = t.Label(image=self.image)
        self.labelimg.place(x=12, y=0)

        self.procurar = t.Button(self.root, text='Procurar').place(x=12, y=360, width=350)#sem ação


        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=400, y=40)

        self.lista = [
                        "Projeto 1", 
                        "Projeto 2",
                        "Projeto 3",
                        "Projeto 4"]
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
        
        self.Processar = t.Button(self.root, text=' Processar ').place(x=500, y=200, width=100, relwidth=0.01)#sem ação

        self.Salvar = t.Button(self.root, text=' Salvar ').place(x=620, y=200, width=100, relwidth=0.01)#sem ação

        self.Cancelar = t.Button(self.root, text=' Cancelar ').place(x=740, y=200, width=100, relwidth=0.01)#sem ação

        self.VisuRelat = t.Button(self.root, text='Visualizar Relatório').place(x=860, y=200, width=100, relwidth=0.01)#sem ação

        self.root.mainloop()



