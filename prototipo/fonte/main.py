from Projeto import Projeto
from Amostras import Amostras
import tkinter as t
from PIL import ImageTk,Image

class Main:
    def __init__(self):
        self.root = t.Tk()
        self.root.geometry('700x500')
        self.root.title('Tela Inícial')
        self.menu = t.Menu(self.root, tearoff=0)
        self.Menu = t.Menu(self.menu, tearoff=0)
        self.menu.add_command(label='Tela de Projeto', command=lambda:self.Pro())
        self.menu.add_command(label='Tela de Amostras', command=lambda:self.Amo())
        self.menu.add_separator()
        self.menu.add_command(label='Fechar', command=lambda:self.root.quit())
        self.Menu.add_cascade(label='Informações', menu=self.menu)
        self.root.config(menu=self.Menu)
        self.titulo = t.Label(self.root, text='Software De Visão Computacional', font='Arial 20 bold').pack()
        self.nada = t.Label(self.root, text='   ', font='arial 20').pack()
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_pesquisa01\\files\\Prototipos_Projeto\\ovos.jpg"))
        self.ima_l = t.Label(imag=self.img, width=700, height=400).pack()
        
        self.root.mainloop()

    def Pro(self):
        self.root.destroy()
        Projeto()
    def Amo(self):
        self.root.destroy()
        Amostras()


Main()