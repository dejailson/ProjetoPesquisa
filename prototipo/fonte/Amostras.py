import tkinter as t
from tkinter import ttk
from binario import Dados as dd
from PIL import ImageTk,Image



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

        self.msg1 = t.Label(self.root, text='Filtros', font='arial 9 bold')
        self.msg1.place(x=30, y=0)

        self.msg2 = t.Label(self.root, text='Identificação', font='arial 16 bold')
        self.msg2.place(x=12, y=50)

        self.Identificacao = t.Entry(self.root, width=65, bord=2)
        self.Identificacao.place(x=160, y=55, height=30)

        self.msg3 = t.Label(self.root, text='Projeto', font='arial 14 bold')
        self.msg3.place(x=12, y=150)

        self.visu(numero=1)


        self.botao_pesquisar = t.Button(self.root, text=' Pesquisar ', font='arial 12 bold').place(x=570, y=149)#sem ação

        self.botao_adicionar = t.Button(self.root, text='+ Incluir Novo', font='arial 10 bold', command=lambda:self.mudarTela()).place(x=580, y=265)#sem ação

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

        self.binario = dd()

        self.caminho_lapis = self.binario.buscarCaminho('lapis.jpg')
        self.img_lapis = Image.open(self.caminho_lapis)
        self.resu = self.red(self.img_lapis)
        self.imagem_lapis = ImageTk.PhotoImage(self.resu)
        self.imagem_lapis_L = t.Button(image=self.imagem_lapis).place(x=570, y=315)

        self.caminho_olhos = self.binario.buscarCaminho('olho.jpg')
        self.img_olhos = Image.open(self.caminho_olhos)
        self.resu = self.red(self.img_olhos)
        self.imagem_olhos = ImageTk.PhotoImage(self.resu)
        self.imagem_olhos_L = t.Button(image=self.imagem_olhos).place(x=610, y=315)

        self.caminho_lixeira = self.binario.buscarCaminho('lexeira.png')
        self.img_lixeira = Image.open(self.caminho_lixeira)
        self.resu = self.red(self.img_lixeira)
        self.imagem_lixeira = ImageTk.PhotoImage(self.resu)
        self.imagem_lixeira_L = t.Button(image=self.imagem_lixeira).place(x=650, y=315)

        self.button2 = t.Button(self.root, text='Voltar', command=lambda:self.mudarTela(var=1)).place(x=570, y=450, width=100)

        self.root.mainloop()
            
    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge

    def visu(self, numero=None):
        self.dados1 = dd(NomeArquivo='Amostras_Projeto.dat')
        self.dados2 = dd()
        self.informacoes1 = self.dados1.lerBin()
        self.informacoes2 = self.dados2.lerBin()
        self.lista = []
        if not numero == None:
            if not self.informacoes1 == None:
                for c in self.informacoes1[:]:
                    self.lista.append(c[0])
            else:
                self.lista.append('Sem Projetos Cadastrado')

            self.projeto = ttk.Combobox(self.root, values=self.lista, width=62)
            self.projeto.place(x=160, y=150, height=30)
            self.projeto.current(0)     
        else:
            self.cont = 1
            for c in self.informacoes1:
                self.lista = [self.cont, c[0], c[1]]
                for x in self.informacoes2:
                    if c[0] == x[:][0]:
                        for d in x[3]:
                            if 'Sim' in d[:]:
                                self.lista.append(d[1])
                                self.tree.insert("", 'end',values=self.lista, tag='1')
                                break
                        break
                self.cont += 1

    def mudarTela(self, var=None):
        if var == 1:
            self.root.destroy()
            from main import Main
            Main()
        else:
            self.root.destroy()
            from cadastrarAmostra import CadastrarAmostra as CA
            CA()





