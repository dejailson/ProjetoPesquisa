import tkinter as t
from tkinter import messagebox
from util.GerenciadorRecurso import GerenciadorRecurso as gr

class ObjetoPadrao:
    def __init__(self):
        self.recurso = gr()
        self.dimensaoObj = self.recurso.getObjetoPadrao()
        if self.dimensaoObj == []:
            self.dimensaoObj = ['', '']
        self.tela = t.Tk()
        self.tela.resizable(0, 0)
        try:
            self.tela.iconbitmap(self.recurso.carregarIconeJanela())
        except:
            pass
        self.tela.geometry("400x300")
        self.tela.title('Dimensões do Objeto')

        self.msgInicial = t.Label(self.tela, text='Dimensão do objeto padrão', 
                                    font='arial 14 bold').pack()

        
        self.separador = t.Label(self.tela, text='', font='arial 11 bold').pack()
        self.labelLargura = t.Label(self.tela, text='Largura do Objeto (mm)', font='arial 11 bold').pack()
        self.largura = t.Entry(self.tela, width=30, bord=2)
        self.largura.insert(0, string=self.dimensaoObj[0])
        self.largura.pack()

        self.separador = t.Label(self.tela, text='', font='arial 11 bold').pack()

        self.labelAltura = t.Label(self.tela, text='Altura do Objeto (mm)', font='arial 11 bold').pack()
        self.altura = t.Entry(self.tela, width=30, bord=2)
        self.altura.insert(0, string=self.dimensaoObj[1])
        self.altura.pack()

        self.butao1 = t.Button(self.tela, text="Salvar", font='arial 12 bold',
                            command=lambda: self.adicionarObjeto()).pack()
        self.separador = t.Label(self.tela, text='', font='arial 9 bold').pack()

        self.butao2 = t.Button(self.tela, text="Cancelar", font='arial 12 bold', 
                            command=lambda: self.tela.destroy()).pack()

        self.tela.mainloop()

    def adicionarObjeto(self):
        try:
            self.recurso.setObjetoPadrao(float(self.largura.get().strip()),
                                        float(self.altura.get().strip()))
        except ValueError:
            messagebox.showwarning('Atenção!', 'Campo só permite números - exemplo: 13.7')

        self.tela.destroy()