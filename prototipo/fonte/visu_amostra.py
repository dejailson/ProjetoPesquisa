import tkinter as t
from tkinter import ttk
from binario import Dados as dd
from PIL import ImageTk,Image
from tkinter import filedialog as fdg
from Relatorio_do_Processamento import Relatorio as rel

class CadastrarAmostra():
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry("1000x400")
        self.root.title('Cadastro da Amostra')
        self.imagem = dd()
        

        self.procurar = t.Button(self.root, text='Procurar', command=lambda:self.procurarB()).place(x=12, y=360, width=350)#sem ação


        self.msg1 = t.Label(self.root, text='Projeto ', font='arial 12 bold')
        self.msg1.place(x=400, y=40)

        self.lista = [
                        "Projeto 1", 
                        "Projeto 2",
                        "Projeto 3",
                        "Projeto 4"]
        self.projeto = t.Label(self.root, width=62, bg='white', relief="groove")
        self.projeto.place(x=550, y=40, height=20, relwidth=0.42, relheight=0.01)
        

        self.msg3 = t.Label(self.root, text='Identificação', font='arial 12 bold')
        self.msg3.place(x=400, y=80)

        self.identificacao = t.Label(self.root, width=62, bg='white', relief="groove")
        self.identificacao.place(x=550, y=80, height=20, relwidth=0.42, relheight=0.01)
        
        self.msg4 = t.Label(self.root, text='Número de Fêmeas Coletadas', font='arial 12 bold')
        self.msg4.place(x=400, y=120)

        self.NFemea = t.Label(self.root, width=62, bg='white', relief="groove")
        self.NFemea.place(x=650, y=120, height=20, relwidth=0.32, relheight=0.01)
        
        self.Processar = t.Button(self.root, text=' Processar ').place(x=500, y=200, width=100, relwidth=0.01)#sem ação

        self.nada = t.Button(self.root, text=' Nada ', command=lambda:self.adicionar()).place(x=620, y=200, width=100, relwidth=0.01)#sem ação

        self.voltar = t.Button(self.root, text=' Cancelar ', command=lambda:self.cancelar()).place(x=740, y=200, width=100, relwidth=0.01)#sem ação

        self.VisuRelat = t.Button(self.root, text='Visualizar Relatório', command=lambda:self.mudarTela()).place(x=860, y=200, width=100, relwidth=0.01)#sem ação

        self.root.mainloop()
    
    def cancelar(self):
        self.root.destroy()
        from transicao import Transicao as T
        T(n=3)

    def adicionar(self):
        self.dados = dd(NomeArquivo='Amostras_Projeto.dat')
        self.contador = self.dados.lerBin()
        self.lista = [self.projeto.get().rstrip().lstrip(), self.identificacao.get().rstrip().lstrip(), self.NFemea.get().rstrip().lstrip()]
        try:
            self.dados.gravarBin(self.lista)
            
        except:
            self.dados.salvarBin(self.lista)
        imagem.save('./img.png')
        self.root.destroy()
        from transicao import Transicao as T
        T(n=3)

    def procurarB(self):
        global imagem
        self.caminho_img = fdg.askopenfilename(title='Procurar Imgem', filetypes=(('Arquivos png', '*.png'), ('Arquivos jpg', '*.jpg'), ('Todos os Arquivos', '*.*')))
        self.imge = Image.open(self.caminho_img)
        self.basewidth = 400
        self.wpercent = (self.basewidth/float(self.imge.size[0]))
        self.hsize = int((float(self.imge.size[1])*float(self.wpercent)))
        self.imge = self.imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        imagem = self.imge
        self.imge = ImageTk.PhotoImage(self.imge)
        self.imge_label = t.Label(image=self.imge, height="350", width="350").place(x=12, y=0)

    def mudarTela(self):
        self.root.destroy()
        rel()
CadastrarAmostra()



